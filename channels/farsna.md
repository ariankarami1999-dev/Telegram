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
<img src="https://cdn4.telesco.pe/file/tYkMKLnoeTD2sPHGSgQ6IzpU7WrzTjRsZouFsViv-qLAO_q4Yd3MWP3mX4WBY2S-u1PYwIBHtuIs57s4vpttsRQ_p55LLkcXXJEh2LXuQFwKJxLgd4D2YFpZSwOyezPAz7ZLvIC-Ug7_KqlowaGCYQ0cXLCbwaM8Jo_4yMBYGNY-htPE0raHtx4U3U6MjpryskmfFcfDnBZVjehMoGYJtZ7S2jvocnj-oU9PqT2iVYq9OpKR8ncVee9kcqa7J1WUWO0hKPKiODRdL_XP7rb4xiXEexytWUzMlBnzDMn-CNhmreCyJbsx5yzD5yMN158ChXBIE7_0t6OK7MerRGsznQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 01:01:02</div>
<hr>

<div class="tg-post" id="msg-461908">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjgViBfdcrnCGJF37R0lVXbVtz2WwtpnSBnn5DD5KMxBUHGSWf8W1nHJamn_86ny1eGXgzUTD9tHFmuSV_VjKuueoXEOoPWizcgrbS6BTMSkYv15bOHzYXOK-bPj1cFDTXUx6N5YK1cDFQtN30W4735dddxVWmM-eX7_syR-bPxh3LD2Vfj3pPTH8U13t5BrmnfWmrHe8gNdSRZ84gtj_wIx9ZoRODbI8OzVUweMe3J9hEiP3BW0qw3fNwuBYQ9trCp93_6sN6sbpwTvcwd82Rppz1OiRHHxFVVjwV_ZmiOikamoiW-L6Kn5NeIe-ZIzs4MvwwQLoHpJqgu0a3oZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۱۲ خبر خوب از ایران
🔸
از شکستن انحصار خارجی‌ها در نیروگاه‌های برق‌آبی به‌دست متخصصان کشورمان، تا بازگشت ۵۴ هزار دانش‌آموز بازمانده از تحصیل به چرخۀ آموزش @Farsna</div>
<div class="tg-footer">👁️ 746 · <a href="https://t.me/farsna/461908" target="_blank">📅 00:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461907">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزیر آموزش‌وپرورش: مدارس دولتی حق دریافت پول از مردم را ندارند
🔹
هیچ مدرسۀ دولتی حق ندارد از مردم پول دریافت کند و برای ساماندهی این موضوع، اساسنامۀ جدیدی برای ادارۀ مدارس تدوین و در شورای‌عالی آموزش‌وپرورش تصویب شده است. @Farsna</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/461907" target="_blank">📅 00:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461906">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e5fa97ae.mp4?token=NS4fcZ35JTLe1Nl9gdJgnVzu6RnPaa66VNNNCd0TipUaq02Kd-iVsPgh1FH7zOUYc29sX2lOVC4otsdqlf2NEf5TqIDpdnzg0m1-ku9lUAxcQYLD4L0zfchBdIP8HrqWZ5xl5NF3pXTXqr4EpJhn_8zFXL5dPkGMv-e0P9_kFW21OErvb5zV1qCbkTN2pKkOaupvq5nThRiYud8UVlp81-q2Y3mXrt-d1xuDzJv5YRQxL-bDDIk6bK8YWI5xIvojZ9p0xK5R9V4fBFtggoXf3LC0bX-1xJfn_i1DPp4scNmbLh5YJLTYPKh1UxbNmkQo1drujizWQtFCJ2ueXyffiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e5fa97ae.mp4?token=NS4fcZ35JTLe1Nl9gdJgnVzu6RnPaa66VNNNCd0TipUaq02Kd-iVsPgh1FH7zOUYc29sX2lOVC4otsdqlf2NEf5TqIDpdnzg0m1-ku9lUAxcQYLD4L0zfchBdIP8HrqWZ5xl5NF3pXTXqr4EpJhn_8zFXL5dPkGMv-e0P9_kFW21OErvb5zV1qCbkTN2pKkOaupvq5nThRiYud8UVlp81-q2Y3mXrt-d1xuDzJv5YRQxL-bDDIk6bK8YWI5xIvojZ9p0xK5R9V4fBFtggoXf3LC0bX-1xJfn_i1DPp4scNmbLh5YJLTYPKh1UxbNmkQo1drujizWQtFCJ2ueXyffiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سپاه: ۱۱ جنگنده و بالگرد آمریکایی را روی زمین منهدم کردیم
🔹
سردار محبی: از ۱۷ تا ۳۱ تیر نیروهای مسلح ایران ۱۱ جنگنده و بالگرد آمریکایی را روی زمین و درحالی‌که در پایگاه‌های آمریکایی در منطقه مستقر بودند منهدم کردند.
🔹
همچنین ۱۷ پهپاد شناسایی و عملیاتی،…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/461906" target="_blank">📅 00:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461905">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da22e4ebd.mp4?token=meaonIS-VAp4SnN6Bp7ZqTUdeXRvE2OLCbupwR8w2pTdQqo86QW7dZRbJIrDsLloNhop5brzcs0ZWUCThOZHHZjpxmYLDwSkVHs5GtEjJ8Qj-HR4AvbTiA1vlsHUvGo3UjkYdZC8cBqbKBNzXOld4Zqk9zmu3yMstmOIeVlz-VoTeZp1nHhMidR-5qpKSdlzwimUVE6V2nvLw0MBw5ePIvMtgZN3AkGSS3R-KAsdRO0TctkVz3E2cH0w6sSB-73NCk85pC67SpSVCuHHMqU9Pb2QmcoZQKD0HO8L_aCh0a5IB8PqLH8WygJjGPHHbdsDMIXvpWe8o-UlfoWE-QLOar6VIu0H3OnOlSt--2GSjImYHRsioGcIWQRR9NoHwWmQ8kXVgzTHEGKrvKxc1zzY1ZvxniLD0wjFWKSo0OIWFD0SJHcmIbjOSxmue1k5tUgrzubMcUWH7dm5XiGeOI5xzowhM6zoke8u-Eu0iRshaaYAgS_nRqw-tWN1eZkQGDEC_61JcQB9rqobl4zngupLrF3GUbtS_QgN438VGOvfUwjOiNYb-mDo2vUb716H08luU7R2xs73hktNDWB73okrDNkeL4JbXnEWImkzI07zGPefGG48pcH8o6ccG9_slWImWeEGzVGNDsUV8_jfidPXsAAFbfQ_mNUKOOYAK1DVad4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da22e4ebd.mp4?token=meaonIS-VAp4SnN6Bp7ZqTUdeXRvE2OLCbupwR8w2pTdQqo86QW7dZRbJIrDsLloNhop5brzcs0ZWUCThOZHHZjpxmYLDwSkVHs5GtEjJ8Qj-HR4AvbTiA1vlsHUvGo3UjkYdZC8cBqbKBNzXOld4Zqk9zmu3yMstmOIeVlz-VoTeZp1nHhMidR-5qpKSdlzwimUVE6V2nvLw0MBw5ePIvMtgZN3AkGSS3R-KAsdRO0TctkVz3E2cH0w6sSB-73NCk85pC67SpSVCuHHMqU9Pb2QmcoZQKD0HO8L_aCh0a5IB8PqLH8WygJjGPHHbdsDMIXvpWe8o-UlfoWE-QLOar6VIu0H3OnOlSt--2GSjImYHRsioGcIWQRR9NoHwWmQ8kXVgzTHEGKrvKxc1zzY1ZvxniLD0wjFWKSo0OIWFD0SJHcmIbjOSxmue1k5tUgrzubMcUWH7dm5XiGeOI5xzowhM6zoke8u-Eu0iRshaaYAgS_nRqw-tWN1eZkQGDEC_61JcQB9rqobl4zngupLrF3GUbtS_QgN438VGOvfUwjOiNYb-mDo2vUb716H08luU7R2xs73hktNDWB73okrDNkeL4JbXnEWImkzI07zGPefGG48pcH8o6ccG9_slWImWeEGzVGNDsUV8_jfidPXsAAFbfQ_mNUKOOYAK1DVad4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه آفرینی مردم سرخس در شب ۱۹۷ حضور در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/461905" target="_blank">📅 00:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461904">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c57jGqmYcjXV2jVYpZN_ESJn2EMOduzo_Ts2wMazVvLEHvZsCQ_fBe0wk0wY8SbuTkvOHC2aBxHP9wb4jbaEy_7KI7KiAB83FUT1IH5oNq-qyTLsjZmlYiKhzx3mLeoH9kIA4iePlpgSht9E2azhSZcNzsvP-I4F_G2NpgW1h4DppxUT0JthbotEFYL7fS4RrMT3fWZ1DtTBI7Y_-BcFlTFOSSyxu0kYfB9fpXx9ttYE3vo25DB8q2pMuYCykCC6ZZqdv7Yj57qv2UDzpYvQwms33fcVRmW_2OgJt5DBoWP6wnqVPOhIdScGEk-UGMYNNLjJ7ut-biRw4FeamshJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایی که حتی ناگفته‌هایتان هم فاش می‌شوند
🔹
دیجیتال‌ترندز:  پژوهشگران هشدار داده‌اند که فعالیت کاربران در شبکه‌های اجتماعی می‌تواند اطلاعات حساس‌تری از آنچه تصور می‌شود آشکار کند.
🔹
پلتفرم‌ها و اشخاص ثالث می‌توانند با تحلیل رفتارهای ظاهراً معمولی کاربران، اطلاعاتی دربارهٔ دیدگاه سیاسی، گرایش مذهبی و عادت‌های خرید آنها به دست آورند. حتی اگر کاربر هیچ‌کدام از این اطلاعات را مستقیماً منتشر نکرده باشد.
🔹
هر تعامل در شبکه‌های اجتماعی می‌تواند بخشی از یک «ردپای دیجیتال» بزرگ‌تر باشد. موقعیت مکانی، فعالیت‌های آنلاین، ارتباط با دیگر کاربران و نوع محتوایی که فرد با آن تعامل دارد، در کنار یکدیگر می‌توانند تصویری گسترده از او ایجاد کنند.
🔹
این داده‌ها ممکن است توسط خود پلتفرم‌ها یا در برخی شرایط توسط اشخاص ثالث مورد جست‌وجو و تحلیل قرار گیرند.
🔹
برای نمونه، کاربر ممکن است هیچ‌گاه به‌طور مستقیم دربارهٔ گرایش سیاسی یا باور مذهبی خود صحبت نکند، اما مجموعه‌ای از رفتارهای عادی او می‌تواند سرنخ‌هایی در اختیار تحلیلگران قرار دهد.
🔹
در نهایت، پیام اصلی برای کاربران ساده است: پروفایل شبکهٔ اجتماعی شما ممکن است بسیار بیشتر از آنچه خودتان منتشر کرده‌اید دربارهٔ شما اطلاعات داشته باشد.
🔹
پسندیدن‌ها، تعاملات، موقعیت‌های مکانی و سایر رفتارهای ظاهراً بی‌اهمیت، زمانی که در کنار یکدیگر تحلیل شوند، می‌توانند تصویری دقیق‌تر از علایق و ویژگی‌های شخصی شما ایجاد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/461904" target="_blank">📅 23:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461903">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb50b917a.mp4?token=TdW6ZboygMGmfIu1arVoAUZKvmt19gzuUoUaOaSHUVsWnyaArOccCxmuXinWzwZC9JGRS0R0R2ndV7ioNLENWF9hfH_uFaCNY8G-8qFx6LU0cqxLq7RaGLN4rhly_2kjTFpewRYCpea7jRRZyibGWYTDn9gG8NTqGVwFA-zxJOKRlRZQmJe3EE35ODGjMnfkIxhfMd1BM6G5bW-7K8HQBBTRbSsom5BSHuMznOiDwjrrGf84Sxadjww351BX0LhGBfUtEmXWFViQRh47XK0UHbroWGc_AnU6IVsXW_5RM3-KhiyMZUgyH3l3g2yixRaU3V0ZtoDtNnriqjNB3gpOBaT4wgMgjcRKKU0xdG31ioUayJ5lNJhGziPnL5Vi4Lp9Q8i1LDgZ3KqcCzrLqK5Npsr1cDwE9uklvzD5TQTX6oqCx8MHbWNvN2qWo8ft5bCACp3UunMCQ0Tgn-WAkO2NwiGPXldKLnl6gw_cSLu-S_1SBwv608xhRjN0iYb00Lsgz2vABFtdRpWXpNvPtSZkFQGcqA3xM0u8X1RWE5KkFyCvbh-L_3X1m_cZc_7Tw_WNILWys5IGynpqQ03-imlU7YoObeMOubVLyOeVhJuU1ow7f7e7nKeDhwlVQDzVAiy391cRXDC8FoDw_DrIoHBJPVZKrjnxiCLh3Q6juaJsrXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb50b917a.mp4?token=TdW6ZboygMGmfIu1arVoAUZKvmt19gzuUoUaOaSHUVsWnyaArOccCxmuXinWzwZC9JGRS0R0R2ndV7ioNLENWF9hfH_uFaCNY8G-8qFx6LU0cqxLq7RaGLN4rhly_2kjTFpewRYCpea7jRRZyibGWYTDn9gG8NTqGVwFA-zxJOKRlRZQmJe3EE35ODGjMnfkIxhfMd1BM6G5bW-7K8HQBBTRbSsom5BSHuMznOiDwjrrGf84Sxadjww351BX0LhGBfUtEmXWFViQRh47XK0UHbroWGc_AnU6IVsXW_5RM3-KhiyMZUgyH3l3g2yixRaU3V0ZtoDtNnriqjNB3gpOBaT4wgMgjcRKKU0xdG31ioUayJ5lNJhGziPnL5Vi4Lp9Q8i1LDgZ3KqcCzrLqK5Npsr1cDwE9uklvzD5TQTX6oqCx8MHbWNvN2qWo8ft5bCACp3UunMCQ0Tgn-WAkO2NwiGPXldKLnl6gw_cSLu-S_1SBwv608xhRjN0iYb00Lsgz2vABFtdRpWXpNvPtSZkFQGcqA3xM0u8X1RWE5KkFyCvbh-L_3X1m_cZc_7Tw_WNILWys5IGynpqQ03-imlU7YoObeMOubVLyOeVhJuU1ow7f7e7nKeDhwlVQDzVAiy391cRXDC8FoDw_DrIoHBJPVZKrjnxiCLh3Q6juaJsrXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای فرار معتادان از کمپ مشهد چه بود؟
🔹
مدیرکل بهزیستی خراسان رضوی: در یکی از کمپ های ترک اعتیاد در اطراف مشهد، ۷۰ معتاد متجاهر پس از درگیری با نگهبانان در زمان استراحت و هواخوری، از مرکز فرار کردند.
🔹
دستورات لازم برای مدیریت شرایط صادر شد و تا شب گذشته و با همکاری پلیس و مراجع قضایی، ۶ نفر از این افراد متواری، پیدا و به کمپ بازگردانده شدند.
🔹
کمپ‌های مادهٔ ۱۶ در اختیار ستاد مبارزه با مواد مخدر می‌باشد و بهزیستی، نقش نظارتی دارد. به همین منظور و پس از بازگرداندن نفرات یاد شده و تا پیدا شدن دیگر متواریان، کمپ مذکور تخلیه و مددجویان آن به نقطه‌ای امن برده شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/461903" target="_blank">📅 23:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461902">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d93bea865.mp4?token=REAfpitQh0tgsOU1RgzCvslB83Q5s5nYb9VlbKlee7HZRMUVVSXQW1TS9V-2G5bzA-1YRBPPYG6llLhfRQQHpQvjhoa7jOCFaf9-NyrIZZ3d4tp_m2vomyDBV48Pl6MoZZz0ORwCbZLEbk_rVcR8B4JBomstVK23IxqYlTCJ1ih1LFidXMdiKwyjfLcuXbKUZTU3vNQdDf255-tijpJh7V5LKOyVlQ71W2oUIUZeI9dxNdT-_PW0xeTcZSzxJDAV4IM-0IOrTub0L2ZSUYSyeDW1rV2oCLZYLlSUMbHOUBOsXaEAgHDOOGuq9vnBtv-jginBKqnnANMELk-2kZYpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d93bea865.mp4?token=REAfpitQh0tgsOU1RgzCvslB83Q5s5nYb9VlbKlee7HZRMUVVSXQW1TS9V-2G5bzA-1YRBPPYG6llLhfRQQHpQvjhoa7jOCFaf9-NyrIZZ3d4tp_m2vomyDBV48Pl6MoZZz0ORwCbZLEbk_rVcR8B4JBomstVK23IxqYlTCJ1ih1LFidXMdiKwyjfLcuXbKUZTU3vNQdDf255-tijpJh7V5LKOyVlQ71W2oUIUZeI9dxNdT-_PW0xeTcZSzxJDAV4IM-0IOrTub0L2ZSUYSyeDW1rV2oCLZYLlSUMbHOUBOsXaEAgHDOOGuq9vnBtv-jginBKqnnANMELk-2kZYpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از کشتی ایرانی که امروز در نزدیکی جزیرۀ هنگام مورد حمله قرار گرفت  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/461902" target="_blank">📅 23:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461901">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bc2aaa2c3.mp4?token=rartuoRP5zRiPmkWu7-cX0kVytRIw_JsS5FB57wknmpBBdIXCONWrdCRNI43lWUn4PVtvpnd3fqdFZ6hPpcMhMMEthOCWyqGvFUC4t355dKkd-jsZjwKSeGVskO3VKOraKGFhsDG0mlyiUQB5p-fQlQ_Xqe7Rw1srGrOHKZzQGrNdOKm2g0MRHj9kXpvYSk4qWqARDayAnoj_WaSoFg0xMoSFrB0sqNZCAmicrdoB0Asd14ajgSUCUUSNQONk7lV5xiKrYZr9jk_rtkHcOKuDbCp10O_OOQh2RjCbEe9lXroMoeAMB_mFlDoxk8tsIU0AOOdGUKuyXqc0LC2yDn_fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bc2aaa2c3.mp4?token=rartuoRP5zRiPmkWu7-cX0kVytRIw_JsS5FB57wknmpBBdIXCONWrdCRNI43lWUn4PVtvpnd3fqdFZ6hPpcMhMMEthOCWyqGvFUC4t355dKkd-jsZjwKSeGVskO3VKOraKGFhsDG0mlyiUQB5p-fQlQ_Xqe7Rw1srGrOHKZzQGrNdOKm2g0MRHj9kXpvYSk4qWqARDayAnoj_WaSoFg0xMoSFrB0sqNZCAmicrdoB0Asd14ajgSUCUUSNQONk7lV5xiKrYZr9jk_rtkHcOKuDbCp10O_OOQh2RjCbEe9lXroMoeAMB_mFlDoxk8tsIU0AOOdGUKuyXqc0LC2yDn_fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع شبانهٔ مردم ولایتمدار شهرستان زرند به ایستگاه ۱۹۷ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/461901" target="_blank">📅 23:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461899">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae0abfabb.mp4?token=P8MkgI1_PMtEnOZBEFN6MKJ-rzJr7fOTqzouV1yy4txCIMRO1ArXER-Axazf_EaXqOP_36IfX_vTTzjHzjXkGTWVKZZ-jPrqdAgoBRB5b9pNOMgkWlWv1dvMi7q3AGTKGTJsLSBabH-AU8t7be8BGayk8Fjn9eibd9bfu8s141DR-x3pAKoJKNi7gbJkeNqSQTEQWnrDkyd9pFOEg3FYESMxrHBxn-XeAQcW9GOI17cplfTHuklvdPoq97a5zt5Y86mLSg-sZPauMsFwoFkB51YfJz_Xy6emPgKyU2RUs979y3O0e5jWkXidfcQ4gb4PvsMTtY1gjmxy3oWR9rtLeG4oobOQoLOaMSuZzF3OKCjlW13If0XDD6N71rkIv_c_ouP6Q1FH1eDR-oxWKmyP5Otsx84A--pQEyIHPe0ooUWZsFteMIbtTA86FtGqzFA5FcCwALGiqMR9Qfj84Pchn8jYmOhL_wGo1sfAw6uYwCn5iNGulS3Cwn-VK_hox661oWzv_Al0tNUMlxwtBozZR_MUii0GxyERJLA1NlEXcpuh5NWvLRxjVkOyllMhKMfWoRzje6xAGU8fMny58uF7qKk2PnMJUTJapqv7Z7T_MQKf4iAvxokisp-2UlgL5SenKVy6xIaz9qxfi5vSgCCft-WWdnXI2CDBQFv9W7N8kto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae0abfabb.mp4?token=P8MkgI1_PMtEnOZBEFN6MKJ-rzJr7fOTqzouV1yy4txCIMRO1ArXER-Axazf_EaXqOP_36IfX_vTTzjHzjXkGTWVKZZ-jPrqdAgoBRB5b9pNOMgkWlWv1dvMi7q3AGTKGTJsLSBabH-AU8t7be8BGayk8Fjn9eibd9bfu8s141DR-x3pAKoJKNi7gbJkeNqSQTEQWnrDkyd9pFOEg3FYESMxrHBxn-XeAQcW9GOI17cplfTHuklvdPoq97a5zt5Y86mLSg-sZPauMsFwoFkB51YfJz_Xy6emPgKyU2RUs979y3O0e5jWkXidfcQ4gb4PvsMTtY1gjmxy3oWR9rtLeG4oobOQoLOaMSuZzF3OKCjlW13If0XDD6N71rkIv_c_ouP6Q1FH1eDR-oxWKmyP5Otsx84A--pQEyIHPe0ooUWZsFteMIbtTA86FtGqzFA5FcCwALGiqMR9Qfj84Pchn8jYmOhL_wGo1sfAw6uYwCn5iNGulS3Cwn-VK_hox661oWzv_Al0tNUMlxwtBozZR_MUii0GxyERJLA1NlEXcpuh5NWvLRxjVkOyllMhKMfWoRzje6xAGU8fMny58uF7qKk2PnMJUTJapqv7Z7T_MQKf4iAvxokisp-2UlgL5SenKVy6xIaz9qxfi5vSgCCft-WWdnXI2CDBQFv9W7N8kto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مینابی‌ها هر شب پای کار تجمعات خیابانی هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/461899" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
نشست ایران با کشورهای عربی به تعویق افتاد
🔹
وزیر خارجهٔ عمان: نشست منطقه‌ای که قرار بود فردا در «صلاله» برگزار شود، به تعویق افتاد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/461898" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461897">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5K9NAprLQL3kYpZTiwcPMlhkja7e4xjOGF7UfVADFN7tD8PZgBqi40EpW8-Cs-kk73Br15nojBPyyjIRR77JJJ-CcAsklEi-HrzxahSAQdYEEPCLwHgye2fuNcHaPgywJA34NjqBxOGL49Wk8y8H0WVxUOwuMN9pMJnXGuAGZnQpbV_hN2JdwQXtqgLwTXyU791b87BJ07v8FLqGhRxJI4uufiR9qOkDRvXAsQ-UitM3XpuHQyf6-Fu5uI7ptkpPFqNe-e9jmQTwu2kl1z_8Q6hAtaQkU1xMeJjO7dGqHYrzguDSyxQ2z1NSlLaFThgMxoMlOO01CEX6_PqKUPugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشست ایران با کشورهای عربی به تعویق افتاد
🔹
وزیر خارجهٔ عمان: نشست منطقه‌ای که قرار بود فردا در «صلاله» برگزار شود، به تعویق افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/461897" target="_blank">📅 23:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c1883a9c3.mp4?token=ELKNvlEBuJY5JIBxGfUgPLFHIfjCfm5vJSPNSY34enVvtYYi9YGggDDp9NksEIFcBuRISiZmjs-gXwl6wo4V3pq43n0xqIXg8jXJchHF9nBXGFxW9Ikt1qwkFWYQvu_tby-la7CZmk7h0kmzViegqiLWFP9KYWVfe-z4MngbIv_DnF_FazXRkWEY-YdZ7WqjOq9_E2FUk7TAjtfwTRxOG0I3EDSrMspGBr0hZhH9uC1tDouzfOytulWcIYTfvcdq-ON1WJXvZvdA-0aXr1q6jLL29cJ4RDzsk_VOzmMszqacFFkZzEcNLhbQW2lnheIBvWttC63AX5E7mrXKIbW2AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c1883a9c3.mp4?token=ELKNvlEBuJY5JIBxGfUgPLFHIfjCfm5vJSPNSY34enVvtYYi9YGggDDp9NksEIFcBuRISiZmjs-gXwl6wo4V3pq43n0xqIXg8jXJchHF9nBXGFxW9Ikt1qwkFWYQvu_tby-la7CZmk7h0kmzViegqiLWFP9KYWVfe-z4MngbIv_DnF_FazXRkWEY-YdZ7WqjOq9_E2FUk7TAjtfwTRxOG0I3EDSrMspGBr0hZhH9uC1tDouzfOytulWcIYTfvcdq-ON1WJXvZvdA-0aXr1q6jLL29cJ4RDzsk_VOzmMszqacFFkZzEcNLhbQW2lnheIBvWttC63AX5E7mrXKIbW2AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت صادق محصولی از تلاش سپاه برای ساخت موشک ضدناوشکن  @Farspolitics - link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/461896" target="_blank">📅 22:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461895">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سرکردۀ مزدوران سعودی در یمن به ریاض فرار کرد
🔹
یک منبع دولت عدن (همسو با عربستان سعودی) خبر داد که طارق صالح، برادرزادۀ رئیس‌جمهور معدوم یمن به ریاض فرار کرده است.
🔹
طارق صالح، فرماندۀ شبه‌نظامیان موسوم به «مقاومت ملی» است که سال‌ها سواحل غربی در جنوب استان…</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/461895" target="_blank">📅 22:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461894">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc8d5a7c1.mp4?token=BWIaiyg3yJnY6D_E-TueeDho1dc2DYvdxz-eNNaVKy-gBOT84-xfU8wWXQJ5fhq6Nibr-0Db7kASRN8aV5cpNzQ0iN0eZ57-E_kBt9Fujb80xHNyxvtIbE-djZvBGyxFJPee5APny8n_AK7HjKDYNAtSW3i8cqZcKx8Uvg4PkjKL5C06HzYETk2yLCraHWD4hkl8_rIAvHMkRndQO96368UfmaRjERW0WAK7L8JRn96Gc7JvHRtmR-EzPogIJy5WtsY3xo3ag4NJ69g3Ds3_rvzfp7li60Xqu8vUIroTxSf6BZBEjydIDbRbCD8q9f4lvpebRlsijWGmjFONrdXMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc8d5a7c1.mp4?token=BWIaiyg3yJnY6D_E-TueeDho1dc2DYvdxz-eNNaVKy-gBOT84-xfU8wWXQJ5fhq6Nibr-0Db7kASRN8aV5cpNzQ0iN0eZ57-E_kBt9Fujb80xHNyxvtIbE-djZvBGyxFJPee5APny8n_AK7HjKDYNAtSW3i8cqZcKx8Uvg4PkjKL5C06HzYETk2yLCraHWD4hkl8_rIAvHMkRndQO96368UfmaRjERW0WAK7L8JRn96Gc7JvHRtmR-EzPogIJy5WtsY3xo3ag4NJ69g3Ds3_rvzfp7li60Xqu8vUIroTxSf6BZBEjydIDbRbCD8q9f4lvpebRlsijWGmjFONrdXMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: دشمن برای چهارشنبه آخر سال ۱۴۰۴  قصد داشت مدل دی‌ماه را پیاده کند اما مردم نگذاشتند
🔹
جانفدایان ایران پیش‌رویدادی هستند یعنی قبل از این‌که وطن‌فروشی به میدان بیاید در میدان هستند.
🔹
انگشت ما مثل انگشت عزیزانمان در سپاه و ارتش برای حفظ امنیت…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/461894" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461893">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff0f87d1a.mp4?token=YvAsZ_wB9xgc1GuHe-v2TLr1N5OPBxENddiXg-Wy_G4wbVlZPJfAAVE71YHWVvK94whHm2rFr9Ev0XiW8Fmvi97tO4S2swaKG6c7beAslY-yujk5tp21PkLZOsoKZy3gbtGQGasHesdAPpmsJC48xTCOyCsHqBpsmKMe7IbeQez0PScL1Zlw6QMGF48ZosaJrKb_moqv7EMDwlAow6x3uOMFrAds4VeR-awUIo_6AVodpx3f0GtjQrAHGki7I1rHRIVeIL7JJndd0cJX6OcSAwJiFVuyKeXF9NcZMgGFtdUcWHexGxDnbcdy9PomcH05zYOGxMr6M7Mwiv1Re4_EWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff0f87d1a.mp4?token=YvAsZ_wB9xgc1GuHe-v2TLr1N5OPBxENddiXg-Wy_G4wbVlZPJfAAVE71YHWVvK94whHm2rFr9Ev0XiW8Fmvi97tO4S2swaKG6c7beAslY-yujk5tp21PkLZOsoKZy3gbtGQGasHesdAPpmsJC48xTCOyCsHqBpsmKMe7IbeQez0PScL1Zlw6QMGF48ZosaJrKb_moqv7EMDwlAow6x3uOMFrAds4VeR-awUIo_6AVodpx3f0GtjQrAHGki7I1rHRIVeIL7JJndd0cJX6OcSAwJiFVuyKeXF9NcZMgGFtdUcWHexGxDnbcdy9PomcH05zYOGxMr6M7Mwiv1Re4_EWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: با وطن‌فروشان مثل دشمنان برخورد خواهیم کرد
🔹
اگر وطن‌فروشی قصد ایجاد ناامنی داشت با او برخوردی می‌کنیم که با دشمن باید کرد.
🔹
در حوزۀ مرزبانی و انتظامی از قبل از جنگ آماده‌تریم و در امنیت مردم شوخی نداریم. @Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/461893" target="_blank">📅 22:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461892">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWu3UXlNDrs7Jnlur3MQJyDumRwPNoqdh-F_q2sxb2vyy89NHM-__h-mk5MkkqToTnDa4ffTGWU7LX6fCajZyM4pORew0fV7kc7fbYXmrSs-uS3nSoojnH_K1ZLFxdLz4Kn-urCE_6Iu_oUcfa8n86XMXuJoIzvvmRDBwRGCMMf2XC711mJ6QaJqOqOttq7A3kPnWt3h1OIYjw-pqnv0TKpwIwt85sBS4ua8SCR5kduDbKczZJr8zrKg5wkunha9d6QR5h9CHaQJc11_SXtPIsbsrNrajfdBcJFJrjTIET6c1crEiPYMRx2Mmzr-fbjBxns-gGFkf1Naxx1mY2pNxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصابت موشک به یک نفتکش در تنگۀ هرمز
🔹
سازمان امنیت دریانوردی انگلیس خبر داد که یک نفتکش با پرچم پاناما به هنگام عبور از تنگۀ هرمز مورد اصابت یک موشک قرار گرفته و از کار افتاده است. @Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/461892" target="_blank">📅 22:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461891">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ded472086.mp4?token=i_Q7GxpFmR-cPVB1Hj8wttBUdcE65zpziW1r3eyqBCDtdl6NfxxkTKjgP4F23MoktFaxv84xcQiN6OgSjaR_65v1o9rGAGXc-I-A8vWLi7eBz7hIfCwnKeVxGAQiKKoOFRsC9zgt7CtSUmOMbfudWBP7ngYo5ctZwzPF5rMFisgS0SgU8-g-xuhS4zJGK5PxJ669LQXk0Be-o2INovDSMAXrkpoKziJP3RCWG6q6qftqqR9MwnBAMzEjZSSH5i2OLLKtReNdHpiJ3ZBtEqAlPEm4Lwj7e9iFSa05sKZC-hhOJbRhROvOba_aQj7OjprJuGDOzrMfqCkTVk4Y4As8Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ded472086.mp4?token=i_Q7GxpFmR-cPVB1Hj8wttBUdcE65zpziW1r3eyqBCDtdl6NfxxkTKjgP4F23MoktFaxv84xcQiN6OgSjaR_65v1o9rGAGXc-I-A8vWLi7eBz7hIfCwnKeVxGAQiKKoOFRsC9zgt7CtSUmOMbfudWBP7ngYo5ctZwzPF5rMFisgS0SgU8-g-xuhS4zJGK5PxJ669LQXk0Be-o2INovDSMAXrkpoKziJP3RCWG6q6qftqqR9MwnBAMzEjZSSH5i2OLLKtReNdHpiJ3ZBtEqAlPEm4Lwj7e9iFSa05sKZC-hhOJbRhROvOba_aQj7OjprJuGDOzrMfqCkTVk4Y4As8Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: در سال جدید ۶۰۱ میلیارد تومان که با کلاهبرداری  از حساب مردم برداشته شده بود را بازگرداندیم  @Farsna</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/461891" target="_blank">📅 22:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461890">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac367f1a5a.mp4?token=kuI_IORlXs3jHPAmTX1RW_HiE4EjV1C-I76dHd8aPCne1giOPnouc2EI3katL_fBfAJ30Yaoz3W78TQOg_42G7SKEU2ODybImpugCFaGHK726XRMrl0MvXymfqYEB625-RDRWvghx1YIMaN6rXFIJKRDVGuS0PE0TQNkprsU6Lh7W0r8tUbRz4ApPCeV9nMlmR4AVGSnPvr3tdQy-mB_2KIsfDQF7qlk2-rEr_qFLjy3cBtLiXJ6RdnuwOHAM4yFmpA_HQV83YRg-SLU6fOkI-otl92THOm7TrzsB_7RdYQgpWlTIrXqNSW2K7OVXmjDAL4ypcEbyibP3FrDLquowA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac367f1a5a.mp4?token=kuI_IORlXs3jHPAmTX1RW_HiE4EjV1C-I76dHd8aPCne1giOPnouc2EI3katL_fBfAJ30Yaoz3W78TQOg_42G7SKEU2ODybImpugCFaGHK726XRMrl0MvXymfqYEB625-RDRWvghx1YIMaN6rXFIJKRDVGuS0PE0TQNkprsU6Lh7W0r8tUbRz4ApPCeV9nMlmR4AVGSnPvr3tdQy-mB_2KIsfDQF7qlk2-rEr_qFLjy3cBtLiXJ6RdnuwOHAM4yFmpA_HQV83YRg-SLU6fOkI-otl92THOm7TrzsB_7RdYQgpWlTIrXqNSW2K7OVXmjDAL4ypcEbyibP3FrDLquowA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: ۱۰۰ درصد قتل‌ها در سال جدید کشف شده
🔹
پروندۀ قتل مجهولی پس‌از جنگ نداریم و پرونده‌هایی که از سال‌های قبل مانده هم درحال بررسی است.
🔹
صحنۀ جرم را با کمک فناوری‌های دیجیتال بررسی می‌کنیم تا به واقعیت برسیم. @Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/461890" target="_blank">📅 22:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461889">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLsIZG-OIAOc_1ygi7ivMPIpGIn1qepvbbQuHQ2jJ8mrAZrp9kzBT08iZzteMuJXTiAzeP76vc1IjwLXwbcUplxGIRPbSuQVFgpc2tp34BzndnNpyB5vVfhAZaqFG4CWagdnFxsaYJm51b7_bpAKg8VqcjHCgoaNlVT00mm9Yk-TqizQo-tjwbbKwTnIqH9OAo5uSXpyhIP38viHsjTKvsm8ZEPUW7caSQvvr6k9xbx7AnkEFZMfCFoEluFFBd8ZREsRaXP2DfhUU9C_fxPRXiTZ7SXZYLB9wjYtNhlZOiBly46zEGe3F_UFqQSW_OTHooCb0msSyqrIv0zyZf84ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باند حرفه‌ای سارقان خودرو در آذربایجان‌ غربی منهدم شد
🔹
فرماندهٔ انتظامی آذربایجان‌ غربی: مأموران پلیس اعضای یک باند حرفه‌ای سرقت خودرو را شناسایی و ۳ سارق را دستگیر کردند و ۲ خودروی سرقتی از این باند کشف و توقیف شد.
🔹
اعضای این باند ۱۰ خودروی سرقتی دیگر را نیز با شیوه‌های متقلبانه در مشهد، اصفهان و تهران فروخته بودند که با اقدامات پلیسی، ۸ مالخر و عامل خریدوفروش خودروهای سرقتی شناسایی و دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/461889" target="_blank">📅 22:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461888">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e754c1c6.mp4?token=Bwj2KOeVr9PxcDlFYp3Afod3M5AB7JeGTphJ_IR9L2avX3UTeAH7U7GPwZsYMOyZcVfyWOLNUJTKNcrp1s_E3lMx2q5LBoe5blDSWFuP_7BPOCynDcLTpKPc6dfYFK_PLDQo3Jl_dnyx-anhOvYKkY53Wk0dN1RqWwzINT9EA94LYvSg23P_xsc1yihqCkhNmDWItkXjF4vMJ2mReVctEEv2_DF-BYwAEqUh6dZFyBQEKKKEdUbqXuv1sHkVIkwCw1PCZbwHv54Mqs-1HwXIoVVYEmwvbYxpECIi33qfI4voLweisEy32_tqQZFxutnxF41n4R3Hdr1_WmRayCIQng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e754c1c6.mp4?token=Bwj2KOeVr9PxcDlFYp3Afod3M5AB7JeGTphJ_IR9L2avX3UTeAH7U7GPwZsYMOyZcVfyWOLNUJTKNcrp1s_E3lMx2q5LBoe5blDSWFuP_7BPOCynDcLTpKPc6dfYFK_PLDQo3Jl_dnyx-anhOvYKkY53Wk0dN1RqWwzINT9EA94LYvSg23P_xsc1yihqCkhNmDWItkXjF4vMJ2mReVctEEv2_DF-BYwAEqUh6dZFyBQEKKKEdUbqXuv1sHkVIkwCw1PCZbwHv54Mqs-1HwXIoVVYEmwvbYxpECIi33qfI4voLweisEy32_tqQZFxutnxF41n4R3Hdr1_WmRayCIQng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: ۹۹ درصد خودروهای سرقت شده را کشف کرده‌ایم
🔹
گشت‌های آگاهی زنده شده و به کمک این گشت‌ها بیش از ۱۱۰۰ خودروی سرقت شده را کشف کردیم.
🔹
در سال ۹۸ حدود ۴۰۰۰ سرقت خودرو داشتیم اما در ۶ ماه اول ۱۴۰۵  تعداد سرقت خودروها زیر ۱۰۰ مورد بوده. @Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/461888" target="_blank">📅 22:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461887">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82b0b5bfd.mp4?token=Fgnk6hG4W1RcnjMw4IBRoEFBF0w6oUcQiBkuEZohmem1bELgfALtGZ2heI0DLSfkKm_2tcMyP2qWJeA3vgpOCC7x5Zj3MCe1YFnmM4WS24eJdxctsQKkEpn2z2gEyPVMcIgKBo5KZZFTq9JCX0QXY_NjylpN83TAPJAj3nRQ5c-gMWq1oJPsXUvpGD85XqSWSTkc67t2gUybwvuZp8DXbQqEGWhI8iYcx6GIKu84kdizgY98F5-BtFq1vIdF_aRRhl6BkWZycdczzeG0_JxLS_btjTm-Ui1N0pM-dEz8ag2NVHUiVbM4dviXW1syzNpegSpBE2s5SJ7oHP0rRtMgQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82b0b5bfd.mp4?token=Fgnk6hG4W1RcnjMw4IBRoEFBF0w6oUcQiBkuEZohmem1bELgfALtGZ2heI0DLSfkKm_2tcMyP2qWJeA3vgpOCC7x5Zj3MCe1YFnmM4WS24eJdxctsQKkEpn2z2gEyPVMcIgKBo5KZZFTq9JCX0QXY_NjylpN83TAPJAj3nRQ5c-gMWq1oJPsXUvpGD85XqSWSTkc67t2gUybwvuZp8DXbQqEGWhI8iYcx6GIKu84kdizgY98F5-BtFq1vIdF_aRRhl6BkWZycdczzeG0_JxLS_btjTm-Ui1N0pM-dEz8ag2NVHUiVbM4dviXW1syzNpegSpBE2s5SJ7oHP0rRtMgQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: بیش از ۵۰۰ سارق را با ضرب گلوله متوقف کردیم
🔹
۵۶ نفر از آنان که در مقابل ماموران اسلحه کشیده یا مقاومت کرده بودند هم کشته شدند. @Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/461887" target="_blank">📅 22:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461886">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75d753ba1.mp4?token=rF98LOh8lbZRXWq5jwrGVa0yr436HwwXG2MB2Ga0vS5W8oCAi0wS0H4IMqs3SsiZ5sg3hXxcljjZtAfI4w6owWZvgeY3bTZfp-bIGJ7qknjFBebY0meJmonBHx0yxZ7vu32iKw-5u4-DrFKK2pExs4PkLRVJjUo2leMDqBKYFxuHsH0nsG-rybTiEUxQOzz58nlr8mKkJULHCSg5DCqQ5sRkqJBZDnN-IIwvk65kJniEtKIsFC8O6H0_XD_j7ZxAa2fz3EdkiTT6XcewwF_MiN0dX1CENdH6Subh7gxq7rdOvrGUJDzab5HEsgt3wffcNGCBwV1g9Nl4nsDb7PJIFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75d753ba1.mp4?token=rF98LOh8lbZRXWq5jwrGVa0yr436HwwXG2MB2Ga0vS5W8oCAi0wS0H4IMqs3SsiZ5sg3hXxcljjZtAfI4w6owWZvgeY3bTZfp-bIGJ7qknjFBebY0meJmonBHx0yxZ7vu32iKw-5u4-DrFKK2pExs4PkLRVJjUo2leMDqBKYFxuHsH0nsG-rybTiEUxQOzz58nlr8mKkJULHCSg5DCqQ5sRkqJBZDnN-IIwvk65kJniEtKIsFC8O6H0_XD_j7ZxAa2fz3EdkiTT6XcewwF_MiN0dX1CENdH6Subh7gxq7rdOvrGUJDzab5HEsgt3wffcNGCBwV1g9Nl4nsDb7PJIFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: با کمک مردم سرقت برای سارقین سخت‌تر می‌شود
🔹
برخی سرقت‌هایی که صورت می‌گیرد روی اشتباهات رایج مثل نگه‌داری مال در مکان‌های غیرایمن و استفاده از در و پنجره‌های ناامن است. @Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/461886" target="_blank">📅 22:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461885">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3901d6894.mp4?token=Z9gHdVPw1TNyKJbK03zW60D843m5-AvOyrPklMDUU9D91JZHDNJeYgaN2RKaMmvx8a3MLda5TQDfsbZRJM2rt72NkY9z6fz0E-dZoqfyMG-jv_WDiek_YtBP0wbHHtEoHehg-QgpcxZYhtUYB3qKvr92FJdtobo43YiKb6lV7z2tnR2YfzEdeCPEIxrmlN6dJvrHaRKqyOQ6kGk1-878J5oSYZGR8MmGAeE9wCD_kV0JRQ7yqBmGABfUt4TRl88EisBux3Yy-P-Qcjc2Na_YFzeMM0go5lplfcPsqw5S4heqUxPT-feOcflCEaNZ-t2qnHAvWtvjV2x7LCQiG1TINA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3901d6894.mp4?token=Z9gHdVPw1TNyKJbK03zW60D843m5-AvOyrPklMDUU9D91JZHDNJeYgaN2RKaMmvx8a3MLda5TQDfsbZRJM2rt72NkY9z6fz0E-dZoqfyMG-jv_WDiek_YtBP0wbHHtEoHehg-QgpcxZYhtUYB3qKvr92FJdtobo43YiKb6lV7z2tnR2YfzEdeCPEIxrmlN6dJvrHaRKqyOQ6kGk1-878J5oSYZGR8MmGAeE9wCD_kV0JRQ7yqBmGABfUt4TRl88EisBux3Yy-P-Qcjc2Na_YFzeMM0go5lplfcPsqw5S4heqUxPT-feOcflCEaNZ-t2qnHAvWtvjV2x7LCQiG1TINA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: با کمک مردم سرقت برای سارقین سخت‌تر می‌شود
🔹
برخی سرقت‌هایی که صورت می‌گیرد روی اشتباهات رایج مثل نگه‌داری مال در مکان‌های غیرایمن و استفاده از در و پنجره‌های ناامن است.
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/461885" target="_blank">📅 22:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgbWpuFva53-2AaYMqsEz3J509hBOm2mz37VyJjqU0PgPtxzAWLJXfJ7KbV7jSM4fKszUJtadSgKZhQ8ffEI_WAEN_OqY3hy8YzNeSzknamdjfn4LdKZe60NyyKjsd064NFlb1oFGW35EmLmGRiOH6DrUu-_e8vQgqtMIiOtCt1gUjTS2-HCvQTjVgswpx6aMzD7Bcm3iAAOqN2JAy2_AfSEmWfPsKlSMR2Dc9oT7bX1UioWcskagNWTB51PT1SiAow1z88eQqLLnTHxBnXQpkb4g0NaovIc_1sxP3Z7XKDTmdpJeXV3ycKqcL-qx_lM2ua9cOG59DAfYw4RV6ajFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۱۷ تن طلای عربستان در آتش پهپادهای ناشناس سوخت
🔹
رویترز: در صورت از سرگرفته نشدن فعالیت خط لولهٔ انتقال نفت از شرق به غرب عربستان در روزهای آینده، ذخایر صادراتی عربستان در بندر ینبع تنها برای ۵ تا ۷ روز کافی خواهد بود و این وضعیت می‌تواند به از دست رفتن حدود…</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/461883" target="_blank">📅 22:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
بنده کشاورز هستم و یکی از هزاران گندم‌کاری که صدایشان به جایی نمی‌رسد.
هنوز بخشی از مطالبات گندم‌کاران پرداخت نشده
و شرایط معیشتی ما واقعاً سخت شده است؛ باور کنید گاهی پول خرید یک مرغ هم نداریم. اگر مشکل ایران‌خودرو و صنایع یا پتروشیمی باشد، صدای آن‌ها سریع‌تر به گوش مسئولان می‌رسد. خواهش می‌کنیم این بار صدای کشاورزان را هم به گوش مسئولان برسانید.
🔹
دو سال از برگزاری
آزمون استخدامی کیفیت‌بخشی آموزش‌وپرورش
در سال ۱۴۰۳ و اعتراضات مربوط به آن گذشته است. با وجود پیگیری‌های فراوان و اعلام مسئولان درباره بررسی اعتراضات، هنوز
تکلیف حدود ۲ هزار نفر
ی که در این فرآیند حقشان تضییع شده،
مشخص نشده
است.
🔹
در طرح
مسکن ملی
هرچقدر پروژه‌ها با تأخیر بیشتری پیش بروند، هزینه نهایی برای متقاضیان بالاتر می‌رود. ما سال ۱۴۰۰ ثبت‌نام کرده‌ایم اما هنوز مشخص نیست چه زمانی واحدها تحویل داده می‌شوند و هر سال هم به‌دلیل افزایش هزینه‌ها
مبلغ بیشتری از ما مطالبه می‌شود
. عجیب است که تأخیر در انجام پروژه از طرف مسئولان و پیمانکاران است اما هزینه و ضرر آن را مردم باید پرداخت کنند! چرا مردم باید تاوان تأخیر و ضعف در انجام تعهدات را بدهند؟
🔹
من از شیراز برای اعزام به
حج تمتع امسال
، از سوی سازمان حج و زیارت به یک پزشک در دارالشفای شاهچراغ معرفی شدم. پزشک عمومی بود، اما در زمان پذیرش اعلام کردند هیچ‌یک از بیمه‌ها را قبول نمی‌کنند و باید هزینه ویزیت به‌صورت آزاد پرداخت شود. وقتی اعتراض کردیم گفتند
سازمان حج و زیارت
تصمیم گرفته همه
زائران به‌صورت آزاد ویزیت شوند
. برای ویزیتی که تعرفه آن کمتر از ۵۰ هزار تومان است، ۳۸۰ هزار تومان پرداخت کردیم!
🔹
امنیت شغلی دهیاران
را پیگیری نمایید.
🔹
لطفا مسئولان در مورد
بازنشستگان کشوری
چاره‌ای کنند با این حقوق پایین و قیمت‌های سربه فلک کشیده چکار کنیم؟ پول درمان پرداخت کنیم یا پول خوراک و مسکن؟
🔹
من یک
فرهنگی بازنشسته
سال ۱۴۰۲ هستم.
رتبه‌بندی
سال ۱۴۰۰ تصویب شد ولی هزینه ۶ ماه دوم سال را واریز نکردند و الان شهریور ۱۴۰۵ مبلغ ۲۵ میلیون برای آن شش ماه واریز کردند به نظر شما ۲۵ میلیون را اگر آن سال پرداخت می‌کردند چقدر مشکلات یک معلم حل می‌شد ولی الان این پول چقدر تاثیرگذار است ؟ آیا نباید
تورم پنج ساله
را حساب کنند؟
🔹
متأسفانه
یکی از بانک‌های کشور
در اقدامی
نیروهای حفاظت فیزیکی خود را اخراج کرده
و در آخرین مرحله، بیش از ۲۰ نفر از نیروهای استان سیستان‎وبلوچستان نیز از ابتدای مردادماه بیکار شده‌اند و تاکنون هیچ خبری از وضعیت و تعیین تکلیف آن‌ها نیست. خواهشمندیم با توجه به شرایط سخت اقتصادی و وضعیت موجود این موضوع را پیگیری کنید.
🔹
ما جمعی از جوانان و پذیرفته‌شدگان فرآیند
استخدامی وزارت تعاون
، کار و رفاه اجتماعی هستیم که با وجود گذشت
بیش از یک سال
از آغاز این فرآیند، همچنان
در انتظار تعیین تکلیف
نهایی و شروع به کار خود هستیم. سؤال ما ساده اما جدی است: یک جوان تا چه زمانی باید برای آینده شغلی خود در بلاتکلیفی بماند؟ طولانی شدن این فرآیند فقط یک تأخیر اداری نیست؛ بلاتکلیفی شغلی، فشار روانی و آسیب جدی به برنامه زندگی جوانان و خانواده‌های آنان را به دنبال دارد.
🔹
در منطقه
خاک سفید تهرانپارس
وانت‌های میوه‌فروش تقریباً تمام خیابان شهید زهدی و چهارراه‌های اطراف را اشغال کرده‌اند و با ایجاد
سد معبر
، رفت‌وآمد خودروها را با مشکل مواجه کرده‌اند. در پایان شب نیز تمام ضایعات و زباله‌های میوه‌فروشی را در خیابان رها می‌کنند و می‌روند و این موضوع باعث آلودگی و نازیبایی محله شده است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/461882" target="_blank">📅 22:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQOCPghppQwhWzBxXq1Y6At71l_Xoza2gaOvpQp8FluuLA3QeqNa_9g4txjgVPQPvtn85ekjHwwFRrpcJ7sw3UVvJpL9DoUohaL-l5YoaI3f7LDRlyZ_n_UQbtd6g6xE6DwMop6wm4dmUBsjDK1rUtkUvEhXM0oN7wTLofKNn4gyqnOLRTGOhmKKAZU0_AF75Fclzci_ZNiO24jzyxYY6tAVmBHFmyY56FIwNKj7raz-tMA-Hb1maiivX_g33a8aBTIpRYiAp83DG2JjtggFBH37nSiTbsoQqF2ilK8IC1UERkACp3pJHihn9YGmlpIVZRcAFRtz04KZdvaEDJc9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
🔸
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند. @Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/461881" target="_blank">📅 22:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7305e36237.mp4?token=qLRNkA5eLsu-BXAavCCv-ebiPSDm1NfZBXFx-BfBB7rF0JoAaMDSm5awPIDABzjCrXWE-_hAvSvtseLSmwCih5gTgAPmAKkB8jxzRPJ6fdpyx_bbAyBsHnZOkQhL-IpRS3wg0KNLF7BlPN75nQt2vEnOPcYmyJ5goUC5mq91vQbrU-ICoJJM_YjOd1_-AYmrJClgK7LfmDCmHgvN3N_YM3Pw1-9muXKcVoHE-767TtXTP7q_O3ebNF6AkbjqBn7NRbEyWFQpC5Iwxv1myB0ay5XfKvIQ5nVb3UWGg3ycWxEVJZzyb7T3wRN45RO3TfQRhFeKGcqMBzR7ASgM58fS3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7305e36237.mp4?token=qLRNkA5eLsu-BXAavCCv-ebiPSDm1NfZBXFx-BfBB7rF0JoAaMDSm5awPIDABzjCrXWE-_hAvSvtseLSmwCih5gTgAPmAKkB8jxzRPJ6fdpyx_bbAyBsHnZOkQhL-IpRS3wg0KNLF7BlPN75nQt2vEnOPcYmyJ5goUC5mq91vQbrU-ICoJJM_YjOd1_-AYmrJClgK7LfmDCmHgvN3N_YM3Pw1-9muXKcVoHE-767TtXTP7q_O3ebNF6AkbjqBn7NRbEyWFQpC5Iwxv1myB0ay5XfKvIQ5nVb3UWGg3ycWxEVJZzyb7T3wRN45RO3TfQRhFeKGcqMBzR7ASgM58fS3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاپیتان استقلال: برای کسب ۳ امتیاز مقابل السد به میدان می‌رویم  @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/461880" target="_blank">📅 21:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f5f9fd56a.mp4?token=aYPAlRXPRnBs3lObCOhUy-r7n6YtCZnymr4xheElE6aPa9Z2hKYKwsI87WHbbJgkiKKMrLS1ET81L1cKPBnvOBqv0YxBguPuc_EGi1cjA--miQNQo1yvHrdlQ8MPkBnZp7g21yUTp_VjYNhrICA7kEWLZc9d0ouWokj0XVQ5gzfsi-AX-d2bKJ9kz_MrHcWvwKqitex0lWDt04HztyYw4REVstYIKq0N72keVBJXI7io8NA6MW3CVoaVeQyZc3TefS36l4aE0m6d0GQQIT_-ZmtFfQ1A_N6t0eNfGM0ujLJh18qazUoms6wXM9IGHQ6XYqZyce9rH0ZcXo-yQzDKfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f5f9fd56a.mp4?token=aYPAlRXPRnBs3lObCOhUy-r7n6YtCZnymr4xheElE6aPa9Z2hKYKwsI87WHbbJgkiKKMrLS1ET81L1cKPBnvOBqv0YxBguPuc_EGi1cjA--miQNQo1yvHrdlQ8MPkBnZp7g21yUTp_VjYNhrICA7kEWLZc9d0ouWokj0XVQ5gzfsi-AX-d2bKJ9kz_MrHcWvwKqitex0lWDt04HztyYw4REVstYIKq0N72keVBJXI7io8NA6MW3CVoaVeQyZc3TefS36l4aE0m6d0GQQIT_-ZmtFfQ1A_N6t0eNfGM0ujLJh18qazUoms6wXM9IGHQ6XYqZyce9rH0ZcXo-yQzDKfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر سقاب: ادعای بلاگر اقتصادی دربارهٔ شهید رئیسی کذب است
🔹
مدیر حوزهٔ ریاست در ستاد تحول دولت شهید رئیسی، در واکنش به اظهارات یک بلاگر اقتصادی گفت: او را نمی‌شناسم و اسمش را هم نشنیده بودم و تمامی اظهارات وی دربارهٔ دعوت به ستاد راهبری تحول دولت و یا تهیه…</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/461879" target="_blank">📅 21:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62060f15d4.mp4?token=f55YVcBGc439uXyPHnQDUFu43cIgJGFt56SC5GhvRLYobKyq-Q9SZVt3b6WJtO2arTU1fXYZfSlN00e-8d1GDdkI0AHpzxedGTfStEisT9fWU_N7a_QcyueFo2IMGGHdMgHfnDLWLi89S_3tNaFf9oKd8uaTrE_PDytTnuAZyq-b_-KxKPnTVSEtFGI2tXrHd9V0Ivjg3k8alE2fQVfzcw6rv9rwj3HtJ7715TNlKRXWpTYEAb_bojyvdv2B6dwgugmINnHa9ESPrPgD6PmprJKi5xFErAbxIhOVNFaBgvvplz4YpsKM_W-QMQ3pgTcy5MB0uL42rk18D9kyDy-gcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62060f15d4.mp4?token=f55YVcBGc439uXyPHnQDUFu43cIgJGFt56SC5GhvRLYobKyq-Q9SZVt3b6WJtO2arTU1fXYZfSlN00e-8d1GDdkI0AHpzxedGTfStEisT9fWU_N7a_QcyueFo2IMGGHdMgHfnDLWLi89S_3tNaFf9oKd8uaTrE_PDytTnuAZyq-b_-KxKPnTVSEtFGI2tXrHd9V0Ivjg3k8alE2fQVfzcw6rv9rwj3HtJ7715TNlKRXWpTYEAb_bojyvdv2B6dwgugmINnHa9ESPrPgD6PmprJKi5xFErAbxIhOVNFaBgvvplz4YpsKM_W-QMQ3pgTcy5MB0uL42rk18D9kyDy-gcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
رونمایی از لباس استقلال و السد برای دیدار فردا
🔸
این دیدار در چارچوب هفتۀ اول لیگ نخبگان آسیا،  فردا از ساعت ۲۱:۴۵ در بصرۀ عراق برگزار می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/461878" target="_blank">📅 21:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/930111983e.mp4?token=An-v1JUmVuWJAx3ekyTDEfnln_sq_1jfF3KTMKCCnlLkxprTE6g2SiiRRd-A0hwx0HqyW13pWmlhSGLSlN6F7uguv7COnx6CRo7Tvp2lomPJGcQSuTAeRD2Ec6hmamUltowznrPX-jGboL7t9uSnZ9ERtrglbisou3sKadZjRrd_uBy6304vArTAS209vRqnTOGlYswHSt9_iwVV9uKjHBnaePSgCcbP0cEtaAzP8gYm8O6MJ7caSuUopIYu-QjXrajVExyepLZ4ADBJjg7jnIY8lxslZ5uvtMP-olVS7TxWOPRejO2J_YLOJaAi811m1lf4J_bLQNC9840xcQAU_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/930111983e.mp4?token=An-v1JUmVuWJAx3ekyTDEfnln_sq_1jfF3KTMKCCnlLkxprTE6g2SiiRRd-A0hwx0HqyW13pWmlhSGLSlN6F7uguv7COnx6CRo7Tvp2lomPJGcQSuTAeRD2Ec6hmamUltowznrPX-jGboL7t9uSnZ9ERtrglbisou3sKadZjRrd_uBy6304vArTAS209vRqnTOGlYswHSt9_iwVV9uKjHBnaePSgCcbP0cEtaAzP8gYm8O6MJ7caSuUopIYu-QjXrajVExyepLZ4ADBJjg7jnIY8lxslZ5uvtMP-olVS7TxWOPRejO2J_YLOJaAi811m1lf4J_bLQNC9840xcQAU_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۹۷؛ بافقی‌ها باز هم حماسه آفریدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/461877" target="_blank">📅 21:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfcb2c70ab.mp4?token=NvNh5uFuVIh2WwKalf0hjWoHM7MqmbjFqPYLXMNd6i7-nfdgaRe9jrxheyM_lnYQjpqul06OWbH-4TUjKs0hXbBlP-bEdeIAYWU8dtO-AKXLnkseRecMbPFmivHQiEYRhx4UiJgREoOkAQTRohbzdXXy-Ebi4bc2Ga0FimtMRZKXzV1xkuFrDpGgEVxR6kqUP92JT9_wUIsOzrTZMCBHN0z3hQu8-6LBF1rzSPtmuPmSpATIZG4jhxw94H3LaS18Vw4ZkAxGoluE-Z4vX4lCDRCrM0YszYL3by2w8W7qreI9ZQEwQuw0pI4yDKkQwHQk8gmN7-3w0RtmOGBK9qfqeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfcb2c70ab.mp4?token=NvNh5uFuVIh2WwKalf0hjWoHM7MqmbjFqPYLXMNd6i7-nfdgaRe9jrxheyM_lnYQjpqul06OWbH-4TUjKs0hXbBlP-bEdeIAYWU8dtO-AKXLnkseRecMbPFmivHQiEYRhx4UiJgREoOkAQTRohbzdXXy-Ebi4bc2Ga0FimtMRZKXzV1xkuFrDpGgEVxR6kqUP92JT9_wUIsOzrTZMCBHN0z3hQu8-6LBF1rzSPtmuPmSpATIZG4jhxw94H3LaS18Vw4ZkAxGoluE-Z4vX4lCDRCrM0YszYL3by2w8W7qreI9ZQEwQuw0pI4yDKkQwHQk8gmN7-3w0RtmOGBK9qfqeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه کسانی کشور را به قله می‌رسانند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/461876" target="_blank">📅 21:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f55a40f9.mp4?token=Hx0uzLwBiVOBq9ke8hlZCD0CeFBbkcOteOwznLZgjZHQ09wv3-Vb-fnnIM9TndqGTdBGzo53QLtn5Y4D1JJj8ZJIBb4GpfncIO_ilrVqsr1KcSLUihcKngUfdCI7oO_idOicZi_FROodeYNEb0bO9URdcLeOBxArspFO-Ki6QMYlxGqPZ0-19VJPAIyu0dWh1LOXjAESHV4P8nSxDOEpgrteLxNF9MvBCjFUiS4kQAytxwRPMuE1tsOdLIWRYD6_v3eQW1nc9XyiyEHW92ZBpBowP_A44M_A0Xp6wY_5GNf4TPPEdm9Cyqbkqr-2iU1BIyRObAdS3EQefo4eW4JFsAvmkyAnQ6KnFVxUJ9Gr5mhH8Mtdj0j6mOH1LMKkp8LiyOzOmuAO6J7oLbdXW68z3_FR7-rUEa5-I_coLDYbyNuLN03jRgz25F9qUh638JI9LFlu-yzjB99AqIQnfplrWPKCz0myJhkTMNBXEI1j8DS9wC7-lKAJvSKBTlZos-Eq6TLTzsRr7ufNUBMWkmjwTrf_a3ve7XYXEw3y92SpkqNQHVR9OGZq3XWTDyexaaZTUfQsbNbCVo7Xa_M5jnbnNPUJT4Eua4t613kpRm7Dlo4l-YyXhEmO_WQzhSSvxtQPPasYbA4J2IYUB876uYhtic6sgDVm1S6aLA1cnX8UJ4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f55a40f9.mp4?token=Hx0uzLwBiVOBq9ke8hlZCD0CeFBbkcOteOwznLZgjZHQ09wv3-Vb-fnnIM9TndqGTdBGzo53QLtn5Y4D1JJj8ZJIBb4GpfncIO_ilrVqsr1KcSLUihcKngUfdCI7oO_idOicZi_FROodeYNEb0bO9URdcLeOBxArspFO-Ki6QMYlxGqPZ0-19VJPAIyu0dWh1LOXjAESHV4P8nSxDOEpgrteLxNF9MvBCjFUiS4kQAytxwRPMuE1tsOdLIWRYD6_v3eQW1nc9XyiyEHW92ZBpBowP_A44M_A0Xp6wY_5GNf4TPPEdm9Cyqbkqr-2iU1BIyRObAdS3EQefo4eW4JFsAvmkyAnQ6KnFVxUJ9Gr5mhH8Mtdj0j6mOH1LMKkp8LiyOzOmuAO6J7oLbdXW68z3_FR7-rUEa5-I_coLDYbyNuLN03jRgz25F9qUh638JI9LFlu-yzjB99AqIQnfplrWPKCz0myJhkTMNBXEI1j8DS9wC7-lKAJvSKBTlZos-Eq6TLTzsRr7ufNUBMWkmjwTrf_a3ve7XYXEw3y92SpkqNQHVR9OGZq3XWTDyexaaZTUfQsbNbCVo7Xa_M5jnbnNPUJT4Eua4t613kpRm7Dlo4l-YyXhEmO_WQzhSSvxtQPPasYbA4J2IYUB876uYhtic6sgDVm1S6aLA1cnX8UJ4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب‌هایی به رنگ غیرت و وفاداری
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/461875" target="_blank">📅 21:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461871">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Obbun7Jas24_3xRj-wgHGvBdaHx6gg97CNgptDBp_zOEYWXr3tdSKwLVonhf_bRmynvnmhyG5eFkEk4Zb3i8yinLwPd_8YMyjvLyP6eVeOSEa2IzO_C8U8FS9ZBuLDNwZct9m80THjWMUqAVzrvT0hdg7-lFRXCu29Wrrg5qNrhnY1yrZsw8P3gsOzi40CQcBzFqjNtXA6frS3UwMLiHy0hybc8IMEEu0siQPVFA0yWznTmiY7GVfDzMuHxdNjLRgRWxlea6W9K6FYTtappeLId5iSacIMAbgomqGvJ3A7Z0GpLwW4mgXrPbQzx46ixzJJG4NSCdHB6tDMJlnDrbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4ifBgBaMhnblAm2UeMPjoCi-zkJMVYfDI2z9X47gHnNNjOoAHsRtBlZK4gGGTzHgtxn18zGD90BVi-06qZh4syW3ujJeU7EOo0UFXVKaW3glKPJtfGMOYsDH1eeeVvIUoOyOnys2WAgKPcal2-hCiujt1Ycc7Cv4WJtNXePH1iLpZEztw0RkdAd2oc-axy0gImiK-Skx_vHicLXfDCGvy2ohxWzX9vercwi8cM6HsUzIqkp_G5vcfI59lGHjL2BnUucK_EI84ZUw_0F18PkMfTWX7FZCp9Q_L_vhVV6WLEhAeQdTLYEvStgqSCLaSqhMw1INtbescXeHDSZm_VpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hL3tF2-tlVyDinz59fAF7BzJJ7UC-UZ2CroaiGdJksrNnTuGfbQRljUlhimfANMm8gFh9bgHB2jDbzhrph_pTPRdPQMG1v8VMK5FjPQC8sIZrKMYoh3bRH6aB7bAQreTKSdS2001Vi2X40_ifLfqMm1NcjD50Xpj1AMJDG-Jyw0zLH-LqP9QoM3qHWWVkMKoKQHucGs6eRE691547f19dvVub5xOoDS4gYNFbBiAvAI2Li8c_oAzQ0hpHlCo13M9synExxa0VRQ2kL6Z6aoiDuPfK0yV5MC42sYlZdNccWhVlNP_7HYh82Zg4pWMvIxBd75sgI0I5gFyQLgGnNEDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjGzB3QVOZPGF_l2ACN6aWzlT5Irgim2Ia6gPuQsDPMF5Fk1DSjUfjNboS2TUAvAqLm_Yp0oQeaMIRM4SowjedG-_pk_0Cvcq5-JQNzxiOl2RzTIiQgn8cLxHptU6NMoY2C9TvV0GERIJHXX1MllQ8jop1o0DeC7BHVnwZbEFGPPUIRWbTSw4JhCDyPXKIJ_y_RITC9PoXgxYcHfU-C5KJXSclgzvmFIKdaiFcNFMWbFRXr9H0lnAqhCTCJuAL5meEgBLEFnqDtL49NVPvxGuA7hH99D449n2HgWwoEd4WWxlQ8C9DcIQ-3He-m9K6R0fVyrY2_vVBNmVI265FmGoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تگرگ تابستانی در روستای گل‌بلاغی در استان زنجان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/461871" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461870">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace70d5693.mp4?token=GY_B5-zetBuzFSmpgC-absq22kT4C1HVJjq9cNUea8OMioC4U-cQpVPWXumDZDGkbm_BGe5Zk_QZhViGVOTSl2Xi_7_H05UO8c1btGOdG1c7Q2RU4NIFofvp1RHDX30GsNQWYrRYfIRO-pm_lvMkDBYP-lo0wyaPW89MJsTkqRWiUZ2u22lwNg6wtWCQgIThzrli5wysEuUHpyRnCL1GnMD1EttqOEf6S_Ioqs2t8VsisLYBHy_xVWn_EJL0KuH4y8Ikt27vR8cYx8w0iGhQNDjXlwdgfitez6qqsntUSFpdUys3MqcPMl_VJDcmDeXEqi8HhdpvkQ59rjJBaXtQ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace70d5693.mp4?token=GY_B5-zetBuzFSmpgC-absq22kT4C1HVJjq9cNUea8OMioC4U-cQpVPWXumDZDGkbm_BGe5Zk_QZhViGVOTSl2Xi_7_H05UO8c1btGOdG1c7Q2RU4NIFofvp1RHDX30GsNQWYrRYfIRO-pm_lvMkDBYP-lo0wyaPW89MJsTkqRWiUZ2u22lwNg6wtWCQgIThzrli5wysEuUHpyRnCL1GnMD1EttqOEf6S_Ioqs2t8VsisLYBHy_xVWn_EJL0KuH4y8Ikt27vR8cYx8w0iGhQNDjXlwdgfitez6qqsntUSFpdUys3MqcPMl_VJDcmDeXEqi8HhdpvkQ59rjJBaXtQ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۹۷ قیام مردم بروجن با مشت گره کرده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/461870" target="_blank">📅 21:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461869">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اجتماعی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADa9pBg_sLudATmruGAsb1qW6i71xWHNYIGWHM8AlYhMzCtUgPrH1mZSTVB3tlyEoJzpIicFdGdVYb4ZfBpZkd9Te4wgzxieXWHJjpFV-2XNZy1LFOqCN7XlSpWf1k_9JnRNkch3EtZynLlyKe4BpE4XdFErRbL0kR3pjPg_HXrsGF9Wkt3iKSe-MjFAet6-nVH8jKOCpOWwNnwoivsgfA4XlgicU6dXxZXyi97a9eXPUmIf9lZX1TF7LdumXP9Nu4jq7JJln6qu3fNVe9CVeUZA3gylkVVTjJ3rc-7GWKWvvb2lF2SDngbe1Ktklso84-_crujN9GUmY1Ux_IXB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست «آموزش و پرورش و اقتصاد در اندیشه رهبر حکیم شهید» برگزار می‌شود
🔹
خبرگزاری فارس با مشارکت اندیشگاه بیانیه گام دوم، نشست علمی ـ تخصصی «آموزش و پرورش و اقتصاد در اندیشه رهبر حکیم شهید» را از سلسله پیش‌نشست‌های همایش ملی «آینده‌نگاری رهبر شهید» برگزار می‌کند.
🔸
در این نشست، موضوعاتی همچون سرمایه‌گذاری و مشارکت در آموزش و پرورش، خصوصی‌سازی، روش‌های تأمین مالی و نقش آموزش و پرورش در قدرت اقتصادی کشور با حضور جمعی از صاحب‌نظران بررسی خواهد شد.
📅
زمان:
سه‌شنبه ۲۴ شهریور، ساعت ۱۴
📍
مکان:
خبرگزاری فارس
@Farssocial</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/461869" target="_blank">📅 21:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461868">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759f26ce05.mp4?token=Xv1uCV8dBsnKNV73uOhQqYCbr1a4vkXV1sWjavX6Kvw9HJJKRxNLBC-HgIn_oJQcIYcjAQF-th6kty__oxY0_u4yPQebf8Y51qVAjsJc9uIUCgQDGN0DJN6Fl9_qhoc1b59XJHZvQRMm_PELJBehdBsz_devisaot7SsUB5C-BWbcJNuDrRKCHNWiQGGWsZ9uL4pEpf378t8DyprNTkAY6-YoCsNyPyQYQwVuYuFIRB429XhMx2lcG3HEzAh9TOFfFIlNEH1nImqI6lSNau9G_APwtXpHU_hs9l120bKFzH_HI1jLfie5-J-ocO5jekD-IR_GVvjF9kleodG_x6r-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759f26ce05.mp4?token=Xv1uCV8dBsnKNV73uOhQqYCbr1a4vkXV1sWjavX6Kvw9HJJKRxNLBC-HgIn_oJQcIYcjAQF-th6kty__oxY0_u4yPQebf8Y51qVAjsJc9uIUCgQDGN0DJN6Fl9_qhoc1b59XJHZvQRMm_PELJBehdBsz_devisaot7SsUB5C-BWbcJNuDrRKCHNWiQGGWsZ9uL4pEpf378t8DyprNTkAY6-YoCsNyPyQYQwVuYuFIRB429XhMx2lcG3HEzAh9TOFfFIlNEH1nImqI6lSNau9G_APwtXpHU_hs9l120bKFzH_HI1jLfie5-J-ocO5jekD-IR_GVvjF9kleodG_x6r-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باب‌المندب؛ جایی که قدرت یمن به رخ کشیده می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/461868" target="_blank">📅 21:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461867">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308494cf81.mp4?token=jLQSFAMqw7c68NNav8ETLzkMZR3cz2tXRm1hpFdmzFHhEy-_3uD80AuuwENxZi-Ofu657Hu2e7Qg96CLrPhKnShUir7-7MLjdo_vJIWEu_ZYqOfrWVkqWM9aHLC4RASzQYsSQQMlbm0lsbTjhHcnTO2V75qik1QC8wOQKOJ6mZV3CJ0plcNnaKiIEZHuWt4PZHvLbfgv9lNcCGowguHsdofQT0_eUPfI7Qhmjy745Hf9HxUg39YnC2N_SRamxtWzHMTMRKkPARnWAjIu0mmZol_UWr5gtI67Z20mYXJ7-Xd7LYzo9pcS_dfZKl2TjlMhk9TcFXqVCjZ8rqw9Xf1_sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308494cf81.mp4?token=jLQSFAMqw7c68NNav8ETLzkMZR3cz2tXRm1hpFdmzFHhEy-_3uD80AuuwENxZi-Ofu657Hu2e7Qg96CLrPhKnShUir7-7MLjdo_vJIWEu_ZYqOfrWVkqWM9aHLC4RASzQYsSQQMlbm0lsbTjhHcnTO2V75qik1QC8wOQKOJ6mZV3CJ0plcNnaKiIEZHuWt4PZHvLbfgv9lNcCGowguHsdofQT0_eUPfI7Qhmjy745Hf9HxUg39YnC2N_SRamxtWzHMTMRKkPARnWAjIu0mmZol_UWr5gtI67Z20mYXJ7-Xd7LYzo9pcS_dfZKl2TjlMhk9TcFXqVCjZ8rqw9Xf1_sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیمت داروها بیشتر شد، پوشش بیمه‌ای هم بیشتر
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/461867" target="_blank">📅 21:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461866">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3511e6b655.mp4?token=uh3sFbvjVUooRYeydM6cHTz8RFt01BrxXSFlXYMNK0BlrilNAIJYL5kIjp9Hz8p2Dg5MgSsnuKa0ifyRxW472bXQG3tsdjFtEJtCHhLX6VYSRFAemiUGNqfEVsep5y98tcnKlNhsa6GgIeN_TVJ18aZESjwYFB-qeJuYmUP9hYelfKrNaQt3GIKkCEIYXyR96Ed0kVBpHP0OkK17ypm3KIIMF62K-fgMT3IyGQ4LGqo404eVV3Xk6i0nbQqYk9lTz9Uq3Y9fu5uGLqXzaoUxmd6PCfpuYpA1TIAXHFA1V7wrFckDNDr0nlAO68zyXfZ8mpZ7XDzz1K3Zsxn3DR2mBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3511e6b655.mp4?token=uh3sFbvjVUooRYeydM6cHTz8RFt01BrxXSFlXYMNK0BlrilNAIJYL5kIjp9Hz8p2Dg5MgSsnuKa0ifyRxW472bXQG3tsdjFtEJtCHhLX6VYSRFAemiUGNqfEVsep5y98tcnKlNhsa6GgIeN_TVJ18aZESjwYFB-qeJuYmUP9hYelfKrNaQt3GIKkCEIYXyR96Ed0kVBpHP0OkK17ypm3KIIMF62K-fgMT3IyGQ4LGqo404eVV3Xk6i0nbQqYk9lTz9Uq3Y9fu5uGLqXzaoUxmd6PCfpuYpA1TIAXHFA1V7wrFckDNDr0nlAO68zyXfZ8mpZ7XDzz1K3Zsxn3DR2mBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنایۀ توییتری قالیباف به ناتوانی تابلوهای بنزین آمریکا در نوشتن قیمت
🔹
رئیس مجلس بخشی از انیمیشن سیمپسون‌ها را به اشتراک گذاشته که در آن شخصیت اصلی انیمیشن پس از ۲ رقمی شدن قیمت سوخت و ناتوانی تابلوی قیمت از نشان دادن آن به طنز از «رایگان شدن» سوخت صحبت می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/461866" target="_blank">📅 21:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461865">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6daa8b0d6.mp4?token=VsTHCDo9vOtWv5QP9NTkST1TnB4FyIeE74M8Yv5yDmsfcL2_xmeXIB6cdavKT6XzX8L3UJcSKiuoVzylIJPAs3-GJK_knicWH9tGlxi-ytTUg5gCTPSYS35jic9a3qNi3E6DVOs-irgTZ8rlwj78VhNFOZ0JXKxomQO_99qgoIHQSkv91ZZbcli6pNyEhB-jQo3KjMztA5A-cV0jJQesnevCaHgEI0BEVJ_o4cwfe_jb81DDaLiXYfeWsI-Xm2avG6IqcBE2Gt784-7zbzon8Pira-mA00VYXdZSRRDW7kw-2G8OqvVBZ9iqdVo8VHigSK7su0oPXNix9zcSZQDesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6daa8b0d6.mp4?token=VsTHCDo9vOtWv5QP9NTkST1TnB4FyIeE74M8Yv5yDmsfcL2_xmeXIB6cdavKT6XzX8L3UJcSKiuoVzylIJPAs3-GJK_knicWH9tGlxi-ytTUg5gCTPSYS35jic9a3qNi3E6DVOs-irgTZ8rlwj78VhNFOZ0JXKxomQO_99qgoIHQSkv91ZZbcli6pNyEhB-jQo3KjMztA5A-cV0jJQesnevCaHgEI0BEVJ_o4cwfe_jb81DDaLiXYfeWsI-Xm2avG6IqcBE2Gt784-7zbzon8Pira-mA00VYXdZSRRDW7kw-2G8OqvVBZ9iqdVo8VHigSK7su0oPXNix9zcSZQDesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰ صیاد مفقودشدهٔ هرمزگانی به خانه بازگشتند
🔹
مسئول دفتر وزارت خارجه در بندرعباس: ۱۰ صیاد هرمزگانی که در امارات مفقود شده بودند، روز گذشته وارد تهران و امروز از طریق پرواز به هرمزگان بازگشتند.
🔹
این افراد قرار بود ۱۶ شهریور به کشور برگردند؛ اما به‌دلیل اینکه…</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/461865" target="_blank">📅 21:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461864">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1a408f8a.mp4?token=DxjPZQ323obALXD8uAunkW1GIzUYutZQ7Te208HWXbx_QM8J17XGu9ABG219ZgawIiY3K2i4yK5ZdjYR4mreRk--n4fHH_jaHyfJ7ix1fSdncCRpZXRNxl_uO7kxLyTZ0Bs8FExDc76VrDYydgmSS-ZUGQZCW4QrlL126FT4B7jiWbnFPTIlAaw8NxSY7jYDR-xNMdatB_Ua3NLRllLjO9MwUfzOQ1Fszc_AMoRHwPCJ5GkFtwnfLiBcFEYsCbebqkht_-6mMxNfT1Dm3ZucED9pzPjljabJHR6Z6cFXDKaI1VGEERjBbMl4sUs50B_DnNQ-YxlEkt93lBKz1wag5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1a408f8a.mp4?token=DxjPZQ323obALXD8uAunkW1GIzUYutZQ7Te208HWXbx_QM8J17XGu9ABG219ZgawIiY3K2i4yK5ZdjYR4mreRk--n4fHH_jaHyfJ7ix1fSdncCRpZXRNxl_uO7kxLyTZ0Bs8FExDc76VrDYydgmSS-ZUGQZCW4QrlL126FT4B7jiWbnFPTIlAaw8NxSY7jYDR-xNMdatB_Ua3NLRllLjO9MwUfzOQ1Fszc_AMoRHwPCJ5GkFtwnfLiBcFEYsCbebqkht_-6mMxNfT1Dm3ZucED9pzPjljabJHR6Z6cFXDKaI1VGEERjBbMl4sUs50B_DnNQ-YxlEkt93lBKz1wag5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات حمله به کشتی تجاری ایرانی در نزدیکی جزیرهٔ قشم
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/461864" target="_blank">📅 21:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461863">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dbebd2130.mp4?token=KVJt01dzVDrvMyVsZynWZbpgHeRHack3xIxNrVrL6U1idb5S-mTkspZH8syp6ZjBSVQK33ElCixMHQ_xIbwheBux6VJdEXDvTWgzW6tRsHXOtq_QbCK2mo-xaJpOkEPX1oKsaYSQRg56pui8Rzg7OG-tGUUseD4dilZnePRG3oU5VhTIhwfchThRYnbkDaK9YlbGIbcwStzhsksPNL8Irt-L4Qi7lhwRZVcSptIrVLY3EjF3Pe6SDf6YOXyzXRx75giNHfyZj9IsE1_9kjbcAa6yxUkPSz2cb6bHMfyeluqIIlwir87XwHrxakq-zkHAc26dutMaTDnGIJym1Z-VRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dbebd2130.mp4?token=KVJt01dzVDrvMyVsZynWZbpgHeRHack3xIxNrVrL6U1idb5S-mTkspZH8syp6ZjBSVQK33ElCixMHQ_xIbwheBux6VJdEXDvTWgzW6tRsHXOtq_QbCK2mo-xaJpOkEPX1oKsaYSQRg56pui8Rzg7OG-tGUUseD4dilZnePRG3oU5VhTIhwfchThRYnbkDaK9YlbGIbcwStzhsksPNL8Irt-L4Qi7lhwRZVcSptIrVLY3EjF3Pe6SDf6YOXyzXRx75giNHfyZj9IsE1_9kjbcAa6yxUkPSz2cb6bHMfyeluqIIlwir87XwHrxakq-zkHAc26dutMaTDnGIJym1Z-VRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس مسائل بین‌الملل: یمن به سختی قیمت نفت را به اینجا رسانده و این دستاورد نباید با خیالات از دست برود  @Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/461863" target="_blank">📅 20:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461861">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5df19509.mp4?token=kY0Xx10CRoIHQFPlKoa-QnC1MMBsRy-7hT9_MpIf5nC5YtJm87z_2HwztvMrGuN58xpp4W1Fl7bpiMk-fAnKv6LZQ8fCCwXOqhRjxKUztszjua0LWayjJhhPwzsGp2k_wBVKImfN32EZQ_uOqbClkn8LwU6g7VyYoyjLjTxD4N4aVVwo4fvsMs9ptzGOdAIU6J4-RKVh2gPxMMpRWeo1dF8s4-qp3iD1vpdiQHKKWVLgGQVq0-MJsM-Xsso2wz3nJGjvzTaSRdZiWNkWzDVNq4MnszwXLTNNDNFr8gKXGpYyuYh9AlP5dC8ZWGgvrZU9oW0NX7IwSX3HdE_NCFwJRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5df19509.mp4?token=kY0Xx10CRoIHQFPlKoa-QnC1MMBsRy-7hT9_MpIf5nC5YtJm87z_2HwztvMrGuN58xpp4W1Fl7bpiMk-fAnKv6LZQ8fCCwXOqhRjxKUztszjua0LWayjJhhPwzsGp2k_wBVKImfN32EZQ_uOqbClkn8LwU6g7VyYoyjLjTxD4N4aVVwo4fvsMs9ptzGOdAIU6J4-RKVh2gPxMMpRWeo1dF8s4-qp3iD1vpdiQHKKWVLgGQVq0-MJsM-Xsso2wz3nJGjvzTaSRdZiWNkWzDVNq4MnszwXLTNNDNFr8gKXGpYyuYh9AlP5dC8ZWGgvrZU9oW0NX7IwSX3HdE_NCFwJRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابت پرتابه به کشتی ایرانی در تنگهٔ هرمز
🔹
فرماندار قشم: یک کشتی تجاری ایرانی ساعت ۵ امروز در حوالی جزیرهٔ هنگام و در محدودهٔ تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناس قرار گرفت که تاکنون یک شهید و ۳ مجروح برجای گذاشته است.
🔹
هنوز نوع پرتابه‌ای که به این کشتی…</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/461861" target="_blank">📅 20:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461860">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
منابع یمنی: هواپیماهای دشمن سعودی با دو موشک یک بازار در شهری در استان الجوف را مورد حمله قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/461860" target="_blank">📅 20:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461859">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a204e443.mp4?token=XAXj7bSZbmNqfP6CeqEvzRntmITnmzzHktoV2eZuxaSOwOG2bntoSrBuAExFFYmYAUUkoA1Qz8d5glvm7Hrg9RhyP1QcYx_cIlEewHEDshAiJPd1eFuoDR-ZDYvxY5508uGU7wB15NDNvq_A06V8jcsslCrm-HP7IXViDK1tyWoT8bOkps97j_DLycpEPCuIKnIBFA2wbTJf4k-xz0MxrRprwXpbv_D2c7LUqAh2zsHsALZ9llCpu7yN8H6qP4uAXjoaTI5Ki9e8Zn-dFnOt87woI4WMnBJKw5ngCllwUcXuI4gjLLcHygpr5QemRrrf2-eFfXs4SU3YWfRJMWqXMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a204e443.mp4?token=XAXj7bSZbmNqfP6CeqEvzRntmITnmzzHktoV2eZuxaSOwOG2bntoSrBuAExFFYmYAUUkoA1Qz8d5glvm7Hrg9RhyP1QcYx_cIlEewHEDshAiJPd1eFuoDR-ZDYvxY5508uGU7wB15NDNvq_A06V8jcsslCrm-HP7IXViDK1tyWoT8bOkps97j_DLycpEPCuIKnIBFA2wbTJf4k-xz0MxrRprwXpbv_D2c7LUqAh2zsHsALZ9llCpu7yN8H6qP4uAXjoaTI5Ki9e8Zn-dFnOt87woI4WMnBJKw5ngCllwUcXuI4gjLLcHygpr5QemRrrf2-eFfXs4SU3YWfRJMWqXMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس مسائل بین‌الملل: بازار نفت آمادۀ استفادۀ ایران است
🔹
هر بی‌احتیاطی در نکات ریز دیپلماتیک می‌تواند جریان بازار نفت را به نفع دشمن تغییر دهد. @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/461859" target="_blank">📅 20:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461858">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns3jS9V-pCzdyCQFyJguNLvO4gDz0l7wUns_8oJGXtvmZveAQGvXAc2duJyAf_Mp2ZE_ZUF66SCbqy161q2MA6SfV23AIUNBkoMcB6cYDAE6yBplEY5EzFRSp_t5Ze1EcyA2poT7WrtuBn61jiSFeKT6yooJUwwq2L_mkM53mZnYJCFVUvSLlMAWAchf7mTw5_PzfU7IgXrfaxXg7Eb2Z0BcpTBgrBmhlwIyFtvqFrktbIkjIzRjlvDd44ysxjbljtYsy01Gce4H6WJeUsIHdICGoufRh44dnXM1wWKtMKQ7ZBoN9ELsxhj5SXyvDgO7yc_Sft3yh2DxfLZKD_WTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن‌سلمان برای مقابله با یمن دست به دامن صهیونیست‌ها شد
🔹
روزنامه عبری «اسرائیل هیوم» گزارش داد که محمد بن سلمان ولیعهد سعودی از طریق آمریکا به این رژیم پیام داده و برای جلوگیری از تشدید تنش در دریای سرخ و باب‌المندب به دست انصارالله درخواست کمک کرده است.
🔹
این رسانه عبری افزود که عربستان در پیامی غیرمستقیم گفته است: «در جنگ علیه حوثی‌ها به ما کمک کنید.»
🔸
بر این اساس، دستگاه‌های امنیتی رژیم صهیونیستی در منازعه کنونی قصد دخالت در یمن را ندارند مگر آنکه این رژیم مورد حمله قرار بگیرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/461858" target="_blank">📅 20:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461857">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1FbIqCQgNC2SYP0VrOmd6QNwYScI0RoS5F5NB9MoCZHH_I0x2Zr_pbRCR-4H5nS5zoo3V5Kn5Y_EHA6mDez4-3NhJjEPIgKfZn5zR4e9fX2wG2ebKM15yt-dyU9u0TJHQLKWyqocs1Ic3AuhbyuZdO1loL4P7jGKYkWU9NZiD7iT4cJmcHmlnysXMi6QTEuL5XvW80EuL8W-1r9B2RTcR1myHzi7HX4rZLM_3ifKI74GCsiXJV5p9K5n3sgcaOxwVJeOJHObpB9uF7eDJWaNs3kCZGYUUltNBA1VF1cUqwL6gt2VxuOv5mS9vAJEwBbPDjBIkDu2rwaHi_ns36QuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حملهٔ روسیه به ۸۰۰ متری مرز ناتو!
🔹
همزمان با تشدید درگیری‌های روسیه و اوکراین، پهپاد روسی به یک کامیون در فاصلهٔ کمتر از یک کیلومتری مرز لهستان اصابت کرد.
🔹
این تأیید رسمی پس‌از آن صورت گرفت که انتشار تصاویری در فضای مجازی دربارهٔ سوختن یک کامیون، منجر…</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/461857" target="_blank">📅 20:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461856">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a0a841cb.mp4?token=j8ND1IPRoQ8gUTbozLxKdAkfVzc4B4QJyNNYHG-lLfzCRQ1tinz9JxwzAS2bTvdhKbLZclSmNCoyR9tgg8LBFtpaNbuT8Jt6YJlt2YTjwgMdqFuFADiuLgvB5HDVHkT3zVOGye7IV5OOuEahunXiYgzb0OLhJlTI6Q39OzUzU8ru7tce9I3eO2_O_XRaBBEHXwU3fRNsGjEXn8EvzIFkPdv1sok60oYQHE4gkQGfPl6bRaSFVNgUzfkFLSJxIjqXb_ueKHKLyhQMHoZ9qkmWfljA0bygmL6O1GiFv9H78Bj--XBQRFB9g9sAOFxOmn0e9WEWCNnmoHbjGsf5DaV25w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a0a841cb.mp4?token=j8ND1IPRoQ8gUTbozLxKdAkfVzc4B4QJyNNYHG-lLfzCRQ1tinz9JxwzAS2bTvdhKbLZclSmNCoyR9tgg8LBFtpaNbuT8Jt6YJlt2YTjwgMdqFuFADiuLgvB5HDVHkT3zVOGye7IV5OOuEahunXiYgzb0OLhJlTI6Q39OzUzU8ru7tce9I3eO2_O_XRaBBEHXwU3fRNsGjEXn8EvzIFkPdv1sok60oYQHE4gkQGfPl6bRaSFVNgUzfkFLSJxIjqXb_ueKHKLyhQMHoZ9qkmWfljA0bygmL6O1GiFv9H78Bj--XBQRFB9g9sAOFxOmn0e9WEWCNnmoHbjGsf5DaV25w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا در روزهای اول تفاهم‌نامه چندبار آن را نقض کرد؟  @Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/461856" target="_blank">📅 20:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461855">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0mdIiuNyPCWyEGjjh495wyXG8-7fh_VeSv6iUfyW46pXR6l1zzyp77E75qX_JOAt_q8CxAfOdadRIu-G7Ii2YKmiacC_2VEibczJbjbKgck-Qukq0PGRxQ0GXhQBuyMn49LoS8OfvXDwQaUsiHBRo-Abgvh2KigPq0wpHkVXG1ccfNkJQ1XXTzI44pdf5G6qTuB0U8dq5Wd3XNlURJl4THQnDTWX6a_nqQtYx1Fxnl4jAtSFVRRA7YC1cfLlJCuLa8lFJCY0lW6SMMeCO19MzcTfLRWmuYgEeFy5Uuj3XhYv4XS21ooHPuAoO-GmhKnf5cz1huk2H59QjxTrB1YWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژیلا صادقی خطاب به بازیگر زیرزمینی: چرا از اون عروسی حرف نزدی؟
🔹
صادقی مجری تلویزیون در واکنش به صحبت‌های لاله مرزبان در فستیوال ونیز: «خانم مرزبان! شکر خدا زنان سرزمینمان آزادند، اما کودکانمان قربانی شدند، جوانانمان شهید شدند.»
🔹
او همچنین با انتشار تصویری از کودکان شهید میناب در کنایه‌ای به مرزبان نوشته: «تو وطن فروشی، وطن‌فروشی که فقط جاویدشاه گفتن نیست.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/461855" target="_blank">📅 20:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461854">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJCi2mxldAvEKkTlW3QUjWNAXbt3dG9VH4nlVJiW-LklVctMUNZenqk6o6cMD48IaJ4SfQWQYCVT8I9WcWBu-75cz6y4a1qgxuI_rfj32zss5ivH9nPsVxgDR2n9gNJM_7fsPrteh7Eg0X9sb0L8_jf1KjvvHdLj9X92ZWUsGOjEQWmYUYMJD1xkxCm-H4RGIP4rA3BJFLneqkpVJnNYTs0t5_dayelHcud-_kMYP_7e15w1-icaWX29OlXhQV4lPc1vxRmtSuqkL-IVUokzbMo63KoQnlTFWLkL381Vze7Vs1BC7QqQkBLhMM1ejqX6HTTsSy5C075di_b63iwBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قوطی‌ دنیا را تغییر داد
🔹
در اواخر قرن ۱۸، هنگامی که اروپا در آتش جنگ‌های ناپلئونی می‌سوخت، نیازی فوری به تغذیه سربازان در میدان‌های نبرد احساس می‌شد.
🔹
سربازانی که روزها و هفته‌ها در جبهه‌ها می‌جنگیدند، به غذایی نیاز داشتند که نه‌تنها مغذی باشد، بلکه بتوان آن را برای مدت طولانی بدون یخچال نگهداری کرد.
🔹
در این میان، آشپز فرانسوی، نیکلاس آپرت، با ایده‌ای ساده اما انقلابی، شیوه نگهداری مواد غذایی را برای همیشه تغییر داد و کنسرو را اختراع کرد.
🔹
این اختراع نه‌تنها سربازان را سیر کرد، بلکه راه خود را به آشپزخانه‌های مدرن باز کرد و شیوه زندگی ما را برای همیشه دگرگون ساخت.
اما کنسرو چگونه از دل جنگ‌های ناپلئونی متولد شد؟
🔗
داستان کامل را در
گزارش
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/461854" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461853">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be10a4e8.mp4?token=W2UbXMdFrsaXCeABAmsUYgoL_6eqeqVvr4ThkrmdDPxf2VT5OUW9k3d9dyrO0yiqcKZ9NCadMxjBywD8FcPX1VT_xWsA1Zbcba7W2EhubwttvRBiyzAuNR2YBI2SA0gbu4jpwHhQSCUGeC3XWPO6eUEabJxFvEpzhxbh6ZTziOoT2ru60I5FX-ECldF-S2t_e9hN4Si0YxL6eVBRgn2Lg8VTIz6HtVea2TldNZYNvMpoLUGvu19l-vjz3IeoJ0K0GFLObzoqgD8oZ-k17ikMQAQqIQBG5qL0uzNuaHRNkJE-pTqCH0dz_kP28A7bP6hizBy47qT9IWr-Loe50JxnjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be10a4e8.mp4?token=W2UbXMdFrsaXCeABAmsUYgoL_6eqeqVvr4ThkrmdDPxf2VT5OUW9k3d9dyrO0yiqcKZ9NCadMxjBywD8FcPX1VT_xWsA1Zbcba7W2EhubwttvRBiyzAuNR2YBI2SA0gbu4jpwHhQSCUGeC3XWPO6eUEabJxFvEpzhxbh6ZTziOoT2ru60I5FX-ECldF-S2t_e9hN4Si0YxL6eVBRgn2Lg8VTIz6HtVea2TldNZYNvMpoLUGvu19l-vjz3IeoJ0K0GFLObzoqgD8oZ-k17ikMQAQqIQBG5qL0uzNuaHRNkJE-pTqCH0dz_kP28A7bP6hizBy47qT9IWr-Loe50JxnjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاکستان هم فقط حملات یمن به خاک عربستان را محکوم کرد
🔹
درحالیکه حملات نیروهای انصارالله به خاک عربستان پرسشهایی را درباره فعال شدن بند دفاع متقابل پیمان مکه ایجاد کرده، نخست وزیر پاکستان در تماس با ولیعهد سعودی تنها به محکوم کردن این حملات بسنده کرد.
🔹
این…</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/461853" target="_blank">📅 20:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461852">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jriHspiG7yxJzFH4bSjDqD655PnYomhHuD_7gcBf1w6gGK5XDsBO6J3nUi746jpUui2qwZbApvR82atLrEeV-LPkPopEVuUSuPolK3zAudDjmOXhXQ8nnK_Wsax_fv3vw76HrjyhxXtEXYo8bir2COLMvSjAnhC4jFj3jA_wvFl6pIim38eTfENluQj0N8gtnm5mCG02_O065_yafkq7Kn_ZT3cJsnTk9XbPGZHAG34OL4QE2cfH2ShMHC7L9p93DPrumsY-ZAkNUnyvP1y0gitrHyJ2ovNpEJmWE5jLDb20eXA6bdJb79-colzrk7uNQrAmb_D3QZd7FWBciDAopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خاطرۀ سردار علی فضلی از حضور رهبر معظم انقلاب در جبهۀ دفاع مقدس ۸ ساله  @Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/461852" target="_blank">📅 20:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461851">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d7804b6d.mp4?token=lnQkzObKHv-UBfxrMgyumNQIQOgaeKizt469RAIr7Q3q7EHtI1mfKZA0cCXHyR2Mu-Ui0pN4S2y3F1iTHh_LJBfQmreG5J0Ex3ClM3Wa1dnbTn7hlZdH5PxgDSSRidnSoI-YdE504bZ3zA5Oe4K5v0hiSJXRpAw_0lrDowuAz41ffPXhN-PiE13Gak4BqpTPdRkW4rQxgU-rHHjyIghAtKW4q7P_GiVSzUhbAzhTg3Ep11U3Q-15W1fycO5T4IMouxAgoyO2S5a6Oo5x5epY7NDwJA1TZ_OPlsSrPpz1RnyLm7EotFibRY1gatDj6QLDwxXiwjIYXWvF4T17jDA34Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d7804b6d.mp4?token=lnQkzObKHv-UBfxrMgyumNQIQOgaeKizt469RAIr7Q3q7EHtI1mfKZA0cCXHyR2Mu-Ui0pN4S2y3F1iTHh_LJBfQmreG5J0Ex3ClM3Wa1dnbTn7hlZdH5PxgDSSRidnSoI-YdE504bZ3zA5Oe4K5v0hiSJXRpAw_0lrDowuAz41ffPXhN-PiE13Gak4BqpTPdRkW4rQxgU-rHHjyIghAtKW4q7P_GiVSzUhbAzhTg3Ep11U3Q-15W1fycO5T4IMouxAgoyO2S5a6Oo5x5epY7NDwJA1TZ_OPlsSrPpz1RnyLm7EotFibRY1gatDj6QLDwxXiwjIYXWvF4T17jDA34Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش شدید باران در مکه مکرمه
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/461851" target="_blank">📅 20:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461850">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa2d1e303a.mp4?token=ov8fHvj9WLDhYhn-dJd20gL5wQ7q_AL97azrpCblzyOQp8-24bCASY8FLsSyPj9pjdb0lj1UM7ietfDjWJPvem1g4-JXV5a7J07LjQmNme560OYr7IFSElP_UaVhmEpDPdI3qK1SGI2WHV-zhpIWV3IUUTyqMgl5-yPXRVxio2eSEbV1cTimqQmj3y73Bowcgyz_wPOfkpGE6h6WpYeLzvmWa0TIRGovKG0QitbBBHlgX5Kn9ZjbWLPnrpoE8CIwLfADIiTEgmUT6jMWs_DSJmrvOxiGM16JAFI4Ze_5bUW6SdF-3KJiJOlNMzWgMW9BoENYSuSrtlOnFVgzMkthag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa2d1e303a.mp4?token=ov8fHvj9WLDhYhn-dJd20gL5wQ7q_AL97azrpCblzyOQp8-24bCASY8FLsSyPj9pjdb0lj1UM7ietfDjWJPvem1g4-JXV5a7J07LjQmNme560OYr7IFSElP_UaVhmEpDPdI3qK1SGI2WHV-zhpIWV3IUUTyqMgl5-yPXRVxio2eSEbV1cTimqQmj3y73Bowcgyz_wPOfkpGE6h6WpYeLzvmWa0TIRGovKG0QitbBBHlgX5Kn9ZjbWLPnrpoE8CIwLfADIiTEgmUT6jMWs_DSJmrvOxiGM16JAFI4Ze_5bUW6SdF-3KJiJOlNMzWgMW9BoENYSuSrtlOnFVgzMkthag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا در روزهای اول تفاهم‌نامه چندبار آن را نقض کرد؟
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/461850" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461849">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_HiEkHjm7G7K8Qcw7wKU3AwFGW0uGHBMVWTt-byaX6lrmQC5M_nbc-9zTlhnGNzBCt4sf3l7K2Al7jMyQcyxzFNKt3EdVFVsm-Gh-2CkgSWAV0xQYbz-tFWNukoIH0nBCRnoE1e1bcxD78Njjgw-N4upAe0AtCW2z5Iu_Ckv4YLnMv9IiMEvlpa3a2DMW4Zt9ZL5XkVMSFArfLaVaHbqz7xyOS4kXHeVpUYsp4fxy6vLhh-H2zqU_N5qy1S5kaIiF8R4j3iLNuOycgqX7Vfog8QZHxjBE2tQORhKVrIaJfg3_G8nn_A90r-NIDn_nwvGF-nslTz2eNHAExgvJa_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلهٔ طلایی پکن برای دلار
🔹
چین درحالی ریاست دورهٔ آیندهٔ گروه بریکس را برعهده می‌گیرد که هم‌زمان روند افزایش ذخایر طلای این کشور ادامه دارد.
🔹
اقدامی که در کنار تلاش پکن برای گسترش استفاده بین‌المللی از یوان و توسعهٔ سازوکارهای پرداخت مستقل از نظام مالی غرب، بار دیگر بحث کاهش وابستگی اقتصادهای نوظهور به دلار را مطرح کرده است.
🔹
اهمیت این روند زمانی بیشتر می‌شود که چین در کنار انباشت طلا، سیاست بین‌المللی‌سازی یوآن و استفاده بیشتر از ارزهای ملی در تجارت خارجی را دنبال می‌کند.
🔹
آنچه در حال شکل‌گیری است بیشتر شبیه ایجاد یک شبکهٔ موازی مالی است؛ شبکه‌ای که در آن اعضای بریکس تلاش می‌کنند وابستگی خود به زیرساخت‌های مالی تحت سلطه آمریکا را کاهش دهند و سهم ارزهای ملی را در تجارت و سرمایه‌گذاری افزایش دهند.
🔹
اگرچه نمی‌توان با قطعیت گفت چین به‌دنبال راه‌اندازی «یوان با پشتوانه طلا» یا حذف دلار از مبادلات جهانی است، اما اقدامات پکن نشان می‌دهد چین می‌خواهد نقش طلا، یوان و سیستم‌های پرداخت مستقل را در اقتصاد جهانی بیشتر کند.
🔹
این مسیر در صورت تداوم می‌تواند به کاهش تدریجی انحصار دلار در تجارت جهانی منجر شود و یکی از ابزارهای هژمونی آمریکا را از دستش دربیاورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/461849" target="_blank">📅 19:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461848">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJYtguJVR7y2Boj0baCTMc4cj5Y6VtaCnh3rHLLlJvd5OOR7zbwJDTZkWUskSBDhxmSVr11MNdi3T_5YuGPYxdWABrIUdR90Z7zUAf61sa26eviNDgP6hi54b28ux8xzsm2X9u_58-ANVkHObPBG6XuLLRXTA3KhzoF2Ta8_VgT-Pa_sSnm4WkN0QPL8f9ubw5ZpI9zjRve9R2gLFqdN6gK4Q0A9wpgQ6wtpUv854HeBmGsjr9cSoVzrS3uoyXjychppIAnMOzdM5DluL1IkB2-PNhjjOqgttKWVzBnrHh0X1WH0kD_-vQgUkqYKbVc5PNtbHkuKtQPQ3CuOm2gnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت سرباز صهیونیست از قتل خبرنگاران در بیمارستان غزه
🔹
رژیم صهیونیستی سال ۲۰۲۵ در یک حملهٔ دو مرحله‌ای به بیمارستان ناصر در غزه ۵ روزنامه‌نگار از جمله حسام المصری، فیلمبردار رویترز را به قتل رساند.
🔹
مقام‌های اسرائیلی پس از حمله اعلام کردند هدف، یک دوربین…</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/461848" target="_blank">📅 19:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461847">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۳.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/461847" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۲.pdf</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/461847" target="_blank">📅 19:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461846">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2PrJT_WLea068eRw7Lbygy1rC4FuMEKJlx0CjwoQSBkFREw5_4Mve3ht0OLrzBi7m6vR77ZoWGaeNzcUctasS5qG8a-PRIgsi6IkWFe_w3Zvh8_yLhPcYgcAL9nQ4BBiVzNovWkc71Tea3lctlSkz56VdrmeVfWSJVrNUQ5acNiZkqyiy1-wCgmJRlE0yzPdBI6YNQ5MSCpXzxkiCV1I5A9bfWBKPGLEGJL8g_VEIfrUzIpIgnB3HlHAAUdf-sCXNjXixe6A_nRR4Acq679peUrHAnKdwjSNWQgWYuyUZr9ijh0_ALZst32wHDfbiQXR5ZCNpsWhxlDNZsIRK7VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سردار رادان: بیرانوند از اول مهر سرباز است و شامل سرباز قهرمان نمی‌شود، باید بین ۲ تیم ملوان یا فجرسپاسی انتخاب کند.  @Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/461846" target="_blank">📅 19:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461845">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTKsren-PZSpNBXCoOSkYtP83yL3kXafg2w3Hq0SjrnFPLlKCHkpgQRNaWvIpID1jfZGQ6oyNN1iRaL5e3-xdYkBi1D8oQEHmUwBYC8Fla6kC5TT_egh93T0AwLH5oMcg7iHG8qcxnmjsjGK9Cd8PAnu9TvVlvQaYGpaeuR0bXHYDskTjNuNxf7aViH5zYY3dsPmAnPty0PimhWdA8HoIsjdJ5egyHU-E8El_VpaVfbOjLQ9XIdcuc8PtAhap2tUylGtn67cALLbxDkiOiMsct8h5mCLLxYewy6M6TYEX5SDwPwvmg7haJwoHRfKv_3oc69AclxaP_ovUkJauDxfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخلیۀ قطار نخست‌وزیر اسبق انگلیس پس‌ از حمله پهپادی در اوکراین
🔹
مجله اشپیگل گزارش می‌دهد که چند سیاستمدار اروپایی از جمله «یکی از نزدیک‌ترین مشاوران» صدراعظم آلمان گونتر زاوتر حین بازگشت از اوکراین، یک حمله پهپادی را تجربه کردند.
🔹
علاوه بر زاوتر، مشاوران امنیتی از کشورهای مختلف اروپایی، اعضای بوندستاگ آلمان، دیپلمات‌ها و همچنین نخست‌وزیر اسبق انگلیس بوریس جانسون نیز در قطار حضور داشتند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/461845" target="_blank">📅 19:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461844">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewq10XHReVBnVtT9B5ZnL9UZVyuTl0A3ERHdfx7WwoTxVXM9L98195GIFsbYNJ9DG1cHeHeUlMqJCvpZ2OkJzRrnFgT8yizddKLzVkwWBvB67-d_p4E0StVvkAqytVIpSRIagCJKNJFQZ9QGioZqhfP8L6v4jzL2mTScayYi1aXl75nd-NS2z_UWgZOCMVsLyPwhQRRsiP3AYCILSjkXwNQiAST9JSoLf4FRruxSodmC93d3uWK_XpIhxgE1uk_FXLrhSf8pLaDUAArfWZYnAeFWWVeAVjPltdPA4hx7t-XdnV8ZCP_fyhcS2xIVX2g_qX-QYYoTpJ-AHJ6LKICX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رونمایی از لباس استقلال و السد برای دیدار فردا
🔸
این دیدار در چارچوب هفتۀ اول لیگ نخبگان آسیا،  فردا از ساعت ۲۱:۴۵ در بصرۀ عراق برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/461844" target="_blank">📅 19:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461843">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یمن اتهام سعودی دربارۀ حمله به یک مسجد را تکذیب کرد
🔹
خبرگزاری سبأ یمن: یک منبع نظامی ادعای رسانه‌های دشمن سعودی دربارۀ اصابت موشک‌های یمن به یک مسجد را بی‌اساس دانست و گفت: تأثیر موشک‌های یمنی بسیار زیاد و مشخص است.
🔹
به گفته این منبع نظامی، علت این حادثه سقوط موشک‌های رهگیر پدافند عربستان در مناطق مسکونی است.
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/461843" target="_blank">📅 19:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461842">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALO87-p8WHNfK68R2xE4SnH2-lFsEKx8PtJL2g1mUF8WcWUawGJLd2XJgBChB03E3OgeG46Ix5dPFlWuLrjHhYv7G7iV9YxlAxgX_uTQLUa6DGJVYjNnWIxKSbfeztPBNKmgesu6anvsYeSZASHyoaffX57P4EJ3QXet5mpn-_Em4GAbu6Eg2YXfJFCaGuwrDA_JWyqcOrL_FqsazWNJacAtAXuBggUOxA7BzGUsm2Rq9_Gh4mOHgVsRXOBPDVtK0Zm4F_PuMdU1Es78b5paBjDL929QFJd6htWoQ1jPwe_8Sc8VLOv5gxcLoaFv9PzM3aHXsb-TaXp3IWmT-MD_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک شیر دریایی بر اثر آنفلوآنزای مرغی جان باخت
🔹
ادارۀ محیط‌زیست استرالیا اعلام کرده که آنفلو‌آنزای مرغی باعث مرگ یک شیر دریایی استرالیایی که گونه‌ای درحال انقراض است شده.
🔹
کارشناسان می‌گویند گسترش آنفلوآنزای مرغی H5 می‌تواند باعث مرگ‌ومیر گسترده در حیات‌وحش شود.
🔸
مؤسسه پاستور فرانسه پیش‌از این گزارش داده بود که آنفلوانزای مرغی درصورت جهش می‌تواند قابلیت انتقال به انسان را پیدا کند و یک «همه‌گیری شدیدتر از کرونا» ایجاد کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/461842" target="_blank">📅 19:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461841">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11d60c2a5.mp4?token=EMsTAtShmPHka-3oO47VEN2mQrx2zSMStUvEpWnd9ydImVyD43NyeQcOdozjsyFZfg3DgET_DThOnpe8GbWo8-ID8NQYKcLYTz_NH2o6rv3ytAJQgb9kE0RrH9QqXaW6fIlzSAJ3E4SJAB8GtGa77gsuvZBKKa7PLxZKCo1QGaUFnVM5ZjYn4venUrcdzYfqFoVJTPuvulRZoOozXgyL5gJWbW1wqiaNWafbZbGDxpdGFTo81W6NIl-kfcv6s9mGy5ZjuIC8IwGaddm3w28_FH4jMn-gc7pPYFJPSgVfDsCfYm5mc7I6Sga6aNv3FZvnR1V9vqF5KzOur8OXSWwgzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11d60c2a5.mp4?token=EMsTAtShmPHka-3oO47VEN2mQrx2zSMStUvEpWnd9ydImVyD43NyeQcOdozjsyFZfg3DgET_DThOnpe8GbWo8-ID8NQYKcLYTz_NH2o6rv3ytAJQgb9kE0RrH9QqXaW6fIlzSAJ3E4SJAB8GtGa77gsuvZBKKa7PLxZKCo1QGaUFnVM5ZjYn4venUrcdzYfqFoVJTPuvulRZoOozXgyL5gJWbW1wqiaNWafbZbGDxpdGFTo81W6NIl-kfcv6s9mGy5ZjuIC8IwGaddm3w28_FH4jMn-gc7pPYFJPSgVfDsCfYm5mc7I6Sga6aNv3FZvnR1V9vqF5KzOur8OXSWwgzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ توپخانه‌ای رژیم صهیونیستی به حومۀ بنت جبیل در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/461841" target="_blank">📅 19:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461834">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOCct3OCXb-2jIKMnHVqtiDB16-DxC9IegwBTWkcmu2HoC40UPvRbNrIGlSw2xB8bx8UbHPNcI02HsGV9HiuRZhkbQYaq-poY1iHw9DNBBWErO9IjT_oM63LSyljMnT0axoinmvhlBtQx00n0SKKkfH83mei2vvawBFFMjBmoi4D4at9oOVEdL439lTwVcZdjMsu38P6_nwJIASR7UxdoE6ckAvZ71MeqadnY5NcKFIz944VA7Wqux94aksKhhnBQIRUUt-mms7eGRj_PI1kLYs87HLqxg6wZKXuxuMuE47UJIKd6fHqxkxNli5ng_PQzqKzQXqwS5sv8qezWufFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CmJaObnqm_XTEWnTr9HXTNPIy-a8kgrHI-Qkz9uuPOGZfIHHWMwj5MdbVSGSZIig0gWLijhHQRUlIhCL--bcMVCQL4ZI5kDDEi9cvuStuWlPCp1cV36lnoe82tPSX2DHcoPvVP9HW1e7XkYHl3162FkCeO9oaSDNCkRvZXYoIBaRVU50GC_mJ5Pv0Bo9gY6jYLL9JNixDKgHJSLFma1bK246UWgyfVNTssT6BSVqQHQ_o2joMSM-J0qOQSF_8j4VGHDtN7iPjYfAUDXfSAlhXENB8QciWP_-rd4zMjZYTRDosv63QJhTjuvTDPmVTbTSyahgIqET5QzT1OMfgPaxwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AT_YcRyOv5BPXBrNBMHF1g_bPgnVLSlBvHHQQZK_HVjiznRjAGVJaacL3ZkcSUN343D2wa1uvJIv9ObMzGiO_wYzqVmdboKilC_ac7t4kXHw4zfd7mlFAbJHm2v1JZf8HeEHVVDNVEU41uIkZ-Q5xRP5MiF3Ccw9eDf1D9aYHo8JVd3fAINgWMm6c-7scCGMbHKf40teqefQqfS1fG0xd7RYfMYju3kjNxL8Uy9Lload0ZBrDcd8IdvdBeTQK_abBwHbunSx8TLi2wyZWZFWi9SssQaVP231DMeL1YqL3Ha_5s4QS6IWzi-SltC54r-FLGqRW6h7UcIe3dcIBhLAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0EmwEPnzLKadNS7-tEiIPU5ATi2uaHDkpOTomxH6rNtx4agHKFmCUdUl-5DgEuYBHFs2Dv0xos2Gu8c3Y5wafQurou2vKYeMpz1-cKNX1ijCktGvCgV8oFfo1Cn9Rg6OHIEAUdJTQgxNYfNZLKxYY9k9DEB17TGl8fNl6HXTR2GzsUvhBopuhKngBg702KIwQvElgniizoVSdInL7x2VIcOCrhMYg1Y2x7KuzYXvkwozX6feftFykvVZoHq1OcnFSXzEoNr47Fig63XO8eMyp7usmfn8Hn1uEFSZe_Xo3nTNzGCytFd6cC3Ncn6QboZWMuwnhjC-wshrP-9J_7vhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjJhmDh38o9BhWdjb3QIOPBYOktL38FDJhfVk6MdzsAeg4yL7CW8GcyEFV50aaYtZcRw2MXOoG9ujiT0OL5X-VvtcgyRwmn5eeUz4zysxR7rk3gev2_hgfzzEnAqsbduyqnE_0A4ftCefvEjHnB-YI1bmSyOWiYbwY9FLdditO1ZcJfgLRcUh5aP03i34TTZVBfoAFMZ99_IDq_f1ET9ZFMo3cZaYvxK79gSjL-Wt5_8t9VIYW01-U3Wj4BS5_N8lqsRJaUnWBM4V5tnNCAvitHhDNGAdLLqPAD5GLPiGcbBrV-Ji8G0MQueGcE9bzp-BsW6gtMFWzlRVQNQqg315A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YapOX94v7vH4XOQhlwfwoIS2PhsroRJ66MsvRWMwWN3nyd6Kz_FWW0Z1JUXnIH0IaTY6UyYhIBpo4VZNL-ZwqxqDTbgG0ezIhm6P9VAcJCnV8X-hFvDYWwut9JcTtxJ4ChYLHX9b28qCIWS98EsT7OTlmB8mCmxNIbnoXpLrojXSPWtCvnqy7Gus_mYUvu_INOxhSMBlV7YFSf0J2xYDnLdfGhRLwUdRMNohjY6cQENBFUQ4v3sDOO89MI9Rax2piJ19Elgz-tHf9rKwSCpfEDWBBlg8i1qJydKocieGgCvhBWcuA-hx8T_aan9-PquplUrhcFvB4EG2uuMB3A9s1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEHBKQpoqnH9TsX58rg842JyP_o_uSlRLCgqbe-IZqaxJicVF0XjUUaJmwJsZpYqGJbT_X2dlW9rYVfdf2GKPkhzme8e7y9a_TXXEeWOrab1E6tXcUn8FKhtaSp3syBtgJMZu54alw70P2hVYHNXSLL2YMYLS988seghSVg-4k6iYbUBiBPwKMoc2zcPLbV85lrRYJ5El87UNpK_bzM9AccIEX0CWUdJnl9phRNML2ybaD7SVat0x2bUUB1UPEHF4N-3zEDp9KrXCJuY36PBbMq8DYMKJkImlHso1E_pshD_7HhQ8_y5bDDGmygDzCEWGJOqmsnYEw8mjNPOrPJ_bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اعطای گواهی درجه یک هنری به علیرضا داودنژاد با حضور خانواده او
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/461834" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461833">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بانک مرکزی سراغ ۱۱ رئیس شعبهٔ متخلف رفت
🔹
بانک مرکزی: در ادامهٔ بازرسی‌ها و  رصد تراکنش‌های مشکوک به پولشویی که منجر به اخلال در بازارهای پول ارز و فلزات گران‌بها می‌شوند ۱۱ بانک متخلف نیز جریمهٔ نقدی شدند.
🔹
با هدف ایجاد بستر لازم برای فعالیت‌های اقتصادی قانونی از همهٔ ابزارها برای انتظام‌بخشی به تراکنش‌های بانکی استفاده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/461833" target="_blank">📅 18:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461832">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار از تأسیسات عربستان سعودی در شهرهای خمیس مشیط و ابها خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/461832" target="_blank">📅 18:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461831">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b857003bf3.mp4?token=AhwDRi5nDuKqFJyy-4yGgkdxfO1Wh84L-KNedHaYuvZq0mIosoicrIemw4SHjleIUvbUYhdrwYjnvWW8b7o7O4dC9ABWlP8PW8Q97N3bb_WHR7ciiK0WJLMF0QA5cOhmnXHCR0kBVbhZUmUc237NzzhSLFaHRcHHBxr0XIXJncgbzXsXSmzXEPTNbSQF9wzHEHTUA1nMGzau-xTIz-EEA601mm6KDqZO25GwwECStj9v4IW9e5j28yIJACpRGnm6RoLkYsM0waXFcD5pls9znqYsHI2Izn3U3523eM4HoRCkAe_-kcxao6JnRTs_Bp23MueAcnAmblbx-ekfVstjkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b857003bf3.mp4?token=AhwDRi5nDuKqFJyy-4yGgkdxfO1Wh84L-KNedHaYuvZq0mIosoicrIemw4SHjleIUvbUYhdrwYjnvWW8b7o7O4dC9ABWlP8PW8Q97N3bb_WHR7ciiK0WJLMF0QA5cOhmnXHCR0kBVbhZUmUc237NzzhSLFaHRcHHBxr0XIXJncgbzXsXSmzXEPTNbSQF9wzHEHTUA1nMGzau-xTIz-EEA601mm6KDqZO25GwwECStj9v4IW9e5j28yIJACpRGnm6RoLkYsM0waXFcD5pls9znqYsHI2Izn3U3523eM4HoRCkAe_-kcxao6JnRTs_Bp23MueAcnAmblbx-ekfVstjkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش شبکهٔ ۳ از پیام مجاهدین یمنی از تنگۀ باب‌المندب به ملت ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/461831" target="_blank">📅 18:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461830">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار از تأسیسات عربستان سعودی در شهرهای خمیس مشیط و ابها خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/461830" target="_blank">📅 18:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461829">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0dcc3c402.mp4?token=hbQOUBnUr-OHQfmWIsLp4aQjbHiDbxMQ8jnwNSunv9MaEvcTPlzYTdQPzgRxtqhmAkfrNeQyMA4ek3WJ9QLVyiBf5lzRRaFSbzAEapb8rlBAFUSk-Zav7ru2vgo3WaeSF8JXrJmLchAevMryQM0roxEHU_5_QACTPMyX7U7b1_3cKBEXqeSuOW7agNlBoRizSaIXUCauNum0Dc2GKhfbfPS7CC_3PX64p6EKZMS82UplF4b4O6sSenIED_Z6svyJuAgWZpSy4ShryoIOrL9-_t7CFmwG67UpeOVT2l6tUzdAgZbUCv6DIS2-XdvTWuHLWkvEIC69aIPtAhlJzfeZhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0dcc3c402.mp4?token=hbQOUBnUr-OHQfmWIsLp4aQjbHiDbxMQ8jnwNSunv9MaEvcTPlzYTdQPzgRxtqhmAkfrNeQyMA4ek3WJ9QLVyiBf5lzRRaFSbzAEapb8rlBAFUSk-Zav7ru2vgo3WaeSF8JXrJmLchAevMryQM0roxEHU_5_QACTPMyX7U7b1_3cKBEXqeSuOW7agNlBoRizSaIXUCauNum0Dc2GKhfbfPS7CC_3PX64p6EKZMS82UplF4b4O6sSenIED_Z6svyJuAgWZpSy4ShryoIOrL9-_t7CFmwG67UpeOVT2l6tUzdAgZbUCv6DIS2-XdvTWuHLWkvEIC69aIPtAhlJzfeZhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهکارهای پلیس فتا برای جلوگیری از کپی شدن کارت بانکی توسط کلاهبرداران  @Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/461829" target="_blank">📅 18:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461828">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwfQEStntHf75IRGHzURrz-WzeJRhP_Iyqyv5oI4n6u4ZuWf6gmT74SUiH72yfeKIjH5AHaQPKtj_CHKd_VN59_HzKaGRvEacMj920YraDyd3L51It4cxtdD8Hm8Uki4hK6mDOf-BEGKi3pr1gdYKRMcdW5EJ9BptYIkCtk9pt_hcyUDCndifY-MZCiEx6voiKFTK7q2aIMt1W-XgVaaLOQ02mlgKs4v_V2ycebn8b5eWixAjoT_Bg_H6dj3Fri3B098G7dz6yjgJVrc8dO2ciC3LiJcalhqX8o1IkD6YSEy6q6ORkRshkJZxW4yUVWkTZBmFbhhmw-KnWa8rAva6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتمام تابستان در وزارت نیرو؛ مردم همچنان اسیر خاموشی
🔹
سخنگوی دولت دیروز در مراسمی کنار وزیر نیرو اعلام کرد: «با همدلی تابستان را پشت سر گذاشتیم».
🔹
این درحالی است که اسناد رسیده به‌دست خبرنگار فارس، خاموشی گستردهٔ برق خانگی در روز گذشته، یعنی هم‌زمان با برگزاری این مراسم را تایید می‌کند.
🔹
عباس علی‌آبادی از یک ماه پیش ۴ بار وعدهٔ پایان خاموشی‌ها را داده اما برق خانگی همچنان قطع می‌شود و صنایع از تشدید خاموشی‌ها خبر می‌دهند.
🔹
میزان خاموشی روز گذشته ۲.۵ برابر متوسط خاموشی در یک ماه گذشته بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/461828" target="_blank">📅 18:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461827">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGLNXow5lVFogruawinjfQ2Sc0cApiy-i40DgEWEFoBtrwE0LuLWz1ZGh39rHvtOu4tTCkpuQ0MMVTy1U4dPlvdBPvIQJM2ETapWUlnBOrXhfz7UGUfspMSnv3UlLcgbaQzly2DfReb1dt6WbvHhwVCd34t8PdgTyU3YOk8lvtfoe3peEEwsmJqxBAzlBHR0bQfagRFDyHondDYvu8v9eP70pbT_DUUOff1OaWwo5eVuKo_kAKpdYRZSsNkv9sySL4tJCZJ4vMrQ0LiQlRYVGCUot1jjgvjUTGTQ4aWWM_xt9aqX_oPG1A2_92O9e-IlOPEab-Sp7HMvkAlyZVnaEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلرژی پاییزی را اینگونه مهار کنید
🔹
اگر با شروع پاییز دچار عطسه‌های مکرر، خارش بینی و چشم، گلودرد یا سرفه خشک شده‌اید و احساس خستگی مزمن یا کاهش تمرکز دارید، احتمالاً به حساسیت پاییزی مبتلا شده‌اید.
🔹
این علائم که اغلب با سرماخوردگی اشتباه گرفته می‌شوند، نیازمند مدیریت دقیق و پیشگیری هوشمندانه هستند؛ برای اینکه پاییز امسال را بدون دردسر سپری کنید، ۴ راهکار ساده زیر را جدی بگیرید.
🔹
مدیریت محیط:
محیط خانه خود را از گرد و غبار پاک‌سازی کنید و در روزهای آلوده، پنجره‌ها را بسته نگه دارید.
🔹
حفاظت فردی:
هنگام خروج از منزل، حتماً از ماسک استفاده کنید تا تماس مستقیم با گرده‌ها و ذرات معلق کاهش یابد.
🔹
بهداشت فردی:
بلافاصله پس از بازگشت به خانه، دوش بگیرید و لباس‌های خود را تعویض کنید تا ذرات آلاینده به محیط زندگی‌تان منتقل نشود.
🔹
تغذیه:
مصرف مداوم آب و مایعات کافی را در برنامه روزانه خود بگنجانید تا مجاری تنفسی مرطوب بمانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/461827" target="_blank">📅 18:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461826">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuzB74gtOzc7cEnjB0O_O3gkoh7DZ4Aaeit4qiz6NQ58D9PIANGD0jzM-NW4XOTJQjG58MBvRNt9Eg617UGMIkC3wgsJUcRNY6xfGVFk0Xhva3wFGLLS2nwFj4JGT-EFS0lRjEU_qpez0AiQAvWaKb9Fgo1OFMO6NGMP6zAQcsW_d24kI3pmSqv9fa5Dbe5nVOCeMoDrkZrMSLyqwOHXcSzI5go_tFriEfQ4mGy_jazNxpEyFg0rIqRWUbLRL89nLWnqJSyHx8JunMT3UN1hqvZfcwiLqe5GTGCfrQ5HGPU3mo7JdMkJnWNOXLE7C-8OaZG4Av3gyEVi8EYVKG8U-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژۀ جدید پرسپولیس برای «پرسپولیس ب» کلید خورد
🔹
یکی از گزینه‌های مدنظر مدیران پرسپولیس برای راه‌اندازی تیم «پرسپولیس ب»، خرید سهام فولاد ب بود؛ تیمی که به تازگی جواز حضور در لیگ دستۀ اول را به دست آورده است. اما مذاکرات در نهایت به نتیجه نرسید و مدیرعامل…</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/461826" target="_blank">📅 18:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461824">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d22c8476.mp4?token=b4kCn7er0QYQHk8aINZc-8Qc6flMdqvGYXK-vlXoHv20vAbCgHwc8aw1CVw1GOlIAzR-7zQyeHvI3IyskFqYBWwytQEB7nXBdZ9enCwG8vbLcf_ogS6c2n8ZSNbhSg9MokXG9P-9zbqJ5RihahzE59XpbY_NeS8g6D5nfgpLYGyx1L2lloEvVw2L99i0m9wScfFZIQp6OmRL0VDE_u6by_3MEXB6bVSeZiAkisSTpxa6Jx1-hClWLG_Q51tLEX5j7I5oGTxauEX91Wwfa-OcDU3fTdifSZUOY24uhMvZPB4vmtCRUSg_uKYjhcZGuzw29voWJMiakfBWzM64SbDmNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d22c8476.mp4?token=b4kCn7er0QYQHk8aINZc-8Qc6flMdqvGYXK-vlXoHv20vAbCgHwc8aw1CVw1GOlIAzR-7zQyeHvI3IyskFqYBWwytQEB7nXBdZ9enCwG8vbLcf_ogS6c2n8ZSNbhSg9MokXG9P-9zbqJ5RihahzE59XpbY_NeS8g6D5nfgpLYGyx1L2lloEvVw2L99i0m9wScfFZIQp6OmRL0VDE_u6by_3MEXB6bVSeZiAkisSTpxa6Jx1-hClWLG_Q51tLEX5j7I5oGTxauEX91Wwfa-OcDU3fTdifSZUOY24uhMvZPB4vmtCRUSg_uKYjhcZGuzw29voWJMiakfBWzM64SbDmNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از شایعه تا واقعیت پابوسی پزشکیان از راهب هندی!
❌
به‌تارگی فیلمی به‌سرعت در رسانه‌های هند با عنوان «پابوسی رئیس‌جمهور ایران از راهب هندی» دست‌به‌دست شد.
✅
اما واقعیت این است که در جریان دیدار پزشکیان با برخی از مقامات و چهره‌های هند، رئیس‌جمهور کشورمان با یکی از رهبران معنوی هندو در حال گفت‌وگوکردن است که نامه‌ای از دست پزشکیان به زمین می‌افتد و او برای برداشتن نامه خم می‌شود.
🔎
برخی رسانه‌های هند با انتشار این فیلم از زاویه‌ای خاص مدعی شدند رئیس‌جمهور برای احترام به این راهب هندو خم شده تا پای او را ببوسد.
⚠️
منابع سفارت ایران نیز در واکنش به این شایعه گفتند که فیلم منتشر شده، از متن اصلی خود خارج شده و به شیوه‌ای گمراه‌کننده ارائه شده است.
@Fals_News
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/461824" target="_blank">📅 18:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461823">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffbed1e0a3.mp4?token=WfYD7-CJIQSvNCXOLquK83PkRzs9x1gbMNQDixYPMkeYMefsZZ6S0zV1BoO_WXhlQvs493Y8bzOAmQJiGUXKFCOlUcIibPpoA44XF6D-Zvnqgum7SR1tyoBF0IIxYJmneBbfHG7FADRKkeUdYtzX3So3-gJIQI_L7yTwP_oknwBqmtps7MN3VOD2F2B2hiymsoaamCGhBiwI0hf7rJZmiBaVLRUCTuxexEbp5AWvF41J4U4GbLTUXglF-EXOVJrEuebMviMg45ueSeumTCKpR8yt5KNkThJwsGBDLeK_DwphnqbPAoL6RdWNSpbp0zgQt9u-dv2-8spgH3qTrijUxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffbed1e0a3.mp4?token=WfYD7-CJIQSvNCXOLquK83PkRzs9x1gbMNQDixYPMkeYMefsZZ6S0zV1BoO_WXhlQvs493Y8bzOAmQJiGUXKFCOlUcIibPpoA44XF6D-Zvnqgum7SR1tyoBF0IIxYJmneBbfHG7FADRKkeUdYtzX3So3-gJIQI_L7yTwP_oknwBqmtps7MN3VOD2F2B2hiymsoaamCGhBiwI0hf7rJZmiBaVLRUCTuxexEbp5AWvF41J4U4GbLTUXglF-EXOVJrEuebMviMg45ueSeumTCKpR8yt5KNkThJwsGBDLeK_DwphnqbPAoL6RdWNSpbp0zgQt9u-dv2-8spgH3qTrijUxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: هر راننده فقط می‌توانند ۱۸۰ لیتر بنزین در کارت سوخت خود ذخیره کند.  @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/461823" target="_blank">📅 17:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461822">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i825F6Azq4BmoQy8AhAmYK4FDWMURl6EINUDpCxEzguWY_ksC6FLSnLAtvo4i-hbTYTAc9pnFsUo3NF1UhXRlmMGK97G1QkHTmZNq0pcOyxZBRmkXM6uTS-fFcBkosr7EnLuVrtoXGPPi68CZJJEerALdSgxCmqo3yMtqYNjVTQP-1B122lFEj1Z7b82v0ms6OzRDuCgzMIx_2gmramKAFzZkiblw0ZHcvbB5XDe-t4vX2WRVt-oqEMeuvqxjomLeyNgutVRdglZlbNP5kbgCBAk4tbaqFBSeKfFU_ywmKjK4zJX-o5LlZzR8OqBcj236x2kB6Y1kb3kuzsb36LoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه به محکوم‌کردن حمله به خط لوله عربستان اکتفا کرد
🔹
آنکارا که یکی از اعضای پیمان دفاعی مشترک مکه میان ترکیه، عربستان و پاکستان است، در واکنش به حملۀ پهپادی به خط لولۀ راهبردی شرق-غرب عربستان، به محکومیت دیپلماتیک این حمله بسنده و بر حمایت از حاکمیت و تمامیت…</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/461822" target="_blank">📅 17:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461819">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeWWs-6D-S7KneubYxZtgkLQ6MOB8z3WMDjknSwSQ3eIAENk-CIl3ghjMcLqsGr70HNxy9J3rhpKYN8Jlcc4mReZ_eXgL6hCgR_J4_8FimBMaEZldplIUXriHDxgCMCpo7yDHHA1DOMOZv75qqiphs7M4z8Nu8RJJs7wL2vzo7Li9UuHf9bDTCiIgUfjIAK6wy-wr00Wf_1iNlZQvJix2Nm5ELsYWOjTZi81-FV5SOgYZ_h1ZJ3QCmGES-fPSWbEcejHdgjm8u9ciISDsDCjA5s6IrzMzJ_C_n1JtN7k3ee2kIT1tfWEcGc7uUE5_K6iUWgXFy8176eXdBxxADZMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۱۷ تن طلای عربستان در آتش پهپادهای ناشناس سوخت
🔹
رویترز: در صورت از سرگرفته نشدن فعالیت خط لولهٔ انتقال نفت از شرق به غرب عربستان در روزهای آینده، ذخایر صادراتی عربستان در بندر ینبع تنها برای ۵ تا ۷ روز کافی خواهد بود و این وضعیت می‌تواند به از دست رفتن حدود ۴ درصد از عرضهٔ جهانی نفت منجر شود.
🔹
خط لولهٔ شرق به غرب که روزانه حدود ۴ میلیون بشکهٔ نفت را به ینبع منتقل می‌کند، طی ۶ ماه گذشته به عربستان کمک کرده بود تا از پیامدهای اختلال در تنگهٔ هرمز تا حدی در امان بماند.
🔹
قطع کامل صادرات و ضرر روزانه ۷۰۰ تا ۹۰۰ میلیون دلار (میانگین ۸۰۰ میلیون دلار)، عربستان در ۶ هفته (۴۲ روز) بین ۲۹.۴ تا ۳۷.۸ میلیارد دلار و به طور میانگین حدود ۳۳.۶ میلیارد دلار خسارت می‌بیند.
🔹
این مبلغ معادل ارزش دلاری ۵۱۷ تن طلا است؛ یعنی پهپاد ناشناس با توقف این خط لوله، به اندازهٔ ۵۱۷ تن طلا از جیب عربستان بیرون کشیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/461819" target="_blank">📅 17:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461818">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/674a05064a.mp4?token=EO3I_CfQ7Y8eHQZU2tNTLu8pV4mn-rAhfmGgx3mmESThTq0aCnlciqJCaTnS07chg0LGTfsTvFjZ1cf_lEY0ghI7lY2HqohCtDDjxQ-PzK_Qy8YNSASuaxzh_SQge6lHIQ6jxJ0TF5s_y8hJLbSJTnL1yjzeKq1ioJ3olX5GQt5QThYve5oqJT6MZV9gM173KcSbKfMMmK9RYW1h24I9mfVNd0SVKGNSxFjBS98MfPvJXLYxuPvm67O3hbQ9ivk4z6XHEiEZs-Op_cST-Aolz7gHpr_54r0XK4gZ7qG1sva50RKZCIGCZJ8XMG1FpTdO8Q3LyacHBq3tOjBmsSYpKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/674a05064a.mp4?token=EO3I_CfQ7Y8eHQZU2tNTLu8pV4mn-rAhfmGgx3mmESThTq0aCnlciqJCaTnS07chg0LGTfsTvFjZ1cf_lEY0ghI7lY2HqohCtDDjxQ-PzK_Qy8YNSASuaxzh_SQge6lHIQ6jxJ0TF5s_y8hJLbSJTnL1yjzeKq1ioJ3olX5GQt5QThYve5oqJT6MZV9gM173KcSbKfMMmK9RYW1h24I9mfVNd0SVKGNSxFjBS98MfPvJXLYxuPvm67O3hbQ9ivk4z6XHEiEZs-Op_cST-Aolz7gHpr_54r0XK4gZ7qG1sva50RKZCIGCZJ8XMG1FpTdO8Q3LyacHBq3tOjBmsSYpKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعات سرنوشت‌ساز برای بیرانوند در لیگ برتر
🔹
ساعت ۲۴ امشب پنجره نقل‌وانتقالات لیگ برتر کشورمان بسته می‌شود و تنها ابهام باقی‌مانده وضعیت علیرضا بیرانوند است که طبق قوانین از اول مهرماه سرباز می‌شود.
🔹
بااین‌حال کنکاش فارس نشان می‌دهد که بعید است بیرانوند از…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/461818" target="_blank">📅 17:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461817">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050035a39d.mp4?token=TPSlw8kZDY1rEkWCoUTk4ptmvS4rq4enZBJpjPuAi2tp_1GQiD4mVlCb4soPEuOsUq6Sds3rX-tNay2_Fr_a3HX63t06vUImzCtCw0_Yr9vZauCTPxwGWdA21kG0nQWyfc5dxtAUmIZaRbFwF3UFow9OrWM-QNABnH7jf5Aoz7BflLMCaOjbFDHluDTTss5oGE9BYZ9NKnOoJ0JLEs_zmCjEKaQu3kWwkEoVO5_GbD6A-StQEzzYK2HUeCNOiGjZlVtma7JYcLWoMXu11JR_wpi_0Pyy1ETApaR_s7I1a608y9fTXaEDdqHEuaYRIFc5XFGdIyMjiDb4ccfYKnyCsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050035a39d.mp4?token=TPSlw8kZDY1rEkWCoUTk4ptmvS4rq4enZBJpjPuAi2tp_1GQiD4mVlCb4soPEuOsUq6Sds3rX-tNay2_Fr_a3HX63t06vUImzCtCw0_Yr9vZauCTPxwGWdA21kG0nQWyfc5dxtAUmIZaRbFwF3UFow9OrWM-QNABnH7jf5Aoz7BflLMCaOjbFDHluDTTss5oGE9BYZ9NKnOoJ0JLEs_zmCjEKaQu3kWwkEoVO5_GbD6A-StQEzzYK2HUeCNOiGjZlVtma7JYcLWoMXu11JR_wpi_0Pyy1ETApaR_s7I1a608y9fTXaEDdqHEuaYRIFc5XFGdIyMjiDb4ccfYKnyCsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روش پرداخت کالابرگ ۱۴ سال به صورت یک‍جا به مردم
🔹
با مسکونی کردن فقط یک درصد از مساحت ایران، به هر ایرانی ۲۰۰ مترمربع زمین می‌رسد. با توجه به متوسط قیمت زمین در کشور، ارزش این زمین می‌تواند برای هر نفر به بیش از ۲ میلیارد تومان برسد. این رقم به اندازه ارزش…</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/461817" target="_blank">📅 17:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461816">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حملۀ عناصر داعش به ارتش عراق در کرکوک
🔹
برخی منابع خبری گزارش دادند تروریست‌های داعش به یک مقر ارتش عراق در استان کرکوک حمله کردند.
🔸
هنوز ارتش عراق به صورت رسمی این حمله را تأیید نکرده است. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461816" target="_blank">📅 17:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461814">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKCh3HO_Ax4HAFzVNrmzQnAUQU73ZkljjYw4lqe_S7vx0LcOCVyczokDXYypOCCBSZ8RZE6nijdc-WAhlGisilTnSYYckvTojqT67YhD78HT2VF3tk5SNOAeJUWqSf6PSIclIrk6ESH-28jBUtkMgu8ZSqzMlmPJRwtT2yq2OC4o29_YATnLppZ6VRd_Pmo-FnGc-2z_eAi3xLuABsyjFxmAxGbd0OKjjypR-pLqY4Qfb4w1jX_0wlds9hs-GJff-GerFu6tFj3vsgTnhGHZCBab30PZFFxUCGP6lzWKV54EZaKeGqc069DxLjlUHkpaPW-Zt0YLLNJUEII3Vqxy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی و عبدالعاطی وزیر خارجۀ مصر در حاشیۀ اجلاس سران بریکس در دهلی‌نو گفت‌وگو کردند.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461814" target="_blank">📅 17:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461813">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566cf6be2d.mp4?token=ucV0eYxVmT7EvASNVJ2rn2PBXhjDwmTTmK36UA39dZb2YJ9MSh9DsafHPsnodHmCJ9z_nEWGluJ7yjSRTBN_XdmwCbJ10G8czDhgxSGwhSluUlh2Rpob99-Vm7js-K9wQCSCXiVTXPVtBarOakoYFnKVBqsZ_bgKMdrd0Auh_mUs4aR-j1wYljJWEWRbb2EcYN3CMfWEw9QLsuOz31Mn1eH522MPwpY09sGN7ZiB0lwFha8H2vGT3g1VmiyYoKjp_uia-8Yh-gGhN7IRCGPL5i5-2zPB1Z_DhMvDDObOtHkF0LpSFGIx-ukRGsOQ48nry3drPutMCHcTjZxE7DX6dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566cf6be2d.mp4?token=ucV0eYxVmT7EvASNVJ2rn2PBXhjDwmTTmK36UA39dZb2YJ9MSh9DsafHPsnodHmCJ9z_nEWGluJ7yjSRTBN_XdmwCbJ10G8czDhgxSGwhSluUlh2Rpob99-Vm7js-K9wQCSCXiVTXPVtBarOakoYFnKVBqsZ_bgKMdrd0Auh_mUs4aR-j1wYljJWEWRbb2EcYN3CMfWEw9QLsuOz31Mn1eH522MPwpY09sGN7ZiB0lwFha8H2vGT3g1VmiyYoKjp_uia-8Yh-gGhN7IRCGPL5i5-2zPB1Z_DhMvDDObOtHkF0LpSFGIx-ukRGsOQ48nry3drPutMCHcTjZxE7DX6dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمین یک خودرو را در نیشابور بلعید
🔹
درپی فرونشست زمین در خیابان فردوسی شمالی نیشابور، یک خودرو در زمین فرو رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461813" target="_blank">📅 16:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461812">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a141234c8f.mp4?token=D5dIkQorr4OxHNLYnDAmQyCetRcRbyipB56NCHwslWoY2kKqSx2N01qxHwYV2ic2ChcUvk_rYXy_zmUzV4_whuJ09xeUef8QZsskIcoKMrwpKR-VrWowH62AKJGAn54c7VnClqKbSfOmB28eimIaVu3e5nRpSE4V4pnR0pl-yMkir5xCuIY0k0dHJdhmf37auCSWwJkuhMbUCXWaSLnXxZ9OGq90qzistWmzD-305QGvF5_Eurkf873E2B0z_3i7OyrGgvdxyd246fLQqnM7-oCzej2XjD8BJh7eixcHhKQObVTGdTSmKLi91oDmrhqmgkK1ErBqfje3zSo0AjYQSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a141234c8f.mp4?token=D5dIkQorr4OxHNLYnDAmQyCetRcRbyipB56NCHwslWoY2kKqSx2N01qxHwYV2ic2ChcUvk_rYXy_zmUzV4_whuJ09xeUef8QZsskIcoKMrwpKR-VrWowH62AKJGAn54c7VnClqKbSfOmB28eimIaVu3e5nRpSE4V4pnR0pl-yMkir5xCuIY0k0dHJdhmf37auCSWwJkuhMbUCXWaSLnXxZ9OGq90qzistWmzD-305QGvF5_Eurkf873E2B0z_3i7OyrGgvdxyd246fLQqnM7-oCzej2XjD8BJh7eixcHhKQObVTGdTSmKLi91oDmrhqmgkK1ErBqfje3zSo0AjYQSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دمنوش واقعا سردرد را درمان می‌کند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/461812" target="_blank">📅 16:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461811">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1769cb0441.mp4?token=PSG0064ZLgj2CTNdQsbgtGbqM6ynyOb8bnWcsi01jgAJMFFcotFMcwldGVztMYnGalw8dGdMesb3AiPij4S3OMru3hP8iqaRdSsx6yCrK6CsG4UY9wnu4vPk7MradwFBfUy0hk4RKlZejAAz2MZNwETLT4FngTZBtwH3Ipu0peM3573LfJ8G-b4ogKmZ6mRQfctIOPzWfsd3p3nFRBndE_7eqwNuYJbU8JeTrxLgl7yiqFH-dZswKwx455hZsRcxcVirA0G-HnoVsV-nl3QfCLGykBfeJV-fsxXQTvN2BThsPc9wwTWwXE2JDiyJcskuwy4EGKZ5JnnkGtUdCLlpKCfmgSVSsIY6Wci2fUBSnkSDEAZfEtWkXkvAZyxVOZ3j-Xe3KWCpkvADfjFLrc46T2IFXnRTa3XZqZgJlx2RykCVMKYuT8d4vj4f8Df0MOvo9-A7roSsh67toHJq9e1d-4B1Yqhluz4to_CT3p0Nx5rGxwu7Hl1TIa4S9N9SqGyy4duBgNrzfTwSmQ6DVIK3ljTSqOZMHnjrvAIb0yvx9cWTYiRN_6H5YTyWsxmTj-NeaOfVb_zjvAK28_MO1TnACaitPtzafG14bUYPovrWzKIBd74xy9bbfHz9lM1lqz4Ftj9XeWIb-mT7SHBM7R4FVRivHYJsZ1EYFwO8459GN3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1769cb0441.mp4?token=PSG0064ZLgj2CTNdQsbgtGbqM6ynyOb8bnWcsi01jgAJMFFcotFMcwldGVztMYnGalw8dGdMesb3AiPij4S3OMru3hP8iqaRdSsx6yCrK6CsG4UY9wnu4vPk7MradwFBfUy0hk4RKlZejAAz2MZNwETLT4FngTZBtwH3Ipu0peM3573LfJ8G-b4ogKmZ6mRQfctIOPzWfsd3p3nFRBndE_7eqwNuYJbU8JeTrxLgl7yiqFH-dZswKwx455hZsRcxcVirA0G-HnoVsV-nl3QfCLGykBfeJV-fsxXQTvN2BThsPc9wwTWwXE2JDiyJcskuwy4EGKZ5JnnkGtUdCLlpKCfmgSVSsIY6Wci2fUBSnkSDEAZfEtWkXkvAZyxVOZ3j-Xe3KWCpkvADfjFLrc46T2IFXnRTa3XZqZgJlx2RykCVMKYuT8d4vj4f8Df0MOvo9-A7roSsh67toHJq9e1d-4B1Yqhluz4to_CT3p0Nx5rGxwu7Hl1TIa4S9N9SqGyy4duBgNrzfTwSmQ6DVIK3ljTSqOZMHnjrvAIb0yvx9cWTYiRN_6H5YTyWsxmTj-NeaOfVb_zjvAK28_MO1TnACaitPtzafG14bUYPovrWzKIBd74xy9bbfHz9lM1lqz4Ftj9XeWIb-mT7SHBM7R4FVRivHYJsZ1EYFwO8459GN3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
رکورد افزایش تولید هلدینگ خلیج‌فارس در سال وقوع دو جنگ تحمیلی
🔹
شرکت صنایع پتروشیمی خلیج فارس در سال وقوع ۲ جنگ تحمیلی توانست با وجود ۲ ماه توقف تولید به علت شرایط جنگی، تولید محصولات خود را نسبت به سال ۱۴۰۳ افزایش دهد و به ۲۷ میلیون و ۳۰۰ هزار تن برساند.</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/461811" target="_blank">📅 16:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461810">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش ویدئویی از نشست خبری خانه سینما برای گرامیداشت هفته و روز سینما با حمایت شرکت بیمه دی
این نشست دیروز شنبه ۲۱ شهریور ماه در آمفی تئاتر خانه سینما با حضور اصحاب رسانه برگزار شد.</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/461810" target="_blank">📅 16:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461809">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/461809" target="_blank">📅 16:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461808">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3652bab1.mp4?token=l9_iy6fWTZyqepzhUcpMEM6HXMlIehZkLqbX23WhXBJoY6K5dzPO-zgZydrXEzyoujRLbetby-qkJhBM3Hz6OJOzXJn19s3McRSd2yGeTTjnKhUfCq2Eof6ljbQngVoiw9sgGuTKM1oBdmCVI5UQwWl6iek2v0ZOuWqeHj4JB63jkZuCJvtY_4Jx_LlMzvZfLwCiT8nf7bsEVDgC4RZS-L7CLjKd2QnqCRAIkE7f5vl352M72mDYlST0BOxuH7oPp_mBsr0a4wpisPYKYQph4_-dbx4E3stu3Wy4tCgjt2n4uuObdbH_x3q_APXegqWx9noqlXzMs3f0ZGZ-1D_xKluZcCMBIPtUfF7sWdriKpd2GreLUTPWvIKbRPJexaxJszUoS4wsPIGiaKvOf59mYovC4UXPS398439M-OJJvHlfaycjriWB1rRTBU45M2zFmNO9oKJKhrQb7lQlnWjqt06zlEaw3TdXZbnaED_gX98JOx9Bd1pkoT8wpx2wijh8xpIlMQfkZpTkRdn-ixOfodTbQGQY5cUQFU8VLA8CnwVnwFiBeE7yUpArJe4GZPW4IX_rfMJi3ixrKAwx7oT9itF99SgsbytZHli478l6lQte19O4WMMkn6BLFfWIWpBxhELMA7tyooC5K9i2QBs8LnO7X0IaIV5wgRHCYFr183o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3652bab1.mp4?token=l9_iy6fWTZyqepzhUcpMEM6HXMlIehZkLqbX23WhXBJoY6K5dzPO-zgZydrXEzyoujRLbetby-qkJhBM3Hz6OJOzXJn19s3McRSd2yGeTTjnKhUfCq2Eof6ljbQngVoiw9sgGuTKM1oBdmCVI5UQwWl6iek2v0ZOuWqeHj4JB63jkZuCJvtY_4Jx_LlMzvZfLwCiT8nf7bsEVDgC4RZS-L7CLjKd2QnqCRAIkE7f5vl352M72mDYlST0BOxuH7oPp_mBsr0a4wpisPYKYQph4_-dbx4E3stu3Wy4tCgjt2n4uuObdbH_x3q_APXegqWx9noqlXzMs3f0ZGZ-1D_xKluZcCMBIPtUfF7sWdriKpd2GreLUTPWvIKbRPJexaxJszUoS4wsPIGiaKvOf59mYovC4UXPS398439M-OJJvHlfaycjriWB1rRTBU45M2zFmNO9oKJKhrQb7lQlnWjqt06zlEaw3TdXZbnaED_gX98JOx9Bd1pkoT8wpx2wijh8xpIlMQfkZpTkRdn-ixOfodTbQGQY5cUQFU8VLA8CnwVnwFiBeE7yUpArJe4GZPW4IX_rfMJi3ixrKAwx7oT9itF99SgsbytZHli478l6lQte19O4WMMkn6BLFfWIWpBxhELMA7tyooC5K9i2QBs8LnO7X0IaIV5wgRHCYFr183o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: وقتی کسی را می‌بینم که با افتخار پرچم ایران را دست گرفته، آدم از شدت محبت دوست دارد گریه کند
🔹
این تجمعات شبانه فضای اجتماعی دیگری ساخته؛ آدم خوبی‌های مردم و محبت به دین، انقلاب و ایران را می‌بیند.
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/461808" target="_blank">📅 16:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461807">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca59819cb8.mp4?token=INwqJjOUonq6NKV6eYbg2lGLPjNeD6HfXjAtOjY4BKF7mJmeX3T3FfCzHV_ICAXKt-SIHOsN1Mj-_T9fmXTigjPFhtd7efuU2i6TtbHJ2UTQuPOIjKAjYOxXJm6Vtgz-4hCC1ae7ki4WwyCVvGnAU-681i-J2Kc2r7YG_9mfAorjQEwDOqdEjKNHa9p_FvuttW6rliAAvytYiieLicw-sOL9mH32hoiOyzpzKlJzTIvuK4kOfytrDMa0ZoyTCfhoA7SwaAbBDVgD5WNUo5ikeLdCezI_AP2MgV08jr8ssfSemwWPME33to9THzINoyzqJ0IlEIsQTIMzX2ltLdXTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca59819cb8.mp4?token=INwqJjOUonq6NKV6eYbg2lGLPjNeD6HfXjAtOjY4BKF7mJmeX3T3FfCzHV_ICAXKt-SIHOsN1Mj-_T9fmXTigjPFhtd7efuU2i6TtbHJ2UTQuPOIjKAjYOxXJm6Vtgz-4hCC1ae7ki4WwyCVvGnAU-681i-J2Kc2r7YG_9mfAorjQEwDOqdEjKNHa9p_FvuttW6rliAAvytYiieLicw-sOL9mH32hoiOyzpzKlJzTIvuK4kOfytrDMa0ZoyTCfhoA7SwaAbBDVgD5WNUo5ikeLdCezI_AP2MgV08jr8ssfSemwWPME33to9THzINoyzqJ0IlEIsQTIMzX2ltLdXTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وام بانک‌ها کجا رفته؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/461807" target="_blank">📅 16:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461806">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0268d7e623.mp4?token=qu1zEalR8v74cuKjWHI5IKHNjXHIh1E5MegdMt8OWLDmXRkCYeW1CBPzZ32x2VGcp4gL7WjPDrSIYGuSE23Q6y4pqnZk6JX0EELIgmoKVMoFrfugIbpaZTwajKA7oHTVrF-33z-q7atNbMDPj9Y3naH5N8BBWMX5twAQ5ctAfo0Xhti_Xxg8du5qdakjs89Tfeudi6YYGrt6tMa5Mm7NFcxeyTD3dk9TpIDY2GNRwzEWVHkYMmsTbSzQiYkLnvRLeWdEVCFRTy9i_Fx3NnQm9Bmpla3RnUvsbFLG0o1IVvmTcJUh9HZPN9GLFlk3aPJ-sM7SOtbKseAYV7nIHbXK4UuHl2dh8aT-7ERRH3fn4LA-ld5_aL31uASVH0GfUZZ-lcWPlVwY1vGuFwubs5DFEKZ2z-XIOKebLtTIZS0vcnWep3vxn9cicxarPpFEhcMxQX9Y-U7bNCq-OXihUzFnTq5ACHjwhouhuO8uA0gEGJJy8KC4PhcVKucYGOaclOCOWMFlXnu4qY785x3WfbNBJ3AhQ2JLtU-sMMBy4BSEWbc9pW2YxONmcNKjcoL9UaG2TYgg5SSoENzhUzZp59DPbuhEhZsVn12qFuEVkdPAQBvr7qfwUDDaXN2Jnhu1h3oD_e7Xcn759PxkzG6ZFGSkN0DSjH3uBDqtoJ6Mg-pzCR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0268d7e623.mp4?token=qu1zEalR8v74cuKjWHI5IKHNjXHIh1E5MegdMt8OWLDmXRkCYeW1CBPzZ32x2VGcp4gL7WjPDrSIYGuSE23Q6y4pqnZk6JX0EELIgmoKVMoFrfugIbpaZTwajKA7oHTVrF-33z-q7atNbMDPj9Y3naH5N8BBWMX5twAQ5ctAfo0Xhti_Xxg8du5qdakjs89Tfeudi6YYGrt6tMa5Mm7NFcxeyTD3dk9TpIDY2GNRwzEWVHkYMmsTbSzQiYkLnvRLeWdEVCFRTy9i_Fx3NnQm9Bmpla3RnUvsbFLG0o1IVvmTcJUh9HZPN9GLFlk3aPJ-sM7SOtbKseAYV7nIHbXK4UuHl2dh8aT-7ERRH3fn4LA-ld5_aL31uASVH0GfUZZ-lcWPlVwY1vGuFwubs5DFEKZ2z-XIOKebLtTIZS0vcnWep3vxn9cicxarPpFEhcMxQX9Y-U7bNCq-OXihUzFnTq5ACHjwhouhuO8uA0gEGJJy8KC4PhcVKucYGOaclOCOWMFlXnu4qY785x3WfbNBJ3AhQ2JLtU-sMMBy4BSEWbc9pW2YxONmcNKjcoL9UaG2TYgg5SSoENzhUzZp59DPbuhEhZsVn12qFuEVkdPAQBvr7qfwUDDaXN2Jnhu1h3oD_e7Xcn759PxkzG6ZFGSkN0DSjH3uBDqtoJ6Mg-pzCR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهکار سفیر سابق ایران در مالزی برای دور زدن محاصرۀ اقتصادی
🔹
زاهدی، سفیر سابق ایران در مالزی: محاصرۀ اقتصادی ایران در غرب،  «پروپاگاندا و هیاهویی بزرگ» است و اجرای چنین طرحی عملاً امکان‌پذیر نیست؛ چراکه کشورهایی مانند چین و روسیه با آن همراهی نمی‌کنند.
🔹
دولت باید با استفاده از مسیرهای جایگزین، به‌ویژه فعال‌کردن ظرفیت سفارتخانه‌ها، تأمین کالاهای اساسی و دورزدن تحریم‌ها را دنبال کند؛ حتی اگر این مسیر هزینه بیشتری داشته باشد.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/461806" target="_blank">📅 16:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461805">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آموزش و سازماندهی ۱۰۰۰ گردان جان‌فدا آغاز می‌شود
🔹
اطلاعیهٔ شماره یک قرارگاه مردمی جان فدای ایران: پس‌از شکل‌گیری ظرفیت عظیم پویش جان‌فدا که تحسین دوست و تحیر دشمن را رقم زد و با توجه به استقبال بی نظیر و پیگیری مدام مردم برای قرارگرفتن در کنار نیروهای مسلح برای دفاع از دین و میهن هماهنگی‌های لازم با نیروهای مسلح کشور انجام شد و مقدمات مورد نیاز برای آموزش و سازماندهی ۱۰۰۰ گردان مقاومت ملی جان‌فدا فراهم گردید.
🔹
در همین راستا از همهٔ علاقه‌مندان دعوت می‌شود در روز سه‌شنبه ۲۴ شهریور از ساعت ۱۷ با مراجعه به سامانهٔ
janfadaa.ir
یا ارسال عدد ۱ به سرشمارهٔ ۳۰۰۰۱۱۵۵ در دوره‌های آموزش نظامی و امدادی جان‌فدا ثبت‌نام کنند و در قالب گردان‌های مردمی جان‌فدا سازماندهی شوند.
🔹
فعالیت‌ها و اقدامات جان‌فدایان برای ایران آینده به‌زودی در سایر حوزه‌های مورد نیاز دفاع از کشور اعلام می گردد.
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/461805" target="_blank">📅 16:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461804">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6383cf15.mp4?token=fIsZANHuaOSXiX2L1z6lvXXF-HxR7xUQ33pmr6dt3eI6lbet7vk4VEX3TBdZ4OTjIlyqH-0uSztLPDYRUiXOKs2yl7E94y2FMGKd2In1RMJOwGmyOAUK3vY1mUoZZXPcQDIz-55bUbjfQsUFD1v-tn7NREoyjaBzDwyTXwobHbNZjPGAkc-Y5nSNXo1wrHC8HDw1w54BYXFSXJ1VIirz4zh5rQtc9M8vA6dO7Z0J1piTx5o5BvZrPhRffWn0VxQ0xFVy9cF2y-e3Rs_3UdXF4voD3ElPq-P892_cpW3aqR96ZLhFnjIX3n67OkIbn5JFqJLmdWy9_5MN8oljvq0O3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6383cf15.mp4?token=fIsZANHuaOSXiX2L1z6lvXXF-HxR7xUQ33pmr6dt3eI6lbet7vk4VEX3TBdZ4OTjIlyqH-0uSztLPDYRUiXOKs2yl7E94y2FMGKd2In1RMJOwGmyOAUK3vY1mUoZZXPcQDIz-55bUbjfQsUFD1v-tn7NREoyjaBzDwyTXwobHbNZjPGAkc-Y5nSNXo1wrHC8HDw1w54BYXFSXJ1VIirz4zh5rQtc9M8vA6dO7Z0J1piTx5o5BvZrPhRffWn0VxQ0xFVy9cF2y-e3Rs_3UdXF4voD3ElPq-P892_cpW3aqR96ZLhFnjIX3n67OkIbn5JFqJLmdWy9_5MN8oljvq0O3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمن چه بلایی بر سر پیمان مکه آورد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/461804" target="_blank">📅 16:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461803">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd4f2aa47.mp4?token=Yrh3cvlQnPsSNq4owO81ObQiOESr_4whTV-L08HgIuReI-MnPUWTYlZnFrNT6YGhUQ2orYSAbAG2_TB_hQcuDl63IWrFEKRDGMs6oKTJpp0N5t4yKSYZAOFCEhf1n3TNb8Ds8fLFvHGF8Ba3NWwaCXxoP_jjX0IkUK3kT1i649Iqp2r-ERRgW8w9o-nkl3Fcj28xbNeXGK18SAjqRi-pfGjzWyF7r28hAXSiWS_RiRDkK7MlULhu3uDyn0rzRcBdDK8LjpWTK3g3jL3JQZqgmOdL6QMFGFYLR7Hf9R5PlU7WuOUdJzai5_oUrgTn_AqTIizT_jZhPRp8IQpEKdZMhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd4f2aa47.mp4?token=Yrh3cvlQnPsSNq4owO81ObQiOESr_4whTV-L08HgIuReI-MnPUWTYlZnFrNT6YGhUQ2orYSAbAG2_TB_hQcuDl63IWrFEKRDGMs6oKTJpp0N5t4yKSYZAOFCEhf1n3TNb8Ds8fLFvHGF8Ba3NWwaCXxoP_jjX0IkUK3kT1i649Iqp2r-ERRgW8w9o-nkl3Fcj28xbNeXGK18SAjqRi-pfGjzWyF7r28hAXSiWS_RiRDkK7MlULhu3uDyn0rzRcBdDK8LjpWTK3g3jL3JQZqgmOdL6QMFGFYLR7Hf9R5PlU7WuOUdJzai5_oUrgTn_AqTIizT_jZhPRp8IQpEKdZMhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: گفت‌وگوهای سازنده با بانک توسعۀ بریکس داشتیم
🔹
چشم‌انداز بسیار خوبی جهت سرمایه‌گذاری، تبادلات مالی و ارتباطات اقتصادی شکل می‌گیرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/461803" target="_blank">📅 16:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461802">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سرپرست وزارت دفاع: اگر جنگ دیگری شکل بگیرد ایران از نظر فناورانه بسیار قدرتمندتر و  پیشرفته‌تر عمل خواهد کرد
🔹
سردار ابن‌الرضا: با اطمینان بسیار بالایی می‌گویم اگر امروز جنگ دیگری شکل بگیرد، جمهوری اسلامی ایران از نظر فناورانه بسیار قدرتمند تر و  پیشرفته‌تر…</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/461802" target="_blank">📅 16:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461801">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2e69e07ee.mp4?token=FnMiFW1oAN4YCFGjtaYg59K4jR3N6c6L9aTZJFi5aeqEfUVmK54uu-N_heGPonGR4opcyjW7jtnD0lD7laBv68OkcTovpE5z0_9UR7piHnCDAcH7wSEQURXneh0uRqLzU46sxWDCOfGtWHT3svicdC1NcE1bFq8w-iBPbyf96Bg4H0-fqp72yASQFvLaeHZtx-rtyQfUkXwNoquBWH1t0F6qQ7nF9R2YVPOGiCNMOvO-ze3wh3t0dPCpcCs2pPrNBj_VjIdJr9WLkg51v4cEmgHEpfvo7dMQvdIVibqGPGFuiuKWdVoGF_xbOHZ0WXgidUNQez992rPlbC_Dmc4ynQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2e69e07ee.mp4?token=FnMiFW1oAN4YCFGjtaYg59K4jR3N6c6L9aTZJFi5aeqEfUVmK54uu-N_heGPonGR4opcyjW7jtnD0lD7laBv68OkcTovpE5z0_9UR7piHnCDAcH7wSEQURXneh0uRqLzU46sxWDCOfGtWHT3svicdC1NcE1bFq8w-iBPbyf96Bg4H0-fqp72yASQFvLaeHZtx-rtyQfUkXwNoquBWH1t0F6qQ7nF9R2YVPOGiCNMOvO-ze3wh3t0dPCpcCs2pPrNBj_VjIdJr9WLkg51v4cEmgHEpfvo7dMQvdIVibqGPGFuiuKWdVoGF_xbOHZ0WXgidUNQez992rPlbC_Dmc4ynQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: حمله به تاسیسات هسته‌ای و زیرساخت‌های ایران در بیانیۀ نشست بریکس محکوم شد
🔹
در بیانیۀ بریکس تجارت با ارزهای ملی یکی از عناوینی بود که تاکید شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/461801" target="_blank">📅 16:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461800">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e9b2c37b8.mp4?token=twgAb1tb71_-gcYiHGusE6M7ssQ-Z-3GG5bCDPtrfd6EepNAHvBwhCk74SAHBVtagl6H52WEW1hzjSUBAJUw13GvIzQ4egj233FJedmS3TUCW0M9JO9JEXLrppejX8xZDFXgljouno0FrTAb4mEWWIO4aFSMxFfJlujyG_ilWe_VzsMeVmshTu74JdxQ2YVTFL52apfUePMrGOUGVBz0Y_p9aUx7PNj4zvvoh5IY4FDEp9E0sxSpzNNgNwi6UNs13RZ5piRlRLwCalw9OLQ5JaPi2RfKyFyHWqVlc5NPaY9kUJVm4A-R8frr2B52n30soNnLPR5OMFjpbHjn0fbtvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e9b2c37b8.mp4?token=twgAb1tb71_-gcYiHGusE6M7ssQ-Z-3GG5bCDPtrfd6EepNAHvBwhCk74SAHBVtagl6H52WEW1hzjSUBAJUw13GvIzQ4egj233FJedmS3TUCW0M9JO9JEXLrppejX8xZDFXgljouno0FrTAb4mEWWIO4aFSMxFfJlujyG_ilWe_VzsMeVmshTu74JdxQ2YVTFL52apfUePMrGOUGVBz0Y_p9aUx7PNj4zvvoh5IY4FDEp9E0sxSpzNNgNwi6UNs13RZ5piRlRLwCalw9OLQ5JaPi2RfKyFyHWqVlc5NPaY9kUJVm4A-R8frr2B52n30soNnLPR5OMFjpbHjn0fbtvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: هر راننده فقط می‌توانند ۱۸۰ لیتر بنزین در کارت سوخت خود ذخیره کند.  @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/461800" target="_blank">📅 16:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461799">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnDqYl9a4Vw6XS2QTSo7Biwv2-WvRsUrFqbDbSA8hrA-26MRVE6Afmx9UTD69GynukLz9qEfNtRa1NbjyvNeR0UJXYroklINDAdDU-XtZv2RhRCycia8z7hOpaGMnsAmB2tqUmJmjItsK6I46u_wNQaApF99SZgPf7kVmZOdgV12dAXZPWdEOFCILto3rU_q-r5ZPrCZ5iH4vvKYV9IpmlHtEW017PwkG8ac40cXZihNHpiA3GVbYFYIGX97jZFfZK-JKhS01A9AguGlDeZFwvrkF5Uazxp385GfjFwzbPWcouyWYkTUtL5FvIirEKAtufBBAUi3ipFpb2pshVRc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: اگر جنگ دیگری شکل بگیرد ایران از نظر فناورانه بسیار قدرتمندتر و  پیشرفته‌تر عمل خواهد کرد
🔹
سردار ابن‌الرضا: با اطمینان بسیار بالایی می‌گویم اگر امروز جنگ دیگری شکل بگیرد، جمهوری اسلامی ایران از نظر فناورانه بسیار قدرتمند تر و  پیشرفته‌تر از جنگ‌های قبلی عمل خواهد کرد.
🔹
کسانی که تلاش می‌کنند استمرار فعالیت های فناورانه و خطوط تولید و کارخانه‌های تسلیحاتی کشور را صرفاً یک روایت یا تیتر  رسانه‌ای جلوه دهند در میدان به خوبی توان نیروهای مسلح ما را  دیدند انچه بعضا به نمایش گذاشته می شود بخش کوچک از توانمندی واقعی و ظرفیت‌های موجود در صنعت دفاعی کشور است و این مسیر همچنان با قدرت ادامه دارد.
🔹
امروز ایران قوی‌تر ، متحد تر و بیدارتر از هر دورۀ تاریخی خودش است؛ توانمندی‌های دفاعی و فناورانه کشورهای نیز متناسب با تجربه‌ها و آموخته‌های حاصل از میدان، مسیر پیشرفت و ارتقا را طی کرده است.
🔹
آمادگی کامل برای مقابله با تهدیدات وجود دارد و این آمادگی کاملاً از جنس توانمندی‌ها و راهبردهای مستقل خودمان است؛ جمهوری اسلامی ایران برای تأمین امنیت و دفاع از منافع خود، متکی به اراده، توانمندی و ظرفیت‌های بومی خود است.
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/461799" target="_blank">📅 16:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461792">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ga8Y51pBwrA9WQNNYraGLXwmmgPM35VIOx1LzP1tmcj9Oxnl--s7U_nSV-Mbauf3VvqFCYUVe7M1svJOjBB_zolTT93DXZGzUvg9C0-dCHMv7ROLZk2P-JKyoWHvdcN2JAGeoC3fzgaLlH6VKBQJPgHOV7VRSGzzBJwlkypPMilfj19v6HU8ulfvmveScLxTzBWD0cbUIbwb9wwOsMBDXb_lklvme9jGu9RgQT9aDsHQGJ6TQphPKKj8STrl9S9ks6AQIsAy8ekieKPOZhq-W9QtVDpybR1V69CW0oXmzvC-vI-WM78ahIwHR3qA8qEXIrAAoH5s2-5LPNKn_3xduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhW9a-3wjttNOUf92d57hs5s86FypwQOgLIn1Z46G0TcPGry3KViWncmR6gsBleVeIW99X_Bxy1xKd4hy4k3wpymiqL_Q3W_Q3sv_tgS8IlibaRymT_HWCQ7uVbebieZNN9F3uWsjX6OHrCl1NytSpG5l2ViLlwAundswWevhPzOVn6yhNr9XRe6WHPQtYWxepvsTjCzfUpPXL40HvRa6_oylWIc9vYbOhzWeREj1I5bdkzJpT0AhTSSTKyW2punY9S5WfVLyHjffFZT9ZW9njHsISgXIpCtyj3FI84tmBsthmlx0N4v9VMotwlz6VahV060RXATN0ecDHHq9VCfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQdbi7i55gkiOyoC6am4ekwNm6AY7IYMN-dnshO9qwtVe5JtHq5x9PosOK-I2BoF9EQGhAf6qSxworYfHTB2GKlIOosjNjD5vIJXW1DnpwR_OkREYN_kPCwyXPz1QvIFUexJYcAHfn0NoTQ6LAEjK6lwqE5a1HSBqJlI6BI_D6MK-mholjP7aZwsiXcdMRSgvi2oZeUZmZMghP7iyKb21hRwe8gqZSmYmfvMOb-AzuHmcGMgKWhnw-4aPT9ZMpxROkvEj-rVkVBdZD3qEwn0Kzq6WdD0hEB0xg8-55Veq-YCDg58Y3Z_r9GYVKk5G-xmRdaTmgiBhlp3jVPqzP5opQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3gLoTD0LazPlS4dWxEqp4NpyVxHCXaElVP4oW7dtr1ZKf80XRGRnH7M56Ngls9HGVILa-d7s8rR31-MygofJKlLph_e_lUyeSi8dfXPs5bbRI2H28bq63UAFt_vhbN8Ko_bxeI1Et6WAruZQY71sw30a6kp1peP8IAaONm9tGgJo4x8UKnlRZ-3HAfJBkcjBG-yY4J7gdQFXOFPrGqa_Ix80lmEe90qvWYsURb846oAnU8R2GQ_J5IVfN0A1GuMi3iSNQDKhEj557GFgzX04d652OKQtKLWA7JtUMNuFNqJYkrZIhNwmFCnglB5fd8f8E4vtAzQvVeTbKcooYUDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRN56udsJy265w78BNZiZOuJavHdCz8Jg5gTyf3vVLesuCaHtmF0m6q3R7kYKL7rxnPdFa79jZvXIxKuoBTTXLIsTR1MB__3CeYnJoiuOCB1BQy1dTVipQax1eLWMpJaOTTXm4bhyA5KSEx8sr2xeCaS7BaLRvooFFHG7Hj57j0YW2sVVuCLcbgdQXHiCQnfPrWv3SXYh7B3aQT7MlVbnwDjclz4xkWwUzYeaYtsasLUehp_WL6GcKWxjMnQI4irhk_x9rujJLPjCHbYrj6Gy7I81u6tNi_21tYnhTJ8tlrPoSdeNSQEguny3iJ2Zt_J0N4-cdvPlMxWTxdpeGXz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWcBlNEckcxliRgYszOLNvm94xMHwV5oTnZwTRrYazrKLuxqp27C-YB-d2FP9fM3GfDTz9qd3Sgv-f22jc25SOC9iTroS7morTLEqIaiAsXqt-OG5Z4w-LkUICTaZjyxYqX6ByneUwS-qFBcibHtc5lLE6bUSdj0ESTmTUHQEzVU6cbzgE-7WzD8sdRvO4PlzOg0pJrhJLhug_JWDuf5TGin1tYOitUy8MSdBuQw4uGBEu3GMvADvIqGPjXCfnR7RXHuJ99ey7KezJ-NxFp15lGxFn_vPY7L2XmYvNgS5xYL57BrE-D2bHHMaU9tPwFHItCKm51VH9Jjorys_k96jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-gToslejSu8fG0RLX4wXJoafUSisDqOIPc6FKOVmElrO-bNrYtHCuYtxZtMd_-rbiNE8EliXRdsIIFhopjEfRw4FMPHFbNA9FcGOE51YFannTiJZy-e9Lm9YyNgliqf4WyAA0RHf5ZWSviwFdSjgzz_T0xe6B6r9f2eYFExue5ujpK90pGok9aPL3C3UP1OX4M_gWo-DIawqk8-HdAqkvVWmRae330_rJuWAgXkEsH-Du1d88MuY3EOoxB_XjisK7y5CryF-Y_qaDODutaTUR_vB5W0vX02Hwv4ljXvEiUSdJxZhhKqbYgWY6BRgjFw96RImK8dEPrIeAqh5iJ4kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ضربۀ پلیس البرز به سوداگران شیشه‌ای
🔹
پلیس مبارزه با مواد مخدر استان البرز ۳۹۰ کیلوگرم شیشه را کشف کرد؛ در این عملیات ۳ قاچاقچی دستگیر و ۲ خودرو توقیف شد.
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/461792" target="_blank">📅 16:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461791">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a934d86157.mp4?token=Q0Dv2_DjMDrQdOYHHcqEn4V8z9OcTUaq6QGTwh4w3WoZj3jTUxSfSeegwzGSUnL7jhZfNi79_-PXP-P4Vpq095YTSVES55_ZP1laWyAITvH1iTJr9d_m9LNhWxqD44taLwRm0A7uVKD6uZksALW90NvcHVogye3cJvf9k3pNDi9XrC-WROA9GHob1Ipg9VFAhOeNMJc8CHs1Nwe_azDykLz8nOF4gdcxgS_LUIxvyxUTHDfb8pp1dOeWmBB4vQDdOCIeKSbC0Mki5xiEZ_fCFISnzxJNbGn-trzWlmCBs5q2rie8MBtxOMJFldXeETjtIIFJ416a8UWZHsuPevR1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a934d86157.mp4?token=Q0Dv2_DjMDrQdOYHHcqEn4V8z9OcTUaq6QGTwh4w3WoZj3jTUxSfSeegwzGSUnL7jhZfNi79_-PXP-P4Vpq095YTSVES55_ZP1laWyAITvH1iTJr9d_m9LNhWxqD44taLwRm0A7uVKD6uZksALW90NvcHVogye3cJvf9k3pNDi9XrC-WROA9GHob1Ipg9VFAhOeNMJc8CHs1Nwe_azDykLz8nOF4gdcxgS_LUIxvyxUTHDfb8pp1dOeWmBB4vQDdOCIeKSbC0Mki5xiEZ_fCFISnzxJNbGn-trzWlmCBs5q2rie8MBtxOMJFldXeETjtIIFJ416a8UWZHsuPevR1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: زیرساخت‌هایی که طی دهه‌ها برای توسعۀ ایران ساخته شده بود، در جنگ اخیر آسیب دید
🔹
این وقایع یادآور مسئولیت سنگین جامعۀ بین‌المللی در قبال حمایت از غیرنظامیان و جلوگیری از عادی‌سازی حمله به اهداف غیرنظامی است.
🔹
بریکس باید اطمینان دهد که هوش مصنوعی…</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/461791" target="_blank">📅 15:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461790">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91359b9ec1.mp4?token=fTM-WiGo1DliWP3gKC2RXcdECPpglu1p8AKvmAYKeGpSmy8_32AuiqxgqU12AkirChI8qOfPMrhSSLJWtSx-px2D_S2zddFslRLAVhq79DzgW4aNb25Kt-mgBL9ss1R_AzblxlCGoFTxElCuDX6xvXvp6RkPIhon4LWilNoX6kyoefBZwHA-42GhA-UZZNZdTHzst8qba2_YBdTTDjk-j_DKfVs8cKS6y6Q19deRIs6TEUG6p-5uev2hmAUvxS4XgJBCQCtAvHhgCVxRXwskGA73vlPSsq1qwi01Bw-dSiFX75R7Xng6SO_Aw2mYTQXQPsbhm3CuOvedBRAUQOynQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91359b9ec1.mp4?token=fTM-WiGo1DliWP3gKC2RXcdECPpglu1p8AKvmAYKeGpSmy8_32AuiqxgqU12AkirChI8qOfPMrhSSLJWtSx-px2D_S2zddFslRLAVhq79DzgW4aNb25Kt-mgBL9ss1R_AzblxlCGoFTxElCuDX6xvXvp6RkPIhon4LWilNoX6kyoefBZwHA-42GhA-UZZNZdTHzst8qba2_YBdTTDjk-j_DKfVs8cKS6y6Q19deRIs6TEUG6p-5uev2hmAUvxS4XgJBCQCtAvHhgCVxRXwskGA73vlPSsq1qwi01Bw-dSiFX75R7Xng6SO_Aw2mYTQXQPsbhm3CuOvedBRAUQOynQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
🔸
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند. @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/461790" target="_blank">📅 15:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461789">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643027f01a.mp4?token=j5y-alVxQa9O3rA7ey-C8xW9cF5SUwTuzQBzDb5HK-wpm7S9wj4sgYimL2TP6ZpjOtzFak3OdfZm1_Pa0HyZOJXV2Dg5qQ2mHlfjKEvr8aeejeKIkfDeapsdhTRlKAMGVS1f6AbBs_AzxwMXPF3NgvVKxgNAsVu2r2zRHib_2SdKC4DH6xbR8wDwiO9x5hztJIkldb1NnbFkeL4aAljy4IKTvnRMN4rIGiJhk3OavFnGFptgl12tG4PbYHvKpr4vxeFZzciTyLI2vax3MeTNak1aYuqh004JyYgj3Yzyd-EQGILpe7zSaVa5OGwqmzH_Ibd6I_J6pB0wzGTRufpSeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643027f01a.mp4?token=j5y-alVxQa9O3rA7ey-C8xW9cF5SUwTuzQBzDb5HK-wpm7S9wj4sgYimL2TP6ZpjOtzFak3OdfZm1_Pa0HyZOJXV2Dg5qQ2mHlfjKEvr8aeejeKIkfDeapsdhTRlKAMGVS1f6AbBs_AzxwMXPF3NgvVKxgNAsVu2r2zRHib_2SdKC4DH6xbR8wDwiO9x5hztJIkldb1NnbFkeL4aAljy4IKTvnRMN4rIGiJhk3OavFnGFptgl12tG4PbYHvKpr4vxeFZzciTyLI2vax3MeTNak1aYuqh004JyYgj3Yzyd-EQGILpe7zSaVa5OGwqmzH_Ibd6I_J6pB0wzGTRufpSeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
🔸
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/461789" target="_blank">📅 15:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trzBB7mC8YCYA7cSSPeNnjKv4LvNjeQt65Isziuq6K4UXzyGUgjhTrEiJj6_tv__i0EklBBnEDuW4To31Vh_tunf4Zpg57Qt6i-GqXJarIAbLtc_Z1EcZIgxcA6AXMhMXO6pJ8cU1LI631hLdXt55R_Yy1j9SDxPasrUM-SfzD_4aPEB5qmvD7TFMAb6fec2YBjFzVxzv_IBMUXlQIOVuk2Z9q3-xE917L8JnSMi2Z0Z5g0QyjEQ2EK1FvqiashVTlMC1ZecKKdZnNdxHeyZO02jasCd_qLaHRiMpGpYn5Q8P50XexcAe7Ci1CP866vFzKCLT1iS2ZaC-DfAs-zx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات از تکذیب هشدارش به نتانیاهو خودداری کرد
🔹
روزنامه عبری یدیعوت آحارونوت گزارش داد که از امارات خواسته شده بود اطلاعات مربوط به هشدار محمد بن زاید، رئیس امارات به بنیامین نتانیاهو، نخست‌وزیر رژیم اشغالگر درباره عملیاتی که شهید یحیی السنوار، رئیس جنبش حماس در نوار غزه برای پیش از ۷ اکتبر ۲۰۲۳ طراحی کرده بود را تکذیب کند؛ اما ابوظبی از این تکذیبیه خودداری کرد.
🔹
این روزنامه عنوان داشت که امارات تنها به پاسخ‌های دیپلماتیک بسنده کرد تا در اختلافات داخلی اسرائیل درگیر نشود و تأکید کرد که «اگر امارات واقعاً به نتانیاهو هشدار نداده بود، قطعاً این موضوع را تکذیب می‌کرد.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461788" target="_blank">📅 15:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23cc25a7ce.mp4?token=VRR4_q0ffnQPWPjGBBeG4eHgEaWKTgvJXzaopt-_lTJSxzZUzvh1-4rMYdhewu6RrR4Lbs41nkMPwRggZTqCjtOBG3loDatnUAwg8VMtKhjUJS-j3JFq3kisDyW86ojcFIRUdnRm3wv938Ko8R0G_-ZuxVvPaFFOZDLFVtFP6Lc7ToO85P2oX-7HfVme4f0McDlGQfIVYwNhea_3Cf_m-qxYhCv9cbcjFmsdw_F124kY4qN9R9nQwWzfYu56JVlNziZZjpZCqXBrKTt5x_qY-kkXIWjmyhJXkIOahtMY0tHM34xSkl07H-dyGKKusBBdU22jlQVo42vVgfulejeeqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23cc25a7ce.mp4?token=VRR4_q0ffnQPWPjGBBeG4eHgEaWKTgvJXzaopt-_lTJSxzZUzvh1-4rMYdhewu6RrR4Lbs41nkMPwRggZTqCjtOBG3loDatnUAwg8VMtKhjUJS-j3JFq3kisDyW86ojcFIRUdnRm3wv938Ko8R0G_-ZuxVvPaFFOZDLFVtFP6Lc7ToO85P2oX-7HfVme4f0McDlGQfIVYwNhea_3Cf_m-qxYhCv9cbcjFmsdw_F124kY4qN9R9nQwWzfYu56JVlNziZZjpZCqXBrKTt5x_qY-kkXIWjmyhJXkIOahtMY0tHM34xSkl07H-dyGKKusBBdU22jlQVo42vVgfulejeeqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژاپن دست دوم را هم از ایران برد
🇮🇷
۲۱ | ۲۴
🇯🇵
۲۵ | ۲۶  @Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/461787" target="_blank">📅 15:35 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
