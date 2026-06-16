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
<img src="https://cdn4.telesco.pe/file/kKowCpNPJWYoPs0AGJhnEIXmHNELLZlPiz0xaPkmljxdzBYOsJWZAQuSXVHvxEwxB9wKZYLUeSr0V9ZIsonXBhW96qZcUiQdWExkajDCU-GHlZjD2orpfmOLfXTJdd7Q1vQQetV_UDt2XTbHLVGOsPOCXSWPOhC77x028mFdEFnau39T8j5xtxiLJjAyL28nGMbZ5Pfv9S73fcFkl5UnfyZMYzoXLJob1uPLm9E_lU0uS986M23m6Ezn6icD0YSlf3nYCo_t9y4quvIx81VAm5c3WiaLR7DQ8NO9FyVCHNDNA4ksRSzHjEgS9HOOsy4djnDTRkiwxsypqA89N3MUaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 21:43:22</div>
<hr>

<div class="tg-post" id="msg-66319">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUnZvHqLex3OsEzFq3uqVkGTQ3Y47oNabE926BKr4XFV5Z5UJZKo7UIL7kca-mFU0U426r-719nd0ozBJQ7bBg-8g3KanyNuyFoNNOXMo-HIwH7ZTRTbi_eQULoI9Tz1A8eZBE8oTrfmuMsfhz85nuNraooC9yyH9zPZj4LhrhxhAX13vZXQHWI2Jf-5x5YnYLHUyOvJRRRkobty6mr-l9Lzi4BhsA4RFiB1icLbDvAL0h6vfa44EZQjOxn0Zixrnu46AT6OWYfD5E3f05aQZdy1_I0p0Q55ot98wZ0487PEr4VgUQ9FZwSug1d9WgM_fS9iGKmesCqJ5FtZt3ubFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نفتالی بنت یکی از نامزد های نخست وزیری اسرائیل در انتخابات آینده:
توافق فعلی بین رژیم جمهوری اسلامی و آمریکا فقط یک توافق موقت است.به ملت شریف ایران می‌گویم که امیدتان را از دست ندهید، جمهوری اسلامی رژیم فاسدی است که سقوط خواهد کرد. نوبت بعد که مردم ایران قیام کنند ما ابزارهای لازم را در اختیارشان قرار می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/news_hut/66319" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66318">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837293596a.mp4?token=N74ucms-Vbn5QGya8AsEME6yLP6psoi1r3QygyhrX5r7Xv_CChK1X9sLi9lq58bkZPWxAwdgRRjlhql8LITiUGPiqnitXBbtUwSPy1WIlzGSPuOJSe_a1bRK0pqB6uH9z3kcB51MN4liJOFbitOvzFcp_IB2Ha2Xgbo2RIzRwyH4V5RHF7sl2Zkawkd2buY_dMUrBRmTpzCA8-daQNzMKFzyub-xDBe-0dvrDlTrOcBPV1rHQ7d7rh2SThA-Vwrx878StGaHZveYukmKe9bIrT74S0EUjSqVMhwLvqgzHja2q2WQ5ibAlwK8cIeRGZvXZNk7FdURz7CWWe9QzrtRyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837293596a.mp4?token=N74ucms-Vbn5QGya8AsEME6yLP6psoi1r3QygyhrX5r7Xv_CChK1X9sLi9lq58bkZPWxAwdgRRjlhql8LITiUGPiqnitXBbtUwSPy1WIlzGSPuOJSe_a1bRK0pqB6uH9z3kcB51MN4liJOFbitOvzFcp_IB2Ha2Xgbo2RIzRwyH4V5RHF7sl2Zkawkd2buY_dMUrBRmTpzCA8-daQNzMKFzyub-xDBe-0dvrDlTrOcBPV1rHQ7d7rh2SThA-Vwrx878StGaHZveYukmKe9bIrT74S0EUjSqVMhwLvqgzHja2q2WQ5ibAlwK8cIeRGZvXZNk7FdURz7CWWe9QzrtRyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند اگر این کار را انجام دهند، عالی است. اگر ندهند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/news_hut/66318" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66317">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان جبهه اصلاحات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMHTwvGauQlvqmS2JROyT3KRPuC7V5dOKsYOgMneceIC_COmGhEl_hkU25ruQZLmDE_O7ZUhoxDk4pFR2X-l_-7Faj8mx1vzVRlqw4AGl2kD55Rd6dWVdjvF1Ru_9Oo-Y-wIy7sky6VPgQvB2eIFDIOsEK4o6-1BJsi8lHqknwV11r5EHbKVi3KTDCN6nD9hjrSZYowQB4ZCRhAOahIrvubT7olswhMZkOBGxB3Re14CeMZdIABebT3XXHXSlOq585zGjVknfVRygAuKpzbcXAJt9ZjuW6PkSHtdLXoJzqQwFMdWpQfaza472_Hn_LfJcKqPbMCriX2cwQ34OxDBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح!
@iranwprldnews</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/news_hut/66317" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66313">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDqBYpUrx2D629fdBomvu1fNPtXIaIBxIMohCXHVFuWrluUiXrdBIcLreWqyVuQshsvzNO6T0UmdEPvbTJuIpRIfV_L1Mi_T8H7jV6u3z6cEM45OOotqAsprntU51zbWM8msVEAnf8wW3d4UEMNPL0ctEtFCbJukwYRsyp92z3QL4QswoDkFc9jhAk2RbJxjA9q4CY38guO-sOAtBIgdGlY7pQmseYOBGeOGrqiZMZgvBGEOmFjkR6iUADVzA9_EygpAOVbLIG3eBWjP8YHHTsfs4AVqOmvBC8dmCi4VhDQSW-v0w-NiWvegE-WPPUNvG8UxiUfPWvgHWx9WOz157w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
زیر نویس شبکه خبر:
حمله پهبادی اسرائیل به دو روستا در نبطیه در جنوب لبنان ۴کشته و تعدادی زخمی برجا گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/news_hut/66313" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66312">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9Y4oaiyMjXIaVQgchuwCTdPHiYFkFOWPthXbQ-1LHSB3H_sk161u9wPtYeouh_z8VsG7B9R83ggVJfuSkfdjJd8O00Fuy-anZECDQOMP2Nua3fc5fDjliVeK6mfzU6Dl2dN-pzrWTQjfR7Gmo1hNlXU9kq-joi3SZ0cIo2wdqmGJJvCFq9vKsBXVL8gjp3RwCJURpu76AKC5F572sOxMWZdCqkKOTKGQt0HZqlDhzk3x-4cT0ntrRt3dddwQBlZrRYWOtpKu5BFZP09nkDpjAOA3djBYD2Jn_6wz1VaSEiTpj5flKV7omSFYlM7UmlWAsZKlng2zTATmkCvTMDWYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل:
لانچری که به سمتمون موشک شلیک کرد رو هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/66312" target="_blank">📅 20:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66311">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=ZUXV93mgLaPTK5GprjFd3ZDk8eo7arbYhipqC6_uSx9vLxw14Eopo5CmqSxsoc7gm6m3APmnWED0G91NbOLnwd8xsqLG1Ww-op0mkHCEj14DHsDbz6q_eYKwmP_3mWuU8W9SbMqgQ8ljOKt5SveTEchrrjOju7yUtqeqao02hIOXs2Ao_LeqIaYvEq6NPfi_W3lO4edmEBYEAUAgNQjzHgja7YjWT1SaeaMzj2Uvj28daW3v8zKFuXIMOf88LyWSxUsHhKkrWTaGJa33bfca0-s5i5zLO3vaefgxWFMr36vnH-v1uyAynLLiYWOwArmZaW6RcYt2UbzMd9DdyovyqFn52ag8fRcW_g_kNahY4qLzud8oPqXusuhCSXo_htYdo_mSIhzQOohwifVX8xd1cIn985fFPED2ozhEmo5EgE-g1kSn9y_BDVW-lspvw7VrvHpyn2nGshkNcvw6UfmH_-3OKBO1PXLPb08BhHK91zUohKihs_ex5yqgdmdJLFFuTYYex-nYncR-UaVqrqqMqYS9Rg7kAti_R1q7i9x0AdZsNQfEhAxazIvSFv_Yx1AzXIKfD4vcRVHXK-03I5wz2BAX4KjbMffqsQhXU-nV4lrz9YgQ1e1B876Z3XH0EskeTkl_NjghF5CE6uYjq3HL-Ul-zW2esTzAhzwwxyqJDwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=ZUXV93mgLaPTK5GprjFd3ZDk8eo7arbYhipqC6_uSx9vLxw14Eopo5CmqSxsoc7gm6m3APmnWED0G91NbOLnwd8xsqLG1Ww-op0mkHCEj14DHsDbz6q_eYKwmP_3mWuU8W9SbMqgQ8ljOKt5SveTEchrrjOju7yUtqeqao02hIOXs2Ao_LeqIaYvEq6NPfi_W3lO4edmEBYEAUAgNQjzHgja7YjWT1SaeaMzj2Uvj28daW3v8zKFuXIMOf88LyWSxUsHhKkrWTaGJa33bfca0-s5i5zLO3vaefgxWFMr36vnH-v1uyAynLLiYWOwArmZaW6RcYt2UbzMd9DdyovyqFn52ag8fRcW_g_kNahY4qLzud8oPqXusuhCSXo_htYdo_mSIhzQOohwifVX8xd1cIn985fFPED2ozhEmo5EgE-g1kSn9y_BDVW-lspvw7VrvHpyn2nGshkNcvw6UfmH_-3OKBO1PXLPb08BhHK91zUohKihs_ex5yqgdmdJLFFuTYYex-nYncR-UaVqrqqMqYS9Rg7kAti_R1q7i9x0AdZsNQfEhAxazIvSFv_Yx1AzXIKfD4vcRVHXK-03I5wz2BAX4KjbMffqsQhXU-nV4lrz9YgQ1e1B876Z3XH0EskeTkl_NjghF5CE6uYjq3HL-Ul-zW2esTzAhzwwxyqJDwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه ای که سپاه داره لانچرو برا شلیک موشک آماده میکنه و ایشون هم شروع میکنه به فیلم گرفتن.
واکنش سپاه:
😡
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66311" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66310">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66310" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/66310" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66309">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI4UiqLpnjwIYGCPE6SyqCvgeCCnTqcYtFuYGCOHeMjYlgHGBxwEkrhsUbJptZSpYM486I9mQSkqQhPfa2fY0IX1OLZGXjUKDYmxkGkosuoH5XMvS3YpIMQu-iStnDEZ3yfZNr2wFk52q0uEMdpxpm6BRazno-zzKAx5f-8ukGqlI99ag0AD4WKUtklyedfptFS2K5kmJVrMRgZXcKP5ELHUIHZFiLbkQrwqWb9iYl6ETstMmb5S-azr2mCPomQ2KpyMQ_TG27-3f_8OyZgVFzU8eSGQwVJX40mAScftYvBODeA7OzK0Du7jG_cEVg9RaYWKZimIxzFYBaVm28vBJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/66309" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66308">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd23rZ_Pik6bU2bSpDMlGfvf2BImaHBlN8IIoyqSExRTGgcToQ5MGchyrZxefEi0Mh6xlyzWcr_ZDsEcTYxduZrTqxWv_Ih44WeqnopaUFEDPU_VLEXJVRwKgr4CCtiRWR_YDe4QA_03EFQ21OH-ew-GEGTQ-ANS6Um5GrLk2gEhEyj4cI6LYt050uAoRvlZ-GK7jYC2AGA--pDI0hKBmq9O0mMOKj0tFFKZ6Lkn0x16uotlMqh1O_J6rOt1P-Wer_AtGitd8Mv3iUaFZldCX7hgEKRQyqLTLbPq35-2zwc-ABXUiEjGNnpBl_B0vq3ijG0a43rEvXWC0Z1TL-1DrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
اف‌بی‌آی یک توطئه تروریستی گسترده و چند مرحله‌ای را که قصد داشت رویداد UFC Freedom 250 روز یکشنبه را در چمن جنوبی کاخ سفید هدف قرار دهد، خنثی کرد.
به گفته مقامات فدرال، این نقشه وحشتناک برای "ایجاد حداکثر تلفات" طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/66308" target="_blank">📅 19:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66307">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCELI6vb_N_1uT_fBIlQ-F7p8IUVZqpaYnAE5HdWMXAoZ2KFW1wYkXZfLu9whd3YPyu-1Zw63d7ESerkql8w1_k-50R7IIPfOfr8y_YvOtzaflQlmhKQxSV4rMqnOCq8r2akMJkO4aUwNIraINtm6kyO_BG2xxNMfpgKWXsKfQOq1iL5BR--dl6T1TAvBy8c4TEvcZPcjdCbpkQIw6kgXOqceBBn2fcJEDl3QMqQeSRGj7U6LVGaQyJZ_Kjs5tl4-ZMZlXdkA7Nj3priC2UuebjpXjrdJKimbV1PyU_9PtfQRhG_YC6kCwrznhTniq9IY4vYcMX3ERz5jkIF_5LPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارتش اسرائیل، منطقه میفدون در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66307" target="_blank">📅 18:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66306">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=J-sfDDHV86HHxz4TDiDIz4IRRiK3tD8VbmhvFohZrxOB88EWPWLZ43qVnrhsRpfbAYPaYuGKY4jqjZAvSQt1wIqIJOop3dSkNen1qmbMIU8oZ_ouOvbPM9YDNySQxbNtt6HD_97n-1l7Yq8hvQI7TxJ9t3_-ow4LSpfHvHxJT1ARDkX9tNAbJW1BvqFRjMTOBoKULFJQ45jgyP1CS8fl5YZRDokRUX-pPukc6xJmStnDG1mTQB7FMSv9vhjC7HOpopnKrehGD-aOJSoyculuyM_-Y4FlFxXJdTZAJcd3FzfT94laWvc0VnJOda50nbEnss4Oss35nM0DYJzDW3weXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=J-sfDDHV86HHxz4TDiDIz4IRRiK3tD8VbmhvFohZrxOB88EWPWLZ43qVnrhsRpfbAYPaYuGKY4jqjZAvSQt1wIqIJOop3dSkNen1qmbMIU8oZ_ouOvbPM9YDNySQxbNtt6HD_97n-1l7Yq8hvQI7TxJ9t3_-ow4LSpfHvHxJT1ARDkX9tNAbJW1BvqFRjMTOBoKULFJQ45jgyP1CS8fl5YZRDokRUX-pPukc6xJmStnDG1mTQB7FMSv9vhjC7HOpopnKrehGD-aOJSoyculuyM_-Y4FlFxXJdTZAJcd3FzfT94laWvc0VnJOda50nbEnss4Oss35nM0DYJzDW3weXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
ممکن است شخصاً یک کنفرانس خبری برگزار کنم و متن یادداشت تفاهم میان آمریکا و جمهوری اسلامی را با صدای بلند بخوانم تا رسانه‌ها آن را به درستی پوشش دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66306" target="_blank">📅 18:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66305">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HooidtglM31xh8_nI9wG6J0Eq7zhzvIxSi6P02znIir6jRANnfYTSApS3i-QvRw5WA_xlSkw3pDPTNfFl5j8K0W2C6rGjN0EL8Y6PsPUWaMaQwoNKtUyJ1wyL-UHY6rntryUFLPc77wLiB0mHjvd8ZyCEumhc8lLBKZ0f6QxFPV8BeY-eiT0Qu-6gLM82VRdSAYPEXFJglKB_7PyI5ytcvUlTyUHkYWhMPUE01ugYxpFcjEWlOJKcBdEnMHkGEkkooJrq9k1bSV3dzklqyQg1wpUK-XpIzLOLtAxNE3Yz8qucIQsiiKucTjQLN_8JsegKFHqnru3KY6pUyqk7viXKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی رو پیش‌بینی کن و جایزه ببر
🏆
با ربات تلگرامی «نتیجه‌باز» می‌تونین بازی‌های جام جهانی رو پیش‌بینی کنین و جوایز نقدی برنده شین.
😎
۶۰میلیون تومان جایزه برای نفرات برتر
⚽️
تازه امکان دعوت دوستاتون رو هم دارین و به کسی که بیشترین دعوت رو داشته باشه هم یه جایزه ۱۰میلیون تومنی تعلق میگیره.
فرصت رو از دست ندین و همین حالا از طریق لینک زیر وارد ربات شین:
@NatijehBaz_bot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66305" target="_blank">📅 18:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66304">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqIadPe6qZRQM991yk1s2JNY7PD5PimCLAq0Swio3yoPSp0qdeWiDL2euBMPZQk3YVO7amrn7p9PZAEZCufTBKWeCLiQ37pdjeYzXmjz0yfbKL9WbTbhEcKZXfPhSP-MVn4lgP5n6uZ18MO_97UNQ_5lQEl6RCcCUARy3x1RFKOwjQfkZ_qn-HYDhbll11XvHZvsdhlcrSzwf4keZWPYl3fIL5M9v9m6PCODABzvNTGsNM9fZIZEBcZBbbX73wMjpxvYqOFkPCcJZm9rzcXej3m8O5Uy0e4j0ZOE6oyhZS3nhy1KxhqEZYm0yJHegSZC3NgOkJvFO7dCJRZt9Xn8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه سوئیس:
قرار است یادداشت تفاهم ایران و آمریکا روز جمعه در بورگنشتوک، در مرکز این کشور، امضا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/66304" target="_blank">📅 17:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66303">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7yrJ8xWw0XArHJ8YjLtK43RNTHsk0ZKpLs743zHoIBWQTJ64eIuR-vUOf-AfevLvH2b8nKmp9DLA68s39M0_CwHotsjP40ZUtTpPSIbGDoqGrNV-S7djPh1sHYkCffJIxWp2Em0Q5Loqc7fkM0-So_TzboMHNGKOyHQxjEHteChcNKE815WP9NGss0RMLyTT-ehaPiH04WzCWUa978HttnqJBU5ap75BH3JEGAjE_7mneos-NyU0g2j2sdbENlSsAnnLXyh_UWNhKf7e8ZV3iLPoOn6S5YVHjpPk49GWilvEap7PFL2sNzz8052LJCwsmnlqH0WWQXxpdULKAg4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر تیم جمهوری اسلامی که آمریکا و اسرائیل ویزای جهنمشون رو اوکی کرد.
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66303" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66302">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66302" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66302" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66301">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmAirgoDNld2Iq_A896Py7ykyRbF7zkm1vumxV3mo2pDhQn3_BiVUQ7LQk7fSvWfQqT57aKceRJP5XsPfJomFOPmjzmlFMpo6QpDVGboPeH_Gv46Aq1LXrErlZCDQBo-0rfk8JCHcS-DgWJYClXFSmjDtvTYEmCh0R3-vZCBhIRZhb7CT9tMWJda8ddkSfoFkG07yJHdJWs5YPXqLfYk2pw__2oy6bsr9NioBlwagmPCMlgYOLBIjwxdSlAFZxmc_unH_R0fDLhTyLcos1S-boNcNdxR1_io5TAY7ip_iPwfR1IRfEigM6dGlHNjFTkjpCCSbKap5QodtpUrMDr3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66301" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66300">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=JOsZ8PDTM9aJ49nHRHG6Pik9--DiVxqhaYPuhfTd96wmmVEl4Mm_CnDPBV_Yciw8_RG4AI_pBUPOVUGwjfvRC89ZhPwrOvzwiZImbcCo0-9_0i2vaNMugp9apOWD5W0wyrEKMMcyqTLVJ62DKxNCjcKhKMtd9s4lzM9vuvSl0UXbnPZi7HSCHb5r-tWDszlyGB5P_nBa7RfIma1_aGrzxZG5Aao6qcjTmFOqqZz0T5n3Bxf--fcnlg2h1zhpQDKKkCIZtgfFGZD5TDciRSQ1PX5UkA-c_oG6f0vHS5UvNFe7-1voCixYvAf2CobQEbKL2gVvOHLZ-4ad-QWp2yrxZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=JOsZ8PDTM9aJ49nHRHG6Pik9--DiVxqhaYPuhfTd96wmmVEl4Mm_CnDPBV_Yciw8_RG4AI_pBUPOVUGwjfvRC89ZhPwrOvzwiZImbcCo0-9_0i2vaNMugp9apOWD5W0wyrEKMMcyqTLVJ62DKxNCjcKhKMtd9s4lzM9vuvSl0UXbnPZi7HSCHb5r-tWDszlyGB5P_nBa7RfIma1_aGrzxZG5Aao6qcjTmFOqqZz0T5n3Bxf--fcnlg2h1zhpQDKKkCIZtgfFGZD5TDciRSQ1PX5UkA-c_oG6f0vHS5UvNFe7-1voCixYvAf2CobQEbKL2gVvOHLZ-4ad-QWp2yrxZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگام بمباران بیت رهبری هرکسی که اونجا بوده کشته شده جز مجتبی.
مجتبی همون لحظه:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66300" target="_blank">📅 17:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ki0DX59vR3XXe9trvVz-SmBlgOCcT761CXZ_v41DmwCEgmpjwbxWL-GvKBoMRBS7ZUCKiml_OUUz8FhhwyJ5q1eizjqMgngQiILn_3kvn4M9fyXMOmgFOUsWgM7sEH8Y5Kh6iC8N1DLYCjTpTd7f40jssx52AvdBlsC_nW8sJOQJpZKwlUomb1Yy5trtQRTvhANTapL2yOvYwlldJ8g079VBPPs-ULr5Plo02AQZjCVziId10p_AO6AeP8Fc3HpIJ62zA2PlLAMXNudE-k_pK1WwYpN1D5Ydvs-0EaODL03-SFZCU1mXP3iLXbyJbqU0a4nSG06n3OrKNepb7jfA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TxYhek32LuzjOVTsrgGIOAOTBucu6as_bMr8gDenQ2PFcglQD1gj1tEZ5K-kKnM3dG824AqeP041zK6OSF6h2a7ZRz874USewEc754M3PqRLYDCnP6P3gXKkdb92JqTZ2H82PTOE9MGLKsT2xEQ3gQs_AYkGjBvcr8wjkZJP6cpS6WwsLH3lB1cFyLBunB_REwgptx7qnip77vespE-S48oRndl1w5v45YUosn9lKDORqqggRj2zxaJesnS8gxlBG3_gBhk4COHHSpGRXKqFqZLQ28HyTB_BNmIuVIaTylKc2M0k8doBc7Z2NTgFh8atNfx2pJEzB3El0j-1IMyxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZycVQmRxGkXKm7CXg7Ca1gmICLCTB8uNctC0KJ1Ml7U2aW1mK2fNtBHY9aSXsczk0UqfRDt3xoV1Mo06JsSuUocBtCukYyhBUsA7oOpPLRjEjR4BAW8nR2StrM3fQJXjLEWf1-qQ96dUl7gejRFxvriNCD02cJ2ImlEKOERkKtzpyiGNZkOw9oBtOxXjRBZsIwzVIWWO7ZQgp9m-GMwArZyEsdBgBgC82HZzOXiKqubar87ENuOg-BdDj6mVI_euqVBccqBt1FCgvPPni-FX1Nxg2ygy-PXCRH9cNGxex7-DOJVuvqNRTlsWBynxWoPPqOqDLkB6K9zarMB3njp7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsmEHCExZLsXGLDrE0khscKMLpGasy69wRUZDq7LL5dTsN3GlvUyBzdf3Q_Ok-HcD2_KG2zG13E_AHMxJd_r6zen5D0itHEYje8_6glw5FdjlSaB23I7pZzCDN7Q1cpO0voTL8XLSvyaP3AdkSleFwM3wWycDWRI3A8G4TgLsU7kp9VlKyCUf09G-QjXl99eDP6l2H_0ZPUWc5i92hR2hCckiveUMPLasB230Hyr5stBAGfMAqUFWFxJof3auTpvf2zasjoz-NSncI_g74JwZnNo5agRF_IRBHimOWy8yFX6XOfqi4F3kspzG3hOOJa1IrEfeaZBaPm6md66AQJfkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ویتنی رایت پورن استار مشهور آمریکایی دیشب در استادیوم حضور داشته و از تیم جمهوری اسلامی حمایت کرده
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66296" target="_blank">📅 16:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=fqQJ9Qhwz1B36yn5dzqLjStdLHzro4DfImDhtLUnPKQsFWYPDUbpjZ0xzlwOqq52DZI1g13vi1m-VrMsikouahvb5Buv0lqQwl_UVHG1lT4PJW4ssjaBvfywBL4FZg3h-YISj3bXaWLfftrOXvcSGfY-aSpq4Wwa-G-8S1nyeSi3uOMB07e5Vw7uxXSsLVGJwXwM7Ni0pwyNBEOP1d8aYKhBFtTykmz048iGZ75TmLHUUNCVke3ytJed7viwCF5oCBc2Kcc2HHWdRmfrGvXq_2TFcZzL31kisnT4REE2S3y8A9iWgUdIqGoORlDqFCJ1m4lQY1hmbAdF7w4ErMN45g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=fqQJ9Qhwz1B36yn5dzqLjStdLHzro4DfImDhtLUnPKQsFWYPDUbpjZ0xzlwOqq52DZI1g13vi1m-VrMsikouahvb5Buv0lqQwl_UVHG1lT4PJW4ssjaBvfywBL4FZg3h-YISj3bXaWLfftrOXvcSGfY-aSpq4Wwa-G-8S1nyeSi3uOMB07e5Vw7uxXSsLVGJwXwM7Ni0pwyNBEOP1d8aYKhBFtTykmz048iGZ75TmLHUUNCVke3ytJed7viwCF5oCBc2Kcc2HHWdRmfrGvXq_2TFcZzL31kisnT4REE2S3y8A9iWgUdIqGoORlDqFCJ1m4lQY1hmbAdF7w4ErMN45g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استادیوم فوق‌العاده زیبای مرسدس بنز در شهر آتلانتا در آمریکا میزبان بازی های جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66295" target="_blank">📅 16:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">واقعا حق اسپانیا تو بازی اول خورده شد باید ۱۶ تا به کیپ ورد میزدن   @sammfoott</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66294" target="_blank">📅 15:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66293">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbQtTD_5Qu1IuNNk9oST6flS-WWgPKeNXz-1V27Xq8DljaGVVarz-IMFb3QHOO1MzqEuybeiKVwN52U_likmpXUpAl9PU8d09Gn1WqomHLaI03yg7ncbHTM_SbAWHgJYKQOnfwVvUDdYL8Ujv5pkXSJWPB6USPoONu46GO49k6-Hrxif0w008y_JypDLFrFxB79Pcq1VKfXoA8WikWeBKOnRYeplpI0GMLshZhqkKQfBeATWVOV_y1lO5Tbws_-hsDnBnov_88H1K_wLZuc71D6RvveuANDeN2DpSWjBKJo948G73xOgP3Bi01AJtBKvW2pi3QZ1n8NN5k_YPyZinQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
جمهوری اسلامی هم‌زمان با امضای تفاهم‌نامه‌ «صلح»، دو تن دیگر از معترضان ۱۸ و ۱۹ دی‌ به نام‌های جواد زمانی و ابوالفضل ساعدی را اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66293" target="_blank">📅 15:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66292">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=Bmf-CqEzDFYSj18f1h4m48od-YUgx-PYb_qQtuqL5v_pSxjlTBDfQPmEMoWPEsFkxi-hZ4_NysGplYUSm8J74guQRRy8MA6zeqf8UnEIseSIEfSptY-OVY5yrCv9pT69JkglNIJ203k7SdntgzOmymfU0A8fk2MX6JmidLw8F2zjNAzCxVC-At5WjIbr1q7Cdig-Ln7PqIOSdOBhRLvj1yLmR1-0tRNgFDiFKGFRLXBtTYoLMzJ3ZNcxxe_jrP6JNBl5b5DJDjrpoFE26W8Jzt6QY1inIu3sgihhBA-RdV7-GfzFSqhgVT06gnFpfnjj6KJWzd9neIXur5nEdxwWSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=Bmf-CqEzDFYSj18f1h4m48od-YUgx-PYb_qQtuqL5v_pSxjlTBDfQPmEMoWPEsFkxi-hZ4_NysGplYUSm8J74guQRRy8MA6zeqf8UnEIseSIEfSptY-OVY5yrCv9pT69JkglNIJ203k7SdntgzOmymfU0A8fk2MX6JmidLw8F2zjNAzCxVC-At5WjIbr1q7Cdig-Ln7PqIOSdOBhRLvj1yLmR1-0tRNgFDiFKGFRLXBtTYoLMzJ3ZNcxxe_jrP6JNBl5b5DJDjrpoFE26W8Jzt6QY1inIu3sgihhBA-RdV7-GfzFSqhgVT06gnFpfnjj6KJWzd9neIXur5nEdxwWSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انتقاد ترامپ از روشی که اسرائیل در لبنان به کار گرفته است:
لازم نیست هر بار که دنبال کسی می‌گردید، یک آپارتمان را خراب کنید.افراد زیادی در آن خانه‌ها هستند و می‌توانم به شما بگویم که همه آنها حزب‌الله نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66292" target="_blank">📅 14:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66291">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=hQXMDjVrO8qc2kX1zEcHGuDmPWw5OGgyAuUD6WJNlZNck_6AGg9TLTmkge8F0AS8BLnJLdHnxrxw6EmUQhRyHNoPiy3WbyEcbTfKa6V-gF8kpjsQXzOc3UsPNHgFwUVtFMAnkb33drTXam6a6RDs8HMRKrDU_OwuQslVByXEZAlLKJY8QreT4kNSwn_3tysf1PGoXS0tsLKyTvEUCwGc4_4i0PpU1Sf5vbmk07BvctDrpfXCFVG-4UscC1tDciKmohbnM2EEMvR7OqfqStokLqYNVJsYMtDwJE-7TY9_6Isbdq34FqZfyiY4j9lNWLZgbzLMmcea_Q1Lzn1qGbKh6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=hQXMDjVrO8qc2kX1zEcHGuDmPWw5OGgyAuUD6WJNlZNck_6AGg9TLTmkge8F0AS8BLnJLdHnxrxw6EmUQhRyHNoPiy3WbyEcbTfKa6V-gF8kpjsQXzOc3UsPNHgFwUVtFMAnkb33drTXam6a6RDs8HMRKrDU_OwuQslVByXEZAlLKJY8QreT4kNSwn_3tysf1PGoXS0tsLKyTvEUCwGc4_4i0PpU1Sf5vbmk07BvctDrpfXCFVG-4UscC1tDciKmohbnM2EEMvR7OqfqStokLqYNVJsYMtDwJE-7TY9_6Isbdq34FqZfyiY4j9lNWLZgbzLMmcea_Q1Lzn1qGbKh6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
در توافق من، اگر ایران به سلاح هسته‌ای دست یابد، منفجر می‌شود.
در توافق اوباما، به آنها اجازه داده شد که سلاح هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66291" target="_blank">📅 14:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66290">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=NhRRD8fCY6YM7U7x-CRycnIswAA5DU_oUBAsk-FwF4w2nuoWO1Q2CNxTCTsAjaXh_6a8ZtrbxHi2dx2jjA9iXxSebmH7xVzBuZsFt76LtDXIhZ7TFi4fSD9n66wzu7eenq8hNVMfYH889yJSpQhV7J4HJ6Cg3dLvyl8MsVon3GTTcQczrP3qcF99i3ajlJyAwB5hRsjxQk9vsKWbdiPZAL_CSvYn8IjwehcYHTxViOecpF9VknvBe6KfLRwf1_tD6Fa1XF6Kk-EDinUdBKlGXkRGYEHLQbDH_72TFAuGD1k_4aValDbN9BpV8xqJhcdy74ZzKryl5okLCt5iERADbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=NhRRD8fCY6YM7U7x-CRycnIswAA5DU_oUBAsk-FwF4w2nuoWO1Q2CNxTCTsAjaXh_6a8ZtrbxHi2dx2jjA9iXxSebmH7xVzBuZsFt76LtDXIhZ7TFi4fSD9n66wzu7eenq8hNVMfYH889yJSpQhV7J4HJ6Cg3dLvyl8MsVon3GTTcQczrP3qcF99i3ajlJyAwB5hRsjxQk9vsKWbdiPZAL_CSvYn8IjwehcYHTxViOecpF9VknvBe6KfLRwf1_tD6Fa1XF6Kk-EDinUdBKlGXkRGYEHLQbDH_72TFAuGD1k_4aValDbN9BpV8xqJhcdy74ZzKryl5okLCt5iERADbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
گروه اول و دوم رهبران همگی مرده اند.
رهبری فعلی ایران افراد بسیار منطقی هستند. تعامل با آنها خوب است؛ آنها افرادی قوی و باهوش هستند.آنها رادیکال نشده‌اند و به دنبال کمک به کشورشان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66290" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66289">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=nAO_APLNxx1goAgxcybZnTJTX9QoGhG9CeStTz1Y2IL8D4haCGIJByCeLiMzqFMy2OFRx1iP5dP7864QTsyzZMrucAA45lWGEYjhlJZCrgtabW_IwBLvzck5PyZ_0ueSckIbeuKYSVU6tW3khsRmUIuldQ-lCFCsDl-IszKtuJReOKGvY3yJGEJkV5Dnvod0IBYFq7qatiQQovnbMp_gDL3VkHR3_JbKtyxKFOLK84BMH35dJdqTjBk66QOT6-YeXx1MXqM_VoEjjO8ddVLwfs0Sob3HVSkoE9DXLeBj97T5b5TsDI3Uww93ryVSc4A59amkGjHUDYZSDkP0gkdbYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=nAO_APLNxx1goAgxcybZnTJTX9QoGhG9CeStTz1Y2IL8D4haCGIJByCeLiMzqFMy2OFRx1iP5dP7864QTsyzZMrucAA45lWGEYjhlJZCrgtabW_IwBLvzck5PyZ_0ueSckIbeuKYSVU6tW3khsRmUIuldQ-lCFCsDl-IszKtuJReOKGvY3yJGEJkV5Dnvod0IBYFq7qatiQQovnbMp_gDL3VkHR3_JbKtyxKFOLK84BMH35dJdqTjBk66QOT6-YeXx1MXqM_VoEjjO8ddVLwfs0Sob3HVSkoE9DXLeBj97T5b5TsDI3Uww93ryVSc4A59amkGjHUDYZSDkP0gkdbYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: رژیم ایران همچنان به کشتن مردم خود ادامه می‌دهد.
ترامپ: بیشتر این اتفاقات در دوران رژیم اول و دوم رخ داده است، خیلی بیشتر از الان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66289" target="_blank">📅 14:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66288">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=PPFdh0gL2t_5GPvqXMN544Q5sRB4d1rctVwT8R-qXmJqUIiuq9UMb2rWyprT4U5TaGmJSMXrQdNA4MoUNmoOQo7xQ911VVi6bzLm_9MAzBq3oP5YM8_PljmpZvIDdcB2V0Eh-J4s5YEVpzWbWL07vNjNcjXTdrAA4Mem1PbDMshh0_Iy8GXixtV5mGdPv_dzk-X_Uea6XK_Elm1eo3OVYMLiqSCcMVih173fu4dIz43Kod7Hmfo0y4rlcrv0QtmlL6CgMOfxkPm5fT6gQ7PU3mhxvgqnnBAi-xlQslKqLMICyS-glLas6tFoV2vmpCfo-FZv4rN7M9NcrJM9XecCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=PPFdh0gL2t_5GPvqXMN544Q5sRB4d1rctVwT8R-qXmJqUIiuq9UMb2rWyprT4U5TaGmJSMXrQdNA4MoUNmoOQo7xQ911VVi6bzLm_9MAzBq3oP5YM8_PljmpZvIDdcB2V0Eh-J4s5YEVpzWbWL07vNjNcjXTdrAA4Mem1PbDMshh0_Iy8GXixtV5mGdPv_dzk-X_Uea6XK_Elm1eo3OVYMLiqSCcMVih173fu4dIz43Kod7Hmfo0y4rlcrv0QtmlL6CgMOfxkPm5fT6gQ7PU3mhxvgqnnBAi-xlQslKqLMICyS-glLas6tFoV2vmpCfo-FZv4rN7M9NcrJM9XecCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد گرد و غبار هسته‌ای:
شما می‌توانید این استدلال را مطرح کنید: چرا اصلاً خودتان را به زحمت می‌اندازید؟ چون واقعاً ارزشمند نیست.اما فکر می‌کنم از نظر روانی، ما می‌خواهیم آن را به دست آوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66288" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66287">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77169efe09.mp4?token=B-_ST4AE3IUy7-rcgdPkt4C6FaJbOMvY3pgw5DR7jXJZOgOWBQYAeBrxa03dlsV6-HLmzlDdrLTeS_bXQhRovA8H5pYEbQx94CfHeet2VRPih9jWM-tC11XxRCc816poR4TLoeBTKBVYokKkbNMC7R9__VEVKUSuLv3G1tdXc6OjYWWCcbpfrrT4ZdDKSGChlZ6IbYZCUK2BdKNc1jlpDjD7LtwtR8ihZ0mSv1DVb0gvjCJzV1EGOjdAERWxyswd2dK82fBm4ePQde6mpzw7GirJO6jTiMcOcFyAeHGz8FxdsY_lOlJrUDfKK7KOrlqnNtDUgrKcj22v6xaVSvWkkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77169efe09.mp4?token=B-_ST4AE3IUy7-rcgdPkt4C6FaJbOMvY3pgw5DR7jXJZOgOWBQYAeBrxa03dlsV6-HLmzlDdrLTeS_bXQhRovA8H5pYEbQx94CfHeet2VRPih9jWM-tC11XxRCc816poR4TLoeBTKBVYokKkbNMC7R9__VEVKUSuLv3G1tdXc6OjYWWCcbpfrrT4ZdDKSGChlZ6IbYZCUK2BdKNc1jlpDjD7LtwtR8ihZ0mSv1DVb0gvjCJzV1EGOjdAERWxyswd2dK82fBm4ePQde6mpzw7GirJO6jTiMcOcFyAeHGz8FxdsY_lOlJrUDfKK7KOrlqnNtDUgrKcj22v6xaVSvWkkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ایران حتی یک بار هم به ترکیه حمله کرد. من هرگز نفهمیدم. هیچ کس قرار نیست بفهمد.
مشکل این است. آنها افرادی کاملاً غیرمنطقی هستند و این افراد اکنون رفته‌اند.
من فکر می‌کنم ایران اکنون رهبری منطقی دارد
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66287" target="_blank">📅 14:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66286">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5225dce7ab.mp4?token=LE8DZxHUkqm3cX9aHSyq3ydkyEx3GE7gTwP8bCfUbLUtSy44EnEmd2xu73-WqxJxFrOIN4xQQ6UdQGqBUNA62TQlpqsixXvyEJmnz-ExBA6rvb9gqFR-NRLFbOA3tt-r6x4co6RQwoS6JFQcb4A677_hsCRgvpnmzeCB-r2k0sZDrBbvOl4uW37VOTrQV4wa9KnQWzUgtP463H2-VdpRsVZQJLpNJ2NGQTtiU_GGvzNJHLMebBU1YZ1mMUhpg-hIDlQ8a3l6F8TqU7HzMvM6SkZCPE-uwRVXPXIzNwlJAYzxoEQjjmiLunbRjgq5DdjGlbBnlZdBd4f88EFSCQ-q3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5225dce7ab.mp4?token=LE8DZxHUkqm3cX9aHSyq3ydkyEx3GE7gTwP8bCfUbLUtSy44EnEmd2xu73-WqxJxFrOIN4xQQ6UdQGqBUNA62TQlpqsixXvyEJmnz-ExBA6rvb9gqFR-NRLFbOA3tt-r6x4co6RQwoS6JFQcb4A677_hsCRgvpnmzeCB-r2k0sZDrBbvOl4uW37VOTrQV4wa9KnQWzUgtP463H2-VdpRsVZQJLpNJ2NGQTtiU_GGvzNJHLMebBU1YZ1mMUhpg-hIDlQ8a3l6F8TqU7HzMvM6SkZCPE-uwRVXPXIzNwlJAYzxoEQjjmiLunbRjgq5DdjGlbBnlZdBd4f88EFSCQ-q3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگن مجتبی تو LA رویت شده
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66286" target="_blank">📅 14:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66284">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j57zoQDGo7e3PLwx7_4U17_ke7C1I4439R3BJebPXPUNhBEDuFyIBImBqVW4N2X-DkNoJDX_Lu9oaHCpvY4vgAdO8YhBh_HXtXYdh-eZ4lh2gDTCSIwlxZdagGEyyFpGiyJjklfhDtms4OCsF4eNgIU1tURbGAs9sEckZ5MnY9ica9NmnuG-ZCdkS00g6GWMJ6xT4PQTyBe4MF0ThcpY-E47KllBg9UbJ2ttY9dHnabkiJgWqdV6HuT86PdArx_eqia9Rm_YWIfCRxY0nY06nSHrXQbZWLI1ZsiHv09gmhGT-idqcsADG5MimX9QLy9_CFNNfwFRX2R0VX-g88PDqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edD-QQ49mbOpwg8No7fmb0P5xXglV39ZWW6aEu08z2byWb-4b5I-VL0Gud2VmpiO_P96fWh9s1DAqFEVpq40jLwVVbfHm4wszhQU2zNLBGqiYolNMq4QdXOfYo0uYELOqDZsqe8Glg622D4Z3WbHgKWQZt9gW2vrBh05wh-R5HWXyN-J_LlJcqNeu-fUjNDopqh3ZbRDe6XqOpHNvqBjhrdMvCnMfYoO2wZuMtwYc7bD9HjBtg7wEU-bN0KB4ZG6TO_f7Iki76i9kCLbZBqgG8hdRMQvW8IxrgiVarqpV_Hr97LzAvwFQachaPi4ghdqgAaSn34zoQu_hrquCBrkVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
برنامه جدید امتحانات نهایی پایه های یازدهم و دوازدهم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66284" target="_blank">📅 13:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66283">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
ترامپ:
من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
جنگ لبنان مسئله‌ی فرعی است و توافق هسته‌ای با ایران می‌تواند پابرجا بماند.
به اسرائیل گفتم حمله اش به بیروت برایم خوشایند نیست.
نتانیاهو اکنون باید در قبال لبنان مسئولیت‌پذیرتر باشد.من از نحوه برخورد اسرائیل با لبنان و حزب‌الله راضی نیستم.بدون من اسرائیل وجود نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66283" target="_blank">📅 13:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66282">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
ترامپ:تلاش هایی برای تغییر رژیم در ایران وجود داشت اما موفق نشدند.
اگر ما برنامه جامع اقدام مشترک اوباما با ایران را لغو نمی‌کردیم، ممکن بود این کشور به سلاح هسته‌ای دست یابد.
ما می‌خواستیم برای گرفتن اورانیوم غنی‌شده به ایران برویم، اما این اتفاق نیفتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66282" target="_blank">📅 13:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66281">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
ترامپ:
توافق با ایران به مرحله دوم منتقل میشود.ما یک توافق منصفانه و خوب با ایران داریم، اما هیچ پولی در آنجا سرمایه‌گذاری نمی‌کنیم.
چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، تضمین این بود که ایران سلاح هسته‌ای نخواهد داشت.
چیزی که برای من مهم است این است که ایران به هیچ شکلی سلاح هسته‌ای نداشته باشد.
اگر ایران به دنبال سلاح هسته ای برود جهنم به روی او گشوده خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66281" target="_blank">📅 13:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66280">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b4a7171c.mp4?token=IPjDRw1BGeciO4u3hqIktTnpZPHSPfoaPEd6prApW4e7Ot_tBBwpvtI_Mb_6G7wNQVO8aeu1RH72VlmgvhqI7KfQ3Z0Gku6R2evW12_JLQlpK1Q2To1-IzBzt2NqLjvcb7qO-limibgJreZ-MGymiow9CIxBmKnwHP-EwHnfg-4ASp6Emay1noGTBcuzww9LzLYPpqfw7S4rxYhcXoWquE-rSaJCZeVQ2kyYfPw0kNV_pKxoSrunYd_m31fQBx44Tu1zH6khbEOiFa7aEdANy5JJP4G3OGxlZ021ePqAWuQkCLBMl-J6zXdPJZ5WJjQCeIVNNVsP2gVBXofQgRiqsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b4a7171c.mp4?token=IPjDRw1BGeciO4u3hqIktTnpZPHSPfoaPEd6prApW4e7Ot_tBBwpvtI_Mb_6G7wNQVO8aeu1RH72VlmgvhqI7KfQ3Z0Gku6R2evW12_JLQlpK1Q2To1-IzBzt2NqLjvcb7qO-limibgJreZ-MGymiow9CIxBmKnwHP-EwHnfg-4ASp6Emay1noGTBcuzww9LzLYPpqfw7S4rxYhcXoWquE-rSaJCZeVQ2kyYfPw0kNV_pKxoSrunYd_m31fQBx44Tu1zH6khbEOiFa7aEdANy5JJP4G3OGxlZ021ePqAWuQkCLBMl-J6zXdPJZ5WJjQCeIVNNVsP2gVBXofQgRiqsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هادی هوتیت، خبرنگار  پرس تی‌وی، وارد منطقه‌ای در جنوب لبنان شد که نیروهای ارتش اسرائیل هنوز در آنجا مشغول عملیات هستند. فیلم نشان می‌دهد که او در جریان این حادثه مورد اصابت ترکش قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66280" target="_blank">📅 13:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66279">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b685347f.mp4?token=iPfRt5XDY_8troeYBhPScko0GEDRoxIB7j9di2F13Bocu-B7VnF5mbH3e9u5LzVovmlUOAbO86WHy9QVqAeLAeAFg102GMVRZlIUu06F0Ubb4sT6oubyW1ra-yMdTAOMzFVokwH3MVuUkUMWuyYVLa4qWcqV7lY1AsmhyFk1pCHNC09XBo3ATVVijtGk_DmgCQ2lljEYnVG0v8K7DEOyFgWfG6J_oqnalfe1MBvdLiGI9lT9AuhFJQdl5NUHw4SI_IEzNaSJgsLz0jDpG_fr77KybkS7KMradYFSDhHu9G4ozFdXu0kTL7Nfu0n_1oCji73Y_Ec37Qzc5L5Q10_Isg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b685347f.mp4?token=iPfRt5XDY_8troeYBhPScko0GEDRoxIB7j9di2F13Bocu-B7VnF5mbH3e9u5LzVovmlUOAbO86WHy9QVqAeLAeAFg102GMVRZlIUu06F0Ubb4sT6oubyW1ra-yMdTAOMzFVokwH3MVuUkUMWuyYVLa4qWcqV7lY1AsmhyFk1pCHNC09XBo3ATVVijtGk_DmgCQ2lljEYnVG0v8K7DEOyFgWfG6J_oqnalfe1MBvdLiGI9lT9AuhFJQdl5NUHw4SI_IEzNaSJgsLz0jDpG_fr77KybkS7KMradYFSDhHu9G4ozFdXu0kTL7Nfu0n_1oCji73Y_Ec37Qzc5L5Q10_Isg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمدرضا شاه پهلوی مردی بود که دستش نمک نداشت
👑
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66279" target="_blank">📅 12:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66278">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما واشنگتن و اسرائیل را یک طرف این یادداشت تفاهم می‌دانیم، در حالی که ایران و حزب‌الله طرف دیگر را نمایندگی می‌کنند.
پایان جنگ در لبنان بخش جدایی‌ناپذیر پایان جنگ در ایران است و شامل خروج اسرائیل از خاک لبنان نیز می‌شود.
هرگونه حمله نظامی اسرائیل به لبنان و ادامه اشغال، نقض تفاهم‌نامه است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66278" target="_blank">📅 12:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66277">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=kbz_Shmuq78nRQ0fCfj_bqphJmE42sco-ycBLfCZ7RR3z2fflrt0OrZTEwRl49n4UpYuNnwYRhHs6ZIfcxpmE6Qd4nfOIiK7kM_CINCHxuFkJtj5tuIZuDaKqwpa0wEpzw3eZRjfrzzzhX-3JVxHyzfzwt5cmkbFmZm73mrddf52BHBVl5rVsW06-m-5W0gPbr6wRlsLnjKWfSvWwN0be7QOJP7imBAwHMPDJ4voKJ1CTsO3xVLA_IDEoYAuNqcSjl0g9t4Qti4c5g7tRkxT9wPELTweA0Y3v6TdouRuO-W-9NaT1nLXJfdAn25Lqn9jUsVyfHpmyM9Dh72NS4sD9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=kbz_Shmuq78nRQ0fCfj_bqphJmE42sco-ycBLfCZ7RR3z2fflrt0OrZTEwRl49n4UpYuNnwYRhHs6ZIfcxpmE6Qd4nfOIiK7kM_CINCHxuFkJtj5tuIZuDaKqwpa0wEpzw3eZRjfrzzzhX-3JVxHyzfzwt5cmkbFmZm73mrddf52BHBVl5rVsW06-m-5W0gPbr6wRlsLnjKWfSvWwN0be7QOJP7imBAwHMPDJ4voKJ1CTsO3xVLA_IDEoYAuNqcSjl0g9t4Qti4c5g7tRkxT9wPELTweA0Y3v6TdouRuO-W-9NaT1nLXJfdAn25Lqn9jUsVyfHpmyM9Dh72NS4sD9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانیان وطن پرست سنگ تموم گذاشتن و اینقد پرچم شیروخورشید زیاد بوده که میساکی فشاری شده و پرچم جمهوری اسلامی نشون میده میگه این پرچم ایرانه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66277" target="_blank">📅 11:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66276">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=WoxY45UkmA-AVtV5R06fZSExMVY542zJaGFrhe5xnRMRuU5sHS9qGm9SScOHiYvBWjmRUeE2SNu9ZKs1vzdudTlYN3dI95bfpLxSjAJUZoOtu3SDw1n_4UahLqhVxZj2He-t1H-fLd5Sx9Ndua98g4zk1OPz_MXA1kYuQxMMZhnhPqbMhP2RdJRsNVwpWRP7KCwo_cV7yZW4_NSIKewxw3pmuz06xF51DU4tzD7f8ZG990smejEMZVKKs-KxKN0QEyu_vts35IdlEwsYCWIDglYhjNAt7Wq0PwfBCSiZ2DRhPgsQHlu0z6qFaBzrJ5Kc-DJfQZdIY0Hzss_Q_03oxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=WoxY45UkmA-AVtV5R06fZSExMVY542zJaGFrhe5xnRMRuU5sHS9qGm9SScOHiYvBWjmRUeE2SNu9ZKs1vzdudTlYN3dI95bfpLxSjAJUZoOtu3SDw1n_4UahLqhVxZj2He-t1H-fLd5Sx9Ndua98g4zk1OPz_MXA1kYuQxMMZhnhPqbMhP2RdJRsNVwpWRP7KCwo_cV7yZW4_NSIKewxw3pmuz06xF51DU4tzD7f8ZG990smejEMZVKKs-KxKN0QEyu_vts35IdlEwsYCWIDglYhjNAt7Wq0PwfBCSiZ2DRhPgsQHlu0z6qFaBzrJ5Kc-DJfQZdIY0Hzss_Q_03oxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل سود نکردن من تو بازار بعد چندسال
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66276" target="_blank">📅 10:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66275">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c971246f.mp4?token=bG0Q1KLwO9IIAZdUt9U4cHtfE0VXL1cq4tVMy1W8O4Ph2QbrMiC93XIcsmAW9X7SdE6S4pKxxShyssFPE-8M04bhKBEZ56VRVdj0BcLuNmNKUPjJcLPdHtQdSBLYTfe6qYJNoXFXwHp275lSUmbhFQO5HCTOHDax6wqB4LZO6Ta1VgRVsCt7R28ex4dFq1U4WdcwgVJ0r9P3RedRoncqBQrGp2425Bex0PrZKXXg16KStvM9nSgXwxIy7D78AVgRS5IUsBiThQUHE5zKGyuCBEz89mJqGNs1I0Mus3Y3G-9ZGiKpaFrgYPFx9Jd2xOPNhE4WaOMVLMfFhenoWND9zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c971246f.mp4?token=bG0Q1KLwO9IIAZdUt9U4cHtfE0VXL1cq4tVMy1W8O4Ph2QbrMiC93XIcsmAW9X7SdE6S4pKxxShyssFPE-8M04bhKBEZ56VRVdj0BcLuNmNKUPjJcLPdHtQdSBLYTfe6qYJNoXFXwHp275lSUmbhFQO5HCTOHDax6wqB4LZO6Ta1VgRVsCt7R28ex4dFq1U4WdcwgVJ0r9P3RedRoncqBQrGp2425Bex0PrZKXXg16KStvM9nSgXwxIy7D78AVgRS5IUsBiThQUHE5zKGyuCBEz89mJqGNs1I0Mus3Y3G-9ZGiKpaFrgYPFx9Jd2xOPNhE4WaOMVLMfFhenoWND9zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از پالایشگاهی در حومه مسکو که در اثر حمله پهبادی اوکراین دچار آتش سوزی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66275" target="_blank">📅 10:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66274">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=tb2t8fcOKIChj3tVlbkHFLeHqeoQM8K-mfDQZo9OQo_b8utd3dgTIsUM4SoHVCFicg4tW9D5_rzhNeKv0w6-BckOcqGoucot40imjMJjUQGOVgumaj0oPKYcQ6-H0hbyLLEJHw8v3o7qXcBr1tzvZv4NMhB2PVFR8eV0wkKRV1BWIkISyJqrj2K0CVfQTeWPnooB9YeMJvenKoQyGe5jYCQ1qmVCERbS50GWvlYBmXFsklv7BVNETylyLFYV_qK2AfC-oT2Rts9_Rx74-yFbocFKl2CVUGhYNxorXMH6qBPp_hk8k8acJWIpdGaN67kuUdJjNXTsVjLwk28B88hEkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=tb2t8fcOKIChj3tVlbkHFLeHqeoQM8K-mfDQZo9OQo_b8utd3dgTIsUM4SoHVCFicg4tW9D5_rzhNeKv0w6-BckOcqGoucot40imjMJjUQGOVgumaj0oPKYcQ6-H0hbyLLEJHw8v3o7qXcBr1tzvZv4NMhB2PVFR8eV0wkKRV1BWIkISyJqrj2K0CVfQTeWPnooB9YeMJvenKoQyGe5jYCQ1qmVCERbS50GWvlYBmXFsklv7BVNETylyLFYV_qK2AfC-oT2Rts9_Rx74-yFbocFKl2CVUGhYNxorXMH6qBPp_hk8k8acJWIpdGaN67kuUdJjNXTsVjLwk28B88hEkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هو کردن هوادارن حاضر در ورزشگاه هنگام پخش شدن سرود تیم جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66274" target="_blank">📅 09:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66273">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=iu10hShyylWpvDH27Rk32Splx_npIBsHluGha7jnZyxN5oJMXKKScMjZ7a_Ggon7WIeytgJU0jnNRUD7iHdu-q4YiObKje1WT8M_-3mtqz2Hv_oY-lXbntIt8rQDDP50-dg3hk9ckc47s0YOflq157iSVdJWB05g0Se0IPsadDNcE7BaKny3VgyWB4YCmflNU9hKyiTAJiLfxIGaBRg3MAyOVaRS-xXBRR-itVlK6esxbll2FcH4wkU53OIZxKjcJuf1jBqIXtuWuXXlNx92rMRAaY9VSuRgnXC9O3Eb7Q2C5mq1CBSGpvpSfKqKRvrRwMSXlXVKkOgd0grgDzmiHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=iu10hShyylWpvDH27Rk32Splx_npIBsHluGha7jnZyxN5oJMXKKScMjZ7a_Ggon7WIeytgJU0jnNRUD7iHdu-q4YiObKje1WT8M_-3mtqz2Hv_oY-lXbntIt8rQDDP50-dg3hk9ckc47s0YOflq157iSVdJWB05g0Se0IPsadDNcE7BaKny3VgyWB4YCmflNU9hKyiTAJiLfxIGaBRg3MAyOVaRS-xXBRR-itVlK6esxbll2FcH4wkU53OIZxKjcJuf1jBqIXtuWuXXlNx92rMRAaY9VSuRgnXC9O3Eb7Q2C5mq1CBSGpvpSfKqKRvrRwMSXlXVKkOgd0grgDzmiHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
عراقچی نوچه و اراذل اوباش آمریکا در کشور است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66273" target="_blank">📅 09:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66272">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaxoS4qGRuei7tSnzKWuiRsmmUh46ccMqMMGadS4Ww8iPH3fD6TFKIfLo3ENbxkd5yyWbJzktcGpy19-5h5TadOaIboP0FxQTa4qqr6M_w-g5mC516EVh-5d94pLYLQGbQvXFUKYn-QJ03haBAnNQ63SNih1F3vDlNMDeYhLG5bOpPmnXeBS43qCr0DMMU6Gtg-T_Wzw3mquhWSzOVJ9vAdub9QhXIJwRDXlYvTVD0jB4Dn7GXaWjr9Xy5_7YiF42bV5W8jx6rICQ8PBY5iZYKORbYoUkKazv1KdfIRYuFhUMLyfjXAMPjSDgPDt_xnBiGQ0DbRrRltDfshKIjThvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
پایان‌بازی
🇳🇿
نیوزیلند
😀
-
😀
ایران
🇮🇷
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66272" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66266">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گل دوم محبی
#hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66266" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66263">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇳🇿
گل‌دوم نیوزیلند به منتخب ایران دقیقه ۵۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66263" target="_blank">📅 05:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66258">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
سخنگوی قرارگاه خاتم‌الانبیا: گل زدن نیوزلند به ایران قطعا بی پاسخ نخواهد ماند
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66258" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66257">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پایان نیمه اول
فرزندان برحق وینتون روفرو ۱
کاکولد های گروهبان قندلی ۱
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66257" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66255">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یه حسی بم‌ می‌گه بازی مساوی تموم می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66255" target="_blank">📅 05:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66254">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🏆
گل‌تساوی توسط رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66254" target="_blank">📅 05:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66251">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6kcDlzGv69D-znqm52yqpRagD16z7D3cigTSc0nMdCuEpl5m45Nd6UzfJlwyKUzYk_XAzCVNGL3zGSyO86qr9N8FHXp7ZUlb2DYYkHquTSVHirmj7Zd3sjCT5J1JKEI3uhjRJflnLgvETq90eY-LAvuTi8Mic4eNhOVPcOTqAt3FngLwnmz1EOvvWJbBJiID8RlCWGAAi1Kk-dsDhz_yLG3TzlQ4AV5yw07tpZvdmW7FCI0eAacSYqJgNgTJds7X-p6SKXnnBE4mmAit45Z_1MB4I4px8CVaLoAQeN67PNFA69RG6q58RC_8EmAKc58yXH-M33uDniMUkStCrII2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه بازگشایی تنگه بیرانوند
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66251" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇳🇿
گل‌اول نیوزیلند به منتخب قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66248" target="_blank">📅 04:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66244">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-poll">
<h4>📊 دوست دارین کدوم تیم ببره؟</h4>
<ul>
<li>✓ تیم منتخب امیرقلعه‌نویی🇮🇷</li>
<li>✓ تیم ملی نیوزلند🇳🇿</li>
</ul>
</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66244" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66243">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1p7SJBaOZ5sHw-9K3gnhDX9wgwZ4Q8_XPUH3K5d4kZ4mXHeYkvYMpK3NoFubmNpDlTK4oOY7rAx65Gz10IPjLlv_zaQLS3tuXIGsx-BVvrUNa4pL3uSONIJIWNqVvZI8dgrs1xh--kACgus5NRT2YpTcMD6pimrKxi10pv6p_ya9OY32JVmCLSldhfKuuSAV2P75kwH5dh5pLYVii09vA95SHFsGPXFhUGSuMoijguSMB24GltRGu0Ipwp7QlWrk_1ASl2MhFk9Hw2iZP52TVLNqTrOcN_WbVoWbubirx3sDl1rvwpjo99aWZgDXfGlNOnoVOss2H2fePfDwZOjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66243" target="_blank">📅 03:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66242">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66242" target="_blank">📅 03:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66241">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhossein ؛)</strong></div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66241" target="_blank">📅 03:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66240">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66240" target="_blank">📅 03:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66239">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66239" target="_blank">📅 03:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66238">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOKeCHo4qTdW2hErsgLaRd7N_iJbWCIIUGG8_5m3-x95oVTg0kwFZWjhtSAfpovhvPdc29h-SKhEJj3DF4B_4ZTV3HDlHz78f_koITdOYQWlDii5jYo-08kY91CpZbxs-lrsE7Pylm_XXIPwrgbp774mjxo8XPlrb5azId1q3PD911sx7touWLrUmpN1egnKW21WFT9xE0aTJEKOjDMiwVQ7KuAaT0bAvxwaT7RpYhL54M13Br4L2vrP4PyhxLDuFWc-2gQHCXLnhUAc8qXdkV5cmnD4eQWSnHlV1ugaYuo0YgnjzniZFWOQZwAnoUHsv4tcXlVYt8T400agDa_wrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
👌
تصویر تراز امشب:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66238" target="_blank">📅 03:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66237">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
صحبت‌های ایرانیان مقیم آمریکا قبل ورود به استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66237" target="_blank">📅 03:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66236">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa7qEzR5ZGgu-dBZLpSeK9yNqK8SLSJjWXzNMvAez3lWmP_kXwUkRdILsX8_nzK1Rtngm5kZ7hSwWZGOyAToimbE5sx9h5WQLgpNCvv0NJlHANJdJ0zCKH4QRD2LPgGVzgM5iJHpBZfsmfRDrgXm00ULEVwbVNa3HDrHAsyu-1LbLBPQcTp_wik--SN-3feeIh8hMKeSAwTAcGAnCiT5KfpJfTqFplDQQgpPJL9PHYaQO4YdNEe4UlqW-8TVWdK4hia29v_8mbiXsKsSr8iJB3pFK_0sx_JMQZKCuAzxVQDYHYpY7l75IsSwovibZustyw_WjCT_ag_AEzqnrjfdng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66236" target="_blank">📅 03:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66234">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=tEXe3IKjS5AHli9yqR-671PNcoSP4hsznDE1ZzOI6AnGHP3dKGYLE2xqvp1NdfFFkABE217R4feiE8yQ2L0Z5XethqJ-G0FSPIWSF7ekmeJd87LpWJPEMk5XY6VInP5KgqNToNDrF-7CNc-OxZor1kYPKDC8dkCpLyzvbwImcDMm59YitoF88sntDMXZWoMXfd1qNQxEh_UZyVQVuNRfUe8TWHYpeC7Xj3MsuxZcfkOe_OWNMndtA0zkX3JTJelDE_moLotdt15QbpihbNfY_NmQVFTyrderOIyVf2RqQQqCYKvkLfx_ZnKEPQ1RhCOrv2Lsk726T1SQYnJijpVzZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=tEXe3IKjS5AHli9yqR-671PNcoSP4hsznDE1ZzOI6AnGHP3dKGYLE2xqvp1NdfFFkABE217R4feiE8yQ2L0Z5XethqJ-G0FSPIWSF7ekmeJd87LpWJPEMk5XY6VInP5KgqNToNDrF-7CNc-OxZor1kYPKDC8dkCpLyzvbwImcDMm59YitoF88sntDMXZWoMXfd1qNQxEh_UZyVQVuNRfUe8TWHYpeC7Xj3MsuxZcfkOe_OWNMndtA0zkX3JTJelDE_moLotdt15QbpihbNfY_NmQVFTyrderOIyVf2RqQQqCYKvkLfx_ZnKEPQ1RhCOrv2Lsk726T1SQYnJijpVzZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تجمع هموطنان خارج از کشور مقابل ورزشگاه محل بازی تیم جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66234" target="_blank">📅 02:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8rwHZSdb0KgqwYN4WzVwklj75OD-rsShqfrtoJ6BIYMSD4dkmd8-aoSANky8A1B644HPQkf5IbtuUKYQs9t6KimxfcAdQ5vgfhi8LyZTJldkwj0_k-_C0LqhhkbfM6rvbGC_POzZi6fjdqAvlqvKiA1IqKVym-Kmp6CzCdcoEP25sH9zFEN_OMUIx4rDbqhdX5BHxWCh0QOyLjWxlR6QHO0LcnxV2XHwyqSi42vSxWKCBbOcfqw0JJGtVFW4MgOb7K9ifrZLOdDHw4DGmbEnnT7YKP3FlS-6PKNedt4DiXsRRNgpAIlUfrLRnMe5OuWGRkOu1bwnfcZIXtlMi13Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66232" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66231">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
#فوری
؛ترامپ:
ایران موافقت کرده که هرگز سلاح هسته ای نداشته باشد.
همچنین ادعایی مبنی بر اینکه واشنگتن مبلغ ۳۰۰میلیون دلار به ایران پرداخت میکند جعلی است و توسط دموکرات های احمق تبلیغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66231" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66230">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
صف ایرانیان مقیم آمریکا برای دریافت تیشرت مخصوص ورود به استادیوم که تصاویر جاویدنامان انقلاب دی‌ماه روش حک شده  @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66230" target="_blank">📅 02:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66229">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=TIhbnYKNoheD9n-3h64d2o_tAxQ_iA9-nGPHiIZOrWv9-aLwh9jIqd26CefMosqk2U2w8O0NtJrjh1wxFTxz_uvqatbY9R4Y1o-vBdCXhD8oto8c10ngDiH4mUs8SiqqDuyBMdoQOCyYIglfti9gvUfV95cs6szuYCy2nljCmhS-l95tViJ1cPoQj9pI2wwx_GZmbGGS6unjT752W_J0g1hyJd8knwYh2zWRzy9j8W4xJrDhZ6Oc6rwBBCT9sBGMorll6vJ5liOxQwAPOiySTs2CinI2JJzEkGMRS3lBUtWHszRFPtw2grp4CdSFhs_CmiPr0F19RKLe0ubt3HNkcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=TIhbnYKNoheD9n-3h64d2o_tAxQ_iA9-nGPHiIZOrWv9-aLwh9jIqd26CefMosqk2U2w8O0NtJrjh1wxFTxz_uvqatbY9R4Y1o-vBdCXhD8oto8c10ngDiH4mUs8SiqqDuyBMdoQOCyYIglfti9gvUfV95cs6szuYCy2nljCmhS-l95tViJ1cPoQj9pI2wwx_GZmbGGS6unjT752W_J0g1hyJd8knwYh2zWRzy9j8W4xJrDhZ6Oc6rwBBCT9sBGMorll6vJ5liOxQwAPOiySTs2CinI2JJzEkGMRS3lBUtWHszRFPtw2grp4CdSFhs_CmiPr0F19RKLe0ubt3HNkcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
صف ایرانیان مقیم آمریکا برای دریافت تیشرت مخصوص ورود به استادیوم که تصاویر جاویدنامان انقلاب دی‌ماه روش حک شده
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66229" target="_blank">📅 02:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66228">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB1cbE5xb7I00syDVvuQir7K45kQCwSTRgqj9-01GlaRWEB3vC94G-xrX38ZRstw-JsioKhyJzrEaNGGp7lOpnx1ME1Urb_6yu-FVRVN4z1rV68WOUxHOGLjRILoGsCESkDPBrEpcZ0Dcn4LLbnHPudWt-cGpipHu1xSBI_XvaqYlQIJqV1L-e4RNL8FrACYNd5i8PMHAG1ugDaIvBSbhM9sSEH2H7r3vbwcHqbz9WxBgZVhbRaz1iHCfRs3Tt-aWC75vZtln09vK8MoI5Fmk8ns_DN_5CXPnxaVcsf6V0fTG4WiPH9matZTC9sUC36Fx5e02Sgb5twtkY1BohcQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
رتکلیف، مدیر سازمان سیا، به رئیس جمهور ترامپ و دیگر مقامات گفت که اطلاعات جمع‌آوری‌شده توسط ایالات متحده، تردیدهای جدی در مورد تمایل ایران به دادن امتیازات هسته‌ای مورد نظر ایالات متحده در هرگونه توافق نهایی ایجاد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66228" target="_blank">📅 02:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66227">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VObpo2OYsbsJGStSZWiaI1NAxCWDOG8P_m8jXQNfrojCeFwWm6y2k6OSI7gjH05a0HQnID6bv8H54kM6shxWu9QrNDtLMUT7Io412VfCE01X-K6R5eCad_PNW14IGNQHXH1epitUIRY_dxpGvB1XQnmZregX5HJW-0UlTqy6a477w_Jg72YvG9_WgVdjbg_8_OsoNCI6neo85LCf0GJdE7Vynw1SGceyrkTvu4SQ25Wy28N4keeCBTZRJ4HI0OFAahJ3Tdt3N_wiPrxdtu8DJAn-4Es7kHQZiVTzF7c8Hf68TXjEdiYycxUhqhaxmaWFCR9Df8Fw8dyaKuoLMspY3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
نیروی هوایی ایالات متحده روز دوشنبه اعلام کرد که معتقد است هشت خدمه در پی سقوط یک بمب‌افکن B-52 اندکی پس از برخاستن در پایگاه نیروی هوایی ادواردز در کالیفرنیا کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66227" target="_blank">📅 02:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66226">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
ونس به سی‌ان‌ان:
یادداشت تفاهم با ایران حدود یک صفحه و نیم است و به همین دلیل یک سند عمومی محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66226" target="_blank">📅 01:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66225">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31d4a9328.mp4?token=ZJbqWVLggfD6fc7IBb9ky3qKC8nzXo_OXmdLe2Rjt5l_xqhcZeD0dYyoV_VRcUdt2y_b3cvGCWlnnL-ZuLaMEZaXuaRk7b0onAWbTGfwnjuGFWvPYSMM90DUCN-E8fuMV2XLl_CVTFBGRYmHqtRoCYwV-lC-oPnJJCGSAtrULU9qT22jZCRi7YRyrEJ3bQnj4GCn-jjNR9VMjfoLGK6J15cgU0P1eWgnj0AGSx-rl66-3gLb8jvuydZXd6MBqUlYlTKNUoUg9FVH7VuzL0ckKCjaSrm7CFGDdggWG4gGGptAvqcBC5XdA4yx44uMKpAztePmToxRQHpDBl3P3Rgs4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31d4a9328.mp4?token=ZJbqWVLggfD6fc7IBb9ky3qKC8nzXo_OXmdLe2Rjt5l_xqhcZeD0dYyoV_VRcUdt2y_b3cvGCWlnnL-ZuLaMEZaXuaRk7b0onAWbTGfwnjuGFWvPYSMM90DUCN-E8fuMV2XLl_CVTFBGRYmHqtRoCYwV-lC-oPnJJCGSAtrULU9qT22jZCRi7YRyrEJ3bQnj4GCn-jjNR9VMjfoLGK6J15cgU0P1eWgnj0AGSx-rl66-3gLb8jvuydZXd6MBqUlYlTKNUoUg9FVH7VuzL0ckKCjaSrm7CFGDdggWG4gGGptAvqcBC5XdA4yx44uMKpAztePmToxRQHpDBl3P3Rgs4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه ای خطاب به قالیباف و عراقچی
🤣
:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66225" target="_blank">📅 01:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66224">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=miMYbomD7bDwhIgzFcbEiMXb4tZ_LrVBE65zKyxs-9dWJpQEhFyU5zzoRc-SXNRXqcLLL2_KW1Au51m8_0JLFXk48U4mR6kT9HaPtpJnTkbIPDcQKQPFGVAtfxBxIi_vUtevIIVpLvGiCiUBbaQjHjwVwO2wnCbnAFUIMNMb71NRNxvkglvl8lcLf-DHJEsWqFPRJEaVkddSU1AdM6BRw_6C-MLQW9ZWNe5s0CttjKqd9uZtQW6XNvIuLQ06jNV6y2AwcAd1ibZebPR-ax3LNxgJkXWCMNIkZfA9v2snmBtJXBRBxOpZrwI3PUHoxYM42EoEKhpbabqvQ3RE3uzw7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=miMYbomD7bDwhIgzFcbEiMXb4tZ_LrVBE65zKyxs-9dWJpQEhFyU5zzoRc-SXNRXqcLLL2_KW1Au51m8_0JLFXk48U4mR6kT9HaPtpJnTkbIPDcQKQPFGVAtfxBxIi_vUtevIIVpLvGiCiUBbaQjHjwVwO2wnCbnAFUIMNMb71NRNxvkglvl8lcLf-DHJEsWqFPRJEaVkddSU1AdM6BRw_6C-MLQW9ZWNe5s0CttjKqd9uZtQW6XNvIuLQ06jNV6y2AwcAd1ibZebPR-ax3LNxgJkXWCMNIkZfA9v2snmBtJXBRBxOpZrwI3PUHoxYM42EoEKhpbabqvQ3RE3uzw7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرف های متناقض اسماعیل قاآنی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66224" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66223">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66223" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66221">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromProxy MTProto | پروکسی(|•𝓗𝓸𝓼𝓼𝓮𝓲𝓷🥀•|)</strong></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66221" target="_blank">📅 00:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66220">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
قاآنی فرمانده نیروی قدس سپاه پاسداران:
هیچ کس نمی‌تواند در مقابل حزب‌الله در لبنان بایستد و هر آنچه از حزب‌الله در لبنان دیده‌اید، تنها نوک کوه یخ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66220" target="_blank">📅 00:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66219">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2752783b15.mp4?token=XJ043eWcUoTKumtgyOQ8Pag_mfma50K4N-wKiYkBS3Pz-AjcoKaTuQkyEXoSUCP4dvtZxsAHD9PnQcJoOpXVZ3mBWDkfVCIpHBvDSYNo1LQblskOFfsMCvbKDNKOZkINFVWmVfNQWLSU7jx4KhDLFfJw3nbM5rta1o0Ddbm4Bx9_fPDVFlVDNSkvdHF2LJ0fLVi0qlbScJWr83Dt0yfTxyeSJrrqyn6H7tEJCUM8a3cwuOGq6-aRXeNovE-6rctftU8Trb2AliR8Q4oll99wkcfTIh_qfGqUNpFBEfO659nfFEyn0PvaSN7qptPtrueLlbI9onZfAD9YZO1OfzrQGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2752783b15.mp4?token=XJ043eWcUoTKumtgyOQ8Pag_mfma50K4N-wKiYkBS3Pz-AjcoKaTuQkyEXoSUCP4dvtZxsAHD9PnQcJoOpXVZ3mBWDkfVCIpHBvDSYNo1LQblskOFfsMCvbKDNKOZkINFVWmVfNQWLSU7jx4KhDLFfJw3nbM5rta1o0Ddbm4Bx9_fPDVFlVDNSkvdHF2LJ0fLVi0qlbScJWr83Dt0yfTxyeSJrrqyn6H7tEJCUM8a3cwuOGq6-aRXeNovE-6rctftU8Trb2AliR8Q4oll99wkcfTIh_qfGqUNpFBEfO659nfFEyn0PvaSN7qptPtrueLlbI9onZfAD9YZO1OfzrQGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
شبیه سازی سیستم عوارضی تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66219" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66218">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f287535d76.mp4?token=XhOMa48k32O0mguZ7LbqZoLj4sEJjpePQt-FYTIJTPhYtCJk2F-0aW1VKi2s6zbTEOOsnmh-hNV-Qmc4y0iUxt6bV0eYXWgUxVkaXBtL0WdjTNL9fgdI9buPJs4dtDMn4kCgUeZabXVIzq32CxVt6-yxQUyIds-MVHrWpW-3osv9nUlQGynsJIr2B5cqj6ha6IalZmBTOGA1bg3SDdakwrNEE5AgUPcDemJeubw4NA-vCC9Zm4e0fJbUDHkVdKRRFa4Jp2z6A7WKrfLBoGgZjy913v38YQ8VfO5N-7TCJpYnTqx3JBg0elQb2jBh9XYpE2JMP5YLW95oz4w36GOzHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f287535d76.mp4?token=XhOMa48k32O0mguZ7LbqZoLj4sEJjpePQt-FYTIJTPhYtCJk2F-0aW1VKi2s6zbTEOOsnmh-hNV-Qmc4y0iUxt6bV0eYXWgUxVkaXBtL0WdjTNL9fgdI9buPJs4dtDMn4kCgUeZabXVIzq32CxVt6-yxQUyIds-MVHrWpW-3osv9nUlQGynsJIr2B5cqj6ha6IalZmBTOGA1bg3SDdakwrNEE5AgUPcDemJeubw4NA-vCC9Zm4e0fJbUDHkVdKRRFa4Jp2z6A7WKrfLBoGgZjy913v38YQ8VfO5N-7TCJpYnTqx3JBg0elQb2jBh9XYpE2JMP5YLW95oz4w36GOzHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:
جمعه در سوئیس تفاهم امضا می‌شود و پس از آن اولین دور مذاکرات بعدی را خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66218" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66217">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !  هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66217" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66216">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awv_LwDCB4qyXOq0-1rG-vM0IT2qvGHfFyOEljFp0Cqmud2ihlUv80Nc74OhXVVcPCAPAaI_oWrQTwYcmeoID-YdAl8MXDJbLKt4dTbzrOhGxvI4d--fq5EKPqGy96Vm4VgnNSvi_2eqEsXmuIXOB0eFdKiSGg6Mo5Wn4YjOjHifn-Qp25GSflgV6MJdxCNGX0Y6eGN8X-Bk8V0_xC7JjJKlvnbgR5wZcg2NJ5wB-KzCAZJvch1KtGLaK3YQc7DK_DIAvHNug5-HRgpr_vu-c63y17S8pbkOOrOlzGNN2nGDezNNN9oEkpxfCNaEct1ZlgYdbQZMEH92ZYd5-tohwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !
هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66216" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66213">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0lJhraJuOB2f5i96ZTOgK_Q31_2n41beMEJJZgBmrbH76NoGYjnmIXejKoequoVQj1GnKXgc0zXJPM5IWbphUBtFAp4WoR9XJzg5WdNaq6pYzV5a2erP1QnLDZjnXGL49mZSG2VZGgUn8w4h8AyEIpQuZLjRVwdV_gSG3rQLzwAP2x7oa1C4Tcs2H2NlvcdZPvZWtYUxeuxQ6X5ugWKkvESLSqVJrBHe3SRnlQ9y9esTlZudXAaxP54jcepUQjpOv_FYXKxrr2KuCcbXw178fAuMXYC4A2-rXxUFJGIPYsBvZcaBt31aLAc8rpdWGe55ru2tHLeg5b3C7o8ZrL30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mS6yzxDIQx859C1duVgpMHuG61ena8lIx10WdKaNoVVf1pBASyiwytacoIv4X6b0inGepfuSUoupXntJpGFARAiGFTjztv15qUPXKIZuN7aBvNByCKZzm1_q5WZ1kHHjSXzVGzW0HBIF_ucvJ68VVOhYQPLP7eqj3A39fMwp6z_mcZUsdQx9zdEddvYJ7sK-A-Zi9AodKXNRUW1UcOcP4sbrjlcQTnShlQwToUIcrE42NBQZVctQNbHV_rZuR1guyrJK5OHZCUPHyjxb0C7az7cjk6XwsmqV4w6GGlk8w0b-JkPalshsEmfXIgQnEcdurIoHbFsugKmjMdyT0_YEWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8fefe1cb.mp4?token=ml40DejWXt9zJXlL9_dSpvr-LFQZDOA7ky8C_yHF2uJsRamkewqMUmgF7XleMPNqoLAtDJJvf4y82x-DftnRzK9s6XNbzicVtYMkwQglw6eK5e--W7H_FOaT5ywKuvRT8OAISNONf3gd2V9-eDfmBJZhsj12Ivapx5O9X-wnRZHTyaVKuYzJ61iea8CD3bDalJAAyK03kqFS2d4G1qI9IjmBJBN7Gh9ncZFKPE0hFpyMKNQqONDrQp7arXOlgCJ4AeS-f4S-umEnegyo64jtnxYP6EMrCQ4q5zFlZ-lGFSz4YgYy9tQYUs2FtfN_JnzI-a4aSnnS5JGhOYPDXlwTEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8fefe1cb.mp4?token=ml40DejWXt9zJXlL9_dSpvr-LFQZDOA7ky8C_yHF2uJsRamkewqMUmgF7XleMPNqoLAtDJJvf4y82x-DftnRzK9s6XNbzicVtYMkwQglw6eK5e--W7H_FOaT5ywKuvRT8OAISNONf3gd2V9-eDfmBJZhsj12Ivapx5O9X-wnRZHTyaVKuYzJ61iea8CD3bDalJAAyK03kqFS2d4G1qI9IjmBJBN7Gh9ncZFKPE0hFpyMKNQqONDrQp7arXOlgCJ4AeS-f4S-umEnegyo64jtnxYP6EMrCQ4q5zFlZ-lGFSz4YgYy9tQYUs2FtfN_JnzI-a4aSnnS5JGhOYPDXlwTEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش‌ها از سقوط یک بمب‌افکن استراتژیک B-52 آمریکا در کالیفرنیا خبر میدن.
این بمب‌افکن دقایقی پس از برخاستن از پایگاه هوایی ادواردز دچار سانحه و سقوط شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66213" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66212">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMain Online پشتیبانی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqXZcvsMR1bpFxCkDU2WjdzhSdJBI9gVdxSm-4TQGbxIt8BRyH7PBPzpBKVe6fkR7fRQhKntqQatd1OtRQ95FWY3RJdo15zy5bzA-en3DLmE5n6m2MtXXrLFTG5pFk5A50eDEetkmJlX6YnMPTx5I7tmZgcV0lEFPc4yHa_HhP9h0ihek3aVCKOZIHcDdDzSeWUzqxdOAPDAdxWxuS1YYB6kOMzdweVvR5-Hc9FGvRqigmliv5utTnt8xyZy8FCmAulkLpnlZfVwXFvQdUCim6xKa2_B8P7hBsUcOo38O6f7vYb3JEvpPex698GdxiHgOXi8BYUL7zZLQ2sSVp1ibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فیلترشکن فقط گیگی ۵ هزار تومان
✅
👥
| بدون محدودیت کاربر 999+ نفر
🔥
| بالاترین کیفیت یعنی تانل شده
🎁
| کد تخفیف : 50
▫️
5 گیگ 25 هزار تومان
▫️
10 گیگ 50 هزار تومان
▫️
15 گیگ 75 هزار تومان
▫️
20 گیگ 100 هزار تومان
▫️
30 گیگ 150 هزار تومان
▫️
40 گیگ 200 هزار تومان
▫️
50 گیگ 250 هزار تومان
⚠️
| تنها راه خرید مراجعه به ربات
🤖
| ربات :
@YOUPINGROBOT
⚡️
| ارزون ترین قیمت بالاترین کیفیت</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66212" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66211">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007bf57d46.mp4?token=kKNU0vED5W_k-lP3pjwgAmnuxvNaz0F0wEPSU_gVZW0pNf04LNzrxpEO1kS-sqc2sHlkbf7jLbELD6yAys7Wb-grkxYaXbMpr7Zkq1M4iwjAubN0GOjuKbcIE5oGm6sRvg3ARx_ekcMi6dxvWME4zAcvHDATVLuN2w0vvD7SDFRx0tpQVOqNwa7LoYf6vRZhGImEDv5mt-i_T77nD5EWJ9NkJcqjt1xC6GpgvNpJk7nQcvbRdwiDKT3G3weyQ44JppSE7OyFo4A69KQFvMkHR2DXIHsQvdHzNksFlTym9ofOH_L-Kug_w-HTjU6Nt5QyedFsu1OdstsyWTGDlsS9eDhOGMmy3EskGlVR_HQ1FFB248s0USrLglDn-GEltp9CZurJUwR1mrs5iRTjE6EpTUGSiGaTEsIwePD1Wzg3rfFTFqK0GFexWa0mqyLMfHcKJ_oIwCvxTI2CjeOZG1GOJOp-CS0yISBzVUYjCY_Hi6qDvqlRdR4d1h5SieUmqB9iWzMDEBeK8PKIttYt6BPoK23SECMr9RoMtJXLP2ZGNXVk-5HCbTX7mrQA_VnTzBw4teiTyW7K5_kLqcooeFEzwV9PYMLb_j6EnBpqhASviVVi_z2CdKOb5OHRx8u8Ye6eugwuNrycLkqkGWMcRyq0AQmHWmjacDnV_stwJBYXA_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007bf57d46.mp4?token=kKNU0vED5W_k-lP3pjwgAmnuxvNaz0F0wEPSU_gVZW0pNf04LNzrxpEO1kS-sqc2sHlkbf7jLbELD6yAys7Wb-grkxYaXbMpr7Zkq1M4iwjAubN0GOjuKbcIE5oGm6sRvg3ARx_ekcMi6dxvWME4zAcvHDATVLuN2w0vvD7SDFRx0tpQVOqNwa7LoYf6vRZhGImEDv5mt-i_T77nD5EWJ9NkJcqjt1xC6GpgvNpJk7nQcvbRdwiDKT3G3weyQ44JppSE7OyFo4A69KQFvMkHR2DXIHsQvdHzNksFlTym9ofOH_L-Kug_w-HTjU6Nt5QyedFsu1OdstsyWTGDlsS9eDhOGMmy3EskGlVR_HQ1FFB248s0USrLglDn-GEltp9CZurJUwR1mrs5iRTjE6EpTUGSiGaTEsIwePD1Wzg3rfFTFqK0GFexWa0mqyLMfHcKJ_oIwCvxTI2CjeOZG1GOJOp-CS0yISBzVUYjCY_Hi6qDvqlRdR4d1h5SieUmqB9iWzMDEBeK8PKIttYt6BPoK23SECMr9RoMtJXLP2ZGNXVk-5HCbTX7mrQA_VnTzBw4teiTyW7K5_kLqcooeFEzwV9PYMLb_j6EnBpqhASviVVi_z2CdKOb5OHRx8u8Ye6eugwuNrycLkqkGWMcRyq0AQmHWmjacDnV_stwJBYXA_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
مصاحبه با رکورددار عمل جراحی در ایران: بالای ده میلیارد خرج عمل کردم که همشو دوست پسرم میداد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66211" target="_blank">📅 23:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66210">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b5122b70.mp4?token=Zi_yHpqHy0ymC9V860jzE6IF6y7wDefne0xXgbbU4HTWdImZJ98KEvJHSajaiY5oE7s115RNEUr6eCNXEMM3cxwQOExTrIs-daF2cdII0pcwBf9m2Z5wmSp5-tlDuDqmhi2NWv98dmnc8Hsobb0qHAXvOpTme36mon74Du90q3x6tjPAjRPPpK6L36jqiylmLRgVfuKhRonMKRI-81ZvxwTpdZYTDGtg_cu3vv7WO0V4mHfSjILURP77IJgpjMPpOK1UrNCf2Exy4zjFzOeXI295mNp9R2R6fsmxspV_zmKPsJs70Wz4oz_2ulbx5ECqRhWY9SkJ2KYb4KVSNusMjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b5122b70.mp4?token=Zi_yHpqHy0ymC9V860jzE6IF6y7wDefne0xXgbbU4HTWdImZJ98KEvJHSajaiY5oE7s115RNEUr6eCNXEMM3cxwQOExTrIs-daF2cdII0pcwBf9m2Z5wmSp5-tlDuDqmhi2NWv98dmnc8Hsobb0qHAXvOpTme36mon74Du90q3x6tjPAjRPPpK6L36jqiylmLRgVfuKhRonMKRI-81ZvxwTpdZYTDGtg_cu3vv7WO0V4mHfSjILURP77IJgpjMPpOK1UrNCf2Exy4zjFzOeXI295mNp9R2R6fsmxspV_zmKPsJs70Wz4oz_2ulbx5ECqRhWY9SkJ2KYb4KVSNusMjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ پای تلفن به دستیار نتانیاهو:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66210" target="_blank">📅 23:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66209">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این BISS کد جدید شبکه سه و ورزش رو Starsat چیه شبای اول جام جهانی اوکی بود الان پریده! دایرکت بدین  #hjAly</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66209" target="_blank">📅 22:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66208">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏
🚨
🚨
نتانیاهو برای استقلال نظامی ارتش اسرائیل بودجه دیوانه کننده ۱۲۱ میلیارد دلاری اختصاص داد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66208" target="_blank">📅 22:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66207">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این BISS کد جدید شبکه سه و ورزش رو Starsat چیه شبای اول جام جهانی اوکی بود الان پریده! دایرکت بدین
#hjAly</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66207" target="_blank">📅 22:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66206">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=iTJ4MBrRezeTls7Q1i6-nAdY0MRQNdKpvjRqR16JUh6pJsLJOQDf78Gihk3r57fCBVLrD81lOLlSZ7Y0JxV47BrnVHeqs2VaqKB7j7KkD24RXrMr_N7vLY7OcKITreY3By25njAQ_5DJ8eTseaCy-_JUt57bqBpxw8NblbV5xrR371XckpnYYQwMHOntS6yPaSebbnpccptyfnIbNSBjyMc8d_iRv4l3A-V-mnkHMXpjzDVwricy5pYw70JdOrkumsUaVb8w_BBO2zTGavrgRETeGG1u5OvSPRTtnRCgArN6PwhwRhWEP5Z6Um6z1g0Hn7VwNRFDOZmSUZK_dFmIBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=iTJ4MBrRezeTls7Q1i6-nAdY0MRQNdKpvjRqR16JUh6pJsLJOQDf78Gihk3r57fCBVLrD81lOLlSZ7Y0JxV47BrnVHeqs2VaqKB7j7KkD24RXrMr_N7vLY7OcKITreY3By25njAQ_5DJ8eTseaCy-_JUt57bqBpxw8NblbV5xrR371XckpnYYQwMHOntS6yPaSebbnpccptyfnIbNSBjyMc8d_iRv4l3A-V-mnkHMXpjzDVwricy5pYw70JdOrkumsUaVb8w_BBO2zTGavrgRETeGG1u5OvSPRTtnRCgArN6PwhwRhWEP5Z6Um6z1g0Hn7VwNRFDOZmSUZK_dFmIBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چرا ترامپ مانند بایدن عمل کرد و چنین توافقی را امضا کرد؟
نتانیاهو: من این مقایسه را نمی‌کنم.
ما هنوز نمی‌دانیم توافق چه خواهد بود.
همچنین نتانیاهو درباره انتخابات گفت که قصد دارم نامزد شوم و همچنین قصد پیروز شدن را دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66206" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66205">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
نتانیاهو درباره توافق ایران ترامپ:
این توافق توسط ایالات متحده، توسط رئیس جمهور ایالات متحده، حاصل شده است و او معتقد است که می‌تواند هم به نظارت و هم به برچیدن برنامه هسته‌ای دست یابد.
گفتم: این تصمیم اوست. تکرار می‌کنم: این تصمیم اوست. او آن را رهبری می‌کند.
البته، من نظراتم را در گفتگوهای مختلف بیان کردم.
از سوی دیگر، گفتم که ما منافع خودمان را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66205" target="_blank">📅 22:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما ضیف، هنیه و بسیاری از رهبران حماس را کشتیم ، تقریباً همه آنها را.
فکر می‌کنم هنوز یک نفر باقی مانده است؛ او هم کشته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66204" target="_blank">📅 22:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66203">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
در ایالات متحده، می‌گویند که رئیس جمهور ترامپ هر کاری را که من بخواهم انجام می‌دهد، و در اسرائیل، برعکس می‌گویند که من هر کاری را که او بخواهد انجام می‌دهم. بنابراین این درست نیست، و این درست نیست.
این رابطه بین شرکایی است که مدت‌هاست یکدیگر را می‌شناسند.
بسیاری از اوقات ما موافقیم؛ گاهی اوقات نیز مخالفیم. این در بهترین خانواده‌ها اتفاق می‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66203" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66202">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
من نگفتم هدف ما سرنگونی رژیم ایران است
بلکه گفتم که می‌خواهیم به ایرانی‌ها در انجام این کار کمک کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66202" target="_blank">📅 22:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66201">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
نتانیاهو رسما اعلام کرد که عقب نشینی نخواهد کرد؛ نتانیاهو، در پاسخ به یک سؤال:
«جمهوری اسلامی می‌خواست ما از جنوب لبنان عقب‌نشینی کنیم، اما من بسیار، بسیار، بسیار قاطعانه امتناع کردم—و ما این کار را نخواهیم کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66201" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66200">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ترامپ توافق را با جمهوری اسلامی منعقد کرد و این تصمیم اوست و ما منافع خود را داریم
آمریکا به تصمیم ما در مورد منطقه حائل در لبنان احترام می‌گذارد.
روابط ما با ترامپ مبتنی بر مشارکت است و نه بر اساس تصمیمات تحمیلی
ترامپ رئیس جمهور آمریکا است، من نخست وزیر اسرائیل هستم - من از منافع خود دفاع می کنم.
مواردی وجود دارد که من و ترامپ با هم اختلاف نظر داریم.
مهم است که از منافع امنیتی اسرائیل به طور متفکرانه و مسئولانه دفاع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66200" target="_blank">📅 22:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-tIXyMzLeWBFnrjpNqB1kJyqdSHxmO4is1bdVLuuRgOupPTd_86fwBok3yJTH-WE1G53Z_3kti74yxH8nYqKnXsBJdxdn4AzcPdPiYbNSDbdIn1RGkvwGcHuzaqjPDIM7M0eCRFu3ztDjFyqRNPa5KFSqARYCFpdqw6RvCCSo7e-qUud3H9OskQ4cMnoUNRckpLKsTusirX0FWI89PKgFSIkxHNhREz0MDlQ50ZUkVvVmU7iIMAn9f1HTWjTHMg2N6MQehul1qwzoQkrOD6KWI9BwiOX5gwEN5ESuR4Mq2w27EHx_UJJR8WyJZima-TL7Ry9gPBGaVfYHBtU9aHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇸🇳
سنگال
🏆
جام جهانی ۲۰۲۶ - گروه I
⏰
سه‌شنبه ساعت ۲۲:۳۰
🏟
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📝
نگاهی به آمار دو تیم:
- فرانسه برای
هفدهمین
بار در جام جهانی حاضر می‌شود و
دو عنوان قهرمانی
در سال‌های ۱۹۹۸ و ۲۰۱۸ در کارنامه خود  دارد.
- فرانسه در جام جهانی
۲۰۲۲
در یک فینال دراماتیک از مسی و یارانش شکست خورد و
نایب قهرمان
شد.
- سنگال پیش از این در
۳ دوره
جام جهانی حضور داشته است.
- سنگال در جام جهانی ۲۰۰۲ موفق شد به جمع
۸ تیم برتر
صعود کند اما در جام جهانی ۲۰۲۲ در مرحله گروهی
حذف
شد.
🧠
تصمیمی که برای جلبِ توجه گرفته می‌شود، خوب نیست.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66199" target="_blank">📅 22:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66198">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33dfcb5d1.mp4?token=nCJBeJyJDl9aa-4gMBtPyaTG_ENSiLl63pU6Nhg8Ahf3X2q0loKxKZOCX0B8XO0y36hJUPRQ73wzXhDW2dsgisJXg621r9HoIEV-14qUgK4rCmoRfs9uzlVqHpYhEWk8AjuuBAorzomMlotwS3o4BIaBrlMDlS1zEJVW5_CKb8RzEXKgpbTLxeEogdjZuGQyqWeXBLLVx1r3joIXtmOTEU2ZY3YirdwNeGzNqbwGBlCbZaNl0v6SDX7b0erAR3BNBenAdqBaaDmaKeJNIzGUpiu8cHd0eLCBpodgNuI3ItSt8S0SoDWX96OPaEcIOAHea9Y14mWUvfA7Zze5flpgQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33dfcb5d1.mp4?token=nCJBeJyJDl9aa-4gMBtPyaTG_ENSiLl63pU6Nhg8Ahf3X2q0loKxKZOCX0B8XO0y36hJUPRQ73wzXhDW2dsgisJXg621r9HoIEV-14qUgK4rCmoRfs9uzlVqHpYhEWk8AjuuBAorzomMlotwS3o4BIaBrlMDlS1zEJVW5_CKb8RzEXKgpbTLxeEogdjZuGQyqWeXBLLVx1r3joIXtmOTEU2ZY3YirdwNeGzNqbwGBlCbZaNl0v6SDX7b0erAR3BNBenAdqBaaDmaKeJNIzGUpiu8cHd0eLCBpodgNuI3ItSt8S0SoDWX96OPaEcIOAHea9Y14mWUvfA7Zze5flpgQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما آسیب عظیمی به اقتصاد ایران وارد کردیم؛ برخی این خسارت رو یک تریلیون دلار تخمین میزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66198" target="_blank">📅 22:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66197">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3fc5d08d.mp4?token=SR2mE_fQUEK_HAcbV_iOw-CSRtg6VKgZILvCxD7NAf9kiB14TnlZRrctU90KY1whVDJFbub38vmvH4JrLdtY_1slBkFEGcU9jl150tKFnX3IYN4FdUyulUZRPcmJEkgSoReOPp3IPU_UxkEPI5FLLxmZz9zOOrvDcF27ZUVuSFa8XoUBoGQ4zp9CV4vgI-K-OcK51WHy-a2-EVT_TXiYyfoH-51vx5vfsNhycCJ4IT_FvJeywerSlNEFWe0ee7NbtRoD1h8zyhRagOgdLLOzuF_gwseBnjFuzjbMgh0Ur9djB2Sj-Nw-0ikljeGFaEqlpX-gx-z1gtES-QUrDUVbBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3fc5d08d.mp4?token=SR2mE_fQUEK_HAcbV_iOw-CSRtg6VKgZILvCxD7NAf9kiB14TnlZRrctU90KY1whVDJFbub38vmvH4JrLdtY_1slBkFEGcU9jl150tKFnX3IYN4FdUyulUZRPcmJEkgSoReOPp3IPU_UxkEPI5FLLxmZz9zOOrvDcF27ZUVuSFa8XoUBoGQ4zp9CV4vgI-K-OcK51WHy-a2-EVT_TXiYyfoH-51vx5vfsNhycCJ4IT_FvJeywerSlNEFWe0ee7NbtRoD1h8zyhRagOgdLLOzuF_gwseBnjFuzjbMgh0Ur9djB2Sj-Nw-0ikljeGFaEqlpX-gx-z1gtES-QUrDUVbBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
هر زمان که لازم باشد اقدام خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66197" target="_blank">📅 21:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66196">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e4d0c9fa.mp4?token=HmVZwOS_DKaCSAh88inDDLPD3xen5zUG3oRt7ZWFeiurg4sqRNiyfJymYHgl2qxYwfvCv7bmSj09rVu5OAH5UUQ8vNOKneEJM1KIG97kXxfysjdFhs5s_EddUvEyLMuCgEuN4ul6Y8nmYy-hiHmAyzG_B7lyFOZmK0FoXTxMrM833fOOWp3PDvML_plwDZbVnVMmWjUSiC4fg43fyFPfpsG0aN4bOCn5-wN0RHapZV6lDYOKeTG7WWmZadVJEUaRh4caPk0tVCNpX9nNysooLp3Z1TpxOxyOY53llsN8FjAqUIyeyifyUMVTfNfkfc8vocA7YhSGK7a7hWVBdRIHsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e4d0c9fa.mp4?token=HmVZwOS_DKaCSAh88inDDLPD3xen5zUG3oRt7ZWFeiurg4sqRNiyfJymYHgl2qxYwfvCv7bmSj09rVu5OAH5UUQ8vNOKneEJM1KIG97kXxfysjdFhs5s_EddUvEyLMuCgEuN4ul6Y8nmYy-hiHmAyzG_B7lyFOZmK0FoXTxMrM833fOOWp3PDvML_plwDZbVnVMmWjUSiC4fg43fyFPfpsG0aN4bOCn5-wN0RHapZV6lDYOKeTG7WWmZadVJEUaRh4caPk0tVCNpX9nNysooLp3Z1TpxOxyOY53llsN8FjAqUIyeyifyUMVTfNfkfc8vocA7YhSGK7a7hWVBdRIHsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ما در لبنان خواهیم ماند.
کار با ایران ممکن است همچنان تمام نشده باشد
ماموریت زندگی من مبارزه با برنامه هسته ای ایران است.
با توافق یا بدون توافق، ایران سلاح هسته ای نخواهد داشت.
اگر برای حمله به ایران عجله نکرده بودیم، به بمب هسته ای دست می یافت.
ما رهبران ایران را کشتیم، به سرویس‌های امنیتی آن آسیب شدیدی زدیم و اسرائیل را از تهدید هسته‌ای ایران نجات دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66196" target="_blank">📅 21:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66195">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
درگیری شدید طرفداران تیم ایران با مخالفان تیم قلعه‌نویی در لس‌آنجلس ساعاتی قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66195" target="_blank">📅 21:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66194">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0695d77536.mp4?token=NPtDOEMs9SLubRNCNXlaTqYga20gHmSIL8RBR5WZnZoREuCvbgn81QnVja-HPUTUXMc4guwpboOjRf1iVX55U1fQh-pTu8GTtM97JWxacYaIJiobSxSfeVzyvcj44c1jBJBxuy-JZnvmG-TLu3I_SlnVXp9GWpiR8TkVr2fV3j5BFBE94E6IQwurID_-XlEbNWfFKN2jbc5Uo1L0qvdl6vNksOaqPzFWYRaqz-uYmVhvyT6i_LZ4a3o85Ca045YYxvAJxVqmYosgE7nI6rAKgF6riCJ93tuZ9YKxnDWJwBroWbbhGNAKrS1A_uQewD5lFF9IpB1-gCG_jl2v_XfFRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0695d77536.mp4?token=NPtDOEMs9SLubRNCNXlaTqYga20gHmSIL8RBR5WZnZoREuCvbgn81QnVja-HPUTUXMc4guwpboOjRf1iVX55U1fQh-pTu8GTtM97JWxacYaIJiobSxSfeVzyvcj44c1jBJBxuy-JZnvmG-TLu3I_SlnVXp9GWpiR8TkVr2fV3j5BFBE94E6IQwurID_-XlEbNWfFKN2jbc5Uo1L0qvdl6vNksOaqPzFWYRaqz-uYmVhvyT6i_LZ4a3o85Ca045YYxvAJxVqmYosgE7nI6rAKgF6riCJ93tuZ9YKxnDWJwBroWbbhGNAKrS1A_uQewD5lFF9IpB1-gCG_jl2v_XfFRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نه جنگ خواهد شد نه مذاکره خواهیم کرد
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66194" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66193">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtXrkMz8hutzSu-DdMnMwkXiz5JCmbTOwqGIpq-3AERqhxJ72S4CTRfXjIuaMMnm3YulRqUtwSV_D_FI5IEUsuhKwYfG-6sLU_IcXdoNbCx3Hs_rUCJgYapH3QPhV68QfqTw_jwepMiOHTFN-v4qcl-Em2kk_-oWNmOKsIpVbViOQSl8jnewwL7n3R8g5o5CUbhoE6390D2noZq9AW-7KU8SV5MPt5b9vgIxhMsJEvq4rVr4I51nTFgh6CEV5pKlMZAh4uhJ-6r-HYywXnj-mayQ59RN3IOSe6OaAF22ESqhfcHilfRzkp5U2uIGLI_9-VFc-UcnDYaZtK4C1Cu_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد از تلگرام بدون نیاز به ممبر و تولید محتوا؟
سیستمی به اسم MTP وجود داره که باهاش میتونی وارد پروژه‌های واقعی بشی و درآمد کسب کنی.
✅
بدون نیاز به ممبر
✅
بدون نیاز به فالوور
✅
بدون نیاز به تولید محتوا
✅
شروع سریع
✅
آموزش کامل و پشتیبانی
🎁
فقط برای ۳۰ نفر اول:
سه پروژه اولیه بهت داده میشه
مبلغ هر پروژه ۲۵ میلیون تومنه
یعنی از همون ابتدا امکان رسیدن به درآمدهای بالا برات فراهمه
اگر میخوای جزو ۳۰ نفر اول باشی، وارد کانال شو و شمارت رو ارسال کن:
👇
👇
👇
https://t.me/+QpsFnjSfC382MGQ0</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66193" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66192">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24683d102e.mp4?token=GFVSV6HzqTFCRcEevsOs8FXMTFUtBHdLundpA0Kw6upyMPZ4utIG-oyxH3SSd5FWY1Wh2MgM6apKEgFYEw1VKnR_aUYTopF4gJmBwQeeCeVqSDAS0AZfMrNShmK0ak69WWUXcR39YZFjPKmInstzl3NjKW42VUYuyxDB-c3vGx-HmQ9QSZ-rAHqC3qALGEmBXkZPB1I662mEltIBESOZ_4RwyRxschopPNRehICXQJ3j4PKHmm2ZMwn1NHacsuk4acLitcAPnaMQvIOu2BcoHYL8tPbluJNLYq4_rw9Mh8GCciXXQgNaM_F4h_urdr58c_-v9TcjfkXMExwsbsHbuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24683d102e.mp4?token=GFVSV6HzqTFCRcEevsOs8FXMTFUtBHdLundpA0Kw6upyMPZ4utIG-oyxH3SSd5FWY1Wh2MgM6apKEgFYEw1VKnR_aUYTopF4gJmBwQeeCeVqSDAS0AZfMrNShmK0ak69WWUXcR39YZFjPKmInstzl3NjKW42VUYuyxDB-c3vGx-HmQ9QSZ-rAHqC3qALGEmBXkZPB1I662mEltIBESOZ_4RwyRxschopPNRehICXQJ3j4PKHmm2ZMwn1NHacsuk4acLitcAPnaMQvIOu2BcoHYL8tPbluJNLYq4_rw9Mh8GCciXXQgNaM_F4h_urdr58c_-v9TcjfkXMExwsbsHbuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
آخرین مکالمه ترامپ و نتانیاهو بعد توافق:
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66192" target="_blank">📅 20:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66191">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a708e029d7.mp4?token=QjZ2tmPvRP8tvvrZQ7xDXaUXxplVJWW9jeRr1a0nRfqzZLDUA40iiy31ZcpKKzmNANChOhBM-GSp35hijE5kizq23Ushole97Fq28MRfDzegajAKtfxqZ3i2f8zyVieVuDbAf1PI69PVSaTXcvYGWWRX7rRa2ZR57htD7OIeNnHBt4yFgSUAOI8slbm3Y_KIYoylAkTo8foA-VHx3gtdPlEUC1e4tZ3GBxaTDDeFtiY8ecUBEK-ksiYwQlwwzShUKuwvQ_bpBOl9S4ulC6q0sETd_L6SJmI030nN7e9V0CbzqLkSfgMOsSq3bhSN_pvu7FsprCAOdutvtjS6g9fq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a708e029d7.mp4?token=QjZ2tmPvRP8tvvrZQ7xDXaUXxplVJWW9jeRr1a0nRfqzZLDUA40iiy31ZcpKKzmNANChOhBM-GSp35hijE5kizq23Ushole97Fq28MRfDzegajAKtfxqZ3i2f8zyVieVuDbAf1PI69PVSaTXcvYGWWRX7rRa2ZR57htD7OIeNnHBt4yFgSUAOI8slbm3Y_KIYoylAkTo8foA-VHx3gtdPlEUC1e4tZ3GBxaTDDeFtiY8ecUBEK-ksiYwQlwwzShUKuwvQ_bpBOl9S4ulC6q0sETd_L6SJmI030nN7e9V0CbzqLkSfgMOsSq3bhSN_pvu7FsprCAOdutvtjS6g9fq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: توافق شامل هیچ‌گونه تسهیل زودهنگام تحریم‌ها برای رژیم تروریستی جمهوری اسلامی نمی‌شود.
ترامپ در پاسخ به پرسشی درباره احتمال کاهش یا تعلیق زودهنگام تحریم‌ها علیه رژیم تروریستی جمهوری اسلامی تأکید کرد چنین موضوعی در توافق وجود ندارد و افزود این مسئله در نهایت به رفتار رژیم تروریستی جمهوری اسلامی بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66191" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66190">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66190" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66189">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKJ7qdqmP3zmQ1tDQdIw3Y4helSIFK5G7SeeDv1qd8kGr5Rle2Eanh57Up9XbAnN5Gv-YR_fUcnqkmhlTlN_lvfpkwP3k9YSwkmS1zppiW2BQW9IKwgKYggCrCKO5VHtBTEHmkM1DQZUprlEeyCTdYsgKeVWUxLC54MNeKNP1oYKRSDbcvvgGAgD0MLqboeDdd0S3JeqDOKMEddhpkGOtFbAc0yLQvqclrxGhkCRdCtzkSE2qTCKWz7GJP1tlPEu1WmrILDotNXiSsZy9JLTRwc9Ea8yvvNn_fsbGEoaZM-WoNNLzeU6GuD-WEOWJnjCCPBO_gGwqypY-bifEt-lpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66189" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
