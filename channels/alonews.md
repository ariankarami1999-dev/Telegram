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
<img src="https://cdn4.telesco.pe/file/Q8DLS9piyvS5KkRcN0ZOwf2xfmJ7_WOrPC1rTkPuH6KNVj-ggMWwXuf2LEVVMKzJBhKDdNQer-4T--stbuTY7UkvSI5qCbxwkE-dUt5UpmQ28Tz58IbkuhiOf_Qb5fgdPVCDSgGqO15TlBCEz5jmNBLGCtadCkw2inUHc0IoFNrJTGkZW--bJCFJkHwQrF4dm7XBzD0J_ziE1kCY92XLHEb_jB3zObGkgRNXqSD3t8zLibLER-lGb174SItnOVq4vV8PiiEGIQMBj5Anos57bjYzpzXWMouGYfGMC9zBZXjpoGNjarDbHId3X1ZpncV7BTmBJ-Pq4tElkM31d1vYhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 970K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 00:53:57</div>
<hr>

<div class="tg-post" id="msg-128576">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edcf3e3aaf.mp4?token=iuU_lI94eOXeYtb-PMjp3UK02QtdxY4m9uO685LXRtezx-GLaJVtlm7ShTigBhvX9yu6Ai6uLSNnyBE4Jr51jYi8LyMNVKO22XC7kiNaYamOIYNEdJPc06FblfIymVBZErqcsG3xNCiJu4fKns8X5t1FU8OCuOOQSadjg4lZozAg6YU50HTd4SVkOGVd4JNaBGtCPp_U_Cf1PGBrmLgExIEFxlX_-Yv6TyV4xMEUIoGRQVFvKVtlTAJftQZfjm_pHWfpvHZdz-GNpBAr_9dAPVp36oVPPVvX3AK0mexoxgGDk7aNkv4Aim4eEfAWRAeuiQJhumU4PJMTnGWdktWOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edcf3e3aaf.mp4?token=iuU_lI94eOXeYtb-PMjp3UK02QtdxY4m9uO685LXRtezx-GLaJVtlm7ShTigBhvX9yu6Ai6uLSNnyBE4Jr51jYi8LyMNVKO22XC7kiNaYamOIYNEdJPc06FblfIymVBZErqcsG3xNCiJu4fKns8X5t1FU8OCuOOQSadjg4lZozAg6YU50HTd4SVkOGVd4JNaBGtCPp_U_Cf1PGBrmLgExIEFxlX_-Yv6TyV4xMEUIoGRQVFvKVtlTAJftQZfjm_pHWfpvHZdz-GNpBAr_9dAPVp36oVPPVvX3AK0mexoxgGDk7aNkv4Aim4eEfAWRAeuiQJhumU4PJMTnGWdktWOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : اگه دونالد ترامپ حتی به عنوان رهبر عالی ایران هم انتخاب می‌شد، دموکرات‌ها باز هم می‌گفتن آمریکا شکست خورده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/128576" target="_blank">📅 00:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128575">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
جی دی ونس : روز جمعه مراسم امضای رسمی انجام می‌شه و این موضوع عملاً شروع این مذاکرات رو کلید می‌زنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/128575" target="_blank">📅 00:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128574">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa0b57d8f.mp4?token=GHP3eOmHKXDFoaAZOttZ-Dn6BiiexfI_Dp7Ak_jUfMggtVHIRwKCYVq4WzlI1mdAsVeA8cs9kREovnrmMDS22VobacV6FaF9Y_TO1eKqF7Z6QY0LjXoxTe_D1lgUirCaZQq5QmEeSfJ_iAXgb5bgHGylRHKYMEKiD_novlFQV-vSO99bEY8LEkY8IswOHjxIWmIwxbxHEPXgtq5YR6CpYXepONBLIhLVfrdgYGBw2s_tZOr2Kf3qsWtW3jgT6Wq1HWXa7_Fnxbsl90rODuByBlZWrGjIOmT_kAJi23gKhCPli4vyQeImgGT0Wkcwnpc-BYGodbDH5tP7Ho5DBQOPpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa0b57d8f.mp4?token=GHP3eOmHKXDFoaAZOttZ-Dn6BiiexfI_Dp7Ak_jUfMggtVHIRwKCYVq4WzlI1mdAsVeA8cs9kREovnrmMDS22VobacV6FaF9Y_TO1eKqF7Z6QY0LjXoxTe_D1lgUirCaZQq5QmEeSfJ_iAXgb5bgHGylRHKYMEKiD_novlFQV-vSO99bEY8LEkY8IswOHjxIWmIwxbxHEPXgtq5YR6CpYXepONBLIhLVfrdgYGBw2s_tZOr2Kf3qsWtW3jgT6Wq1HWXa7_Fnxbsl90rODuByBlZWrGjIOmT_kAJi23gKhCPli4vyQeImgGT0Wkcwnpc-BYGodbDH5tP7Ho5DBQOPpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیندسی گراهام
: صادقانه بگویم، عربستان سعودی و اسرائیل خیلی به ترامپ بدهکارند.
اگر این دو کشور با هم صلح کنند و روابط اقتصادی و تجاری برقرار کنند، این اتفاق هم برای منطقه و هم برای جهان مفید خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/128574" target="_blank">📅 00:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128573">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سناتور لیندسی گراهام: مطمئنم که رئیس‌جمهور ترامپ توافق بدی را امضا نخواهد کرد
🔴
یادداشت تفاهم (MOU) آن‌طور که معاون رئیس‌جمهور و دولت توضیح داده‌اند، بسیار امیدوارکننده به نظر می‌رسد.
🔴
من ترجیح می‌دهم مسئله برنامه هسته‌ای ایران از راه دیپلماتیک حل شود. تردید…</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/alonews/128573" target="_blank">📅 00:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128572">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سناتور لیندسی گراهام:
مطمئنم که رئیس‌جمهور ترامپ توافق بدی را امضا نخواهد کرد
🔴
یادداشت تفاهم (MOU) آن‌طور که معاون رئیس‌جمهور و دولت توضیح داده‌اند، بسیار امیدوارکننده به نظر می‌رسد.
🔴
من ترجیح می‌دهم مسئله برنامه هسته‌ای ایران از راه دیپلماتیک حل شود. تردید من به خود ایران مربوط است.
🔴
یک توافق خوب چه شکلی دارد؟ هیچ غنی‌سازی‌ای نباید وجود داشته باشد.
🔴
باز شدن مسیرهای کشتیرانی و توقف درگیری‌ها به‌خودی‌خود یک موفقیت است، اما اینکه بتوانیم به مرحله دوم برسیم یا نه، نمی‌دانم.
🔴
در مورد برنامه هسته‌ای، بله، قانون می‌گوید که کنگره باید آن را تأیید کند. و ترامپ هم گفته که توافق را برای بررسی به کنگره خواهد فرستاد. پس بله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/128572" target="_blank">📅 00:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128571">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
معاون رئیس جمهور جی دی ونس:
پرزیدنت ترامپ هرگز نگفت که هدفش نصب رضا پهلوی برای تبدیل شدن به رهبر جدید ایران است.
🔴
آنچه گفته این است که اگر مردم ایران بخواهند قیام کنند ، عالی است. این کار اوناست این بین آنها و دولتشان است.
🔴
چیزی که ما می خواهیم توقف برنامه هسته ای آنهاست.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/128571" target="_blank">📅 00:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128570">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e8bb5c7ab.mp4?token=IlXl8BWBpcdHV1ljnRbYI8Bs8QEZB_BMjthlkA5OU9Xn6CEKdORtfgkJPZyaD3DUp_rCRi_IE74g-Izw-FtQYiSaz4P1q0wa20rC3Ud9tt0lSuQdHAarDWz8hgyUqGjJEqDkwUEfcJ-J610D8zX2PxZTuYM0m8Hb3-IQWOFIpITdR6vdOxC2aj1p6y4X747-PeR70Tae1GndBDwORsJlIJhs6j6SuNt-Uo2milb4uHd6MfL2Huvmga96wW8cqkvQbWOx7jovp1o07xBirVTJThW7rdUO9JEgZKcd1LUhOXyvrQWwe5Bdo3BEMtjSbn954AG-9wsp0OCOb9_sxmRCNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e8bb5c7ab.mp4?token=IlXl8BWBpcdHV1ljnRbYI8Bs8QEZB_BMjthlkA5OU9Xn6CEKdORtfgkJPZyaD3DUp_rCRi_IE74g-Izw-FtQYiSaz4P1q0wa20rC3Ud9tt0lSuQdHAarDWz8hgyUqGjJEqDkwUEfcJ-J610D8zX2PxZTuYM0m8Hb3-IQWOFIpITdR6vdOxC2aj1p6y4X747-PeR70Tae1GndBDwORsJlIJhs6j6SuNt-Uo2milb4uHd6MfL2Huvmga96wW8cqkvQbWOx7jovp1o07xBirVTJThW7rdUO9JEgZKcd1LUhOXyvrQWwe5Bdo3BEMtjSbn954AG-9wsp0OCOb9_sxmRCNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران:
در حال حاضر افرادی هستند که می‌گویند باید نیروهای زمینی به ایران اعزام کنیم.
آن‌ها می‌خواهند دونالد ترامپ صدها هزار نیروی نظامی را وارد ایران کند.
ما به افرادی نیاز داریم که از داخل همین جریان، در برابر این دیدگاه مقاومت کنند و با آن مخالفت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/128570" target="_blank">📅 00:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128569">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb6fc009c.mp4?token=KCT__1fcHJWrw8_6yfsaLE8U2CNIsz08KZ4scLh2uCJ-9Tl6efq4cdkaavjHKgCgeaPU_6KVB8zzcrFtL6Ua9Dyh4PTlhLRmtPclC2A42-28Y9rmqsCAmvbO3to3dBpDs2VChTJ42V5t7pzf0_QnuoQBFlhxx6LJgL7KkEDI-7fZLBp0lMVJjsNuJvtxNnTpd0cSxPYmddKoUUY19ypTuEVPvTh9WEYRCSkaerwKR9bP5AP0dB08vPDeZoUloZf9X_oLLJ00EVwGv9MHKJU7XXAuH6nOXQZ2h3QeShYg3joTMgMwSnoYHMSc3NbBVCyTXHSFcSdndtzL4P67IBhYD4zjyxe1BKYTAHFspILNHF60bZAQz8qz5ff0gG2onTeNBQ77TNZND1lybHNdr00JSA34WWqmkNQ6Q7mOsFuaZQAyAfjTlboljsV6KjbYaQpMq-ZY3PMescYWyIpv90-ZdJQCzTt0aWPbNv8_uzdWTOgK5bQOQDQAfvTP_MTEuumj9EcrYkmFO46tNHNElfXTbB9fueWctewlKiuW3hrawdxclebhelqlBSAAN5xAeBnQtrlUCV4b3ZIvXNr7kAnmg7KsIBgmqHXlKHf_uiOOyz95kRn6IHucWK_6cqNXSk8F01OCMWcFbK1RhzzUfee8_FYuupjoScDy6_TKZ-o99KU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb6fc009c.mp4?token=KCT__1fcHJWrw8_6yfsaLE8U2CNIsz08KZ4scLh2uCJ-9Tl6efq4cdkaavjHKgCgeaPU_6KVB8zzcrFtL6Ua9Dyh4PTlhLRmtPclC2A42-28Y9rmqsCAmvbO3to3dBpDs2VChTJ42V5t7pzf0_QnuoQBFlhxx6LJgL7KkEDI-7fZLBp0lMVJjsNuJvtxNnTpd0cSxPYmddKoUUY19ypTuEVPvTh9WEYRCSkaerwKR9bP5AP0dB08vPDeZoUloZf9X_oLLJ00EVwGv9MHKJU7XXAuH6nOXQZ2h3QeShYg3joTMgMwSnoYHMSc3NbBVCyTXHSFcSdndtzL4P67IBhYD4zjyxe1BKYTAHFspILNHF60bZAQz8qz5ff0gG2onTeNBQ77TNZND1lybHNdr00JSA34WWqmkNQ6Q7mOsFuaZQAyAfjTlboljsV6KjbYaQpMq-ZY3PMescYWyIpv90-ZdJQCzTt0aWPbNv8_uzdWTOgK5bQOQDQAfvTP_MTEuumj9EcrYkmFO46tNHNElfXTbB9fueWctewlKiuW3hrawdxclebhelqlBSAAN5xAeBnQtrlUCV4b3ZIvXNr7kAnmg7KsIBgmqHXlKHf_uiOOyz95kRn6IHucWK_6cqNXSk8F01OCMWcFbK1RhzzUfee8_FYuupjoScDy6_TKZ-o99KU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس:
اگر ایران حزب‌الله را تامین مالی می‌کند، ما اجازه نخواهیم داد که مجموعه‌ای از دارایی‌های مصادره‌‌شده به ایرانی‌ها منتقل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/128569" target="_blank">📅 00:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128568">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e8bb5c7ab.mp4?token=JIjKiLDK0rajeuKH8SNrI91dJrRC05vHZCt7N8XKelTN6dqtZZfnLThPsvUByDFdbRFGQt-K3mveTvLqeJFjtQd3xpRI3pqTeWFwUDSc-iPeSAYgkrOzbAALaOmFdzVgD83kjW9J4yK-o3dFeQN9ooJtThdBKMfAH5tS0hCU7LrqG2xejnDduTF4QLA3zkOE8YBngl0upz5t1QuaX3u05_g83ufE08QtOH1j4g--dTPMkP_-p6Vi3fjvp0erssINFzm3iQoCFMZk4Njoiygw88hpFDLOyjLqStLYgbzeEXmqagrhwvorPbVAeoV82SUVNBZK8wSOLUQ6rx5g0fHprg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e8bb5c7ab.mp4?token=JIjKiLDK0rajeuKH8SNrI91dJrRC05vHZCt7N8XKelTN6dqtZZfnLThPsvUByDFdbRFGQt-K3mveTvLqeJFjtQd3xpRI3pqTeWFwUDSc-iPeSAYgkrOzbAALaOmFdzVgD83kjW9J4yK-o3dFeQN9ooJtThdBKMfAH5tS0hCU7LrqG2xejnDduTF4QLA3zkOE8YBngl0upz5t1QuaX3u05_g83ufE08QtOH1j4g--dTPMkP_-p6Vi3fjvp0erssINFzm3iQoCFMZk4Njoiygw88hpFDLOyjLqStLYgbzeEXmqagrhwvorPbVAeoV82SUVNBZK8wSOLUQ6rx5g0fHprg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران:
در حال حاضر افرادی هستند که می‌گویند باید نیروهای زمینی به ایران اعزام کنیم.
آن‌ها می‌خواهند دونالد ترامپ صدها هزار نیروی نظامی را وارد ایران کند.
ما به افرادی نیاز داریم که از داخل همین جریان، در برابر این دیدگاه مقاومت کنند و با آن مخالفت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/128568" target="_blank">📅 00:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128567">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965eebaf12.mp4?token=AwLJzwnjCVR4QuxFs-PGJCuLaP8l_oEdBnprJEd22jO7_CkKxxOKtnLYX7XL_RzSOTPIyLTJh2Qauy_kD3vLJTtty7TOtvT9jhQoBoppY3aYYvnXMg634OAY3c9tlMcr5buRGml8Ko08grbZ-IW-IzP_cYtUsNNXhcHCt6oihmkGEw4RHNZfCGtPUSLaJGEXZmjDJPra9ahmxaBA16YZajGwKTjmBZMOX5jpyc3ZcQCkdnnoUY8mdDbR1xt6cOmAEXCEM0waqLGWI5Qe7eZLoXQOasU_GDZSETqO1sHWdhMRRKR7tsAXa_6yaJfF3vj2xj6KLESCF29t24Ymd7OwzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965eebaf12.mp4?token=AwLJzwnjCVR4QuxFs-PGJCuLaP8l_oEdBnprJEd22jO7_CkKxxOKtnLYX7XL_RzSOTPIyLTJh2Qauy_kD3vLJTtty7TOtvT9jhQoBoppY3aYYvnXMg634OAY3c9tlMcr5buRGml8Ko08grbZ-IW-IzP_cYtUsNNXhcHCt6oihmkGEw4RHNZfCGtPUSLaJGEXZmjDJPra9ahmxaBA16YZajGwKTjmBZMOX5jpyc3ZcQCkdnnoUY8mdDbR1xt6cOmAEXCEM0waqLGWI5Qe7eZLoXQOasU_GDZSETqO1sHWdhMRRKR7tsAXa_6yaJfF3vj2xj6KLESCF29t24Ymd7OwzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمار فاجعه بار ستاد مبارزه با مواد مخدر از مبتلایان به HIV در کشور
🔴
از هر ۸ نفر معتاد ۱ نفرشان مبتلا به ویروس اچ‌آی‌وی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/128567" target="_blank">📅 00:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128566">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سوال
: آیا ترامپ در حال فروپاشی است؟ او تازه ۸۰ ساله شده است.
🔴
هیلاری کلینتون: فکر می‌کنم او قطعاً همان چیزی نیست که قبلاً بود.
🔴
دونالد ترامپ این روزها مدام در حال خوابیدن است. او این روزها خواب کافی نمی‌بیند.
🔴
جو بایدنِ بیچاره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/128566" target="_blank">📅 23:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128565">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
هیلاری کلینتون: وقتی ترامپ جنگ علیه ایران را آغاز کرد و سپس از کاخ سفید شنیدید که «هیچ‌کس به من درباره تنگه هرمز نگفت» و پرسیدند «تنگه هرمز کجاست؟»، این چیزی است که نمی‌توان آن را ساختگی دانست. انگار فیلمی است که به دلیل عجیب و غریب بودن از آن خارج می‌شوید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/128565" target="_blank">📅 23:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128564">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=oY61xMBzcwagZ2I7RYz0FhaR4N-4VTVRys8vUKX2hQlOfpPCHhpy3bHnsnw8om1sz_KWii8ZHpQVu-i0xg5JNIOVPTGe3hqfbkvcAR5PZMJA1pWDKBpEcXO_NbwSd2uRu1smtNKv8xtx8mFsh5Ia5fS2SquREiRdplbFctRsXVvFssVJwVZyB_AfDkL2T4QeBpxfD79XfTnn5DWCrD3li_LdYksbBE57aPiVTaw93-g00rKEiOxJw6yeuHIpW_2MkrxeZXNnUDnMLfDOkvi-iz1OBGbMUuvjEb8IfrIm1L1PEKWSrbjZuT2LmqdyYYxYQKPhRYhj5yIAKffZLc_Pew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=oY61xMBzcwagZ2I7RYz0FhaR4N-4VTVRys8vUKX2hQlOfpPCHhpy3bHnsnw8om1sz_KWii8ZHpQVu-i0xg5JNIOVPTGe3hqfbkvcAR5PZMJA1pWDKBpEcXO_NbwSd2uRu1smtNKv8xtx8mFsh5Ia5fS2SquREiRdplbFctRsXVvFssVJwVZyB_AfDkL2T4QeBpxfD79XfTnn5DWCrD3li_LdYksbBE57aPiVTaw93-g00rKEiOxJw6yeuHIpW_2MkrxeZXNnUDnMLfDOkvi-iz1OBGbMUuvjEb8IfrIm1L1PEKWSrbjZuT2LmqdyYYxYQKPhRYhj5yIAKffZLc_Pew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرف حق پزشکیان:
مشکلات خودتون رو خودتون حل کنید، من سیاستمدار نیستم من دکترم، برا سلامت مردم اومدم رئیس‌جمهور شدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/128564" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128563">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
پزشکیان: حوادث دی‌ماه سال گذشته قابل پیشگیری بود
🔴
بخش قابل توجهی از کسانی که در این رخداد‌ها حضور داشتند، با آسیب‌هایی همچون بیکاری، محرومیت درگیر بودند،
🔴
اگر می‌توانستیم زمینه‌های شکل‌گیری این آسیب‌ها را شناسایی و مدیریت کنیم، بسیاری از این مسائل بروز نمی‌یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128563" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128562">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
کانال ۱۵ عبری: سند تفاهماتی که میان امریکا و ایران در حال شکل‌گیری است، مجموعه‌ای از امتیازات بسیار گسترده واشنگتن را در ازای پایان فوری جنگ در تمامی جبهه‌ها، از جمله لبنان، نشان می‌دهد
🔴
واشنگتن متعهد می‌شود محاصره دریایی را لغو کند، تمامی تحریم‌ها را بردارد، از منطقه خارج شود و دست‌کم ۳۰۰ میلیارد دلار برای بازسازی ایران اختصاص دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128562" target="_blank">📅 23:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128561">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
به علت پخش و انتشار سوالات امتحانی تو کانال های تلگرامی هندی، این پیام‌رسان تو هند تا بعد امتحانات فیلتر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/128561" target="_blank">📅 23:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128560">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joBb7tLs1jwfQsvuAIcQME-6gXVsKyvma7VDh5sEkEQ7oEHfVeHU3ckceDaNdKbJslofv7gl15WyrUkC83lnw7Naxx28jNzVxA2JPSkVKJLaEfULlkWp7w1wM4ahgQ6-qNyczX4PzRLtN-3dOsx_krbT_gzMqW1kQrVAQstpAJLflQ7onHFJcnTm42dF4qoLtpt4xZmBPwuYDQSgCdWIFY77aID-SnMy8m71bhs7KgVTkDsmDxTT0pGcxc_U4MRQSR8E-koXoFrCDHhNyo9n-WQWIryC__3FEnMPwRR-VJSnXPr7QU0l-Ne42PSchQJgBzRk7d6CRoHbIxgGWjBr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی: خداروشکر یک امتیاز هم نتیجه خوبی بود، با برد مصر و حداقل تساوی با بلژیک میتونیم اول یا دوم‌گروه بشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/128560" target="_blank">📅 23:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128559">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb9e0a16c.mp4?token=iZtb9ff0bH-YATvVuZz80eVT1l7LjbtNoyoEB_kZ6qb62Y8dXPc3vdIvlqJcHxf9Rva1liLmUSyqbk_l84nYs2Uzw8mCLhy_F_wOs4K6nNYXRnvISAOCUfvoZ7H4MDZwIuUyNw_VXD4Hm6czns1owPm7eYoQpevHuQ4s5l9te8__N8d8mQhoE1XnL32pOfTR3s4O24eJX64BhR9s1gGXVVEj28hjSX16SQ4_u8bGYhU7LQQnFa6wllLnFWdVUiSFQC2i5foeE2_mspM80S-umcbt5YUFYQe2_0LJx7tTGHkS3r4Yvy1lEITOxLifLG2_UQfefb-kFX3pHWVT61FlpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb9e0a16c.mp4?token=iZtb9ff0bH-YATvVuZz80eVT1l7LjbtNoyoEB_kZ6qb62Y8dXPc3vdIvlqJcHxf9Rva1liLmUSyqbk_l84nYs2Uzw8mCLhy_F_wOs4K6nNYXRnvISAOCUfvoZ7H4MDZwIuUyNw_VXD4Hm6czns1owPm7eYoQpevHuQ4s5l9te8__N8d8mQhoE1XnL32pOfTR3s4O24eJX64BhR9s1gGXVVEj28hjSX16SQ4_u8bGYhU7LQQnFa6wllLnFWdVUiSFQC2i5foeE2_mspM80S-umcbt5YUFYQe2_0LJx7tTGHkS3r4Yvy1lEITOxLifLG2_UQfefb-kFX3pHWVT61FlpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون سابق رئیس‌جمهور ترامپ، مایک پنس، درباره تفاهم‌نامه آمریکا و ایران:
من نگرانی‌های واقعی دارم، حداقل درباره آنچه در بحث‌های عمومی مطرح می‌شود.
🔴
در طول سال‌ها زمان زیادی را در اتاق وضعیت گذرانده‌ام. تفاوت بین آنچه واقعاً حل شده و آنچه در رسانه‌ها مطرح می‌شود را می‌دانم، بنابراین نمی‌خواهم پیش‌داوری کنم... اما من به ایرانی‌ها اعتماد ندارم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/128559" target="_blank">📅 23:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128558">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
عراقچی نمایندگان مجلس رو در جریان طرح‌ها و پیشنهادات مختلف مطرح‌ شده در روند مذاکرات قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/128558" target="_blank">📅 23:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128556">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbiKoudNSp-I9anmEb3PF2XHv1to-5-NV9rFQ2w460eiS11HDVjCzIR6yqb52eycTzZf7qoxgB8LORXrEC0K7LEholx3nTUJ2HBOfFGqxVIUXyfOaEDY8oT1oFbN5VD6ZwXwOKvWwcvSJ_nDFL5hFDjrHgbBLzhlmHIdXTSHBGFpyzQYxacng60uFHSfa0HOqRr_tDpGxsUD3xC126xIzFt9oqFlT1zTCET6hSrSlLc9100jlTj41QCuO-t_znNoqtK6IkATmQHLgbkH5BdjSi0xtf_zsRfpOFKjJuZe7l1bkmLtps6Vc6S2QuY7eMLpdJUgJGGYaYqWkZhUtsd1yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbKRZSRmwYpTiEyv-Nz8ipLCrngB8pOTg0iznHbUaEQzw-hRvt5tTSPcnl79uxC5pzOb2e_mcOok6KFHLhgQABNzt2549Q5A5iI9SU-e1lxzvRQQj9BOydOjawi_9KVKYpaBF-Ou8ynU2zy7qfWmyp_MziSpIIkzlVwW1_WMhMLp5g0pXWuiq2m_NRj_iKoTA6SdBOUX_nbjrnsFletzLrLVfVgToWqjxE8Y9eBo3MveRN49EZO--uPJE-fR6_CJ0JmndoaI_klDV1IsoarOGebdd3NQ3euUiWrOJu8Ls2l77tugrHcCvItfMmiuiSga_JHICH01FIe0Z4fSF8_OPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دست ترامپ امروز در اجلاس هفت‌گانه در اویان-له-بن، فرانسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/128556" target="_blank">📅 23:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128555">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93292ab714.mp4?token=RSEVsNiDkviAZRwPJIjZBAjKYsJUmcGvfAYkYcEuAV_cGNTWaf6aYGVfWb23JPjr51GYXmjd-tSQmZw5-hQxvvypgOh7LRL8pKBHMa-sudsBGKOHYcffPPS1uEhkwQYfT6ZTjUGg2iZroz4NKHIZAK7-OMGPCMiJvBB8_bP2jUX2cPRyz3QEMsON8G7PbwIwFz8RpH26Rf2aWziK56mkjLsAfnZFa-4aYqwPU__IT7ZVmBz6ve8_LEGmfRHRlKblVXvxGIV41KPmRCn-I6PtQeNBYAtCxYXpCNwSxxs2FgJuzLBwfTtePtTJvaoQJqQ3LeSrT2Bnqu7Qb8ihqEIPCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93292ab714.mp4?token=RSEVsNiDkviAZRwPJIjZBAjKYsJUmcGvfAYkYcEuAV_cGNTWaf6aYGVfWb23JPjr51GYXmjd-tSQmZw5-hQxvvypgOh7LRL8pKBHMa-sudsBGKOHYcffPPS1uEhkwQYfT6ZTjUGg2iZroz4NKHIZAK7-OMGPCMiJvBB8_bP2jUX2cPRyz3QEMsON8G7PbwIwFz8RpH26Rf2aWziK56mkjLsAfnZFa-4aYqwPU__IT7ZVmBz6ve8_LEGmfRHRlKblVXvxGIV41KPmRCn-I6PtQeNBYAtCxYXpCNwSxxs2FgJuzLBwfTtePtTJvaoQJqQ3LeSrT2Bnqu7Qb8ihqEIPCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
: آیا توسط دولت درباره آنچه در توافق با ایران وجود دارد، به شما اطلاع‌رسانی شده است؟
🔴
جان تون، رهبر اکثریت سنا:
من قطعاً هنوز این کار را انجام نداده‌ام، اگرچه ما درخواست آن را داریم و فرض می‌کنم که در مقطعی از دولت در این مورد شنیده‌ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/128555" target="_blank">📅 23:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128554">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رضا پهلوی: بمباران ایران باید ادامه پیدا کنه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128554" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128553">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6Z9wrTBW-q3JoiLXCLwv31AVL6-iMKvqt0JT9moVixHyVW5s5YMDIFczD-vbCpFb8ZrdmgqpXs-W1A1qPUboxr8Sn9p4uyeaBePaz1sgdzxo54i2oDg5e6NXFpDSagsicESlkwzy7CJlPw15rAgC-dL4hzEYgJzG2hwwSLLnjbVStC1mNnBWgsa247pJ5AnrHMIYrXU-iSIzLMP--aCvXDjhCx62n0vjQibOj6i-wzcXqQTxLFHnqHaMFrO7JA-NiFUazJjnwneN35vYVwINejMvSRzS_3iNhwX2-_osy7IViwnRZKz-NFhcrwHVslwTUfisW0NRqm6r2g8f4XmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی: بمباران ایران باید ادامه پیدا کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/128553" target="_blank">📅 22:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128552">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / گزارش ها از انفجار در اربیل عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/128552" target="_blank">📅 22:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128551">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
به گزارش ان‌بی‌سی نیوز، کارشناسان ارشد صنعت نفت هشدار می‌دهند که علیرغم فضای مثبت ناشی از توافق میان ایالات متحده و ایران برای پایان دادن به جنگ چندماهه در خاورمیانه، بازگشت بازارهای نفت به حالت عادی و از سرگیری تردد در تنگه هرمز فرآیندی زمان‌بر است و احتمالاً چندین هفته به طول خواهد انجامید.
✅
@AloNews
خیر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/128551" target="_blank">📅 22:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128550">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVXEeY50ugz3CajRi5DkNzO8GaylL7-dzoYPaHktNp2JltZ5rp-_1ihf10Xjl-6-Oc6HX1W_phwtsBKh3VQ9SwlhPNR2QkcsPQNgr8Sd1rin9jYD6FMSYoSEv999zfD8If-UVY5yyMcLSk5v6gSBDe1syNd7xR9FdoEr9Gy4xjJHl0SfPRkvYVqsrVFcfoemRSjzzON8RaeAaQcTg8Ma0eJk4JPUstL2bHAbPpeZHfF-lNE3tDaeJQA1iTTr8c7_k8Md5OKV2Qv0yFges5TimfUd4pg3DcfY_nYOu440ne81gA9dxvmIqQh4yPg6eGyce25ofBUUE-yFOechEUuV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: تفاهم‌نامه ایران شامل اعطای صندوق  سرمایه‌گذاری ۳۰۰ میلیارد دلاری است
🔴
تفاهم‌نامه بین ایران و آمریکا شامل برنامه‌‌ای برای  تشکیل صندوق سرمایه‌گذاری ۳۰۰ میلیارد دلاری به منظور حمایت از اقتصاد ایران است.
🔴
این صندوق تنها پس از امضای توافق نهایی راه‌اندازی خواهد شد و شرکت‌هایی از آمریکا، منطقه خلیج فارس، آسیا، آمریکای جنوبی و آفریقا متعهد به سرمایه گذاری در آن شده‌اند.
🔴
این سرمایه گذاری در حوزه‌های انرژی، لجستیک، تولید و حمل و نقل  خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128550" target="_blank">📅 22:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128549">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران بخش قابل‌توجهی از توان موشکی، پهپادی و دریایی خود را حفظ کرده و همچنان از ظرفیت لازم برای تهدید تنگه هرمز در آینده برخوردار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128549" target="_blank">📅 22:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128548">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIHqzhbV7Rh0uGUfXFibb77vIPA1ZbPP-MPAZqQeljvDNOfx0uNHenPYuQJHJlEHt3AE5v5q1g4JZLbuDb4MgSh0ETd0XOOPeVOW_S46CZETvyGSD0S2xcYljVHCEmFQ6k_DAtbBENgrqnpe6GJF2lX8LUT-95_FuZtdL817Su9CZZBvP5aizhrUSt2jLLZmgH-lcwkReMUFTBsU2wTQYfCje7jb0DITrwMMV8C3gDwNjJuFrUJNdb7kB30PHIC7G1jmRctToCsEyc85nXO__TYNXhD8DtrUorxu0EnHh3iyzQ6HSEnCdNyf7LWPHt0bqfRW2HaxY0FSg8idmABqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزب لیکود به رهبری بنیامین نتانیاهو، نخست‌وزیر اسرائیل، فعلاً کمپینی که بر رابطه نزدیک بیبی با رئیس‌جمهور ترامپ تأکید داشت را کنار گذاشته است، زیرا ارزیابی‌های داخلی نشان داده‌اند که ترامپ در حال حاضر نظر عمومی رأی‌دهندگان اسرائیلی را بهبود نمی‌بخشد، طبق گزارش i24NEWS
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128548" target="_blank">📅 22:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128547">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
هشدار قرارگاه خاتم‌الانبیا : ارتش اسرائیل تو دو روز گذشته ۸۴ بار آتش‌بس جنوب لُبنان رو نقض کرده
🔴
با وجود اعلام پایان جنگ، هنوز هم به حملاتش ادامه میده
🔴
همچنین هشدار میدیم، اگه این حملات متوقف نشه، نیروهای مسلح ایران پاسخ سختی خواهند داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128547" target="_blank">📅 22:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128546">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uu9I32Z-OtGJBD3y_-jelF3YWIQqqpRRPc8sAnSztmmNzNL7hQLMxmxEwaXDTrqgw-ycGZuj85T-EySx24PFQIdTU904Dklz2m1Gz1l-I63kq8nMy2EeJ6tbXYrGQtmHS45y5uEI_PXDqSFTvkgSQqrM0su680e0TexHGcxvdZ3E634u9kq_rmqXuPc4OKyCyynjBSZesNBdXIlIORAEsWvfVsut6vZk2xPM9STUpsv45T_qO42eKYnfPpb_qt-eylO80Q-hDSfsH57yvNpUXRBgSmS1viktGmbieIdUg_0wlDf3V-cbmZlszxWwZzh87YsIMsuwLjKDa1cESzeE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز : بیش از نصف غرامت ۳۰۰ میلیارد دلاری ایران از قبل تأمین شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128546" target="_blank">📅 22:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128545">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
قطر: هیچ بودجه‌ای برای چارچوب بازسازی ایران اختصاص داده نشده است
🔴
الجزیره نوشت: ماجد الانصاری، سخنگوی وزارت امور خارجه می‌گوید: هیچ بودجه‌ای از قطر تحت چارچوب گزارش‌شده ۳۰۰ میلیارد دلار اختصاص‌یافته برای بازسازی ایران پس از جنگ پرداخت نشده است.
🔴
او در پاسخ به سوالی در مورد این رقم به خبرنگاری گفت: «ما نمی‌توانیم در مورد ۳۰۰ میلیارد دلار اختصاص‌یافته برای بازسازی اظهار نظر کنیم.»
🔴
با انتشار اخباری مبنی بر راه‌اندازی یک صندوق بازسازی به ارزش سیصد میلیارد دلار برای ایران، رئیس‌جمهور آمریکا روز دوشنبه گزارش‌های رسانه‌ها در این مورد را رد کرد و آن را «اخبار جعلی» خواند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128545" target="_blank">📅 21:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128544">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کان نیوز: مقامات ارشد امنیتی امارات متحده عربی در آغاز جنگ علیه رژیم ایران به اسرائیل سفر سری برای بحث‌های امنیتی در سطح بالا انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128544" target="_blank">📅 21:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128543">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری/باراک راوید، جزئیات تفاهم‌نامه ایالات متحده و ایران را به دست آورده است، او می‌گوید ۱۲ نکته به شرح زیر است:
🔴
ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان. ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند.
🔴
ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
🔴
ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
🔴
ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
🔴
ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
🔴
ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
🔴
ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
🔴
اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد.
🔴
هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود. ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد.
🔴
مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/128543" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128542">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
فارس: برخی منابع نزدیک به تیم مذاکره‌کننده ایران، ادعاهای شبکه خبری العربیه در خصوص متن یادداشت تفاهم ایران و آمریکا را تکذیب کردند
🔴
العربیه پیش از این نیز گزارش‌های نادرستی در خصوص مسائل مرتبط با ایران منتشر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128542" target="_blank">📅 21:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128541">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سازمان اطلاعات داخلی فرانسه، اداره کل امنیت داخلی، استفاده از پالانتیر را متوقف می‌کند، وزیر دفاع سباستین لکورنوی به نگرانی‌ها درباره وابستگی استراتژیک به آمریکا اشاره کرده است، گزارش خبرگزاری AFP
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128541" target="_blank">📅 21:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128540">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فرهیختگان: بیش از ۱۰ هزار پزشک زیر میزی می‌گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128540" target="_blank">📅 21:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128539">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یک مقام آمریکایی و یک دیپلمات منطقه به تایمز اسرائیل گفتند که آمریکا خود را برای ارائه تسهیلات به ایران در قالب معافیتی که به ایران اجازه صادرات نفت می‌دهد، آماده می‌کند.
🔴
اعطای معافیت تحریمی پیش‌دستانه آمریکا در مورد فروش نفت ایران نشان می‌دهد که در واقع برای برداشتن برخی محدودیت‌های اقتصادی، نیازی به امتیازات بیشتر از سوی ایران نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128539" target="_blank">📅 21:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128538">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عبدالناصر همتی رئیس‌کل بانک مرکزی به خبرگزاری تسنیم: پس از امضا و آغاز اجرای یادداشت تفاهم، اقدامات فنی و بانکی لازم برای راستی‌آزمایی آزادسازی دارایی‌ها و امکان استفاده عملی از آنها انجام خواهد شد تا اطمینان کامل نسبت به دسترسی مؤثر به منابع فراهم شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/128538" target="_blank">📅 21:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128537">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
صدراعظم آلمان مرتس در مورد جمهوری اسلامی ایران: ما همیشه گفته‌ایم که آماده مشارکت هستیم. ما قبلاً اولین کشتی‌های مین‌روب و کشتی‌ها را به منطقه فرستاده‌ایم.
🔴
ما آماده هستیم، اما هنوز تصمیمی نگرفته‌ایم — نه در دولت فدرال و نه در پارلمان.
🔴
ما باید، البته، همچنین پایه حقوقی را روشن کنیم. این سوالی است که هنوز به طور قاطع حل نکرده‌ایم.
🔴
اما این واقعیت که ما اساساً آماده مشارکت در حفظ این صلح هستیم، برای هفته‌ها موضع مشترک دولت فدرال بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128537" target="_blank">📅 20:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128536">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
صدراعظم آلمان مرتس: همه چیزهایی که از ایران می‌شنویم نشان می‌دهد که ایران نیز این موضوع را می‌پذیرد، زیرا با توجه به برتری نظامی آمریکا، به سادگی هیچ انتخاب دیگری ندارد.
🔴
من دیروز عصر به رئیس‌جمهور ترامپ گفتم: می‌توانید از این مثال ببینید که قدرت نظامی شفاف نیز قادر به ایجاد راه‌حل‌های دیپلماتیک است
🔴
و همین موضوع در مورد اوکراین نیز صدق می‌کند، آنگاه ممکن است به صلح در دو مکان حیاتی جهان نزدیک‌تر شویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128536" target="_blank">📅 20:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128535">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کانال ۱۴ عبری : نشست اضطراری تو دفتر نتانیاهو با موضوع ایران و لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128535" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128534">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سی‌جی‌تی‌ان: یوری اوشاکوف، دستیار ولادیمیر پوتین، رئیس جمهور روسیه اعلام کرد که استیو ویتکاف و جرد کوشنر، نمایندگان آمریکا پس از امضای یادداشت تفاهم با ایران، احتمالا برای مذاکرات درباره اوکراین به مسکو سفر خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128534" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128533">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
اختلال اینترنت ‌بانک پاسارگاد برطرف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128533" target="_blank">📅 20:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128532">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e3d11339e.mp4?token=RPIVihF8idy23xII0h4RkXAr7brUyMZFBIpORvFB7QEYr42nWQCpSqEKDlfFpiGf9NXO-YzmxKlR3W42iEdGKQp2P4K6OsmpSFigcl17qQX3yUDIxOonS3STn2o_NhUjCntqBIeBvW9D4_iPzY8aH3P4cjKEh8qq6z7V62m1VqJiaDmt0UVQuC-S8Sb8ZdayGsFmSmEvrf69z5PiXUgj58zMRF7Ekxg7A1UXZgds34UV4tjaVMFTiiIqQdvhD9UnfAMXhsJXF9zCvYrPgpRBNd03h4nGhumGsAVUD3ZwIqQ4AYa1HMmi7eONnndzhikFZLWgMSQXqhapxJXMBjAPwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e3d11339e.mp4?token=RPIVihF8idy23xII0h4RkXAr7brUyMZFBIpORvFB7QEYr42nWQCpSqEKDlfFpiGf9NXO-YzmxKlR3W42iEdGKQp2P4K6OsmpSFigcl17qQX3yUDIxOonS3STn2o_NhUjCntqBIeBvW9D4_iPzY8aH3P4cjKEh8qq6z7V62m1VqJiaDmt0UVQuC-S8Sb8ZdayGsFmSmEvrf69z5PiXUgj58zMRF7Ekxg7A1UXZgds34UV4tjaVMFTiiIqQdvhD9UnfAMXhsJXF9zCvYrPgpRBNd03h4nGhumGsAVUD3ZwIqQ4AYa1HMmi7eONnndzhikFZLWgMSQXqhapxJXMBjAPwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدراعظم آلمان، مرتس، در مورد توافق جمهوری اسلامی ایران و ایالات متحده:
من به رئیس‌جمهور ترامپ وعده دادم که می‌خواهیم سهم خود را برای موفقیت صلح انجام دهیم.
🔴
این شامل کمک با ابزارهای نظامی برای امکان‌پذیر کردن حمل‌ونقل آزاد از طریق تنگه هرمز به صورت دائمی نیز می‌شود، به محض برآورده شدن شرایط لازم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128532" target="_blank">📅 20:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128531">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2668d0c29b.mp4?token=SKe8IdpkLqOmB3HRzlG59yfpgwY165nsWb9S2rf_BVLTlDcRakpujbo962B-_nWM3mVXj7oQckdALF87uWfkLTQ7bhV9KF4zyinpagpaLIIL0k4OLYqRKCDenfdoZeQAZ88f2du9155nBnrNp3X5-EDiRC7flFsmPwbx32gKnVFNOExds7c_lNcMcTLqsjMk6LGhGhFM1o7ku5JDRQItziaVqrd1ozHSNz3QtsAsdKd5Hkq8WaFqES7uWJYA6_fZVVU0XOPiyVpB1tuAG6ElALbGxqO9pOZCneb-1ipw2_0kDIA0zpOH-3EvbqBrr92_Y-q6cm-VEZ9l7X8vcgn_wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2668d0c29b.mp4?token=SKe8IdpkLqOmB3HRzlG59yfpgwY165nsWb9S2rf_BVLTlDcRakpujbo962B-_nWM3mVXj7oQckdALF87uWfkLTQ7bhV9KF4zyinpagpaLIIL0k4OLYqRKCDenfdoZeQAZ88f2du9155nBnrNp3X5-EDiRC7flFsmPwbx32gKnVFNOExds7c_lNcMcTLqsjMk6LGhGhFM1o7ku5JDRQItziaVqrd1ozHSNz3QtsAsdKd5Hkq8WaFqES7uWJYA6_fZVVU0XOPiyVpB1tuAG6ElALbGxqO9pOZCneb-1ipw2_0kDIA0zpOH-3EvbqBrr92_Y-q6cm-VEZ9l7X8vcgn_wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیمای نظامی اوکراینی، که به گفته منابع یک جنگنده میگ-۲۹ است، در منطقه خمیلنیتسکی اوکراین سقوط کرد.
🔴
جزئیاتی درباره علت حادثه و وضعیت خلبان هنوز تأیید نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/128531" target="_blank">📅 20:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128530">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utss_j5uclQgJDpZUkk-RSPDjETqgqsI9rDcI__FziIRm9gpSRQZWnpXaEQpYdbh52n-uYkRTpSAzUr3K34Htxp2zs-yNWcKiSf5VBgd-3ni0BzO90KfcFXqYJyI6jR7hmIUYnyDW2ZXkNHyiKz32h97rXRaIzJujuNvQCnsBDmkflB-gai1HZewh2a1sGc8h1XKLJqjg6cW39Wz-L5032arU77utH1lFBncw_IC9sRBeGT5IE1jvfMmckm7SnfH-kjZzbQOmi8MMd1Zey1j0y8vDWyghsPJh28Ik5CUhVdpDtN-W2v9Kqb8SIWqkcw9bCcaZV62Cqdw-jScvAsTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش شبکه‌ی العربیه از پیش‌نویس توافق ۱۴ ماده‌ای میان تهران و واشینگتن، در متن این یادداشت تفاهم هیچ اشاره‌ای به اسرائیل نشده است.
🔴
این افشاگری در حالی صورت می‌گیرد که جزئیات این توافقِ کلیدی، توجه محافل دیپلماتیک را به خود جلب کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/128530" target="_blank">📅 20:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128529">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
قیمت هرگرم طلای ۱۸ عیار به ۱۵.۴۰۰.۰۰۰ هزارتومن رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/128529" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128528">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/023d758892.mp4?token=rGtEHig_zZX3xj95hCC6Dj5PVhMuv1m7qkK6oRibYz05q-qPUD8mkc4cU1JXFXkz-oPxr_8q47fC3-kUooX_vZ41UnRvMU4zj2MNheHiIcHXGzoDOxuqFG090ExTRlhIEHcI9z9wwu0cbo_lgs_Zvvm0SVStPgcLdnsoL2cIWyTK2nfxEPkrBwYFsQ2IPMFoyY_v0j5AsBsRuK8q1kfu_ufIdVeVbt5Xgn93HgPnUPnibw7uMxYvI29gWtIa-rtwXlQCRmgXTJTixqD7vpFThYcVKRM-sFbTgSlwBmvT0adWaLOWQO22veqfqxSE1ITNGi6Z-TQ3NiZhD34jmTMVyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/023d758892.mp4?token=rGtEHig_zZX3xj95hCC6Dj5PVhMuv1m7qkK6oRibYz05q-qPUD8mkc4cU1JXFXkz-oPxr_8q47fC3-kUooX_vZ41UnRvMU4zj2MNheHiIcHXGzoDOxuqFG090ExTRlhIEHcI9z9wwu0cbo_lgs_Zvvm0SVStPgcLdnsoL2cIWyTK2nfxEPkrBwYFsQ2IPMFoyY_v0j5AsBsRuK8q1kfu_ufIdVeVbt5Xgn93HgPnUPnibw7uMxYvI29gWtIa-rtwXlQCRmgXTJTixqD7vpFThYcVKRM-sFbTgSlwBmvT0adWaLOWQO22veqfqxSE1ITNGi6Z-TQ3NiZhD34jmTMVyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات اسرائیل به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128528" target="_blank">📅 20:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128527">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
خبرگزاری سی‌ان‌ان: برآوردهای اطلاعاتی آمریکا نشان می‌دهد که ایران اکنون می‌تواند هر زمان که بخواهد تنگه هرمز را ببندد. یک منبع اطلاعاتی گفت: ما عملاً کنترل تنگه را به ایران داده‌ایم که سلاحی قوی‌تر از هر سلاح هسته‌ای است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/128527" target="_blank">📅 20:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128526">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
فیصل بن فرحان، وزیر امور خارجه عربستان سعودی از تفاهم میان آمریکا و جمهوری اسلامی ایران استقبال کرد و ابراز امیدواری کرد این تفاهم به بازگشت ثبات در منطقه کمک کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128526" target="_blank">📅 20:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128525">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3RVmNAaYRI0Al_4_VI_qUEQpN6ADV8gVp1oG0wwHM2ahx8KAzXtVHKPQHsbnsUskEjumEFbl-E0U6CO1GoFlY_J25gIrJKz2gaxYDTa831BIpil_etHq4oQSOmuqMx-Qhd8chNC6OhmveGarTD-03bMZoFwCIMYBAN-IZgnmGhItl2UszIPva-rMY_RVJo_tQDqqW5cGhc9RcwJwyY4HlZqwh6iaqf7bhjD9Hr_Zbh0l8_R05_O7I4c7deqPEP-JnkhVAw6XS4eBHqFY99pZZyCV1nmJYr14m5sYXcSdDTyFyrT3B1CVTn48z7NDfZATPFM6VdAV8XH1SwMrWBlcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس نظرسنجی مؤسسه کانتار، میزان حمایت از دونالد ترامپ در اسرائیل طی فقط ۳ هفته به‌طور کامل معکوس شده و از مثبت ۲۳ به منفی ۲۳ رسیده؛ افتی ۴۶ واحدی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128525" target="_blank">📅 20:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128524">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
هم اکنون پرواز پهپاد های اسرائیلی بر فراز لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/128524" target="_blank">📅 20:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128523">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری / منبع به العربیه انگلیسی گفت که ایالات متحده، طبق این تفاهم‌نامه، متعهد به لغو «همه انواع تحریم‌ها» علیه ایران است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128523" target="_blank">📅 20:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128522">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164440dd96.mp4?token=JV5tPzVwsssSFFHYMNOoISArg_-LhsGXXbWp4Ey6_HCJD_jrFp29lEF8b_LC0fSD4CzWiSKgIPLXD9qgvqkMAHPgtUrQGHihiRMyBGk8HOm9TTzo2oLx1ckeKRoHC26hy2PEI4c2mSciusAoUW7MrdRVBfVwY90CPNCcHUthQLI33HFHBoCyxIuZZx1QQne7V5BFEDSYefMIjIDdw82chy6ORZkG8aN5nGmef9oBGqrel3EjbjG65tFFRWP6Sa6cdt_hpEj8j4NpkFjuRHnZOVPwaZjvovuxH91QeHL-NfIthzlM7yb0BoaqaogHiM7byZhtdKDZMtZTfqRccf3aOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164440dd96.mp4?token=JV5tPzVwsssSFFHYMNOoISArg_-LhsGXXbWp4Ey6_HCJD_jrFp29lEF8b_LC0fSD4CzWiSKgIPLXD9qgvqkMAHPgtUrQGHihiRMyBGk8HOm9TTzo2oLx1ckeKRoHC26hy2PEI4c2mSciusAoUW7MrdRVBfVwY90CPNCcHUthQLI33HFHBoCyxIuZZx1QQne7V5BFEDSYefMIjIDdw82chy6ORZkG8aN5nGmef9oBGqrel3EjbjG65tFFRWP6Sa6cdt_hpEj8j4NpkFjuRHnZOVPwaZjvovuxH91QeHL-NfIthzlM7yb0BoaqaogHiM7byZhtdKDZMtZTfqRccf3aOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل: لانچر شلیک راکت تو جنوب لُبنان رو زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128522" target="_blank">📅 20:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128521">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر امور خارجه چین، در تماس تلفنی با محمد اسحاق دار، وزیر امور خارجه پاکستان:
چین معتقد است که در مذاکرات ایران و آمریکا، نباید به عقب برگشت، چه برسد به استفاده از زور.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128521" target="_blank">📅 20:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128520">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری / منبع به العربیه انگلیسی گفت که ایالات متحده، طبق این تفاهم‌نامه، متعهد به لغو «همه انواع تحریم‌ها» علیه ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128520" target="_blank">📅 19:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128519">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): پس از ارزیابی وضعیت، دستورالعمل‌های دفاعی فرماندهی جبهه داخلی بدون تغییر باقی می‌مانند و تا سه‌شنبه، ۱۷ ژوئن ۲۰۲۶، ساعت ۲۰:۰۰، در حال اجرا هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128519" target="_blank">📅 19:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128518">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxWbGpje-YHywfQQp9jIk0kBIxl6glqsk3m0iRc708XGTg3lNd9T0cihjR6iB0Vjyryfjvt0aB7jf_ui_xquvmlG6WIXGsqfxcBBf5mfdPkkCPR4GnSdq2rgn0MfxHtS1WD8qREXqa9bC5O-6ibPTWFgGKvcDVrktFtu2l6WkHnupT6C9hfNZV8aJ2Jw7fZL9mq-meuWqFT6fvV8X_ZaXDx3QAgMNZ3pHCO91l9BNHhBh9E5C2lZu_SIG6l6zanDC-xLaSHkgXeCbWG42a_kkYjstxx4xcnHYnjwvlmuAv1mm_g3jS7Nc-hOsR9NAjutKOjT5SAIKjzj7lMH68F3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش بلومبرگ، توافق صلح با ایران و بازگشایی تنگه هرمز در کانون توجه اجلاس سالانه گروه هفت قرار گرفته است.
🔴
اگرچه متن نهایی این توافق هنوز به‌طور رسمی منتشر نشده، اما سران کشورها بر سر امضای آن در روز جمعه به توافق رسیده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128518" target="_blank">📅 19:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128517">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رایزنی وزرای خارجه ایران و عمان درباره تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128517" target="_blank">📅 19:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128516">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک منبع:
تفاهم اولیه آمریکا و ایران به تهران اجازه می‌دهد فوراً نفت بفروشد
🔴
واشینگتن به تهران اجازه خواهد داد تا طبق توافق پایان جنگ، فوراً فروش نفت و سوخت را آغاز کند
🔴
معافیت‌های ایران شامل خدماتی می‌شود که فروش نفت را تسهیل می‌کنند، از جمله بانکداری، حمل و نقل و بیمه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/128516" target="_blank">📅 19:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128515">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
اف‌بی‌آی یک طرح تروریستی عظیم و چند مرحله‌ای را که هدف آن رویداد یو‌اف‌سی فریدام 250 روز یکشنبه در چمنزار جنوبی کاخ سفید بود، خنثی کرد.
🔴
طبق گفته مقامات فدرال، این طرح ترسناک طوری طراحی شده بود که «حداکثر تلفات» را به همراه داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128515" target="_blank">📅 19:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128514">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6b516f19.mp4?token=nGQoaXJb0d3SDkYMufEfH6as9bWCL65qYwoixUI3qmIPMc2oRw3SCilBNof6zCSY2z8kmJAYqJMYh2e6JQoIGw5c8aB2Gyy3bfGHKHfqKOUJLrPceYF196VnRzXWxfJdcoWUWNAsSuheCeQ-u1LqcqGWyw6LjO0ZtEcXqFI5Yo_qFDuHDAQjuz26BOreoIea-ordj5OK33jLC1dyTG909Fj7XNrEJJc3jDVhcfVIeuZgyL3uRLPuMCCf4LFOA19Ce7Yruz204yMFw5ktLVYyyBJSD41Kl2nbWiuJ5BzjMSj3If7F6aSemdtGcbzOc2FmWh6o-FVHVl55SBI6ylIZ0iva1ddtRTwxpNhzRuFyv9PYWPUQ177e0AA-bkLqcUdsO-u93tP3ZFA1xmUsFK5x8xM8uZOZk1Z8b11fTEkoro5o50QJFyH9u-X7tqD2l4tBOZKAeRwpBEOSLjHrhkOxKcyKLUHy9eV18oj1BG-kos6UqAeNgO2hjwmQ9TXYDMF0P6CQmBmKtHOuakvYqAsVfCFP-t0u3k2JzKr7E3axehNZMUkHu7qP6_nC-ESimqm54zaMI-Wvfkf3aywNKkz9NzJlvimZ2n9XO8CRDkFI9Jeeu3851_k1e73IfM9zGQdX7jY2pZVmBOzB0MEM585GvF1HX7RefAiFmh7EBM1HhCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6b516f19.mp4?token=nGQoaXJb0d3SDkYMufEfH6as9bWCL65qYwoixUI3qmIPMc2oRw3SCilBNof6zCSY2z8kmJAYqJMYh2e6JQoIGw5c8aB2Gyy3bfGHKHfqKOUJLrPceYF196VnRzXWxfJdcoWUWNAsSuheCeQ-u1LqcqGWyw6LjO0ZtEcXqFI5Yo_qFDuHDAQjuz26BOreoIea-ordj5OK33jLC1dyTG909Fj7XNrEJJc3jDVhcfVIeuZgyL3uRLPuMCCf4LFOA19Ce7Yruz204yMFw5ktLVYyyBJSD41Kl2nbWiuJ5BzjMSj3If7F6aSemdtGcbzOc2FmWh6o-FVHVl55SBI6ylIZ0iva1ddtRTwxpNhzRuFyv9PYWPUQ177e0AA-bkLqcUdsO-u93tP3ZFA1xmUsFK5x8xM8uZOZk1Z8b11fTEkoro5o50QJFyH9u-X7tqD2l4tBOZKAeRwpBEOSLjHrhkOxKcyKLUHy9eV18oj1BG-kos6UqAeNgO2hjwmQ9TXYDMF0P6CQmBmKtHOuakvYqAsVfCFP-t0u3k2JzKr7E3axehNZMUkHu7qP6_nC-ESimqm54zaMI-Wvfkf3aywNKkz9NzJlvimZ2n9XO8CRDkFI9Jeeu3851_k1e73IfM9zGQdX7jY2pZVmBOzB0MEM585GvF1HX7RefAiFmh7EBM1HhCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله یه خودرو نظامی ارتش اسرائیل رو با پهپاد «ابابیل» زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128514" target="_blank">📅 19:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128513">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4bpnfG8gqprJhKfQ2FOaB5MXH4gk7mxYzHCWV-d13cBlri12ciI9wDw1iGFLq7LiBGv9zjvh4Ov005_SHKRPapz0RXiLJE2p2jq1bbF8puwpvvM7N7BynKA-DVKEHVKfkS0-hZaRuUJ6Q8Gi6OqU_J8cYvpXDuYYo8H-tDP6oBlHu0m68Qn0rNQsqqSPtXvsaf6HzQoTRx620mTjrfAvc01YnV8d1YK0uJf3ZGkSBya1zmvjcHQ6WR7dNMSzx2OAsmT6HLpq2gBvRc0omCKFz5FQwIQMCkNoRFhvJsooSzjjg8tR5nujRuyymEUCFZzj3Ky0i9zGxMZpwIY82YHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ‏آنچه تفاهم شده، گامی مهم برای توقف جنگ و شروع مذاکره است
🔴
تمرکز دولت با یا بدون توافق خدمت صادقانه به مردم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128513" target="_blank">📅 19:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128512">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnUfWzLF153LNAK4b-uJSLWUeze3SqI-rY0rrAQJ_oZQgXYZmRpTZoCkp9OBgOvT3kmfTu4ezWSe8JgrHmop0HYFXnFMTPKHu7xsYzjIBFoSB_BFlCimE3YhCOwk3_sLILn-ZC6uZomgTGaRpqW7byiCZpb2o_BDc8gyzo_vR7G-UfCTIg19f77BDG7HfyDdLCLyoH1Bzt7XCZKmEFuZ4GJG-GUjnbgcMFO3OIWR45VsdS5AE024iY8xgOTPcs2NGQrMt8QCu-HrF46fkoHvTxRsrztevVKP3c1BpzsCSqYqZtzCBfLhQvHRqvyobl2jXIcA1WHr-jQxV2uIs0pwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر به ۱۵۵ هزار تومن رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128512" target="_blank">📅 19:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128511">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
توپخانه ارتش اسرائیل (IDF) شهر مجدال زون و همچنین حومه المنصوری در جنوب لبنان را هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128511" target="_blank">📅 18:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128510">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSSMco_ST_4CoDwLC3ELEYQJoj3MQ3Es3KBhnCI2BVjzA5rb6LTXVAGrHHqBPESdqfxT_8_Z9l379zjxDNZSoML0q7L4cTav9ql0yTdS7ltq_O_JkcGPa0Vihtahy8QO00-_OdteTwe5dVbkY_cc5T3Jo4zGRgdi-1jNmpKMnqSuYnFSBKiabjtVAgt8raKJ_QtvDGcPPXaAU9dJ7VJF4VwttW0HAEgOk-bTjFIdvzuVeYLuD4LQceQ_VPW1N1cW56H6iMw4Qxrd-EJaTXhWeuQ5hso7_pmYyQCrkLqInSBwhzD4nt-xuVFKDgbcOzyZS9OVqnxz98Lngk9a6dUgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ویتنی رایت پورن استار آمریکایی تصاویر جدیدی از حضورش در تهران منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128510" target="_blank">📅 18:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128509">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/023d758892.mp4?token=pJxErUXSIB9K5Pk-icFWvo-3UpVR83ZGRwmmd4HUP9GSTgldSqIu8T35d7iTDY8VY_w8WpxqfVpDuuQi6HqgMgimBknRA726qeYjQQr_cgzPLIVV1f-aDvjxuD8dBBPDXdNdowJ_heNka9NR95TW0X1yiKjAAM-dIaph-Z0thVXHqm1HWAwxKzAbQ1iGGOfEzU-9FCJerUTKm-kdQatxU_F-7iHtmXiNzUyIIgUmBadDULq2SuZ7EIxGVySwwRMW-KMsh0_2_lZ47rFcDryQ_o_WMLxzoe4LU5mqfzw6Ku-8662FiQKDcMUfQZuhhXSZxhxLdLihofNuthJnWb_5BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/023d758892.mp4?token=pJxErUXSIB9K5Pk-icFWvo-3UpVR83ZGRwmmd4HUP9GSTgldSqIu8T35d7iTDY8VY_w8WpxqfVpDuuQi6HqgMgimBknRA726qeYjQQr_cgzPLIVV1f-aDvjxuD8dBBPDXdNdowJ_heNka9NR95TW0X1yiKjAAM-dIaph-Z0thVXHqm1HWAwxKzAbQ1iGGOfEzU-9FCJerUTKm-kdQatxU_F-7iHtmXiNzUyIIgUmBadDULq2SuZ7EIxGVySwwRMW-KMsh0_2_lZ47rFcDryQ_o_WMLxzoe4LU5mqfzw6Ku-8662FiQKDcMUfQZuhhXSZxhxLdLihofNuthJnWb_5BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات اسرائیل به لبنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128509" target="_blank">📅 18:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128508">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfsVcat32lukRwHhQ2JIMYkBgh_hK8mvzbChCjss-obgXWDysT2X3EfiZ6fDeC4e77LxZBzhvmfTnd_hB5pw-UOgfOjLjXSGexKCpQ_N0cRnu_saRl4d6piFFmXs9f36Y8ueIKUMMXnOhGoOHNyYrO6GFgEOrkQ2jMulMWau2pdZjAYf_LkfpcOJgQqgtOXqNeN15I2KiukB97FXxijU_B0z-fH8Pw7QlAwkdsGCrPbnoXCQ-1cmW03pAS2UqH04t9OeGbqHt_Rld5DPc65ENZYOAwzU6DgA0mNDR9WYswK8_Fh7OmZ7h8NjjNi24sQrWvuEIB7bbFlMEvXqVNp0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی زاده مجری صدا و سیما در ونزوئلا قبل سقوط: اوضاع اینجا عالیه و همه چی اوکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128508" target="_blank">📅 18:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128507">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b13e4ca3.mp4?token=erjPsDIR8wzQ5_gFsh3Sy2UvwHXonQXd7JOQhwC9zsNxKH_pUO--EgWNymkd9QM3XQae3gxTsghrs786Bg6iCKgXCTPG_Ds7oRz4LyVNs96YB9Wlh5zBujYFn46-r2FjVCLS9n2ibI8t6UT3oP_rSyuQY-8mKKhPOZwVoP3-GSHn6VRbg5YI1CPC1G9Iyu52JDLuFha0cdzl935Pp9sa-NaWk38nVMFTKzSJuzz6tDgfY3erOa0AvcPGcBaaX1xngL-SiuF6GlpT6wA-QHGrwCB4XKcYVypqA0knU5WWbROLJsLzDOsu1oudowD_hoptdc4aLMCwO5G6e4ZpkXXFh5y4oX3vdJo7i1Vtp3q2a9vwLz7RczbEmPQXs0-PO1mUg9uQ3W0V5M2nKAq8uM6VM5OMGsRORjtl6OyKoaVUSaYTxmSw3O7YOudEgwRMj7W72pSOyalGx6kgcXK5HgeFg00aKIquTnIwXEgJwkkhNwvI70a8eEqFKATYGxRGDi5dWIPVIXXMc7gXe56QuBEP7dZt_elG6DyWydCz7Oe9YFQpN9GPStlwxTJypmSKaN1j4zXyEinw1WjNtxZur-_o-dE-x22ec8i9VzuMAP1Jk2FfZq_6JV68YZRGzb_YCcwVk7qYaPv0d1f-xqbUFDKdNQGx78ye8ACth769UdsPWmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b13e4ca3.mp4?token=erjPsDIR8wzQ5_gFsh3Sy2UvwHXonQXd7JOQhwC9zsNxKH_pUO--EgWNymkd9QM3XQae3gxTsghrs786Bg6iCKgXCTPG_Ds7oRz4LyVNs96YB9Wlh5zBujYFn46-r2FjVCLS9n2ibI8t6UT3oP_rSyuQY-8mKKhPOZwVoP3-GSHn6VRbg5YI1CPC1G9Iyu52JDLuFha0cdzl935Pp9sa-NaWk38nVMFTKzSJuzz6tDgfY3erOa0AvcPGcBaaX1xngL-SiuF6GlpT6wA-QHGrwCB4XKcYVypqA0knU5WWbROLJsLzDOsu1oudowD_hoptdc4aLMCwO5G6e4ZpkXXFh5y4oX3vdJo7i1Vtp3q2a9vwLz7RczbEmPQXs0-PO1mUg9uQ3W0V5M2nKAq8uM6VM5OMGsRORjtl6OyKoaVUSaYTxmSw3O7YOudEgwRMj7W72pSOyalGx6kgcXK5HgeFg00aKIquTnIwXEgJwkkhNwvI70a8eEqFKATYGxRGDi5dWIPVIXXMc7gXe56QuBEP7dZt_elG6DyWydCz7Oe9YFQpN9GPStlwxTJypmSKaN1j4zXyEinw1WjNtxZur-_o-dE-x22ec8i9VzuMAP1Jk2FfZq_6JV68YZRGzb_YCcwVk7qYaPv0d1f-xqbUFDKdNQGx78ye8ACth769UdsPWmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تغییر رژیم به سریال‌ها هم رسیده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128507" target="_blank">📅 18:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128506">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b5a68df5.mp4?token=UfYhzYns8deD8Dr_CdTOo___sk-TFtDNALJOE4C5_xZBIdyuZfYTTrKxActgQ4OazmgosfZbggzIFzlhCPikg4I1RuHGiH-URB52QiUU-LEsr9R41uNLcwv92MctHbeZ-OGPa2lmod20vX2vk5qrN10xbaMRRv8xw4jFXbHbbWvsxMDzmuU6vh-JmmJGn67kaRN71Di-2JOAS3JA96tPMx_IPzMH5rEE-OfiPYNZAjUk3GMZhN67u4murZAK2b8XpKpPx9gXpLKyonJvCrA4ihz8WbW2WYjhwGc4gjJrAJb3qb5OxJXzoeE_xbhyTIxhBddp_uAwG5n__MVbrG46Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b5a68df5.mp4?token=UfYhzYns8deD8Dr_CdTOo___sk-TFtDNALJOE4C5_xZBIdyuZfYTTrKxActgQ4OazmgosfZbggzIFzlhCPikg4I1RuHGiH-URB52QiUU-LEsr9R41uNLcwv92MctHbeZ-OGPa2lmod20vX2vk5qrN10xbaMRRv8xw4jFXbHbbWvsxMDzmuU6vh-JmmJGn67kaRN71Di-2JOAS3JA96tPMx_IPzMH5rEE-OfiPYNZAjUk3GMZhN67u4murZAK2b8XpKpPx9gXpLKyonJvCrA4ihz8WbW2WYjhwGc4gjJrAJb3qb5OxJXzoeE_xbhyTIxhBddp_uAwG5n__MVbrG46Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس فاکس‌نیوز: زمانی هدف ترامپ تسلیم بی قید و شرط ایران بود
بریت هیوم:
🔴
اگر تمام چیزهایی که رئیس جمهور ترامپ ادعا می‌کند که در توافق هست، در توافق باشد و به آنها پایبند باشیم، احتمالاً یک پیروزی بزرگ خواهد بود.
🔴
اما او به دلیل حرف‌های گزافی که در مورد دستاوردهای اولیه ما زده، کمی در موقعیت نامساعد سیاسی قرار دارد. هدفی که او زمانی گفته بود تسلیم بی‌قید و شرط ایران بود.
🔴
ایران چیزهای زیادی از دست داده است، اما این تسلیم بی‌قید و شرط نیست، این چیزی است که وقتی مذاکره می‌کنید به دست می‌آورید. دولت به وضوح در اینجا کمی عقب‌نشینی کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128506" target="_blank">📅 18:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128505">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veWXJgP7G32wt-8LO4D3xUdammsLug5UHSzOcr7DSdh5iL_VNTdh3nBbP4lTQuNqD5k6ZAkvsQk7XvYjdgD8pCSoS2Oedica9EMEDetJSdz-lFuTuNyEiLIWOZ47ZZx_wFRhve_uJByQb39Dd0kyoPSnaJeqfBZ3_1Y-PrP45QTNATVlmmN_sMkwaJhzKcGjKAmuFHx2QA1Keuv5mG0tDoe4wPPGXeg8VUTaoKx_7_TNqidqgxPyWwt6Km2ucjbKfCRV0cwu1LQZkdl2jw8Iomngp588d0ciGsBP5GTFSSgM25aRRUgOefF-5JrWYX8U4C8Z4FpaDTWqllfhkhtOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس
یادگاری سران G7
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128505" target="_blank">📅 18:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128504">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a196a552c3.mp4?token=ImXj-NIeHwek3PWpWdmhI8nIpTb5tf9HsajM9fI0GVm3iecXz91qcBJrVGtQ3iMJXvzdNNrp4lv67ueekwXpElgavGR7pQYrCU-a7JqOgLwSJ5e2IXe2pH43InWqi5KPNcDh_5yWORCWOp9pmVDvEkXldHdIYrJHrFF1k15EsGcb9St8HmeXEH_biyCtAcfmcFI_XXbkid1UU0ysv6dZ0XWDX0fpcZ7oRq89FYh0xclivjVipHy71e9o_6skgQ3daViA-6Qb4HJLJMOWIem4pgDkLrX1tR5-RKj5vKQY2i6j8ejUDrI2pSqhO_0vMLtf6fzlxtLF0yVZcH3yF-wB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a196a552c3.mp4?token=ImXj-NIeHwek3PWpWdmhI8nIpTb5tf9HsajM9fI0GVm3iecXz91qcBJrVGtQ3iMJXvzdNNrp4lv67ueekwXpElgavGR7pQYrCU-a7JqOgLwSJ5e2IXe2pH43InWqi5KPNcDh_5yWORCWOp9pmVDvEkXldHdIYrJHrFF1k15EsGcb9St8HmeXEH_biyCtAcfmcFI_XXbkid1UU0ysv6dZ0XWDX0fpcZ7oRq89FYh0xclivjVipHy71e9o_6skgQ3daViA-6Qb4HJLJMOWIem4pgDkLrX1tR5-RKj5vKQY2i6j8ejUDrI2pSqhO_0vMLtf6fzlxtLF0yVZcH3yF-wB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جِی‌دی ونس
:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند.
اگر این کار را بکنند، عالی است. اگر نکنند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128504" target="_blank">📅 18:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128503">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ونس به فاکس نیوز:
ما پیروز شدیم، چه ایران روش خود را تغییر دهد و چه تصمیم بگیرد به توافق پایبند نباشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128503" target="_blank">📅 18:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128502">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/c96ac20501.mp4?token=kpabYDiOM_RW3A86AkhbYUL5zWIrjgV2eojlJifMIeOiGUmKAw1aqC9uv3xZ4dExhmDBlIeFC3_1FEU8RzlUxHUZkesyF-RyB1sH5WvvQzpGJnM_plbhhQF7iJWasmrPSteFpGauVF0e-FKKDQP54JTe6ZyLjW2AWrIEIHM6YF4iEW0-A2wVTU_cgM_0PYNu8oT-Pbswi81w8qfcl0aZiLpd6iN_25ZJKrZzs4rlGVOWXMBU-bEXm8En6xDQDM0kKpuCTrRVxxBIeR1L_wHKZFqFcOPHpGad5gbA9fmoRkyxD4zwUby1-xsigpMw5TqoZMagyIjA-iM3Q-5cVeJkyg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/c96ac20501.mp4?token=kpabYDiOM_RW3A86AkhbYUL5zWIrjgV2eojlJifMIeOiGUmKAw1aqC9uv3xZ4dExhmDBlIeFC3_1FEU8RzlUxHUZkesyF-RyB1sH5WvvQzpGJnM_plbhhQF7iJWasmrPSteFpGauVF0e-FKKDQP54JTe6ZyLjW2AWrIEIHM6YF4iEW0-A2wVTU_cgM_0PYNu8oT-Pbswi81w8qfcl0aZiLpd6iN_25ZJKrZzs4rlGVOWXMBU-bEXm8En6xDQDM0kKpuCTrRVxxBIeR1L_wHKZFqFcOPHpGad5gbA9fmoRkyxD4zwUby1-xsigpMw5TqoZMagyIjA-iM3Q-5cVeJkyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهبادی اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128502" target="_blank">📅 18:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128501">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پاسخ قاطع قالیباف به مخالفان توافق  [@AloTweet]</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128501" target="_blank">📅 17:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128500">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqw9lvvVVAOgykDsjiBsAN5t3q2WSu1UNsr3kLmoNVtp29GVDmtDscDVOo7GUBFHlXLAgPif4w2Ze--cTaFQKrLZ9o1J2LcKAHRt0ZvptvFfmeGLfDjKcMfiHrpsC6sx3uZDzPANQ4UOf6Sh2ILHZkk4vV3dvkOVYzea8mrgRyQ6p4KrWqqPEBsVsFVbGpSnF82jamM6mnE7ODvhtOBh5oq3ngC0oLan99VhGbE9sfOiIuMTYGirgvdBQgQdKaK_IsFli0o_a2hRplumKnCvRoP-A39__HfCHMmBd1hEeNicTKSpB92noP15MVgWRSb2rLsL-8p3HQn2nqGnIRfhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان :متن توافق منافع ملی(کاسبان تحریم) را تامین نمیکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128500" target="_blank">📅 17:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128499">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
نتانیاهو خواسته متن توافق با ایران رو ببینه ولی ترامپ اجازه نداده و گفته به تو مربوط نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128499" target="_blank">📅 17:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWB8JPS83q0cElPo1ppcM6BSec9D2gqb-gjwVdTva1rMkpzF-hIvzXAQobKf9KjQnfjYEp1tu7Yc_w8csc9GolYEaTMEHDRtQZ-7mHcQu1EEHTlDhOTnCdM_sHv2WfzXjBk4TgBaUX7IRBlAgS1uX0XGVABHmrdfPsS1A995gcDBPSvK09p7tbf5zKvtQTW5guZsBnEuH6xenL2Vrj51yKcnvJohiujKz3lG1KK711kdxJxr6bSljfhr_TPDdp_xCD2CKftfdS8VOvrjtEEB2WxVGSPB3CnZBHRKyzg0vmC4IYkpWXySwFEJo7MFTOTn7Gnqe1JFaCI7CZCIjPAQwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJWuxJTYSx_2_BcRGrGDC4pkeTPyU9DcHiiGQ8qbaZFwqfgd2_sTzlEOsyuWFG-z_dm1MsEN3TcvnZbkUH5z7WHLW0gHSA5Y37CkAP2h4VREGWTtjR9Fw9ma0Gs5ZB42wFaEq4z3PS9GJa38f49jpLUN9vdKUAaULSq6_RjdArEswyAyAnvWoezkLCYw5karcrN3K1QCpSpirD7IkGIrdshjML0wkyiP73DweT2U5fr1ag8V8NE-Jbsq0jp2FJIGdKmjysgjrLaLR2HuK13PC-xgvZJrzVxmaA7AmdgFKd_wqfTZSCq1pek5V0tvDmTtagRdGhs-Q4FsP93Dt9oc1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
واشنگتن پست بخشی از مکالمه کوشنر با قالیباف را منتشر کرد
در بخشی از گزارش واشنگتن پست آمده است:
🔴
طبق گفته یک مقام نزدیک به مذاکرات، وقتی «کوشنر» در ماه آوریل در اسلام‌آباد با «محمدباقر قالیباف»، رئیس مجلس ایران، دیدار کرد، صریحاً به او گفت: «ببین، اگر شما بهایی اندازه رولز رویس را می‌خواهید، ما هم محصولی همانند رولز رویس را می‌خواهیم.»
🔴
به عبارت دیگر، اگر ایران با باز نگه داشتن تنگه هرمز، توقف غنی‌سازی اورانیوم به مدت ۲۰ سال و متوقف کردن صدور انقلاب خود، به تعهداتش عمل کند، می‌تواند انتظار دریافت صدها میلیارد دلار منفعت را داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128497" target="_blank">📅 17:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128496">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6909ecd3.mp4?token=RQ7RJXuBSbMzgbyGs-gZd718n35jNiIlX1hwp-WhIWg8CwFtKzfkU3ZYB3i6opXcz5zzXjaVyY4lgVXpd75_37Y6oPYW_DzzFVAEJJSHyjgrXa4arWaOAH3h85f2OV90iVdMnuBiCA5Lmfhj-VZKO-3_Y6euEBhzh8ur3Z96R-8nKdZqElCH-bOvFYCqh9ywAzskFkaojbMhMomWK6mGpFDcQnVyN-r8PE5Qbk1E-QhkJOeTNOJctEboi5TSUNht5GWupV8ciwq9xFGFDcizuimmt1J_vL0TyObFnftxyL38ScLnFdpMTiU4iQzQMV-OuT6DK9K1DvbbyvA_tv9OTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6909ecd3.mp4?token=RQ7RJXuBSbMzgbyGs-gZd718n35jNiIlX1hwp-WhIWg8CwFtKzfkU3ZYB3i6opXcz5zzXjaVyY4lgVXpd75_37Y6oPYW_DzzFVAEJJSHyjgrXa4arWaOAH3h85f2OV90iVdMnuBiCA5Lmfhj-VZKO-3_Y6euEBhzh8ur3Z96R-8nKdZqElCH-bOvFYCqh9ywAzskFkaojbMhMomWK6mGpFDcQnVyN-r8PE5Qbk1E-QhkJOeTNOJctEboi5TSUNht5GWupV8ciwq9xFGFDcizuimmt1J_vL0TyObFnftxyL38ScLnFdpMTiU4iQzQMV-OuT6DK9K1DvbbyvA_tv9OTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی تندرو: ترامپ راست میگه رژیم ایران تغییر کرده. اون صادقترین آدم روی زمینه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/128496" target="_blank">📅 17:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udRSq8HZ9qBYrFJI77ePxL4ZsGgXQeSRhh-E6aV3vA6PxLfAM5SkylaotLhL4dawfE12UwZey9xIiarRoaEE3BGtpQQGi0NcOgNwY-omxGOcvceQML86oJCaobBi3Mux4k_Xu2XzY4npw4nGrOLP1vIwR97ghhqDCP1P3YBJkBvW0KvxOJB-sbHpITWl3KuvBWjLFeMMmclnnhdSskQFErqXf5y3sLSYdKaU4E6JJJph56486sbP3M4lYhpdtxqM1rFPXjok47yyjENogTuC5mXXOUByKoq6RO5v9MBQiY_X7FA9BXoOlznnTXK8TCW5N3Lck3OlHowOoOIlQDskqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوئیس محل امضای تفاهم میان ایران و آمریکا را مشخص کرد
🔴
وزارت امور خارجه سوئیس با صدور بیانیه‌ای رسمی تأیید کرد که مراسم امضای توافق‌نامه میان ایالات متحده و جمهوری اسلامی ایران روز جمعه برگزار خواهد شد.
🔴
این مراسم در مجتمع «بورگن‌اشتوک» (Bürgenstock) در سوئیس میزبانی می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128495" target="_blank">📅 17:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر: قطر در دیدار آتی ژنو حضور خواهد داشت
🔴
توافق فعلی گامی نخست به سوی یک توافق منطقه‌ای گسترده‌تر است که ثبات منطقه را تضمین می‌کند.
🔴
ما در نزدیک کردن دیدگاه‌ها برای دستیابی به یک تسویه میان تهران و واشنگتن کمک کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128494" target="_blank">📅 17:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128492">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHBZ2k7zZpuf5PdBThvRTVrGFZUrc4H0ecc5hy2yXSMP4QdYO5wp-72UhLBkKi7iPO7FvdRwGjGb8h45vP_siElv8WAumVKTM-bAZLbNTf0Yhy--HfpcOGhG7DETYtw4yJdzRcAAqGXGbXLDs1ISNdjGeCVEPNfnxc70WvFaYK5jl6gbj7OEXD86yzPKqxKXCOFVPRBRub1vtkFP0gBpkxQDJIyBPB8DT6GldZqRHkSAqropmUNLuIEk9dJv1tlGAWoAwaqOjtqo1ii2lCXzkFhSIL0W2Ss508-VHSJ47zJU6bU1FEeh6SPseFa9bMaD1_BTmrPhV4NprldBSjIEOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجید تخت‌روانچی، معاون سیاسی وزیر امور خارجه، روز سه‌شنبه ۲۶ خرداد، در حاشیه نشست با دیپلمات‌های خارجی در تهران، جزئیات جدیدی از گام‌های اجرایی تفاهم‌نامه اسلام‌آباد ارائه داد. او تایید کرد که محمدباقر قالیباف از سوی جمهوری اسلامی و جی‌دی ونس از طرف آمریکا برای آغاز مذاکرات و امضای توافق در سوئیس حاضر خواهند بود.
🔴
تخت‌روانچی با اشاره به اینکه بلافاصله پس از امضای تفاهم‌نامه، گفتگوها درباره توافق نهایی شروع می‌شود، افزود: «ما در این مرحله وارد جزئیات بحث‌های هسته‌ای از جمله غنی‌سازی، ذخایر و نیازهای ایران نشده‌ایم و این مباحث پس از رسمیت یافتن تفاهم‌نامه آغاز خواهد شد.»
🔴
معاون وزیر خارجه در پاسخ به پرسشی درباره نقض آتش‌بس از سوی اسرائیل تاکید کرد که در متن تفاهم‌نامه بر خاتمه عملیات نظامی در تمامی جبهه‌ها، از جمله لبنان، صراحت وجود دارد. او تصریح کرد از آنجا که آمریکا از طرف شرکای خود متعهد به پایان جنگ شده است، در صورت هرگونه نقض عهد از سوی اسرائیل، از مکانیزم‌های پیش‌بینی‌شده در یادداشت تفاهم استفاده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128492" target="_blank">📅 17:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128491">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y88DFpqMIctW-KzS0UxZaG5cetvee8cbhQCOyxxKAsiT5V9dzcWxO2eDPyiTtyhzfznVm_rgU0dQ17uW2sKMFnLtRa3zHoeUAZomS_IIjL58JTNfmMP9sO-VFW2xSvYg1n3_tn2r3506qpwLHxatDdWqVOq0gsuK0ZZjn4pm4t3vjrqJXdUqixmJ6pczbGIgvVjUpEWsRQjJVT39mxiOKN52fHJXEqPs013bO0mEmCvu1uLmlv7pv2K6lf32NuIrvYVIsCm32BoB8viRz8NzLOvHt0qDBFJzNqNlDi_0nfEnDvaRpU4mHyy9FG9EjfiAJdxlwIj8upjCrehTy-1Bsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون اروپا: من به ترامپ به خاطر توافق با ایران تبریک گفتم هر دو موافقیم که این توافق باید به معنای پایان قطعی برنامه هسته‌ای ایران باشد ،تنگه هرمز بازگشایی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/128491" target="_blank">📅 17:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128490">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0zdEZseoT2beTWTZe6eVsUJhdmKIOJFclJWsrlChCdn6CXIZ6H5MH-R8WV9dHzZVb45R0kqQdwwqyVD2gkcbhM--8vws0qoT6mjuD9ssbL99CwHFz9bbuClMwtpXEAhLCVF8bt7lB1WNj6raaBFFRwsObjrMDTEYI9N1dSODoY1neTPWsca3x4ODZZpUAE4_jCV_lKShemOlplldojCysva7JfbH_prOo9EPZ4sAwzwStg4rh4k97ZYApsPYN-rrPfiKqoC4tlFzDcayuQnxzepSGwiKJxODFdprahtAvAucb6EmMFaS1AjxVmMxsUYCDyJPle9JC2NKqJ7Uk3HGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ایران در رتبۀ چهارم؛ پرتماشاگرترین بازی‌های جام جهانی تا اینجا
@AloSport</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128490" target="_blank">📅 17:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128489">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f469266c7.mp4?token=Lm-cRc3qxWSoFOalDHZWj7p4SGebt9EdpOSj-u2Ais--hYH9hku3AOaWc4bSwJjWw2ehTby_FLEQkBTVc96v-Po3Xg6m4dXZ-1bi-eauoX4mhWrVd5v_A-CCBmjbJo-dwrduKwqA10jhJKYHU6iEq9X7QM78f9Y6v8xgW2BEChJJs5CUwuEY0Q5VyhH3hGmVpxni4oVyWOuvYfeA5Wya9Um5hx1ZhnXujx6L0ez8IzPghv3JKo5LmXFLh95EjcFjZnN1X8m2mp0Kaep4-02-p6YOUz8WEY4Yc2uSHQE052qPhKNZIfVHeTOmvZsszIZAbdXdatYezf9anHJoqD9oAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f469266c7.mp4?token=Lm-cRc3qxWSoFOalDHZWj7p4SGebt9EdpOSj-u2Ais--hYH9hku3AOaWc4bSwJjWw2ehTby_FLEQkBTVc96v-Po3Xg6m4dXZ-1bi-eauoX4mhWrVd5v_A-CCBmjbJo-dwrduKwqA10jhJKYHU6iEq9X7QM78f9Y6v8xgW2BEChJJs5CUwuEY0Q5VyhH3hGmVpxni4oVyWOuvYfeA5Wya9Um5hx1ZhnXujx6L0ez8IzPghv3JKo5LmXFLh95EjcFjZnN1X8m2mp0Kaep4-02-p6YOUz8WEY4Yc2uSHQE052qPhKNZIfVHeTOmvZsszIZAbdXdatYezf9anHJoqD9oAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دقیقا حرف ما هم همینه. میگیم چرا وقتی حکومتی که 47 ساله داره دروغ به خورد ملت ایران میده رو, باید حمایت کرد!
🔴
تا وقتی که به مردم نیاز دارن صحبت از وطن و ملی گرایی میکنن و وقتی نیازی نباشه بهشون به راحتی پشت پا میزنن.
🤔
حکومت دیگه چیکار باید بکنه تا عرزشی جماعت بفهمه که بازیچه یه مشت شیاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128489" target="_blank">📅 17:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128488">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dd7a8dd9c.mp4?token=UpsP60xlqCzuOACic9FmijizfRRID5xngHg66dkoJl8fOpbdchorVGNiC7UtW2xsQlJN8c3JHtKaAQxu7HSPWjoW7jg5ZK4qpIo7L_jsaNTatFaawNlYEHFPtFrzRkhJP1Cwf1m_XVeGnlhjKq4UPCwHrwyca5vFonhh7E1DYNtyJEFNFxy4Q2wYlcnjvLMZElcIQPqMRXDBCKmLV09GoqAiQlRTlNHoldBirNEYvuj9aFPtQJI8Rx7AJtc8Prj0Cjb7D3kK6ay-6fKrI42CzxeShIRNkxdLsQnDZWI0O-WwxuZ6ZL_bo7ZIxM7DrcHl-TfsnYTybiHjqQZr4gojyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dd7a8dd9c.mp4?token=UpsP60xlqCzuOACic9FmijizfRRID5xngHg66dkoJl8fOpbdchorVGNiC7UtW2xsQlJN8c3JHtKaAQxu7HSPWjoW7jg5ZK4qpIo7L_jsaNTatFaawNlYEHFPtFrzRkhJP1Cwf1m_XVeGnlhjKq4UPCwHrwyca5vFonhh7E1DYNtyJEFNFxy4Q2wYlcnjvLMZElcIQPqMRXDBCKmLV09GoqAiQlRTlNHoldBirNEYvuj9aFPtQJI8Rx7AJtc8Prj0Cjb7D3kK6ay-6fKrI42CzxeShIRNkxdLsQnDZWI0O-WwxuZ6ZL_bo7ZIxM7DrcHl-TfsnYTybiHjqQZr4gojyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو تیم رسانه‌ای هیأت مذاکره‌کننده هسته‌ای ایران :
🔴
مدیریت تنگه هرمز دست ایرانه و تصمیمش رو هم به کشورهای منطقه اطلاع می‌دیم؛
🔴
برای این کار هم نیازی به تأیید یا اجازه کسی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128488" target="_blank">📅 17:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128487">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZSG5EjF9e4MIeZ7BMHh4zABJEa0zTCOKk_5TgCAGBJ3-oExE1YUe68b8oHRafS9O4PL0zTNEKJk73n7p2ClnMR71qu8meOvgjIMoiLwbzFfe6o0rpN9I5-jstQv8LYOZCRxWUUf4IHtNb-c1YCLTTi6FVWL49BxZ6pCas1ILW0o19GqRPQ9wNTlYZvKYAf8Qt6f1GExol70GZ6s1_xB3fWyJcAPtLf7dv5h_9adREdRTDhDunBUQieLRkhSUiLUFJ-vZuJ3NxjCgaQLfRCqSkAQ9Fq3i9h081r7qDBHIYbe4kPzffCIP16UeXp2G5X3QP3qupMagc41COjawOVjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه های چینی تصاویری جدید از جنگنده پنهان کار J-35 را منتشر کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/128487" target="_blank">📅 17:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128486">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9727a3ae46.mp4?token=aQewZzN64hjCCIOqLc-avcG6nzd2uMV88VKUwgT1sMcZ2_zU1fmWe7hxG5giWmjQ59IEsLDhbv1pcDCIfIIWecKhLXbunm1DvUAq0Ia_4Ejv0iHHVCt-ZSLTlDozeatvS_iMi_jeCbW_4hI3h6kYTYCJz4xhHweJfPyZggAJdUxrd-VEO0zaCoMs0miUUl9L-hsrJwvSihrzOYd5N-BKrVNeDvR7VNRLhl34i9O5fItrQLFabZCqEe4qMq04PakDvxw1MTwgS-GqHHdtnAqmGyZjMJn_leOXLuEP7Y055Yi-f6G0eHhzyZGRTQhlcsbyDPwlyQ6EYaTZxaIiX-SKcnXqf6mTA3GIlo15IDmr8mfyqrC8_YYilco2-b2bKgOlENwPBDUg3bq1TtoZIIXU9Vy3nZ8P3D542v0tx27Q5LXo9ToqnTul3hoZLbwcBfHOOvaSaXUgyW7dZZmwBcY2Bv1SCRFM4lKlO2nBGozOOwRT_isHSvpvBOsMwIDpuQWfGk-ga3oNrJuA4rt5F7Pwp4ssH2RwnRODFJFTDsHJhL6WXxzrt6hD7jT5q0gHxJ0dgK3GNOsG0LYYCxEZntm1Ncmi6xDtScH8XEaxcUELH3XPKHT6JYyLS8D3f9m1BolzUgTDS29u5n7Da9Leb9Ub5GYGyyhtCUBwNKZPurMGN3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9727a3ae46.mp4?token=aQewZzN64hjCCIOqLc-avcG6nzd2uMV88VKUwgT1sMcZ2_zU1fmWe7hxG5giWmjQ59IEsLDhbv1pcDCIfIIWecKhLXbunm1DvUAq0Ia_4Ejv0iHHVCt-ZSLTlDozeatvS_iMi_jeCbW_4hI3h6kYTYCJz4xhHweJfPyZggAJdUxrd-VEO0zaCoMs0miUUl9L-hsrJwvSihrzOYd5N-BKrVNeDvR7VNRLhl34i9O5fItrQLFabZCqEe4qMq04PakDvxw1MTwgS-GqHHdtnAqmGyZjMJn_leOXLuEP7Y055Yi-f6G0eHhzyZGRTQhlcsbyDPwlyQ6EYaTZxaIiX-SKcnXqf6mTA3GIlo15IDmr8mfyqrC8_YYilco2-b2bKgOlENwPBDUg3bq1TtoZIIXU9Vy3nZ8P3D542v0tx27Q5LXo9ToqnTul3hoZLbwcBfHOOvaSaXUgyW7dZZmwBcY2Bv1SCRFM4lKlO2nBGozOOwRT_isHSvpvBOsMwIDpuQWfGk-ga3oNrJuA4rt5F7Pwp4ssH2RwnRODFJFTDsHJhL6WXxzrt6hD7jT5q0gHxJ0dgK3GNOsG0LYYCxEZntm1Ncmi6xDtScH8XEaxcUELH3XPKHT6JYyLS8D3f9m1BolzUgTDS29u5n7Da9Leb9Ub5GYGyyhtCUBwNKZPurMGN3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی ایرانیان کانادا(با پرچم شیر و خورشید) بعد گل اول ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128486" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128485">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e6d8a076.mp4?token=r6X-7y_OFW2AP5w-7DOH6tswSRdOWfYBfEUPrTi0YxzLvr18Lza38Ou2CstUoyDyeYhlwIH_2PZbW9SOUU-1S7ioCoPfoVsZxHO7HwV5Gy77Aj-aWufVN3ecZ3SbqWgLBOxIN2cbJ4IgaJnGrfWdDd198SPopCWGww4y-4-S8Cs4-fTFo8cseXO5SIfccUHJccWiAqa_Izbh3hokPSFMZYhhKQ3_Mx1r_tbiDOTwYECMVw0YQr1z7MPaplyU1Cucj0fVNItAu6eGd6y_ZaKQAz47KGAnJS-RgYyJ5a8qv6AY9lOQcNGEe9YuPjoA6vmj5z8EcN4bAwbcLWa8IEIvJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e6d8a076.mp4?token=r6X-7y_OFW2AP5w-7DOH6tswSRdOWfYBfEUPrTi0YxzLvr18Lza38Ou2CstUoyDyeYhlwIH_2PZbW9SOUU-1S7ioCoPfoVsZxHO7HwV5Gy77Aj-aWufVN3ecZ3SbqWgLBOxIN2cbJ4IgaJnGrfWdDd198SPopCWGww4y-4-S8Cs4-fTFo8cseXO5SIfccUHJccWiAqa_Izbh3hokPSFMZYhhKQ3_Mx1r_tbiDOTwYECMVw0YQr1z7MPaplyU1Cucj0fVNItAu6eGd6y_ZaKQAz47KGAnJS-RgYyJ5a8qv6AY9lOQcNGEe9YuPjoA6vmj5z8EcN4bAwbcLWa8IEIvJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‏در اوایل سال ۲۰۲۴ بازیکنان تیم ملی‌ کنگو در یک اکت اعتراضی و زیبا موقع سرود ملی کشورشون برای حمایت از مردم و جلب توجه افکار جامعه جهانی به کشتار هموطنانشون این حرکت رو انجام دادن.
🤔
با تیم ملی جمهوری اسلامی که خودشون رو ایرانی و وطن پرست میدونن مقایسه کنین. یه مشت شیاد خون شور
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128485" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128484">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a279890145.mp4?token=JhuSJAIxAVn7U9D-B7sTnSw4mZd3tgr6dVSsyz8bKwxoXm5C6Trgi9ATArpRxD_2Svzp-77GFuV_kFyxPVCU3c73Ee5NUww_FXAQIli1o7wzyKLgLduqeMngljY9RUnFpFoLLT51q5aseBzLWwASQn7sXYjCdPhiOJOGxw3iHMDCl3THw88xIvc3H06yIvUH7njEmuo4kbTh5cc1oS_NBpDBT1oezOmY_gxQrdw-r8G_dXblKDO1iUSQDDLqpYfpxl-7fpdeP52KgCh59g0K2PkhJr0-WnBPABkRTsI9Yv6Uu9NdZayLxBFmYJBwOBZS4UEjloFr4jYRSLxLQ6ouvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a279890145.mp4?token=JhuSJAIxAVn7U9D-B7sTnSw4mZd3tgr6dVSsyz8bKwxoXm5C6Trgi9ATArpRxD_2Svzp-77GFuV_kFyxPVCU3c73Ee5NUww_FXAQIli1o7wzyKLgLduqeMngljY9RUnFpFoLLT51q5aseBzLWwASQn7sXYjCdPhiOJOGxw3iHMDCl3THw88xIvc3H06yIvUH7njEmuo4kbTh5cc1oS_NBpDBT1oezOmY_gxQrdw-r8G_dXblKDO1iUSQDDLqpYfpxl-7fpdeP52KgCh59g0K2PkhJr0-WnBPABkRTsI9Yv6Uu9NdZayLxBFmYJBwOBZS4UEjloFr4jYRSLxLQ6ouvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: کلمه به کلمه متن توافق را برایتان می‌خوانم
🔴
من نه تنها آن را منتشر خواهم کرد. احتمالاً یک کنفرانس مطبوعاتی خواهم داشت و کلمه به کلمه آن را برای شما خواهم خواند تا مطبوعات آن را به طور دقیق پوشش دهند زیرا این یک سند بسیار مهم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128484" target="_blank">📅 17:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128483">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkJDCNhr-Wjlg7OL5OJgM3twaHPIu_IZvDW0UkovASM-hR9eN2UVeXi-iNcn947YhJserelncIb78EJK43WCuiwCVZQ-gZwlQRR5HWCo2toXngYPGZAZs5fqB5ZijIezq5URLRR0ODYaz-8t-3r3xclOQDFXX4uFLWOL5JfvyNVeb3C4BoD5ewmwnzNn4QQ97UlArwCNnhkvgwjl7BM1hqJfCKUlljqw9DR-27uImyZW6IKEsnHLTyLHXr1YTFsndxWcvtUweQDtLkTOTjDKK4G_xLu_uKAmCKX8TlxZw-PIf29GNs9MKEDY6FOFFyBgt0vGjYDWZid8GdREDU-HNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش ایالات متحده قصد دارد یک انبار دائمی و آماده جنگ برای سلاح‌های نیروی دریایی در سواحل جنوب شرقی استرالیا، فراتر از برد بیشتر موشک‌های چینی، ایجاد کند، طبق اسناد مناقصه و اظهارات مقامات به خبرگزاری AFP.
🔴
حدود ۳۰ میلیون دلار در ساخت تأسیسات ذخیره‌سازی در مناطق روستایی ویکتوریا سرمایه‌گذاری خواهد شد تا سلاح‌های نظامی آمریکا در آنجا نگهداری شود، با هدف بهبود واکنش نیروهای آمریکایی در سراسر منطقه هند-آرام.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128483" target="_blank">📅 16:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
یک منبع ارشد حزب‌الله به تلویزیون العربی گفت که ایران به این گروه اطمینان داده است که یادداشت تفاهم را امضا نخواهد کرد مگر اینکه شامل خروج اسرائیل از لبنان باشد
🔴
این منبع گفت تهران خروج را شرط لازم برای نهایی کردن توافق می‌داند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128482" target="_blank">📅 16:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128481">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7a9z-MXWiDUtS_uWALrl8o_p23BhNPQCUQZXSB-t6THWocmLu-EXP3MmGWejAVGg3cL3oSMPD0560vvGPIBDNwImA_VnqB2zGMvX0sFa7hNuPR0BKtzEr75F73bqOO52StAXL62mruQ2tY_IKraZzh24fHwL5yW0Orz4x8daSwD9uZtGkxyNoaLrhd3ql6Xby8xVN33WyKZokhGd4yAxnw3Z8hclPn70zkzfiQkEDEGUu9moVmK3Dijpf0xQQOHLsOlJ-1JGf6P2hj9WEEu2VD3IfjtzDVzesgA0CchPP3OBKKLnApPx3fIJ_0SZC1i1ZYezcQl2ddflvQs43_h5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شب گذشته ایلان ماسک ۱۶۵ میلیارد دلار سود کرد و ثروتش به ۱.۳ تریلیون دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128481" target="_blank">📅 16:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128480">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اسرائیل درخواست دیدن یادداشت تفاهم بین آمریکا و ایران را داشت اما طبق گزارش کانال ۱۲ اسرائیل، این درخواست رد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/128480" target="_blank">📅 16:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128479">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ در مورد توافق هسته‌ای با ایران:
این توافق در مورد یک چیز است: ایران هرگز سلاح اتمی نخواهد داشت. هرگز.
🔴
بقیه آن، صادقانه بگویم، بی‌اهمیت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128479" target="_blank">📅 16:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128477">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: توافق با ایران را برای بررسی به کنگره خواهم فرستاد
🔴
ممکن است به زودی تحریم‌ها بر نفت روسیه را دوباره اعمال کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128477" target="_blank">📅 16:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128476">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d2b0a36c.mp4?token=VJDlsFZscNNw4-T2vL03T6W2zUsH_GUn3tOAVYcr1vyrzOFtUBT71hNs1U7RiIw71GbE1FXhZr4KWTXdwnmezY5NnWWgJTMQzZ9Baoox92uWL9KFeQf0HytYDS78pr-FwD0gfvpzRQS2FS6Q30XzVSMDtFmBrvUxWkb45RRVmT3JJABNnTX-doVXsf-jhCcDwcgYzzk-c0oIIAFs3Hzs3m3ZMKmt5ixRYkA-ktrjznueqQhSf4WuY6xRZ8mWR-CA3WrB6ZnhbzOgt-2G8pWC8Le7yyOxfyfK42vlIqZtiXeH_sVQNQQtLUNFuaM55t4mVmA7WyuhaAhblui710jnfGr1SXbbdJiuM8OEiUuTbDW02lIxF46mXL8zy1s3EszKHuOTtHAZmpvPa0fxq4-Q115fAOJenUraxmTg0szx_gfgV2SmYCFJcKfddCGKviMBHVn-xlA2xNmofgF1ZxpQEYtqlaaBa1jSfsOy-oFkYuIja9FxK6ogvb8LJ-UhTGbpQiGTSn9nSMMFGcLZ5rNMtBW2-gXAy5-4pCJToUPL7K4qQC97XDO_RQXTb8hh6SeLd9fOWtMKV1fGcOmsuw5eQk-sl1h_nCX49lXJlOX_4Vyu55Dl-3h6bmYATlR9dq6ph09tE5zL5yrDP8wd-UEzVHpe_PfRxar8dTxTzppwRrc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d2b0a36c.mp4?token=VJDlsFZscNNw4-T2vL03T6W2zUsH_GUn3tOAVYcr1vyrzOFtUBT71hNs1U7RiIw71GbE1FXhZr4KWTXdwnmezY5NnWWgJTMQzZ9Baoox92uWL9KFeQf0HytYDS78pr-FwD0gfvpzRQS2FS6Q30XzVSMDtFmBrvUxWkb45RRVmT3JJABNnTX-doVXsf-jhCcDwcgYzzk-c0oIIAFs3Hzs3m3ZMKmt5ixRYkA-ktrjznueqQhSf4WuY6xRZ8mWR-CA3WrB6ZnhbzOgt-2G8pWC8Le7yyOxfyfK42vlIqZtiXeH_sVQNQQtLUNFuaM55t4mVmA7WyuhaAhblui710jnfGr1SXbbdJiuM8OEiUuTbDW02lIxF46mXL8zy1s3EszKHuOTtHAZmpvPa0fxq4-Q115fAOJenUraxmTg0szx_gfgV2SmYCFJcKfddCGKviMBHVn-xlA2xNmofgF1ZxpQEYtqlaaBa1jSfsOy-oFkYuIja9FxK6ogvb8LJ-UhTGbpQiGTSn9nSMMFGcLZ5rNMtBW2-gXAy5-4pCJToUPL7K4qQC97XDO_RQXTb8hh6SeLd9fOWtMKV1fGcOmsuw5eQk-sl1h_nCX49lXJlOX_4Vyu55Dl-3h6bmYATlR9dq6ph09tE5zL5yrDP8wd-UEzVHpe_PfRxar8dTxTzppwRrc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره گرد و غبار هسته‌ای ایران:
ما عجله‌ای نداریم، اما آن را به دست خواهیم آورد و نابودش خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128476" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128475">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bf48e1e56.mp4?token=K4rdrTOeh6GJLdBLNg6HsCQLF26UN8HSlX9dojBq3gt1hv8qag9ouERLnAU7iIQe5TYni1zXDbGVSYeRS2x66FZBEtjgkbzqmCS1J9oJBb7_JK6btrkXn2i9nDsDzHLQ8XUuEYZuEQ9mFya7KpoG2fhln85-MDo24FrXqOqqjxVJsIZe8u8uwFpS9YLcszSvcw342M6uIiHh87sMesKnliUALMTdGndh_qJ3D6sXeHGpV9emhjwFxJGsTlwyCa4ZrZ3vYsJgWnXbHXqQGyzXJQUBy_Ob9HHbM3uZhgSb59tPLuVifTnEICT7EJKHM7RShTXRHvwM4ABE_T9QNJ-RQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bf48e1e56.mp4?token=K4rdrTOeh6GJLdBLNg6HsCQLF26UN8HSlX9dojBq3gt1hv8qag9ouERLnAU7iIQe5TYni1zXDbGVSYeRS2x66FZBEtjgkbzqmCS1J9oJBb7_JK6btrkXn2i9nDsDzHLQ8XUuEYZuEQ9mFya7KpoG2fhln85-MDo24FrXqOqqjxVJsIZe8u8uwFpS9YLcszSvcw342M6uIiHh87sMesKnliUALMTdGndh_qJ3D6sXeHGpV9emhjwFxJGsTlwyCa4ZrZ3vYsJgWnXbHXqQGyzXJQUBy_Ob9HHbM3uZhgSb59tPLuVifTnEICT7EJKHM7RShTXRHvwM4ABE_T9QNJ-RQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره یک خبرنگار اماراتی: چه آدم خوش‌قیافه‌ای. آیا او از کشور شماست؟
🔴
محمد بن زاید امارات: قطعاً.
🔴
ترامپ: او رفتاری بسیار دلنشین دارد. مردم من خیلی بدجنس هستند.
🔴
محمد بن زاید امارات با خبرنگار شوخی می‌کند: حواست باشد حالا.
🔴
ترامپ: می‌توانم همین الان او را در یک فیلم بازی دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128475" target="_blank">📅 16:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128474">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18495babbd.mp4?token=DwLAeeEVc9s9D1NMskxd66GUG6AK4dBy-rvkmlbV29ueA4f2-9CzX6D3nTYBAYc7B8cS6fSm4nYvOt8LMfVP-kF-6xmIoGsPeVzBMmnO48NBlYtGGZEgB4BWkdd3oucbVXLiW-PkQPwRyPVCjG2jaszCW39BlvyQL0CsdgxmHDEt8aYFU9a-a9SSgeDJX-YCvKvgEwHi6DfQJ3VCE3Ib9v2_USMAcKsSNm4HPBCo-4-KaawcEdgLTs_DXWtvbstNhJVGIaH9FcbL1q4Fzr4kyLXNhlNd497V2RM3R9-JZ5jwEbZmePysjRlTO-mOwfpdAGE0vQrghX6ELEyQl93FiChACWJtEJAJqyNGBdMoc3S-zvoUuyDy2siG3kKekSsfh3yC26NjqSZFWMs-pTqcqbWjN5rD0lV5HcZPEVkiUlP5BnUkYGHYJUNa73eVKSYBmJ0xoOOlS6Xy8W3rP3bVdZjaVHWYhqlvH1iWQMdHvTNpFg7DcAC7WHDO8h8MX6E45D3Gjtyv_z1Ao8MTZu7lSW-8_iehFZtlZvtZM6-xrB2wA2bPRizzYrIxCF_439x7CMZd8Gx6Be3b96u537oaVMggDqUtTz-hISW9tOp4ho_fO5uevWiLOwLOROycITb9ftoL9p8urXyLKUzOuy8deELL7VxmdNYxCtE9N-qpbUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18495babbd.mp4?token=DwLAeeEVc9s9D1NMskxd66GUG6AK4dBy-rvkmlbV29ueA4f2-9CzX6D3nTYBAYc7B8cS6fSm4nYvOt8LMfVP-kF-6xmIoGsPeVzBMmnO48NBlYtGGZEgB4BWkdd3oucbVXLiW-PkQPwRyPVCjG2jaszCW39BlvyQL0CsdgxmHDEt8aYFU9a-a9SSgeDJX-YCvKvgEwHi6DfQJ3VCE3Ib9v2_USMAcKsSNm4HPBCo-4-KaawcEdgLTs_DXWtvbstNhJVGIaH9FcbL1q4Fzr4kyLXNhlNd497V2RM3R9-JZ5jwEbZmePysjRlTO-mOwfpdAGE0vQrghX6ELEyQl93FiChACWJtEJAJqyNGBdMoc3S-zvoUuyDy2siG3kKekSsfh3yC26NjqSZFWMs-pTqcqbWjN5rD0lV5HcZPEVkiUlP5BnUkYGHYJUNa73eVKSYBmJ0xoOOlS6Xy8W3rP3bVdZjaVHWYhqlvH1iWQMdHvTNpFg7DcAC7WHDO8h8MX6E45D3Gjtyv_z1Ao8MTZu7lSW-8_iehFZtlZvtZM6-xrB2wA2bPRizzYrIxCF_439x7CMZd8Gx6Be3b96u537oaVMggDqUtTz-hISW9tOp4ho_fO5uevWiLOwLOROycITb9ftoL9p8urXyLKUzOuy8deELL7VxmdNYxCtE9N-qpbUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: سناتور گراهام همچنین گفت که توافق نهایی با ایران باید برای بررسی به کنگره ارسال شود. آیا شما این کار را انجام می‌دهید؟
🔴
ترامپ: هرگز به آن فکر نکرده بودم، اما انجام می‌دهم. برایم مهم نیست. یعنی، می‌دانید، دموکرات‌ها — می‌دانید، ما به آن‌ها «دموکرات‌های احمق» می‌گوییم چون آدم‌های احمقی هستند.
🔴
خب، چیزی که دوست دارم انجام دهم این است که آن را به کنگره بفرستم و بگویم «نباید آن را تصویب کنید»، و من آن را تصویب خواهم کرد. هرچه من بگویم، آن‌ها می‌خواهند برعکسش را انجام دهند. به هر حال، برای او خیلی خوب پیش نمی‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128474" target="_blank">📅 16:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128473">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea5ead7bb.mp4?token=BW-WW9SxxskB3YrbvRqMVLxJBoCspFb5gTCdHQtdvb4YQ0YS8nutnk2PkLLEAV21JSVj_jUOjhXKg3GALVPc48FUa_leF3XN3LD62KX5m87VjSHmvLVh33_07I4XiHIYa6pcoTLW6h-tCf1LlW5opUwRdOZWqunf6lM-ss2HgrDwWXWI2GINrKJ_6FL5V0NTrh59bB2kl7kypBz8FcbIoa2eKXBsaLS97QZ1LfXTLR-izsUn-YZzX9GgJuAMweI9SEOmKs8KpfnbZziLBWUX4OMNJmXb7rNFUvVgTtVnKQ7gTZ4IRjz47B3GXvimSiEOG9hOPzmrpUDDU1-8IN4K_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea5ead7bb.mp4?token=BW-WW9SxxskB3YrbvRqMVLxJBoCspFb5gTCdHQtdvb4YQ0YS8nutnk2PkLLEAV21JSVj_jUOjhXKg3GALVPc48FUa_leF3XN3LD62KX5m87VjSHmvLVh33_07I4XiHIYa6pcoTLW6h-tCf1LlW5opUwRdOZWqunf6lM-ss2HgrDwWXWI2GINrKJ_6FL5V0NTrh59bB2kl7kypBz8FcbIoa2eKXBsaLS97QZ1LfXTLR-izsUn-YZzX9GgJuAMweI9SEOmKs8KpfnbZziLBWUX4OMNJmXb7rNFUvVgTtVnKQ7gTZ4IRjz47B3GXvimSiEOG9hOPzmrpUDDU1-8IN4K_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: تنگه هرمز باز خواهد بود و همیشه بدون عوارض خواهد ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128473" target="_blank">📅 16:11 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
