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
<img src="https://cdn4.telesco.pe/file/BuIeljnvCH4Dy_OvHVaKkCoDYWF8q11ZPScvC-zfUvJTqlsv_gMava8bts3q_3ET_PYXygpT28Vrf7fFAyCMwi4vA-MnZWgQ8ZGtb0JWO32SFy-dkGpZUd5pYQ9esOWO12esdIqFud7RukC8159nidbUMSJ87X2O1xxOp-VPEDUB0_D6i1aNd2nOPnMNt8RmgqSiTkbkw-Wf0xx6mFpFUPF23gfV5eqlf_rJiKHNVEhJVUhG-fYlMpxSfo-BC1eB-dflg0TZ5NaZYg1OnU9c9UlkzsW_zaxNpqAesrbXac_j8DTocUQumjei0UWjapwh3QePS4EnAA4yVgewUDMv5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 329K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 11:31:22</div>
<hr>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWk-JyTIUlQxXyDBmZGpuQP0ibDa9Kaa411AynCp1qol6I7tm3V6QvZe6DaFdi2XyFdnFSc-FNvuhFKxvsEryr7LOQixd9-LNjQQsjO4bg5QqbEq10kBPdzPEPVKkv4V-3afGEbJvyPCW-a1rkiii2HwlmYwWbO7XjRZr64MGrcmw2ylW6KNYrscdcHIOJkbFJjvyOrhj-LLwgc42enmCxnsvOw5ArEZp9DpzJeWJoca1XReK2PmOubPXNtsdv-DtpaGLO9fU8LZ6BpANNFEtAjYmYORHOy3Cr6M_jXx1pvL9OKojyiB2ArGTX3ENij0XD9WjcP8y-8ZvXV6MXhXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#فوری #اختصاصی_پرشیانا؛قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/persiana_Soccer/24521" target="_blank">📅 11:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
خوشحالی بازیکنان تیم ایران ازگل دقیقه 90+3 الجزایز به اتریش قبل از گل مساوی اتریشی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/24520" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MujZELIeh3QyKn1l9i-ELVu9tFAI9t3D1AH5DaxfavFAET9nrXf1e7PM5GgLDII_Ba4COEJAS5u2I_mh1tw-xVLcu0WjnR_wnYLsGNEz60Luz0foh5bCc_kryE_pS3nEb0-QPl7WZZpibuXHvy7NoPtVdSuqosWYDa8ohcX-JCyGYmbNZmC96WF9vqbPXnjdw2mkvL36GlDi62PbS4tisCdTh_0G7w7St74ntYvFIQP3_-ymhPrakSDAPJFhgzSmDJJJgTmWhR8ceueqEocgjBYbCSjxrb6OyYZjY6_tvbN4gxeQ3hAKUowWEHvOoz2yWWMhQxzXA1pUZnZLGG_MQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
‏3 قهرمانی‌پیاپی‌جام ملت‌های آسیا؛ ‏صعود بعنوان تنها نماینده‌آسیا و اقیانوسیه به‌جمع 16 تیم برتر جام جهانی؛ ‏صعود به‌جمع‌هشت تیم المپیک؛ ‏صعود به سه المپیک پیاپی؛ ‏بهترین نسل تاریخ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/24519" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=EO7wGbJVI-eYdWvYyAX3-xryJ_uJpXNVUdrmrvwE5CRk-l3aa7lVN0I8MW3bWuwt4IgdLhUiLfiAi-WMvsFs9mKzNHV9lp_jdZ-ixyXo_JajYFhuDyy2mKQVOwrCO3YGJhqKFAt0wzrwReh1lMPTcCBMi1tR-67QppieFo8vDXa8_m_Pg4FDBZByKOE64lI8CK44boPMc5-dazjgCo3VBQsxheiGq0NW-rgrSYGJ1rQdL4uwb-alNSDZ38Y8u4fFGCREAzfcB0kOwnMCrIPJ_PT0WKri7Nn5zySRu2OM7vqAy1Gju-nIHOF_A31aVSPO9uEYbM6NLassQqljehr1NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=EO7wGbJVI-eYdWvYyAX3-xryJ_uJpXNVUdrmrvwE5CRk-l3aa7lVN0I8MW3bWuwt4IgdLhUiLfiAi-WMvsFs9mKzNHV9lp_jdZ-ixyXo_JajYFhuDyy2mKQVOwrCO3YGJhqKFAt0wzrwReh1lMPTcCBMi1tR-67QppieFo8vDXa8_m_Pg4FDBZByKOE64lI8CK44boPMc5-dazjgCo3VBQsxheiGq0NW-rgrSYGJ1rQdL4uwb-alNSDZ38Y8u4fFGCREAzfcB0kOwnMCrIPJ_PT0WKri7Nn5zySRu2OM7vqAy1Gju-nIHOF_A31aVSPO9uEYbM6NLassQqljehr1NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌میم‌از بازی و تساوی پرگل تیم‌های الجزایر - اتریش که توسط پیج‌های خارجی ساخته شده:)
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/24518" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24517">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چرااین‌روزهاسایت
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالات
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/24517" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=ldD9XWXMhRr8L5KwFokC2iLtQb8DfrrHOnhfeLuqptzZrO5qyT2uKa0gUHFYasm50FWPSrsdMsJhUslrsFDEAFUUS3vTX9AaNUgb9wwG4QhD3CjaOTwwUdBxjXU0ycqTK4rQF5f5ThRgCmeB6e1dE-fScHQdTBb3KLoKonF9dEZJ9YRfcDR6CDVgq64a2RDzzJ3cWNkja1YPQzuFyKmr-_aTDjAl_lmYSJj9JTvbYi5cR490DmXD38jk7_2NQaupwIT2tHi29YWtTNJalcL5kxDuaAqgHUaVh93p8Al7c2xhKkE_rIGoLTVpdBJuClhmLy-VnYaEmeqUxa1KElVB2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=ldD9XWXMhRr8L5KwFokC2iLtQb8DfrrHOnhfeLuqptzZrO5qyT2uKa0gUHFYasm50FWPSrsdMsJhUslrsFDEAFUUS3vTX9AaNUgb9wwG4QhD3CjaOTwwUdBxjXU0ycqTK4rQF5f5ThRgCmeB6e1dE-fScHQdTBb3KLoKonF9dEZJ9YRfcDR6CDVgq64a2RDzzJ3cWNkja1YPQzuFyKmr-_aTDjAl_lmYSJj9JTvbYi5cR490DmXD38jk7_2NQaupwIT2tHi29YWtTNJalcL5kxDuaAqgHUaVh93p8Al7c2xhKkE_rIGoLTVpdBJuClhmLy-VnYaEmeqUxa1KElVB2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ژنرال به زودی بعد برگشتن به ایران راجب بازی‌هاشون و حذف زودهنگام از جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/24516" target="_blank">📅 10:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=TwiZbEaT2gpGxZ-gyqVAJNTVDy6RGy_nvzhAGV6Eukd6gt-UnR5m8RAnQ4a9qevNbixp1xaHjrwNsULA400mua7A_iU9ypXVC0jrlPDVKvahjFtkRcfBBwq2jiOAxN5A2QKEJfSlELb1Japl5DGiB0U_OOBuugZK6NlDwSEsMOkRPoQ5VEidjq9klzykgImbHjsVIGaLZC0ZzmWZCNYp3yNPS0M_4I54HSMrw2bV2J9AygMNq73ilwvIdVBS_Y9OYikSnGFHN51eoNVIoHeEWqVt-DmOgbPplwDN8ZPo8Hf6VK8wGWonZwYx3dBj3k1SxbqfHcSxp9B-7KK05W-JCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=TwiZbEaT2gpGxZ-gyqVAJNTVDy6RGy_nvzhAGV6Eukd6gt-UnR5m8RAnQ4a9qevNbixp1xaHjrwNsULA400mua7A_iU9ypXVC0jrlPDVKvahjFtkRcfBBwq2jiOAxN5A2QKEJfSlELb1Japl5DGiB0U_OOBuugZK6NlDwSEsMOkRPoQ5VEidjq9klzykgImbHjsVIGaLZC0ZzmWZCNYp3yNPS0M_4I54HSMrw2bV2J9AygMNq73ilwvIdVBS_Y9OYikSnGFHN51eoNVIoHeEWqVt-DmOgbPplwDN8ZPo8Hf6VK8wGWonZwYx3dBj3k1SxbqfHcSxp9B-7KK05W-JCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
باحذف‌قطعی‌ایران از جام جهانی و بازگشت آن‌ها ظرف 24 ساعت آینده به کشور منتظر اخبار جذاب لحظه‌ای پرشیانا درباره نقل و انتقالات باشید.
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/24515" target="_blank">📅 10:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGGBcXi5X7yyd3IlAwv3086ykBfSnASgslDYJXhkqyRmUD5yFURU_L7Hj0YmoPfnkSkYN4eTenICZHSU7u_355ptBICvGuson4hpnDevdQFJghMJ6zAgkby3Ni0K1MEmFnpN_dOUzdznL7Ou99_DdpFFbp5YNhQN2rJAYwOhwJDa4G0oO5BU7gL4cZF3mfiXSSkKhUonnVV94qMimVVBZ9VVZDOjUIkipvUFirHHeRGQEmRFDa1eYVUNI_0jHRlkE7gtKS8UnMErzJtMr9C5vMOmJfRornOuj-csmJ5vht7jElAz-UAJXMwzokK3HhluC7Homi_qQuRF27YlxBfU3I7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGGBcXi5X7yyd3IlAwv3086ykBfSnASgslDYJXhkqyRmUD5yFURU_L7Hj0YmoPfnkSkYN4eTenICZHSU7u_355ptBICvGuson4hpnDevdQFJghMJ6zAgkby3Ni0K1MEmFnpN_dOUzdznL7Ou99_DdpFFbp5YNhQN2rJAYwOhwJDa4G0oO5BU7gL4cZF3mfiXSSkKhUonnVV94qMimVVBZ9VVZDOjUIkipvUFirHHeRGQEmRFDa1eYVUNI_0jHRlkE7gtKS8UnMErzJtMr9C5vMOmJfRornOuj-csmJ5vht7jElAz-UAJXMwzokK3HhluC7Homi_qQuRF27YlxBfU3I7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ مجری بی‌ریخت و مفت‌خور صداوسیما که بیس چارساعته خدا گوه‌خوری میکرد اینجوری روی آنتن‌زنده‌شبکه‌دو صداوسیما ضایع شد. می‌ثاقی هم که کلا فشاری شده بود گفته بود دو تیم بت زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24514" target="_blank">📅 10:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6vN91C-85w7bzQkn-U2bIcjCQtcv5YWJhMIPwhNRm8_fc4napLndzJOG2U0ZNod4gbiDxNUW_jKtejhoplpkqbXePty-082TiC7k_Ilx_YNQkdqII62C1MoNc-JPtTQ-ZVlwgG2iVKSGXdv7JjgVWHBTboD7t7VgujUyfio_mEeg94Zz49fxGt6sElts5J3hmWWHBIBqv5YVf6tDamlMakdnkBYDz01HuA9ESQPCkRU-2JQN4o6OrlAxWxQ0Zcz84Sfnj6BNLfxEwBp119TI2vJ434EirpX7YOw4kgc2WvnsPC_ntUKdLSjGz-KH7dBZr7ahOWCaid087_YhgvoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/24512" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiGIGqMtXdQmoh5_bgF2RXLoUkOWR35jptQtAIY8js7OxUmkOcKRSy3p7WmZUPLCmdq9RpU5BZZjJg5hfkhsYQ90AKNSTn_S7oKf4h6pVDlNKGpVd1N904VDF0-ioxiWmDeQLJIo6M1_hQWmUHk4Jk87JeR1Ipi5toohnpCDD1v0WYwlz4A1Ykb1w6_VwysihRX6DTeT7ysb8G_YHz-3L3AXPMXvNjYMv6h1Rq5g0LF4t5FxT-_6TKfsysLl4lWTfDxjxcZ2_mZfeF3W2Fd0pZdCx6Hw_lphysdj1jnj9o9BpyA2Jism5BqByLYXQlfxqfcj8s1QzjRzYe8zX_-llQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛
این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/24511" target="_blank">📅 09:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pSakpMmwbcgQBPezyAfvcxJ0_xZ6BNBDr-pR4HdzrDIEZYTo-xw9ld_DjQX9gMg7ii1uAXzxFxKS_c0E-otPVwTBOS7iVWJpiTwTYVJX_ztMj4bphlUfdOQ34dagyzOaxZwLe2Gu6_JFIBCJ1zfFekjumIoVp9mwkkcRni7Xa_pAYsM2M2aABvRijVoLQwg4oidg4tQuh3HfPrztooEinwmKrGPOnZAgZW2W7Vh0fq0CP90weHBKR0untxQBRdIrDsOw1qe9Kr4x7kfDfFTITIEJnaNeET3kZhos3HMpCT6cGSA_9RCxwZkKj8TXR7mAtDTZNghJWAtb1z6bpWeVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNLHyKq5OlxSr3xlMKXn_ej7iy0Bei20O78IbDa9TkjD5byY8pZU31I0oi_5TXNSmOa4FYfWcBZePUtwfPrRjlK3s3Z5yB2lR9SaLuOBuaqoiph2dL25IvdY9R7yMAbuKgtZwrvUdFCo-5EK6mnAt712moc369uWsBTSQco04C_uZQ-iLwy67Zt_4kLgSjVca_zRuKZAMzFfDKk1brzP-XDgcYt3P36eJZairYEZB9j7j3iIZc-3UCub8LxQgbsoq6L2JO_46Qj98lmSdo8Krdb6xAYXlW8VbCBfGYRqXz0kT-vGEqlYL_5-ZCXBcfxp6gzM9U4ES3nAqZAH2iCGfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/24509" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛
گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/24508" target="_blank">📅 09:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/24507" target="_blank">📅 09:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=emhG4lPBRQPzmtvd42Ca6-xlL92SSmA1O7OcEsnWKRMpVOdV9PJMIOXBOcrbvjV5DzZfuENkibDOzkX97caBpUJjAlQ6SG7Yuu0Z-COdfDgfPb-ZgNCbQK3olfti8nxrIN-oW33Ffj54YuJVErF6B5qfna-QtvQVJsdXxc07D1cK4-M25MfFlGuMFyAPRWD182UWn5Aw8OQQCR38miKk5pEq89zz0e8rIz8VAIXW0aykjo16X8SSvlqYhl6FEeHlONb_zz2r_LtVcLAiYedWH7NAjEfTMNt0FfkQmQAz6i85eh1_M9RdaoKUcSvxbhQwTgSzUZCCyufXiORRheYckwp052WA_L9EZt57zWvjsxFGQMvm3HhWtpaeVMOdNkU6JOGsSNq-c5gkcThYhKr7DZ5K1kNeH9c8D_g2Rf03XkEpTdwjF_ziyx5e5ZYI0nhphu-BpWL9qokIdO_-S98PRV8DhQgL0kHtZ0P1C6YfOoo9p7ozG-f_GTLHkvPJ3gg2MlkF7bUeLOKQusP26AD-xwRjMHWP4bokHOc7ArIPdVzVj9i9GNuAuAsoR5-eHARcTbzzz9VrfzlzO9gkifdsWK7RL-AuMwbkaslWT1dbrSjZprUPAutc3sAMH9OgoVqNvJnY5APf6YV7BfCr9_l3ACWUJc79VLUOPS775sx0luU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=emhG4lPBRQPzmtvd42Ca6-xlL92SSmA1O7OcEsnWKRMpVOdV9PJMIOXBOcrbvjV5DzZfuENkibDOzkX97caBpUJjAlQ6SG7Yuu0Z-COdfDgfPb-ZgNCbQK3olfti8nxrIN-oW33Ffj54YuJVErF6B5qfna-QtvQVJsdXxc07D1cK4-M25MfFlGuMFyAPRWD182UWn5Aw8OQQCR38miKk5pEq89zz0e8rIz8VAIXW0aykjo16X8SSvlqYhl6FEeHlONb_zz2r_LtVcLAiYedWH7NAjEfTMNt0FfkQmQAz6i85eh1_M9RdaoKUcSvxbhQwTgSzUZCCyufXiORRheYckwp052WA_L9EZt57zWvjsxFGQMvm3HhWtpaeVMOdNkU6JOGsSNq-c5gkcThYhKr7DZ5K1kNeH9c8D_g2Rf03XkEpTdwjF_ziyx5e5ZYI0nhphu-BpWL9qokIdO_-S98PRV8DhQgL0kHtZ0P1C6YfOoo9p7ozG-f_GTLHkvPJ3gg2MlkF7bUeLOKQusP26AD-xwRjMHWP4bokHOc7ArIPdVzVj9i9GNuAuAsoR5-eHARcTbzzz9VrfzlzO9gkifdsWK7RL-AuMwbkaslWT1dbrSjZprUPAutc3sAMH9OgoVqNvJnY5APf6YV7BfCr9_l3ACWUJc79VLUOPS775sx0luU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/24506" target="_blank">📅 09:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZuoN_Y_gB5TtGkJwryQLtf1YanT8sKeIqGNtaDTxO2Z4wFPPSvd-nN6ezwOv8CiYYXBVXAcnxHbS4vyM4GGN_kLu9iAlvMLD0MMsyFARMugFp9qA79aYIN4vbGf782PXF51IjTecSjr89lZCP28ckMR_JKsmdTLtdjIP6IX3_LrWNVwtfZiVODre9Zu5XQ9eqTGO309TQpPNKKZX72MUzQ-jFQd47Zt6p8QEufy57J15fbWOs2XuSKveXHOyVFIJJoa1DD3DDazRZe8UDVNcwK4VeVsNj4iBsLbK3CcD0DlG2rLhyGUpyFAz7OYuiQtw-Kf4yZ1DRd-FRRY-BxoMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/24505" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=AH1GOFMqhhDdrocvwoCFxbD6_xeJ0d5wCPz_cWtIPaej_K2wifguWa8D3QdD2kbycPaZXzJk1v1RZL30znA4zY_aLrb-NcjZ2Q3_ZXNtwwgghYsGw53VLcnN_V-SpKgzan2Z4Oni8nDnA-OI6VpZLy0njnB43lQq2lRzIerSbZpTNc94f02_cK4ieTMnXgljrl9t5XF2gcew1bpcI5TL1VtSlZAGPOPOouD--v2o7WCfK-7DkEtn6ert8tiC6UPUfeGiKt1pT3ywlWLne5WC5UPaLz0BrzQ2A2KIQ4wpS4vqjSVC0IVyewKhjOVacZTvQscu8gOjpscDnUyOuEA0dpVjuSqx5XeShFwnikG2GRfS0uUIkbpi4HGqlOygxZn3E9tp4amSd42kqg9lipPbV-yz4V7Mb7h2eCgPHU_imxZka6RrQmEw9aY_pX-hyC7r2ZjRp__OX87m7j89Y04URFtsGju1dVGJktpFnvtDrV0t43_5NR5dsTJ-e-zemYMSe8lPrbImcTM7NZFxD9Tt1mkVoGydJaDqc3-FqvHCBeoU7Sf_i_v2SZxd2MLavn2bljbT4odff5hHIIoDCfRve-Yp2x11WdBtZARO-bbE-3uARrDRg3xhp_UoAGsQzkNgu1U1yXO2lMQFTxr23Q48Jap7J0pPgiMTMe6HhcqM8ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=AH1GOFMqhhDdrocvwoCFxbD6_xeJ0d5wCPz_cWtIPaej_K2wifguWa8D3QdD2kbycPaZXzJk1v1RZL30znA4zY_aLrb-NcjZ2Q3_ZXNtwwgghYsGw53VLcnN_V-SpKgzan2Z4Oni8nDnA-OI6VpZLy0njnB43lQq2lRzIerSbZpTNc94f02_cK4ieTMnXgljrl9t5XF2gcew1bpcI5TL1VtSlZAGPOPOouD--v2o7WCfK-7DkEtn6ert8tiC6UPUfeGiKt1pT3ywlWLne5WC5UPaLz0BrzQ2A2KIQ4wpS4vqjSVC0IVyewKhjOVacZTvQscu8gOjpscDnUyOuEA0dpVjuSqx5XeShFwnikG2GRfS0uUIkbpi4HGqlOygxZn3E9tp4amSd42kqg9lipPbV-yz4V7Mb7h2eCgPHU_imxZka6RrQmEw9aY_pX-hyC7r2ZjRp__OX87m7j89Y04URFtsGju1dVGJktpFnvtDrV0t43_5NR5dsTJ-e-zemYMSe8lPrbImcTM7NZFxD9Tt1mkVoGydJaDqc3-FqvHCBeoU7Sf_i_v2SZxd2MLavn2bljbT4odff5hHIIoDCfRve-Yp2x11WdBtZARO-bbE-3uARrDRg3xhp_UoAGsQzkNgu1U1yXO2lMQFTxr23Q48Jap7J0pPgiMTMe6HhcqM8ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/24504" target="_blank">📅 06:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp2Yz4_mJgNXgVqQaW_qejN_dVIu0AHs2YaNQVO2NCxUT8AeO9oMVJOz81FpxKDqGz98HrTeKS4V6bJbwZZppOkUBPUoOB9W5lQnmduCojm-4NTk75ms5s59fyP5LtQ2gUhTgtOfTtXwOvquyLuu4WNfsyblxdg6tQa9V4xOiCZZAU4crUk_YgCC9Ei0ksa2TvUnwGAUeX6iZcgNKbAuHbUAl0h9ELqfKh6myh7EfvSG-6u9MLO_Gpmfo9G0ZaL5wQ0KlYYQFxD2EmLFHsRr35Rjj9rrUQEDgay0UMMIFWhUJ5kAGvosuqJBPVgVPVL6ZEzlF-AbGJ_31V5KLst_iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/24503" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnYZ0wfly9rqkh2IDpzvlIWIbQiDYC7onrlXtQU07vR9nf78ApIcxuNYKg2v3gFD03fvCqwIDyN6TqyLXLmMhu6DG2XAnHg8WGtU53tmbwjLs6qRcOyCBbBN94TAQoqOAvoNt33KJxpSLYRLpEqIaMb-hCkswvRkwoe4JxKjTtKk_zQrNd7maRTsWJk2jqKGjtISBuPmpRgk9BJ2_w4OswA3IBH-PrFjHa2JRqwZIuirm4nR6lOxX5sfck33ccXP3MtzjkbqoTT7Lz2MDSP5P_1X_ryRHQYkLdn3NCm6FDB6c5UpRACGlj12jqu5gWHpl49iqv6HZGg0R0n_HxTXpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxgrDAi2nU-5CPClgcmPDEnTikTSDnFVBrmj9qDsS24YKN-QPj0DkyAbrjsVyKD83RyrTs39H-sRuD3Sou_lPA00P0dhkYmenTgpoUdENGyKKB6Zflq0TeTXVynQKNiHaV64U9Wx0U3ZDlepXxVArSiCyAVzvKWBHn9XXVR8AAkXPYozl9wlQjN0MJETQ5LLWHeZjk-nIImDCOxYKDKk36LyC_DKHby5d588UyRmPMSVUqT7_CRBBdQLjv6O5KrQs84VY9Ryla9A370_ZfxWoS3OOMQeo7_XvfkUdbC2YzfRfFkQT1wZ0VZt93Wc6WdwIWwhu0sLe8Px_vYxIQkr8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی کنسله. این دو تیم دیگه تا فینال به هم نمیخورن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24500" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOTqvZbAx0awZs6IvciinhavVKVpw1dnj-DlB6rdo8v7ys_zhohj_IM6O5A8sjr3HWz8_8xsbITrfjyb5UwSzqUKBUlQ9AM9tAJK2lgpbIkEHeF3w1UoRKuP86p1Y-36WQg6Ynr4SnlM8jWWAXPU5ynHBqshkZhmm7iN4GtnRrNz9mpKbuoyaSuUeLd_6kwRCDhlzkzVtilkd_aCn1HfqlE4xbCBdAjQZfpKRXyra9-p6XyDcN1RaGtJNKwlIy6MqWJRdW0NFOuMYd_WPgBiZXdr7bkz64mAV6VnGM0y_SPz8go6RfKoT5gmyvOQSmE4Q0csnO2or9IGM4EkhsyjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ دراگان اسکوچیچ سرمربی جدید پرسپولیس قراره تا آخر هفته جاری لیست ورودی و خروجی سرخپوشان پایتخت برای فصل جدید رو به مدیریت بدهد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24499" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24496" target="_blank">📅 00:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-f8Ou3A-13JGpNO3akjw2xIl9tGszRwv7CL9WZ1DCajRd7IXBYIksvTcq4g3p_c6ZqHo9FVH1xtm5iWI50QQGxO29d-npNxCHivaxQHKkxrhriuPMEmX0j9TliO6Vhn9QdQo6HZEa62kWk3Ws8w3zdfEBWv6wYGMmLMZU2IAKNyZ-zLrch22La793K7sYbWV_pyZQM8cqx4H4FEv7MgckL0bNuHG1kkjc_NNfBYIYZDJGG9eRgfSHFzm0tdxrtdRNeKMxZ3nHYtTaLdGeekE5XMzm5qZzlTh_mgr0-Vk28DR-4H1jIQtuIERYcd5jLOCr80YfoWU41YzYykH3u9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24495" target="_blank">📅 00:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PERhzFCEdqF3hvMK2ms_zAmuOtI3hUYFefY-ruvKtEabgxPv5MZnIsPiME0JzmLdSBzxK_DMNNknGsfqjP7JFpvAhbgeu4PcC-lvUpkKMi755mATLZmZDWcXOKVC2gTk76z9Hxan22j_BE6-GdupVkbBizTktFU4OX1QHxznHtgNV3DIB_hR6EkSDfs71GnB_mgfEKYgnAwBwhdXft8XaG5nmxFiGJX9U4zNvf3BXYSoWXvyROMUcLw6fHshdkoaaQmhZg0UpfVmTODMyMkm927VWdhto22E-_qcAyouT-C2xG4cmm-GRrN3MbpSNThub8p70hscQ4ryq8gEELVuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24494" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbUZTsSA-xwyTBW5r_kzNNlbN8IndZab6krLMCGWK5LMQsuUeJHp6ePRS6kuWBNE3zHoCHumKw9S1r1UTid1hr8959QKz7sz45zmBo0PVAQdpnUxgoVs616jmfC8pFsCAddz5ph9JKQt8H13SNdQCkoCMnAMw60LLc2racqRti256i2GjOtUTQw5iAGlXOAqoivbZip1LcG_AOYlcv1gzogtuVe0uil3arUDGgecBPYfBc7LDLnxAcu0wadFErT7Ben-nCnd7OhTYsGspsHS43besqPm4-4BTVrYLsaDNHzRtADLkqZXCzYYuaUMJGlh-HJJgOCKWCWMnNzdU7nBmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت‌نزدیک‌به‌مدیریت‌استقلال به‌ما خبر داد که ظرف 72 ساعت‌آینده گابریل پین قرار داد خود را با باشگاه استقلال امضا خواهد کرد. همچنین به محض باز شدن‌پنجره‌تیم، چهار ستاره ایرانی رو به استقلال خواهد اورد و ممکنه که یه مهاجم خارجی نیز بیاره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24493" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f250d91879.mp4?token=Sew96AwXJWAJq3LqhNdxHvFwrUhyRyqwrkmm54TrNYwhYx5cAbEdBsVCGrKD5QgGIkhnQO0zS0XeGasw9ek6XpvkAHdnMFxxbATrr8cXq8Yp67_wgmWLAZm0nYbJLAKdigL6-8Fv04qSMDh1OJWXM_m60Z8_nk-OMHVOAoUR7DCCN-NHA1pn64Cc1PiAvLNZLvtb9gwkMOw8eoUHYIFFUCoGR2dOivY6WktWLfiaGEEwWq17Y-u59WqN4sYerjQ6fUASof2oPY0YZAiYVKGNCtpuUGOHx816KNKfsV2PcrPvy6a3Ff7-ba0Lc7T48W6AT9JBRdOcy1mZapOgnBqyV5hJdSTYsRdgmjPhUxmXY0OxFCAoTwEPi7WCfnbGKfH0uHHQ36FjYyFpH84tI0DorY6FMfIb4wcFFvcr13WDBtqIMsbmeEaQ3nXxbzKo2l_N-DZk0DLFFuYWuWFDYjjvRGoCKZYy3zYTXBpTMIoRT3T2eOxs8Q_LuUAxFqftvBrEJsfpKSdFA7eEMjq07iqMBfhNQHzHVK9o8eEsj-jZkP_2JQtZz93_8t0muLKrIst9ye9SCDpBN4YtxPChlJDV5ag5cd9k_DWOSM8vt6ho9NrVNKmkekP9LKME-DpeZNLfN4QMREiyEhdRuk1BcB2qyW1NDjkuxTcUmKGosLbozPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f250d91879.mp4?token=Sew96AwXJWAJq3LqhNdxHvFwrUhyRyqwrkmm54TrNYwhYx5cAbEdBsVCGrKD5QgGIkhnQO0zS0XeGasw9ek6XpvkAHdnMFxxbATrr8cXq8Yp67_wgmWLAZm0nYbJLAKdigL6-8Fv04qSMDh1OJWXM_m60Z8_nk-OMHVOAoUR7DCCN-NHA1pn64Cc1PiAvLNZLvtb9gwkMOw8eoUHYIFFUCoGR2dOivY6WktWLfiaGEEwWq17Y-u59WqN4sYerjQ6fUASof2oPY0YZAiYVKGNCtpuUGOHx816KNKfsV2PcrPvy6a3Ff7-ba0Lc7T48W6AT9JBRdOcy1mZapOgnBqyV5hJdSTYsRdgmjPhUxmXY0OxFCAoTwEPi7WCfnbGKfH0uHHQ36FjYyFpH84tI0DorY6FMfIb4wcFFvcr13WDBtqIMsbmeEaQ3nXxbzKo2l_N-DZk0DLFFuYWuWFDYjjvRGoCKZYy3zYTXBpTMIoRT3T2eOxs8Q_LuUAxFqftvBrEJsfpKSdFA7eEMjq07iqMBfhNQHzHVK9o8eEsj-jZkP_2JQtZz93_8t0muLKrIst9ye9SCDpBN4YtxPChlJDV5ag5cd9k_DWOSM8vt6ho9NrVNKmkekP9LKME-DpeZNLfN4QMREiyEhdRuk1BcB2qyW1NDjkuxTcUmKGosLbozPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24492" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J98If_Tj7uyLlEfqs_QbHUO9B00JrL2AV7CdL_roRPCx0Kfd4lefrmFQPYtvqHkLLeubtFi7nFf6iGBb9o6iLzzr1sj5AnbYnHasMmoTZ5tsz5flXDXK3O3CwSG4x0pjbAlFFJwHesAiU5kkKSjG8W4NCKCIcGQJPWIJhZs2NpCE6muXmE3LvzJpHShAZlSh80585YdQR9r1PTgfguZyterUn-YWi5g4J2xSqaDhH2kn5-H_eegOZtvQF7DWl3g8XXqDlvOQi19z2tJ6y91XdsFnDBMgU-5PIwaGsHUUKyswVsNYujONQd4E3XrwTo5a8ZipXnZgqnQnZt1Ixz-YKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
دوئل فوق‌العاده حساس دو تیم پرتغال و کلمبیا با قضاوت علیرضا فغانی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24491" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DR_zC17ENOIM3DfmorwCGtJpJhBNSBeS_SElA0j1bBJcWJLT_uyMW-BywHGlauF9ewaTwNkQmFsD6VnXieM47vxhdnjcHqncWJ_jiclXE7oRbJ8hltBBQh3NTB3p6Ri2QPFuFi8gJ9edV7Pejtkzs-Iz2zapjJJ--JNt3IyT2jOCOD00O2M2YMeBB_KYzWy9LpcLCbCoHOGTgXz4AuMkGdZ0lEOWGv48b19dFmyE5j9AFXA7WxRHtu-Aeyo0C0et--8H1x_bS27OVpUj8OadTWEzI3hR_Dy0Maj6usTC-rcJVczzvQ8YybTCCc3TC903BFiylxBcBzl6k5eOtx4A-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
ازنمایش ناامیدکننده یاران والورده تا تقسیم امتیازات در جدال ایران و مصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24490" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/citcQAUscV5xbbZglTg-G-ne6O4sD7zMTFas5J6LWK0DKuNfcQzYu07-bH7pYrwho0-RzSJimgZ5SycWOKrH-XCMWC-KFX1HNKZ5PHQQWxh6DDRi0r0P_2Qix9p5lCPyA3Bajri3SU965i3wyBIxt-Y-nW5J1fuJkAl-JKGbaeig3FguFXAZ2-Fa5hXtabloRO4ywFMskBEFjZaxz3oDLwcDy5NrpRUD1KOK5z-zdXiO0Fm5Ad6TQYAbYsnWw9zSlxUGMRSeK3J4Ya2gti7DQKryPNsE9aTF3EGhdqABzTKDXwYD5HNUIw2QPBieHfNnOA6mUYMMBo1hHrmpAXK9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
هنوز چند ساعت نفس‌گیر دیگر تا مشخص شدن سرنوشت صعود ایران باقی مانده…
‏
🇮🇷
ایران برای صعود به مرحله حذفی تنها به یکی از این نتایج نیاز دارد:
‏
✅
🇬🇭
غنا،
🇭🇷
کرواسی را شکست دهد.
‏
✅
🇦🇹
اتریش و
🇩🇿
الجزایر مساوی نکنند.
‏
✅
🇨🇩
کنگو نتواند
🇺🇿
ازبکستان را شکست دهد.
‏
🔥
🇮🇷
شانس صعود ایران: بیش از ۸۰٪
‏
📅
تمام این مسابقات روز ۷ تیر برگزار خواهد شد.
‏
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
‏با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽
👉
betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24489" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=kaUa6REGT5cr2Ta32179lq4IbuRMTMi_FOXoZcoFdq_qyPfH3yDKM3T6Rd-X9dSbyosJGWHoG9cBegvQuysbxg08a962QIHR8AKeZ8hLWmcHTPqNJPzlKlWbZxQ9NM5pcPt-DxZtSHplMCX3JWomaPPkhRfNDlnk-Z075L9IPnDMH7LC9ZzNBwFMeFNfd6m66Ovc-K6qLBaKjxzrqC9IGfZxDhgiwtuDb1Ob3YdRC7SdQnKLsHFZWlL5ZwkRyr7BXtskNLsLfpugDAojT5jwBngbt9KqFxUQO4tdBKqAyBRTKaO5MceZ_ZwdNDY4WJ0YMCZobk82Fwvhrd-mtrgL8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=kaUa6REGT5cr2Ta32179lq4IbuRMTMi_FOXoZcoFdq_qyPfH3yDKM3T6Rd-X9dSbyosJGWHoG9cBegvQuysbxg08a962QIHR8AKeZ8hLWmcHTPqNJPzlKlWbZxQ9NM5pcPt-DxZtSHplMCX3JWomaPPkhRfNDlnk-Z075L9IPnDMH7LC9ZzNBwFMeFNfd6m66Ovc-K6qLBaKjxzrqC9IGfZxDhgiwtuDb1Ob3YdRC7SdQnKLsHFZWlL5ZwkRyr7BXtskNLsLfpugDAojT5jwBngbt9KqFxUQO4tdBKqAyBRTKaO5MceZ_ZwdNDY4WJ0YMCZobk82Fwvhrd-mtrgL8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیویی‌متفاوت‌ازگل رامین‌رضاییان به مصر؛
جدا از ضربه دیدنی و زاویه بسته رضاییان به شوت زاویه دار میلاد محمدی با پای راست توجه کنید که دروازه‌بان آماده مصری ها رو مجبور به دفع آن کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24488" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgFPmy2r-_XDZZI4R2M8gJHQhR0EbZX2ltTQhyDh-SvP4LePK6uVz-Cf_AxEUy3I_9WSLp1GBqclt5mwXwt6S78dB1LTbgokmXXv84GEV7rbw46TncKdN38ybLXrcET3sqhGsRHSJxWewaRIoph9sdugBZI9G5zwrHcSfRI1RrThWkn1ifAnC5gnjmobc4aDaagFKSM1pFJIRjeqdeC5czRfmda6VaPZbAWBavK8SOT67jtB5wv-m_M1Y66dXlG59FeqGofq1ah74Eh92R46-4Jez8lc4JMPeXVXGS-mT0k6a1H1lKX4yW8G9uK91WSnVtPJuI1aqPUI59VegWScfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24487" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuAYIZ9YIDYIRjSOeS52-j3oHrjCiZzeCFm1CCq5P2xMZa8tt__xIY5EG2RV4F_S2E--1GsBlU4OUAPz0U89Nd0g1FY-j0NU8wHuItlTlTk8c6AnuSRFpX2TI6ONA90dtsgcpU_WInCQ7YNfvX4c8urAs7XBbvCJeFIAfkzvjqJvnEBA5ekkypp3R1prpn-3qTFUl-VYa4IxD5KhP_sFq6EyJCt9HVupKzR_Ovps4JgkKAT4XgMKoMfg4k1Z9BKfRARsgR693sZCW93NROeo5Jle34TUYTUWIH8hXrQLGIOwCduQ3dc0XeEAQbxlOf_ELzcZjdqIwtRchToVd1RG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدازبازگشت‌زودهنگام‌نساجی به لیگ‌برتر؛
حالا درفاصله سه‌هفته تاپایان‌لیگ صعود باشگاه مس شهر بابک به لیگ‌برتر نیز قطعی‌شد. اگه جدول همینجوری بمونه صنعت‌نفت آبادان در دیداری پلی آف به مصاف مس میره و برنده اون بازی لیگ برتری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24486" target="_blank">📅 22:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRcrWkUpT1_Rg9GSMMm_lfhMYzsNwFW0Uc1eakw5VRjx2mz_fsTk4t3zblqyQYZDGFV1-3DTK9Xa0k_LzMdogt8dp5Oa_vZTgHk4kZ5UhkcZWvjy-dYn8h9tpxLpACfiuGcxb0AR41dChFw64O5p1mB1WyxV_qpVq1nVmcWJJESL83ImY9fzoM3XHmbaVTFDV6iWPKjVknD0nBmlPwOcESh9lz3PcamftEXk-O_2c8JJ1aVVsiOgaaQrMzwdzI4niZlOp7ek9ZJDnZV29UXvMtb5ITKbaxaKfHbINlWGJxbulBiNLYRdw2zRV1l8ooGrvfwd0wV0Eo5RVWJdb7EL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24485" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq5bEDYrw468VjfchIFb5wCOXQCBlKaMoKUTvTExF1vS9MLjXHPn1WLGDmYk2oHGPeGU_-7_apqKj35A-5ma2mbJGT9EAZWmR9BTwwFe5EH07Xgm6PLfGmstT-iusii5O6hUq6-iWpXHLPBPcGj95Rl2phBoxhQEQr7osn01ne2Pxuvmh26sk2_hCc-Zn9j3_8q2wZmsfhH4bab5QgLnTkT75sO09fZRkwd5pk4oTIarBugnJ5QwS-D-ntzxyNi6CxqKt-nutbrViVcijJSCe1b4rZisIIAncwnzi9sSpoQpopueQfTco5aJ-jmF_hhoo7vQHgtWef9y3HQYb3tgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛
یه زن‌وشوهر جوان تو شهر قرچک که تازه هم ازدواج‌کرده‌بودن بخاطر اینکه زنه طرفدار تیم ایران در جام جهانی 2026 آمریکا بوده و شوهره دوس داشته که تیم قلعه نویی ببازه از شوهرش جدا شده و گفته دیگه خوشم نمیاد باهاش زندگی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24484" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbeb7hXk3EwiMKcWbI-1bU1t0SDA_YDZkGno_dVcUFIIKD5MdAHl7yxCK3bGc24RawcCt1Y0D8MxfNfJTyVPgRwJrIvQLKbkRt4Pw4kqlAFZyllOFwMpMmXKnr2xsSHxvgQvS0YIr_4vmUbc3QOCNh53EZg51KzHx3jAKBuo0oxIqHE1U9lMToYIlm7Zh8SKCS44tt-TfjMC2-LLs6lKjZYgxHbpG5faNZeD0u7PXB5wa_DKNO9YKp1WQb6GiPs64hATGAdOLG4P9dffHW7CxcQtfVhoxSdxmmk7fGY92Q9csptDkQJEfnCJWdqiAKtUmzMUt1rIQZLl27EDxI2gHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇨🇦
بااعلام‌فلورین پلتنبرگ
: بایرن مونیخ میخواد در این پنجره الفونسو دیویس مدافع چپ 25 ساله خود را بفروشه و جدایی او از بایرن قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24483" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD1t8SSSBcxG2MxjCQnw_d_d0x-PZ6fPxPZN9Q1T5IJSpqiZP730iY863VCTh6g4KwmEUBxTMsR_LowvifyBxeewWweBCwd5hhexLOHuUuR1Y6c6ig2gAX_WN1ixtjHovsIQ3l98uqmkFXUv-Md5RiF8AgdvtdZVm2rakPJ6A1YdrNCXVoSLT6OxSwZhM_pOqkCqeedHKPm2ulxOIpXgVu3HgiHAFVt5UGpse9kAXgzrwkFkvE7RQk1ypx3lnwOtodSEps-BaTFaTjTl0_EY3wd-bPhFesdp6jRSv9S51TpDv_IB-f-bxEjrkLF4P8MZjit1eGsPx5MQvGLMRbpyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24481" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l45UZTHVz3bJIDOieOkFmt4HLUlXFoUwhF_qGI1r-LecV-GRKnv2PYcTWUiYSp_iKSZFczPp8nRdEyRXiCb7gioXJxoeKVnrdfrssIFgSatjpV2Wh9U0PGmRXhxOmuWsr8Y7SbVeXJ5MR6DFI1kz96V1sph17OImEI2PWvmOg99yZAVnR5Dg3yjH8LsjMGym4TxT8J8x5-75kMULvuibYOeNSrSYiXbZgucr-Rus2TCGNKzG-2TRNE_QQ9du8z0-petGuF1DoDfcnP745wcCFtICrt5R-TPky9cXVGHCIQt1Yv-Tn1NO1JLi9mmghq6JB56Mnitf4wEAwkMcs4fBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یه‌نگاهی‌کلی‌داشته‌باشیم به تیم‌های صعود کرده به‌مرحله‌حذفی و تیم هایی که در لیست انتظارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24480" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkBqacVAAXT0TPLkF1a-ymhldOzxHbKgkPrRcL6StbyisgBV43Nw4uKGXECz3SPq-oxzx58l2y06PpmkugiwYF77uJLvfLIg2M4I7jROxs5Uq3otxDMbqeLRbfOQbOei9pqQLr8EnnuRA3G062EefuwuY2beSAhg68W2mXGWo50jCMP2Ziv_GP79rQF9gyBHSBMpLf4dp4aLfjipVQMF0j0BfiqXnqwXZUbZravzJYZvc3uIA4cIVClqVl3bYPBuoy-A2iqOEPFOFfT0nOOSZakqg09hAwDypKvNSaLWcQtTWzhOquE5jsSgPcuOkBu0DGFuo5iDhVHFpgpkgDGsDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرعقدقرارداد باشگاه استقلال با گابریل پین که از امروز صبح تو رسانه‌ها پخش شده رو شش روز در کانال پرشیانا اعلام‌کردیم؛ مدیریت آبی ها قصد داره بااین مربی ایتالیایی قراردادی دو ساله امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24479" target="_blank">📅 20:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=sALoWcUCA2IOpkOhZ8P25XrurhU-AkEnON4p-h3MnW-HXAvlAOCSWGW_7aedBhzHFU-jvSNmANkdvAFlvErlh31t-zTBCqAVP2Mp6TNLfBZohfdgRSQRxP7iOdBcUBER78X-3WzPggZLuASc5jo1dY3CKKuPUIm42TCxR1F_Y_dJHAHKGR0v0J5BvlJry_OKbZwC65r02BLLsi2LHgMuyXa6TlvByw0CHvWbxqi4G5L1kaScPeCVnTMEuB7tHmw2xNZJC5Eb0ixrqCv5faYlSvM9fog0r8wpMFwj-ASlAVK_66TJcgOqMnRO4rotAWA0U2lVxq1VeisBfN2EJlN2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=sALoWcUCA2IOpkOhZ8P25XrurhU-AkEnON4p-h3MnW-HXAvlAOCSWGW_7aedBhzHFU-jvSNmANkdvAFlvErlh31t-zTBCqAVP2Mp6TNLfBZohfdgRSQRxP7iOdBcUBER78X-3WzPggZLuASc5jo1dY3CKKuPUIm42TCxR1F_Y_dJHAHKGR0v0J5BvlJry_OKbZwC65r02BLLsi2LHgMuyXa6TlvByw0CHvWbxqi4G5L1kaScPeCVnTMEuB7tHmw2xNZJC5Eb0ixrqCv5faYlSvM9fog0r8wpMFwj-ASlAVK_66TJcgOqMnRO4rotAWA0U2lVxq1VeisBfN2EJlN2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUf_cmzLhvi-LfLU1vm63U24P0wzrkH-B7ybda6nxyK6EZ982RI3NWb5QjPzXz65nILDye0ObiFwnoEcwryXHFbm_2Hh-l-E1v8yuWj7VoOeTiE-H8KdV5qfqVKuUirZ0l80YBDTrHJ8kmx3qu_ySlsDbArsMqDS-E0gNoO1TIIf_cSC2oRvfD6L6CwOXJ_n1ViNvIAr_5OW-N2qtqvpFQbWnlW5FSzGeAal1w05qitCF-fqrs-1G0H2VXfb-R5xJ6Gtb0Jst3g2ngq-pkQVU2kJQplazPdsu8DoCP6f0T8Q2wAf8xD7bto68hrrpUzmnUHZRwe99x6OTOVuDYawSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf1fT1baBfZeBAaqurmo0eM0StgsZmlKGfoTXoK8JPswP8WiUMwlssOvMZp8EFz4WRnpfXiJlTILJPEBOxJIO746b0TVlGGGE7vGwbHLEK9dPrTospJva6MCa_m9rNG0uCAKDhuUjqmoi6TmEn3S7CIsjRVANye03pT67-ubxJSwzt6XWyv0rUBR2gncjI_HWeg4RbrA7EAsexnX-frZAOTshYR8TiuUc76L8YSGQOpvnhYXae5SH8vbDQ721mJ7WWe-swW7n_gK_6ahYgGtv-B0787NW6-f7zVl_5CBEnD7tzWToAh-r5qE4kRr5t7cXWRy76F0TCtBm6uLFZljow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlU--fywcKBQougDMHneCF8p1u9upW9z71z0NpI51l-Q1AKKJbYYj6AmtkfOQARua7IFaUN8xBBOrjKqS9krY_3lNYissD-isN8ne6X9bGOC0qRfxuSzqPZnCLcZE9szX4SjmptZXbX6ODQwOJLcLGN_pOeHfcAQIuQJ7O7arMisNYv4NLlsjedxaeZvSlRIZ0Ff7ei0jFjpaGxBL06JBbB9WQqDFDDzsfUVFEdYFTetG0EQ9QDk8XdMifPITKFAb7gMG6UFPcq-X__dre1yavqFS0QOavptwiRpiDoDjKyG6UD5SocWnd-OAduBVNrFTGyC936e1z-C2At8k4JDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0SGpEhvj3pA0QjvJPwWQtSdljBzk7o0mIgcNackYvZN_ANBNL0EiZZjMStPUmhl1vD5iWaK04KywXSI9KiQgdLJZLndo8mtMg774j4eUWlfq6xR44IPLIDfCtwNmTyx1jga4ewv3I4iCZy0gkkUfOHr0hSWQY0UD5kSn5KbG7ko-B2OwGobMWzNif47JRaIBhDOyCHHx4aNp9b_s17nr4daPnSLDXg8zPRJ1ZqQsYAFUbAhp0cSmQSzgJ_qsVxz02oGOZFISFbJoB84ZSMLnpzNB2aqdWuqb32vg_m3krA1ZSvL14RVCuFjGIr3cmeLYiQhYJuOBc7i1ehDXyed_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=t97c1llWse_8seqhPTcGZ9iKvh5un0YDVK0Rk1LEThbPDTrAyEbh1IgzYgJnijVCClt1AeJo9YSHEBfayiZd7fA3rt-U8h82XDPQpDX6tOgNtUBfmebaw1P9EfRJnUdLjNKrwozV2lRQ5NR5vvITzX-xeA3vRHEfjnH5PkopSBNUC1sZd021MZGZ3dHgpIaS1DxFKz8yhypa7pWMS2T5OClmxU2zVtc6cfHAsjuyMhX4VyhkEtduyaKSjmuKIOeRW2a3r5vuGclFwdhDbKLJZEAf59ncftG-_0XdF1TstSm2f-Es4JVWQwWzmHjVBV5TAS7iE_U3aGwjd1VsmZkbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=t97c1llWse_8seqhPTcGZ9iKvh5un0YDVK0Rk1LEThbPDTrAyEbh1IgzYgJnijVCClt1AeJo9YSHEBfayiZd7fA3rt-U8h82XDPQpDX6tOgNtUBfmebaw1P9EfRJnUdLjNKrwozV2lRQ5NR5vvITzX-xeA3vRHEfjnH5PkopSBNUC1sZd021MZGZ3dHgpIaS1DxFKz8yhypa7pWMS2T5OClmxU2zVtc6cfHAsjuyMhX4VyhkEtduyaKSjmuKIOeRW2a3r5vuGclFwdhDbKLJZEAf59ncftG-_0XdF1TstSm2f-Es4JVWQwWzmHjVBV5TAS7iE_U3aGwjd1VsmZkbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArzzUqT3myezm2E4rIY_bgrfdA_Z_HTpL6XJfbCUG7Ei1SBMhjt0MYcfQwnE6s-OQtt3YzO0rUtt5b5Q6ELDfUbfounNao1Ewq-PUcwYS2BHB4-e7Hgbk2lT50Cni-3b7Ae6qEv4nMR92AqPv2Bs2MkR8ZwLwASG5hMG4pTiNVYdhGwyhjm5q06uWXLXialuK_fNOSX35gRrhadnfwZgXktLTz-B6MAddNMJCm5Hys2jPyjEyl9iwMRjLTz7dtdYOXv4qaH3qz_ln0FVpJw2OlYaCviD9EAXIpZR6_5DNDvOjHIQDwoT5Bp2TFAuLgIqvtaNebMx2VizfEXbunOqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTJPecoUXtUKZFl5nT0gP0Hr5Yi3GNSfXuOIM_onkA3mrYjGZxghDJTNt2jJNRG45QYlNATnVTQ_4o7OVhW5BAe8zvjWUW_OnWBd8JP2udf1VV73CLF_aL9jJPQSqCgpyo2NtRtUDjIwAkEZ7PohhGEwsfXhPYm0AHuKMVXzFkvcXA7rOtL5fEFCM0J1QFSdRXGE0aROjDe9vo35J7yeaxIHKRjKuZI7La8moL3LkONYXSxvWTRPGcCKZWAndSX17g6R0IMCRavVS_0VL9SgMSZNkpRPkIGUv4-QMlXudaMWkj1OdmY7ApgUIRVMPhpOFWfI7UXvUH6UCzwwYHA-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbnnzt24GrTjoQjNMmcP-AAzOvgGfvU4zUeRcBsKlNdm7BrxToj5kfV7REotrF_W3_Nysd2TtqYDg9fOyTTeOTkPLBe6udTfsxDVtF9vpoI-n8m4p5j-UKJd-ZGTgR9IpD1WTrCUxxBXtxmU4vx3Lsu2VwRgSDJaHREkWkSZfvpj3czoLTm15aIe4xWOrPvEW8aDcIHB7GmFrRjrG2kOHbokg-x53NC6S5xhpz9UNV1dxvtn0aD0xtgocQLCsw8IaX2oI8BBXEwrd13tNLmnAmK5-jQRPIiLV4eWzDwAsqGA4y9Eu5fXYBOyAHkwoJAJKxPuNoyeUreSTtT5RvBjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsGMifHXJV_0ZrtRNJ3rbkAmZr-ngSeE1zOuxU6vfNOkW-cV1L8hzjqf5rPBGwb1I1Kg4B_JjC1qoms47XPbNjhWsN2qYaPIKJvO0ClmpinhSWxlDlZtNz7zzmzWxG8wotI2kwcdNvJkO1zbOhw1nqu_hNkPbUbQrqRS2Cp7z4p8H8Nq6Uai96T_W1yqhmP-T3viTkFWQRQ6xVcEXoOv_Xlv0CSLw6h3UE3ZFDJWOG1nAEjUQo2EQmEvi4q2LgJxrFHEU6F8hujtwSfa7OYXmYpxjN5kS-c_pdH1EHVqGe0Q5jr0rlLZW73GClosOgXoEeyvSphlMbF4e0H4l_Qfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7vx4BE_YWhYp-qqyioLFeqUj8GgJCHUy_YzzeyIdlxCl3ZsQEV7kMmCvlU-K-XEcszK6uiWeAdEVQ50SZFZ8Op7L-NZmOp2pOQvYSFd7RytCABrnmpJjHXskgXj6NTlcxeU6Up9moMsLme2tJDn2qJ23L7-x6dImAl-cTR-H69wGspkiwrS43T9L20EYvogwCTN2j9Rb1ylInsvN22EN4j5YvVAg3imdOZqqbbWHTtCeI0rkQXniQUme5F5P2z-hmpT7NbAnIzwOMIlN8yIxcZAiQCIWCKEeM_uwRQM6lD3baFHYAqer08ZEvFO0C-fgchhbIzUUWh0RJ_AS8HA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKk7FD0gwumuwarwtXGYgoh-OyNcOKDM8CVOzSJDGtIqzSnznYLTVgNrbfAIcapfBSHqiQi35ojy1ZiSEy3IgwF-WMJdBaLtdHlw1IMysazewyfqibwOY0UGK8jsh8kXKmZmkwBVn-6cEUSTlByqtDtNcedPmkO_OmIfWq5d74jH6QQzmkI2cvT2lBl9e2hkfU-3ung5oIWuKbfccGnVQSC-ngi6ASblBZXwT1t76rEi3P92hjPv-uCR4GJvSqDjrwSvo2fRfnPCeNdsdWBVn0GuMgVwhu0FEmhCb6Jp_E7YkcYu2YUhghYtck3G20Nvqai5d8AbULWV3tB-UOfB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZhQR8zLAb06zPZjceI6rn8cGlFMcY-LZLJPltvns64eMiLa6cZOySGqzhnpcVOIazMSexACUAzWV2ZWdoKqMkxxXVWUlFUUNH3v1fy-nlZqZUYPd9wN9rnhlyuz32sKPJtRo13ZUnEeg0NIQ2NSLoY3jhCR4qHuATqxjJo0icH_YoBgpsXv4OZ_Wly7TAtdsy5EPTEdGa3Yl3FKxCBxrR7bA5c8T8khcIH0-lkkYDabrZfvLsOC5AauDWRmA8fzDziE2J9WLx7tTcr36JaV--P-JdYrbGYpdEV5szLCCBz1Iv3iK8caxnb_0o3pJiob2KIkx13_0UQ17YecLuxRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQSnunTtcKL0vdieXEwMC0XsLji7RJxd4FCdGzQ97LNsDpLWsWeQIEpTEPyR5wpOuORvqyGwThwNTjKkq7mh7JCSoMuLziMhKOX3pokyvmWl9HgTyBOABMOaq_n0_CHBrwIzBZKOTjgbqFXVZOvPSEpGAJ3mvag6XJqF0AHXIrqKN8tBaWjpknjD9T9B9oouoTQAv_tgxawQhD0RbLdx91xplnqDTE9l4lVQCXNFidO0462y4a2BBVPsuXyuzGMInhUhldcyWCDHurVu4d9oKivfaA8vRvej1l2Ai152wtYPtHE0MS947xLvIctb6u-Za3oUVzmLn6hPVvlvkF6GAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=DHjYVbywVc2JHi3DQ4EpDIGNi9kAyYOpggzobb3Z5bwLjhCeE1nuTe6eJcukYBKYVaUL45Gmycpdw3xuinw2sJBTIAWA9sTlaYsG9gwUo7Puj_o9QNHbvJf6nZC2cB_asy4uhfmuormfHIdsu_ZoYr5kfjOZkARIuodO4BPy8GL7sZDha29BoQqA8BzEXhIatfHTppGyjY12apJH9Wp1eHnrpGs5PsKJv_EJDNjGpb-1Btn0uIIew0YslUfex48u2n2JRsmyO4xB1XdQqmTrL7GorA2zNFyJex8AQKpDAOi1nZv0apv0iuYzbhiMPEBi3ImRBZP23a8sHyzodwSMrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=DHjYVbywVc2JHi3DQ4EpDIGNi9kAyYOpggzobb3Z5bwLjhCeE1nuTe6eJcukYBKYVaUL45Gmycpdw3xuinw2sJBTIAWA9sTlaYsG9gwUo7Puj_o9QNHbvJf6nZC2cB_asy4uhfmuormfHIdsu_ZoYr5kfjOZkARIuodO4BPy8GL7sZDha29BoQqA8BzEXhIatfHTppGyjY12apJH9Wp1eHnrpGs5PsKJv_EJDNjGpb-1Btn0uIIew0YslUfex48u2n2JRsmyO4xB1XdQqmTrL7GorA2zNFyJex8AQKpDAOi1nZv0apv0iuYzbhiMPEBi3ImRBZP23a8sHyzodwSMrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=sSfd_f2rMqLJSfD9LEmOGdKxdeOOcAYafmtXmPUDG3ABBzl_lvzUa6WW_9rbd_eEcuOOIvNPdCrSOilvVTuqTrHlkyqldq1l7V4db8oB_Qs6neKP21QdiU3a7G1EvLFWVLOSATnSgHM7tRiv1l8udN_UTyHkMX1TOpNAaj7KjgETpgocIUGQ9LC9J8jqpguyWuXlleFYOQL8l2RiN-jrq3BPszn5b4v-ZpjAKHFOA7UaSDkPLpQ6h8hq7tomYSm4ZRlOOGvrIgSycBz69LIFr73miBNwG4H-G-HJCJvqLsZI1aOng-04q3iMHhOm_3lkjmGgx6trPO6Vd3XgHwNqhk0RSg0S5mutlCp4O9GvmYn842VL0Bvr5QBOSbKOIqCVCEcm6zh6EWR03_ahDIFave5nSYMKpdFXMQselFphJQVt0IUKOf_H2yYKMpRnl6Dw0kD86eeHrUukBM3DfAvHHTEu6T52Ms3XsqjBRiimzpN7MT0Dx0LcPoXG12I3d4mpAhc3lDMAQMgM-BuWY4PltZ9PIxsvIACP5St2XTnqndqMm6YX4k1ShcYQCKKEwH6_3vB439nPya_chCTW7mSweSBJ8iLKLbAQCxCr9DmWGm_WOJ85tX4rCGaPX8XmqV-QvvH0h2zqGqq34RiYUAr9SkbWOb-4K8Xc2mrUmUD7AV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=sSfd_f2rMqLJSfD9LEmOGdKxdeOOcAYafmtXmPUDG3ABBzl_lvzUa6WW_9rbd_eEcuOOIvNPdCrSOilvVTuqTrHlkyqldq1l7V4db8oB_Qs6neKP21QdiU3a7G1EvLFWVLOSATnSgHM7tRiv1l8udN_UTyHkMX1TOpNAaj7KjgETpgocIUGQ9LC9J8jqpguyWuXlleFYOQL8l2RiN-jrq3BPszn5b4v-ZpjAKHFOA7UaSDkPLpQ6h8hq7tomYSm4ZRlOOGvrIgSycBz69LIFr73miBNwG4H-G-HJCJvqLsZI1aOng-04q3iMHhOm_3lkjmGgx6trPO6Vd3XgHwNqhk0RSg0S5mutlCp4O9GvmYn842VL0Bvr5QBOSbKOIqCVCEcm6zh6EWR03_ahDIFave5nSYMKpdFXMQselFphJQVt0IUKOf_H2yYKMpRnl6Dw0kD86eeHrUukBM3DfAvHHTEu6T52Ms3XsqjBRiimzpN7MT0Dx0LcPoXG12I3d4mpAhc3lDMAQMgM-BuWY4PltZ9PIxsvIACP5St2XTnqndqMm6YX4k1ShcYQCKKEwH6_3vB439nPya_chCTW7mSweSBJ8iLKLbAQCxCr9DmWGm_WOJ85tX4rCGaPX8XmqV-QvvH0h2zqGqq34RiYUAr9SkbWOb-4K8Xc2mrUmUD7AV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای دم صبی جواد خیابانی و پژمان راهبر از این صحبت های امیر قلعه نویی شروع شد که گفته خدا باماقهره. جوادخیابانی هم گفت این حرف قلعه نویی چرت و پرت بوده یعنی چه خدا با ما قهره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346c907015.mp4?token=Lq3qmyiNnsLHExPWJYM2BaADEx20k1K39Mbm4Ka9SJSRnvrE20s44KAKXP0NCSDOYHE8GJ38AN5am7fnVJtvubMf4bqDblDcXV3J1dVrGL5jEuIQn4m555Y2mUnMoY38ZK3CzNrk6gyFxQiGQ73Y3TDDfY6IKj6SkyoWjXnTV8w14FdfSIN2Mp7ZQ4vDK79dI2R_69UtFtj4im4mKkKwMqcem_hnMvLqIa49p_uWcRukfiLGxRr6b0JFcieG6zbZ-dkLp4boV_lQRak714dECgzZdXdVqfuRdLwHOSR1Bg2p6cCJtdbLBdYVfcw-PsyNXX84BPEcSm4xE1eDAsWAHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346c907015.mp4?token=Lq3qmyiNnsLHExPWJYM2BaADEx20k1K39Mbm4Ka9SJSRnvrE20s44KAKXP0NCSDOYHE8GJ38AN5am7fnVJtvubMf4bqDblDcXV3J1dVrGL5jEuIQn4m555Y2mUnMoY38ZK3CzNrk6gyFxQiGQ73Y3TDDfY6IKj6SkyoWjXnTV8w14FdfSIN2Mp7ZQ4vDK79dI2R_69UtFtj4im4mKkKwMqcem_hnMvLqIa49p_uWcRukfiLGxRr6b0JFcieG6zbZ-dkLp4boV_lQRak714dECgzZdXdVqfuRdLwHOSR1Bg2p6cCJtdbLBdYVfcw-PsyNXX84BPEcSm4xE1eDAsWAHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مسعود اوزیل هافبک‌ترک‌تبارسابق‌آلمان‌که فراتر از یک هافبک بود، مسعود درتیم‌های وردربرمن، رئال مادريد، آرسنال‌بازی‌کرد‌. اون درقهرمانی آلمان درجام جهانی 2014 هم حضور داشت، اوزیل در خاطراتش میگه وقتی که آلمان میبرد آلمانی بودم ولی وقتی‌که آلمان میباخت یک ترک مهاجر بودم، بهمین دلیل سال 2019 از تیم ملی آلمان خداحافظی کرد و در سال 2023 هم برای همیشه از فوتبال کناری گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLVvR1IxQpsK67wJV7sg0bfl-lNXOtCbzi1pJmmIisD0PUscowFiDQTWbFhOQQujymqcYmZGShE1vO-ha8YWvY8YVKaugLSTZfl_NFNKvfM1bO8IoM3lbww5Y3KYvoNLuq31cOqhnKS2kSbFFoHPhYrAUBSCYh91va08we51DhHBjwQqlkRoWTKdhx_cQ8Py3N25j0Y3NA3G60nC-0LZb0yo7m1sD0gIW5e48GSZxr2GVeJV3wu577IQyXAiWDUHfsNykoWOfSj74dueVHjjm68-4pS6Pgb3rA9MMd4PDX0Ig0T19pWDNGndfwl6n-BW0h-Q_2BlNX_HAVSXfHfvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuoZLpm3sLiIrOxwQ0nrtfHToWpZ0lmG8TluuZ_u-J9158hWClNJQX4CmJCui1k1wmyEeXLtDkShnVRsMR5u_MTXFBl2scUkWDclb6vVhb6wRsPpa0eOV3616FtAjYi_EyKprZczUv3a-LBMT3117cMPQlQQwVdAAxb6P9TrZdVasG_owRyBsWdAyW2MNdXgG1XYUxXmYzHYdvaWGeJNSSRAlEhrhmwfSHPQBYOH5UjFHh6UUyQz-6Ary_u4Exv6WddggXEtvPCQ8VEVOs_Nq0iigLeEL07Pexpclrt8esBur4cRWECYtwFkGR4VMErsP1544GsP0eUNcnDZTOBxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=vRT3d6iN5-rx4M9kKbAwj58eBIzkboBROJGZzzW_Ucc07OjD0CnbS38vYhTycc9AlJHgz9Oi1Q9nnIeYCHMaFHkIavSW5EsnKKTAMAU-G8kmPv7AX1RSzi6AYG-tCsRED5eMeqwxAhpOERYgBVtq1I__udXZhg_DIEK0uLPir6ZiV2zukb3rOeqDWfgAaU8eIts9vUvHFp-CVZlS-i2vNbh9WUQharWI34gdaYZa9t_OOQEE9SXiJ65dfxRX61Um8PREY0Kh53HanSO2_6znbY5fFW-D1uaIr2WNuCmUBl1gGMdYbt7eXBkxO2-aQoW49wd_S4pBkkP7LxBbdHnl5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=vRT3d6iN5-rx4M9kKbAwj58eBIzkboBROJGZzzW_Ucc07OjD0CnbS38vYhTycc9AlJHgz9Oi1Q9nnIeYCHMaFHkIavSW5EsnKKTAMAU-G8kmPv7AX1RSzi6AYG-tCsRED5eMeqwxAhpOERYgBVtq1I__udXZhg_DIEK0uLPir6ZiV2zukb3rOeqDWfgAaU8eIts9vUvHFp-CVZlS-i2vNbh9WUQharWI34gdaYZa9t_OOQEE9SXiJ65dfxRX61Um8PREY0Kh53HanSO2_6znbY5fFW-D1uaIr2WNuCmUBl1gGMdYbt7eXBkxO2-aQoW49wd_S4pBkkP7LxBbdHnl5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrApB1TJCqgNvnBR6loM0-wf-09Rn7YDNB_muLmMxRzhJF9IWa_WCEwDeK6dvPkYU4ytqlGnajRAF-Z69uLvudsscPOniR2tLvJvU5DAIaaQfP2ZBnJtp91MsOkdgTpCqoroxy9r_t_V2qUFTxUePcpRDmVryUG99QbFDV3V7s8CPjMcpgZtzOG5reETbaAbrhbesr8jGHp0OePn-DISis2QDhBVtHARSQAJVg3mG6QBsY9UJooRfJCr4tSPgz8RvLVC4vObNxvhZ1HdfPpJg4hzAKOedAvrKsVGp7I9ZxNwLNcmPuHjwLXpFVKO1JWYWpB9DM-b2c9aq-LjUgqXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlhARet2qo8nY9KEjcekeQCXRp35cPzykMEqk-apoILrbLBZO8nv0Va6weUOv4UHx-W0Jx3OkIVPPtEiy8q18DHuHGyg56Qz4VzZUgwvahRVx60fN-32QGZwNA3qcVLvnpBHykbRnzlzFSHx-ROh6BCg1zMfG2nihISdfVoubcqPZDWOdPDvPec03mE6Uq9HAddlxrAZJyykTF0X-AieOt4z02xKdvyRiVVVy17-xyiQXZtdy06RLG9C8TmwwGk9xT56OpyuRcVOwYSwCeDC5VRrcce-UipAZ0VdqOgMON2Co9W9FYIRM4b0nYdzr6juhGnri-LWIYTcX568wUEe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joLOw4_E0Ai3duOfY7_oCjubWW7BCqyZVgCDws4gpnMRE4ZHvUdkULRShc5hpeyREgITxQMH60aXU78enYh9qlvbEghcT7TckeRprzaq6ySrD7--rRe0RugzCwhan7yU1HOZOanmAMz8mlDH6GA5FmpFYwgYuUrs4C1AqNH_WLPh9rs-etlWj1FAZ3smZjWjDzZYp3CGbwzMP96IrV1l1NHyDxebOb-w4oauBFVUutvrzdkkkyELuKjBZ8qYGY0t5ckgb32Q1jqOG1E94Gj6L-g5pXB-22t2_CfC9HlGizxKXWanKXteFCm7xmThIPSPeLa1IT8K5Eig7PLTl9GUiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2IxL-mTR_E21e2b_CkkbPtIVP2QNpcxYTBVSytqpbsdhLL9wW_Z9iuUWtmhLmvQb5hIsaTd5aa02Raprr6tvua_XCiQHwUWMEhf2CvKoY4rT6HF9RlsUGLrFRth-nsd_ObsUWswklsyg1yhKW7A38K8YWbNkzsOQukFM0z8ducqIAwsV-VAw8hfCo5t6bv-BWeo7yjyj9wfxc6Uv-nGf1fOYVmPRYcwjgGAVREswADiNe8Z-sNhEpzAcEdKnaAGKXXtZk-G7_sa6Uw7-5iHhS7ByjZk2-IZ65xw7osuIjQ4l41QgiLvTMK5k-kq0Ts5cZkQAPtXckQJHKqbcRiu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb5fimENuMiKKii6N4Pk2MG2LVvqbRzUAwfUzur5rW2_QhrwiG7Esy96eyP2TcQEjRPncZ5LMntsVRHgEQXLJO5Rg3u5Yhpv0jYy3byL_i1ZvkI6Vkk6vhlIuJdbulUZs0pWGSibQW3vfwqR5sJvTB5e_dH7U7yA6jMkL8syW6yaRmILz9xFRZB1GRwofNgbjjjWXw67aWFbsr8nvpPkDcVGIcwK3hDF-smQID0G57HKA-g6saxm_xZApBvqeJ8gADDQsxZGH0j1eiYgmNLFWEspfbLcq_9txy25SSW0V2OaezBr9JVj1Tpib5MnSonkX-zFJCfd9UoMpq7QilJF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7VrzEdZfmbfFFPaHMz3iVM7RfPA90y0ASYjAxBPydvywbOoHLw9C4eCrkLtT8oqCa0q2FfkG9_w7cvX50C1L4Bp0wNNxtqrfkMtWHMg6ZunH_FnkzA7XHQr6QvF33DSZxNGHU7g1ORhvioulsqYsw94NPHGQ8iN4OSXBrPd2yn7uTNPw4T5AI2G3_u4HhBwg7m0u-ksfrzSYhllCCBNAZdzlNRzplDO9sJ2I1_X0u_VgQyv-oEwZ5NnIe_71PHBQY65KegkYgY5FMWtwAH804MfK3W6hGwsyIami6lii-B6psbv9obXvlfvXCiELShpCSmW8oO1DJjy90sUXw_vLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4LalTv3ZrClMKog1ccUCxb4nBZDqMKaCmFkrbENt_Di6OE8c1Gtpf8gwWsjtZoG_aVql8gF-flmjDVt-MS12UVeZvZ8zFIqNRns3blFjbsZhcqiRYdDei2NDI6wgKC5aoLmYnq1XUaR7zoTDjsiPvIJbtfuiQItrK5d8k4QA-plFRjVPeMpZr3au8yuIjjvV3ycXin-YfOgGVzdqpbxSDHX0FdLEk5iuiZYINovXYhhk7ns3jwkHoMCF9IM5j4XUMoqkuZdZO8PyjFn31caAO1SzY_WyH1Va6R43c8BaY0O86hvSGI1CUadHPcCn1cjR5QE6Qa3Ot848cPQ0LJmVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWeGjjjPhL-qRUnKQlO_Iv1UjACuQaoqeNPmbT19A0PaEfQh4o_xsxYtRwIVxXGqdc74LJpmA_peMV2FRGo8mIBn2vhhwIYsBQqlTs0WJQGjyEbNk8QwGYI6VViaACfH0e8pZObLckZ27XcjdKU0oCKSwUZvrEIW1zSlrfJm6mQXB3IaoOroaSmCv_1eiyIKZVRconMEnVwkrFiQz_tdcp8PF6acA7LT0veVnM3OWrL6IEL5efQV2fYCnC3pgh5ze6Q08oH3PAX1TJvkQcy5bwK-DpLraSf_Zq4f-PgKPFZnY3pBMTxGVGKLzkUUZ5PsnZSXm-K5g3u9EUWYle7ycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhbKKTlh1j5wWdvEcCXlLsHTxUpp6zg1eJg2T0ptzzsEwGeF4ZMtuse3BMAKtCOh9dXWPUs_cJssLnaimp_0MxhHkooc_C7a_FxnJ3QTc0ThCOAXyV1CITiZiUfMH_3XPqs0DHa4chC8C3ttaF0QHFCa6Y8T2Y3LC5rJURddbbKPWNNzNedSyM8QZ4ogR5D6M7S_jODmG7tag1d5A396vo6el9r3qxzY568tu7kYJFmJoN4IK_NAbA38NaygQUz9N7Pes-XeySU1W3wrsU8ioUMeZ1wTlkNhrl27rMRT5UnJ8kG3LTNJ7gyRWaGSJDmaQtehprXdGdEPcIvGaJUMmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=nZK5yBHjh15fF-EmLgwYosTV_bE-iwI79YDNkbe9bv1KrMUliwz6oEBSKzz0KoJgEwJQaevI4qpVxWUI5z00fOCeZKSrOKfjZDe23uuxC1gPny8C-4rkGWxDsYxt7OsmPunLVmS9WzrUiZ8fvCpBLrkhXdNCIsVjxDXmiymNB6Z1pOs54hkC0EjBTg9UZ9UzuGYvouYxM_ImWTCU91_S0PZmLI4rOLDI5GRUrlB5HJuYRpSbVc8UkS5dovbSaRKn-Z3qkJg_tJoJpJPeeKjjpFBXso3m0bHlzOOqTpzVe0ggVGZG9EwKktTAb_X7LAxREB-uv4hvaVFTHZodkplV-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=nZK5yBHjh15fF-EmLgwYosTV_bE-iwI79YDNkbe9bv1KrMUliwz6oEBSKzz0KoJgEwJQaevI4qpVxWUI5z00fOCeZKSrOKfjZDe23uuxC1gPny8C-4rkGWxDsYxt7OsmPunLVmS9WzrUiZ8fvCpBLrkhXdNCIsVjxDXmiymNB6Z1pOs54hkC0EjBTg9UZ9UzuGYvouYxM_ImWTCU91_S0PZmLI4rOLDI5GRUrlB5HJuYRpSbVc8UkS5dovbSaRKn-Z3qkJg_tJoJpJPeeKjjpFBXso3m0bHlzOOqTpzVe0ggVGZG9EwKktTAb_X7LAxREB-uv4hvaVFTHZodkplV-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=vuP6Zj0M8twu18qeZXt6VTM34fYAfCh26APXhJjiQP0Dq15ucu_3YrI2t2eWo0dW8fwq7MRbZsV6dX2WrCvLFiGmi3HrNQnmg17FMIjq32nrijTnah8a0-O6IXiHt_oQM6UDxdlPBzE9LrDSvUwcaQbOQDSRdSY8VTI0e0lm8RYQJz5qJfEPZwQNaYxrs54dwKomazOdikxEkTbmC1HOXCLuFQRDGAGiOE0gbKjsNVTidGq8bI-1OIv_4_QfhUDX-PrpMe7f6UotrAM5RZ28JvwSDTfMr_Jf6sNnvVpa8USsEAWbYX8sFmTPl17gZJpi241ofJjuekxBAwg1LV0KSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=vuP6Zj0M8twu18qeZXt6VTM34fYAfCh26APXhJjiQP0Dq15ucu_3YrI2t2eWo0dW8fwq7MRbZsV6dX2WrCvLFiGmi3HrNQnmg17FMIjq32nrijTnah8a0-O6IXiHt_oQM6UDxdlPBzE9LrDSvUwcaQbOQDSRdSY8VTI0e0lm8RYQJz5qJfEPZwQNaYxrs54dwKomazOdikxEkTbmC1HOXCLuFQRDGAGiOE0gbKjsNVTidGq8bI-1OIv_4_QfhUDX-PrpMe7f6UotrAM5RZ28JvwSDTfMr_Jf6sNnvVpa8USsEAWbYX8sFmTPl17gZJpi241ofJjuekxBAwg1LV0KSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FugyBtfahNvJf34kiwPOAIoEIIFh33sYLEBP8pnDkBKSEFNNFUXjL274tcpyZL6qjuTCMHkammpDpm038K0kQ2jnoI9Vnx088fornlYwxT0WflNniez-g2oQSwfsSia00I_j7vFBPFulfBFx4OWkwPIUiqEmdgTZlzABAujrWPlNxJi1uf3fOIFWxNiNMhUe534mJId6Cj6YzIYjkmrbxk76O8DYVun2k2irDUAC9XMKWUbwRomTJoaRiLJ5KPPL_IRjXl3MpLuilBmi8jBgbHQyMNF5ffViXrxBdk3AefoQKdjBUMKZKmWVK_Dt-Wdbbdav5rU2MrKl2gf2TRDtpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3Xq16jtF2PdI1XcfUeZYh7iES6iC5eUuqCNqDko0QRsQUYp-MeMqei_TPaoYJ8SGbiVgIRKjqZz1fIBNtTrDjRgqqnmL_ugzm-Uti-sgTobb2rWJGbCPZwfelZBpizqUDq-ONeH314E_KENYlZwsKI0ZwlVZLEN10kpDgJbRHSmWppv3vlz0KXEQ827mQqGmkf1qwyeai5x1dbxN4VEZTlM92wqpXy2jPlkLJdgAfCkJ9UTQSwF4p4xx-Hkg_IAk7U4CP5Du_mdDWCLYX6y767D3k1LCSF8JoKLrVfMl2WXf2v6ry_cMssqyRegaFfAw9ib5x8zbNYQbu6yA5ABXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=tAi8w64uhSyHJTpuf9zb21taCSWUu7dcoA89alM6lXjb90IsW6dP2rilIAhSj8XeS45OX0JF7fEaC--xP_Pczs3eSiT0Ru-QQLQBYX6-OfJmUzyGlEYAvf2mHVXsomwECi4yLJU735biVMpQgHYET5iwLEDvS6JnqZU-2-EgQYTxwrr3EtrrL_H9AxW-XXzrqMa3iUfe402yn1RhmcpOU9ABmEbKYXKDG8yTmQ9R6TGegfB13_20Y9t2dwHoKI73cmjZPoqSLLLNRxtk4fvhkWEY366QXMJJkNf38jISrWRGix7Te7BFAYWW8OOTUEoj1x3gqE0U8UmCwBSinZiH2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=tAi8w64uhSyHJTpuf9zb21taCSWUu7dcoA89alM6lXjb90IsW6dP2rilIAhSj8XeS45OX0JF7fEaC--xP_Pczs3eSiT0Ru-QQLQBYX6-OfJmUzyGlEYAvf2mHVXsomwECi4yLJU735biVMpQgHYET5iwLEDvS6JnqZU-2-EgQYTxwrr3EtrrL_H9AxW-XXzrqMa3iUfe402yn1RhmcpOU9ABmEbKYXKDG8yTmQ9R6TGegfB13_20Y9t2dwHoKI73cmjZPoqSLLLNRxtk4fvhkWEY366QXMJJkNf38jISrWRGix7Te7BFAYWW8OOTUEoj1x3gqE0U8UmCwBSinZiH2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=nLR_22xs1mYmXBu_slDPHvtvyE9U4t-IfYL47ECN4_Bi3PoYNHq57yVn88S0BlUY7p1XC2Yh310UQFohliroUDyFb2q74ppj5JeWZZPWdDYir5ssAIJvQ8zFrJWV8XalOVt-XH-KHvGJastew4nMIDEDx6FNRGxU8m-WEBcSPtMAhOOjSwjbCYNCrMiu1E0_1f-lZwkqAGFvjnr3pMKACvvX-cO5dIvtnDlXAqU858eTuaEed3IQAATBGYW6ekQw3bx-PtAEYXUQ0UQGH-0aE16piJIPxm1bhaaCIE5TqUz3EzZpWGTTXIdcHk9Bo570o10Q9ghCB_oWjll3YXB-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=nLR_22xs1mYmXBu_slDPHvtvyE9U4t-IfYL47ECN4_Bi3PoYNHq57yVn88S0BlUY7p1XC2Yh310UQFohliroUDyFb2q74ppj5JeWZZPWdDYir5ssAIJvQ8zFrJWV8XalOVt-XH-KHvGJastew4nMIDEDx6FNRGxU8m-WEBcSPtMAhOOjSwjbCYNCrMiu1E0_1f-lZwkqAGFvjnr3pMKACvvX-cO5dIvtnDlXAqU858eTuaEed3IQAATBGYW6ekQw3bx-PtAEYXUQ0UQGH-0aE16piJIPxm1bhaaCIE5TqUz3EzZpWGTTXIdcHk9Bo570o10Q9ghCB_oWjll3YXB-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGDzv74jIlFlGNwV7S7uqmVpwzwLIAj3SkPs7Onc9t1VsOET_Hu97I3tgS7syzeIEFibUXBIOqCEndlzKKs9tozP3fHOoFVFdsnHdkgsPrQAfAdEp1dnAJdT8rkPCPk9tAyXgv3AMW8NpA7PQmn6nqwYMLGJO5pq3FuGK87fiYiTt8__X_D69b027ydP4mhK5_RZ5hdb9NL-Lu506YMgbK54Qfr4Ikjt8V1c1H7LVIrsCOk5SYrXU4f2yMTplGyYvwYQyXFskfehkd4J6LIZnF5bBPTgOMOKOWkrFIKfuR2Mb83YTTJ-0MjYF4kHokXzk94kt16zPeQom92aivGLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPsB1lNGYPRdlvXmjGer8TP7RLpdjVAhEWIkXa59Hes1huDDWVo6SOOmYbOdhB_Q17vvqZ7dCJQRuckm2eKwNl4aikYrMuGWsoeFUPY3w9-_utb_X_4frPPth_5_x-VqtAeYWaPpbi8z2bNOSlgrH9U9ZfvDmNKS7tGK4JrAd9U93xaOcdPBdCJWXdr53p4CGMMS7Vr6pPD8prgaWDq3y2cSlyEgMtmvgoIzoZnru_jX2qRYHZNVRlHtQ5Z3kxcntCkIj8kLt6fEDghsKpB2emPLmKaHGQbnk_LMDstYJ69Ht0c5EuaP4_k44TXnRNElS-7xljS94oQ-hAe0bFkWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVG84MlwdSCQ3xC6S4ZrpSO6-KX1Ep-rECTwaqFtL6WrEZO3YmE32_36sQOAEV_a-0qt5yQkPGb9QdP7zS8VyUjXLmn54T2F5AePF_Xcat5ij_VheMEyMG4_ZFymp3SAN0w_eu2j4sb1wh3NB4uOEdgGVYLBUUth3-thC51C3mKJiJBLkVxXPzSd5NjkiP0nJb7u-xstKVMEQISvXXkeVkl8IWNz8YCLvLe55c5A0RJoraBdUchdrb-crHINgTxfaRotzj40StCnc74uwi-fNKKhzAqBmNk6eo9xVr6R4vNyVx1rXUINxVDQu_UOGtI5pFQ4Tg_QdPXXyGDPFLy_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LNU3JIHnTPREmBfdbJ1N9RJ_2MZt0mtGxr-3OMdN113MfwsYhUiEeUbZp_vVQWL5oByncD4hvTEZ2foB7DN1MBQVePJ3ld9KHsJHRJ5IwR1d69PVKcogclrqbev1tOv8LF7HG7dTPw4ha-dgENZ_qKBDs3TRvJJgE07ipCZhAVRLDdHG0D6K3cFWx3xqV64bDuvVP-fawxskFYuDEcVU5NNuIsUg4RcExj7O6xE8UIzTahBkj6pJ4J6ZIIv1ihnMBBUPR95fZeHt-e9f04wyznw_pFI_y4Oa9k7Hqx_9C6BY40gxvFXZAJroBxEiTWgS_DIp578n8gfHfu4VknARLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYMmJHabYEdQ92fzR8ymNOqIFTLzSdUWl-uwQcJbteeBMtfsZX5GZXF5QxH9Zcywc-Go9e-jJAthaM5QhRs_sYfKBb7N58N2x8h6i0XxUIbPmNf7-gAp_9fmGHxm_v7GKj2jBDCUv9PqOADJGiTfG400eTPjwtg9d9iLrUqLz4BOV9EJ_kYO88wZuI9TcAc7xqibjDBFg3Ks8dbW3Wei5TqKZEsgOtf_FYNHUnUUInOd-adSbLDOTOE44nwKl_wkkFdFKKnZz80e44IqDp94IUkJAyIlYkuUvusPQwNxGhjku333ux7oanRnSqLnbW_aiCXQgzoevrNqIqLuzcIqOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmeZMtVmotGawIuVWzn1-rVV5U9uos1M67JlUF7VaUQR0UWPnMMgllviBeLna693BUYkX9QYGSiCmAsXWhmM_zdnzONPZpKxlFPotmyMZt8JI4jkDQOTFORi_GL9eeh0iCTwD0vTcAQcTcR1bGLUnEEpljd940ur8tcxUDZUCksbFxPzLr1RldmXNLMDXzYFkoIiOCY8WK-oTCMTnmePrWpauvNuQk7ec9JJDMIo3EBo86ETUJPmEe7tcOco3DLOKOOc-k2h03sxGxxso_M02x63QizcAt_hr8qbWHa_MsUgt1FYn6J41IL1kqvi1uRFMAwn2bpM9H6T8AYYmh0KDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vrl0RO1DvnKrQJvvAHOtSkwXW4ZMY5LvTSvXqEU1dVwt58qTbY_n5m2YNc368PuuEZ4gOS9GUDgJKXhjmL4YvhSIMgm4GNKhBJi50Eox6uKiw2IWN7yGYn9oW0XIgcDHxApho2DDMMiPbHC6OidSMK6K95x6V0Km8Df2CWrD8XbuVuCGMUgI4GtYKyb-eq-C9ObJXA45IgMu-1nBsldeoMm2XzdqvfFk0BtOV8U0ERer18o0U0SjZVoXqh-a4wLjlYFcCJJBwWNhlMF329xy7qiVTzQxufmmyCWspibPm4DSiYf-7UUru6ELsWSkWUTmqb0CtavAOzGq6_KRAaKgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7j7oceXd7IUGwd986Mb-Y8OB394-85GPAwAvPxiweCOUw-Lfz1cN8VWxgGk43kTqmnr0z98sTtZ3wIAIHSBPUzqIBWmLcdg6F_5wEt7Nei9_23O9qjonSrLi8sYETN_0kYn-fZNV7JifVVgtWfq3gThOZpJEgyzq75GIh-FTmp7Bz2l27UjVhu3g1zVcwdP8nNizcxsc9L__l5diAW5t3sz2jm7YfHu7n2AhesS-Xih7Fw-vejHD2NLg4i2h_R0g84MXEpkDtE35nmJ68TzNIXrk3Fw1_3vsi-ew0TJxATd_tT7pTfn0tj_BJOgk7FVPy9kRoyOEuvvBDuMw1izRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHiFJLXKt5uCnrdJKvMPOok1yUM8KxEovLqkeXpa42RmcDn28vCMqFXInmUK_k1vYKLm_l_Yr0bzz4L-18d5dcv7jHB96D9DCwM_18mbjFnfhzuKXg7VbgxQDPr8t_t6EmL69sCcmNjEOdVJgCcYfmIvaq5xPaIIduDmJ133Mw_I-nozSSB-uMuHdjyaBJ9oPbyh9whwq8rXvs8zotmiUkTf3hdCYFe22lVFGIKDpk4fM81JjrIOBw_5zm5pktxuXO0osdONJASvjjRSmCIY_n-67TgrZ8KNAS1654liv_hmiaohtsGzoq7Ri_syoyXbhlooAkUG2lGP6bxVP0S4RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqpUzy58mh6nQUcUM1lcTkixQUCN7ynj_OaKtVouYo6M8nUHHofDu5qsrlS6HutjtKRN_GEOK2qH2MEqeeAZ_0KEaJggupAp6xZ-eWB3xro7U0E_opCWoDUk4y09ZVZ4iHjMZpy29QW6HulZByfcscPtMdLZGr9JRoBk-5HHGJIbsy2jXqAr-8gVemZ4rx1vpE8VkNcGpKggNXY-3p4M9KHdYKvM4xh39L3GUkNxcG2Yr00dkPAnZbiNP2kf37x6FRol3cH2qljh4Sa9frarFPU--xJRNCU5R1UDeDIOROvgdjwDDrEcyam3A4mbqhpocROQdbmDzVNUmP3MG6TkOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌‌های‌رسانه‌پرشیانا
؛ ابوالفضل جلالی از دو باشگاه اماراتی الشارجه و الوحده پیشنهاد دریافت کرده و درصورتی که مدیریت باشگاه استقلال برای تمدید قرارداد اقدام نکنند لژیونر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24425" target="_blank">📅 04:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2mIslvvcz78DZPpiTxJzgSluv9v5mFb8RWlZQWEGDX4MuOL_cSaI1_JJv3w_fc5Yk59xDmTj-ZNiXMxMukfQlKQRLa3khr3oDPrhaC1WZqFB082v-wumUNGm4C8k8U-KVwO1dKNgaNh6bkLrmhElXpPyQACOYJ1tqCnFPz-oeexSqqNSaXf27sNW6c2rsySbrgE5vNEE8sprrJIu9tfy5PMTKxbwvVoC-SBK-fdfq-EN3hcrfw8Ug-lEhHmEh-D3jj4iR3bS6YomPsoBUB9ESx0vAx0m7QNQ9TlzUmdJ_cJtnnEN1dVNFq3p5s5FNgwSiZi4C_z-2iA4mWSaPYWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24424" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=mGbiuOryNaL6lJORC06TBs1i0ews4zQHvqdZop4A4kpG236vnLvCBMkO25l-OwvTCCrE9SxoDXrYlECifUIfZQazIOwACnLkZJ3HQDPtYVOD22d30dyeNswzwLWoASQ7IHixNArSxfiWgRjBtvTKSfi5VNK8J6bXIkk2XKZPO91YMZs9b0RjrRFk1mlb8lRxY9Saz2_QC1uigYWAqJNNNUExTeK6eN75FLpCFYOkSKM4Z5y-c6t7I1VSjDlZPdjEMZ71GjTiCPOAch7UFQOm7vAT3S0dT0xbDRE1q3C9fYr051aDRZCSvZPJ6hjNsvO5Zar406PUEoq-z7382sXmNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=mGbiuOryNaL6lJORC06TBs1i0ews4zQHvqdZop4A4kpG236vnLvCBMkO25l-OwvTCCrE9SxoDXrYlECifUIfZQazIOwACnLkZJ3HQDPtYVOD22d30dyeNswzwLWoASQ7IHixNArSxfiWgRjBtvTKSfi5VNK8J6bXIkk2XKZPO91YMZs9b0RjrRFk1mlb8lRxY9Saz2_QC1uigYWAqJNNNUExTeK6eN75FLpCFYOkSKM4Z5y-c6t7I1VSjDlZPdjEMZ71GjTiCPOAch7UFQOm7vAT3S0dT0xbDRE1q3C9fYr051aDRZCSvZPJ6hjNsvO5Zar406PUEoq-z7382sXmNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
عارف غلامی بازیکن استقلال به این شکل جواب صحبت‌های مجری‌صداوسیما رو داد: آدم صندلی دزد از مفت بر هم مفت‌بر تره. اشاره به همون شعر شایع.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24423" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHbcFfT__keJimuNe8vE9JUKH9-OcF7HvfMLu003VO3NWQrLNvL8jOYpblGRXJimpFlr4m62Y7zKDoTXTros-eJOw4VApy2Tk-oYm_HwVJ8t-tvUAKbQhDkW-jViCapRfVn0Cg8AuJiEzVaJIkc7x6_GmpBcooWaObgUP8wETBxYsd3sFeiucf9vNxhFvcDXZ0rkd0YXOkxRiYI6gBtmU0DKDm32tGu-muovi3_a00gJwJSZjX7bcYfnRBV5UEoCq7xhkara_FE8WnzfhqWZFAMt9y0lnWpa0ZrvDzkdEfslO0M-dB9yjFR50wBb9bq5bfvrCR5XmeUQDXfM7yDWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=FAIKycAo1EruwAkrBHXXKKcnmZ6N5XBrvRLPC6soMdTekTmkaYpC2uRvhb_NKlZPvsPxRAzyb21vZ6lVmvwurWbe1C2PkavtPrMBXHNuR9_HJYe2YZhs_zZpDbkZoMB-heOa1LIsjL6qKnSyp8iF5Xna7N_ZBbgv12JZy5koncMUSMW3dRA9SzRL2TfGd-YANWjfflgTTss00bBneVmFu1DUcOsIWOmv1vB6YZv4WSjS3CP2FrR6ae3r4IahV2MbQF_q9Xu-eEpDRE-a867E_putH401PNKJv_sp78JAFpoyn2yofC0hAwRXThqDZR5BjZQU9QsudHQeASyC0OiqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=FAIKycAo1EruwAkrBHXXKKcnmZ6N5XBrvRLPC6soMdTekTmkaYpC2uRvhb_NKlZPvsPxRAzyb21vZ6lVmvwurWbe1C2PkavtPrMBXHNuR9_HJYe2YZhs_zZpDbkZoMB-heOa1LIsjL6qKnSyp8iF5Xna7N_ZBbgv12JZy5koncMUSMW3dRA9SzRL2TfGd-YANWjfflgTTss00bBneVmFu1DUcOsIWOmv1vB6YZv4WSjS3CP2FrR6ae3r4IahV2MbQF_q9Xu-eEpDRE-a867E_putH401PNKJv_sp78JAFpoyn2yofC0hAwRXThqDZR5BjZQU9QsudHQeASyC0OiqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ms8GTNxknGp3_8Pur_pDaKUqpT1x7uPGhQG3s1vH_6kvMAmHUFKYya0CfIq04a1cLdTv3gCwcexA4JZobo2ATf4tl8aA75IAVi-451GUP7qZPg5PkGui4IkzxC6RA-yMWDqXa6zSnex1Dr7xmqj-6MsC9RSMXk6YsqN5DE441OFuT4Ohk_i4mYN3ypl9zveBR1siTSWGDk54r-u4D1r6bKmmUydx5aAefyaINIqsNqRtRge3S5e9uwL8pdkqs9LoQ78kKXo07Qwt4Aro_oFhABXu5GUrd87Q6LEOrGzxnEosDkoajIfma4UKETcZ9Bo44r7IrGvN9RvoBx7g0EGJKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa_jh6h0varieYJPtrgsvTmG7tOrMezRT1_RVovjvJgd51K7lyQVux1kJmHgQs2boQ3QDx6nFIl_QfJkITNWcHJ7zrnAjh_pSLxsvDaw-TRaAO9iEJRxJa-pPqLGknQWj72Vgopz16YHsdONhigvmmvhHTF80ckL2E9d6TsTcdc3E53xbKn2jlIZiG9JXb9Fy-cchKUAPOV_sFqwPMwBaPgGuC99okV-WJ_7ZxyRcfqr81i2f8BufKZJNJNCfKLtGUeS9SsoSGBxQaAZ3F3xi9WC95zky1_4UXpl1LPJDEbxEICjoXYXbFrD-hoSmjmIkTyjcvC6tUmQjsDPn5F5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3EfcOexJIC17k0oCAqmQXhUVcjLZ4om1koYiqPfZHMD2y2pWFT2M84iNBsKOBTxTYRm3-8hgQtYJZaU84kM9mwyU0ohx_cNyg7wU7PYfDZocBhV2ertqp7PPfjHI5z65cG098Fq9ziA3g3ufaVCbXm1cJc0s8XGJOubYTNRGb8nH9U82_oJ6fMhRnNuePpZkErskTfYD5I3d2D1r2yfjN9HuJ7fmHlKVnTxVJHn3Q7u4taio6KK1MMaYEibDcVj0TmbVKXHc3hgaxsTxaqDHQZjmHGmf1tnSKrMjV91MerItbOhjhi5mu1ToztNzyZ6E3wSfxfwqLqNp5531Ns68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnFjoT3mDedwaDPL8YFgzcm4y17BogcU4QUXwfWwzicsHTlTTIvNib4LQI3yqtY2bsi5GB3muStt59o2vPCoxnjxGnMkKswYx5-18iB8sQ_XvvsgSELs2_VBG0QhhWR3uT-U8ylwWkcQV6FResS_WsWdEzHlY6SmweJT_njvfC6SvA83IQ3nsXqc_7VOHBOOdUVNjJyJxiGwLIVHQDzCJanmghxxTOFr3G7dbOm7uuCnu0Tg0wL99hrVLlFP5aN6zmQRmIaPrmzfzOKYzOcrerLIAzfvbTZYinP-Db_vAwPQbXlKF9ERh-2K4Lt3klUYMfKuBKZn_5zw59leRaXJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do12cpAh66oppBCLbk9GSMfaYmKsGG7ETffdQ7qDvnm0RPN4pOHZTY3maRD6nqxh6aAWBW3EKUUim_9bkDsioCW326igUT1RUKUhmo7cqVbLuuwA26a4OK8DPPVIBehvs6yTyknA0pFRMdIx7J8DU55UP19D6O6O4LXGBI1J9LcSIauoaezYl_AoTfit0hrHMYMf16N0gDAV-9OESmL792CNu34G3BdqODL8pq4IyMBgP2q7EiTxQ2xuUvaGxUNNpM797eBNjct0dDZAXwJaj0hd5YTXQOPYtknrU6bEQppwmXJZ_K5M0c7TMmVe2huoHJzTXzRo99xxSYCeFgCvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
علی‌تاجرنیا رئیس‌هیات‌مدیره آبی‌ها: وکلای ایتالیایی بهم قول دادند تاآخرهفته پنجره باز میشود. انشالله تو هفته آینده خبرهای خوبی خواهید شنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24413" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiV2GlMynwO5B1Q2Iy1kqX7OarzInNnWPEqzMB8IzxzhFuCUSEsNl13OnLx9DT_8f6N02OkdgVbQhu5ZGlARSchNDTJZw8xxgdc7nc3oGXzcSLaBML6pKxgTbXFxRVYWhpDcp8vmymeQHnCtuKnF3F19c60JVyJZ3UNEQXrngQNikcw7uZ9m80otexp1s0ekEM4YE7XpShKcrodJTxjDSbghIoz-6yUJDeCPeMinIKS6g0m3hrr_V9w6tV1wN3mg30EHruOghUxaL_YI9amNW8luEcnEc5710cSmh3vGBJOfhDX-VLtZKdlW09DBQj-TBEGLwZfJtVBLCTB2Zs8cGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله‌حذفی‌ رقابت‌های‌جام‌جهانی؛ داره کم‌کم جذاب‌وجذاب‌تر میشه این دوره از رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24412" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzbLYioqGVZMaYJSL5on5AeVQZSzKFO9XJ6a9Vy3GtYJmjMcKUfABpm5n18as9OL9QERhZSrwBFPiqKf0NKCVS7UyCGQ79zaWjjvGCu55vDPtP67aFFK_G5r7sGaxzPDwJZz8rHlHeSTvBbIUwgblq8PpZjiUk9rbrMp9wyx8yYQYNCCnCMJ6IVnxLeSIL1WuBNQQy5kw8lQu0_VYd0r9J8qy2y3qgrREoNz4vGE4XJeKhaLCXhBFUe7W893UprocnJPdRgfqEbpyXdq1eK71RmEMF6oCBc-HmrfhwLrNlvk78e1qplIep_8mTPSzEHeINAqs_w1BD0wakt8vyca9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24410" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24409">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7zVd04xMfGqtOXjU5-BlWQET_dpvvwxt14SK9dj92z5WvtLxoKq6nU9Ch90704rnJC1faPEYLIGP-VUXNFzvyDbvH3XaYur4EKieH361_c45RI6NV9vvAazIKfAgFFvGNkTGx-ha5m1TEddEZjgZxQ8tshBu5LzY6GYaPC95VTBowqH3lxN68N-WudHCCiD1OUTd7K5cBhAU1vZ7JcUYBFlCkecIPMy7j_BsJ3z_DpBU_xmQbdyxbiV9IUxmbFsuqW1prCiMgWQAxDVipAjdqEq_BEWotiZ_Z9Bfwmzg1jkBw34BmXYNDChN3JMDFl2ojnqzFNgWiDRXdziSyVCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24409" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24408">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWHLE_QORNpcP20mFp5RpHqlkpKVOzSANs-0XmDYPUaPp_r9EeCKmd-u5O61OtsR81UqhazMfOyawFd9biwmBV_yABUlpdk5NUopiM8bMn0rKAG5qsZtoQ_dwIBZPZASCJqXNWorfK4kvRT2GLl8N6W8qo8tZVK2pNGDN-3tcmipEbjGmw64hQcSqRve4A9payA5mw5f9gWmnwGehPpDLkOGPJTii6QmeX6mZUmXbDpFaWKVl7EWS7fLDoocP8O5n9LS97lQ6hRleCCvlVWHM0yGx24m2ekpeBdmrCGumbGCJp-p0VNULlHkM1T_u8tJg7ioADm5A_ZLGZzEV_QerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24408" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL5z_xPurmjvheWrG5h5_rVs59CSNSst8kLJOdQsxonAsjC0-J_2370A96i8M-_-Hlta4AtxkJRTjNQf7EoVBl5awclJ3g5Ojz0Q7gUw17rf-4TZpsON8Vw4q81XlVRdVVoZ__fen-o_Nd5SzOP7PwDqLUD1TvMZMckzrHuGSVPbHHHTEVpoYKTW9JLeOC0wJGLBvzu1WRUys8X3h7S_cVTu3jHQXM2I_oajEPrx_5RyIdUVmbmpKLA0bfzp301AekQqt30HMFdxRyizvXmhpO5rVJvKXoeUA5yyX7vUhWTY9sTP5cABmQ6LxmVA1TZWVy2sj1PQf9qs0ylvl3gE_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24407" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP_HYrSpqfue0o2M0ULP6jtJGDyN29eKbXrigJ16ask0btEJytmrnjU7ccyziURy9WGlZJrea6m4I3VZRvzTTU36ERkjf9H_jNgAr85bagWNT8iAPOf7powqd77Px20c2LqLVDgCzYnuchCBMN2o9-rK0G7UT-QqRy5OrNI06X1pow7dZPYC4ozBk0Zy4UPDO8A9S6vCohBSyaDfwkAJyVzSJTd-f2QumEC1Ef3Cd-j9Klv4xNX75qGNYoljUJBcHc_a4W9iEQwcu-Xppq0aZ1dPnKe6LTArxfO-lxshStH6iD8lPi2vP41MjqegDjspvLuION2BhScDPmX2SPfI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24406" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=qD62aGJhebpFRV6zf-38_7sOzW7A-Gg4ZV4qQIZzwE11voiRs7NLraMnTwMMGbLfAUSjb26DiwADnMVft0anbFenKnxZAfIvvP4VSAMthoFCcQyQSx3kLmdg1GQH39gZe-54LmW9yFjOAZ1_KuDE0onVsW7hrdhjxl8Vzr5CW5NAz6mTZcwQPz-xg8dbyN7CaaUG9y15rxBSssfOSweTDn5fCNw6zRH_-84SsYENVywtXpwrs_7xRAehnolCrn6NlAHKE7p8s2UlEQebKak7FzUtd7vdQfiAhdze7ZGHmbNoAMdGb3tjSDcmT3sXRgPOfqnGoMA8uU4K-fyJugj0uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=qD62aGJhebpFRV6zf-38_7sOzW7A-Gg4ZV4qQIZzwE11voiRs7NLraMnTwMMGbLfAUSjb26DiwADnMVft0anbFenKnxZAfIvvP4VSAMthoFCcQyQSx3kLmdg1GQH39gZe-54LmW9yFjOAZ1_KuDE0onVsW7hrdhjxl8Vzr5CW5NAz6mTZcwQPz-xg8dbyN7CaaUG9y15rxBSssfOSweTDn5fCNw6zRH_-84SsYENVywtXpwrs_7xRAehnolCrn6NlAHKE7p8s2UlEQebKak7FzUtd7vdQfiAhdze7ZGHmbNoAMdGb3tjSDcmT3sXRgPOfqnGoMA8uU4K-fyJugj0uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24405" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wn_tK0zxnvn4jfjXB0OWMB555yJWZZRkcP__fYuaTX2R1oI52atWzUoxLnj430axdFPedATZ6zQQ3Yh4PxWm1nn0kH5J1YemUQfnd3dCbGs1A5eUT0t2QyG6CcS1XRNgH6QM75Dgl_KXUJpaLAFFTrv_6eBO-3J6DA2BeoMkYLceTfuQF_1SbvrTUtS1mPMWmxCod5gauNcn4UQQCEb-825Q7CU7hSXgBwS4pJ4uRKmI_AbyLhUzKIfS6hmFzHGcu4UpYczadkV6KK-GJI_yg83y_IBXa74dzVTlSy0Zm4wOv9VyCfMlhse0Nl-DLYrf5JCiqu9sGYIhLC--YprpHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل اول چادرملو به پرسپولیس توسط سیروس صادقیان در دقیقه 57؛ بازی حالا یک بر یک شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24404" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=oWR8j-IZlyEeIJrTax_TU-KaQ384b7j10HyQVaklHzN-dB4fHs0Yy_aC9eNWbFSVmu8nHISMiA8wsfQin8HOApoVmC0pgwvwF0xP0X1w2wMTFN6VTgNknNaFWITxJKAMrV5DwM7UfA_WaETtNwADj_wPSquyB1TYCkoiN2JqG4IP6Pg-0hH1x8H4pqVeKY1y9MaFO3mEhEmOWBGyFcKuyarK4Hy_IhpeX73N1AhtobvXU_3DZ1RuwanSOgoVYwgo_Gkj2M44IeycuwbPCwwGmhZZrGdJo6pRyuhm-D55iQGHAZUbWSZNbpCFgVoMtAx5esKK0S9BOyfxgj8jr1ZMBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=oWR8j-IZlyEeIJrTax_TU-KaQ384b7j10HyQVaklHzN-dB4fHs0Yy_aC9eNWbFSVmu8nHISMiA8wsfQin8HOApoVmC0pgwvwF0xP0X1w2wMTFN6VTgNknNaFWITxJKAMrV5DwM7UfA_WaETtNwADj_wPSquyB1TYCkoiN2JqG4IP6Pg-0hH1x8H4pqVeKY1y9MaFO3mEhEmOWBGyFcKuyarK4Hy_IhpeX73N1AhtobvXU_3DZ1RuwanSOgoVYwgo_Gkj2M44IeycuwbPCwwGmhZZrGdJo6pRyuhm-D55iQGHAZUbWSZNbpCFgVoMtAx5esKK0S9BOyfxgj8jr1ZMBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌جهانی ۲۰۲۶ رسماًبه‌پُر‌تماشاگرترین‌دوره تاریخ جام جهانی تبدیل‌شد. مجموع‌تماشاگران بازی‌های جام جهانی‌فقط در ۱۵ روز از ۳.۶ میلیون نفر عبور کرد. این عدد رکورد قبلی مربوط به جام جهانی ۱۹۹۴ آمریکا حدود ۳.۵ میلیون نفر رو شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24403" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=kVlB--0SXS04ntyqS_PQHfJlfgkUwJzhShUhmdFY0pjPYXuqVFqdKQ3WXxiv65io9K-hMQl94kLduUx4g0A5zm_Al5Qoc7rHZuL4JGUBxdiCqlhvYTJTnggl8-TxC0yM6JOfc_CpBuJalFR8xG708RsnNjHndkSHIOswiM-Bha1vtK6mPoRUKq-NdBLsZ1GTR-Ey_4BqX4DMpzYa9bmwt5JDF4P7pKcjgRgtz0zUxZwi05IBagAZsN6kFAVlYqf4Ak-pa2ZGnpUDOIRN8yeTHYIvBKm0Y-6c4qpB3hNKSP4xWcWolJOa3AqLaC6ZxHi4Ygn47xJJeqmtG4WRBjKE5zqIGRbsoSkN6b48XHh-JyKY42iShJ7kz-vtAqkOBZW6pIZfad20iwV-5qGZjmln26c-j3hBXk9NtSm-2Y0q7n0wzTW6wvBh2IPvKzRrAmb1-yZa1Khnw2RtpBrwJky1JBKhXhqeCywqWBN9Br8auti0zNMJGf89DdvYcKXOApwAGtLzzWfDqFsl-RjINuu-l6TkPulJicKiy8SomESB7PB_1mrvPfs9r2a3pbRMYFbQ76P6fkcuIKH1CQYii4cNDFd_HxYduQXmBb5-Ojc5n_49c9nWPyaiKNqOnzryi630KvWVkE5qSwbKeTt-bLDarHuqzpsnPA8l9hSu1zFt5To" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=kVlB--0SXS04ntyqS_PQHfJlfgkUwJzhShUhmdFY0pjPYXuqVFqdKQ3WXxiv65io9K-hMQl94kLduUx4g0A5zm_Al5Qoc7rHZuL4JGUBxdiCqlhvYTJTnggl8-TxC0yM6JOfc_CpBuJalFR8xG708RsnNjHndkSHIOswiM-Bha1vtK6mPoRUKq-NdBLsZ1GTR-Ey_4BqX4DMpzYa9bmwt5JDF4P7pKcjgRgtz0zUxZwi05IBagAZsN6kFAVlYqf4Ak-pa2ZGnpUDOIRN8yeTHYIvBKm0Y-6c4qpB3hNKSP4xWcWolJOa3AqLaC6ZxHi4Ygn47xJJeqmtG4WRBjKE5zqIGRbsoSkN6b48XHh-JyKY42iShJ7kz-vtAqkOBZW6pIZfad20iwV-5qGZjmln26c-j3hBXk9NtSm-2Y0q7n0wzTW6wvBh2IPvKzRrAmb1-yZa1Khnw2RtpBrwJky1JBKhXhqeCywqWBN9Br8auti0zNMJGf89DdvYcKXOApwAGtLzzWfDqFsl-RjINuu-l6TkPulJicKiy8SomESB7PB_1mrvPfs9r2a3pbRMYFbQ76P6fkcuIKH1CQYii4cNDFd_HxYduQXmBb5-Ojc5n_49c9nWPyaiKNqOnzryi630KvWVkE5qSwbKeTt-bLDarHuqzpsnPA8l9hSu1zFt5To" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
#نقل‌وانتقالات|رسانه‌‌های عربستانی: عبدالرزاق حمدالله مهاجم کهنه‌کار مراکشی قصد داره در ژانویه قراردادش رو باالشباب‌فسخ‌کنه و از این تیم جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24402" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
