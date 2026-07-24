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
<img src="https://cdn4.telesco.pe/file/COUeBOHS89lnRK1xf9cHnOL__ll_W_sm3n1t06vwbpUDJr3Mylx_AhC9GzRdIKHozcyjGWUOZShI_wL7wFUNr4wzB1dIjZTmuwLa1Fs1A6hah6wBTLbjkm3gB5WzbNOs52utfIyV1veXQdzvWV8DGuu9ArkPDFqNjxR4k_GOnGaNqiHfN9PA2Bd3xW7BlRhNRHGaNRPQvI0E5mT0z7zmGTOsdCh4bF_LvQ4Ui7l1689Gzyz7Wvjo_BHzG3jL8IT8Mm5tloC5Ts9Rn2Sw_4aeQfHP581eBDsatVFPLiKwR0enivG_IYzYYlz-I0VcRvD_-bqwTdrJAyh7hW0OGIpnLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 932K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 13:38:17</div>
<hr>

<div class="tg-post" id="msg-137190">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پلیس فتا تو مشهد یه دختر ۲۰ ساله رو دستگیر کرده که پسرا رو میاورده خونه فیلم های سکــسی ارباب رعیتی و فیتیش پا و... ازشون ضبط میکرده و بعد به قیمت های بالا میفروخته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/alonews/137190" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137189">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myL47O1tp2WCo6r6NpUslScm_5R_rJyqkwwbefHy2gZkfKyyRLxJhhvjcAxJd3j4SrG34W7i2nNQlE7oQUCLczYRWGO9BH-PyhcjMlwQS-SjRBPli4c-j7ugB5V6ore57VS2Ay43qML45wksrCaF9Fh8ijMOJHZBf9TXM4L-ngYyPp8RwZdNE8PdDxMxCDX3b8ygkuPQweWvmJ443MvmkIA4yJH8arQjIl1ftRBGW_h2M13rU7EpcKMvyVRSUhehRXBDnaB1ciYTPeHWLrS4H29gnv0flkk8aE_hZj2LQZ8-n80xcgaeidAAIa3O6PqBUxAWnxXp88c00vBODs4Pvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلیس فتا تو مشهد یه دختر ۲۰ ساله رو دستگیر کرده که پسرا رو میاورده خونه فیلم های سکــسی ارباب رعیتی و فیتیش پا و... ازشون ضبط میکرده و بعد به قیمت های بالا میفروخته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/alonews/137189" target="_blank">📅 13:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137188">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نیویورک تایمز: ایران، پیشنهاد آتش‌بس موقت آمریکا را که توسط دونالد ترامپ به تهران ارائه شده بود و توسط نخست‌وزیر عراق، پس از بازدیدش از کاخ سفید، به تهران منتقل شده بود، رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/137188" target="_blank">📅 13:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137187">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رویترز: در ۱ مرداد، تنها یک نفتکش از تنگه هرمز عبور کرده و این کمترین میزان از ۱۷ اردیبهشت تاکنون است و هیچ نفتکشی نیز وارد این تنگه نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/137187" target="_blank">📅 13:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137186">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYkqfdZeCV0QfGv0Am33gFDvAdSwI2v0Xpx0u7R3JJVCXjtQNwXQGyWG8jmAXytNo4f8K3ABCzWSXpN7LAvSJk4Q3xIuA3knSG6wndCnf7yI4bab9fTc-VySQAYc3hdRIyMvEVZ44o0mROQD3UJJ8PG8MzKvN5zDQ5t2_BRj0FGalTE3jCSl4YhTvLpIxM4iykwRdS7OSvFhNpBF8pRj5o66GqE1VbKjm_-LswOba4IQjDH7T1Rzb6MR1qyQUSFjKgPq1_LHhyr-Y4FBGigKofOhKlf7i3LococfAqG52TF7BJvfr2sMVqaUF9TCvyLkTBdMvKsS2_eT70zOq47IEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس آمریکا همچنان سنگین داره می‌ریزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/137186" target="_blank">📅 13:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137185">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2EojfSDvHyquYhE0CsqIwL6OTcAigk3X8oSIBP_2rprSnLRwOFGX_BbfWLrKUz070JA2B_ZHTo3oCDBKmXUrMn-E9EKzFVe2OR73YIaoOBhmdntR1iJwOw_qrm6dpdV_4VKeuTut6B4MQ62CSrq1l-tkhr_xJuWtCnd-79deYv_DwKnwyhh93JhYa9BKd-tDHkb6BSsSQtzRkglhalpefV42aeG2ZHsM8m1XPBowBVzBa0vAJg-Bzq3YD54wQnvE91VWoLQLBJVBWCE80t8NDwGUIbVLoLQvbwjJ5cYIulk6Laa7SYslali5dVDtdBoQFKfsHAml23KX_6FWjWJDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب فیروز آباد فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/137185" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137184">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=KqcKjSrJGWgMVatgGLMeoNB1sDYSlFo46yyHsbS4zc5oxFt1fLARm7-LF8MxBjPxhKYn5rrukYvoMERfHz5JRHv4hOx2gI5Qr-F0nqzvFATAsIQWmkSzSJmCEfe96pkJTdSxj3rTSIbtFURYHr9jdRw0VtThhJisON2OhF07vssO9Y-Grua9elW5wS7jEk-HX4-jb0cSJ80Sba0USr6YE00G56mntYa-0uY64VBsxuUUJsdSyN1yKpHFT_oUuEF5_hjyqLsnaxfzZVYln_UecWjXqayulFQ5QpyFytLwNvtTM11nRfQhLQu-_zZwaXYlf_zTW-q_DsMtPGypvCYxIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=KqcKjSrJGWgMVatgGLMeoNB1sDYSlFo46yyHsbS4zc5oxFt1fLARm7-LF8MxBjPxhKYn5rrukYvoMERfHz5JRHv4hOx2gI5Qr-F0nqzvFATAsIQWmkSzSJmCEfe96pkJTdSxj3rTSIbtFURYHr9jdRw0VtThhJisON2OhF07vssO9Y-Grua9elW5wS7jEk-HX4-jb0cSJ80Sba0USr6YE00G56mntYa-0uY64VBsxuUUJsdSyN1yKpHFT_oUuEF5_hjyqLsnaxfzZVYln_UecWjXqayulFQ5QpyFytLwNvtTM11nRfQhLQu-_zZwaXYlf_zTW-q_DsMtPGypvCYxIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رائفی پور: آمریکا به روزای آخرش رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/137184" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137183">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
شنیده شدن صدای چندین انفجار در اطراف فرودگاه بین‌المللی اربیل و مناطق غربی این شهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/137183" target="_blank">📅 13:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137182">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d9d6f9b1.mp4?token=n9NI2ouggvXeWqb2-5vwzibetGEsudzLy-aRal1Hx5Z2EQ9I1v8rDR_wjBsmqUu5_KGKdEYNtayZ42q19RRMWLVAtxO3-t5tIKXuZix5Z412CZfvw3djMdqz6MYThkrp2yI_iuiLgqeOUma4Rl_t1GGSfcLSutt4bwO5nhrMmdW03he1Ni4n920owe6mP098_rLKPSscDECvduLQ_QX3dp0gN1NhkCVVDKCM6u-jDO9lvDRyNeV5dF05m16xA_kuSmkzqNezkUjKUENMbWxOTYjcTG9XORL5fDOBIz6tv9iW7FIHin7lQyqpwpp2DWAeOe6vsspQNrQojRdcO3ry-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d9d6f9b1.mp4?token=n9NI2ouggvXeWqb2-5vwzibetGEsudzLy-aRal1Hx5Z2EQ9I1v8rDR_wjBsmqUu5_KGKdEYNtayZ42q19RRMWLVAtxO3-t5tIKXuZix5Z412CZfvw3djMdqz6MYThkrp2yI_iuiLgqeOUma4Rl_t1GGSfcLSutt4bwO5nhrMmdW03he1Ni4n920owe6mP098_rLKPSscDECvduLQ_QX3dp0gN1NhkCVVDKCM6u-jDO9lvDRyNeV5dF05m16xA_kuSmkzqNezkUjKUENMbWxOTYjcTG9XORL5fDOBIz6tv9iW7FIHin7lQyqpwpp2DWAeOe6vsspQNrQojRdcO3ry-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبتای احد شکوهیان از داخل زندان:
من یه کارگر ساده نان‌آور و سرپرست مادر پیرم و پرستار برادرِ 55 ساله‌ی ناتوان جسمی و سکته‌ی مغزی خودم هستم که همیشه وضعیت مالی بدی داشتم.
تو شلوغی‌های 18دی دیدم که مردم برای نجات دونفر دارن میخوان مسجد رو باز کنن و وقتی رفتیم داخل هیچ کار خاصی نکردیم به جز یه نفر که تخریب و آتیش‌سوزی مسجد رو انجام داد و دوربینا هم فیلم همه‌چیو دارن.
بازپرس‌ها بدون در نظر گرفتن حرفام و فیلم دوربینا، میگن که اون شخص که مسجد رو آتیش زده و باعث کشته‌شدن دونفر تو آتیش‌سوزی شده، منم.
از مردم و جوامع بین‌المللی خواهش میکنم که صدای من باشید و نذارید یه شخص بیگناه کشته بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/137182" target="_blank">📅 13:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137181">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">گرفتار قومی شدیم که کلا ۲الی۳میلیونن اما خودشون رو نماینده ۹۰میلیون نفر میدونن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/137181" target="_blank">📅 13:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137180">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گزارش انفجار انتحاری در منطقه خیبر، پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/137180" target="_blank">📅 13:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137179">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عطریانفر: جریان سعید جلیلی فقط هیاهو است ، اما به حاشیه خواهد رفت
🔴
این جریان فقط قدرت اخلال دارند.
🔴
این جریان ضعیف خواهد شد و به حاشیه می‌رود
🔴
این جریان با ضریب دو برابر به سرنوشت احمدی‌نژاد دچار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/137179" target="_blank">📅 12:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137178">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزارت بازرگانی چین : علت اعمال محدودیت بر صادرات کالاهای دو منظوره نظامی و غیرنظامی به ۱۴ شرکت اتحادیه اروپا به دلایل امنیت ملی است.
🔴
این ممنوعیت از امروز اجرایی است و این کالاها دیگر صادر نمی‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/137178" target="_blank">📅 12:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137177">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUoMX8VG5LoY_JYjUjE3Ke17PUVu6FlXzcRnfEx8JNHf_jlBbtBDW6wLhFb6X-ztq6gW-vQ5dJcc5hOGCPmCXUdnTZWgqhTiBXbGCBkg5q4rmWH8W77WStXPP3_d0x6Sk54v0xNvMjz5NBVbfHcl982Fm7664rynIV1Lz0Yg63us-WfzW1hoYui6-ITnyhdSs2j5tU3Ya_fHl-72YCWdj4Pfawu5EGetamp8zrvB2yEpHyPftP_IAX8zEe9cym0iLZ0qZ68rIG6txBOCa1X1HsPWQbNs_r8fH0zKzI2km58xPj4d8cZo03WWcRiX5fxhaDx4leR8nPRKzYXVHvWZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: مردم ایران عاشق رهبرن
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/137177" target="_blank">📅 12:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137173">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf63a433c0.mp4?token=pWIJaFGI2S62Fx9fuUo7MmmDqYtfhrHskQmLWouEvIzrUXdz_JJctbanGD87IbU5lJCi0eeCHjLcZQyvkJvqH33BmmpBG3uWOKDopqVl13kklUw36ihNd3wBZum9CHq1_1iJa-4G2TOwv-Gu2lSMCiIGljbPh3tn8Yxidi1t0D62c-3nzcOjfMHRy5B7jQ8oRcKzifOuTeWm5gJoTfxkqlsgoO1thy2fe_rC7GmvGUn9gaf_8ojxo1JqVSmF8bUOFi1dTiMknDeXWpCOtjSpRREn0aC6pbuf1H3F7zP44P8whTESsORxVy_bN4Z68iFH-JJm7-jk4r3RceRNQVagwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf63a433c0.mp4?token=pWIJaFGI2S62Fx9fuUo7MmmDqYtfhrHskQmLWouEvIzrUXdz_JJctbanGD87IbU5lJCi0eeCHjLcZQyvkJvqH33BmmpBG3uWOKDopqVl13kklUw36ihNd3wBZum9CHq1_1iJa-4G2TOwv-Gu2lSMCiIGljbPh3tn8Yxidi1t0D62c-3nzcOjfMHRy5B7jQ8oRcKzifOuTeWm5gJoTfxkqlsgoO1thy2fe_rC7GmvGUn9gaf_8ojxo1JqVSmF8bUOFi1dTiMknDeXWpCOtjSpRREn0aC6pbuf1H3F7zP44P8whTESsORxVy_bN4Z68iFH-JJm7-jk4r3RceRNQVagwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی اوکراین ، چند مرکز فروشگاه زنجیره‌ای «وایلدبریز» روسیه رو نابود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/137173" target="_blank">📅 12:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137172">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وب‌سایت کپلر برای داده‌های دریایی: تعداد کشتی‌هایی که در ۲۴ ساعت گذشته از تنگه باب‌المندب عبور کرده‌اند، به ۱۲ فرارسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/137172" target="_blank">📅 12:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137171">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
گزارش از هند: شرکت کوکاکولا قیمت نوشیدنی‌های رژیمی (دایت) را در این کشور بیش از ۱۰ درصد افزایش داد. این افزایش قیمت به دلیل اختلال در زنجیره تامین ناشی از مشکلات در تردد کشتی‌ها از تنگه هرمز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/137171" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137170">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ddf0a505.mp4?token=pxP119UnA1rUNdJuYvxDr9kv7yUVbjI9NHUN5ptp2lVWelDhEZH7tw-w5loP_d8VU2a6FXoLv8KL5gMPGNjD48kTkRrOdr5DXsGZa0TxRHvKssELTctcqE8T0uBieISqhf4h8KwDETwL5ZELq43C7t2Fgf-lEO4ZR8xxvjwbkbISZqhYg7yOiuRjdXn1P4oVfGpKWSLEYC5OPEr6dACJ2DQ_bbRSfOmR7wWSMei6Cc3X4NzJHfTyzhC-1lWyOgsNXHTuusdQ_RApZq9h7zc55x3KMY9omRMKnpAn8xzIb74_sEWRl0tcaSWyiWpHaqSeNUkS9qIxZAyO-oKJl6XmXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ddf0a505.mp4?token=pxP119UnA1rUNdJuYvxDr9kv7yUVbjI9NHUN5ptp2lVWelDhEZH7tw-w5loP_d8VU2a6FXoLv8KL5gMPGNjD48kTkRrOdr5DXsGZa0TxRHvKssELTctcqE8T0uBieISqhf4h8KwDETwL5ZELq43C7t2Fgf-lEO4ZR8xxvjwbkbISZqhYg7yOiuRjdXn1P4oVfGpKWSLEYC5OPEr6dACJ2DQ_bbRSfOmR7wWSMei6Cc3X4NzJHfTyzhC-1lWyOgsNXHTuusdQ_RApZq9h7zc55x3KMY9omRMKnpAn8xzIb74_sEWRl0tcaSWyiWpHaqSeNUkS9qIxZAyO-oKJl6XmXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهریاری: ثابتی جان جوگیر نشو، رهبری رهبر شیعیان دنیا هست نه رهبر مسلمانان
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/137170" target="_blank">📅 12:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137169">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رئیس‌جمهور رومانی، کلاوس : یه جنگنده F-16 یه پهپاد رو که وارد فضای هوایی کشور شده بود، سرنگون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/137169" target="_blank">📅 12:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137168">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA_Qd2BUewEHMc7oRIM-KpLCHVasobpYSGIqEABcqIbHHBpEWW4uyuFlD6fZ-ct-Y3GRX5fQ9niiBvMSLmSMbXrol7yIO7RQObjyLvQvopgsBdPdUr2P4A5Um7_vtefMebMJOhMbl-GGcjcw27lIdnBUx1wX0wTGp7JzB3ub3rKWD9A--1yvcbJ8e3Kcfm6YYZrkjYU3a7DXs97c4b6-N4CJTGcQ5PMCElKb5Kkrd2uTK2SEHdMdENc85Ilt40d6gSc7PxvEArpg6BraUF0K36yXNbAUzvczd_oDh35-UP_kPYpYhJBsCq7plitcOzw_iR4Tmfyh05k6R58Uxn45mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: "توقیف دارایی‌های یک کشور برای پرداخت مطالبات احتمالی و نامرتبط در آینده، ایجاد یک سابقه خطرناک و التهاب‌آفرین است
🔴
کسانی که از چنین منابعی استقبال می‌کنند یا از آن سود می‌برند، باید به خاطر داشته باشند که وقتی دولت‌ها مصادره اموال دیگران را به یک رویه عادی تبدیل کنند، دیگر هیچ دارایی‌ای از امنیت و مصونیت برخوردار نخواهد بود. آشوب و بی‌ثباتیِ ناشی از چنین روندی، نه خوشایند خواهد بود و نه صلح‌آمیز"
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/137168" target="_blank">📅 12:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137167">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بقائی: با چین و روسیه درباره تحولات غرب آسیا بحث می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/137167" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137166">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سپاه:
باقی مونده ساختمون آمازون رو نابود کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/137166" target="_blank">📅 12:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137165">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W57sO88pxOurPToLBGfsF4jaI1ycZjFrzLY3nc8EfbJODyF7uYozQTDkd0YENYewv4I_06CzM0qaVoQfP13DuPWa7HBrYTf0lKWLqqZ1BzGoY6HkKdhRZM08yE-b8Thd9g_w2RiYlTfQMHbkVaIll12TZhRz6Bol8q_M8XeBE8UfsHxt2b5HmvV-gYqO15wTtny0oG2Pp5zAyxRXAwsLjURXBK72vrBi3CyMo3DeCLhRI6PM3wGWb9hakuK6D8EB2YN-C_0MX6cQD3mxHWH31uIlKso6PTpX53MJZsLqYEf2QpwvgmMYpWifIrv8c48FN9iAvHNJQItjMTMP-bciSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا یک موشک کروز آمریکایی در حریم هوایی شهرستان کهنوج، واقع در استان کرمان، شناسایی، رهگیری و منهدم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/137165" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137164">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a7d74649.mp4?token=mCXt4cbePqu-OmTfAUZLrWROLpW0ERd4vdpXwALBLrRWDNfSXBf5P7NE8rjta3zRYl6mz5-nQc0O_-Io7bLj9Qy7fQWgTw8DeL5okKy9joHq8JX43u16D5uDW3YFT5_aT5m9JSC5FNWPEkqqRvGTgprlkxq8cdbwW8Yj2hzPKHI6E1aSNSHNEFZJMQKQwcx3sDgW_1O0XqoVG7qihktrPOCd3T39HGCddQSfMeNSi9ltvi3JQWCS6KDGBOKMMGSyDKZjHmd-lo_0vYrN-hUFb11UuO8MoCsOAmmCm09f-GF47UwWl0mYlK-XG1Xp1LvDX1H_F2XUAeFAp_H3HlZsKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a7d74649.mp4?token=mCXt4cbePqu-OmTfAUZLrWROLpW0ERd4vdpXwALBLrRWDNfSXBf5P7NE8rjta3zRYl6mz5-nQc0O_-Io7bLj9Qy7fQWgTw8DeL5okKy9joHq8JX43u16D5uDW3YFT5_aT5m9JSC5FNWPEkqqRvGTgprlkxq8cdbwW8Yj2hzPKHI6E1aSNSHNEFZJMQKQwcx3sDgW_1O0XqoVG7qihktrPOCd3T39HGCddQSfMeNSi9ltvi3JQWCS6KDGBOKMMGSyDKZjHmd-lo_0vYrN-hUFb11UuO8MoCsOAmmCm09f-GF47UwWl0mYlK-XG1Xp1LvDX1H_F2XUAeFAp_H3HlZsKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اعلام کرد که با استفاده از پهپادهای "آرش"، انبارهای تجهیزات ارتش آمریکا را در پایگاه العدری، و همچنین پادگان‌های نیروها در دوحه و تعدادی از مواضع را در پایگاه عریفجان در کویت مورد هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/137164" target="_blank">📅 11:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137158">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41ff96b40d.mp4?token=nK8ZU6cSNTxxgG5zyXfeN12rd0cTAD9UHY5bUDLVRaOuCoij4tSiSErzwSkXusgtSgvXxdBl9Z5v_HzSwbMm0jDnHvQ6PzrbZ3ncHp5jA1jn6iZeNFy4WOx6Cq9tMx5yJCe2zYLm_ChIw10lXNC5J5NwY0nbRi6Dd0BrxNbSH1nQlh59iQernTshMK8lj6dsSkri2VT2ZEjjzhjPgLluV-MEJ9wwTYHJVkHYML37pqa-2LFmA6BFTMFrH7NZcGaZSP5aDonuttjEKhXqiowdAI1AQdzPEocgOZ6p_9KZPH7-PAOwKGRDtoDliO8fo05b-qPiYm4tqMt8MqbWfZXDtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41ff96b40d.mp4?token=nK8ZU6cSNTxxgG5zyXfeN12rd0cTAD9UHY5bUDLVRaOuCoij4tSiSErzwSkXusgtSgvXxdBl9Z5v_HzSwbMm0jDnHvQ6PzrbZ3ncHp5jA1jn6iZeNFy4WOx6Cq9tMx5yJCe2zYLm_ChIw10lXNC5J5NwY0nbRi6Dd0BrxNbSH1nQlh59iQernTshMK8lj6dsSkri2VT2ZEjjzhjPgLluV-MEJ9wwTYHJVkHYML37pqa-2LFmA6BFTMFrH7NZcGaZSP5aDonuttjEKhXqiowdAI1AQdzPEocgOZ6p_9KZPH7-PAOwKGRDtoDliO8fo05b-qPiYm4tqMt8MqbWfZXDtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوهای وحشتناک از انفجارهای دیشب در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/137158" target="_blank">📅 11:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137157">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/137157" target="_blank">📅 11:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137155">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3Kd4q07aJAohdA6eP8RzK53oKxKT9oFC4GBgd5UgWIAEu5zEwBiUR0uaa3QN5xSGUANk6rObbIk4xnS2ewFVNzXA1Vdh9uRoo86OmaXdCxTPoH-enF6Htgq3Z0pOYDkEKmZL1NQ8LMFSXlKoLDl2rqMOx7VMhRsGOzYgmIZh7AJPuRRLAy5Vx1wFLBtBldlYeHmP_z5-oXT1tqC79nsiee-noLkPFYytpEz3Jj82TfQqa-KgJIoeMGZBKliEDRlEbBDQCfUXcOmDoFzh3gwrSYtnuLzuMu9xSoVQUvNQJZGYNV2QeNBVEU4kRDmqT1oNT4m9WZiG_TmCoKGLc5Vhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdYKeQS3MuNP4369i_0poqb4mEV60hTMEjC2WySnBs9vL2PFH1EbjdyE5hubzaKTzkDV5QmpTBbz66Zq16TPAgsM8MQD0FppEDdiTVfkHV5cwNHnK_bHDjHmPtVw9ddjL3NaC9ABQNPDjN4ft57tKgdLzDFy-6pCLp6kQJcBKJBhie7QAaarz05YxK7D_NUgOjcDcu5VwJDsyVnbhAHAzZtbFxsy2KQCIbAXRbl9xvTKNUW3zXt3vPdxWZjjDdYs9eysZBI4x0dsl8MG0boYpmseGL-j2GV4pokDeHJJtwDpecZjVEeB7_GqImct0cX1m4M4fEtVS1RWil8lOg8Dtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای مستقل Sentinel-2 آسیب به مرکز داده Batelco RJR در منطقه عسکر بحرین پس از حملات ایران را تأیید می‌کند. این مرکز که از زیرساخت‌های مهم مخابراتی بحرین است و بخشی از سرورهای AWS را میزبانی می‌کند، آثار متعدد اصابت را در تصاویر ثبت‌شده در ۲۲ ژوئیه نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/137155" target="_blank">📅 11:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137154">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
شمار مجروحان حملات اخیر آمریکا به ۶۴۵ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/137154" target="_blank">📅 11:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137153">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
هواپیمایی قطر پرواز به بحرین، کویت و اربیل را تعلیق کرد
🔴
خطوط پروازهای مسافری به بحرین، کویت و اربیل را تا پایان ماه ژوئیه جاری به حالت تعلیق درآورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137153" target="_blank">📅 11:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137149">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmjQsm1WougwxNlB52NjE3LlNXuApzUgkauy_YEsokWtOyWYrwaETCbFT_tOGrVpQ6n2Hh36cyqyaTPpW2eQI674m4Wvr4BU3tVtTmtwZGHt7_k7gsqVtA1EBZ1nnlX-IXOgrP2wK_dcjRRq48RGdV2VIdKo32Q9qrY1fZ1EYOd7RqAQV5D3_6cQYqqD16JLLEx8WFyKw80U-O0DJZnwRSHrCw-N8ZZEJqHb8g17YHbtsuKvXSwpjzKBzIXDM0KxDGXoEpzksiFXfg8SVtPlSoq5iJ-T3OM-ACA5yD2hEqERMzfrrI9m1tgAD8ay0jEBE_MbgQ_Yy_dwsVEpvp_rbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ciDXDa8F6_KDnXwc3NU2_gJBFRpnkqMRJY-GGNpflMuiGX9cZM86R0Nf9RzayH9OzGhGsDOYxtK1cAAHgHqAG8goE5_tRSerWEzXO4aH94cBCiF0NtwsOkK1_oVIADjff3XAjzZKt8HzuhFvbhw534rUNrBWAGxPX3q9f8ecYDxa50DZIyh46O5Mm1QCt5kPg1LHD5vKXvdUX28vC5y6E0MM1k_aW5ZskzF_ehd0ihBov3ZgqpTRByUOoyhGPlf2GNeNjCIj3wdCSbufAi2kGxtmErloyhFLinVFJ7Kw7oCHmlAMzu4FEy-6Sc7eDL3eNAs7hIYHRjHKBOtnXhIJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMNkN96AKePoM7EHn9TyVjBXMj0efd0InSqU1xr6q4jncY1goRFmNkEgLQWp2BJGREPjBQIjBNvvRF3ZU2XTIg7twsc742X4NKEgvYx91HXIJvTuwd4HZYXp296C46_SyNk2tdN_6sZGVmjJArJ8PNMLfMUuwgf-t5HQnnTPlHzR2sn5iya4HIf_b2Gj_4wP38OaoB7xnJUO4ph1LwJiZfAyZJiDid_V5pIioWqXccnP1Z-Udwpa4ImQ81xV4hKSQ2eH96lX2FPVxf1iC_bJNfaz2gwxGfVIDisXqC1NdKeel-6cHsS8lK2U-5RwAay8lbgwW0MnuKFNxzfSnke6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4ro9UitdepW-7RZTW69u_5sY4VGv5xm_IbhlZRAV56-QAx6RWYcOjwR7O6UXeB3WKxpzQNbZ6X2_gU6nPDY7mLFp8TjSDYqDokGAVXJPwC0a6-bUft0N62jUXbtBt_aP0_HBIMWL3PWpCUWtqyY-v0mJcA-5tGBOaRXo90QHBaPevSXXwbZ3r5E2jL4FRNpLR31PD0i01S6jdRGfO_lB0t2yih_CwQLXyySDtc7NCEB3ULfRwsCb4_SrLjPEgIbpO2fkC5asoZYAcnxElT_3SHJLXkL0V1eJUhwbSYjaowrB0tGoFL0J_8oGVHPLEAXWpxUyFVvG1kA05mgKNLLEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تمرین آمریکایی ها برای مقابله با ریز پرنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137149" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137148">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/137148" target="_blank">📅 11:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137146">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5552f9e237.mp4?token=YWToalxbz3lCdhcsIGF-GpEKPbAHVs2tI6fPGvFZ089p5S2pnwEqvBdfXKdF9Grog5AhpIbsq9LdqGRZV1CFhXrjRXHgu5MZ2N4PQVOf3SA7pZ3bcDJCJQq4OL_mt1UGcDHOcLI68ZnjvmQYvG0OJVrKSfoArM4aAywkLFi6lbl-ltQMRQuvIUQkPRdQbKjJM_ye44sT4bZnKQ7evJUmq5g_6j2oU3MIFAp0Mp2Hp8356viL8fEZAa9Pl8b0NssVQrLiCkbrIwhU7THslWVmSZJGIDXO8xDasae6q9gzrppZbr9Ae71eE5AIcoQLM11phyQr31H_zNJQTeqIOPBr0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5552f9e237.mp4?token=YWToalxbz3lCdhcsIGF-GpEKPbAHVs2tI6fPGvFZ089p5S2pnwEqvBdfXKdF9Grog5AhpIbsq9LdqGRZV1CFhXrjRXHgu5MZ2N4PQVOf3SA7pZ3bcDJCJQq4OL_mt1UGcDHOcLI68ZnjvmQYvG0OJVrKSfoArM4aAywkLFi6lbl-ltQMRQuvIUQkPRdQbKjJM_ye44sT4bZnKQ7evJUmq5g_6j2oU3MIFAp0Mp2Hp8356viL8fEZAa9Pl8b0NssVQrLiCkbrIwhU7THslWVmSZJGIDXO8xDasae6q9gzrppZbr9Ae71eE5AIcoQLM11phyQr31H_zNJQTeqIOPBr0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد شاهد در کردستان عراق قبل از اصابت مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137146" target="_blank">📅 11:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137145">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پرواز های فرودگاه اربیل تا اطلاع ثانوی به حالت تعلیق درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/137145" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137144">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d440c579ec.mp4?token=ROrr_PXNFEmNw7Ry61xEne8NJz03qFTtn34p43aMc3-rjl6eRPVPEAGz95bAGaHstI2lW-Z77SFxBh6wAbICDXPH9R9lZFgl0KqhI9ZqooB65i581zx5MV_KrXMkjl75HsGj4hgS_h8Am5o4hg4vz1wMIyZcia3FCViF5O4UraZrbmMTAh--_vAv9qB8MvSbLHoWJgQSitv3UnPJrVhmQtvNVj4hISLpxTyZuUdIJ0JwHmO2bf_HISa6HkA55GLQboYNatKh5xDV7dgboDWEDcUEzom6wM6UjRcIKJPBHms-yCmpWT6QLjt0gD6iKBgwn2uXRW7ojllD0H6V8ml_5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d440c579ec.mp4?token=ROrr_PXNFEmNw7Ry61xEne8NJz03qFTtn34p43aMc3-rjl6eRPVPEAGz95bAGaHstI2lW-Z77SFxBh6wAbICDXPH9R9lZFgl0KqhI9ZqooB65i581zx5MV_KrXMkjl75HsGj4hgS_h8Am5o4hg4vz1wMIyZcia3FCViF5O4UraZrbmMTAh--_vAv9qB8MvSbLHoWJgQSitv3UnPJrVhmQtvNVj4hISLpxTyZuUdIJ0JwHmO2bf_HISa6HkA55GLQboYNatKh5xDV7dgboDWEDcUEzom6wM6UjRcIKJPBHms-yCmpWT6QLjt0gD6iKBgwn2uXRW7ojllD0H6V8ml_5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارها در انبارهای کنسولگری آمریکا در استان اربیل، شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/137144" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137143">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
۲۵ سند در قالب ۹ تصمیم در پایان نشست وزرای خارجه سازمان همکاری شانگهای به امضا رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137143" target="_blank">📅 10:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137142">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B_8VpBfF8O0lxn3ObZPSYh7GUC4TIfaRKOdBItpSf6yAp3RYrlJi2e4od6zikLQUOImJkGQL5HKSMcClo6Y6p0s8w6KFTwxZfVSgeHu0pY6tuFTSBaxh-Cu9V3Mj7857RIRyVKEZlfR42pTx3qKkNzYwi3OEIB2Q1cov669fORUS0SnrLiDF25g3MZ5Mpqn_RDrhf-7QsmQ5BOfvPx7N7yy_-D9TQrJGkwWHm_4nriM2XxRblMfL75-iQLlUdkT58fpjP5HvSn_mzUG_QufEKBhPWNqPGDcXlqWiJvSOO_J3O4dWWSXLwE4NChQ9afqDU0pKnkWa-SuPB-P2ZD8Y7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله دیشب ارتش آمریکا به یک سوله ایی در نزدیکی اهواز که از قبل منهدم شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/137142" target="_blank">📅 10:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137139">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpsaOCVc5sqeCMCSIlaRzCJMNLGaroImFmnqLXwyutq2fMOltUzjImFOgf6Ml17oX2FJrMJbEIKhQyfxrevJmjXjC_oT4MIO8PugXak-qc-kFyLPOVxpdpOJqBQOdGR6IgmTWpow3aE64oSDdYsZ8FwSvGfv3emZJsdNLn8nE4ud2cIsEjEnxbwo1Jv9VPzgNxUY6CkqzWmia0fLyPQlHQXnH7sKZ2dFgKP5L8K3FFZI6vgtLjMRIVw-H0sklw-7EOQFBxojw6hvx8BUO1BBdZ7bifDLdVygFVxvx8QPFD9oQs1tItX9WexXjUTjoUfRBfDV_UP9ApoO2uc7u7N_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIwVGoWaj97oWeFzfEYXPOrpJ0_xkRP7BjG_FyDSX0VkEU2rn4mGghD9pSdBJQgOcyCIb7SKHNZYS2l53nKtCWX04T7y15UAxRy4jvmkTPeEhDslEZ9VMFBN03y13MnV6XD82YoZUnlUW-qUZRv30UHHIwZDYtiGcoETZXM7sEg0Ers-iTwRRE1nsT7Tk1LOx40LXlC9pwRE1nDzS2zDSaFSbeUP0LcuUeLDorDbyBCJdJ0M7ZANW2-w72eKkhG08nCEqJ6UlB2uAHucNAfPooxRT2XIRj3PXoKzPZ0jvhn_Rjuozl2HusH_6zJhkHEqK1DzZczIT6gnCu1BUTl1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujmN5EknypubzxDuS40D81KBckj5NCxk-aBnIzMcm6bX0ADLFlkQp0GwdNMPNvpd0jUrENGtc7VjBwgbP9l13LyMVk3WRjo3O48ZNdLi0SGur8miLpOexJX2q7yV-HeJRewCWP2oIrEdXApH6kp_dc1cMljE0-kTokQRGBBLsMK9KPCrjbkJEBRGOafIzYVPtOW_QKVgjRArZL4qutjSOkXpnrqG3XRCmow-JxvBv0aCGu94__hIWEk7slv5cwz5NQEetgXD2BC4Ytgp6-CDBqw1y81Stw3oWm9lQYdb3TYrCR0F8VQQ6-4drgLQgEVNRxjMuQoyvAruhhIYFcmk1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
استانداری گیلان: حمله موشکی آمریکا به مقر نیروی دریایی سپاه در زیباکنار
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/137139" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137137">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81df070eb2.mp4?token=Hl1Y24m4AFrXSnqONfN3iRMK_pJnaducwD2JHJrDJKyRweXMXPkXnUfSc8td8X-jrfhgRKnLLvBTC4UKRXZ5Hmb34Dw6PRfAhZsXtKp1A5T9ptNGuVE1EG_MhlCuqDR70TFH-_9EogiXmw5LU_YWsxhThndME5sSVNozAcrBSHFuSV0H5DVi7vSCl8QsIK91yZ2GiH3EmI1rlnBj5EFBja-ob64zyPiSqJ7iBqOjJBcQgjpG3CI3juV7m5wIFeY2vEPad4NOjqd6f__1IWneWSCxpoAkRCok_Mi3JLc-RzSTaeYujMqlsSSdkV341XC1Z0KUcn7ilgqCWfNmeOwiWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81df070eb2.mp4?token=Hl1Y24m4AFrXSnqONfN3iRMK_pJnaducwD2JHJrDJKyRweXMXPkXnUfSc8td8X-jrfhgRKnLLvBTC4UKRXZ5Hmb34Dw6PRfAhZsXtKp1A5T9ptNGuVE1EG_MhlCuqDR70TFH-_9EogiXmw5LU_YWsxhThndME5sSVNozAcrBSHFuSV0H5DVi7vSCl8QsIK91yZ2GiH3EmI1rlnBj5EFBja-ob64zyPiSqJ7iBqOjJBcQgjpG3CI3juV7m5wIFeY2vEPad4NOjqd6f__1IWneWSCxpoAkRCok_Mi3JLc-RzSTaeYujMqlsSSdkV341XC1Z0KUcn7ilgqCWfNmeOwiWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از محل برخورد پرتابه در نزدیکی فرودگاه اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/137137" target="_blank">📅 10:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137136">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
استانداری گیلان: حمله موشکی آمریکا به مقر نیروی دریایی سپاه در زیباکنار
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/137136" target="_blank">📅 10:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137135">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314e4b0791.mp4?token=q86rNIlDOgZ50onlH4ypRNXfba52_drO6iKbDwfvlkL9zU02HXFgjgHrH68pGpY1f2StLGfo7EYSBSGXK7XJr0P6qSiww1x8Tw-RNoPouL082YOSHi7UoCtsSGcmda_VdIh4wKU4b1ySMaaMJ1_JM7v7pBbzloh35xU46rtVoEwYfFi0TBxC3SVDhjJTyiJnH5U97QZWZmATPdjmUfudn7nWzhNjiPJZJ_CbcbmTNJUUQsXQt6tFu6qwOf9etDsP1gh8tSHYc-WkkgCZ7BnjCXtjYCTKBvCQUgOotDinzK8tYfyksyQeVYx1iljA05zHBq1lNoNtO_NnHwOFSqSv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314e4b0791.mp4?token=q86rNIlDOgZ50onlH4ypRNXfba52_drO6iKbDwfvlkL9zU02HXFgjgHrH68pGpY1f2StLGfo7EYSBSGXK7XJr0P6qSiww1x8Tw-RNoPouL082YOSHi7UoCtsSGcmda_VdIh4wKU4b1ySMaaMJ1_JM7v7pBbzloh35xU46rtVoEwYfFi0TBxC3SVDhjJTyiJnH5U97QZWZmATPdjmUfudn7nWzhNjiPJZJ_CbcbmTNJUUQsXQt6tFu6qwOf9etDsP1gh8tSHYc-WkkgCZ7BnjCXtjYCTKBvCQUgOotDinzK8tYfyksyQeVYx1iljA05zHBq1lNoNtO_NnHwOFSqSv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حمله هوایی به اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137135" target="_blank">📅 10:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137134">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgz5XKHQlpm3eCk_I3s2xwAE0SyPWwEFhJYNzNTpJ4x-UiV-TWsqbrqgKBV-LqYvfK1oZG_HHJE3QLWvITD5c1fDuzq-iwem3_0HU3UHgHNG40wQp_J_HXd3Gp3YnS4kpJTV1l_WpGhf6UKMSTAM4G-y71J_A6cSPGf23RYsnxKzE8H4KChCwFtXI3f8FJc0559l8lP6nnPkvtOy74wix9kY3OopkLAppf5VzAbkckWaRY3EGHUuGefXNJLjhEpw02UVSos_llu1pcV9QUWmVC8E4LQnS3pdwTfnWqBUcuPNMt3j-ItpN5UY7WsTHep6yCv2mTFQrxKjgIOBYA6ckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۷ فروند هواپیمای سوخت‌رسان دیگر آمریکا راهی خاورمیانه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137134" target="_blank">📅 10:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137133">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نیویورک تایمز : تهران در صورت عملی شدن تهدیدها تلاویو را هدف قرار میدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/137133" target="_blank">📅 09:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137132">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
روزنامه نیویورک‌تایمز در گزارشی مدعی شد دونالد ترامپ از زمان بازگشت به ریاست‌جمهوری، درآمد قابل‌توجهی از سرمایه‌گذاری‌های خارجی و بازار ارزهای دیجیتال به دست آورده است.
🔴
این گزارش می‌گوید: افزایش دارایی‌های ترامپ بار دیگر این پرسش را مطرح کرده که آیا او از جایگاه خود به‌عنوان رئیس‌جمهور برای افزایش ثروت شخصی‌اش استفاده می‌کند یا خیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/137132" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137131">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
گزارش صدای دو انفجار در نزدیکی پیرانشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/137131" target="_blank">📅 09:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137130">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
عراقچی: ایران آغازگر هیچ جنگی نبوده و نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/137130" target="_blank">📅 09:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137129">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d58fa8f7d.mp4?token=KcSv-8SUyKhWLtNjsQ9pYWdZseLp3JdwD_f3PujjCG-hvHO1IeZdlB7lAG_Vh01vbkZRVWspIZm5oPA5t9J8am3xsEGVcR8JwnGYsqnKsWDPI8gFyF0iZqv4J7VOMMl8iv4WayafdqH51BFIU7FRm9lLlR0apmBcZ-L3nhNrt5L6o5XHKVjZ_xtHK7w94wlR_vTdaAKy8NNJTGGgIZ5jtEqT-1OOaka40auXK7HoMYzpeYM8-xq0pDflG_MQG5J3OK9K8ZCt68VNDifoXgFyrNwj03beNttQ1x4cCSWRb6I1jF6lACwEycyh9pmoNtXekRXBBPBKq0j0BCYrUsbthQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d58fa8f7d.mp4?token=KcSv-8SUyKhWLtNjsQ9pYWdZseLp3JdwD_f3PujjCG-hvHO1IeZdlB7lAG_Vh01vbkZRVWspIZm5oPA5t9J8am3xsEGVcR8JwnGYsqnKsWDPI8gFyF0iZqv4J7VOMMl8iv4WayafdqH51BFIU7FRm9lLlR0apmBcZ-L3nhNrt5L6o5XHKVjZ_xtHK7w94wlR_vTdaAKy8NNJTGGgIZ5jtEqT-1OOaka40auXK7HoMYzpeYM8-xq0pDflG_MQG5J3OK9K8ZCt68VNDifoXgFyrNwj03beNttQ1x4cCSWRb6I1jF6lACwEycyh9pmoNtXekRXBBPBKq0j0BCYrUsbthQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: سکوت در برابر حملات به غیرنظامیان، امنیت جهانی را تهدید می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/137129" target="_blank">📅 09:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137128">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وال‌استریت ژورنال: کوشنر و ویتکاف همچنان بر این باورند که دستیابی به توافق با ایران امکان‌پذیر است
🔴
از سویی دیگر، ترامپ نسبت به توانایی و شکل ادامه مذاکرات با ایران برای دستیابی به صلحی پایدار، تردید بیشتری پیدا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/137128" target="_blank">📅 09:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137127">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ارتش اسرائیل از وقوع تیراندازی در نزدیکی شهرک «مزرعه جلعاد» در نزدیکی نابلس واقع در کرانه باختری خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/137127" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137126">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce2852983.mp4?token=Qfd6dz8NeOZ17oUNntZoXvfWe7F0Fcz4_iy7pdgIKhqrZl_Kj5Y-xfZHy8DFNqm_cqwuVWYy8pKhdTkDLCw9O_scZjwI-4XpF5DR9xwQFRw-nB-19H8POCm5kR4J8k52L39DSfAmnnWQjte6qzvJEajEAhAGZwWcPGj7HlrNo3ZyCT81xGsj-mtZlq8wZIZMRLYzHYaI8MKsI4F56Yx2xt38BWJnl_LhEHoi6CsEkgwzxfQoSM9eCSQWfGVJ5Uv2RmvoaqzCP3e9Ppji9R3DNrGw2HNqaD1jVDl4i3fobsCnGreHS6rLatbNVeTImY3OaIJscq8NZJaliqLPLe2qjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce2852983.mp4?token=Qfd6dz8NeOZ17oUNntZoXvfWe7F0Fcz4_iy7pdgIKhqrZl_Kj5Y-xfZHy8DFNqm_cqwuVWYy8pKhdTkDLCw9O_scZjwI-4XpF5DR9xwQFRw-nB-19H8POCm5kR4J8k52L39DSfAmnnWQjte6qzvJEajEAhAGZwWcPGj7HlrNo3ZyCT81xGsj-mtZlq8wZIZMRLYzHYaI8MKsI4F56Yx2xt38BWJnl_LhEHoi6CsEkgwzxfQoSM9eCSQWfGVJ5Uv2RmvoaqzCP3e9Ppji9R3DNrGw2HNqaD1jVDl4i3fobsCnGreHS6rLatbNVeTImY3OaIJscq8NZJaliqLPLe2qjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/137126" target="_blank">📅 09:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137125">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
عراقچی: برای رسیدن به تفاهم مسیر سختی را طی کردیم؛ قسمت داخلی‌اش هم سخت بود
🔴
برای اینکه به نقطه‌ای برسیم که اجازه مذاکره داده شود، گزارشات متعدد نوشته شد، صورت‌جلسات تهیه شد، فرستاده شد
🔴
تحمیلی صورت نگرفته؛ اگر که تکرار بکنیم که به ایشان تحمیل شده، یک جفایی به رهبری است
🔴
این تلاشی که بعضی‌ها می‌کنند که با استفاده از کلمه علی الاصول در جامعه ایجاد دلخوری و التهاب کنند، واقعاً درک نمی‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/137125" target="_blank">📅 09:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137124">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UT6CIhzU-aP5BaW40plmrKXiLqmUD0TVP5-H3fk1DYdXVAzFRIlaypzZHD9MsfEmiOqaOlysyypymPPU41_ilKuqKebaD_Ey22acZpHH4Y0FW7s_8DQPlOa7_E361gTicHnX7MqrPIaZ2OIiQZfCnyRNFLPcQkHKs8vocQ5IPUz6ojRGW-NW7zv7WBMeage_HLtE9zKBDP08-zh7M4j8hxjMlnf4kC_RW64szFoRTt-4MfbX-AFlga4jaQRRa3zMf1G0nod4Uryu2Uj34tUL8RNSvas-2J6AQQidDjUFOlDGK1pofTue7ydF1NbziRkjiB_D4_yHMm_Rq0JaIrn5qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هفت هواپیمای سوخت‌رسانی دیگر آمریکایی به سمت خاورمیانه در حرکت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/137124" target="_blank">📅 08:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137123">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
عراقچی: برخی به ما شعار مرگ بر سازشگر می‌دهند اما عراقی‌ها استقبال عجیب غریبی از من کردند!
🔴
کشورهای منطقه در حال تنظیم خودشان با قدرت ایران هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/137123" target="_blank">📅 08:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137122">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUvlemBmP_HhqZ7BxWG3jqEm1XqNJOZpzCuxAEdKaH2BBA1ym_vxLea-_asaqSRIZiMlVTR5Og_-pexY7yymcoP9O5IqP7j7DBqsBOLcRIV_aclnL9m8BN41GeZLHzsnI7QwwMd98mW3gHyslOBWgInnNauYfDkGO_nCJmmypWGhSm9gBXP5XM7okteTx69F0P4BNl2mFWM5TIY6kA6E77tzzyyybgC57CkRnKjBlTDimceipS5nTfrxHZwlp3pO0p24Pi7nQFSWsdreewr1NYsOmMxZHWe3aaK4IswY7LBcTB8i2jX5WsZM9nMBw87JtvEgP-vIxDadxVbGFxH1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/137122" target="_blank">📅 08:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137121">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGoBiNrW1dJ3Zf-qSMrNg49GAL5wOgUEADog6dx2XUOMgbzTatUfdxX0keFYNHlZVGiIk8-pXJKqYiKCClHymoLOb0YUnliKBEUzfNCP7PsSkgXLDwzFa0T2P2tK_j5HENMCHNY4SerHvgv-lDRDdhF8EFlS7J4L1JExMvum4FPDLJd0Qw_LWceCJnR8wB03NlC3XLnoGe7mzKwTNoNg0RR9IqPj4AB8nDHedIpjtpTlqe0CnV8q-y1QeG1coAEO70Q_HyzsfezQvAvxJo6CnYSNXJcwk_p38rS9HGVXYAqlYiTl7F32B9Px0P5mwPLNrt6Sw_8OAOuDLXaXVss7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی در کنار وزیرخارجه پاکستان در نشست وزیران سازمان همکاری شانگهای
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/137121" target="_blank">📅 08:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137120">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
مسئولان آمریکایی:
ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/137120" target="_blank">📅 03:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137119">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
خنداب اراک رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137119" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137118">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کوهدشت لرستان رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137118" target="_blank">📅 03:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137117">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4I5iUGaJuDg8fTJYZ_afQ7yBOyF4z2wsMn-uhlEDuHeoJXMffRP6weTiMbU37fTv7VPd_VV5Y9JWqktiP9cvfH0SWVKl9hi233lv-xtPZv8EVKYeC5gkI2n80RoiTCaanWgdvYmceOdtffq4Z53qCRBZ1eWqR_yrhwH5jlpa5RIyMfl_lrjniU4FJ0bmCKyGd48PbEOOw7a1FbfenA-Eaddi-Tm0emgJt_ldbo_m-HzFZJTZ3J-asy14Lr2mOlA_gVg-4oe5g1CY-dMpXTdXqzAkyG7htOlG-wctQrS2ce9saAHEuWN8CF9MUwKOj9wdNBPB30edMaRumVtR0KE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از بمباران امشب اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137117" target="_blank">📅 03:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137116">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
دزفول رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/alonews/137116" target="_blank">📅 03:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137115">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
خرم آباد رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/137115" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137114">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
نیویورک تایمز:
ایران امروز پیشنهاد آتش بسی که نخست وزیر عراق به تهران اورده بود رو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/alonews/137114" target="_blank">📅 03:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137112">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
چابهار رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/alonews/137112" target="_blank">📅 03:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137111">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قشم رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/137111" target="_blank">📅 02:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137110">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c10375a07a.mp4?token=vtd3vU4DZlix0o0SZe0Kjmb4BTYuhzRn1aZwFannZXLlz1XvODr2oUKmPrAa57h2e91OLmjpobo99gZgoYIg8IixRXfbjTXcMK8r6grhS-ZDWebA3qoR1SYeAz_Zc_xDQzxZ8Kc5AsqeQNAyNm4irbY2p7iNyN9Tx0h-mjd59oWkSoH5F_3ALdGqp1-Nn9kjMDHcMgvAn9DQYzXMiUeymOt4uwqZOADa22XHF_9QoN9kggFuUkA6L-dlpF9tamBv4li_KhDe5eK6Gnzj8D5VyQxoB8TnlXCPX3ttZUoCBE8hSsIf7lTizXrvcpEiTVyRms5hs9OeVHZ4D_iICMr2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c10375a07a.mp4?token=vtd3vU4DZlix0o0SZe0Kjmb4BTYuhzRn1aZwFannZXLlz1XvODr2oUKmPrAa57h2e91OLmjpobo99gZgoYIg8IixRXfbjTXcMK8r6grhS-ZDWebA3qoR1SYeAz_Zc_xDQzxZ8Kc5AsqeQNAyNm4irbY2p7iNyN9Tx0h-mjd59oWkSoH5F_3ALdGqp1-Nn9kjMDHcMgvAn9DQYzXMiUeymOt4uwqZOADa22XHF_9QoN9kggFuUkA6L-dlpF9tamBv4li_KhDe5eK6Gnzj8D5VyQxoB8TnlXCPX3ttZUoCBE8hSsIf7lTizXrvcpEiTVyRms5hs9OeVHZ4D_iICMr2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اهواز رو امشب بد زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/alonews/137110" target="_blank">📅 02:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137109">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBI_gbPEoSW0oD5P0Eg3hu0lxMdZLgFkY66Ji9Uu9gM5RIlK52XvdvfXr0N3XaY_kOoSe5yPsbN6nq4VUsdExthPGr3NJyEH-aqczf-bPt9gf5av2NsALO6cgk76f3vcyp83G2Wz_zYQDBHObXxKFf6pEBWAbZINM3EhwvUdwAgUBGTzXg9Pa3cdRpIZNv7BiFqXKmd6faFqAjxZb8fb_tNu4thxYHqOrbxqMR60Nr9_nu4-aJ-kj29J2LP84uVf5b819U0Oe_luLy2zacpi5EMJxpP6kQ22fKzs7y-HvYS1ORWD_E8cxP0GzPu4-Q_e4rv9TBXhODgMoV7yIHtsrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: دور جدید حملات شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/alonews/137109" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137108">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g44Iduizal35rbzyoErik4WcTBTIJqOmCtbP3mDACeYd2cpZOHGANTx_0GWi_TUn7RZfUKjGbJCG4oIcRb-JRjhZCnsmL_uUuH6My09eZHJHiRz095Tnj5ACFFua-jIG9KmZxU6Tn4PA0kDLhZ2AZMLlQfbVzBHY8x_SEfPyfFMSpF47DRfwn3e_CYdygxs7GXMiyssLnhFAMHHA_QONkR-jo-cDkClXQhbnFJofpucLZNqWrkBSe2qXMjbKWbamzCraDpn_5jDA-aCCj7fSY2cVFI7evZ2bsKuhkfmK_F5hLXIcrmETMPZYhgZ-ktnv8uT7m94g7BDRG7I9EJZemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات امشب به اهواز با b1 انجام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/137108" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137107">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بندرعباسم زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/alonews/137107" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137106">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62de7a19f2.mp4?token=aBLJtHEA-B_HlBKVX-Pd6s_i65ElFuPiEMCPAD2ICH57ReWZ9Ox0BnSmKS6Ru5l2vWIhFcZtX3tSMneJiIcNi_Mp0FxC0Ke9hvr2vhhQBqQSiF8PyoQQ9aXdvZ5PlVPObxCf1Zf5Et8MWAn-TqdtsX_4cqM7qPTp9wIKx1WZpKqUnIuiw5xOHxpwKefVDIxe5Wf5LWM7b6AoMiMVbFsm0HO2P4-W5jgB9VcbVFtGbJ2ScAh8KMRzrD72SbVePrFQTLXHLX9g2Wd1_HYZTWL94sWezFdLKqt87VZJ2el1sUeY5Y8eLirh9shzYpucPLrq_feEtZIethojj-8RLrBCiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62de7a19f2.mp4?token=aBLJtHEA-B_HlBKVX-Pd6s_i65ElFuPiEMCPAD2ICH57ReWZ9Ox0BnSmKS6Ru5l2vWIhFcZtX3tSMneJiIcNi_Mp0FxC0Ke9hvr2vhhQBqQSiF8PyoQQ9aXdvZ5PlVPObxCf1Zf5Et8MWAn-TqdtsX_4cqM7qPTp9wIKx1WZpKqUnIuiw5xOHxpwKefVDIxe5Wf5LWM7b6AoMiMVbFsm0HO2P4-W5jgB9VcbVFtGbJ2ScAh8KMRzrD72SbVePrFQTLXHLX9g2Wd1_HYZTWL94sWezFdLKqt87VZJ2el1sUeY5Y8eLirh9shzYpucPLrq_feEtZIethojj-8RLrBCiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منتسب به اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/alonews/137106" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137105">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اهواز زیر آتیش سنگینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/alonews/137105" target="_blank">📅 02:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137104">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
اهواز رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/137104" target="_blank">📅 02:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137103">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036ea5904f.mp4?token=Un1h5JlOGr87ENav313pF-DQIJKzSfOEFjG_zWShNi0QupeavNlsI5O6dLNjhSc6gfwwqpyxhiVeAbMGvOuqXwbVt9SnqUQ0QOOOQn6lsy7bHK6-OwVitWCx-8vAnQKFOzdBRf6cnhHCa1-LvZ8fhhASLyvmQphgyZAwU5n9tS_ZZZwBE0lAbq5U45SXy_jJw5MzoUWjaH1VkeT50J3tV-E8cS5EwAVMb_tIy3UMvscMZLOTNOltWjRyVFqFqveyGPEtFkcAnLDuMUp1Ew-35OiyVOzArGInKnNpwA6LT2iZIoKCqVmkYvxmB4JMxzAz2l5xdsyugHRjG_H3SXjcjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036ea5904f.mp4?token=Un1h5JlOGr87ENav313pF-DQIJKzSfOEFjG_zWShNi0QupeavNlsI5O6dLNjhSc6gfwwqpyxhiVeAbMGvOuqXwbVt9SnqUQ0QOOOQn6lsy7bHK6-OwVitWCx-8vAnQKFOzdBRf6cnhHCa1-LvZ8fhhASLyvmQphgyZAwU5n9tS_ZZZwBE0lAbq5U45SXy_jJw5MzoUWjaH1VkeT50J3tV-E8cS5EwAVMb_tIy3UMvscMZLOTNOltWjRyVFqFqveyGPEtFkcAnLDuMUp1Ew-35OiyVOzArGInKnNpwA6LT2iZIoKCqVmkYvxmB4JMxzAz2l5xdsyugHRjG_H3SXjcjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فارس: الله اکبر جنگنده تو قشم زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137103" target="_blank">📅 02:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137102">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=eTMRno7VhsSHrTyP9bXbHDT_OnWkkCJq1WUW9RzWTdo4LNA5Dp4YH0EsLikeoUXFCzFhdJq1dsBpL1HvFxZGsBeLLG3KyyNeK1-QMdWrFxI04gNb-WPw26ZmD386n3NmfZLy49CHx29NI31VjE2VXBBGjeOmgKuN6R-DRB81Oj3FpMt5imMCUDhBKLCfGBPWI8xg2gQhhqptvyMb8DOGE2FFT7uroHePzO64kGtpAimiOCfyLxEk7VElOcRxQ32YiNPSwISscQITjtiQ5NnHbYGHVhlsZ4H8nhHjk2bT6gvGzPH0beNGD2E0qK3OidiRaGBxWvBbrjUnSBZzegwB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=eTMRno7VhsSHrTyP9bXbHDT_OnWkkCJq1WUW9RzWTdo4LNA5Dp4YH0EsLikeoUXFCzFhdJq1dsBpL1HvFxZGsBeLLG3KyyNeK1-QMdWrFxI04gNb-WPw26ZmD386n3NmfZLy49CHx29NI31VjE2VXBBGjeOmgKuN6R-DRB81Oj3FpMt5imMCUDhBKLCfGBPWI8xg2gQhhqptvyMb8DOGE2FFT7uroHePzO64kGtpAimiOCfyLxEk7VElOcRxQ32YiNPSwISscQITjtiQ5NnHbYGHVhlsZ4H8nhHjk2bT6gvGzPH0beNGD2E0qK3OidiRaGBxWvBbrjUnSBZzegwB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جواد اوجی وزیر نفت دولت سابق رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
🔴
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
🔴
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/alonews/137102" target="_blank">📅 02:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137101">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ به اکسیوس:
جنگ جدید با ایران می‌تواند از عملیات خشم حماسی که 40 روز طول کشید نیز بزرگ تر باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/alonews/137101" target="_blank">📅 01:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137100">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgV6Wl9BqTQM3BlkCQSwAYl1rUK3t31GphFMfVsJnfObVT0-hsxTeyZJxREe7jtorsCOnb7E5hU2S93-QpKn-Zp8uYgJPCoz9PTPwGST-NKRK-vdA0qgBqwifDL2Dy3TP1mUVsISxyWipspTR14DgDmJW0Yap3o4EkLucNEhCkCYbNk3sCAv8P5TZj8MSVuKvkrVZPkUej6ZTDXZqRW3CmDX-9kLrf5foZkhYpQDPCBdFV4d8G3YLdk1yJMLxn6VRkneZiK4NgwMoAo_tlTCAzoBPbEeG4swUpJGBaEu74F7j8wVYL_ZCDXwftcjunD1hbvZaEYy08z4xlxa-l9eLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ
:
از این لحظه به بعد، هرگونه خسارتی که به کشتی‌ها، کالاها یا هر چیزی مرتبط با آن‌ها وارد شود، از طریق وجوه متعلق به ایران که در حال حاضر در اختیار ایالات متحده قرار دارد جبران خواهد شد.
ممکن است این خسارت‌ها قابل‌توجه باشند، اما با وجود این، این اقدام عادلانه و درست است و باید انجام شود.
از توجه شما به این موضوع سپاسگزارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137100" target="_blank">📅 01:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137099">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/137099" target="_blank">📅 01:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137098">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkZC-0pJsSLdcOIsWcUkp67C-rVxe7-NREddP52CYjeZ8OMdHxM7CfSwq6EcLl__0TUB-sLqfCpSMMeuiYS1Hz2P6Ujqefamzt3tNGVovO_97qjVCGYX3884WFnZibkI3uJsxCnxGurcb2AN2cJ5l5CIo2xC5kO1LSZ-OQTV3zgfaituka8RXRHOUD5mF4oQ5miZHoPnW2iBqDzjquRU9tG5uRAdGPL3LXyUoDAXQkmuk1fg98E8zcHTSgf8VPp_D5SsFtHDDzzyI2urtjnJgrG45woXdbC-Lf_BHtMJ9qilbAytY6ah-RGRWXM6aJIdCeHgg2tFk9q3AoLbP2b6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
/
بمب‌افکن‌های B_1 در مسیر خاورمیانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137098" target="_blank">📅 01:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137097">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
حال حاضر ۸ سوخت‌رسان بر فراز خلیج فارس در حال پرواز هستند. به نظر می‌رسد سبک عملیاتی بزرگتر و متفاوتی در حال انجام است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/137097" target="_blank">📅 01:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137096">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وال‌استریت ژورنال: تصاویر ماهواره‌ای نشون می‌ده جمهوری اسلامی روند بازسازی تاسیسات آسیب‌دیده در حملات هوایی آمریکا و اسرائیل رو با سرعت آغاز کرده.
🔴
سرعت بازسازی این تاسیسات نگرانی‌هایی رو درباره میزان اثربخشی کارزار هوایی آمریکا و اسرائیل علیه جمهوری اسلامی ایجاد کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/137096" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137095">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
خبری منتشر شده در کانالای تلگرامی تحت عنوان تخلیه برخی مناطق در اصفهان کذب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/alonews/137095" target="_blank">📅 01:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137094">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🙂
وای خدااای من برید تاریخ سه روز قبل جنگ رو تو این کانال ببینید دقیق درست گفته بود آمریکا میزنه با ساعت! هم قیمت دلار و طلا دقیق پیشبینی کرده بود  چند روز زودتر همیشه پیشبینی میکنه! الانم تاریخ حمله جدید اسرائیلو گفته
‼️
🚨
نمیدونم به کجا وصله ولی از همه چی خبر داره بیا خودت ببین
👇
👇
💵
@Tahlilgar_Jang
🪙
@Tahlilgar_Jang</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/137094" target="_blank">📅 01:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137093">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
یه موشک رفت تو تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/alonews/137093" target="_blank">📅 01:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137092">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=oV1jVraStwuogNmN4zJxA701W3Jikv95dgR89Xc5Y7bGbZujJ0l1NpyTY5tHFDly4uplORkpj0qC-EQB1Yv83x50hdcBhuFRnMnXGBBU80PWjGJjLe2vXYpOjMSFuDJvsOShawX8UNdAIKKd55KkbZnBhJggdFK8x42Ri8qIhn6VKFGLRATd501kE4SOOV9elPb59kxFhH6R_uFR3F_uQJpUP1vdbScijPpSC0I-Hq0j3sETbLi2mGXC5EcEkSUb2E9W5W4qgyJYLm35CnSlkvbrDaVRSkpEF_oQ8QPWij8wKjnqcj1hn68GDJRA2YV9B9-JB7wBDcAtZ4A0UEpYmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=oV1jVraStwuogNmN4zJxA701W3Jikv95dgR89Xc5Y7bGbZujJ0l1NpyTY5tHFDly4uplORkpj0qC-EQB1Yv83x50hdcBhuFRnMnXGBBU80PWjGJjLe2vXYpOjMSFuDJvsOShawX8UNdAIKKd55KkbZnBhJggdFK8x42Ri8qIhn6VKFGLRATd501kE4SOOV9elPb59kxFhH6R_uFR3F_uQJpUP1vdbScijPpSC0I-Hq0j3sETbLi2mGXC5EcEkSUb2E9W5W4qgyJYLm35CnSlkvbrDaVRSkpEF_oQ8QPWij8wKjnqcj1hn68GDJRA2YV9B9-JB7wBDcAtZ4A0UEpYmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یبار دیگه ببینیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/137092" target="_blank">📅 01:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137091">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">💢
فوووووووری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/137091" target="_blank">📅 01:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137090">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
گزارش‌ها از پرواز جنگنده‌های ارتش در برخی نقاط کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137090" target="_blank">📅 01:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137089">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
از اهواز موشک شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/137089" target="_blank">📅 00:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137088">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
قشم رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/137088" target="_blank">📅 00:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137087">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کانال ۱۳ عبری:
نهادهای اطلاعاتی غرب بر این باورند که ممکن است ایران آغازگر اقدام علیه اسرائیل باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/137087" target="_blank">📅 00:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137086">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
تسنیم: دقایل قبل، اصابت ۲ موشک آمریکایی به محدوده روستای مسن قشم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137086" target="_blank">📅 00:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137085">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نیویورک پست : روز چهارشنبه، یک حمله دیگر از سوی ایران توانست سامانه‌های پدافند هوایی آمریکا را نفوذ کرده و به یک انبار سلاح در نزدیکی همان پایگاهی اصابت کند که سه سرباز آمریکایی در آن در اردن کشته شدند. این حمله منجر به انفجار شد و در نتیجه، یک "ابر قارچ" شکل گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/alonews/137085" target="_blank">📅 00:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137084">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ارتش کویت: پدافند هوایی ما در حال مقابله با حملات موشکی و پهپادی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/137084" target="_blank">📅 00:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137083">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3U8vkPfWK1hSUQeI4P11L0NMzB5Zz69ZW_8WB0pe_Yjnfsmr4DUSAquOiO4DuiD2X816smqd9ikaYxGV2YiTd9ga7xBI-rv1nRNUmg0-EjzQfu2FYdLXE-SJI_ilVlF9vdjhFvSSVOCB7khKiTPj300LOW4v9Avn8pofYih7r4GH-B_ZanhDmiJrb9zZIs1m0_RgDjevtVldPF9oYyp_3nrAu1glEI9uIrIZFgbZ-QOGFTiOD3TZhpGxcRJlWjC7F7CheJX98PFkgmF6EPKMe2h7nwbyruYpnkm2Zs1hJa7qnzrhddLfMoRDYmG19l4gJakCpx9vyIFn49Rzh6r1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی به قلعه‌نویی:
به عنوان یه مربی ایرانی کاری کردید که واسه اولین بار تو جام‌جهانی، از هیچ تیمی شکست نخوردیم و این ارزشمند بود؛
🔴
امثال فردوسی پور طبیعیه که شما رو تخریب کنن چون ذاتا خودتحقیر هستن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/alonews/137083" target="_blank">📅 00:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137082">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxVsQiBRZwY_ojXudvWtmua-jN2eULQtsWnidbnYJbqYhf4Uiovgn0O8Ch709f89C0SsAIY8KBywJPxJPvJyHlsjgTZjtc2g09bcEqPMoVOu578sVNsdXKYYp5qJ8IKR3hseSArjzPxiLKTZCQIOfKZjdm-ryBSADB4MVJN332rweCtzsXzwGJ5i1JoyJiae1NmxN-izHcSkImf6g_W5pIertqIY68zkIcc5jJBXwWhxj6HIFlzXUYhNVMTuAeC4J39p8sN7Ea5pmx7RCdq5yZjxLvdxo9rM2rR-PMj-mOD9MqnglR_OQHSEEejSqMwojp47-9dWxqqlopFRPQSXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تهدید انگلیس توسط ابراهیم عزیزی برای تصرف جزیره دیگو گارسیا
🔴
دوران سایکس–پیکو مدت‌هاست به پایان رسیده است.روزی که دیه‌گو گارسیا را نیز مانند دیگر مستعمرات خود از دست بدهید، چندان دور نیست.
🔴
بریتانیا بهتر است درباره شکنندگی مرزهای خودش تأمل کند و دریابد که توانمندی‌های ایران بسیار فراتر از گزینه‌های نظامی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/137082" target="_blank">📅 23:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137081">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxIxZ7PFzr2FJns9fyJXPfvp6Bhw1A06zihKbFjlNGSCifrxZgWhceHDQEtEuV7WHdpZTJLoK0M0-roRPdaK8aTSCQkE4adV-9XjiyRYlgWm_L3pothoyM7RiCjICkyf5JtTMG_Udx9i01QkULIg2EeFHNFaEWc-wMXy-QtnHw2pdmtTOFyd2TnabFHzIJY6mQCjz4IXcASzGl_ZaLb2XekrsHOVr3NRgb3PdRNKpCrF0thU77H2BKKw0TZTD2npZTe3QapHdWrwyrSO2L24d0GTzkSE0pPqk5PXYzuaSpm5r8rxFd2-wkVKL4D2rWVRJQXWEEPpnLUOKW3HNXsuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تعداد زیادی پهپاد رو به سمت روسیه فرستاد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/137081" target="_blank">📅 23:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137080">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtvVxgXpivjCnVm_uamuKh2VXLKBG5e0r44DDI1cxs1hqSW4MZJOmgJQWhZ8sPFx1dAy1SR6pCJVkn2ji2wDvx94kxOwl4BH6-xVFzXz_WILelSGvYtM5ICCWDEy8YpyIQcAMlkh8We89nwqQwKd-cjL9gn386SE3n_m3PQYKhBzO4NtHTf8cO3KuLcYKQt6GfZ4HGH_J5ikkqBq-oY7ofF3Z3Z8Q4_TU8VXf4IUmwBLoTBi_gn6Xug5BVNgoJXu_kJr5GugaNZj_qpr0qNuK4vLQWYyyhS2YXPBRR4PHVb9DEFqSY-PPl7LX5udlCjibmHkbFkvyiYf4khpoFHoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا انقدر هواپیمای ترابری داره میفرسته که تو آسمون ترافیک شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/137080" target="_blank">📅 23:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137079">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwrkoSnyiu1FXElh8MBoGxFtVhvX2PKrQmHKm5iDAJzysp5Y-wSyN5L9t1pSqHamBCjb-hQMzLZPXhJI1yFR16jYvxaoEHzB6HpLKt04nOtMKCsf4xem1Vcul6gf1RODBTvclSq0rGeNDFeDfwELaoZLv4sRdnVUV93yKt6zwo-NRQ6rE4cVpgJMyD3EkElW231lwfHzWMmaGfZtGZzx61-krXRxkqXUD7lFHxZH3KSBWTd0LoJYmlgHFq_vG0JGnV1is1VgyH_i4KxyjHRoqirD-tpZ0vNHH1n1AouiCA1jJjnTJWuWwOedeYORRdk3twYcF7yeD85yOz_CEFJEXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت مالک شریعتی نماینده مجلس بر علیه پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/137079" target="_blank">📅 23:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137078">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd81f5131.mp4?token=aqjQ3s66MFDOA2z7BgQMOmCUWpmM-1F64q3kpwq46mizxtVbf3uqcBqE3NsUq_8TTdyw1M4AW1dwmlfTBw_dsbRzwQsU1lvtOet5WLrMDtS5L7aKoFty90O9yElYiZYs1Z2pr-7WoKnCtiKPeouOUA9G4zHO5cZa4mV8SmCV2FJwOTUIbrXd02hhakxo1Axskcx010_gOJbGV9y8wHnQ8KmygR4JmQzlOYPGAYv-scktOI9GHTjOpNfast7VoijMaw2HTR8zoWUQptZ7sF6bDrfCPUJeLJu02y0YRpY4nKfQ70Fsc6iRpgoSXaayFetd-iNZsSsFIWN7ZQCLXtC3LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd81f5131.mp4?token=aqjQ3s66MFDOA2z7BgQMOmCUWpmM-1F64q3kpwq46mizxtVbf3uqcBqE3NsUq_8TTdyw1M4AW1dwmlfTBw_dsbRzwQsU1lvtOet5WLrMDtS5L7aKoFty90O9yElYiZYs1Z2pr-7WoKnCtiKPeouOUA9G4zHO5cZa4mV8SmCV2FJwOTUIbrXd02hhakxo1Axskcx010_gOJbGV9y8wHnQ8KmygR4JmQzlOYPGAYv-scktOI9GHTjOpNfast7VoijMaw2HTR8zoWUQptZ7sF6bDrfCPUJeLJu02y0YRpY4nKfQ70Fsc6iRpgoSXaayFetd-iNZsSsFIWN7ZQCLXtC3LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قسمتی از ویس دادگاه نوید افکاری: بهش میگن در یه فیلمی دیده شدی! نوید میپرسه خب اون فیلم چیو نشون میده؟ اون فیلم رو به من و شکات هم نشون بدین. میگن LCD خرابه. بودجش تامین نشده!
#نوید_افکاری
🤔
لعنت به جمهوری اسلامی، لعنت به حرام زاده های طرفدار این حکومت قاتل که جوانان زیادی رو با اذان صبح اعدام کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/137078" target="_blank">📅 23:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137077">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72219f7361.mp4?token=BdiFn4ngCgFjmKWLmk6tO3wAObaR4nemH27DwcthNdbGN6_EHozY2kx0J9u2MhV5Agh65mz77FPydZFDiNaMt_nGc_Tnjxd0tKGs-aWG6LZ4ij0H8qxa9036H6rrsP3u8bsBTciVWJCY8wD0jo5RQcxjkkbaSI7nvF5TBmARCcAe4Hhdb6U43Gsfft9oldzPSgn8uOJ8TjcdSZ90gR5-wuUUNJ62KjhbF1IPUbR-ndxuFn4Nu_9CFeBeBYzhhTpVY-2pNkT7Lb4xHpJx7u09L9KzAZds-Zi0J10ZAJkc3XPkoUgN4Imf7Xw2xU0yFb1A0rgl0NZiPaZi_9OmyzNfXkJsuvD7CjHc328Z3sV2iEGhr4HEfBX3V2KUatujxZ46N9nzvsT4TElkxTKNhmVqlN-YK5hT0v8yAvmeEZQ4gkNcZeAXIaI4wgeupmebCGakbIT4EED2FQ7Oa3Ao4GfuSv08UUB2ObLOkW9g7Nrp1m3VD1qomDx_WjwfeeY_oD-r2RimEuybYe7mMSkx3WbunmwyMYg4Zb3nyrYKfUparO0iyf5BZJKjc52A5GpzoUQ-jCDwJ10xt589GvubLwGDE-lv_DK_R234V0bb1UCb3T7UYELGYShoHcHq8PeUMsxtzEHzGdnjws5FHDkFap2bruXqSsLTeBdc4QvZ_jTCH5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72219f7361.mp4?token=BdiFn4ngCgFjmKWLmk6tO3wAObaR4nemH27DwcthNdbGN6_EHozY2kx0J9u2MhV5Agh65mz77FPydZFDiNaMt_nGc_Tnjxd0tKGs-aWG6LZ4ij0H8qxa9036H6rrsP3u8bsBTciVWJCY8wD0jo5RQcxjkkbaSI7nvF5TBmARCcAe4Hhdb6U43Gsfft9oldzPSgn8uOJ8TjcdSZ90gR5-wuUUNJ62KjhbF1IPUbR-ndxuFn4Nu_9CFeBeBYzhhTpVY-2pNkT7Lb4xHpJx7u09L9KzAZds-Zi0J10ZAJkc3XPkoUgN4Imf7Xw2xU0yFb1A0rgl0NZiPaZi_9OmyzNfXkJsuvD7CjHc328Z3sV2iEGhr4HEfBX3V2KUatujxZ46N9nzvsT4TElkxTKNhmVqlN-YK5hT0v8yAvmeEZQ4gkNcZeAXIaI4wgeupmebCGakbIT4EED2FQ7Oa3Ao4GfuSv08UUB2ObLOkW9g7Nrp1m3VD1qomDx_WjwfeeY_oD-r2RimEuybYe7mMSkx3WbunmwyMYg4Zb3nyrYKfUparO0iyf5BZJKjc52A5GpzoUQ-jCDwJ10xt589GvubLwGDE-lv_DK_R234V0bb1UCb3T7UYELGYShoHcHq8PeUMsxtzEHzGdnjws5FHDkFap2bruXqSsLTeBdc4QvZ_jTCH5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل، مایک هاوکابی: وقتی شما، یا آقای مامدانی، می‌گویید که بنیامین نتانیاهو مرتکب نسل‌کشی شده است، یا اینکه اسرائیل مرتکب نسل‌کشی شده است، این یک اظهار نظر احمقانه است.
🔴
چرا؟ زیرا وقتی کسی مرتکب نسل‌کشی می‌شود، تلاش می‌کند یک ملت کامل را نابود کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/137077" target="_blank">📅 23:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137076">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: آمریکا بداند اگر جنگ را آغاز کند، گستره جنگ فرامنطقه‌ای خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/137076" target="_blank">📅 23:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137073">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed11b92b0.mp4?token=cFZ80yaCh3P0G_kRiwa9Tj9q4h1s9GEVEDbCVTPfKbbMmVoVHkGjG6A6xJnC8uC6Vq6UD4A-RpjwYrx_g5zfkWQRhbN1_KP5jdaWvup2yo29FHyITENdQj-niBRQ6COrxhkGn4EwAiB201l0kNTeMojhg7mBywTXl6RWz0M8Ale-jwLgqy8ZFU2mbXjsLj65jxLjTqXhlY-XuPj9uUIlp98q8Sazra333dZfBb3W2YK_wyZnanj6Xo8C2Hah4aCxu3Sk2pZmg4IJ5eZR000WH6EeUNtH8kXIVGPhOBI1GiX4rP88BbjDuY9wi_4CqAMFSVLIMhEzxSRVAJGwzPKZqJBJKFzvB5jwxhDOHy-ODnjbsczQrlMdBvmiLPtnqQZLX_SPyM7vRRulBUFMoWGOrYARYjqWnsgSXh3XjIULcEZKeg-1Tf4tOQHCmn8zuwY9lVMasRKGLCIrdIocCFcpNHTtK4w9qBqDzdSKRwgF27N5fheA0PzvT5VwLQB8kB74fTBqfaNwBQwsVd2G2-coBxaksVHLwojVcG1PvnE83taUo4iZcHFdi3nX8Wb-9_TUdfKikV9JM6Ig0srg7uKn5o6SdWMw6Ex5-egiVYzZf2aMWS5LEzvcbJOSbzp6zpkOJE74OQ0XPk8-3ZtnieVdWDTf0yV3DoUgZTHkme0TCdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed11b92b0.mp4?token=cFZ80yaCh3P0G_kRiwa9Tj9q4h1s9GEVEDbCVTPfKbbMmVoVHkGjG6A6xJnC8uC6Vq6UD4A-RpjwYrx_g5zfkWQRhbN1_KP5jdaWvup2yo29FHyITENdQj-niBRQ6COrxhkGn4EwAiB201l0kNTeMojhg7mBywTXl6RWz0M8Ale-jwLgqy8ZFU2mbXjsLj65jxLjTqXhlY-XuPj9uUIlp98q8Sazra333dZfBb3W2YK_wyZnanj6Xo8C2Hah4aCxu3Sk2pZmg4IJ5eZR000WH6EeUNtH8kXIVGPhOBI1GiX4rP88BbjDuY9wi_4CqAMFSVLIMhEzxSRVAJGwzPKZqJBJKFzvB5jwxhDOHy-ODnjbsczQrlMdBvmiLPtnqQZLX_SPyM7vRRulBUFMoWGOrYARYjqWnsgSXh3XjIULcEZKeg-1Tf4tOQHCmn8zuwY9lVMasRKGLCIrdIocCFcpNHTtK4w9qBqDzdSKRwgF27N5fheA0PzvT5VwLQB8kB74fTBqfaNwBQwsVd2G2-coBxaksVHLwojVcG1PvnE83taUo4iZcHFdi3nX8Wb-9_TUdfKikV9JM6Ig0srg7uKn5o6SdWMw6Ex5-egiVYzZf2aMWS5LEzvcbJOSbzp6zpkOJE74OQ0XPk8-3ZtnieVdWDTf0yV3DoUgZTHkme0TCdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون بمباران غزه توسط جنگنده های ارتش اسرائیل
🔴
ارتش قبل از این حملات، اطلاعیه‌های تخلیه را برای مناطق مورد نظر صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/alonews/137073" target="_blank">📅 23:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137072">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f877915d27.mp4?token=UJ_kB1Gk2ap6RxH3v18a8Z4QpEN07Y9MkUcW9vDyakkmQLN_VOVDNBiZiiu65zKFmd9gEB6MFc5qmuP7Sdg0XdKiFFFlIMBmdRAoURbCnWyCh3SMPCNSQeBrG8MPCmz7-lW8azWI3wmmgRGLewkjjLxrWOxFaM_lY2e122_5uR1diMHqDFAJrZKAmU7OlQnF2Kx3uCGU2YOO-kgdoaUCnaHQoX2572ZNy-TQPt77hWfJnvNQBQbeTiGOB5OiJZz-pGxwftY0fpbhDuh7cNCdnl9LjXuEG1CPlceftjvWKhSkWIhbzelPNbvRYmn9BLxSltspbcZJ2sVg0ZIgy4pqkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f877915d27.mp4?token=UJ_kB1Gk2ap6RxH3v18a8Z4QpEN07Y9MkUcW9vDyakkmQLN_VOVDNBiZiiu65zKFmd9gEB6MFc5qmuP7Sdg0XdKiFFFlIMBmdRAoURbCnWyCh3SMPCNSQeBrG8MPCmz7-lW8azWI3wmmgRGLewkjjLxrWOxFaM_lY2e122_5uR1diMHqDFAJrZKAmU7OlQnF2Kx3uCGU2YOO-kgdoaUCnaHQoX2572ZNy-TQPt77hWfJnvNQBQbeTiGOB5OiJZz-pGxwftY0fpbhDuh7cNCdnl9LjXuEG1CPlceftjvWKhSkWIhbzelPNbvRYmn9BLxSltspbcZJ2sVg0ZIgy4pqkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منوچهر متکی: نامه‌های احضاریه ترامپ و نتانیاهو به کاخ سفید رفته است
🔴
آنجا امضا گرفته و از طریق کانال بین‌المللی به قوه قضاییه برگشته است.
🔴
اگر در دادگاه حاضر نشوند؛ حکم غیابی قصاص برای ترامپ صادر خواهد شد؛ صدور حکم، تنظیمات آنها را به هم خواهد زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/137072" target="_blank">📅 23:30 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
