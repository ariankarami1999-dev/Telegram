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
<img src="https://cdn4.telesco.pe/file/fqcG5RfpsVYHIqZrI3_9H4bDSdhiTiZg5mSHK-bHT9QE8ob1bFnFNFRMfguH-WLyBjMPtg5LVYKJcT7r2T0YIzq8iXz9V6CykhXiP0QkJhY9_STBEqrXr-nwA35b3sWLggBrHJE5WGRJLDUAgXsisZsHu7-cBvcP1Ns4ZfznKbAv08Vxj34xHNuUfVzq0Dj1q39lfLwSe_SsSMeZqVOIWaiWHtLQryQK-RxOqflpGFFXLj7yDiITIU4w8q0Pt5i18V6KgYGJaejFo5fruS9otrJIV36y-G0FDhc4vpb0hS74M483R1Ig_cguJGlC1M4KZbeND3eWJV3epF6X0Onn3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 126K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 17:44:53</div>
<hr>

<div class="tg-post" id="msg-69941">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⏸
صحبتای یه فرد رندوم:
سوال من اینه؛ چرا بعد جنگ 12 روزه خبری از این تجمع‌های شبانه نبود، ولی بعد جنگ 40 روزه شروع شد؟ دشمن که همونه؛ پس چی عوض شده؟
دلیل این تجمعات شبانه مخالفای داخلی‌ان یعنی مردم خودمون؛
مخالفای حکومت هم مردم همین کشورن، وطن‌فروش نیستن. ممکنه با حکومت مشکل داشته باشن یا طرفدار یه مدل دیگه حکومت باشن؛ خب حق دارن نظر خودشونو داشته باشن.
اگه واقعاً می‌خوایم بدونیم مردم چی می‌خوان، یه رفراندوم برگزار بشه تا نظر اکثریت مشخص بشه.
سال 57 یکی از اعتراض‌ها این بود که مردم آزادی بیان ندارن و مخالفا سرکوب میشن، اگه الانم مخالف نتونه حرفشو بزنه، پس دقیقاً چی تغییر کرده؟ مخصوصاً وقتی وضعیت اقتصاد، روابط خارجی و خیلی چیزای دیگه هم بدتر شده.
در نهایت هر ایرانی می‌تونه کشورشو دوست داشته باشه، ولی در عین حال منتقد یا مخالف حکومت هم باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/news_hut/69941" target="_blank">📅 17:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69940">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kff3DGmIM667V1c1190JiDNQ7YEZjWrETCjyA6Q_2m53ZfvJd69MeeXJWSauUXhS3y6BCiXs6h7Rwf6dIPuUL5e3Q2HMz_fgVTTntMZ56TRbcgtAHgoH2aXcHeDcaqQvWffK58x82zyfKulx5bFkzRHCBGMObV8L7zLA2cEM2PhObjQExwd2c6kYC0BFCtVpHan6A0UEJ1oLnVpFkT8orUL046lfjByi1JX38-AjwP2fb4BXJM61OQLIyaDV1E5dowFtzcznosADdli5vOCRVGCxJ-EM-lxfNWhBoaHNVtqHG-XdaGpYip_XYlCABdafggq-oE2Dx9O7v1tZ24VAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو ایتا، یه آخوند به اسم  "شیخ ‌احمد " چنل آموزشی با موضوع مقابله با غریزه جنسی فرزندان راه انداخته
😶
مادری که پسر جوان تو خونه داره، نباید با آرایش و لباس آزاد تو خونه راه بره، باید چادر بپوشه چون باعث تحریک شدن فرزند و راست شدن شومبول وی میشود!
همچنین پدر نباید با شورت جلوی فرزند دخترش راه بره، باید حیا داشته باشید.
پدر مادرا جلو فرزندانشون همو بغل نکنن، وگرنه میرن جهنم
@News_Hut</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/news_hut/69940" target="_blank">📅 17:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oG1rFyrSKS7PoZx9f3de0tbrpAPJz5H5Dn4V3zFTH3P1ztTl_F2hTQK4QN2jEBXwRW2CocaEZ1Zc60qygFa83If4_qjN29Pv0lndwvMZCEJnPrdaK6gEK6RqOBNjyKhpzqp-NwCwC8Sf_D2GwWaUShfo4VFR4Oo6Bk6NSxfV0q4u5gB3WEA6XVkh6mHIfzPoIiIaN84FQZQKB-g_H0BfcENlelZ0LKGUVx5Vzw1oroBDkrxq3KDhmaOEE-zj4-CmmPgG6l4cxgIWaSS82SbadHuiS1pzipa4dMKRxRYsEkjSbWxImKstUF7hSZERFJsjFhTjYvn5g3i_DKVabCJz-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9298752134.mp4?token=rO1oEOvQwt5h_0jMBdJ0ivMFbzRp_5VUI5Cbb5-54BLsR9SfYtiYPADoRc2nEZy8OZBDhYkNeOFNbvXAcR0LM2hUHoIZSEKcCsrBTVmHT-SfIZXVmr62vr4AQQKcVz-SSyt4m9RD-93ehHJk557TVgUrA2bXjhpSAiZ0evWTobc9S3QJlAxUMMXFFZuYKYJbZambTFguE3-WWH5ozswQ9mE6pYn0uKaxHSQuK3vt7yTbBJNXeDlQdshRUTXSOt5JoRgru27hV5Bop2FDPgc9rHJ-5UDZerDnS-FFE9WtqV5R0dQw-83VSoOy_Mxf9QuQ82nJT9cXQrj8-vZxZ4jO9oG1rFyrSKS7PoZx9f3de0tbrpAPJz5H5Dn4V3zFTH3P1ztTl_F2hTQK4QN2jEBXwRW2CocaEZ1Zc60qygFa83If4_qjN29Pv0lndwvMZCEJnPrdaK6gEK6RqOBNjyKhpzqp-NwCwC8Sf_D2GwWaUShfo4VFR4Oo6Bk6NSxfV0q4u5gB3WEA6XVkh6mHIfzPoIiIaN84FQZQKB-g_H0BfcENlelZ0LKGUVx5Vzw1oroBDkrxq3KDhmaOEE-zj4-CmmPgG6l4cxgIWaSS82SbadHuiS1pzipa4dMKRxRYsEkjSbWxImKstUF7hSZERFJsjFhTjYvn5g3i_DKVabCJz-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کلاس درس «ریاضی ولایی» با تدریس محمدباقر خرازی:
«شما اگر ولایت داشته باشی می‌ری زیر خط کسر...
اگه شما به این دکترای ریاضیات رو بخونید اصلاً این‌طوری نمی‌فهمن...
حروف قرآن از راست به چپه اما انگلیسی که زبان شیطانی‌ست از چپ به راسته...»
@News_Hut</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/news_hut/69939" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69938">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
🗞
رویترز به نقل از یک مقام ایرانی:تهران و واشنگتن در مورد تمدید آتش‌بس گفتگو نمی‌کنند.
این منبع افزود که از دیدگاه ایران، هرگز تاریخ رسمی آغاز آتش‌بس وجود نداشته است و بنابراین، چیزی برای تمدید وجود ندارد.
این منبع ایرانی، ایالات متحده را به نقض توافق‌نامه همکاری متهم کرد، این در حالی است که این توافق‌نامه تنها ۴۸ ساعت پس از امضای آن نقض شده است.
این منبع همچنین گفت که مذاکرات فعلی بر بازگشت واشنگتن به توافق و تعیین یک جدول زمانی برای انجام تعهداتش متمرکز است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/news_hut/69938" target="_blank">📅 15:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69937">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e246580c.mp4?token=cmOXonODcb4S3aMvXF6-okAj4bhAm-RUJpKdB426bkN29xmCnd3m_tCDB_zWNAeCPIHnxmV4Im6ciEyRc3NF9jiPs0hzvfZmn5gbb2UDTTe1HEOdiDTDXEXPqYv205J4WYp4itWd7c_jOanPM8yRJf9hcs8jASyVmW2PfwM_PCWf1HIVJSlB_SwpgABshJlOQM7nHCAQRYVLFJx8yzxQTJedtcz7M3Vrt6bEp78AmkS5Ib_1PDRMhjwIoEaRk9B67NnEZfQSHj1yhdgqGVyTzkNQB6wD4FTkeFqOYg3Ghh7OA7-uJAmluJwAsaHF0R_jaGkygNaf-JhQVp_r9y5Fsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e246580c.mp4?token=cmOXonODcb4S3aMvXF6-okAj4bhAm-RUJpKdB426bkN29xmCnd3m_tCDB_zWNAeCPIHnxmV4Im6ciEyRc3NF9jiPs0hzvfZmn5gbb2UDTTe1HEOdiDTDXEXPqYv205J4WYp4itWd7c_jOanPM8yRJf9hcs8jASyVmW2PfwM_PCWf1HIVJSlB_SwpgABshJlOQM7nHCAQRYVLFJx8yzxQTJedtcz7M3Vrt6bEp78AmkS5Ib_1PDRMhjwIoEaRk9B67NnEZfQSHj1yhdgqGVyTzkNQB6wD4FTkeFqOYg3Ghh7OA7-uJAmluJwAsaHF0R_jaGkygNaf-JhQVp_r9y5Fsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حرکت عجیب مجری در پخش زنده
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/69937" target="_blank">📅 15:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69936">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vct1DEK63YEq8hVqrmXGLoU0aqtIyoaVMogkFZNxnHbIXa-vojxxGRarV8sRheYViJkeKvuFuLZX6mjI-7gV5fFyc1AtbKnaqqnJKWrmBrRGUoO5CulBwmrs8me2QIGdJSf0I5X_Lv8J88aU9qhIO9ocVhwCv14Y7bkqbPfNXCFWuwjOEhOA_74gUlKheapY0fjqRMDrgC44l4sSt9hJ3PVqcGkntJpjNwGBbHEU5WhAuLGhphPbzy66kdfqu4cPRvf4g4p2Qg2KqXjNtyw8MS6-h6JJHbKIyUrmzAcL0vpH0u2VTlFp-lik9N9kZLhA3TFZtY2oFDkfGdTINY0rWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
🇹🇷
🇺🇸
نیویورک تایمز:تهدیدی که از سوی ایران مطرح شد و باعث شد رئیس‌جمهور ترامپ ماه گذشته به طور مخفی هواپیمای "ایرفورس وان" خود را تغییر دهد، زمانی آشکار شد که او در آخرین روز حضور خود در اجلاس ناتو در آنکارا، ترکیه، در تاریخ ۸ جولای، در حال عزیمت بود.
اطلاعاتی که توسط سازمان‌های اطلاعاتی آمریکا جمع‌آوری شد، نشان می‌داد که یک تهدید خاص از نوع موشک‌های زمین به هوا علیه هواپیمای "ایرفورس وان" وجود دارد، صرف‌نظر از اینکه کدام هواپیما حامل رئیس‌جمهور باشد.
همچنین، فردی که در نزدیکی محل برگزاری اجلاس ناتو حضور داشت، در حالی که یک موشک قابل حمل روی شان خود داشت، مشاهده شد. در همین حال، عوامل ایرانی دقیقاً می‌دانستند که ترامپ در آنکارا در کدام محل اقامت دارد، از جمله طبقه محل اقامت او در ساختمان.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69936" target="_blank">📅 14:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69935">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=oFjSyF-qxgxI4SxMfCT-J2PaafF9DIGGoxTpq8PAh4KtEMw-tpczuX-HITO5R5TC2NENUMqWOkINzHw_Zi5IeinXjBXbQlqO9k3f1rM7Wnsw-oW2XmnVs3mFmytgu6W2Cxhr952CRdIOydeXfEUpI6UeqkOexZUwOBc_fHhIj0byuwn0Fjg2CiuRBYGWsiKAi4xqaKlvcSmROj1iR3bvnWD8Jh6veIH5BXzERXpUNAHMUTuEFJxJSLGlin6z-ICBDxr1r3biJhKBUWO603Xp8Yi5MIDcSLs8JAn1R47s2sFYrXv8PigQ4sK_ym12RskNSgiKWRMoypSP7odZ6Lr0XkJpgtzmwsEe0ZKRoQExMFGqUwLjlR-fnI0-Gfidp_Lj4inzx8w_s5r8aLftp1js2yhXeAgZx-Q_Q8SgngLHllDTcZwh2DS8d3qao65H9cLg-crXZ1db_fCSzoBFrqyBtCx0M1nKI6Rg5RRKAyTYT_-9mtZzMMzHr9u_-2rEb0W89jqDwMxqe0tKb77X90qjbhVajwGXjs3uW2Se3VSrIlIS3ps6ncoj_HH-7mfR5F4n9qYY1kFabQf-y-pjRtXxr9Gmx7ioVRq0ur6Qd_05K5bnV4i7tZWsfN_f8-3FvrzYr7vbZafiOVpTjOKEAuClelSYxyqV7bix9uYQX4gkNaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7465fa629c.mp4?token=oFjSyF-qxgxI4SxMfCT-J2PaafF9DIGGoxTpq8PAh4KtEMw-tpczuX-HITO5R5TC2NENUMqWOkINzHw_Zi5IeinXjBXbQlqO9k3f1rM7Wnsw-oW2XmnVs3mFmytgu6W2Cxhr952CRdIOydeXfEUpI6UeqkOexZUwOBc_fHhIj0byuwn0Fjg2CiuRBYGWsiKAi4xqaKlvcSmROj1iR3bvnWD8Jh6veIH5BXzERXpUNAHMUTuEFJxJSLGlin6z-ICBDxr1r3biJhKBUWO603Xp8Yi5MIDcSLs8JAn1R47s2sFYrXv8PigQ4sK_ym12RskNSgiKWRMoypSP7odZ6Lr0XkJpgtzmwsEe0ZKRoQExMFGqUwLjlR-fnI0-Gfidp_Lj4inzx8w_s5r8aLftp1js2yhXeAgZx-Q_Q8SgngLHllDTcZwh2DS8d3qao65H9cLg-crXZ1db_fCSzoBFrqyBtCx0M1nKI6Rg5RRKAyTYT_-9mtZzMMzHr9u_-2rEb0W89jqDwMxqe0tKb77X90qjbhVajwGXjs3uW2Se3VSrIlIS3ps6ncoj_HH-7mfR5F4n9qYY1kFabQf-y-pjRtXxr9Gmx7ioVRq0ur6Qd_05K5bnV4i7tZWsfN_f8-3FvrzYr7vbZafiOVpTjOKEAuClelSYxyqV7bix9uYQX4gkNaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران:
«ما بیش از نواخت شلیک موشک‌های بالستیک، در حال تولید و تحویل آن‌ها به رزمندگان هستیم.»
«ما فقط ۹۵۰ شهرک صنعتی داریم به علاوه صدها مجتمع صنعتی که خارج از این شهرک‌ها هستند.
اگر روزی برسد که ما هیچ موشکی هم نداشته باشیم، ما خطرناک‌تر می‌شویم چرا که دشمن با تاکتیک های ناشناخته ای مواجه می‌شود که می‌توانند منافع آمریکا در جهان را به آتش بکشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/69935" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69934">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyCngHQYJ8Px8QVZzaC9dqLFTCY3mLChmHEfHpit-3YQPbsBYsWdJB09e2BeFQIHMh1Em-k2IDxj_4Sl1PIK8MSFz8x2XQDGxb8YL0z_QeFmTCfYeL0P1TvtPKie6P9qWUv6KBg46bm2fgz52Fa0yX_wyUBFa71hiF7HFWCkBDrLAuLEwVir-WfjHox9R480UXfMKhZAh71RkFsQ-LPMAEB5DUkpkF9FN7-mwhve-_azG8PuWNQtCb4ksMfOhbIfH7N2haOkX0LeIaleocPzFXC8uDCWqOXs0awpsmZc-xd2dSQrA3Fl7xbRcehrlLFHHHD_CpnDH7_1nWclz8FLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69934" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69933">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=SyfiZdCJhCgKWwVTJ-7Mo9bcpG2BQmhZdhcRTALTO9C5Cev63X9DE9g1VJNBnbXUH4WsmbzxK7WvpZBWGeXqOJdYZjsOSMsQItBKayWKs8T7tGjoaa5p7RM7BwOptjWwDro2Isk1ki-umw_ktv0NAF4fFbq0NPZ4EklVVwNFqk_QHkprNSwvAbqZKFE9lrdOZPBtLpMxmhdF57pa2PLq352szhUSAzhzqs-bGZcvVwyDH8PFLbq8YnT-WOC4Fc4SKTAYSMvTxPRirgg9JoRPaH9uzYomSaJbMvI0wenM4cG17gWmD9zt9S5ONE79RPWSDqJypomexeftmBJxFCykvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae5c53c68.mp4?token=SyfiZdCJhCgKWwVTJ-7Mo9bcpG2BQmhZdhcRTALTO9C5Cev63X9DE9g1VJNBnbXUH4WsmbzxK7WvpZBWGeXqOJdYZjsOSMsQItBKayWKs8T7tGjoaa5p7RM7BwOptjWwDro2Isk1ki-umw_ktv0NAF4fFbq0NPZ4EklVVwNFqk_QHkprNSwvAbqZKFE9lrdOZPBtLpMxmhdF57pa2PLq352szhUSAzhzqs-bGZcvVwyDH8PFLbq8YnT-WOC4Fc4SKTAYSMvTxPRirgg9JoRPaH9uzYomSaJbMvI0wenM4cG17gWmD9zt9S5ONE79RPWSDqJypomexeftmBJxFCykvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سفره‌ای که واسه عرق‌خوری تو زندان پهن کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/69933" target="_blank">📅 12:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69932">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=dNgac9IfY4QDzka5ifP82kXpDwJnsvJVTLqrtdvrGNkyN9edHRIgtzTbOL8o5G50CVnSF0h07wpcbTiDzqhgkJ-QSCkZB6GeEEvkVFTc4WK8DR3BidhwuFgLSShawkpQFhBnCNaZN2p31egKFBpy0zjg4hDjGSlKAcPLx2_DfD0etnnp_dgb532IBjeL2ODk5aRgP3P3hUG_KxYmlLF7WR1Dy-2Nq_RaUYYTnSL0Nby7m6JXP3JcoMcCKSUh903vl_os9M1d6c6tdLkzamL2STT0H1KepNBkQrNxNZ0GrmEYVsacdbH9Pu-4XJ0aiab6Ivb-CaEcdesBceeor1HDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca7afc613.mp4?token=dNgac9IfY4QDzka5ifP82kXpDwJnsvJVTLqrtdvrGNkyN9edHRIgtzTbOL8o5G50CVnSF0h07wpcbTiDzqhgkJ-QSCkZB6GeEEvkVFTc4WK8DR3BidhwuFgLSShawkpQFhBnCNaZN2p31egKFBpy0zjg4hDjGSlKAcPLx2_DfD0etnnp_dgb532IBjeL2ODk5aRgP3P3hUG_KxYmlLF7WR1Dy-2Nq_RaUYYTnSL0Nby7m6JXP3JcoMcCKSUh903vl_os9M1d6c6tdLkzamL2STT0H1KepNBkQrNxNZ0GrmEYVsacdbH9Pu-4XJ0aiab6Ivb-CaEcdesBceeor1HDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تصاویری جالب ، از تلاش ناموفق یک تیم آتشبار سیار روسی برای رهگیری یک پهپاد انتحاری (کامیکازه) در حال عبور را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69932" target="_blank">📅 12:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69931">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=X7qVTw5loN072RRP6TX4CDdmD-PIKQpamy8XmIft6lPESt4RBhnXXC3IgRuRJOqG2n2YCW4zVmbNZgBqzX-emCDX0ThcNR-hNiSW1OHoV-4OU0IISUATAfLzDvDXCl-kHCUmuczlIOtJEli6yadnWUamEyfAN4ctgEhMNIrkRNrYBxeoM7Jtesz2bZMSWVhUczqBhAsche26XO0kktWSxzrjfcTvwqN0jeL_e5g6JqH26nhBfI4Q2iBM4Pebax2V9N5wYy2BJ4RM7B_X2krYvtICWEhqhbKclxPD97u-vsaEuWVwZAu8gI0Oi1PTJT84KNVrd1aOUYd8crW8ZLWwHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd2c3a8ef.mp4?token=X7qVTw5loN072RRP6TX4CDdmD-PIKQpamy8XmIft6lPESt4RBhnXXC3IgRuRJOqG2n2YCW4zVmbNZgBqzX-emCDX0ThcNR-hNiSW1OHoV-4OU0IISUATAfLzDvDXCl-kHCUmuczlIOtJEli6yadnWUamEyfAN4ctgEhMNIrkRNrYBxeoM7Jtesz2bZMSWVhUczqBhAsche26XO0kktWSxzrjfcTvwqN0jeL_e5g6JqH26nhBfI4Q2iBM4Pebax2V9N5wYy2BJ4RM7B_X2krYvtICWEhqhbKclxPD97u-vsaEuWVwZAu8gI0Oi1PTJT84KNVrd1aOUYd8crW8ZLWwHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از هجوم انقلابیون به کاباره های تهران و نابودی هزاران لیتر مشروبات الکلی، در سال 1358
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69931" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69930">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/69930" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69930" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69929">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahjHkbDS7PpcszymJ3A_Y45CWJKXVCrGxuQTv1SzWg4qDOk1-Q_3lV4pkk7FLci3YUhKsvUdHMrHLkK_TT6CsBNvUNMWoxxCiiD2zwVT0MPenvgMqL_sFtENVwYBhs-AaZ7MvqLWcorW1EdsvihclyNUiCdMUBmP-bWBb96HPqE4Rz5Sv-Zkpqx4lFhQ5F05xVSRVMqRPSuBsIDiGvZhuCEzdqSbN7Sow_yKjNrbxaqCLCA7I9h1wksvSFvNhmbQOuOHtz-Ph09jDOz_lE9waBCcPl9G-mHXGS15JRlnbbED-77Co0yBosLPmulN-aaODQaerFkvXrx8stebNram4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/69929" target="_blank">📅 12:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69928">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=KwyWNXKBKxXlG7JbWm_fwHain9JJE7BWEOpr5oQ1xwVX7NTE3d-Wb22BaoFssB8yiqTqUgwh3Rudxe6U9m620A48kaDgsnEWCsXM882o6rFFJLtMOcBcTPog8ToYp6tE-jj91RnCfsZtiwy3w-Zod3yMJBS2OjXkPi65X2VmoM29bZS_QDn1l0zq6XXykg6EDntVCbkYTYlPzR2RAsOHwRvOPze0LsFHQY_PD6M1B9FSSE8bGdS09ITyCh8ZzY9q1E6hhS0jD7Z926N7CxUo5Ae-B4nq_vfwc8PE5dPCTOof93MThu6UYwiFojOqkCmrYkGh72-7NQi_6mdZTAG9yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9676b05e8a.mp4?token=KwyWNXKBKxXlG7JbWm_fwHain9JJE7BWEOpr5oQ1xwVX7NTE3d-Wb22BaoFssB8yiqTqUgwh3Rudxe6U9m620A48kaDgsnEWCsXM882o6rFFJLtMOcBcTPog8ToYp6tE-jj91RnCfsZtiwy3w-Zod3yMJBS2OjXkPi65X2VmoM29bZS_QDn1l0zq6XXykg6EDntVCbkYTYlPzR2RAsOHwRvOPze0LsFHQY_PD6M1B9FSSE8bGdS09ITyCh8ZzY9q1E6hhS0jD7Z926N7CxUo5Ae-B4nq_vfwc8PE5dPCTOof93MThu6UYwiFojOqkCmrYkGh72-7NQi_6mdZTAG9yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قیمت های پشم افکن خونه و برج توی فرشته تهران بعد از جنگ که به متری 2 میلیارد تومن هم رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69928" target="_blank">📅 11:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69927">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=wBla5BbLopaBzQ7kHZweGJrlRe0m3o4shvuMNfdHirhJatWcKE_jFjge-b143T6USt3MSof3DdarHsPprFDwMktlbpDv_OhXW35Rs49rTJileFL9UAhvu2NeqFt_dNI-AJW7DYFMeqoRkbGeLBpyIIWStlkBjKFrCqoPtZQAQVjwswB_rmgXn6kA-FjvVDn7T6EWkhm5IqfKLBGMxtSBf1zH5M9LQp_MWbXvyDCO8oMN1ZzZQeDl2eZ52pDjUgxY7XynVxXV5WE5bMw0RTpSTqD9tUMiXrWPf0uTIzdLjqv0wtBPkty387TGl-NBgS1ini3ZGn_xsfFOGL7_MXA-xCpueMD0e4nN9zAIdyhE42QGSKV0uB3Tgtypxf4q_5h6TGEliLzwl-4x88-rzlsZILiErNCYwjZtL7cPYMiWfVjP5VYCyB0U1ujNgu7M2eJYD60KiF68LWe6wWPQjOdPViAP8m9BrQlCzqOiWnRo0tvuH1VZ9baV5j28vUwFLgM7XLPUmNz5UEZwWGv25IfWRCfaBCBu7uIAky082bNDzuoNDYg48jDjFNJWajItJdniPhaXuUjpoXE3LrBjKjfyX4V8McELNFgRi-eftHT7ZaQBDqQWMUH-3auIWLm0jnSwmdUmnZfrNLNytHiNREQY1mFYEO_J8qI4VQXAC34W0Gs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6983998d5.mp4?token=wBla5BbLopaBzQ7kHZweGJrlRe0m3o4shvuMNfdHirhJatWcKE_jFjge-b143T6USt3MSof3DdarHsPprFDwMktlbpDv_OhXW35Rs49rTJileFL9UAhvu2NeqFt_dNI-AJW7DYFMeqoRkbGeLBpyIIWStlkBjKFrCqoPtZQAQVjwswB_rmgXn6kA-FjvVDn7T6EWkhm5IqfKLBGMxtSBf1zH5M9LQp_MWbXvyDCO8oMN1ZzZQeDl2eZ52pDjUgxY7XynVxXV5WE5bMw0RTpSTqD9tUMiXrWPf0uTIzdLjqv0wtBPkty387TGl-NBgS1ini3ZGn_xsfFOGL7_MXA-xCpueMD0e4nN9zAIdyhE42QGSKV0uB3Tgtypxf4q_5h6TGEliLzwl-4x88-rzlsZILiErNCYwjZtL7cPYMiWfVjP5VYCyB0U1ujNgu7M2eJYD60KiF68LWe6wWPQjOdPViAP8m9BrQlCzqOiWnRo0tvuH1VZ9baV5j28vUwFLgM7XLPUmNz5UEZwWGv25IfWRCfaBCBu7uIAky082bNDzuoNDYg48jDjFNJWajItJdniPhaXuUjpoXE3LrBjKjfyX4V8McELNFgRi-eftHT7ZaQBDqQWMUH-3auIWLm0jnSwmdUmnZfrNLNytHiNREQY1mFYEO_J8qI4VQXAC34W0Gs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداشمون در یک دقیقه به ۱۳ نفر پیشنهاد رابطه داد و  همشون هم ریجکت کردن و تونست رکورد ریجکت شدن زیر یک دقیقه دنیا رو بزنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69927" target="_blank">📅 11:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69926">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
لحظه نابودن شدن خونه های مستحکم و نوساز توی کلمبیا بر اثر زلزله!!
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69926" target="_blank">📅 10:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69925">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=Stv_mSYYjzR09AzJ4zxfoD76YjPObUDMBueYAJkIo-a6I-yOEsuFLObi-AXrtwT5RlF4Trrk2ayyhXX_VzUfrsOILM_X5jbNTmcbf0-yJXqeTdicWJWi5NPppwJkFs3XBYhZw5UehtyBNBl8KfVZcve88ElhFHQQQ9Kn7X7hWItkdU3yuv0RGX1wOJCNG74sat4i_e6sngam8T8gyQrZgOs9Wzo_gqyp-eNOHrr7k2lIZYqi3FqASps7t9IZOAYOiI0NagPMejHlDQsj09bUqAkW0r8u8p-ue6lpisNmUwyLmfp3bJItj5mMCR-DCbd_gD2rCwJqcWpqu2KNjwlRxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ecf27139.mp4?token=Stv_mSYYjzR09AzJ4zxfoD76YjPObUDMBueYAJkIo-a6I-yOEsuFLObi-AXrtwT5RlF4Trrk2ayyhXX_VzUfrsOILM_X5jbNTmcbf0-yJXqeTdicWJWi5NPppwJkFs3XBYhZw5UehtyBNBl8KfVZcve88ElhFHQQQ9Kn7X7hWItkdU3yuv0RGX1wOJCNG74sat4i_e6sngam8T8gyQrZgOs9Wzo_gqyp-eNOHrr7k2lIZYqi3FqASps7t9IZOAYOiI0NagPMejHlDQsj09bUqAkW0r8u8p-ue6lpisNmUwyLmfp3bJItj5mMCR-DCbd_gD2rCwJqcWpqu2KNjwlRxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های یک مقام حکومتی رو ببینید که باخنده درمورد شلیک به سر معترضا صحبت میکنه:
ما به پای معترضین شلیک میکردیم ولی میخوابیدن میخورد به سرشون
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69925" target="_blank">📅 10:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69924">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tZ-F7KlFJ7XScrbeghwjetZMK6GKK95JUkiH1IZm64Y2CrM8uX5WLun2wx59wB1uAnjP1cDqOHgE3eDHmxXCBCwS2KWTIzjUM7094i68nrJyxlgpYiehFLqUp1wE8XWIl7D8GX6yKpBTdtmq5DdlU-B5d7sSNDnPCJsB_5zEuyTd1ZJ-E-moKLnOmODKa8B4Rxhtp9sBeQ1HpHche6ujA1HL7XF5W_lKVg943nSdDfmY-G1_nR-xk4b4bSb_eFO3VWnktxJp-mWp8knAc2f0CPRP81WrRWTttWdH_ero_jpdh61deOV1YLWXNYHAP3BP9lCGT8r53B9prF5kec7dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a54f6b8d.mp4?token=tZ-F7KlFJ7XScrbeghwjetZMK6GKK95JUkiH1IZm64Y2CrM8uX5WLun2wx59wB1uAnjP1cDqOHgE3eDHmxXCBCwS2KWTIzjUM7094i68nrJyxlgpYiehFLqUp1wE8XWIl7D8GX6yKpBTdtmq5DdlU-B5d7sSNDnPCJsB_5zEuyTd1ZJ-E-moKLnOmODKa8B4Rxhtp9sBeQ1HpHche6ujA1HL7XF5W_lKVg943nSdDfmY-G1_nR-xk4b4bSb_eFO3VWnktxJp-mWp8knAc2f0CPRP81WrRWTttWdH_ero_jpdh61deOV1YLWXNYHAP3BP9lCGT8r53B9prF5kec7dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:«بازندگان و برندگان انتصابات جدید در جمهوری اسلامی چه کسانی‌اند و آرایش جدید قدرت چه چیزی به ما می‌گوید؟
🔴
انتصاب محسن رضایی به دبیری شورای عالی امنیت ملی و حسین طائب به فرماندهی بسیج، دو پیام مهم دارد؛
یکی رو به بیرون، درباره مذاکره، جنگ و رویارویی با آمریکا
دیگری رو به داخل، درباره مهم‌ترین نگرانی حکومت: خطر خیزش دوباره مردم ایران.
در حالی که هنوز درباره زنده یا مرده بودن مجتبی خامنه‌ای و میزان سلامت او تردید وجود دارد، سپردن بسیج به حسین طائب، یکی از نزدیک‌ترین افراد به مجتبی، یک پیام روشن دارد:
نگرانی اصلی حکومت، خیابان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69924" target="_blank">📅 09:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69923">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=GDtstVzFlYS9q1WaO1FHSMSEtmEmdd6XW2Hdj-SXQyHrn-T-EUCdowTV4sNmn3iucvYLJEHzpduWA7TGSHq2V53eUlKcpKzHxZas1l6jvJLE49CulJFTRpv-K79hVNBF_IrFux3v7zXLDZwx7HYYwqw3H69Y0y4K8tm1OnLVNA4wB_hR1Y1aaWwOGAQiZnZVdSc5yDwDPCU9KtNXHniBvsMGRLjHBp8qALRwXi3vJZTYIyR7_lQOzZmRGYNGu8YMqOEyMM0t9g_9IpBX2FjFfNcMkvtlUmxBLRiOV0oASuLE9-xQKZoVMlAWWupmlK67VWJwz7I9ANrtsDlGgtrL7ajD1FHe8jVoIzIxfV0uMQAML9xy45c3NZWK-ZN3xCsX7tAoOM6KjVzOYmjFPMzwpPGFf6sx0fJ6GnThiJjyPpW7ZEFRHqwTI5yjP8QLiJqSHR49jpSuhPPznTAOK0s71y2uyOeYqV6U1Pxdb0lGiWqQAt2DSjZUkIrYE6r8vL9qaHRmPlBbHvAGGrCLJj9Im33l-vqI2aD7Mw2RGxm_mFqKMDdZ85adzvVznZtSqP4emD5raxfa757Ht-DmMdAyppzNTKC-yiUqjuwLPvMkUgU9SxbKVDYctAqeE0OJZudMMmVGlpjsRfeNbLda_VAoSq1onw2VaUZg-VZ1iGYCF0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa002b9fb9.mp4?token=GDtstVzFlYS9q1WaO1FHSMSEtmEmdd6XW2Hdj-SXQyHrn-T-EUCdowTV4sNmn3iucvYLJEHzpduWA7TGSHq2V53eUlKcpKzHxZas1l6jvJLE49CulJFTRpv-K79hVNBF_IrFux3v7zXLDZwx7HYYwqw3H69Y0y4K8tm1OnLVNA4wB_hR1Y1aaWwOGAQiZnZVdSc5yDwDPCU9KtNXHniBvsMGRLjHBp8qALRwXi3vJZTYIyR7_lQOzZmRGYNGu8YMqOEyMM0t9g_9IpBX2FjFfNcMkvtlUmxBLRiOV0oASuLE9-xQKZoVMlAWWupmlK67VWJwz7I9ANrtsDlGgtrL7ajD1FHe8jVoIzIxfV0uMQAML9xy45c3NZWK-ZN3xCsX7tAoOM6KjVzOYmjFPMzwpPGFf6sx0fJ6GnThiJjyPpW7ZEFRHqwTI5yjP8QLiJqSHR49jpSuhPPznTAOK0s71y2uyOeYqV6U1Pxdb0lGiWqQAt2DSjZUkIrYE6r8vL9qaHRmPlBbHvAGGrCLJj9Im33l-vqI2aD7Mw2RGxm_mFqKMDdZ85adzvVznZtSqP4emD5raxfa757Ht-DmMdAyppzNTKC-yiUqjuwLPvMkUgU9SxbKVDYctAqeE0OJZudMMmVGlpjsRfeNbLda_VAoSq1onw2VaUZg-VZ1iGYCF0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
من به ایران اعتماد ندارم. من آخرین کسی هستم که به ایران اعتماد می‌کند. آن‌ها مدام به من دروغ گفته‌اند.
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آن‌ها کنترلی ندارند؛ ما کنترل کامل داریم. آنجا در اختیار ماست.
و شاید زمانی آن‌ها دست به کاری بزنند و آن‌وقت نابود خواهند شد. اما فعلاً در موقعیت بسیار خوبی قرار داریم.
ما با کشوری سروکار داریم که ۵۰ سال قلدرِ خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال می‌شود، مگر نه؟ ما چهار سال بود که می‌گفتیم ۴۷ سال؛ و حالا دیگر آن‌ها قلدرِ خاورمیانه نیستند.
🔴
ترامپ درباره تغییر هواپیما در آنکارا:
این موضوع صرفاً به «سرویس مخفی» (تیم حفاظت) مربوط می‌شود. من فقط از تصمیم آن‌ها پیروی می‌کنم؛ بنابراین تابع نظر سرویس مخفی و ارتش هستم.
آن‌ها می‌خواستند که من با پروازی دیگر و هواپیمایی متفاوت سفر کنم ــ که از نظر ایمنی تفاوتی نداشت ــ اما چون خواستار انجام این کار بودند، من هم پذیرفتم. من هر چه آن‌ها بگویند را انجام می‌دهم.
گمان می‌کنم تهدیدی وجود داشت؛ البته من خیلی پیگیر جزئیات آن نشدم. من با تهدیدهای زیادی مواجه می‌شوم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69923" target="_blank">📅 09:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69922">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69922" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69921">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IMji__YcFJlviLGTI_s5j7bEjpZ5-2ZstFa9XPTpc8mj2gnY_yYHf3lkxbxZXFrex3F5s50PcMX-JgQ9bUJ1h9HFJS2qUbg3IzHOSt343eblKxTMmgP8Mt1LpsQVHQ51iw7S9DTvbvIfXnI2EacAlDOl9mFyp3LljYHywsMCpVtSIsszw4gH2cv7hRjm4DqUR-K-wn0bvKFj3I0I4isu6Mz5TdzTGU1a-b8uCE4Xc68g_LT53MX-EFNCMSwdpXYkZtWX1gpI9xZLhisOrwdFa0_ds4i4ZFpQILrbh8Q9djPen1vFu7Ic0Q2u28bNxYtTKTp6kFkk2RW2rTdi3W7TaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=IMji__YcFJlviLGTI_s5j7bEjpZ5-2ZstFa9XPTpc8mj2gnY_yYHf3lkxbxZXFrex3F5s50PcMX-JgQ9bUJ1h9HFJS2qUbg3IzHOSt343eblKxTMmgP8Mt1LpsQVHQ51iw7S9DTvbvIfXnI2EacAlDOl9mFyp3LljYHywsMCpVtSIsszw4gH2cv7hRjm4DqUR-K-wn0bvKFj3I0I4isu6Mz5TdzTGU1a-b8uCE4Xc68g_LT53MX-EFNCMSwdpXYkZtWX1gpI9xZLhisOrwdFa0_ds4i4ZFpQILrbh8Q9djPen1vFu7Ic0Q2u28bNxYtTKTp6kFkk2RW2rTdi3W7TaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69921" target="_blank">📅 01:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69919">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=CDjHmWIMNl80RjVBGXHog3qk2fHnCf75eCwNoJVMPO-m0enE2_cSRU-eNnBjkxJ49p5v3YHFqlqFbmCuV1pFtKXj19jI_MjuJ6fIYPhlG2GRG3VRKO_3xUkSG_6Ww953IWjDzOI6Wzx17JnMe4ak9S6vxxB5nhq1x-WJw2R88p8MuKF8gp0ZCTyd_qIYBoyfuLZgvZ0Hu6TlYo5Ajn3tV0Mti-ubXYrUzzKOUC7vFDV6t2MrsINWwVzh8djrDB6ZxGeEccGx4II5Fw-vHPEvbiQCxWqr85iJVTP4Enyi4iUFgUaS6f903FVGebJEN0tUs8lETYoGf9TWbClrEWt8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c53c5d72.mp4?token=CDjHmWIMNl80RjVBGXHog3qk2fHnCf75eCwNoJVMPO-m0enE2_cSRU-eNnBjkxJ49p5v3YHFqlqFbmCuV1pFtKXj19jI_MjuJ6fIYPhlG2GRG3VRKO_3xUkSG_6Ww953IWjDzOI6Wzx17JnMe4ak9S6vxxB5nhq1x-WJw2R88p8MuKF8gp0ZCTyd_qIYBoyfuLZgvZ0Hu6TlYo5Ajn3tV0Mti-ubXYrUzzKOUC7vFDV6t2MrsINWwVzh8djrDB6ZxGeEccGx4II5Fw-vHPEvbiQCxWqr85iJVTP4Enyi4iUFgUaS6f903FVGebJEN0tUs8lETYoGf9TWbClrEWt8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی یک مخزن در اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69919" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69918">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=MPkT01P9kMxQDzpx_2urqEA9dkfwtNxXmY50fx62nf9WVPlHunFdEqbJtRHZBr3Pq06gleWyTa7NLMrXOeh_OC7uiztos-zwxwcLBwadcwMJP_aG66yQxu8-oahGgymHypRz4oWALZ12axjMSs1c6eYytCX0uLUhJdF6ANuJRyPjUtLhwNtoo7Gx6K2sxBblRO4sEm-NYoRjJb0J6y1Pdip8MYRcxRvFXwbEOzW2JWGU6zbSsy_GfoZnZ-aYmdvMF7GMkZy-eOTVafZ1i5EmdCYuPEZyC3jgYquZ_Of4Kto3eUJ0hXFWB2OqOCPcbQQsQxBaT_KNV_OHQcjScioWZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c665ef2ed.mp4?token=MPkT01P9kMxQDzpx_2urqEA9dkfwtNxXmY50fx62nf9WVPlHunFdEqbJtRHZBr3Pq06gleWyTa7NLMrXOeh_OC7uiztos-zwxwcLBwadcwMJP_aG66yQxu8-oahGgymHypRz4oWALZ12axjMSs1c6eYytCX0uLUhJdF6ANuJRyPjUtLhwNtoo7Gx6K2sxBblRO4sEm-NYoRjJb0J6y1Pdip8MYRcxRvFXwbEOzW2JWGU6zbSsy_GfoZnZ-aYmdvMF7GMkZy-eOTVafZ1i5EmdCYuPEZyC3jgYquZ_Of4Kto3eUJ0hXFWB2OqOCPcbQQsQxBaT_KNV_OHQcjScioWZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اولین ویدیو منتشر شده از عروسی رونالدو و جورجینا:
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69918" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69917">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=VJDvgNFKSgOPEGDIMbx6aUoEedqNPCh5ZzAScX9g34BsalSP9aBx0qddY1dQ6iS8965PU8KsOmHztCzy_kq89y0zJ2HRF0RTV4GNWEtMKDNvTJYa1WdWZev4kcmqF_qBfdzY9rgZO218IvtHFM3iF5Nqh_MhqTt_YlUevo-jNrDInWVx5vcPXUibcG5lHU-r_mLNjc6OmDJue-wkQW12Zg7bgiq6Z6jhqAlaB4-drmDMohmqmo55xX_SlkhFufGDJcufuBGvWKTDUI1iHingAD2bCBCdZXnH6fD5xXnHCJGEmVWtmbse8paKml54MXzGSwRUrWEL8Y1aepYuwdu49Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bd3b48d.mp4?token=VJDvgNFKSgOPEGDIMbx6aUoEedqNPCh5ZzAScX9g34BsalSP9aBx0qddY1dQ6iS8965PU8KsOmHztCzy_kq89y0zJ2HRF0RTV4GNWEtMKDNvTJYa1WdWZev4kcmqF_qBfdzY9rgZO218IvtHFM3iF5Nqh_MhqTt_YlUevo-jNrDInWVx5vcPXUibcG5lHU-r_mLNjc6OmDJue-wkQW12Zg7bgiq6Z6jhqAlaB4-drmDMohmqmo55xX_SlkhFufGDJcufuBGvWKTDUI1iHingAD2bCBCdZXnH6fD5xXnHCJGEmVWtmbse8paKml54MXzGSwRUrWEL8Y1aepYuwdu49Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر محمدرضاشاه پهلوی درباره نفوذ لابی یهود در آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69917" target="_blank">📅 00:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69916">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lrr2-uAXNwvaoqh66oHVo1CQtWlmHTiFJXBiqu820SyqTqouNDJ5QqxG7VXYrozY3HIXoQVid32KhMWGW3EwNMWU1aP9PPevWMVKIKUjw6-6jIGObSPRxd5yoQiLl7S5bGcaJvQm_EN5bFHJkgjQMnm0xTVQFT2AdnrYqIt3_8bA7WJ6zfNU53BfuVYrp-H7pacFGCZlp96hHR_ldedN_NZCMUnN8YhDZKKoAnxz3Gmw8PZ_E0EBD_W9kpNXND0G8aGFOjvZEllsNnGnXuuLNufMglWrrPp1tmZU5W5O39wL6rALYgEsFOiuYq8SZQOzmFJKXkwEM0s-AQkgqYcF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو و بانو جورجینا رسماً ازدواج کردن.
رونالدو هم گردن گرفت بالاخره، دیگه وقتشه تو هم گردن بگیری
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69916" target="_blank">📅 23:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69915">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=UXSce1fnygdLNIyfCs7ho4gKv6JtN76hz45rOhBBOIG4E7yLIfSyyT8MY1LQ8Ydl2PR6uop00_bEj3xgRh31rMlMMYMFZtviS6LXoZbGQXvzudvaysTmNP8Balinw68Wb20-7c1pLJ117V3ubTGR08wtyLIaiLq4DLDfUou5CjArerpicL23jXt87RUImyOSkmm0KDG9wp7WWMCJDpmA98DvNJeDVBMZhNRfQ_BvkyELU-mbtAOQt94YtlNQfx4W5Wfr5aM7muG78qMgiA4yPj-iCjWmO1no7f1_pkWue-1d0C9_DjlGj8_7PtsV3co9LmHuYGKD0JITwTlop6BmFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1d1d4e3c.mp4?token=UXSce1fnygdLNIyfCs7ho4gKv6JtN76hz45rOhBBOIG4E7yLIfSyyT8MY1LQ8Ydl2PR6uop00_bEj3xgRh31rMlMMYMFZtviS6LXoZbGQXvzudvaysTmNP8Balinw68Wb20-7c1pLJ117V3ubTGR08wtyLIaiLq4DLDfUou5CjArerpicL23jXt87RUImyOSkmm0KDG9wp7WWMCJDpmA98DvNJeDVBMZhNRfQ_BvkyELU-mbtAOQt94YtlNQfx4W5Wfr5aM7muG78qMgiA4yPj-iCjWmO1no7f1_pkWue-1d0C9_DjlGj8_7PtsV3co9LmHuYGKD0JITwTlop6BmFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
روحانی:
صدام پس از کویت به دنبال عربستان و امارات بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69915" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69914">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇺🇸
سنتکام اعلام کرد نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۵۵ کشتی تجاری را بازگرداندند، ۳ کشتی را غیرفعال کردند و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69914" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69913">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8iA6IdOfD0cjxETahUVeIq4e1x6Bp5t8P8ECMqHV6E7YJvrdHAlJes9bas5tLLo0d5attdZq0b9i_budojYjm4zVpiQ9wglxXqiH5FCbBk3kb3hM9ogAv4LDB4lJktR5rFDIdF2WfdIGY4dx9qCLe-mQPn3X8GNLwrAQWkeyw7ueDxRHqbIdNiKWHi5cqmwr7bjUfaAurhXIFXn2YXNpkuE48zsHIBef7hn4tvpmSI6OUbncqIHwacMCu_GwOhUsKUFqwo5YndXOlzbmYa6cJtYI76B7nRzBJyEhHQP4aqvUzdzsXV03vLEfb1hN312XlCSXrZ7JzjucM3No4fkrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
وال استریت ژورنال:اسرائیل دولت ترامپ را در جریان اطلاعاتی قرار داد که نشان می‌داد توطئه‌ای احتمالی برای هدف قرار دادن هواپیمای ریاست جمهوری با موشک‌های زمین به هوای دوش‌پرتاب وجود دارد.
مقامات امنیتی ایالات متحده متعاقباً پس از اجلاس ناتو، رئیس جمهور ترامپ را با استفاده از یک کامیون پذیرایی فرودگاهی در آنکارا به یک هواپیمای نظامی جداگانه منتقل کردند، در حالی که مارکو روبیو، وزیر امور خارجه، دیگر مقامات ارشد و خبرنگاران به عنوان بخشی از یک عملیات فریب در هواپیمای ریاست جمهوری باقی ماندند.
در نهایت هیچ موشکی شلیک نشد و هنوز مشخص نیست که تهدید گزارش شده چقدر معتبر بوده است. این عملیات اولین باری بود که چنین اقدام فریب‌آمیزی در دوران ریاست جمهوری ترامپ استفاده می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69913" target="_blank">📅 22:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69912">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=gAd69SGVVkPgxcnO-LhCbAMDrF2loDqjJuo1_2222ovfJO4-HYVp6W0gpjjJiXDOGQFmg7iCOovpdGTJyweD6lNs9-gptcRwaccO-y-Q3HE2S4rd59fCYWO8ejH1tZMTuvLTtR1TkXgntTMQyAg64fZ02WeGcp5cg04-dsV1uxa01egpZAqngQBmgcSLoXs-EBPLgBxMBxgO5uTzQ8oVAoEfAYPeFLNaYiGs3Og78vfLnjd5TK09xxR8HCOv99uT1g1AdBUVCJftZjE-sI9BdbFsDZUy0YRlUtC9dDSvRUjRnlfyOEu41Ii2vlx2Id3XVRn2swyQjxT5g6BQJ3Hesia_wiPtBaBkjk3L8a4kcF4QzwoaLFOaOPcrQ4IackilJ9uu57YIOOKXV82dEDotsbEglDctMdrWmH9WUfqQwN8yB5iyKxhOqyu_amFaQEGLwzNI9VYkRkM6eq74Ev_kQtst8i64AyiUeZ7cKkoxm6_VJG18TdFlWqNoQcQKMZzYhVtPmlYSAA1swliHxnVa9V9Qe3En36WbP6A1Js_pWRdop_D4VJeVGirfAjdIrjSWN5QVcRHpq-9RQvsCYizKQiqTg8lZKTDtKmMMYdrPMb3oNURXLcU05s1xDAe_E6QPPUK0VeJJIl4zhfXJ9SoRy3wEatUSRzeb9xPQ3GG9T6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=gAd69SGVVkPgxcnO-LhCbAMDrF2loDqjJuo1_2222ovfJO4-HYVp6W0gpjjJiXDOGQFmg7iCOovpdGTJyweD6lNs9-gptcRwaccO-y-Q3HE2S4rd59fCYWO8ejH1tZMTuvLTtR1TkXgntTMQyAg64fZ02WeGcp5cg04-dsV1uxa01egpZAqngQBmgcSLoXs-EBPLgBxMBxgO5uTzQ8oVAoEfAYPeFLNaYiGs3Og78vfLnjd5TK09xxR8HCOv99uT1g1AdBUVCJftZjE-sI9BdbFsDZUy0YRlUtC9dDSvRUjRnlfyOEu41Ii2vlx2Id3XVRn2swyQjxT5g6BQJ3Hesia_wiPtBaBkjk3L8a4kcF4QzwoaLFOaOPcrQ4IackilJ9uu57YIOOKXV82dEDotsbEglDctMdrWmH9WUfqQwN8yB5iyKxhOqyu_amFaQEGLwzNI9VYkRkM6eq74Ev_kQtst8i64AyiUeZ7cKkoxm6_VJG18TdFlWqNoQcQKMZzYhVtPmlYSAA1swliHxnVa9V9Qe3En36WbP6A1Js_pWRdop_D4VJeVGirfAjdIrjSWN5QVcRHpq-9RQvsCYizKQiqTg8lZKTDtKmMMYdrPMb3oNURXLcU05s1xDAe_E6QPPUK0VeJJIl4zhfXJ9SoRy3wEatUSRzeb9xPQ3GG9T6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
پرواز بالگرد آپاچی۶۴ آمریکایی در نزدیکی قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69912" target="_blank">📅 21:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4Ues5hFAswTF_5NON7ns1vcZ-k7ZGTfmPeeuQ1jUyaOrhp0xgLbYiRNHP6v-OXZiE5GgBKUH-S6ZTM7vmdL9CpitySNdTGJGz2bkUjCchELxxF-wr99jXMyB_xJcOcsm6B1K4o7BIlL8uc-dfeOqXiG0tgItl1OuLAp_Xl9gjLx7o5QssmRgsil4kXP_6J4nQCbaQmnxydd2eGkAZgEE6Zevdb3Pl8be-mAW7MnZT_q2uQqID6UVTfpCcVyveSXWycFffMnrrc3pJPKONgJdW6e_5DMVXPfg3lPUOx8RioeU8xvVx6B8SBUjdGQ4ROscLxJ_EB8axbIFDMb9RqtGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qv80zNPmg5Ubj5fh6i04tpv-NWRq7h-daejE0gA7SRMLOS5hiLJ0oao5mqbBxlYogGyd908WCz6YJ9EBjQ6-N1HCEkBL6kS3mQxwFeFiC9jUNMDip8Satn4ed7BsRHBuPccizckY-TUOrhKFWrfnW659FJQe3RItgsWgQ2KXMt_Hn2I_L3g-yNOhTs34VsQ5xmfF-lsUpIayGQ1LxNt7wzYUOmXpMCsJsVF-JqJldJn_TF8_8tIwPZk2G6x1u6KJ_WwiSZs6xCx1ZGJk1tIo3OZTMQkuTQB-KOWDEcN8aPImMc1WHOrv48tmI9LQVX2U_mAuQ-L9473iH9gJMwAvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZCt2zm2hq_WTPx2lNqZUhyl_vtvc7N8siSbXvC79-qSJgbV6ofv1da8_GupOMlRZ6ZJWGn-fOoFrJFTNh5YbqY-IvyGN88YFWgli1hg-QuENrV0gTlU9O9F6rZYSoFH-6ijuR7oGxd1wVQ9CaNAlVi-r1fSmsy241YBYz-zQg8VLmzaFk0QLWp63U4cd_SAdJztqdzts9O8ZBS6zGaMyNudEPxeX-CLEEytdS1HwmaOrHiKQTrbLTYzQ2umeAtxc4mmQwqMCbv7mkI2MzIQLbjIshyZf3EClrjup06XK8OfjQMfeT6DBlLl6Go2q_84YUdtN87GgbIadZ3e5OsDpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=VDVqTayBH3t4cGOu4hM6nXIUnydOcUODBTcu6h3EXS_qD40IF2MAm-2oYrChPjdRhIjhZl67Ju6Jc_GmDrqlGZMNE7xdb8vDpPsKhO6ffPsBRcNQJx7h2LwblakJho_3nyA5aatVnDlcZS5jxYbZPQ9ET-MYrdCFt3QfqAnXG5bwHtMAgS1OLMU5hurmnqJjlvQGJqnvF3Z9GZBQi2ltrXwvI2ulO39bTDeIR7adNitvaPZPya3ItJrq_ae6cHzxNIP2gb7NS1j0opqyiafULasQprVquSQxpMpN-aSQ7bU4YWBFAiUDMWn6qbNHjwR23CCDpvERAbh4OMbs5zB0Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbe5c4282.mp4?token=VDVqTayBH3t4cGOu4hM6nXIUnydOcUODBTcu6h3EXS_qD40IF2MAm-2oYrChPjdRhIjhZl67Ju6Jc_GmDrqlGZMNE7xdb8vDpPsKhO6ffPsBRcNQJx7h2LwblakJho_3nyA5aatVnDlcZS5jxYbZPQ9ET-MYrdCFt3QfqAnXG5bwHtMAgS1OLMU5hurmnqJjlvQGJqnvF3Z9GZBQi2ltrXwvI2ulO39bTDeIR7adNitvaPZPya3ItJrq_ae6cHzxNIP2gb7NS1j0opqyiafULasQprVquSQxpMpN-aSQ7bU4YWBFAiUDMWn6qbNHjwR23CCDpvERAbh4OMbs5zB0Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛  با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]  وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد  @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69908" target="_blank">📅 20:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69907">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=GDAb3PLrKQW5fhvI-pEU-NyOTkmpnSSoDgVQg1y-TLTw0ZRo3MTsV8QU0gSbsLjpVLPJ9Dxoa-pLs5FVgfpDzSPtdBzkbIHs1Y0TS7UXYBW-Q2lJ58a9wqvTBVByd_K2RtJAgJfjCkclEupTK_qAj1XzVLa1K2kK9CBo6D7Ri8Y1vEXYZMsuPmYmaANi79KFOwtnRph_tTECIRdmCZ6eh3gO9PnP2YFZWC9adb9v6ds48RUtBGrah3Y1dBNmehmr1LHR8FNj5HuKTsXRU_DNVT5A-X_GOBKl1euuEMKssrVnr6ws-dcChlm4_jm9N5yzZO_qv4iD0BPYBku688Pnkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=GDAb3PLrKQW5fhvI-pEU-NyOTkmpnSSoDgVQg1y-TLTw0ZRo3MTsV8QU0gSbsLjpVLPJ9Dxoa-pLs5FVgfpDzSPtdBzkbIHs1Y0TS7UXYBW-Q2lJ58a9wqvTBVByd_K2RtJAgJfjCkclEupTK_qAj1XzVLa1K2kK9CBo6D7Ri8Y1vEXYZMsuPmYmaANi79KFOwtnRph_tTECIRdmCZ6eh3gO9PnP2YFZWC9adb9v6ds48RUtBGrah3Y1dBNmehmr1LHR8FNj5HuKTsXRU_DNVT5A-X_GOBKl1euuEMKssrVnr6ws-dcChlm4_jm9N5yzZO_qv4iD0BPYBku688Pnkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
رامین رضاییان:ما خودمون از عمد به بلژیک گل نزدیم و تیم بلژیکو نبردیم.
🔴
چرا؟دلیلش:
جلوی بلژیک شما دیدید مهدی طارمی یکاری کرد تیمه ده نفره بشه.
مهدی بخاطر تیم به بلژیک گل نزد.
من باهاش صحبت کردم داداش چرا نزدی گفت داداش اگه گلو میزدیم فشار وحشتناک میاورن و جبران میکردن، حقم داشت مهدی
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69907" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇮🇷
فیلد مارشال محسن رضایی دبیر عالی شورای امنیت ملی:
آمریکا باید جنگ رو پایان بده و خسارات رو بپردازه.
به هیچ وجه کوتاه نخواهیم آمد.
تمامی جنگ ها باید در کل جبهه مقاومت پایان یابد چون شرط اصلیه.
شروط دیگر را نیز از طریق میانجی ها گفتیم به اونا ک باید بهش عمل بکنن.
توافق با عمان ربطی به باز شدن تنگه هرمز نداره.
پول های بلوکه شده باید آزاد بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69906" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69905" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n--r724nC1FTy7LF6v-jHo2SG69BAVwvodc3UrbwTrJ5vDICPA9n5uXOQNXH6_2w-OqSEadXHT0ZcdwgCdTNmKXcpENqy1Hre9n-7igrdewrlhbVuyO0RdFoJTx2j5TCHbnCpXzWKNG1IuOgiw5Op44AZY0szXw7PTt-5WWRE7zDRg3oVEVt4iYOxdkPX78s_qTCFDcSRfL5x8FNh_qqRz7rwncX1JstXgCgBxCxRwGRwgQb-yX2RbhBVRmb_27-xHRxl5iNHpT88j0MmdfqFB6XuxGj_phlQwCxuB0M4Y_e-Q-NAafGk3a07e0-epVgqyiLDTKVyvFCFl2k2yqHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69904" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=lBV4ToCv3YuwX4SYEqBs8ci3i00nrf4N28m1W5VKRrl9W8kvtCwG7-P5FjmEwmWybXgeWe0zX3xAxZ69RR3bvgja2kG7aoo10R3tx_LXft_4DYA0zT8vtWrQbvaVO9qC9ZJ3RpquQJ-AdpBNgwRVysUrQnEwKUtayVKPlccFcftMCa4-o2Xy3UX97C6ZBwYrMJkzwmvbKLmEZ0LbtNwNqwDkCxfgutpLeivFFFQzpvVNY1ewY3oFiQSGAqNT4BdHSYXbqpjb09TEkzPdyFDLgKa-RuIu-cobGPPS6Tgu5tFmrtBSa5z5TIp4ODZjvodadUP_q1-vx4I_P09qhY_aFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=lBV4ToCv3YuwX4SYEqBs8ci3i00nrf4N28m1W5VKRrl9W8kvtCwG7-P5FjmEwmWybXgeWe0zX3xAxZ69RR3bvgja2kG7aoo10R3tx_LXft_4DYA0zT8vtWrQbvaVO9qC9ZJ3RpquQJ-AdpBNgwRVysUrQnEwKUtayVKPlccFcftMCa4-o2Xy3UX97C6ZBwYrMJkzwmvbKLmEZ0LbtNwNqwDkCxfgutpLeivFFFQzpvVNY1ewY3oFiQSGAqNT4BdHSYXbqpjb09TEkzPdyFDLgKa-RuIu-cobGPPS6Tgu5tFmrtBSa5z5TIp4ODZjvodadUP_q1-vx4I_P09qhY_aFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت تلخ یه فرد نابینا:
اینکه من نابینام به عقیده پدرم کارمایی هست که دارم بخاطر کاراهای اون پس میدم.
پدرم وقتی جوون بود نابیناهارو مسخره میکرد و بهشون میخندید.
مثلا پدرم بهشون میگفت بیاید جلو بیاید جلو و وقتی میومدن میفتادن تو چاه و پدرم مثل خر بهشون میخندید.
پدرم بهم گفت من این کارارو وقتی جوون بودم انجام میدادم.بعدا وقتی تو دنیا اومدی دیدم نابینا شدی و این دلیلش کارمایی هست که من باید پس بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69903" target="_blank">📅 19:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69902">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=gaqcS0XPEtiPgsyjycYFtiQ_ZEkC1CBzZTTkX-59kt8S5R0RmdYNHfRLl9XacQTUbS4LLNQ_8xrRMbxdvx4XoUxOl0kSER2D92LVsGX00Yv8O_pLaoufxEFt_IelU1ozXd4TYx9RJSlcB4D5co8Z-r7lXUIsCfNhVeXbMGAnV2nVhrTpJHxzUsrpjUwTYTDcCwmCYyIOp1bL98ig3fkK9wvMGSCehekXFkfZmpD9eVPfHP1BbTCVQU3YKTmNVGf-8K9VJFsAKXJoyjbM5AZ8qtlnucfZq3LEM-fawODwvMjylCqj5hjeq2y4BaZWrOChJXlZPG4pEOdSHM8tgvnUXCIX9yZn2x2MF9Gr5wzfDh3taaqox9PRdY-fHNX-7a1_Yc-d11cvO5QmIXvu9UJtCVj_jeH2M7SOqaadmAB30rLw4N-USyjChd8mhaQBGL3lDfmQ2GRnmnfMhkHoctL9m5ubUQXfLtA4Z8SPhGupO0jslnS0BbntpmQkrOgT4v2t0_UB9exP5egwrWfrsh1WNdF-_rx950fOJx-MZ7gD0d6J91rx36SLwODhWlTGz7p09KqQAy8vi1djpiQdZmAiWy_iSkjQATxktOTYERqT4vJj-WIf4fhtSx8oomWcvq2LmOHpEDsK6ErjOKujuL_JikB3VYTIYhYXFmrEts4TvKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=gaqcS0XPEtiPgsyjycYFtiQ_ZEkC1CBzZTTkX-59kt8S5R0RmdYNHfRLl9XacQTUbS4LLNQ_8xrRMbxdvx4XoUxOl0kSER2D92LVsGX00Yv8O_pLaoufxEFt_IelU1ozXd4TYx9RJSlcB4D5co8Z-r7lXUIsCfNhVeXbMGAnV2nVhrTpJHxzUsrpjUwTYTDcCwmCYyIOp1bL98ig3fkK9wvMGSCehekXFkfZmpD9eVPfHP1BbTCVQU3YKTmNVGf-8K9VJFsAKXJoyjbM5AZ8qtlnucfZq3LEM-fawODwvMjylCqj5hjeq2y4BaZWrOChJXlZPG4pEOdSHM8tgvnUXCIX9yZn2x2MF9Gr5wzfDh3taaqox9PRdY-fHNX-7a1_Yc-d11cvO5QmIXvu9UJtCVj_jeH2M7SOqaadmAB30rLw4N-USyjChd8mhaQBGL3lDfmQ2GRnmnfMhkHoctL9m5ubUQXfLtA4Z8SPhGupO0jslnS0BbntpmQkrOgT4v2t0_UB9exP5egwrWfrsh1WNdF-_rx950fOJx-MZ7gD0d6J91rx36SLwODhWlTGz7p09KqQAy8vi1djpiQdZmAiWy_iSkjQATxktOTYERqT4vJj-WIf4fhtSx8oomWcvq2LmOHpEDsK6ErjOKujuL_JikB3VYTIYhYXFmrEts4TvKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از لحظه حمله آمریکا به پل B1 کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69902" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69901">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:از شیوه مذاکراتی ایران ناامیدیم.
ایرانی‌ها بازی فریبکارانه‌ای با ما در پیش گرفته‌اند: در اتاق‌های مذاکره موافقت می‌کنند، اما در رسانه‌ها [توافق‌ها را] رد می‌کنند.
ما از هیچ کمبودی در ذخایر موشکی رنج نمی‌بریم.
ما می‌توانیم با نیرویی عظیم به ایران ضربه بزنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69901" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69900">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=HVdf5lOCW1taW856IblmxoFfmQbEUFIZlT_uR1mVB81lGCTtDBaDRmBq06ut9sE7UYU78FLIvt2FGvPeSoSc5CG7qkRm_8mptReDW0CKdLSFlbS48WIELClWwvtaLvus9ahnuZTc-ggWJWfbEvg_O2LeUUvpX9OFruY3r4mcWh-hNvttHnJVG7xWVKSrDjaRG4xn_K3LXT5JUVjD5OoZGGeeY2HNxvss1o0X1ACxhmuybyZ9Iw3whGd-sqdx2NAQ0gjYV4mIySiyMxTEdoHDjyJLZQ7ixGwKYFlgd6fVLPPc8KUeSOr9KBRjzLWAbWQpbeXmSawG49Y37BOpwmPzyWvrha0P02cIVH19B3eNmuY96oeZsbK9wzR5ng-hJhAFvLE8IgnwniD7fbRqgzoiYZjspoBvQ5kTRY2Z0f0h_1FN2VNcwwCw45YcdS5oLTi2iHdUjjqt_2T5AokqcofnTt0PCYx0I7J04UghnWTjsQ14KgePWqdGElqwwZTAEBkRIYWiJ9I7YbJo1So0HEU3BvJJjgM8lNNKdTNqSCG7YZTTEHj9GmoS3EWi75_4EyWpdPln1STY7Icvz1gjmL5UpKe1NOmqKsWunpp0jAbYTTWwJ-VRuVbkPkY0PznqZgnm6YIjSGsf23Iir7iYY8o3HHRm4-zzVuGPY0axeZa099M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=HVdf5lOCW1taW856IblmxoFfmQbEUFIZlT_uR1mVB81lGCTtDBaDRmBq06ut9sE7UYU78FLIvt2FGvPeSoSc5CG7qkRm_8mptReDW0CKdLSFlbS48WIELClWwvtaLvus9ahnuZTc-ggWJWfbEvg_O2LeUUvpX9OFruY3r4mcWh-hNvttHnJVG7xWVKSrDjaRG4xn_K3LXT5JUVjD5OoZGGeeY2HNxvss1o0X1ACxhmuybyZ9Iw3whGd-sqdx2NAQ0gjYV4mIySiyMxTEdoHDjyJLZQ7ixGwKYFlgd6fVLPPc8KUeSOr9KBRjzLWAbWQpbeXmSawG49Y37BOpwmPzyWvrha0P02cIVH19B3eNmuY96oeZsbK9wzR5ng-hJhAFvLE8IgnwniD7fbRqgzoiYZjspoBvQ5kTRY2Z0f0h_1FN2VNcwwCw45YcdS5oLTi2iHdUjjqt_2T5AokqcofnTt0PCYx0I7J04UghnWTjsQ14KgePWqdGElqwwZTAEBkRIYWiJ9I7YbJo1So0HEU3BvJJjgM8lNNKdTNqSCG7YZTTEHj9GmoS3EWi75_4EyWpdPln1STY7Icvz1gjmL5UpKe1NOmqKsWunpp0jAbYTTWwJ-VRuVbkPkY0PznqZgnm6YIjSGsf23Iir7iYY8o3HHRm4-zzVuGPY0axeZa099M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رونمایی صداوسیما از «قوی‌ترین سیستم جاسوسی جهان»
تماس با پذیرش هتل عمان برای جاسوسی:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69900" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69899">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=rRyx8nKNezQKmuvptq4YyGmeYQBu4jCQCZrwCGI6IJfpxFaRcaXIVG8M1QJ9WF_CgFmSxlkhxHWmYnC9z4JzaH0hg3t8_OC_nTBDU8zQfRJmPW8UiIVnPZQWzF9ht1qjpQrHSqQA8TxKK-CpSmSecFUBjKygVZk1j8cmMuwc7AvxCZnqtQpV2mDbNwRzNS_EEVs_oXoLuLCw0kkPQgUp0xCL_dE16RfegF_VtTvlPl5PxAfzbxpUyjl0uZ8eweM_PGM06_k0dTdUISVHGFPzuYpynLG15VMmYjlKxdZyYXq2mnd4_7CTuRQXNFuAWpa20pyUN9s-Qbk7XOAdoKAFag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=rRyx8nKNezQKmuvptq4YyGmeYQBu4jCQCZrwCGI6IJfpxFaRcaXIVG8M1QJ9WF_CgFmSxlkhxHWmYnC9z4JzaH0hg3t8_OC_nTBDU8zQfRJmPW8UiIVnPZQWzF9ht1qjpQrHSqQA8TxKK-CpSmSecFUBjKygVZk1j8cmMuwc7AvxCZnqtQpV2mDbNwRzNS_EEVs_oXoLuLCw0kkPQgUp0xCL_dE16RfegF_VtTvlPl5PxAfzbxpUyjl0uZ8eweM_PGM06_k0dTdUISVHGFPzuYpynLG15VMmYjlKxdZyYXq2mnd4_7CTuRQXNFuAWpa20pyUN9s-Qbk7XOAdoKAFag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
مشاور قالیباف، مجید شاکری:
هیچ کس نمی‌تواند با ترامپ به توافقی برسد.
این تیم فعلی با هیچ کس به توافقی نرسیده است.
او هم با ما به توافقی نخواهد رسید.
همه فقط در تلاش هستند تا "تحمل کنند و صبر کنند" تا پایان این دوره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69899" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69898">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=hb63dC5aVNgBByFxJafy182yuz9Wq3lWA6i7d_oLEC82NOpLeImwQ5d-rE4z90ERZotp_4_OAFI9_4t_sU7HioHREEDKqBREz7DkJ1-H9im7uu2h9-RUeJu4kmcSvA6ql4s7vsVgW8eWVfI8Ls3m4h8dPjd__vlY44B6hJ0qmEo7mCI-WwwEDwwHkArVxroNk8aNl0yZBDagpyzwZInbf-32QNclLrcbka7_Ek34-KqqYtmx9EHlm9Kf14sCjzN3w9I_YZECCiHBAPvoj1nOydv6wnkPZW5iKP3zW3ljIYT36IlzWWA1UQmDXmNFLL0a09O61p9FPqgZVnYLF35sbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=hb63dC5aVNgBByFxJafy182yuz9Wq3lWA6i7d_oLEC82NOpLeImwQ5d-rE4z90ERZotp_4_OAFI9_4t_sU7HioHREEDKqBREz7DkJ1-H9im7uu2h9-RUeJu4kmcSvA6ql4s7vsVgW8eWVfI8Ls3m4h8dPjd__vlY44B6hJ0qmEo7mCI-WwwEDwwHkArVxroNk8aNl0yZBDagpyzwZInbf-32QNclLrcbka7_Ek34-KqqYtmx9EHlm9Kf14sCjzN3w9I_YZECCiHBAPvoj1nOydv6wnkPZW5iKP3zW3ljIYT36IlzWWA1UQmDXmNFLL0a09O61p9FPqgZVnYLF35sbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی تلاش کردند تا یک گروه بزرگ از خودروهای سبک را در یک نقطه تجمع، تقریباً 20 کیلومتر پشت خط مقدم در منطقه دونتسک، مستقر کنند.
همانطور که در اینجا مشاهده می‌شود، پهپادهای تهاجمی کوچک اوکراینی این گروه را مورد حمله قرار دادند و ضربات متعددی به آن وارد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69898" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69895">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=rAVjFsgJjyN5WrvMKElWQdyNiP_QYKdrjrCFqciL5G8VON7O--v3jeT1TYSmeZFOLvfFSXC4IuVEaGQByXDgz3EUHT0fAyVAfyYAqaxJABffXGIFi9JMih8FJPYBu8BEIYTyDAyFI1vtx6AnMTOP3garIzOV7Uo99_L0O1qSc9O8-9feyPcHb60Q9T4Rw_XX1uxm3vnJIBZX8r6wORsQd_bB_lasUYXmU9wsVpZIRgZB8pXOOSK9NMbqQ1R4aA4QZMfsYwsL-JlEDG9pOO1U_GF5xRkwFXvxWgwltiTje1eSeDjauzO6uF7Z6u34g76zMP2dbEoodDc8n_CNuYrG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=rAVjFsgJjyN5WrvMKElWQdyNiP_QYKdrjrCFqciL5G8VON7O--v3jeT1TYSmeZFOLvfFSXC4IuVEaGQByXDgz3EUHT0fAyVAfyYAqaxJABffXGIFi9JMih8FJPYBu8BEIYTyDAyFI1vtx6AnMTOP3garIzOV7Uo99_L0O1qSc9O8-9feyPcHb60Q9T4Rw_XX1uxm3vnJIBZX8r6wORsQd_bB_lasUYXmU9wsVpZIRgZB8pXOOSK9NMbqQ1R4aA4QZMfsYwsL-JlEDG9pOO1U_GF5xRkwFXvxWgwltiTje1eSeDjauzO6uF7Z6u34g76zMP2dbEoodDc8n_CNuYrG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سامانه‌های پدافند هوایی «اونجر» (Avenger) و رادارهای «سنتینل» (Sentinel) ارتش ایالات متحده در نزدیکی محل بازی گلف ترامپ مستقر شدند تا پوشش حفاظتی کوتاه‌بردی در برابر پهپادها، هواپیماها و موشک‌های کروز فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69895" target="_blank">📅 17:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69894">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=GleCbDQIS0UYuqfxUOt-TG1CJW6iB4UFnzQlEv_fJ5J8ooeHjtF02IFKfqqdQWPDbHjAnFkeKAbwr4uZt2if8MEUtynv4I1dtklUUkyNr3pf1zJyWSXXaEFLURO4EsbZ9paVUihVMbuuvm0MO3Oe3y2psrdGofvJNt0blkLcmOnJbAbBdy9mTL6FmuM-2lfHBSBNUT-fckYYr250766cU_A5O3dBBg_c8pquh8T_trGeSatZUTHuNcMGEXc2-cMmEfjMyZpX58KBkYMM_4YwYlqDPU7BTEnOhs_enVHzQ7VrmrcBXmhtxcgS3F1msAk2_8X9DzofbJiPuYXWFScZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=GleCbDQIS0UYuqfxUOt-TG1CJW6iB4UFnzQlEv_fJ5J8ooeHjtF02IFKfqqdQWPDbHjAnFkeKAbwr4uZt2if8MEUtynv4I1dtklUUkyNr3pf1zJyWSXXaEFLURO4EsbZ9paVUihVMbuuvm0MO3Oe3y2psrdGofvJNt0blkLcmOnJbAbBdy9mTL6FmuM-2lfHBSBNUT-fckYYr250766cU_A5O3dBBg_c8pquh8T_trGeSatZUTHuNcMGEXc2-cMmEfjMyZpX58KBkYMM_4YwYlqDPU7BTEnOhs_enVHzQ7VrmrcBXmhtxcgS3F1msAk2_8X9DzofbJiPuYXWFScZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیشب توی تهران، یه نفر با یه دست رانندگی میکرد و با یه دست فیلم سوپر میدید
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69894" target="_blank">📅 17:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69893">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ps7cGJmOC5sILQa9cnOIzqvgRnZ6QnifaeJr9Kvvlt2cdG-_aNfZ8vKatVEG7Ma1xKQWIYnz2tCDKa64Pw3L8Jk7k1KJRnFugr9qsM5rC4NzndKYr0vRbuelosTNyxSZypJNmTjbC4f7i_C7AAkC66K12SS6zKgktPD854G2rsvvA0bZd9B6rDbx9t9zs5WuaXgncl3waS0UccPvByvtn_uWk-21oSSpg8HFrT0-Y-rYiT31OQUF_jPYeT33uiGBKLyOHC2GsCpn4bTPh8dTmXjma5PqrE-mZs-OGoaIHLW-dSoKpbIjCO8GYgRm7Y9B8ol5weYJASX2B3O6TCk49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال:نیروهای آمریکایی بامداد سه‌شنبه به سوی شناوری با پرچم پاناما آتش گشودند؛ این اقدام پس از آن صورت گرفت که شناور مذکور ظاهراً تلاش کرد محاصره دریایی بنادر ایران توسط آمریکا را بشکند.
پس از آنکه خدمه این شناور هشدارهای مکرر نیروهای مسئولِ اعمالِ محاصره را نادیده گرفتند، یک بالگرد نظامی آمریکایی سکان کشتی را هدف قرار داد.
خدمه شناور در حال تلاش برای انتقال به یک کشتی غیرنظامی دیگر مشاهده شدند.
در نهایت گزارش شد که هر ۱۷ خدمه کشتی در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69893" target="_blank">📅 16:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69892">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idoKYDXiLVpbEw4fZku8XyMPPaYWuKQstpIVLVRaPgZRokTKkKW0mxNyvvlC1Q8bVyyf4iWIel7QUL2ish7PTrDaWgPJSXxFklvhQYcA_G3tgHnxvNp-L7-7ncWNL68c26Q-QH8d1YNPMafCnniUAo-HgKwWUUQQ3UR07GFmH61e3dsNKizhq0oyDFrO2jqhWaHoP0FWM-vb3JBxhWJCiuCk4dARYVyHnQyfcBH2H5ygNMeODz3qcLuUk7ZGlv3DroMH5N-CQzuV5ZuVHxnrrHZzeOo8QoX8v0xa0kZ0-b_-569MGjJmE5Jgxm6lida2qvNVy7r-2WFCOMz-5thHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📚
#فوری
؛ زمان برگزاری کنکور مشخص شد!
صبح پنجشنبه ۲۹ مرداد : کنکور تجربی
عصر پنجشنبه ۲۹ مرداد : کنکور زبان و هنر
صبح جمعه ۳۰ مرداد : کنکور ریاضی و انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69892" target="_blank">📅 16:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69891">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=nK-Hx7nE9qicWM67KQuYD77O16JMo3-2fajHRImJdoJWcYTqm7pZAXUwncja4Es5rPsgEdPo6LcGVUChQClCAQJXgMgWpatJ5RzTalt2qtPqqncOapRZNkP0kaWYFOoHE3Mv_QP3c8yMdn2a9wthLUS3Fm3Vg_hfa3Paz7LNf68w3OTZzAHeW6Qo7QBOkBtKHeD5W13otb13sWpA8e9mDGOeH6wIhcpDVvQkQIstXDAkQ5-iPBCtQNUwbB4WJ6hmqeM7J1ZYFEMGetzbNvlfmEls7oAKy09_8TDO6o77uCSOyf7dRj-42Wj0sGSfTYk94Sw8RgH-R8uLrjekuOvizA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=nK-Hx7nE9qicWM67KQuYD77O16JMo3-2fajHRImJdoJWcYTqm7pZAXUwncja4Es5rPsgEdPo6LcGVUChQClCAQJXgMgWpatJ5RzTalt2qtPqqncOapRZNkP0kaWYFOoHE3Mv_QP3c8yMdn2a9wthLUS3Fm3Vg_hfa3Paz7LNf68w3OTZzAHeW6Qo7QBOkBtKHeD5W13otb13sWpA8e9mDGOeH6wIhcpDVvQkQIstXDAkQ5-iPBCtQNUwbB4WJ6hmqeM7J1ZYFEMGetzbNvlfmEls7oAKy09_8TDO6o77uCSOyf7dRj-42Wj0sGSfTYk94Sw8RgH-R8uLrjekuOvizA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یه آخوند توی برنامه زنده داشت به اجرا نشدن قانون حجاب اعتراض میکرد و میگفت ملت بالای ۴هزار تا پیام دادن برام؛
بعدش گفت بزارید یکیشو رندوم براتون بخونم:
چیزی که خوند
😔
:
«آقای پفیوز احمق بیشعور حرف دهنتو بفهم»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69891" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69888">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=rjS5Rr1JkQZAOGaf9uu_k10L9DBb1PePSVJb9G72OgydgJGdnkzmde2jDJysRpYo0XIuQUd4Rma5IexQVVPiPqrALmW72jDxQMd-e_hBHgFNvgvc95wVADzSMcW8kWN0IJezagXOeSCDJJbyPsdTxl_eJv9q_5n8E6ixobKDNBbj6hdRk56wC-wU-x-UQ59Uge3W4vGrA9C8nZ6CNFB9MTsv8iSy1WskVAQSf15IuMs6ar9MrtdLVYd6aTKfgN97j32d5E1igSgOl_9UITOsyYQ65d8ClB_odR5P9EIbBRvlQ5MaGXsMhjsGBGF_P1DZ5wLAYr0sdwewNATiQoTkVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=rjS5Rr1JkQZAOGaf9uu_k10L9DBb1PePSVJb9G72OgydgJGdnkzmde2jDJysRpYo0XIuQUd4Rma5IexQVVPiPqrALmW72jDxQMd-e_hBHgFNvgvc95wVADzSMcW8kWN0IJezagXOeSCDJJbyPsdTxl_eJv9q_5n8E6ixobKDNBbj6hdRk56wC-wU-x-UQ59Uge3W4vGrA9C8nZ6CNFB9MTsv8iSy1WskVAQSf15IuMs6ar9MrtdLVYd6aTKfgN97j32d5E1igSgOl_9UITOsyYQ65d8ClB_odR5P9EIbBRvlQ5MaGXsMhjsGBGF_P1DZ5wLAYr0sdwewNATiQoTkVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه توی آخرین مصاحبه‌ش گفته رابطه‌ش با شروین حاجی‌پور یه اعتماد اشتباه بوده و این رابطه تموم شده.
بعد از این مصاحبه هم شروین یه موزیک منتشر کرده که خیلی‌ها معتقدن حال‌وهوای بعد از جدایی رو داره.
جالب اینجاست که اوایل رابطه‌شون شروین توی یکی از موزیک‌هاش گفته بود قراره تا به دنیا اومدن نوه‌هاشون کنار هم بمونن!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69888" target="_blank">📅 15:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=UEpz38U9UWiZIRMut875NNQ7RRYRno-i_9dm8XhSj-FIjsi0e7WbEdzzr6HzAECHw2b3GoQc805SI7zVPeWdo09-vfYZzeUTl1igj4r5kreCytcPKF9Qo4Ohb-IBtt453zAx6LuOYg5f__KpimcEYWGO1FSFJL2vA178b5tAKQPkVBP0L8nYruBlmIY_Aayp526JzHRAo1qaaJnGoki06tVPyDYujhVrIn0rb8-z94VSKd9KPfEtSVcRCWn_DvQ0MErE05nIcgIaSPfEMWWd_KDlwa3qg1mM3cL-vlzL8IMjIadgvV9EVbeWxr_g_2znMMaeKEeTU-8fkX_6mSjk9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=UEpz38U9UWiZIRMut875NNQ7RRYRno-i_9dm8XhSj-FIjsi0e7WbEdzzr6HzAECHw2b3GoQc805SI7zVPeWdo09-vfYZzeUTl1igj4r5kreCytcPKF9Qo4Ohb-IBtt453zAx6LuOYg5f__KpimcEYWGO1FSFJL2vA178b5tAKQPkVBP0L8nYruBlmIY_Aayp526JzHRAo1qaaJnGoki06tVPyDYujhVrIn0rb8-z94VSKd9KPfEtSVcRCWn_DvQ0MErE05nIcgIaSPfEMWWd_KDlwa3qg1mM3cL-vlzL8IMjIadgvV9EVbeWxr_g_2znMMaeKEeTU-8fkX_6mSjk9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود هواپیمای F-18 بر روی ناو هواپیمابر در هوای بارانی.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69887" target="_blank">📅 15:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=X_JtWc4EVw0RdeO0HlQjX0YrENue2oNkxbqq4JAFvnP-zbzY21YcTh4XxHrPVe0v_-ts4OrX1Snny6gYfutdMS_68bDbl9INpRkuXtUL6xB_kdg_Hq6PeYlkkK4q4aVoBrx43dHUlb1F5sX_RUVfUE77i7EnQgSsYNQRNFzeigUeJPN459qf6V5Yihr-DobXwEsdFA0wRjSIy8vKDVz3snI4NpLtdAiATOEm3ttOaQDTSL2k4027qLzDON88tpxt_l1SKsnThHlvWAdM9G3MaQVuxe5P78scNKevc50P3fETFTdA-Y3Tljg-qlWmid9fpfUCuo3TR3guRPLliFecQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=X_JtWc4EVw0RdeO0HlQjX0YrENue2oNkxbqq4JAFvnP-zbzY21YcTh4XxHrPVe0v_-ts4OrX1Snny6gYfutdMS_68bDbl9INpRkuXtUL6xB_kdg_Hq6PeYlkkK4q4aVoBrx43dHUlb1F5sX_RUVfUE77i7EnQgSsYNQRNFzeigUeJPN459qf6V5Yihr-DobXwEsdFA0wRjSIy8vKDVz3snI4NpLtdAiATOEm3ttOaQDTSL2k4027qLzDON88tpxt_l1SKsnThHlvWAdM9G3MaQVuxe5P78scNKevc50P3fETFTdA-Y3Tljg-qlWmid9fpfUCuo3TR3guRPLliFecQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زیبای زندگی کسی که هممون باهاش خاطره داریم...
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69886" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
🔴
ما سه راهبرد داریم:
ادامه دادن به همین روال فعلی؛ یعنی صرفاً پیش رفتن و نظاره کردنِ وضعیت وخیم آن‌ها، چرا که تورمشان به ۳۰۰ درصد رسیده است. ارزش پول ملی‌شان تقریباً از بین رفته است. آن‌ها حقوق سربازانشان را نمی‌پردازند و سربازانشان در حال ترک خدمت هستند. بنابراین باید همین روند را ادامه داد، چون این وضعیت پایدار نیست.
وارد کردن ضربات بسیار سنگین به آن‌ها، یا... در واقع راهبرد سوم، شکست دادن آن‌ها از طریق اقتصادی است. اما ما به هر حال داریم همین کار را می‌کنیم؛ این [راهبرد] تا حدی بخشی از همان راهبرد اول محسوب می‌شود.
از نظر اقتصادی، وضعیت آن‌ها آشفته و نابسامان است. آن‌ها نمی‌توانند وام بگیرند. ما کنترل منابع مالی‌شان را در دست داریم؛ همان دارایی‌هایی که در اختیار داشتند و رقم بسیار بزرگی هم بود. آن‌ها سرمایه زیادی داشتند و ما اکنون کنترل کامل آن را در اختیار داریم.
من بانکدار آن‌ها هستم. من بانکدار آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69885" target="_blank">📅 13:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69884">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=lWvjrk8OumtYLGWDtBWFsb5xLEsjVcWaO9Xc5gcwsT7tO6L5MGzfcob4-alh681UTRfI20JycS3Z4Iupyo658jqef16I7WKUIum6LMj9qXanUAgcBpmLHa789tnJyCr6SzKStfSyh7eU5dYh_hIz1CrA1AiYhTQO5-EbQSJJuuJVoFqVEPfK0VGV9J8kq0QO_RJZEtoP8d7hC0vuAuP1F27nxbYxqxWgI0Te_N81A1RXo9iqYm0VKVDNeSElODfHPh4wUav1LAapuzhtDqu7V4Hu_81lKJt0JgGmhRF7WY1F-kSS6iBqQDRNR2Xb9fWT_EN5slwsMrLY_EsJUhYFaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=lWvjrk8OumtYLGWDtBWFsb5xLEsjVcWaO9Xc5gcwsT7tO6L5MGzfcob4-alh681UTRfI20JycS3Z4Iupyo658jqef16I7WKUIum6LMj9qXanUAgcBpmLHa789tnJyCr6SzKStfSyh7eU5dYh_hIz1CrA1AiYhTQO5-EbQSJJuuJVoFqVEPfK0VGV9J8kq0QO_RJZEtoP8d7hC0vuAuP1F27nxbYxqxWgI0Te_N81A1RXo9iqYm0VKVDNeSElODfHPh4wUav1LAapuzhtDqu7V4Hu_81lKJt0JgGmhRF7WY1F-kSS6iBqQDRNR2Xb9fWT_EN5slwsMrLY_EsJUhYFaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سینا حجازی، خواننده:
اگه زنِ هات میخواین، زن گوشت‌خوار بگیرین، زنایی که گیاه خوارن، سردن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69884" target="_blank">📅 13:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0nY1Frj1SJ7z6w5QeaQsNk3CX9B7hhCAMpoFoNy9Sr9fONlieaPYyFPEOjcrxhCEvdumHnEVVfbgzfNlgv7bPnagi_dJj2a5y--D50hn6Fvc1aA0Dcp6rccIGG0O7BdiKyr1uB7KfUfIjvk1Z6qnpjrA7DKWJVW8vK6hnHaaNBptXLU56GqUO-Xk-R2-O4LMfrCruF8Lb-bsCRMfp1wqvTm6OsZGQvUZb79OEqyfZxYnVNz63UIDvmsKAiUQ7HKh29PX3dRqrhVUMF6U1G4U0jENeYbVpiHNX6b6NskbLjkph8W25ZFyBvMdod1Pf4dtH06BDBPYSKULf9QLWy9qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه‌ای میان یک نفتکش و نیروهای نظامی در دریای عمان خبر می‌دهد.
هویت نفتکش و نیروهای نظامی درگیر در این حادثه هنوز اعلام نشده است.
در حال حاضر جزئیات بیشتری در دسترس نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69883" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=BBGxvCEQqJlt1qPMM6ZdPF-WN5O1w9PSrwU7_WLYEBnRmqnezcKmIE4MoTrOiwy-ia3Q3F5OtwsPaz2kLcDVsmjbewEV0-EW9SK1jqxVRV3LOCqYmzzNu0wnoxgIAZO8ATNcQ5ebWCjqkv_FQ3tYdLWaPgsf7f2jQNUKNv9cNWgHTVX199cSiZa-lE4genrw-IsrSWOJjzLYRJRwtw-NLO1GL5IewclsUIWTygxZ-jgyORfh0JpI_o5sRS0vFUSKwm1rO23wq1IhBASJ_PO4m85bCJwr2fZVPHc5BwhvOu5gVGGC-NfnZ2p8pZS5UBZEV9NWuMERpwzWohg3yKTO7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=BBGxvCEQqJlt1qPMM6ZdPF-WN5O1w9PSrwU7_WLYEBnRmqnezcKmIE4MoTrOiwy-ia3Q3F5OtwsPaz2kLcDVsmjbewEV0-EW9SK1jqxVRV3LOCqYmzzNu0wnoxgIAZO8ATNcQ5ebWCjqkv_FQ3tYdLWaPgsf7f2jQNUKNv9cNWgHTVX199cSiZa-lE4genrw-IsrSWOJjzLYRJRwtw-NLO1GL5IewclsUIWTygxZ-jgyORfh0JpI_o5sRS0vFUSKwm1rO23wq1IhBASJ_PO4m85bCJwr2fZVPHc5BwhvOu5gVGGC-NfnZ2p8pZS5UBZEV9NWuMERpwzWohg3yKTO7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازگیا به نوع مدیتیشن تو تهران مُد شده که کلمات رو به صورت نفس‌نفس زدن میگن تا انرژی بد ازشون تخلیه بشه
😳
هزینه هر دوره بالای ۴۰ میلیون!!!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69882" target="_blank">📅 12:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=ZJ8jlR7J0YB_hwaS0kLcWkLSVgA0lSn5-gmwWYndp-SpI7S1we4WQLGA1l64B7oiyiOT5sTTTKwiXXKUQ1i-02HN1reKkGjOpTM4856WGfx3a9LRqUBC07sUOHf9b0oDFj-gapM9vF9q7RFjk8M4_vNi6O2Nysa3PdwwULBS-DMhyBdT41gBsmd5hWVqXYNdqgXiyNnNW9PkpQ-4fNhCbUbWWHXbJYv2PR5-vceoPPi6tm-PiUKvNNli7r-QapTlEvF1aVU2Br-1adS5cC3Ob3QY_iiwsR_4ulgF0UKuRnBDUeXq88XiPrYJ53iGGV8Xrer6F5j6ReYD4HAAaMXfFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=ZJ8jlR7J0YB_hwaS0kLcWkLSVgA0lSn5-gmwWYndp-SpI7S1we4WQLGA1l64B7oiyiOT5sTTTKwiXXKUQ1i-02HN1reKkGjOpTM4856WGfx3a9LRqUBC07sUOHf9b0oDFj-gapM9vF9q7RFjk8M4_vNi6O2Nysa3PdwwULBS-DMhyBdT41gBsmd5hWVqXYNdqgXiyNnNW9PkpQ-4fNhCbUbWWHXbJYv2PR5-vceoPPi6tm-PiUKvNNli7r-QapTlEvF1aVU2Br-1adS5cC3Ob3QY_iiwsR_4ulgF0UKuRnBDUeXq88XiPrYJ53iGGV8Xrer6F5j6ReYD4HAAaMXfFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
استایل ثروتمندترین ورزشکار دنیا
🆚
استایل پسرایرانی با ماهی ۱۵تومن حقوق
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69881" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=WDnVVL8T0V-HNoxqJwsV5JpNua1kO5FCZApvv0oxIR6exVbn1v-rZBOwsbFSWvBnfOqmDvSMdg16zWtNcGY_ey-btns3NlucrtBnZqtF8M_14425P5xk2wI5CbyRIEtk4NnQdpK7TLiQyMr1nlGpRSH9ZbhzrnrJllMqPAc-iT2QFRnpmAJwiFF74iqguucqQO-kEBNaR4tIHY2UF-jgCMl80bjZbxL_-AOvZ1Ca7COZBZY9hC9Yq81sWpaXwlvA_CK6VPOnO3XwS77cHbG2cshcDp4v9xvbpEwXOKeelu3XbRxD-JJP4N7yZxGnmQGidPP7VVl02o_qWLoxLi0y3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=WDnVVL8T0V-HNoxqJwsV5JpNua1kO5FCZApvv0oxIR6exVbn1v-rZBOwsbFSWvBnfOqmDvSMdg16zWtNcGY_ey-btns3NlucrtBnZqtF8M_14425P5xk2wI5CbyRIEtk4NnQdpK7TLiQyMr1nlGpRSH9ZbhzrnrJllMqPAc-iT2QFRnpmAJwiFF74iqguucqQO-kEBNaR4tIHY2UF-jgCMl80bjZbxL_-AOvZ1Ca7COZBZY9hC9Yq81sWpaXwlvA_CK6VPOnO3XwS77cHbG2cshcDp4v9xvbpEwXOKeelu3XbRxD-JJP4N7yZxGnmQGidPP7VVl02o_qWLoxLi0y3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:درباره گرانی ها هم توضیح بدید؟!
🇮🇷
مهاجرانی سخنگوی دولت:
قبلا توضیح دادیم، گرانی های موجود دلیلش فشار اقتصادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69880" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=dh4AaBnXkqVZ7bwHMB-kUlvkeIdJJU7SLl76_NjYyeY0hhrN1x4NdMOCrbIBF-AdnP2ZWlNufhwJbnMHXBDSX_8x3OSV6qDJmUz0_vcAp31is7GJgHo_1HO0XRPV8pqmfOIT6HL6FjpbJHvDtReQxJNxhloNL5TLLQS66FhipdX5J5SasWv7lAQGYXvBsJzmlTEfBDLvsWBpkfs9zTCbILFwFTx1JLcWoEjL5A7I5PkBgRxBMX9NI6XNr4eqjWMkZfOK2Lw52glOpWckyDBGgadBw8z1GVQj9QHVGQOfVHJXyf_uEYFQyUwqIyZajqjFyXZqIIyUOO90o14DKLpNug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=dh4AaBnXkqVZ7bwHMB-kUlvkeIdJJU7SLl76_NjYyeY0hhrN1x4NdMOCrbIBF-AdnP2ZWlNufhwJbnMHXBDSX_8x3OSV6qDJmUz0_vcAp31is7GJgHo_1HO0XRPV8pqmfOIT6HL6FjpbJHvDtReQxJNxhloNL5TLLQS66FhipdX5J5SasWv7lAQGYXvBsJzmlTEfBDLvsWBpkfs9zTCbILFwFTx1JLcWoEjL5A7I5PkBgRxBMX9NI6XNr4eqjWMkZfOK2Lw52glOpWckyDBGgadBw8z1GVQj9QHVGQOfVHJXyf_uEYFQyUwqIyZajqjFyXZqIIyUOO90o14DKLpNug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دکتر مشاور خانواده :
یه مرده اومد بهم گفت زنم عاشق دوستم شده و منم بهش گفتم که تو حق داری باهاش رابطه داشته باشی!
گفت منم با خانمِ اون آقا چندبار رابطه داشتم ولی چون اون خانم خودش پارتنر داشت، زیاد خوشم نیومد و کات کردم...
ولی خب موقع سکسِ اون آقا با زنم، من اونجا هستم و تماشا میکنم!
الانم از اینکه خانمم از اون آقا باردار شده خیلی ناراحتم چون آمادگی داشتن بچه رو ندارم.
ولی خب بازم میخوام شناسنامه اون بچه رو به اسم خودم بگیرم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69879" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69878">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69878" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69877">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLrS_0FtLZuhVH0mMJjx4h2gLtrxrtJD4VNjk6a9FDHj5P72RhcsHfxSsVF5OyxmVbeZfbQVo6Y04TT22wYeeve7InrxCEpwvUgQ-Kkbiz2kqZ3Gv7k9wPWfajaRCv8pTsv9te5AQ7mMaqf_CqcascU8gE032ruROTUMfL2BzzTKZMqzFhUA7sb7VK9cVW4lyQpgj850oeEKJt0Fy6K1mutIK0cKEt-4cSI4d2Wfw0AR4td7yJfagVrS4ZQMDviX3O7nCT_SqPQbsjfWiDrE2iN6obk2pZpq_Th8I8BYpj58cD8daJQN97xMoq-cijA1KdRKFPJv8ohzYChoBzj_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69877" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69876">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2435556002.mp4?token=q5pmiXRvMRAyGcvAisJ0Z1KzM4cCMordtNkzD_hSawqU1Vagti03hawysx1pOTPtZu_b4u8XBwlLJcqhF6AdYtqstOc_pXeq_thpr-Qw2trDWVgfDxUj7MzNA_fRx5JJL4sT4K4N05DRUmbONLUBHVhxowzK8EpP_R5D7K1BB45sTWLHHKHCY9oOqFnAtSce2kF52LNCS5krYlk-uhHzDd3MzPkilJB1RlI2srube2RMLdwBxfSRbsLW5TP7SzhEmVaDjLFkI_R0nU_Gy1HyxObapdphp9WG-m07h2Djo2aRjRf2OwKSg7m0ku7PWMjED_gRNMCWGwccfzTQexGMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2435556002.mp4?token=q5pmiXRvMRAyGcvAisJ0Z1KzM4cCMordtNkzD_hSawqU1Vagti03hawysx1pOTPtZu_b4u8XBwlLJcqhF6AdYtqstOc_pXeq_thpr-Qw2trDWVgfDxUj7MzNA_fRx5JJL4sT4K4N05DRUmbONLUBHVhxowzK8EpP_R5D7K1BB45sTWLHHKHCY9oOqFnAtSce2kF52LNCS5krYlk-uhHzDd3MzPkilJB1RlI2srube2RMLdwBxfSRbsLW5TP7SzhEmVaDjLFkI_R0nU_Gy1HyxObapdphp9WG-m07h2Djo2aRjRf2OwKSg7m0ku7PWMjED_gRNMCWGwccfzTQexGMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری و بلاگر طرفدار حکومت:
یعنی چندنفر باهم مشکل داشتن و همدیگه رو به طور کامل میشناختن
این پروژه‌ها از این به بعد قراره زیاد باشه واسه اینکه میدون‌ها و نیروی انتظامی رو ضعیف کنن
قاتل‌ها تو کمتر از 24 ساعت دستگیر شدن و کشور الان تو بالاترین سطح امنیته مخصوصا تو تهران.
متأسفانه قراره خون ریزی های از قبل برنامه ریزی شده شاهد باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69876" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69875">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=m-HDesmh8L0q3apX6932mcMHachm30XRxd_1aAFzQc8XYdx_idUSnv3pILgC70dlCyiX-SiwO0T-4EZWWZGVqpzR6DIa__RRHahjkV9PtkyvM97ugCiY4EgMXp6etSyGSvugfHRE-94vZ8JDGQxZL3QQs6rMNWXJ_sol2JXAW2FPECWbFBXFdeW55I_HkZg3neYoR6Msr9L7_MLS7tjfMVC6BXgGt1G58T3pgPhQgptQnqyzIgOHiCqqI4rqkDN0oT5z3cC2mqvcGi-nkXGHDS3w-m6XZA1RYFOLknipxWNQb3LF9l9ZqAuoujaccCzK126F7igvMmuwt-sXE8kQWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=m-HDesmh8L0q3apX6932mcMHachm30XRxd_1aAFzQc8XYdx_idUSnv3pILgC70dlCyiX-SiwO0T-4EZWWZGVqpzR6DIa__RRHahjkV9PtkyvM97ugCiY4EgMXp6etSyGSvugfHRE-94vZ8JDGQxZL3QQs6rMNWXJ_sol2JXAW2FPECWbFBXFdeW55I_HkZg3neYoR6Msr9L7_MLS7tjfMVC6BXgGt1G58T3pgPhQgptQnqyzIgOHiCqqI4rqkDN0oT5z3cC2mqvcGi-nkXGHDS3w-m6XZA1RYFOLknipxWNQb3LF9l9ZqAuoujaccCzK126F7igvMmuwt-sXE8kQWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇺🇸
واشنگتن پست:پس از تهدید ترور از سوی ایران، ترامپ مخفیانه هنگام ترک اجلاس ناتو در آنکارا با هواپیمای دیگری جایگزین شد.
او با هواپیمای جدید ۷۴۷-۸ اهدایی قطر (اولین سفر بین‌المللی ریاست جمهوری‌اش) به ترکیه رسیده بود.
برای عزیمت، او علناً و جلوی دوربین سوار هواپیمای قدیمی ایر فورس وان شد و گفت که می‌خواهد «به یاد گذشته» با آن پرواز کند.
اما دقایقی پس از سوار شدن، او و چند دستیارش از طریق یک کامیون پذیرایی فرودگاهی که کانتینر آن به صورت هیدرولیکی به دری در کنار و دور از دسترس رسانه‌ها بالا رفته بود، به یک هواپیمای کوچک‌تر C-32A (757 اصلاح‌شده) منتقل شدند که از دید پنهان بود.
سپس هواپیمای قدیمی ۷۴۷ به عنوان طعمه پرواز کرد و همچنان از تابلوی تماس ایر فورس وان استفاده می‌کرد.
روزنامه‌نگاران و برخی از کارکنان کاخ سفید که در هواپیما بودند، اصلاً نمی‌دانستند که ترامپ با آنها نیست.
به آنها گفته شده بود که پرده‌های پنجره را بسته نگه دارند، که امری غیرمعمول است.
هر دو هواپیما با فاصله چند دقیقه در فرودگاه سلطنتی میلدنهال در بریتانیا فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69875" target="_blank">📅 10:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69874">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ما ۳ استراتژی برای برخورد با ایران داریم
رصد نقاط ضعف این کشور.
وارد کردن ضربات سنگین.
اعمال فشار اقتصادی.
🔴
اکنون ایران در وضعیت آشوب اقتصادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69874" target="_blank">📅 10:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69870">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=grcoJwPQ43dB70NzGrxKK6_JZHI2b66QxFGqSNGXTVNl0ltbx2UMGqzxVs1zKNnUUrhI8p4EwSAgKLXAYthQtbkDziVzn59GafEZh1vYi1xKsmMieroDjxLSJYUhbi-_tfl43wcpagba8JP_M8IubKKWsQMFp7Og1bKIQ0Pd2pbPgKNy-2W3SgWsNHbQGcz85eAQ3sccq61RzlfqdMzhsIBWpEj62Ylm7IRflKpfRMdq363p_yMxnRdXXgZGFlGincAcfZTgNIccN5I6GiNR9lfj0OaIn4TawHybqCZyaocVbcrtYXoPAtCSF-MMavp2-PRjTKIJWwbw45AenXZL6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=grcoJwPQ43dB70NzGrxKK6_JZHI2b66QxFGqSNGXTVNl0ltbx2UMGqzxVs1zKNnUUrhI8p4EwSAgKLXAYthQtbkDziVzn59GafEZh1vYi1xKsmMieroDjxLSJYUhbi-_tfl43wcpagba8JP_M8IubKKWsQMFp7Og1bKIQ0Pd2pbPgKNy-2W3SgWsNHbQGcz85eAQ3sccq61RzlfqdMzhsIBWpEj62Ylm7IRflKpfRMdq363p_yMxnRdXXgZGFlGincAcfZTgNIccN5I6GiNR9lfj0OaIn4TawHybqCZyaocVbcrtYXoPAtCSF-MMavp2-PRjTKIJWwbw45AenXZL6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
دیروز تو کلمبیا، یه زلزله 7.4 ریشتری اومد و اینجوری به ساختمون ها خسارت وارد کرد؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69870" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69869">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=T0tv1AcDXLvu4hdj8qNmXriNxfLIjzWE2m7tLF_VyKj7K9ZU-IBoKuNan2paAmqplcjERoJwZjAv1OafUDpdhRv_tWH4-L4DM2dewfjp9w2fSX7lHj9b8Ikc06d_C24goi7iYFNy_ykjh4GFFEuiVgAAvHLqBEXE_QVEbYetLLahjl98vXOaVvYLdnYrBDhTZs1gogXKr9p4vlufsSnvvqhUCfYoAW5_nvY6POON6Q32VstgAtJAz3Fq_lAVTM9hy0E0QanCjLyKWN2ANiDu_wR9cdGc-XzMwVN1j2Avspv6N9KlaziMbuEkWTteebWvKrC8k-0ffyC7tIQuXHWwXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=T0tv1AcDXLvu4hdj8qNmXriNxfLIjzWE2m7tLF_VyKj7K9ZU-IBoKuNan2paAmqplcjERoJwZjAv1OafUDpdhRv_tWH4-L4DM2dewfjp9w2fSX7lHj9b8Ikc06d_C24goi7iYFNy_ykjh4GFFEuiVgAAvHLqBEXE_QVEbYetLLahjl98vXOaVvYLdnYrBDhTZs1gogXKr9p4vlufsSnvvqhUCfYoAW5_nvY6POON6Q32VstgAtJAz3Fq_lAVTM9hy0E0QanCjLyKWN2ANiDu_wR9cdGc-XzMwVN1j2Avspv6N9KlaziMbuEkWTteebWvKrC8k-0ffyC7tIQuXHWwXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی:
مجتبی خامنه‌ای اگه تو این سه سال از دفتر رهبری طرد نمی‌شد، می‌کشتنش
خود علی خامنه‌ای هم همین‌طوری بود، تو دفتر خمینی هیچ جایی نداشت
از احمد خمینی بگیر تا کروبی و... همه میخواستن مرگ علی خامنه‌ای رو ببینن.
ابراهیم رئیسی هم قصد داشت رهبر بشه که شهیدش کردن
اصلا بحث همینه مجتبی اگه زیاد پیش پدرش دیده می‌شد خودی ها میکشتنش
تو بحث رئیسی هم یکی از اعضای دفتر اومد خونمون گفتش ک دارودسته اینا میخاد رئیسی رهبر بشه ولی شهادت جلوشو میگیره
خیلی حرفا هست ولی خب مطمئن نیستم بشه گفت یا نه
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69869" target="_blank">📅 09:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69868">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
🇺🇸
✈️
پشتیبانی سنگین آپاچی‌ها از نیروهای ویژه آمریکا در افغانستان
⏺
تصاویر نادر و حدود ۱۵ دقیقه‌ای از عملیات دو فروند AH-64 Apache در افغانستان؛
آپاچی‌ها گروهی بیش از ۲۰ نفره از نیروهای طالبان را که در حال آماده‌شدن برای کمین یک گشت نیروهای ویژه آمریکا بودند، شناسایی و درگیر می‌کنند.
در این درگیری، آپاچی‌ها ابتدا با توپ ۳۰ میلی‌متری M230 مواضع طالبان را زیر آتش می‌گیرند و سپس برای درگیری با اهداف مشخص‌تر از موشک‌های AGM-114 Hellfire استفاده می‌کنند.
تصاویر این ویدئو با سامانه تصویربرداری حرارتی FLIR نصب‌شده روی آپاچی ثبت شده؛ به همین دلیل صحنه‌ها به‌صورت تصویر حرارتی دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69868" target="_blank">📅 09:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69867">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
a19
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69867" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69866">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_tlxLmrE-QgsAozVIYkUvHRX0L_1OTkA54beLx_c4yNQwMb4NXFCQONwxxb5NpVg6gclVARr8cU1oGObgfjb-iRh_0RNShpHEsoJjFUukXUJ2Wrt_1wn7-nTRVF2Gy-QVn33Vli7HERLscN3n_zx6bfaM4gd2qWiN4XMFqFKiuNtwzWs_fcRrxxEhqTLVlaVf0VA67fxOwxcLqCuQ5O84j7bZunnBEOiesmVRbB9i5xp8M-mMBdGEbkkTBLc5y160rBBglI4Vs8p-nHMs2xUaRmdpka8IznztcBtDeTOtTEmN8YAUlmJftr0QHLbtUw4yRQWDk1t872MEsXxDYf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a19
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69866" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69865">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=YSuvO9Wu0WeLohLzgM87a7LO3M6m1cIbEnfHQcY8qWwuS68zaUzlSREoY2wApzHiOib9lV7wrv9PZD2Xn-_nEE7nqNTYHKKQ1DQ8vXM4oN5NTJLXhKPhPBnTRcIm1UTHf8GQXzbRTgJKNM8zKqec_b4b9hKdlzegEZpJYmLBAizYQwSSaJv8ePT-OUNkvuhp_EjeHjPR7LwC-YjokU5v2mmL9KMMPVLn1zd5qctywLySSYTRpYsKYkruIUj9-jrzRKu7G0f0PDE2U_vOgLayN3rPSHR5YJVqLsJ7z9nVGrtMXITeas07KdXd0TBy5dYdJ79o2Fd1Uur-8687XQYa3bdRLPk2Ex1e27pJrSXsOye2p1QVjOlFBW1LoDMajxoV8B7vsSS7Cf6w53GgSFeE6QHRKQtJJuQH6eY2Hjcfu53DEo0uAkQ8OPnHv37_g_3JTFwLeT2U74GC14Dwk5v6XfJKxCZ2Mlxq-BVg5Q1dIO4Ohubm5XgiSWAD-bQ9Va9uuYwmcZpakMR5RM6oOJbzArPHzphRNIVoaEFzg7via6mgdglTmK32_LOchYlL77Iax301Vfj7mp8pJ-dRnae_03D6NiKRnLASYLXteaYuL632YswNqc01c_oh8R7y8Kw1HtHN5dN6uDH__g0MRMA2FDw_hStIlNm1tRBJAdYmhfM" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=YSuvO9Wu0WeLohLzgM87a7LO3M6m1cIbEnfHQcY8qWwuS68zaUzlSREoY2wApzHiOib9lV7wrv9PZD2Xn-_nEE7nqNTYHKKQ1DQ8vXM4oN5NTJLXhKPhPBnTRcIm1UTHf8GQXzbRTgJKNM8zKqec_b4b9hKdlzegEZpJYmLBAizYQwSSaJv8ePT-OUNkvuhp_EjeHjPR7LwC-YjokU5v2mmL9KMMPVLn1zd5qctywLySSYTRpYsKYkruIUj9-jrzRKu7G0f0PDE2U_vOgLayN3rPSHR5YJVqLsJ7z9nVGrtMXITeas07KdXd0TBy5dYdJ79o2Fd1Uur-8687XQYa3bdRLPk2Ex1e27pJrSXsOye2p1QVjOlFBW1LoDMajxoV8B7vsSS7Cf6w53GgSFeE6QHRKQtJJuQH6eY2Hjcfu53DEo0uAkQ8OPnHv37_g_3JTFwLeT2U74GC14Dwk5v6XfJKxCZ2Mlxq-BVg5Q1dIO4Ohubm5XgiSWAD-bQ9Va9uuYwmcZpakMR5RM6oOJbzArPHzphRNIVoaEFzg7via6mgdglTmK32_LOchYlL77Iax301Vfj7mp8pJ-dRnae_03D6NiKRnLASYLXteaYuL632YswNqc01c_oh8R7y8Kw1HtHN5dN6uDH__g0MRMA2FDw_hStIlNm1tRBJAdYmhfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
لحظه سقوط یک جنگنده میگ-۲۹ اوکراینی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69865" target="_blank">📅 01:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69863">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=gpYRiJWC1uWsMh9vQK7pBbNZZeLwJBwJjg-CiaVcNACUBX4f9wq59knjTEJFuq1rvXVdD43x-BAA7z5U6F4WFcztUtqdFKu1yq4QR66YKD6ePw-N2Im9OWMwwZFonrIoDPCpsRboBtHDD_wARoJuBfG5JzYUpM2MQsDJ0pI521c7MOdEXwJzfDbkafCyw14g_C-HzJK-YZtktVVgHYk1tzNPfBVveAWFxwD9Ze2JT3F4jGmEb0TWOP4KRJaf7TDEgrs8falExEaYtm_5eXhHzud46bSG4YgYz_L28NlfgjSVAOw4Z0-JfXZE2Coyw1azIMGYMsiWYifDt6ZZ-LREPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=gpYRiJWC1uWsMh9vQK7pBbNZZeLwJBwJjg-CiaVcNACUBX4f9wq59knjTEJFuq1rvXVdD43x-BAA7z5U6F4WFcztUtqdFKu1yq4QR66YKD6ePw-N2Im9OWMwwZFonrIoDPCpsRboBtHDD_wARoJuBfG5JzYUpM2MQsDJ0pI521c7MOdEXwJzfDbkafCyw14g_C-HzJK-YZtktVVgHYk1tzNPfBVveAWFxwD9Ze2JT3F4jGmEb0TWOP4KRJaf7TDEgrs8falExEaYtm_5eXhHzud46bSG4YgYz_L28NlfgjSVAOw4Z0-JfXZE2Coyw1azIMGYMsiWYifDt6ZZ-LREPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
املاکی رو ببینید؛طرف یه ساعته داره جلوش گوه میخوره بعد این کصخل یجور لم داده رو صندلی که انگار تو تخت بغل ملانیاست
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69863" target="_blank">📅 01:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69862">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=Fo9RusCr4Ar8fxXAgY3-k4ZCddJa7cW4E7v_EkEJMmeTk4ct9t69A75rZiDG3ut5pyXeQwJeG2lw3CdckhI-nVCeO4KQiWf9vS31ESfe0_0XnexBZITkICK_cfqyGGg2wwXJdJjW8ZIVuaJUyCYPDtYzh6B0M3st6MnSxHCYEgSNvHdV6ZHNJCHIoF09oQ-mAy3Sv3kCegV0u3jqN4voaWCVaAcu2ocEINIf7u4V2XdJDHxCFaTQi7ISXIL-bcC3XHYI_sCFctAY4iTswC3nu6qRT4uuFHAWe_Vs7WKQd0MV1wtW5AaArIhZjgBlRtxLyq9nYmUoPxBhu2CHcAz5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=Fo9RusCr4Ar8fxXAgY3-k4ZCddJa7cW4E7v_EkEJMmeTk4ct9t69A75rZiDG3ut5pyXeQwJeG2lw3CdckhI-nVCeO4KQiWf9vS31ESfe0_0XnexBZITkICK_cfqyGGg2wwXJdJjW8ZIVuaJUyCYPDtYzh6B0M3st6MnSxHCYEgSNvHdV6ZHNJCHIoF09oQ-mAy3Sv3kCegV0u3jqN4voaWCVaAcu2ocEINIf7u4V2XdJDHxCFaTQi7ISXIL-bcC3XHYI_sCFctAY4iTswC3nu6qRT4uuFHAWe_Vs7WKQd0MV1wtW5AaArIhZjgBlRtxLyq9nYmUoPxBhu2CHcAz5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: گفتید این آخرین فرصت ایران هست چیشد؟؟
🇺🇸
ترامپ: به زودی متوجه خواهید شد
ما توانایی افزایش تنش رو داریم
خسارات های جنگ رو از طریق منابعی از ایران جبران خواهیم کرد
خسارتی رو اگه قرار بشه کسی جبران بکنه این ایران هستش
هیچ اتفاق بدی قرار نیس بیوفته
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69862" target="_blank">📅 00:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69861">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=aFQQnoJ-ZewdIUFhTic7XlcmVFFTDx6lb-7tuK3zY8Jgk9hdXSMoHxFKqJ_DIoSBxEaN2q1w-DavOdDMhL718PG2Gc_8aHmLeU-sSY9Fw1UBApWPryEBr8Nj3gdfiFPpX9yNw9WPIb4EoAkgqUA00oTr2W3aWPMmSnWiC3Kwr2ULub_645aIwDrkF34CusxGUIEVNvC9dFlLYvh-aXCsGpSPv57MEdv6vya4EbjUyGj5HDK_t85Fcy09rv_BQv2hJQvDfi72ohiGYnPb3lHaevdgcFsH8wi13tQoS30IXy6L1tvkgq2iBenn3-tXToAyBy8WARjf2xzzBf2lFOm4Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=aFQQnoJ-ZewdIUFhTic7XlcmVFFTDx6lb-7tuK3zY8Jgk9hdXSMoHxFKqJ_DIoSBxEaN2q1w-DavOdDMhL718PG2Gc_8aHmLeU-sSY9Fw1UBApWPryEBr8Nj3gdfiFPpX9yNw9WPIb4EoAkgqUA00oTr2W3aWPMmSnWiC3Kwr2ULub_645aIwDrkF34CusxGUIEVNvC9dFlLYvh-aXCsGpSPv57MEdv6vya4EbjUyGj5HDK_t85Fcy09rv_BQv2hJQvDfi72ohiGYnPb3lHaevdgcFsH8wi13tQoS30IXy6L1tvkgq2iBenn3-tXToAyBy8WARjf2xzzBf2lFOm4Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پس تنگه هرمز کِی باز میشه؟
🇺🇸
ترامپ : بازه!
ما صددرصد کنترل تنگه رو در اختیار داریم.
همون طور که احتمالاً شنيديد، كل تنگه رو مین روبی کردیم. البته شاید هم نشنیده باشید.
اونا میتونن دردسر درست کنن، ولی ورشکسته‌ان؛ پولی ندارن، ایران کاملاً ورشکسته‌ست. حتى حقوق سربازهاشون رو هم نمیدن، نرخ تورمشون 309 درصده.
ایرانی ها صدها هزار نفر رو کشتن، حالا دارن تاوانش رو پس میدن.
اگه قرار باشه خسارتی پرداخت بشه به نظرم ایران باید اون خسارتها رو پرداخت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69861" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69860">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه؟
🇺🇸
ترامپ: شما متوجه خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69860" target="_blank">📅 23:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69859">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=gvYFdoiIQPBP0SNMR1K7udzZYD5TMxnXckkqELADipdPkgL86dxfZpV-QFuxHgl7bBccoA63v_JelLTL9kbkcUBF8qLlfev4CCM1YTQIXOW4KVf902qQrxPv39G1W7x9AxghnzGle84CNiWkWEtGZReLtrurx33OY_FUxyvc70f6B82eIEjfg3jmkM_YdOuRQ7WKVqcqY9c4y71P_fj7p_LXX3AeMynanBHOy5cxoNlZn8xR-dBh_WO_jT3CZA302NWhxQXsfb9TtrCNYdvJg5hXiJvpS22BwrQg7wPpVRkVZoBx3q08W7bNaJt-v-jD47JACPGScDukXqNkNhfkRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=gvYFdoiIQPBP0SNMR1K7udzZYD5TMxnXckkqELADipdPkgL86dxfZpV-QFuxHgl7bBccoA63v_JelLTL9kbkcUBF8qLlfev4CCM1YTQIXOW4KVf902qQrxPv39G1W7x9AxghnzGle84CNiWkWEtGZReLtrurx33OY_FUxyvc70f6B82eIEjfg3jmkM_YdOuRQ7WKVqcqY9c4y71P_fj7p_LXX3AeMynanBHOy5cxoNlZn8xR-dBh_WO_jT3CZA302NWhxQXsfb9TtrCNYdvJg5hXiJvpS22BwrQg7wPpVRkVZoBx3q08W7bNaJt-v-jD47JACPGScDukXqNkNhfkRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
🇮🇷
عظمایی فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
«اگر اسرائیل، ایالات متحده، یا هر یک از همدستان آن‌ها حتی جرأت کنند نگاهی خصمانه به جزایر خلیج فارس داشته باشند، با کمک خداوند متعال؛
چشم‌هایشان را کور خواهیم کرد و خلیج فارس را گورستان آن‌ها خواهیم ساخت.
»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69859" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69858">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=SuWQvrzJXASZkUuT5nUFITp40ygihxdcUIqTP96sLsF_wmz0TDK_DtxBkW8QOxzxoriRNWMOYgHwZjVcFQxPDwUcTv03dA-CW-tXD0biEPlkzN0BwOAWp8yW3ukOLVLlLjiZOxoKAnEQ6yol1l-MoMOHGiT2WyFH4gGEQIAv4WeMtV5WIJdxy_wNyBRRVHEs2LvBYOt6gbgHugC8bbHoA7ZAS9hVTebtxVxZKQXCoTkXaoUG7dmmsRefI2FxofOVkium56hsSiGBOPnteX3oWR3meGyrxwIZ8znZeCEXgV2d_J2CSPOVxghEfom7nLaeD9GhbFrbOb_7x5HZ63rRuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=SuWQvrzJXASZkUuT5nUFITp40ygihxdcUIqTP96sLsF_wmz0TDK_DtxBkW8QOxzxoriRNWMOYgHwZjVcFQxPDwUcTv03dA-CW-tXD0biEPlkzN0BwOAWp8yW3ukOLVLlLjiZOxoKAnEQ6yol1l-MoMOHGiT2WyFH4gGEQIAv4WeMtV5WIJdxy_wNyBRRVHEs2LvBYOt6gbgHugC8bbHoA7ZAS9hVTebtxVxZKQXCoTkXaoUG7dmmsRefI2FxofOVkium56hsSiGBOPnteX3oWR3meGyrxwIZ8znZeCEXgV2d_J2CSPOVxghEfom7nLaeD9GhbFrbOb_7x5HZ63rRuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه مختلط تو قیطریه تهران همراه با استخر جکوزی سالن  ماساژ سالن بیلیارد سالن بولینگ و...
😟
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69858" target="_blank">📅 22:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69857">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTUJ0JkPDMGkCeDe1XqDXXZrVdkLLO292xY1pS9tQi5pjnndHlvJ8RWWzpvod0EqwxIWXWdTd1rAQ8Ofkf31ydkWPQGpzF6-C_81ksEZEgBLRC__uQbXA3CBJ_Xv6KSZTo9HBiI883GgFldnSG_I2R4AVUtEEoW75GXRqNuliIUEPTP2MO6YGYaBt6FTYM9LTsLe2Je1RlUWFBcglJy34LoIV_s35PRYxmiHFnMaObFs4HmKwESbn7xNuRDuAMzj-gcbvGEEyYiLmprMB5-u24LOkkhmvH09bxdGftVy_utsekK1kIVcWRPUdb7HW9xTtkWtnuxT8TwV4mHxdn_nFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:   می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69857" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69856">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=Ye2Llpos0Y26B-sviIDKjaSUbvCn3QCccnKHTHQkrfCk8xC0KnVwpo7QR9k-76Z_6F_IhY-PBAKJ41342kifLR6kN8iwoZ4w5FzA-kt8sRfuLILQ7YF6gPVg2ao-5XQ4tWB9XQMPi8JEkbkxNnAqU4LciH7XMcQPjxfKak1ltjMSDvupJyOCZG37_qzS2b08IAJfSzJSgy0tJp7YH2pFVPIQlVUzgUyIDJOiQek9hPHjWyFB4sRw9IOzEsuurAfKsfmAni4A74NudBarWucGmRp4gfOQzUpRdACkyV0KxGpv2ctNeQPQAgZvYEpp42NXI-xcuN5KKGqLDi0UtQIlVwW7yIC3jpbVkU9rP60YfGf_9tnZMz7nwqVSunpRrOHiaEyS5QexRBgL4P9lMFteDejI58SUrlCS4KGibsXZwPPKehh06iZ77Wp1X1s5lHfXvc5yLWOm8UIgSrD_TOtMO-kMswBHw55lNRMUXySN3d1kBhYSsdlXEfkvjd7hq6vAA2w-8HyBR6JVmR7YzYX0Wscx4yTA-pQjlgZ9dYT8-e7uHps6SZEnomA9zK5RuuiDuXQChWUt69a-qzMMASBVTxrKmDFT5FRMgSng3fzHF7pyMD2J36PJo1JpULfCgSFVqUSJTGuhNNncL9HEhnOowo7875jvUtu3nJSo501dHqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=Ye2Llpos0Y26B-sviIDKjaSUbvCn3QCccnKHTHQkrfCk8xC0KnVwpo7QR9k-76Z_6F_IhY-PBAKJ41342kifLR6kN8iwoZ4w5FzA-kt8sRfuLILQ7YF6gPVg2ao-5XQ4tWB9XQMPi8JEkbkxNnAqU4LciH7XMcQPjxfKak1ltjMSDvupJyOCZG37_qzS2b08IAJfSzJSgy0tJp7YH2pFVPIQlVUzgUyIDJOiQek9hPHjWyFB4sRw9IOzEsuurAfKsfmAni4A74NudBarWucGmRp4gfOQzUpRdACkyV0KxGpv2ctNeQPQAgZvYEpp42NXI-xcuN5KKGqLDi0UtQIlVwW7yIC3jpbVkU9rP60YfGf_9tnZMz7nwqVSunpRrOHiaEyS5QexRBgL4P9lMFteDejI58SUrlCS4KGibsXZwPPKehh06iZ77Wp1X1s5lHfXvc5yLWOm8UIgSrD_TOtMO-kMswBHw55lNRMUXySN3d1kBhYSsdlXEfkvjd7hq6vAA2w-8HyBR6JVmR7YzYX0Wscx4yTA-pQjlgZ9dYT8-e7uHps6SZEnomA9zK5RuuiDuXQChWUt69a-qzMMASBVTxrKmDFT5FRMgSng3fzHF7pyMD2J36PJo1JpULfCgSFVqUSJTGuhNNncL9HEhnOowo7875jvUtu3nJSo501dHqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله تند مجری صداوسیما به علی دایی:
وقتی جرائت نداری جیگر نداری به دختر اونور آبت چیزی بگی پس اینجا هم خفه شو لال شو
یه گروهی گول میخورن میریزن کف خیابون بعد از این دایی و خاله ها زیاده هشتگ نه به اعدام میزنن
یکی از این آقایون مشهور دخترش مورد دزدی قرار گرفته بود کم مونده بود دزد رو بکشن بعد همینا هشتگ نه به اعدام میزنن
بعد این وحشیا این بیشرفا جوان مردم رو به شهادت میرسونن یه عده یاد حقوق بشر میوفتن
اعدام نفرت نمیاره شماها نفرت انگیزید شماها ترحم انگیزید
ولی یه پلیس یه گلوله شلیک بکنه داد میزنن عای دیکتاتوریه عای خاک خون کشیدن
شماهایی که لال هستید همیشه لال بمونید حتی اون ور آب
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69856" target="_blank">📅 20:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69855">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-5Xo_4aRnOPezskv1TFwztn6LzsBx-GhhC1cZm8Gf6713eCfYxf3H53pbo3WU4luBk2K_9D0YgQxvGP6hwZZ5C7-FHRJ8tLupBMFy1L8de3s14oa-QhL706ci6VlvCJG7S46SK4ro6YpRkOEw1twkwduQZyRW-SDND3snn27cn-fJp7P25HY1V2yqp84cRwaTgj0eVbF-XWkO1bHlG3FAMmXxMZyeExLl8py6kvhepzaVsLMXOiua32aJ56JnvGAXS1c8zm2-WexymFi0-cas6iDevaNtYbOzCCiBmI2LQloaCkjiWfaYbglcSp3ZK2Lv2qGuJRWKIOG6fZiDhLnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما این ایده جالبی است، چرا که من نیز اکنون متقابلاً از ایران درخواست غرامت می‌کنم؛ غرامت بابت تمام کسانی که آن‌ها با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد — که به آن شهرت دارند و در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد — به قتل رسانده یا به‌شدت مجروح کرده‌اند؛
از جمله خانواده‌های کشته‌شدگان حادثه ناو «یو‌اس‌اس کول» (USS Cole) و هزاران نفر دیگر که در میدان نبرد جان باخته‌اند. به‌علاوه، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته به قتل رسانده نیز غرامت پرداخت شود، چه رسد به آن ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
من به نمایندگان خود دستور داده‌ام که این موضوع را قاطعانه در تمامی مذاکرات آتی بگنجانند.
از توجه شما به این مسئله سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69855" target="_blank">📅 20:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69854">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A38l0vNEEwBhpGli8xCXJPKzAKnZkEJibOiEM6aAxqHVK7t9aPQjPRod5s4iUXFgRz-HqYkrHHVfw7gxuNgQs4TtzOPQYdwU3dKugb4Wgx6GbkZt3FgnBULK1YmkLAL6U5nPIqZdAGWl0YhkDHbRxqko-uVGd5GjYbfSKPcbF-hh-irxt8YtEoR6VNRUyFn1Rgs7CdXgu-39ANjSncrYE8jfOekOM49zyxCdQo7CzSj5mn5pBxCtGaAZ1pBYloeOp7aVcIFgmSrSoPmYBQpj4Q2vBzWmdSL9sJotIUveen52POu8G0p2gGmf8d0YuTTIltApTnsNjn653pEDMiNeuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مرندی:
‏ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه - احتمالاً در کنار نیروهای اسرائیلی - علیه مردم ایران هستند. جمهوری اسلامی با پاسخی سریع و کوبنده آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69854" target="_blank">📅 19:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69853">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🔴
🇮🇷
لیست فرماندهان جدیدی که مجتبی خامنه‌ای انتخاب کرد:
سرلشکر  علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح
امیر کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح
سرلشکر احمد وحیدی به عنوان فرمانده سپاه
سرلشکر مصطفی ایزدی به عنوان جانشین فرمانده کل سپاه
حجت الاسلام طائب به عنوان رئیس سازمان بسیج مستضعفین
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69853" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69852">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=irXOhxqmfBs3xJSoU3XruM6BRDq2N7a7NiuAmq8-PgecPIdv9dNsd5JrmnJ-9od43Ox8NEFMElYs2cZQ8dU3E49pAQCTbxtrcpZPZCSwWaQKFoVnEVJb0hmRDu_9GcJ-UAy4zknP1jXVHOvlUhQlGZCHHRTA1tYEc36UpH7rBpnbuCmrd8Wfogwqk9rAWusY38n-ntAlEuq2nnDzi_Wfxcs-vRmGsx_J1xr8QYPU69UVeW2MCKB0NDTk_s8TuohW9gX12jxnkl-JTL3JVm8s1Qg9-7xsRX3xc6gZRrdjRJ86iP5pReyKhKf3PgAk2t19iJ_x_VTnkBO1EZ65LSbmCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=irXOhxqmfBs3xJSoU3XruM6BRDq2N7a7NiuAmq8-PgecPIdv9dNsd5JrmnJ-9od43Ox8NEFMElYs2cZQ8dU3E49pAQCTbxtrcpZPZCSwWaQKFoVnEVJb0hmRDu_9GcJ-UAy4zknP1jXVHOvlUhQlGZCHHRTA1tYEc36UpH7rBpnbuCmrd8Wfogwqk9rAWusY38n-ntAlEuq2nnDzi_Wfxcs-vRmGsx_J1xr8QYPU69UVeW2MCKB0NDTk_s8TuohW9gX12jxnkl-JTL3JVm8s1Qg9-7xsRX3xc6gZRrdjRJ86iP5pReyKhKf3PgAk2t19iJ_x_VTnkBO1EZ65LSbmCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇫
طالبان به طور رسمی برده داری جنسی زنان رو قانونی اعلام کرد تا محدودیتی از این لحاظ نداشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69852" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69851">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69851" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69850">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI-77OW_Jg7ZZBBhJmGmJe0eOhrkygTrqLipSnFhuq27fUUIMlK8eW8ChivDYVpcBkk0br6t5spsyjFtd_T8l7Z9t-uYwz7Du3jWAqdh-qbcLwgsesm82OuK_6OW6Eo1bJ2-wno7ugAT7BL9-1kC6rCrQZJeDeTVCIRUQ49UuEBFVe3tD9bqfUTsHfRPxrBBNoctwt1qg0qQSS_e2UYwF6WgLMrdMDfD7nEFb7hphpBBa7-X3l_8p1CnG6QZtra3GWE1e3Fn2ghIFL_kq-tgXcOBrHz43Km4il6HEAlKgMcUpJ2nOKRXgfKr4stoJptNLp4GbmUpYPd2JNGFRxUGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69850" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69849">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
⭕️
مجتبی خامنه‌ای تا ساعاتی‌دیگر اسامی فرماندهان جدید نظامی را پس از بیش از ۵ ماه رسما اعلام‌ خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69849" target="_blank">📅 18:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69848">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=sUSubnQcbxhk13uTN25qGQqsKJZtrAGlIf_OSZr_LHUheHfAimuPxaUj4pF4QxKgbo0j41ZE1RP75PhEtTH3CcgHtS65ZaOne0SOxRHJZ6PkoDrS3xj45Ts7V3Aqzf04BRw3vHA11hkDlTZZbf3IfTI8TLJCJO3qn9CHqBMDGzrJOreCO8wbgmv0pfP7auF1RIr6VKJ66VCTI-kIuIjRft_5yGmT3Dhi2OGVCxGuIvIYchi03PbHs58hbptCtmoufbGERjGrn8Z-mLfc73UJPqlEnkgC7vTtJ44lXuBb3rDJwTaSwBPCnenQ2DXJ5ZR-0yWZe4m_eHrZr2R-wBAHrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=sUSubnQcbxhk13uTN25qGQqsKJZtrAGlIf_OSZr_LHUheHfAimuPxaUj4pF4QxKgbo0j41ZE1RP75PhEtTH3CcgHtS65ZaOne0SOxRHJZ6PkoDrS3xj45Ts7V3Aqzf04BRw3vHA11hkDlTZZbf3IfTI8TLJCJO3qn9CHqBMDGzrJOreCO8wbgmv0pfP7auF1RIr6VKJ66VCTI-kIuIjRft_5yGmT3Dhi2OGVCxGuIvIYchi03PbHs58hbptCtmoufbGERjGrn8Z-mLfc73UJPqlEnkgC7vTtJ44lXuBb3rDJwTaSwBPCnenQ2DXJ5ZR-0yWZe4m_eHrZr2R-wBAHrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره مجری و کارشناس‌های برنامه به وقت ایران:
این همه علم رو از کجا آوردید؟
چندتا جوون نشستن رو صندلی و درباره اقتصاد، سیاست، جامعه شناسی، کشاورزی و... نظر میدن.
از چهارتا جا یسری اطلاعات ناقص می‌گیرن و بعد درباره‌اش حرف میزنن و نسخه می‌پیچن و جامعه رو منحرف میکنن.
من 18سال تو دانشگاه درس خوندم و استاد تمامم، الان فقط اجازه دارم درباره یه گوشه قلب که تخصصمه نظر بدم نه کلِ قلب، اونوقت اینا...
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69848" target="_blank">📅 18:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69847">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=rCJC8p-bwrXT-Lmmjcbn8kI-svu3soCWQ4i_CuRGPhmnuGut3DgFGN5Q8GjJbgajxwzJYC7POObu9ENKhF6r_YXEDeREGAgxH2g-bDMhckFr3Bdmzq9gLnuur7FEw9rkZ5fIAu5AG6dtxOaz-40eqmp0ahWIfULtSVsjdoTNd02caRLsWVoZWiHGMW6S7AoD5YoVSwF9AP8t3MZ-zoMwPFafW6ZDYdVfVQ9pcrFPtA0CFwQv4YeYL8GmSaDc_2uwq_BMJU1Z5zCoiDdbUCaDB9TZbzsqrcch1fkZ9IGU2ibsqMjY5Gppi2mt0vCX969tt9DjlO1r3GBVD2tobGjPng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=rCJC8p-bwrXT-Lmmjcbn8kI-svu3soCWQ4i_CuRGPhmnuGut3DgFGN5Q8GjJbgajxwzJYC7POObu9ENKhF6r_YXEDeREGAgxH2g-bDMhckFr3Bdmzq9gLnuur7FEw9rkZ5fIAu5AG6dtxOaz-40eqmp0ahWIfULtSVsjdoTNd02caRLsWVoZWiHGMW6S7AoD5YoVSwF9AP8t3MZ-zoMwPFafW6ZDYdVfVQ9pcrFPtA0CFwQv4YeYL8GmSaDc_2uwq_BMJU1Z5zCoiDdbUCaDB9TZbzsqrcch1fkZ9IGU2ibsqMjY5Gppi2mt0vCX969tt9DjlO1r3GBVD2tobGjPng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی (1392):
اگه آمریکا به ما حمله کنه ما همون هفته اول هزارتا آمریکایی رو اسیر‌ میکنیم و بعد در ازای آزادی هرکدوم چند میلیارد دلار از آمریکا پول میگیریم و اینطوری مشکلات اقتصادیمون هم حل میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69847" target="_blank">📅 17:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69846">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=oSBr66czltSTf7awUJ2FGZaGJ3xnE2gdEPUju4fAy_ILoAP-GyTiVnK5ddrU5Kte20y2B-KkOJbmIfmYnnSSdmHrbfBLCoFeqKvAc2pc7Unbgl_q55xVR6hxwi2AIj8FZ-ZvxM8u0BiRSFRxc5UoXr892I4_w4hWWmEljeqffRPOmW064V_Y81nKhoOHq8uyD3Y8yOUKCWyNfb4Si3vFvJ6zsKnmfsTJbWF-8anQ4Xc-2UGX_L2-iA-xYO4en1XKbTw2fy1nJpJRDY_f1C6fXaDzoW16SFR7soW4wBMmsi1Y-FBWf0vPlhAi1Fdwu7CIDzE72EOsZI32no-eVOpb4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=oSBr66czltSTf7awUJ2FGZaGJ3xnE2gdEPUju4fAy_ILoAP-GyTiVnK5ddrU5Kte20y2B-KkOJbmIfmYnnSSdmHrbfBLCoFeqKvAc2pc7Unbgl_q55xVR6hxwi2AIj8FZ-ZvxM8u0BiRSFRxc5UoXr892I4_w4hWWmEljeqffRPOmW064V_Y81nKhoOHq8uyD3Y8yOUKCWyNfb4Si3vFvJ6zsKnmfsTJbWF-8anQ4Xc-2UGX_L2-iA-xYO4en1XKbTw2fy1nJpJRDY_f1C6fXaDzoW16SFR7soW4wBMmsi1Y-FBWf0vPlhAi1Fdwu7CIDzE72EOsZI32no-eVOpb4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی سمه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69846" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69845">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=I-zYSj0I0FWokjvPEws0psPCQO5L9vy69WBWAfHwvOlsnmxStphmV5cEi92r1y-jYVJDny-HYVfhy4VyXYnzddmKIBae-vVZEM7Z_Weu9BJ33UbxgWpwiK1hSYZdYUSI9WfZp-Lng7OceQ8CHLnGlENIM_YPWoEr6Lp3tynSvLrATkqxEM3RYDImpO40D3tZtbVTg2gL2KpGr2AwejI-dQjyjiui1kQ6gVToUpmIYiPC3pQeYPHaAiA1JlMiHw3lhcaZs_MrmMdm7Ft1lAaj76e9WctDlLCHAM8ZOqo5xB4t2BRpCcdR_RzuY4OFAXVROAHqchE884J712LS732M-BDXWcJaHbrZaTmIrQqCv54ioPxbYAUef7DFAUMF3U-V_0E7qmFXDIxZ9NLIMyaMMWBxUnxSC-mTR8_2IPaI2qHqPmTBTkl0ZuEkmg9fWGy-68QZmFvYrgpByQVQAF24txKgTvVX_hxUCY1IFgbz8XWSTcvFMZ1g0YwYrHgCilME7QJ_CcZs3jmYQhUTlPOO5XGrhox0HfoF6ewo2cmdlhPyelBw_zlJe5xvj8a4rfoAqUG6jjafAUmd-W_iXX-6Tt7-eMq_AfTH2P-pB9G42u2d-lg3zaKlYskwCyFGP3Ms65yR1_gZZd25bHJdYLuzKcYGIEA5rmi8yHo5Rhvofps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=I-zYSj0I0FWokjvPEws0psPCQO5L9vy69WBWAfHwvOlsnmxStphmV5cEi92r1y-jYVJDny-HYVfhy4VyXYnzddmKIBae-vVZEM7Z_Weu9BJ33UbxgWpwiK1hSYZdYUSI9WfZp-Lng7OceQ8CHLnGlENIM_YPWoEr6Lp3tynSvLrATkqxEM3RYDImpO40D3tZtbVTg2gL2KpGr2AwejI-dQjyjiui1kQ6gVToUpmIYiPC3pQeYPHaAiA1JlMiHw3lhcaZs_MrmMdm7Ft1lAaj76e9WctDlLCHAM8ZOqo5xB4t2BRpCcdR_RzuY4OFAXVROAHqchE884J712LS732M-BDXWcJaHbrZaTmIrQqCv54ioPxbYAUef7DFAUMF3U-V_0E7qmFXDIxZ9NLIMyaMMWBxUnxSC-mTR8_2IPaI2qHqPmTBTkl0ZuEkmg9fWGy-68QZmFvYrgpByQVQAF24txKgTvVX_hxUCY1IFgbz8XWSTcvFMZ1g0YwYrHgCilME7QJ_CcZs3jmYQhUTlPOO5XGrhox0HfoF6ewo2cmdlhPyelBw_zlJe5xvj8a4rfoAqUG6jjafAUmd-W_iXX-6Tt7-eMq_AfTH2P-pB9G42u2d-lg3zaKlYskwCyFGP3Ms65yR1_gZZd25bHJdYLuzKcYGIEA5rmi8yHo5Rhvofps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
تنگه هرمز از زمان حضرت آدم تا ۹ اسفند برای همه باز بود
ادعای ساخت سلاح هسته‌ای ایران توسط نتانیاهو دروغی بیش نیست
به ترامپ بگم که ایرانیان شطرنج بازان حرفه‌ای در طول تاریخ بودن( ترامپ جنگ ایران رو به شطرنج تشبیه کرده بود)
هیچگونه مذاکره مستقیم با آمریکا نداریم
باز شدن تنگه هرمز منوط به لغو محاصره دریایی هستش
نگرانی بابت پیمان دفاعی مکه نداریم چون همسایگان ما هستن
بحث کنوانسیون دریای خزر به مجلس ختم شد و تصمیم نهایی با اونا هستش
درباره عمان نزدیک به یک تفاهم هستیم و به زودی نهایی میشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69845" target="_blank">📅 16:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69844">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=E6IRu2Tvvbd693-U81_BftctcP0u30rJFbOmwC60X81Cjas33LUWcVcrPVzgHoKYIQ3RA5tfUqJYIOsOTBnARJoDCwFVB2uRnI7A_o4E52hiU06eRAi-kKT7_JRDOiXzAw6mWrwkbuysA1M2VJSYURkT1aJKb5q_Emu8rY8Rw6kGVRl80C1eCCzvbb7jmIopEMCh4dcDAYlsDVgqQw4qFuCgkPLoYJrUzl65EnX9E0GqwfzGQyEgiv1xreLiUC_lqZf9GBzuFRHge_YkVpUeMFrnDSUuWoN7dYL0q2gPhY4Ys4kZgexmqmt41ei1SAXOtLTndSBHJzbvHagErV_qGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=E6IRu2Tvvbd693-U81_BftctcP0u30rJFbOmwC60X81Cjas33LUWcVcrPVzgHoKYIQ3RA5tfUqJYIOsOTBnARJoDCwFVB2uRnI7A_o4E52hiU06eRAi-kKT7_JRDOiXzAw6mWrwkbuysA1M2VJSYURkT1aJKb5q_Emu8rY8Rw6kGVRl80C1eCCzvbb7jmIopEMCh4dcDAYlsDVgqQw4qFuCgkPLoYJrUzl65EnX9E0GqwfzGQyEgiv1xreLiUC_lqZf9GBzuFRHge_YkVpUeMFrnDSUuWoN7dYL0q2gPhY4Ys4kZgexmqmt41ei1SAXOtLTndSBHJzbvHagErV_qGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
پزشکیان:
با رهبر هفت ساعت دیدار داشتم و درباره مسائل مهم کشور باهم گفتگو کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69844" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69841">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU2NWgCbgISvNEC9OZW9qrHIpmSkVuvPKsWkQPTNL4NoPPE6s9VqvIAQZVcjWxOTgP2WvweDxrYifU3CSYeOjOVC70hmIWaL_vitODkZEEgLjzDJ43Y-22X8oMaZmzjcTm0Nh_0lJAqUJ8IvzcYkR53dkdbLcqPWdNZRu00qb-HIBo1IW-u5OEeUJ0NqaaD6daMDHNecd9y8AjccFeFKEOQDOVnuFKuzyrfzsrbPbD_YJwttR-vV3WXUousZL8EhqZTSgBfntwiOI2QQDqzYxuWXAWEDPbj4y9m28b2I9PIXvwS3ihvP0ooZ0WqZa1aOvGATa5nj5xqdkL3QgZYZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hk8AR3J31RcoW-ZlqRQw8q80ami_d7BeL4piNRYRbsoXRBn7y-v21UvOtUFiQhDyLYgw4z0fUxb9FTKHHFWeOkj84n1D0mnQ93XrKTFGfjRE3yb2qEmeNtAcnG2Eps3HZUHxstype58a4eZxZlbAbu6jK_BJ45BLc_JLSZpVky8NpOLWX6BgIrEzXxEvXZ8xRl3mK1-43BQqMxqZf_TknRy9LEKBiLI_BkeotStFvSVrEJo-E8Seo656f3y9nXr6vce1oGwrb5Z3dXA6toFgB-GG8_6HAaK5FEqBvP-oi37XdbRg_In_X3ooo8t0shwB9rNN25WoObme4j4pKCLJhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92217bf769.mp4?token=MQCllTREl_1z8yCXu1zoCrVpVTRifHpp1z1CbYQThKx1dWaRv_xNOAKC1XOEoi0Debs8mLfzosaOcqydDroqY9rSqHoNeMpqg850ac1hMMnEQB_gxwG_vhZyeBGTrWtkRgSDZ9jO4AfNqpKyRTqw44MkoV-Zz4d7mUAtpLR_mOFkRF2McSTM6V9O1V0PAzOvPowFnme3-9peClg6sn3m_IE6RG0qgCeR7OyeYH0BHT97lQ96ajfnI93pzbVDcg7keEMnwH7esZWCXz4lI9-fk2OuEzBDIrl6iJ2eiXYvGlxrjMToZE117K2Wdr-rPUmOzKDcCSrj67YX2Crwsb3vrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92217bf769.mp4?token=MQCllTREl_1z8yCXu1zoCrVpVTRifHpp1z1CbYQThKx1dWaRv_xNOAKC1XOEoi0Debs8mLfzosaOcqydDroqY9rSqHoNeMpqg850ac1hMMnEQB_gxwG_vhZyeBGTrWtkRgSDZ9jO4AfNqpKyRTqw44MkoV-Zz4d7mUAtpLR_mOFkRF2McSTM6V9O1V0PAzOvPowFnme3-9peClg6sn3m_IE6RG0qgCeR7OyeYH0BHT97lQ96ajfnI93pzbVDcg7keEMnwH7esZWCXz4lI9-fk2OuEzBDIrl6iJ2eiXYvGlxrjMToZE117K2Wdr-rPUmOzKDcCSrj67YX2Crwsb3vrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دیروز عراقچی برای مهمانان خارجی تو ساختمون وزارت خارجه بساط تعزیه راه انداخت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69841" target="_blank">📅 15:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69840">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=s8k6WLGN_JbVk2zgPhqIRbO0cqACH8z04UDrfnYM5LtmKQe9P9f-Ur9YB-9DCT61s3TL-bUvRzPHWrdaULOX7SCOYF-dp3QiT9aBNCMY4fRwblu6biexGnjxvKvvY7db3sP9EbD6rnvGNHgm_-T4d9Xn-wrdx-_YXkgb90auPLG2lKwGu_UDacEs4NMdBGQsGiNAnEdZDO1bYftm2guKiUnzpQqIDyAHxih7GjFxuBv9qnCrqzl3qOcORRGi9mp4IgDcB3XX7svLWcx7rg1CXaFOT7HBhGHZByXmH_dyEKAciNGu7mmkiE9y-ihTT0tCO2xkXAiEvnUsvejQQ3sEvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=s8k6WLGN_JbVk2zgPhqIRbO0cqACH8z04UDrfnYM5LtmKQe9P9f-Ur9YB-9DCT61s3TL-bUvRzPHWrdaULOX7SCOYF-dp3QiT9aBNCMY4fRwblu6biexGnjxvKvvY7db3sP9EbD6rnvGNHgm_-T4d9Xn-wrdx-_YXkgb90auPLG2lKwGu_UDacEs4NMdBGQsGiNAnEdZDO1bYftm2guKiUnzpQqIDyAHxih7GjFxuBv9qnCrqzl3qOcORRGi9mp4IgDcB3XX7svLWcx7rg1CXaFOT7HBhGHZByXmH_dyEKAciNGu7mmkiE9y-ihTT0tCO2xkXAiEvnUsvejQQ3sEvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از قیمت یک پک آرایشی که ناقابل سه میلیارد
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69840" target="_blank">📅 14:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69839">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO4TxzKbMhiLuwuBSYvDrASTXvNYQZOdMBd2jrvYfhduq7OfA0u5ebkUD4xUTODX2FsbCnQp6ZKAGLNvMxoiLYueigQooGBNSUrNbECu_odfd_-Qp547f7WeMrUv0tCy8N_HfSC597F_wVxx9146d5Og5H1hDA8qyRI2nCLCxhnxk5p6TH2a7DO6aWNRWEm-ZtEJOI99Bbz4jg8_ojf1VCmcmfoQ6KDEgRSQGWUo2LtEKd09lnNEqR3YJwR5mA81PwU8fVsrcViviqgAodjHRzaB-Kz9sQixTzogapzlfk5oX-inX22-veL8cGp6VlR-QGBqkaeKE6zIZcakKRQNEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «ناراحت نیست» و آن را بخشی از فضای انتخاباتی اسرائیل می‌داند.
این مقام آمریکایی گفت: «ما نیازهای سیاسی "بی‌بی" را درک می‌کنیم. تا زمانی که او به انجام آنچه ما می‌خواهیم ادامه دهد - به‌ویژه در خصوص مهار حملات به غزه - مشکلی با این موضوع نداریم.»
به گفته یک مقام آمریکایی، نتانیاهو هفته گذشته در تماسی تلفنی با جرد کوشنر، فرستاده رئیس‌جمهور ترامپ، وعده داد که علی‌رغم تردیدهایش، به این طرح ۱۵ ماده‌ای فرصت دهد و حملات به غزه را محدود کند تا روند خلع‌سلاح این منطقه بتواند آغاز شود.
از آن زمان تاکنون، اسرائیل حملاتی علیه غزه انجام نداده و ارتش اسرائیل (IDF) به‌تدریج در حال عقب‌نشینی به سمت «خط زرد» است. هم‌زمان، آمریکا و میانجی‌گران خواستار آن هستند که حماس روند خلع‌سلاح را آغاز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69839" target="_blank">📅 14:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69837">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=lWgvYDW1v6HgIZRlvLkggRH6o8SxH2aYGydPcPWMD89-bWCcvG3cNh5B6s9xzFPpXpiIPYs8GkH1JWzfHEpUVA2e_pSiS73OhREAkA5mpZ6cd07j3nzbyMoc33bWuzDBJUCdYkHweCMCipt-qLy9BHklZKCc_n3qvyGNRhEIGeEgBE5-ZIL_guO-bxMPlTlNxnH_MDL4HmMwWrK0KXcgyLHU4jkT4UwOQUyP39pOxbjL7AaTA7oydtr4DdCMwE1Kc6y2ZhCy-Zbns3pNE7LKGvx_R4cCi32sOPmloOTQff3xYPlf9jhpFVKmZPt7MhIEND3Sw1GWoVw1glI0yLfcvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=lWgvYDW1v6HgIZRlvLkggRH6o8SxH2aYGydPcPWMD89-bWCcvG3cNh5B6s9xzFPpXpiIPYs8GkH1JWzfHEpUVA2e_pSiS73OhREAkA5mpZ6cd07j3nzbyMoc33bWuzDBJUCdYkHweCMCipt-qLy9BHklZKCc_n3qvyGNRhEIGeEgBE5-ZIL_guO-bxMPlTlNxnH_MDL4HmMwWrK0KXcgyLHU4jkT4UwOQUyP39pOxbjL7AaTA7oydtr4DdCMwE1Kc6y2ZhCy-Zbns3pNE7LKGvx_R4cCi32sOPmloOTQff3xYPlf9jhpFVKmZPt7MhIEND3Sw1GWoVw1glI0yLfcvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فوران یک آتشفشان قدرتمند در جنوب غربی کلمبیا
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69837" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69836">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=TFqn_2pBaSFSdN_hx1HoIOqhppxVZMXXU5DS-cXXA8oHerCMrSyZKDi5SMhcUN2FRWukXGyDM8EUtDnW8KMFoss3TH3zpwI1exu-51_DMy3jg4Qc3snqRlc1kbJ3N_TecHhQrXUrbfPSVl5iKTBet03HfAeSJ1FRL0JbkIqffPEMK4Pl9GqkMZQ5aE6bAf2hI38dVrNWbmmVXbOyJ7xkNTZ1dFm_06Gm-yT8tz5YNUvnWWuAv7MpAVoe3e0C1VOkdut_rszREbGO5SaFoCzrRLA7Zisa9wVr2-mPKjKJw3PEmNbs_3xla2p5c6dk9cKxRupLa26_d_VeD4Ep6Wu-mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=TFqn_2pBaSFSdN_hx1HoIOqhppxVZMXXU5DS-cXXA8oHerCMrSyZKDi5SMhcUN2FRWukXGyDM8EUtDnW8KMFoss3TH3zpwI1exu-51_DMy3jg4Qc3snqRlc1kbJ3N_TecHhQrXUrbfPSVl5iKTBet03HfAeSJ1FRL0JbkIqffPEMK4Pl9GqkMZQ5aE6bAf2hI38dVrNWbmmVXbOyJ7xkNTZ1dFm_06Gm-yT8tz5YNUvnWWuAv7MpAVoe3e0C1VOkdut_rszREbGO5SaFoCzrRLA7Zisa9wVr2-mPKjKJw3PEmNbs_3xla2p5c6dk9cKxRupLa26_d_VeD4Ep6Wu-mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتیبانی سنگین و فوق العاده از نیروهای زمینی آمریکا در جنگ افغانستان ( طالبان ) توسط بالگرد آپاچی ۶۴ با توپ ۳۰ میلی متری M230 Chain Gun
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69836" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69835">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=roHXBo4Tm7jEIVtD5ypabD5CIpt4GJIe3aoRtr1m8kihe4rRzg6-ip4DuLMg3nyRmPBUfgTnrUIudDwi9ePnWkXJ1VHJHPZQ1w6VIgiQPoX5LHuV-uslLQRiFA6hMkjiUz2MOSIakPd92_yswciWyXLuqY9JVOEaUjKM7OPditUyTwJFWju12CQxpXih_tfzwYnwJQeQWGb-5R9hCfhaKOmv6eQa5NpO0453aaOi4gbOS4-DpzR2hcU1Jri-S4LR9fZzKrcMCVO0KzjBf72ONMFF_TIyRXzZueS7sOB7O_TEdoAq6i2YxmST0zElNwGrTCZmFf_QilyKMls8QVJIPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=roHXBo4Tm7jEIVtD5ypabD5CIpt4GJIe3aoRtr1m8kihe4rRzg6-ip4DuLMg3nyRmPBUfgTnrUIudDwi9ePnWkXJ1VHJHPZQ1w6VIgiQPoX5LHuV-uslLQRiFA6hMkjiUz2MOSIakPd92_yswciWyXLuqY9JVOEaUjKM7OPditUyTwJFWju12CQxpXih_tfzwYnwJQeQWGb-5R9hCfhaKOmv6eQa5NpO0453aaOi4gbOS4-DpzR2hcU1Jri-S4LR9fZzKrcMCVO0KzjBf72ONMFF_TIyRXzZueS7sOB7O_TEdoAq6i2YxmST0zElNwGrTCZmFf_QilyKMls8QVJIPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پرستار از اتفاق عجیب شب زفاف یه زوج میگه:
ساعت ۴ صبح یه خانم با خون‌ریزی شدید به اورژانس منتقل شد و اول فکر کردیم
سقط جنین
اتفاق افتاده، اما بعد مشخص شد مربوط به
شب زفاف
بوده.
خون‌ریزی اون‌قدر شدید بوده که مجبور شدن بیمار رو
جراحی
کنن.
⏺
پرستار توصیه کرده زوج‌ها برای اولین رابطه عجله نکنن و با آرامش و احتیاط پیش برن تا به این روز نیافتن
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69835" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69834">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=k3HeX2TbsJp-YgCBlNd0RB7561kWEYWvdKf-fdoppz10uwir_T8LKK-MrqkXPXXB-PbKtrdGyGjzw-yYkbcguMtY8esVFlmVfFv0Qe8hgp6srOpgUH6ZHhNNVewiHcRhW_CNDm9n21qgTqfXyJwcEkt3xktxaqd2UNVxGjTMpLs_dGIPWt5_Y53hOlejM9gQlEWiAA-ZS4ku3JGp2Wf2wVunBD3ZK-930-3l2boFOFSkx1ECzzY09G-74Xp1kq8m8aLquR35N0af05LpO447bImHKBTVKLgVw4ECAmPGdArGdvGcYgLgnEeVu2WYVYt4oe7KUu2S6unhRF7n-RHDyKN2Yolyzx5TfVM1RIlfyHY4phpCvxhZ5-tAueyfpW87POFzlyD2Alm--PBzxLUfDJbK5J_6JDhj4Y5n6wHFOBTHErSgc-OZxtp4I5vhLXu4iEIqimsHJMyixJjbkuP27NsTaO5m9vl-rBqQ96uO_hScMcUHkGpt7ZTytdl3-z40UjcEzLSXMKuKzql8oob92wCP5R6YXke6lhfqKpiX8DOgxOSiC7oTfFhkcG-KOHBkvEBTDtO0z_XP9xfPFp4AYpKu8-870myJ-Hz2ogzVlOrvp4FCCS38VMA0jYsNyzW3hqZ0d1e14ZtrGI8tf30zncrStpH2SlV-eBBo6my0O7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=k3HeX2TbsJp-YgCBlNd0RB7561kWEYWvdKf-fdoppz10uwir_T8LKK-MrqkXPXXB-PbKtrdGyGjzw-yYkbcguMtY8esVFlmVfFv0Qe8hgp6srOpgUH6ZHhNNVewiHcRhW_CNDm9n21qgTqfXyJwcEkt3xktxaqd2UNVxGjTMpLs_dGIPWt5_Y53hOlejM9gQlEWiAA-ZS4ku3JGp2Wf2wVunBD3ZK-930-3l2boFOFSkx1ECzzY09G-74Xp1kq8m8aLquR35N0af05LpO447bImHKBTVKLgVw4ECAmPGdArGdvGcYgLgnEeVu2WYVYt4oe7KUu2S6unhRF7n-RHDyKN2Yolyzx5TfVM1RIlfyHY4phpCvxhZ5-tAueyfpW87POFzlyD2Alm--PBzxLUfDJbK5J_6JDhj4Y5n6wHFOBTHErSgc-OZxtp4I5vhLXu4iEIqimsHJMyixJjbkuP27NsTaO5m9vl-rBqQ96uO_hScMcUHkGpt7ZTytdl3-z40UjcEzLSXMKuKzql8oob92wCP5R6YXke6lhfqKpiX8DOgxOSiC7oTfFhkcG-KOHBkvEBTDtO0z_XP9xfPFp4AYpKu8-870myJ-Hz2ogzVlOrvp4FCCS38VMA0jYsNyzW3hqZ0d1e14ZtrGI8tf30zncrStpH2SlV-eBBo6my0O7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون هم اینطوری انتقام قتل حمیدرضا رجب‌زاده رو گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69834" target="_blank">📅 11:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69833">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=TB5hCQGiGcp9d-W9ylPQYAbvfG__4tfrwDpxmiKzTCm6kEFLsGSTYXHMNm6fUIkXK7ZZ_K4NMdcVHbkSyj96XMp1DX4-GBVlCv-xMLcdJaQsxgR7JwxvP-lI6soM6zGLtHWDs6DY7K5ddczvGa88ukCbYjX8dX2U4GnnIVV7WXUwvRaTICIo4zcmQ9eYt6wxOrsDkSJyQqgIYZoAQjDxMslQuWOP3yPppaHNeZAaYHEOAUGaU5g9MpnyG501qqqOlb5_fcMa-bJ52RdfnmtQjSR-2wCM-BTLSyZrsYucMl6s3Cs_FsZbmbVQ6vrqwuFEonDAxRUbxyCiosfciPqMdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=TB5hCQGiGcp9d-W9ylPQYAbvfG__4tfrwDpxmiKzTCm6kEFLsGSTYXHMNm6fUIkXK7ZZ_K4NMdcVHbkSyj96XMp1DX4-GBVlCv-xMLcdJaQsxgR7JwxvP-lI6soM6zGLtHWDs6DY7K5ddczvGa88ukCbYjX8dX2U4GnnIVV7WXUwvRaTICIo4zcmQ9eYt6wxOrsDkSJyQqgIYZoAQjDxMslQuWOP3yPppaHNeZAaYHEOAUGaU5g9MpnyG501qqqOlb5_fcMa-bJ52RdfnmtQjSR-2wCM-BTLSyZrsYucMl6s3Cs_FsZbmbVQ6vrqwuFEonDAxRUbxyCiosfciPqMdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69833" target="_blank">📅 11:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69831">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=ChiegCqvx54ncFg778QP9RRMU_q2536yMQi1agDuQ_5bf5SLR94tfhe9toDRaYGJXFjlTQ6lDxbQswh-lt7Bp71uP_9delZMf2WlALKwOEOUHqqMsseeFw1eCoi0_cws4hKfBay0EplcmU9meR3VBUw3EDXu8FqveCcu2lvBBnpG5OSiuUXbw7wcIAsm2GF9070uXeYcFgGyRLXSfiiP8hJk95eJM8VWaeP9Uf_ZtR3IysktCTaWTdkYES9so73L_rumhf3byWoFJEGkQeCKFyTHIqRd3PI6l6q8KEmPoaZWnB2Q7z69jrwV-qftHzQ6jmaM6Bo79dwqzDzDDeJhr1HroCTY-28v5G7K3oNpCpwGHjiWZQcgZIEFWxqFKWupa8EdvWwVAeihTIAva8MRt3OB77vhVYyqYcvG5qTT0GuMJaaFjVtKiMzMZeTtd2va8SIDlS4BvwvQmJT1GqsXb3VUmP_DuA3js4HPjSH9aj4ZM1rYuyY-IkK7On3qVfEt-cdS6vDKZ5sLRDAxWvujDGLylXUB9tLT4Bl62it9W4uvZbIkFU4vtoZWNUczw-BXCzFcNy6gmWpgr9D2UBTozu3JGfE8q865chJkgzVzwAAItNH04zVY_uK87TwVYEjyhFL-syicQspSMxjYwCcXw98BGykInsNn8qgPWLgnIoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=ChiegCqvx54ncFg778QP9RRMU_q2536yMQi1agDuQ_5bf5SLR94tfhe9toDRaYGJXFjlTQ6lDxbQswh-lt7Bp71uP_9delZMf2WlALKwOEOUHqqMsseeFw1eCoi0_cws4hKfBay0EplcmU9meR3VBUw3EDXu8FqveCcu2lvBBnpG5OSiuUXbw7wcIAsm2GF9070uXeYcFgGyRLXSfiiP8hJk95eJM8VWaeP9Uf_ZtR3IysktCTaWTdkYES9so73L_rumhf3byWoFJEGkQeCKFyTHIqRd3PI6l6q8KEmPoaZWnB2Q7z69jrwV-qftHzQ6jmaM6Bo79dwqzDzDDeJhr1HroCTY-28v5G7K3oNpCpwGHjiWZQcgZIEFWxqFKWupa8EdvWwVAeihTIAva8MRt3OB77vhVYyqYcvG5qTT0GuMJaaFjVtKiMzMZeTtd2va8SIDlS4BvwvQmJT1GqsXb3VUmP_DuA3js4HPjSH9aj4ZM1rYuyY-IkK7On3qVfEt-cdS6vDKZ5sLRDAxWvujDGLylXUB9tLT4Bl62it9W4uvZbIkFU4vtoZWNUczw-BXCzFcNy6gmWpgr9D2UBTozu3JGfE8q865chJkgzVzwAAItNH04zVY_uK87TwVYEjyhFL-syicQspSMxjYwCcXw98BGykInsNn8qgPWLgnIoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به مجموعه‌ای از اهداف در سراسر روسیه و سرزمین‌های اشغالی حمله کردند.
پهپادها مرکز خرید گالاکتیکا در ماکی‌یوکا، که قبلاً مرکز منطقه‌ای بود و در سال ۲۰۱۴ توسط نیروهای روسی تصرف شده بود، را به آتش کشیدند.
آنها همچنین پالایشگاه نفت در نیژنکامسک، تاتارستان را هدف قرار دادند، در حالی که روسیه ادعا کرد ۱۵ پهپاد در نزدیکی مسکو سرنگون شده و عملیات فرودگاه را مختل کرده است.
طبق گزارش‌ها، حملات پهپادی باعث قطع گسترده برق در ملیتوپول، بردیانسک و دونتسک شده است، در حالی که انفجارها و آتش‌سوزی‌هایی در سواستوپول و کرچ گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69831" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69830">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69830" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69829">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=Zl1lsUfE_Nhb_tO0wcc61wEjNie0PpKhO-eiSw42z8mgbSBn_P7dyunXlEoCE2WXJdyzZCmWULGmbABpVLFRy4BZV6qPO2_KXsu60g5h8mTJxCbpscb15liAznynRCYR8yNMpWH7t7cZKXSYW2SGHUFQVN19c6VmPOtBVpptS_lWt35lLcRlaGo73RecFz7iMMcggjn3DgEYsKal9fPzMa7Dd_j9UzefYmr5TwcSTHZQval_WU1VS1YsttQ91mQLdHrf0o6GkNi06cOptEFo5FCpwX5AsGfemsmvyrYIuaCddEtTonjnqxBbslik51mDMMS7GBik93PfDGOvOJ5r-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=Zl1lsUfE_Nhb_tO0wcc61wEjNie0PpKhO-eiSw42z8mgbSBn_P7dyunXlEoCE2WXJdyzZCmWULGmbABpVLFRy4BZV6qPO2_KXsu60g5h8mTJxCbpscb15liAznynRCYR8yNMpWH7t7cZKXSYW2SGHUFQVN19c6VmPOtBVpptS_lWt35lLcRlaGo73RecFz7iMMcggjn3DgEYsKal9fPzMa7Dd_j9UzefYmr5TwcSTHZQval_WU1VS1YsttQ91mQLdHrf0o6GkNi06cOptEFo5FCpwX5AsGfemsmvyrYIuaCddEtTonjnqxBbslik51mDMMS7GBik93PfDGOvOJ5r-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69829" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69827">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7UBqcleIu1rvBQ6PW4pl6riF280gz_moRkWisQkTKiXNFIUzRyotNlHn7Q5OhgyiHuBfNdM0BBL8nGepK0L2Zvr-ME8zzmaFUrxm3ELFssuvYzPkobkXhhyibYya22Q6fQVmEnAa4kg5bvdiuo0e5byjTT1DeoQQKC34rWkRfvPUhj6jvceOWC0L2NrkLKTC-862vE9znwm5HykLHARrhHZ29zaEr8ji9na3W7zk786Y5q96HLhnEdIVieN_oAw2mCAldKiG5xgEmHfbUKyNT-K2DZkqmOPHLOf-Mj0xEk5fd1qcoSpxiLVtukcCxEj-TWmKVFl8CJaxNGNjvFgdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
شرکت آمریکایی BlackSea از پرتاب یک پهپاد FPV از روی قایق بدون‌سرنشین GARC خود رونمایی کرد
؛
این شرکت اعلام کرده است که با استفاده از تجربیات به‌دست‌آمده از جنگ، استفاده از پهپادهای FPV هدایت‌شونده با فیبر نوری را پیشنهاد می‌کند.
محفظه‌های پرتاب این سامانه قادر به حمل پهپادهای FPV در اندازه‌های ۵، ۷ و ۱۰ اینچی هستند؛ پهپادهایی که از نمونه‌های FPV مورد استفاده فعلی روسیه و اوکراین کوچک‌ترند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69827" target="_blank">📅 10:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69826">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=Un-lJmAzXhNvw1nKT9xZDcVKfyI_VB4OxZh4IKQAnXljGqBDg3JAbKX_6gCb39Zd8IOAYd1iDaV-OY3lnLRPbREnG_PADcBJPYBmEawCSCcwzdlgkfE7csc2UVXFt8fanDgJfBUF2Cmf8O6pTRitMmoVTVUdrHEhB0uYSOgx3IntquG_ARrmQQU0dusr-90I1pqOxm5vaoW8hSnj_3QfOU3QUupwOb73EIloZm4HQLdEUs4wzVx_BUgF-3q6C0tfqihis-p7n8muDWXixwXgUec6Hi4GsaLqVW0zM7oNEMxIgLKp4FRl9bUo8jLqmUFlWunc11nSRHuyJ4RJvDTlBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=Un-lJmAzXhNvw1nKT9xZDcVKfyI_VB4OxZh4IKQAnXljGqBDg3JAbKX_6gCb39Zd8IOAYd1iDaV-OY3lnLRPbREnG_PADcBJPYBmEawCSCcwzdlgkfE7csc2UVXFt8fanDgJfBUF2Cmf8O6pTRitMmoVTVUdrHEhB0uYSOgx3IntquG_ARrmQQU0dusr-90I1pqOxm5vaoW8hSnj_3QfOU3QUupwOb73EIloZm4HQLdEUs4wzVx_BUgF-3q6C0tfqihis-p7n8muDWXixwXgUec6Hi4GsaLqVW0zM7oNEMxIgLKp4FRl9bUo8jLqmUFlWunc11nSRHuyJ4RJvDTlBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جهانگیر، سخنگوی قوه قضائیه:
آخوند خرازی، بابت صحبتاش تحت تعقیب قرار گرفته و به دادگاه ویژه روحانیت احضار شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69826" target="_blank">📅 10:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69825">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🟡
📰
مراد ویسی تحلیلگر ارشد اینترنشنال: «جنگ بزرگ در خاورمیانه، برای سرنگونی جمهوری اسلامی است.»
⏺
پرسش این نیست که کدام زودتر می‌رسد؛ پاسخ روشن است:
جمهوری اسلامی سرنگون شود، مردم ایران به یک حکومت عادی می‌رسند.
جمهوری اسلامی سرنگون شود، نیابتی‌ها خشک می‌شوند.
صدام رفت، یک کانون تهدید در خلیج فارس از بین رفت — کانون دوم هنوز باقی است.
خلیج فارس می‌شود منطقه‌ی صلح، ثبات و توسعه؛ چون امارات، قطر و عربستان دنبال توسعه‌اند و ما هم دنبال جبران خرابی‌های جمهوری اسلامی.
ثبات منطقه از تهران آغاز می‌شود، نه از میز مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69825" target="_blank">📅 09:33 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
