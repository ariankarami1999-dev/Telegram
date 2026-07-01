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
<img src="https://cdn4.telesco.pe/file/ugdklN52CwXJRtIv2FAqLqGzUQeWupP9Gd65ewfnHndEa7MQhBaeN1FZhXrzovDt9bJqna_NgAYpcH7xBI59C6ltK8Fr1TkB1XiRIIttjZeArLT7e7uSatxAuwdZ6sJIL006ga1sfuRX6Rg2ruE1pLc_H_0npUL1GiYE6PN56MTwdwNtNc75R68U9m-7E0c7uVtFQXo2bJLMLFIluRfNMdeRd_tuBOpxfhYIaf7_47J5Sv7qBSruorXharmu2SBxVshEOB94DiYhu300PrITVTgHL0aKbQ6i9_MArQbd_3IhB7xWvLoH6BCKs9-OVrLs0YF_-N_L7foGW8SM99Yw0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 186K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 15:22:34</div>
<hr>

<div class="tg-post" id="msg-79163">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بازی رفت بارسا و رعال تو لالیگا افتاده ۳ آبان تو نیوکمپ.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/funhiphop/79163" target="_blank">📅 14:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79162">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ترامپ درحال بررسی بازگشت به جنگ تمام عیار با ایرانه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/funhiphop/79162" target="_blank">📅 13:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79161">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تو زندگیم اشتباه زیاد داشتم،
(یکیش ادمینی همین چنله)
ولی هیچوقت عشق ابدی ندیدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/funhiphop/79161" target="_blank">📅 12:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79160">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6094ff0128.mp4?token=EvdMHXp_7sPHTjMoF1dnFo1S_hQ6VORRfWWvW-NoMeZocff-lnG5NVLuqeOquYQ1ryxRxDrQ6KuHT8QWPyWWEjSmt39FiGdIKkofTTqhqFIUZzoa4LEAZyfI8Zny4jKQDFxAazbZurpaNUSIb5VYy_RwMLxpp8jiVYodNjwxReXUtBHqNfvMiTpkt5mddAEuJCBkelXCxs9TsFPI_Dgkf5uTrBzXZfTS1o-4Bv5GJjqCTGPbV3v6DBdXIHrwnGb2LxdactMHgLMl3aS25GUO7KWIrxiHVkUqbT7DEW-Njnjh6OD1q_ykceGXxDLxHk2u2gI9YiyysM5TCgluY-1dKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6094ff0128.mp4?token=EvdMHXp_7sPHTjMoF1dnFo1S_hQ6VORRfWWvW-NoMeZocff-lnG5NVLuqeOquYQ1ryxRxDrQ6KuHT8QWPyWWEjSmt39FiGdIKkofTTqhqFIUZzoa4LEAZyfI8Zny4jKQDFxAazbZurpaNUSIb5VYy_RwMLxpp8jiVYodNjwxReXUtBHqNfvMiTpkt5mddAEuJCBkelXCxs9TsFPI_Dgkf5uTrBzXZfTS1o-4Bv5GJjqCTGPbV3v6DBdXIHrwnGb2LxdactMHgLMl3aS25GUO7KWIrxiHVkUqbT7DEW-Njnjh6OD1q_ykceGXxDLxHk2u2gI9YiyysM5TCgluY-1dKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرم معکوس با فان هیپ هاپ
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/funhiphop/79160" target="_blank">📅 11:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79159">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCerBv7S3WMGIdyhEcdg7pbXkVTX_zNEqGyqeGmUeKCRUzqBpCASsDp93Rr4bAxG_hEyH9BOqKzoh97EPs0vDHpCKNGZXPLjX7nipgQGN05vbO7CrI6y1k4EJI9svD2jRaVQ8DW0NQ6_KrRfpBAXYVvtR4GtuytdJa9vCqk28sDjAeY3dBjJHkNb9JlJHRVawYk2HU1BOdOGQhgjjOZQkZk522jPYrm8L5Y1CeF-zMUQsvlF20ga0ywWOgOwkmpL_jEe4rYOT7ZlRSiAeSdkh5sCZOi9cG60LkIIGmHcxrZB6qrVow16lf2QXlf_kdLgUoznIpL8HlcSa4atufmeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت صندلی قدرت تو ایران
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/funhiphop/79159" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79158">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scV0cKW9UitdyuVvjUgqx1hnLqQnRKZe3BRH57ZMjUyxJFgK1KnVjG-kPDeTF8-qmA8gho9lbtpTpr7G8wYHqPuVR5ydf5_ykdLpacyhvGsDA1SY3BkK3MQWWZ3caO61Zfpnjz9GDc43BHi3Ms2kOJQxR3WJy9Qf71iCRSKMxeW6kyP8Gt8LS9tFw2rqic7DJsoQD-zLt_aHo4qudfre1lhxTYwlUIhsxLpZEFpBynXrLhaDD6sItjDeeO_vICTYxs6drW02eIa-4E-GNziXvXnxSGsG0lb96ihCN-oMd1WVY3z9x-HppJ_73xFfZK_GCNVMefQIyOcX5ef01igoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بلژیک
🇧🇪
-
🇸🇳
سنگال
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
چهارشنبه ساعت ۲۳:۳۰
📍
ورزشگاه سیاتل (لومن فیلد)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
✍️
اطلاعات و شرایط بازی:
- بلژیک با ۵ امتیاز، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- سنگال با ۳ امتیاز، به عنوان تیم سوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی آمریکا و بوسنی برود.
- با توجه به عملکرد دو تیم در این تورنمنت، باید شاهد یک بازی نزدیک و غیرقابل پیش‌بینی باشیم.
🧠
پیش‌بینی آگاهانه، تمرینی برای نظم ذهن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/funhiphop/79158" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79157">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">۰۲۱کید تورو خدا یه کصشر جدید بخون هرجا تو اینستا میبینمت داری میگی "فیفا ترانا بن مای فلگ" خسته شدم گاییدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/funhiphop/79157" target="_blank">📅 10:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79156">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39eac96d35.mp4?token=osjcRkWVTcPmbpZjviVyxHHhjQo66NZe1mSX1pAn_Zw9gacpiTeeJ-q_dnoT3KlpC-7_8MpcKFfkE43DVLO4ipcgbgIHTK-DASDWGwvT-hPoNSJID2JAl43n9T5x3lSU5rC7Cnld-L_WxoOdfsETi5tcvT8IzSUDIYgcBLkuEKhnw3i5nmdemSNTlovcd9DM_XASTAPLUWVRwhCCT0knNg0fO4OaaO5DfCvP8BoeBUsQcj8vGZ_gd8XULndyX984zdJylLTQYRV1APClymNhToLYrDgjjCwxA9l8KnRHXHOVIQfGw8ipBucEmy-PBI3ustduCtKoxnGX9qSbLu8Mr4BWw6fO29NcHEKNNzsneY6FESCfR-LsUXv9pPj5OUH70JgZDnkLAUlD8TXVfBiMmvRjkVdWB_S_Giy8A8gKSrTLrLxTDUPVbIPxI6aIXzihdOm70CgMrA3XkGWuRdggECymEwAnY3d6Spkt2gh2PbJMgvHSQ46t_1qVJaP9KxA9kpQ9oDTdWELkvJ2RQUtRt6tFuySgJSxpKaSPaefhdU6Ho3SQWZ38f_6y_TCnD6iJycrI1Vbbp-koa8znI8JtCCe8fL1U9CLeO222aPUfdC1IzGjZWbrAEC85Hz2TB33LvfiOtpI_mBnz_4eaF-v_Vo20up8j2dj_AM5t4P9y82A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39eac96d35.mp4?token=osjcRkWVTcPmbpZjviVyxHHhjQo66NZe1mSX1pAn_Zw9gacpiTeeJ-q_dnoT3KlpC-7_8MpcKFfkE43DVLO4ipcgbgIHTK-DASDWGwvT-hPoNSJID2JAl43n9T5x3lSU5rC7Cnld-L_WxoOdfsETi5tcvT8IzSUDIYgcBLkuEKhnw3i5nmdemSNTlovcd9DM_XASTAPLUWVRwhCCT0knNg0fO4OaaO5DfCvP8BoeBUsQcj8vGZ_gd8XULndyX984zdJylLTQYRV1APClymNhToLYrDgjjCwxA9l8KnRHXHOVIQfGw8ipBucEmy-PBI3ustduCtKoxnGX9qSbLu8Mr4BWw6fO29NcHEKNNzsneY6FESCfR-LsUXv9pPj5OUH70JgZDnkLAUlD8TXVfBiMmvRjkVdWB_S_Giy8A8gKSrTLrLxTDUPVbIPxI6aIXzihdOm70CgMrA3XkGWuRdggECymEwAnY3d6Spkt2gh2PbJMgvHSQ46t_1qVJaP9KxA9kpQ9oDTdWELkvJ2RQUtRt6tFuySgJSxpKaSPaefhdU6Ho3SQWZ38f_6y_TCnD6iJycrI1Vbbp-koa8znI8JtCCe8fL1U9CLeO222aPUfdC1IzGjZWbrAEC85Hz2TB33LvfiOtpI_mBnz_4eaF-v_Vo20up8j2dj_AM5t4P9y82A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فری استایل جدید یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/funhiphop/79156" target="_blank">📅 08:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79155">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بی جنبه ترین پلیر های تاریخ ایرانیایی هستن که میرن چیت میخرن تا با چیت لول آپ کنن خودشونو.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79155" target="_blank">📅 04:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79154">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9iYIL8JJjvJR0HlTOUetJl3hU5UsH70yxbYsjviyCNb3AkwcI92e7aQPF-a9AhdzLX_shHw5-02cxLMC9dIltATb5hGdMfvMSe8ZWwlc7DRsM3N0HoZNoEHUb2l5-GvKQUtIsbdqG84AbqlxhZOrIwmOO8EkCpFFEIhADFft076YUlHQa1OLiv_vB49MbyLcB8bOV_ocgIDmTb7K2lENkiHIKj8VecnEzzSetS4os5xm5CiWUoTOyjJwBNXiFhOLpRZl-nK_dIXpNhkxPdIRyNLXfv6qbtFMYwv3GRyE2vI9ySBBJ2N8TxIicH_TCQi2NovyKvPYpcZdEDu37S3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فعلی جام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79154" target="_blank">📅 02:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79153">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مکزیک قطعا اکوادور رو میبره
شب خوش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79153" target="_blank">📅 02:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79146">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فرمانده نیروی زمینی سپاه درمورد جنگ زمینی:  یک دفاع ملی چندلایه برای ایران آماده شده است که ساختاری غیرمتمرکز و رویکردی نامتقارن دارد که جنگ را برای دشمن سخت و غیرقابل کنترل می‌کند. جغرافیای ایران زندان و مردابی برای هر مهاجم زمینی‌ای است. نمونه‌اش ماموریت…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79146" target="_blank">📅 01:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79145">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcD0-BzMWLM3DPOrk_10k_aecTLMKutDHOFNphvSQNx8qHaU0ljQsQ3zlnspoejksKM-X_epP-PprrOjdbD2p8bGkcc31Ea5R9lnfUviAMFAjqACMX2c7p3VD03fO7TK5-SQLIPdLmqTGL3TjwVb_lDOe3E8CBzc66_M8zpTMR7URaLrOk9oc-8DcXJLZRv8sngQLMWhZQgw121bhKWL8RvB1CmdzFc0VmWeZz7lW1MlK1QWDZvcL1PP7WOcs5GN5C18cLR_V8dmL6R8Q2T4O9EuIWGp0-WX_euu5IMWrPIKzhFBI8ktM27oGyHO1FHJOWSQRaPHmOagigOnhwv44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده حمله زمینی امریکا باشید
ناوهای آبی خاکی USS Boxer و USS Portland آمریکا شامل چندین هزار تفنگدار دریایی وارد منطقه خاورمیانه شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79145" target="_blank">📅 01:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79144">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اولیسه و امباپه جوری کنار هم خوبن من بارسایی هم یه لحظه دلم خواست اولیسه بیاد رئال</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79144" target="_blank">📅 01:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79143">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امباپههه
فرانسه برگشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79143" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اولیسه داشت گل قرن رو میزد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79142" target="_blank">📅 01:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">امباپه زد ولی افساید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79141" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79139">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUApEzH0s_rWrvZs9xK2gWimZb3TvsVC1yoQmj0LqZ5u_m6s6UIPcjt05fWiToZFj5O-EquEPs8EBDx_MOE2jZOIvkHf-nEQdE-pv-rjG1ztOQotYiUhITTGtF5iGcrMFSxwb_8z8El0DTVN_9mDAsC7f8G361uRfAt39fivt6JZ0iHGhsiqRN33753JcD51zY0Oc1eL6uaRVGbbeVGEcFSQjOZNAmLZslPhcRH-mQekq-vhxcE0EAz3rRXlbF7qlEm0oYXw0rm67RjkFAioYAlmI1DNEFMOXzELzIiNfTaK07PDPWDZD4-pK2bxTtoX6AujRFUQO7gbZEVi3xLt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس تابوت علی خامنه ای منتشر شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79139" target="_blank">📅 23:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79137">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صداسیما سخنرانی ممدباقرو قطع کرد
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79137" target="_blank">📅 22:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79136">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXRaRTweylwEjOqx9ABn_dimuyI96cwRksAKvIcPGV8ofBmdQ0gZhxiJGF01bdlzhMde66GJMsGnownWHXUZCK4ssNs0vQZarqzqFaob_clD3-xb3od3frd0UA4avk3NaiZHkrQAeFYo4y9_ydpN8HObpfKZMP9y6nDMJYXXXTNuB1wNp3-8aLTMPQIoqgsKiBviPDGUmAYVdBVU3QZtH-LiOKwJuu33PH8dOrEJYDxHTWHq-iQ2qHCsMzp7LvjonOLc1rysnepuC_GpmWidb5gIDDZHb6z2M_40y3NWtLgW1KBDvDkm49UZGRp82f55PN3oLgZkjpSrUctGCOvaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسنوپ داگ
:
«یک نفر دارم که تمام‌وقت کنار من کار می‌کند و تنها وظیفه‌اش این است که به شکل حرفه‌ای برای من ماری‌جوانا و گل بپیچد. در رزومه آن شخص، در بخش مهارت‌ها واقعاً نوشته شده «پیچنده حرفه‌ای» این تخصص اوست.
من سالانه بین ۴۰ تا ۵۰ هزار دلار به او حقوق می‌دادم و تمام هزینه‌هایش را هم پرداخت می‌کردم. اما اخیراً متوجه شدم تورم در آمریکا خیلی بالا رفته و همه‌چیز گران‌تر شده است. مجبور شدم حقوقش را بیشتر کنم. تورم آمریکا عجیب بالا رفته.»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79136" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79134">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🚀
20 گیگ
--->
❗
فقط
49 تومن
🚀
30 گیگ
--->
❗
فقط
72 تومن
🚀
50 گیگ
--->
❗
فقط
99 تومن
🚀
100 گیگ
--->
❗
فقط
169 تومن
🚀
200 گیگ
--->
❗
فقط
299 تومن
🟩
تست رایگان
♻️
ضمانت بازگشت وجه
🔴
تمامی سرویس‌ها
30 روزه
و
کاربر نامحدود
هستند.
⚡️
قوی • سریع • پایدار
📶
تمامی سرویس‌ها
آیپی ثابت
هستند.
☄️
مولتی لوکیشن واقعی در
8 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🇷🇺
✅
خرید فوری از طریق بات
👇🏻
✅
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79134" target="_blank">📅 22:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79132">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">۶۰ گل ملی در ۵۳ بازی برای هالند
😐
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79132" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79130">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=qJrNe-XHj_7Ht67CE4csPKHAkkM9IAchvCe8YsoVKIL6DzTmyXUyBompSs8Y-azp16IkqVVZ1nM9rlsIIB3uEXG7A4ySZgSKjFP2HyQXt4B1JWHO2a-vMRMc37UdXjaBLd3AtDtshvDxQyuI8KncOqQoGXNiMXaiAMYEgrNO7ecmiGAjd6EGVyucHxtOjvXTRZJ82U-5YcFk3zlsGm_NSWPU4KScJIFGKh6ZLChNM5l_eiLECK4-zPNLonf_WmbFWM0fgZXY-8QMQxgHjLFgdJRgvv3ZzIefA8JZM_EZu9oGoj5Xfz5oyGEWWCH6ubLzr5JgIGfgCPrepZWhiva87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=qJrNe-XHj_7Ht67CE4csPKHAkkM9IAchvCe8YsoVKIL6DzTmyXUyBompSs8Y-azp16IkqVVZ1nM9rlsIIB3uEXG7A4ySZgSKjFP2HyQXt4B1JWHO2a-vMRMc37UdXjaBLd3AtDtshvDxQyuI8KncOqQoGXNiMXaiAMYEgrNO7ecmiGAjd6EGVyucHxtOjvXTRZJ82U-5YcFk3zlsGm_NSWPU4KScJIFGKh6ZLChNM5l_eiLECK4-zPNLonf_WmbFWM0fgZXY-8QMQxgHjLFgdJRgvv3ZzIefA8JZM_EZu9oGoj5Xfz5oyGEWWCH6ubLzr5JgIGfgCPrepZWhiva87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خالد مشعل یکی از رهبران حماس درکمال گستاخی اومده گفته رهبر معظم انقلاب اسلامی زبونم لال فوت شدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79130" target="_blank">📅 22:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79127">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ساحل عاج واقعا شایستگی یدونه گل زدن رو داره</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79127" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79126">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">میثاقی: بیرانوند از بشیکتاش ترکیه پیشنهاد داره  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79126" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79125">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">میثاقی: بیرانوند از بشیکتاش ترکیه پیشنهاد داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79125" target="_blank">📅 21:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79121">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ساحل عاج فعلا بهتر از نروژ بوده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79121" target="_blank">📅 21:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79120">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نروژ یکی از استان های خوب ایران
به امید برد فرزندان کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79120" target="_blank">📅 20:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79119">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=P0YBXfZ7aqlgBR880jo-lHEWRmn9TpySEcrvY9e3gdFEfBt4SHJznpbcqTr7Fszu4tEwIl39RrabzAguvVULojnqO8wAaS0FKMdY8EUjVX_GWC4Ksn1UawFwrxWy3N0rQTYfdJ1u37G4-F0_Y2me2ZgFhnp5kKI3imPeRH02I4kZFamInysGHFlcJzX0SMz7QyuWkPM3Cbtpu1iwVY2ZeD0BtKNnG24fjx9mx4LSM5y0I6umJG_Jtl9m_kNfwvZkvej8opy-VUhXCMmFCytScCqQ9ZYrY0NUF2xAvP8LrOyzEfpCxiWBLmW6QlEm7k60xODkc7wAWld34ykBzeDvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=P0YBXfZ7aqlgBR880jo-lHEWRmn9TpySEcrvY9e3gdFEfBt4SHJznpbcqTr7Fszu4tEwIl39RrabzAguvVULojnqO8wAaS0FKMdY8EUjVX_GWC4Ksn1UawFwrxWy3N0rQTYfdJ1u37G4-F0_Y2me2ZgFhnp5kKI3imPeRH02I4kZFamInysGHFlcJzX0SMz7QyuWkPM3Cbtpu1iwVY2ZeD0BtKNnG24fjx9mx4LSM5y0I6umJG_Jtl9m_kNfwvZkvej8opy-VUhXCMmFCytScCqQ9ZYrY0NUF2xAvP8LrOyzEfpCxiWBLmW6QlEm7k60xODkc7wAWld34ykBzeDvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تحلیلگر صداسیما:
جنگ تموم نشده در وقت استراحت بین دو نیمه هستیم؛ نیمه اول هم ایران یجور زد گاییدشون که کل جهان خایه کردن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79119" target="_blank">📅 19:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79118">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromJik Vpn | جیک وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC7LiZwtYfStnXb4kTZ8qJOjnyF8LsJjjZuDBudE0frK7LXxTGmhQ8PewHHbVxuu77lFDWsoRJMGvHBBkoUETMO4Gfp-hTZgwjpB2pe9asIK2xp4TuVrcrn3kkM8q01fGHLP48QsHq7KJFAGYk8-n8Ormq7wI5HfEc4tC6YpR9tPbIGzhEtR_hpistxf4mIovGaM0HaOYiSi_gDp0IvvDxs-HphJWekcl_gol8hsxVSDvE9cKHhRXS13Idn2wTWAl8pdnSNW1U7Kni8GSyZzJmeGp2EjzIlX0ofpoi8rr1qYMm8QD67hbpdZ3n6cuMWeMvsAjA7BQx-eu5NKZyk3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
Jik Vpn | جیک وی پی ان
🔥
فروش Vpn نامحدود یک ماه | دو کاربر | پر سرعت
فقط = 99/000 تومان
💀
سرعت بالا
اتصال پایدار
🏖️
پشتیبانی تا پایان سرویس
🏖️
کاملا نامحدود بدون حجم تعریف شده
🏖️
😎
جهت خرید از ربات
👨‍💻
@JikVpnBot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79118" target="_blank">📅 19:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79117">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یه بروزرسانی داشته باشیم از اتفاقات اخیر: محسن پاک‌نژاد، وزیر نفت رژیم جمهوری اسلامی استعفا داد. محمد اکبرزاده، معاون سیاسی دفتر نماینده رهبر جمهوری اسلامی در نیروی دریایی سپاه پاسداران در یک حادثه رانندگی در استان کرمان کشته شد. فرزاد جمشیدی، مجری صداوسیما…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79117" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79116">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یه بروزرسانی داشته باشیم از اتفاقات اخیر:
محسن پاک‌نژاد، وزیر نفت رژیم جمهوری اسلامی استعفا داد.
محمد اکبرزاده، معاون سیاسی دفتر نماینده رهبر جمهوری اسلامی در نیروی دریایی سپاه پاسداران در یک حادثه رانندگی در استان کرمان کشته شد.
فرزاد جمشیدی، مجری صداوسیما که در تجمعات شبانه بار ها علیه تیم مذاکره‌ کننده ایران سخنرانی و از آنان انتقاد میکرد، به صورت ناگهانی سکته کرد و مرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79116" target="_blank">📅 19:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79114">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به نام خدا
بریم سراغ پیشبینی دقیق بازی های امشب
۱: صعود نروژ
۲: صعود فرانسه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79114" target="_blank">📅 18:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79113">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d3fbfab9.mp4?token=tLdIYpV5XaiOn_9krSfFEHYcMumW5OH_xEhLAdcyT3bERzAMU97Avf19ywz3wcArfbqgUREhehpIIIMqBHJLO-RkS-rn8AVKqZ9XaEIqdLBJZIZsFpgSAqGMn9RuIW1WDZAcphokokUt11tQshvVotaw9PPrbBH9E07gXI8RvEiRNSx4cRU7jkmRDmN5n80r2FDJTQFvsVJhzA5zyD_1eT0goBFYYg1oV43s-TzXx5FsSZ6Bk8Iu8BcbxV84JeX0jAMyGIM6hmeiNmcJ5wif8lplUQBRFbYjhMBhJUNbDKVgilNdSU0d_JtcKfrtbgmWaR-8NesjMuz0F3IvZRgAFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d3fbfab9.mp4?token=tLdIYpV5XaiOn_9krSfFEHYcMumW5OH_xEhLAdcyT3bERzAMU97Avf19ywz3wcArfbqgUREhehpIIIMqBHJLO-RkS-rn8AVKqZ9XaEIqdLBJZIZsFpgSAqGMn9RuIW1WDZAcphokokUt11tQshvVotaw9PPrbBH9E07gXI8RvEiRNSx4cRU7jkmRDmN5n80r2FDJTQFvsVJhzA5zyD_1eT0goBFYYg1oV43s-TzXx5FsSZ6Bk8Iu8BcbxV84JeX0jAMyGIM6hmeiNmcJ5wif8lplUQBRFbYjhMBhJUNbDKVgilNdSU0d_JtcKfrtbgmWaR-8NesjMuz0F3IvZRgAFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیزر تبلیغاتی جدید فیلم اسپایدرمن با حضور بهترین تاریخ
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79113" target="_blank">📅 18:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79112">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj45g0MRuxZylsPOe2Lk1Ey0gZ6JxgtYTuZDVlm7tBvA5TxYmRTj_tZcgirHzb-Zg41EjCqrep5j_mntyRJWImAm3sfBnMXj464VslGpUTeWm132cmz8F8M6aew1A6rNephqLP5ntU29A9TUVmoRMCXadd-ftWNQP_QlR2bQ-sfRzJalPeVGaVlwApEmpT05OpyX9BFmF-JvUq8C-UZn4fv3P-r_h2v1Ubr0YLzcjtwkkNbUgR6unhvjJAM7zgHHH_3RiLT2tjPS9S3B7_V-i6IJsoQxjlBzPGBaViiBCNSHcpsfjV3IuKaOD6iU9hc_5vsZ-iXcFjw5neLXBLu4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇸🇪
سوئد
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد چهارشنبه ساعت ۰۰:۳۰
📍
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
✍️
اطلاعات و شرایط بازی:
- فرانسه با ۳ پیروزی (۹ امتیاز)، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- سوئد با ۴ امتیاز، به عنوان تیم سوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی آلمان و پاراگوئه برود.
- احتمالا در این دیدار شاهد پیروزی و صعود فرانسه خواهیم بود.
🧠
آگاه بودن یعنی انتخاب‌کردن، نه واکنش‌نشان‌دادن.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
G9
🅰
🟢
دریافت سرورفیلترشکن رایگان
💻
@BetForward</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79112" target="_blank">📅 18:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79111">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOfcxmnlbdQ4os_6cOnx5jQe3jRyhJu_rltQ6gRYLhKMAL_tZZMEQB2G10M8ij8ksKljXdaqnCMwq5gwjAfvJUGKjsbqF8CSryN-4x9r1oV8YLu_0ThzW3r7OzbpxR_rynQzFRGCLRX6YexvPzSjuvsEDuAPKL9zp_APd_tVKuUlYpZUI0jqO4OOoDymTNY_8De2UcRLuHSsRXuWVs8rY5hXpAOdZQx6jxIcEMiCu9O8UEKO_E2R0-rY-doCgKJNkZAYfqIMMQlmSGqaV3dXeZJomnsXYFukI_jip_3C8tJkOsamq_VRXGc6Ea2vAI8mA3bTIUdP8VlNeKIontoyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا و ارژانتین رو هم حذف شده بدونید.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79111" target="_blank">📅 18:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79110">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شبکه i24:
ارتش اسرائیل در حال آماده‌سازی برای ازسرگیری فوری عملیات نظامی علیه جمهوری اسلامی است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79110" target="_blank">📅 17:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79109">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbwMhxMncpoouO_TsI3sUNNxjT2XdXocnNXhC4qn13ZgFaipK9Fu8NkwRwX9GnvjJHkxwP1UFQLC1mtUROV_jiJbbxMZ52IXvHNtMNu1TS-jMFqpXcv8wOlZV6L3IPMexqhaUjFX0K0RnRAaL0U8dNhd1Kt6j-uVMJ_xOUEmJp3ezj4CZV8JQ8HK38Khn7D4vy5oOmCQua3GVY3uovwQm5sL9S11e_ksxmboD4brPkI8B8WYpNv2XA0nJw6jeDMFK8JOljY3fiaq5d3fNRvnkK5A4uJwlSDDxZq0btIHTqGY41bq-xM-Q2zh1E8_jciwPlC2uOxHPZtdJBgQHFHG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برج اسکم در علم نجوم در آستانه‌ی خط تورات که به معنای انبوه است قرار گرفته، اسکم انبوه در راه است
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79109" target="_blank">📅 17:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79108">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uc1_MIcQzMMC4WWWacn9zpCGPifrBzI_QbTQzIhk7BAm0R2QEgR3ESwnfyGUVOsvelC-OCyZn2NKZSv7GTbQBvZA4DqgdWNE3SksrJSISGO5wds_3inmc1gV4PLodjG_MeXU3W0Lz3LQhYM02wgZBp6pPgH0Qx4qLpluUJqYeDHbVcV3YgkMiN8jhWUitjdshlRQ1-Tzo91HaEZN4VyZkzfmxa9oU0TP77-kyuavvC7CS7c6pZnUZ5KW2Wszp1y-FfwYWX6dhIOwcaQ10Tn6v6xKWnkIHFKsIkVHX0I4iAX_ypdGGE1saSv7nKvyLqcWDGFoEQ_39wgJAxJEEJDnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هفته توی ارومیه یه نفر بچه‌اش که دختر بوده بدنیا میاد و چون از بچه‌ی دختر خوشش نمی اومده، یه پسرو از بیمارستان میدزده و فرار می‌کنه. پلیس و پدر و مادر پسربچه الان دنبال این فردن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79108" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79107">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSN7uAp26qBoIY49wSpKB9ClpgiMg2vQUMVm1buCORIYi2KD4mtGORfk5DSg6F0OMyXgsUf6mrvHBW8VtseyoL3Uwb1BHtfreF4gXlmidnCh4Ox293M5aAqmEab8ed_-1s7wWYLXvPwMDLsECBc7a-6CCn375tT7wdZ2VEjpU00KErPJDki3X8JnQWwXLm2dtK-UK97ndE_1frXNgrEk5SkvabtCt9ZcFXt5sxvoYPCjel5VK3qDVO8t-dcmBYTtABpsDBIzAjUl_ASJStKcoU5YD00RCYFK_pNDq9ATsTAk3n9oclbzxHSt7P98342qsAiAH75mOVzm21kDGRJZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپویل: فن خال سرمربی هلند شد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79107" target="_blank">📅 16:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79106">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0WxP_iEsEDJ1ca67DTlj2N0j_MVYF854CRg8ETeh08TdSoN0ttHl8Sqvwzonq5OBsaO40N2pqA9RWsBKd79XELMIX4mO_gkLOZQ_w6fImSSTh67Eg3-7tTsbkdlYydfeBcExHyo39rLG82WvrVfQoXYTCJvMIXD_yUPEaGW0GQrEpzN_rjMMh17CIviPcFIPT1GSOAVJn5oqajyDVtllvLQ9spYB4RwB3PHgAigKU3ZicedCfckLatHkY52STw7PhxLVerBfUQ_ddbwtGHy-WQ9yM6nHwYPvGFgsBA-YgiLZprkPAi-yZ60Gv2tCwRKtSVQu-4fw1YJh6SRYwvIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو کی زده گاییده</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79106" target="_blank">📅 15:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79105">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائيل گفت مجتبی خامنه‌ای، رهبر جدید جمهوری اسلامی «برای مرگ نشانه‌گذاری شده است.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79105" target="_blank">📅 15:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79104">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جدی انتظار دارید آنجلوتی وینی رو بزاره نیمکت به نیمار بازی بده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79104" target="_blank">📅 15:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79103">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW2KU-H4nlS1bwr-2vNBRquz4Sc-OIov3mMKwbF-703xMJ0Qhi1HDuh7n0wZsaRfAK7AInDbQknYeqwkGo62mc6NPNTHOhqXbgza60d2X9VnuP1Trn7-ma2IBFirIXgiHZ-_fQYPji8_HhNIAH4J1fKX292jsPwWtB5xd49A02tKv08c1-OOK0cfUHv43VjTEWCSlg-gMge8nFZEGyAb5OCt6ye7RKXo8x9JYB4WvZR-0H_07WkbVpsFA3ccX8Qc1KWmGn9-2BWnprELrXYc9sSrn_3RMcpqawwcdnPQ-0msUNo7ML-nv0BR9TeaC0fzAgaHDZlpsdrgGMRWeVHnCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79103" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79102">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شوک به تیم ملی؛ سعید عزت‌اللهی به دلیل ۲ کارته بودن بازی جمعه مقابل سوئیس رو از دست داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79102" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79100">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxGdpRr8zhqJdzbgznRwrt5rRgI9inJqybSqoPBwMMQuFQEMjiRGMIibczguboMOvK5x5wuIK--yrHt-1YY8kO-AoBB_wWumlLQx-Cweroje9jNjvMei-TqR5XzVBeoYd_uKroiLi9029yU2MwhjK5tIUcdhafjIGfylxMVelXYE6x4oj0FnAC1_TteQa7RzuN31dz47089eN-BDw8Dlkg8B9OUUVEqSh7LaIqRt_IOOdmF-EPz6NdpcK7TG85clMT7haOjsuiR00b1xMoVbY6mqGIKs51CUmE96CexwgJGzgnZyZWZpEzLqQ5wAVD23OkGHvgVZJenbAzQNFlQNBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کونکشم داره آرشیو برنامه هاشو میبینه هرکیو مسخره کرده رو دعوت میکنه
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79100" target="_blank">📅 12:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79099">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">از الان خودتونو برا ورژن ۲۰۳۰ مراکش آماده کنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79099" target="_blank">📅 12:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79098">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWrJq1kreJMzXutozxJTCipg6hdOcCDyc0oPmiU_e7dCRWx5ssciXJlHuZgvMoy6AhDeig698nxQE1cQxBff-fAggsAJea8B2CdWnhgYjpWRoiMiVaKFMTVdTnMXYgI0yB3lQfl0PUE8J9xXCqY-VWJYoNq6G6Uh5o1BhpyqAXnDefost-_UWmHY_ubwheC45OyjG6dZ1fAA_TNgTifoPfHseZFtnvQiXqwW5xwn43MGkaznJTtY2CdLvI8AKA-URdUJgLJK2s6fYQhXZlnNpUytEbohGyGKOuADPnIxCp3P2NOTHwal1O764B3TUdgx77iubvoySTIRzIPz1rBNMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امان از کرم داشتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79098" target="_blank">📅 11:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79097">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw0lA7gMMf7WvwzjtLwYDkAoyIT9B95-SVlmndMA5vZj_RQhDOrrvooHf8XAvPHjhCXDP8oFB2ah9g8Au9GRObw7VPywpvrwJ4L_afE8CEH1AbPBqokNkF_1EUPdU6XvtDF7mUB5i3ERko8PRd5oUp8R56AGpHYwS78zf7V6DaBeObCStkTBxrdo9vh1lnwvBb4L5frvoxQaLfRtS7uSOLWMjmL4LNte8X4WscwikSzOu-BW0y9lbj4B9YDBE2MhqZJxNT62aHwU--v6UXAQk41_vx9NFLr72R6GBmcMpMBRBQK31noMFPLhh16P0ZQJpZxovNI8Wbd9FlcMtYI7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇸🇪
سوئد
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد چهارشنبه ساعت ۰۰:۳۰
📍
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
✍️
اطلاعات و شرایط بازی:
- فرانسه با ۳ پیروزی (۹ امتیاز)، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- سوئد با ۴ امتیاز، به عنوان تیم سوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی آلمان و پاراگوئه برود.
- احتمالا در این دیدار شاهد پیروزی و صعود فرانسه خواهیم بود.
🧠
آگاه بودن یعنی انتخاب‌کردن، نه واکنش‌نشان‌دادن.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
R9
🅰
🟢
دریافت سرورفیلترشکن رایگان
💻
@BetForward</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79097" target="_blank">📅 11:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79095">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کی قراره دست از این که مراکشو یه تیم ضعیف میبینید بردارید و بفهمید اتفاقی نرسیدن نیمه نهایی جام‌جهانی قطر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79095" target="_blank">📅 10:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79094">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLcs4pKNDbAvJ_6nJkp3nwHS6Rm9_hBR1vMWt4OIyRFSyD2sb8ylHe7BGhgeDBmzKF-dS_wOJjXN2Y_8GT9D0UnNkrz7UAd911GMM3s2OJR_YFw7w5aJm0gT9_03MQWJh4qQxlR0XRO_FaL-pMf_-36J30_VN0t0FTfxgiRUOt_Ak-Htwcvzf4n0YPOinkeIDT8XbstCslfZSPhZ1KexWnUAIciHNRGXStKPGBxYra2--uyzE-grDcmYG0gObHAyJNN1LqVrtttw4iiPdtds2hkEDIy25Do1IDyRijVuEIDCyyA_I7RLrE616QkWEfHhhwFmn3kGpZadLacQXd3vsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام دوستان تازه بیدار شدم مشکلی پیش امده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79094" target="_blank">📅 10:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79093">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چه جام جهانی عجیبیه تیمای بزرگی مثل آلمان و هلند و ایران حذف شدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79093" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79092">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAgbnlnwdzybACquPjHO8oiiPAFUn5be3ZwQ0YFFiRJY_K_ggMGQw6mHzjKCKba41GLL9V0wp7BL9xTWJz9vCiMJNThZGdiJLzGddivK7xqjTsbJcTT3b_-oxqOd0_1lxMf39hfW8wICvWsA-bGa73acI4znRvAkvaJPDX6A6HoP7BcuQpCdeLjzFX-ksjw9KeN8alQC3bTr2xbthcMlYFTS8nAT4gXKFmZtgR0ZIYWcEYYGYzPHAe4m_csIgYih6no2a9HrRFgRDD125Rb-xZjRgbk_aUcSK_lqx0EkP8OMGFToeJZvMCFk_ipowebNF64U1bzJnJrx6kfEpMN0UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79092" target="_blank">📅 07:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79091">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هلند هم حذف شد
😂
😂
😂
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79091" target="_blank">📅 07:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79082">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فرید خوش چشم نظری راجب بازی هلند مراکش نداره؟</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79082" target="_blank">📅 03:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79081">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ناگلزمن در مصاحبه بعد بازی:
واقعا نتیجه عادلانه نبود ولی خب اینم شاید یه آزمایشیه خدا داره منو میکنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/79081" target="_blank">📅 03:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79080">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دیگه هیچ نماینده تابعیتی و ژنتیکی‌ای تو جام جهانی نداریم
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/79080" target="_blank">📅 03:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79078">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">میدونم چی میخواید بگید
ولی جدی جدی بنظرم هلند دیگه مراکش رو میزنه
شب خوش
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/79078" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79077">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">و تمام
آلمان حذف شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/79077" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79072">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عشق ابدی فصل سوم اکسای تتلو رو جمع کردن اوردن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/79072" target="_blank">📅 01:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79070">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">میثاقی رو در یک کلمه توصیف کنید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/79070" target="_blank">📅 00:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79066">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کصخلا غنا جادوگر قابل داشت مردمش از گشنگی نمیمردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79066" target="_blank">📅 00:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79065">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCFoZBkPAsbIJVIeRYviDriO4pcrxkxdFrzc23DIvQNmB587x5w3jw1jzZAShCV00LF-_Reh-cn-h9HlvuNV8lUs9-szTigxQCfPFgx_ZYVyOZsQYeTPuM1j0w3SkYnN2DmDAgbIZmcv8dbpD8-SHXVFiMbHphSETU20gkr5bmwffwTzS3hMzmfbxyz5BSgVPoAk2yCCxmddYqUiROh-fZFeVczD6RKvJJcvXxxfBZRsvB7l3-WCZUN32nGndf5u4xE1yFuf3qJggXTNfxWgpWeDZB5IMGuXNMTXSLjZVXo5erSXfFVSqIVOx9Evc6xhwv8fIW_S2c3JH6wb-S5jlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😏
😏
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79065" target="_blank">📅 00:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79064">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سلطون هم رو اورده به دعا نویس
جادوگر غنایی:
کیپ‌ورد تو مرحله حذفی، آرژانتین رو حذف می‌کنه؛ از الان خودتونو برای این شگفتی آماده کنید!
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79064" target="_blank">📅 00:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79060">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هرچی دارید رو بذارید رو صعود آلمان به مرحله بعد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79060" target="_blank">📅 00:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79059">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وزیر دفاع اسرائیل: آغاز جنگ مجدد با ایران ممکن است در عرض 2 روز آینده و با شلیک موشک از ایران به سمت ما رخ دهد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/79059" target="_blank">📅 23:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79057">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حله داداش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/79057" target="_blank">📅 23:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79055">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امشب ژاپن کل دنیا را سوپرایز خواهد کرد  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79055" target="_blank">📅 22:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79054">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برزیل برد و رفت مرحله بعدی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79054" target="_blank">📅 22:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جدی باخت ژاپن به قلعه نویی عجیب ترین اتفاق ۲۰ سال اخیر فوتباله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79043" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ژاپنیا همون عزیزان افغانی هستن که مهاجرت کردن به شرق آسیا
پس رگ و ریشه ی آریایی دارن زنده باد کوروش کبیر
🔥
🔥
#sajat</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79042" target="_blank">📅 21:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79038">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امشب زوج سوباسا و کاکرو کار برزیل رو تموم میکنن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79038" target="_blank">📅 20:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79037">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI_3UGb1wOAo4E_hStzIJZLlpGMBvbzoVbAjjaBRMU9Pk_z40A0lEwqldyWCq33r6QvpGt8EhduffzLFVOuH_o1r1WwJGPokWS57WbmdvK_pwDbdgDy_kxqKzlXiHCV3i6uifvcYDlJuGk-xgSSQjfY-8_jxL5qJMEIr5TnIwB67tW9F9Otei6KJwUHh_34zinzaipI97LZH-5p_gNnPlYofp_xwxG7haWhp2bQD_AXPjUMe9ojm2Jm7DoRKBNSRE4LasR_uF4z59MZxU2g_gzWVOWaa13pdJ_nkweHKeeLv2aH3NpEkDTTZzzaNkN6KL0jJlIdBZp1LEO3gAmOtpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون موقع که ما به توماج صالحی فحش میدادیم امثال این آدم به ما میگفتن شما وصلید و فلانید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79037" target="_blank">📅 19:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79035">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtiliLxH7EkkYwOY3Xh7so3xmFibp4cFyTJ2aO5533IdI9HYc-pykhBBylbkLTILUyB_8yU5BvmXxXG4MYwns54PvH1c_12jy1RfQUjr3AcPAiRmIfK0fKKc_scKCoo8fW78ab_tiqBGnPOcMqZOvr_Fe7cJvmLi9EdHQDGGv3wIIbAvFyZL9HNf3vH8bQF9xtuBoJZvo1o4QzPL1FZ1edD20MExvSdAO1ZTS-bIYLQoQv-3J28AOqmZzc3flshft1DAuNqvRiMw5PoCcGSc2_co2bti5tRW_a0JAU7S-WisuPs8GpQvLbMG75Z0tcZhaemlNzeKnDlgqZCxeQfeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwDKSEfCiTAIoYa0HsJs0rUZbCexkPys007e_ALN2u4OhDcQybWLukjnGjMAJMyxsFyi7xYYEeA96Vrg8rbMJLZXV1Qw-Dk5yaEgdw9Va6wB0M4DBfVieTS6wmqwXUhnDe3_j3NOCL9ZGu4zLxA9G_FtTGYuI74r84ziOTsze1GofW_DXrKC1E9MKOSObpQcZFzmjWltCAieAVfbyb-PigwtyMrnxSr2WKH28RdC252sCZ_sTGJ1rmvhiTerv_xxQj0o55o09ldE47cPW_-m5YrAD7ffkVsoMDcuNK31rCqX8ZOt5uxNaDFs1EBEhM8KPzE__oIYmkkR4DiqVXhfMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیلی ایلیش رو به پسر ایرانی وقتی تو کامنتا چنلا یه پیامو کپی میکنه و ترتیب میره:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79035" target="_blank">📅 19:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79034">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niE937511x9VTHKrc73odDLN4QFjPdcUisnHKtZ2tQRIkohcebWTAjSw8X2JDY9_JiGIgaSEJsPucHfr9N8GfP25DClXolkGo2bJERNVdEsZKYDIUJ-yVwqp2elYqhCsG-5H_ZMm_YgWdVVS9L08AeW2uYKcsrzRB5-dv4jxW8ELbOg_qdpYRhxoDhsoLvLagC5k94thnveRqsHVPzpzlEpaaV-HbYFLNNF2GVq0n0eeNZUYEI5AwnW_OXDuUOPMQNKnjnLPpmcBcobc4eiciZKOYQy0QOLzrC9oSrj0DngPbJkkQS905dY6nGSUNF4ilZOQYhggL-oycXYbrpvaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم از روزی که دمبله بعد بازی مسی رو لخت کرد.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79034" target="_blank">📅 18:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79030">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چرا هوس اف دراگون زمین تا آسمون با کتابش فرق داره</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79030" target="_blank">📅 17:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79028">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سارن و کوروش کی قراره به این نتیجه برسن که ترکیبشون کیریه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79028" target="_blank">📅 17:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79027">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان پدیده یعنی شما حدس نزنید کدوم تیم قراره باشه، نه این که ۱۰ سال منتظر باشید مراکش و ژاپن همرو ببرن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79027" target="_blank">📅 17:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79026">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کسی داره ۱۰ هزار دلار دستی بده؟ بخدا برنمیگردونم
@Funhiphop
| محمدرضا ناصری آزاد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79026" target="_blank">📅 16:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79024">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کسی داره ۱۰ هزار دلار دستی بده؟ بخدا یرمیگردونم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79024" target="_blank">📅 16:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79022">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حزب‌الله رو که دولت لبنان اجازه کامل به ارتش اسرائیل داد خلع سلاح کنه، عراقم که کودتا شده دارن مقاماتی که ایران تغذیه میکرد رو حذف میکنن، از جبهه مقاومت فقط یمن مونده درحال حاضر.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79022" target="_blank">📅 16:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79021">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حزب‌الله رو که دولت لبنان اجازه کامل به ارتش اسرائیل داد خلع سلاح کنه، عراقم که کودتا شده دارن مقاماتی که ایران تغذیه میکرد رو حذف میکنن، از جبهه مقاومت فقط یمن مونده درحال حاضر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79021" target="_blank">📅 16:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79020">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فنای بارسا اینطورین که از بازیکنا هیچ تیمی اندازه اتلتیکو بدشون نمیاد ولی عاشق آرژانتین، حالا بازیکنا آرژانتین کجا بازی میکنن؟ نصف بیشترشون تو اتلتیکو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79020" target="_blank">📅 15:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79019">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4pbJ9yaQ8iPQlcqGyTUqswuuWG4sxZrqgzxmuTiuwMmNlau3vvDuKWaL0cMkJ4Wl8_6UT6W5IvMWdSKy3IfJcLUfRGaWj30gNR9OZ7NNVTfydTEtYae3g4UlW27PoHGMQDUlT2nJtuZSNshdfIKdgMXy0S-V2NjpxP2UU3UfZ_6jayIwW65IebJFhSlP5itvR_C7lcf5P92qrLsq6lBPVAyvUP3P8rfcYJslAcngePkYpnN3i8oWww3WQZAY9eTRyLH6UlVeCsTjsaW08T6qyzhPWmfC44wVBNd-TAitJYU6abcG8Hckl-Olu8PeXEgVI5u5hsed_dz6vDjj2nDaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان خودت نزدیک تر بود ولی.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79019" target="_blank">📅 15:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79018">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSYaEpv8cMz11LZIZtjMbRH5lasHU_VZUSnhR5PNgbeBGnWEr2N9DX8BZuH2U6Yvi9wKtRFY1FywC5LfQpFP49TVnDGBE1zQykN-OusM8vYmvGCLEkAr5y42eVUHdAQviWRjuX7MrRI1ESa2eK9Q8BYs_RhizmfnbHCSN7l9SCXZ_cA8KRlZLNRnb_6DBj87LIRESFz6_AnAV3QqOLYjLdxnf_waYP0S8xDhdyDR6S1FrbFnxyU-CfLdqxjS1XVjNwYOl2xKUx6hh4-wMBVBTtyZIHYjyX3k5jP5hT02wR7LfF_udeG4_DiUMnGRE8huhE_u1umiprjc-SFM7Xp91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79018" target="_blank">📅 13:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79017">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">میدونستید یکی از اهداف اصلی ارتش اسرائیل برای جنگ بعدی سایپا و ایران خودروئه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79017" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79016">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آناناس مادرجنده تو دیگه چرا</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79016" target="_blank">📅 12:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79015">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_si39uQeEIJd31IEDNkV-ye9vaSq0-En-etJAuo_5axzaxyOWZJHa7iHKkVsstrsvjAnh9A2oDhlCGjQ5Ny6mF0xTKVPKH4JX3G9pX9STpcijQEdPPQ1eZ20cEd05Ud-cG1TYYzKamErOe_EVtB47vc7lt74P8qLtLnbuOoUD_NTx9X5AjRIc09dLhfWmvaZ-vZY9-bIZ_fO5Bwu6_pny5tLauZDsHZ5YaRcTakEf-RxjsQO1H7D3eRrvmvZHWZDwsxIt4ktgyEMbSDwxAHX3WUDMyjKqAtEnbRGNcYvlmUs_rEXVIh11ho7AUuSrFUpOTvsg1fw-Xr4E8LPFnzAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش و سارن به نام بهار ما گذشته منتشر شد.
Youtube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79015" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79013">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امشب ژاپن کل دنیا را سوپرایز خواهد کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79013" target="_blank">📅 12:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79012">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be7060d94.mp4?token=OKf-3lM7jjW3knLTFNO4vdEQwPeuAWeTPsf5NaJqqK_dnwZiH-LFvuqvuSE-OLLwSZUnouTIGDIfBaWIqRMzPRVeFH0-rEhZY4V2M7UE2_eOqaI68omoPNomSOWO6qo9G0SKRLf20Bx2ki4M1A5tXL7s0l7sP2qRi54jsm4N04r4fMPcZVM0woP5_PzAU2_XcVuZ4_MAEqqc9Ot9QVz7Meg7J2mfzAl4uOSe3T77n4XUeK18vIV3MTw_pXKr2W95WGNdrFzfqLLr5QYlyb4edOX6RUeJDMCIQrM5su4ZP1Dd06vse0BrgeAf4LiXjoo9mxMHmPuzu4fNk5Mvv5_Tfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be7060d94.mp4?token=OKf-3lM7jjW3knLTFNO4vdEQwPeuAWeTPsf5NaJqqK_dnwZiH-LFvuqvuSE-OLLwSZUnouTIGDIfBaWIqRMzPRVeFH0-rEhZY4V2M7UE2_eOqaI68omoPNomSOWO6qo9G0SKRLf20Bx2ki4M1A5tXL7s0l7sP2qRi54jsm4N04r4fMPcZVM0woP5_PzAU2_XcVuZ4_MAEqqc9Ot9QVz7Meg7J2mfzAl4uOSe3T77n4XUeK18vIV3MTw_pXKr2W95WGNdrFzfqLLr5QYlyb4edOX6RUeJDMCIQrM5su4ZP1Dd06vse0BrgeAf4LiXjoo9mxMHmPuzu4fNk5Mvv5_Tfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیلیان امباپه 178 سانتی متری در کنار ویکتور ومبنیاما 224 سانتی متری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79012" target="_blank">📅 12:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79009">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yjx7teuzuDbCUmjOKqcBe831VDjzuz0a7xbVwHWou1ttbdkgMil1WPg38CSPK6mp50EPZXdlEsT51buqxt5pYs-qAL0RX6gBT-WOM9vRfIUmuDplVaikKFGsKMtdsy699rmU0lbqzN4s0rc6QpnSw1i3KkRBS_Umb7rBAhR6ZBK6YwCvuOp8Uiq9vtSQImXV4laxqjn0cSf6CsWX1maOIjsk72SG_4yzC-Mw-ch_5OeRHqa2lfqNSTc2xtfwAfyCaLdXO8SBGDJUra3lJz65GP87TWkePdP_6N3bQ6ojrf15DuL0h4DtB6ZGdw5ck3pbjV1iITfpXND9yRESYtErnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه کیرم تو دهنت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79009" target="_blank">📅 12:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79008">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ناموسا نمیدونم دخترا از چی پسرا خوششون میاد، پسر خیلی کیریه</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79008" target="_blank">📅 11:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79007">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ناموسا نمیدونم دخترا از چی پسرا خوششون میاد، پسر خیلی کیریه</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79007" target="_blank">📅 11:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79006">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هعی از وقتی اومدم کسی من و تحویل نگرفته:)
چه چنل مسخره و دختر پسندی:)
ما پسریم همونایی که موقع حرف زدن بهشون میگن هیس:)
همونایی که نمیتونن کراپ صورتی بپوشن:)
💔
🥀
✌🏿
حرف دلته؟:)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79006" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79005">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حال و احوالتون چطوره؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79005" target="_blank">📅 11:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79004">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حال و احوالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79004" target="_blank">📅 10:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79003">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پشمام با این گل کانادا رسما تیم قلعه نویی صعود میکنه مرحله بعد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/79003" target="_blank">📅 00:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79002">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نتیجه میگیریم دریک کیر منم نیست</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/79002" target="_blank">📅 00:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79001">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کانادا زددددد
دریک برد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/79001" target="_blank">📅 00:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79000">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">لیگ ایرانه یا جام جهانی؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/79000" target="_blank">📅 00:12 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
