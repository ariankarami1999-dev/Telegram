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
<img src="https://cdn4.telesco.pe/file/U3tXZOi1J_sW_ACPha3F830QfLfnxHjX9PquzIYjr3-jMZOvXdxB1qThZhMPe9NYdQewQiyPmu1rVwTtXDZteMMhuSdZSQLSDC2VXRBnTCwblPyCFEhAQ_V-md89IO7xKIjVa5YclXIj0SWbKtIhFxdT8U4Y6GacZ3eE-nthoAL1GJmD_diIQEJwXP4mTwiI_Y2Z80bGvEaCM3MAt2f78q43jwgQkVbCfLZDMVfdrzDClU0iXThRVD2vR0-0dz9W32zpCWh31Aw5lbV_f52UpjaHlsElomEmh5lAoTwnZhZmbuGdzS5j8m9Att4OlSlMzmubWjXmoZT-9lQQrxw0Cw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 920K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 03:14:36</div>
<hr>

<div class="tg-post" id="msg-133345">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
🔴
این چنلو حتما داشته باشید زمان جنگم پروکسی هاش همیشه وصل بود  @proxynab
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/133345" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133344">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری/بر اساس گزارشات، ستاد فرماندهی نیروی انتظامی اهواز، هدف یک حمله هوایی قرار گرفته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/alonews/133344" target="_blank">📅 03:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133343">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انگار نتا یکم ضعیف شدن  اینارو داشته باشید تا در صورت قطعی متصل بمانید
✅
پروکسی |  پروکسی | پروکسی پروکسی |  پروکسی | پروکسی پروکسی |  پروکسی | پروکسی پروکسی |  پروکسی | پروکسی</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/alonews/133343" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133342">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انگار نتا یکم ضعیف شدن
اینارو داشته باشید تا در صورت قطعی متصل بمانید
✅
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/alonews/133342" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133341">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37792480c.mp4?token=n50fFsZp0pGpVzHMNPTM_rMdACl3lJOr31x9L8SEn0nZfms-ZZj9Qb3AoaDyuPxHI2sccPQ5eYJvTD59Z6Yt_YzP8_p_4veYoCFiMBtg4QNUHMaKcb9GO3bII9pZ4pcwlFNEYzVfDcESg8FtJiZmZ08C3FEF9JwKcIYTZNmd43JkX-iIZlogVAyqa18etLmtqPf891Sf5vCfWKqBWQqZCLwrb6VKOkbV2yhIdQepFEz531-RKuIjAdCRLjfcR7Zo-wG1SlUZVBwLET1b2d8A66BD5ZGfYXVIIyUdbBp0EPMr799vOji9WYAYZH45Rl6jiAG9TNlUiuZMaCV_mtGYvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37792480c.mp4?token=n50fFsZp0pGpVzHMNPTM_rMdACl3lJOr31x9L8SEn0nZfms-ZZj9Qb3AoaDyuPxHI2sccPQ5eYJvTD59Z6Yt_YzP8_p_4veYoCFiMBtg4QNUHMaKcb9GO3bII9pZ4pcwlFNEYzVfDcESg8FtJiZmZ08C3FEF9JwKcIYTZNmd43JkX-iIZlogVAyqa18etLmtqPf891Sf5vCfWKqBWQqZCLwrb6VKOkbV2yhIdQepFEz531-RKuIjAdCRLjfcR7Zo-wG1SlUZVBwLET1b2d8A66BD5ZGfYXVIIyUdbBp0EPMr799vOji9WYAYZH45Rl6jiAG9TNlUiuZMaCV_mtGYvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری که دانش آموزا صبح باید برن حوزه امتحانی:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/133341" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133340">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
انفجارهای پی در پی در جنوب کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/133340" target="_blank">📅 03:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133339">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">💢
فوووووری/پرواز جنگنده بر فراز تهران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/133339" target="_blank">📅 03:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133338">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فووری/سی بی اس: حملات به تهران هم‌میرسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/133338" target="_blank">📅 03:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133337">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/133337" target="_blank">📅 03:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133336">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7sVCytAoU85DGm_Ctr0tqZLkS-pPEpXHyN4EdWklkstZ3VxPDTkX5i5iJ2seqPV3nAd_4vMmr9rsf6F3_KCq3RYwEZIabZsBuzS8DRJ08tLO1OZNsmZlD2OCzJLgFKKQlylGwiP1H2FC-ScUPq_lDXqXf2o6Zr8J04-rMv74_VPG2YgnXN3ZLzRtD_5sXih_Fp7zFCIV7VUuy0hxqHOCY4XhAwnbxkwkieTojf3R84xuy1gtE_Jo95n7eWqyEjm-8j0UW1p334Ktvtu2a-5sUEgbavtNmjfNza8cYUxlpvUH4NNJ42OtBDILraTy0zsjhl0kgVACXYRRafeN55m0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/انفجار شدید در بندر دیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/133336" target="_blank">📅 03:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133335">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/133335" target="_blank">📅 02:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133334">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/133334" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133333">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری/حملات به تمام خط ساحلی جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/133333" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133332">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c2812772.mp4?token=qH9v7jDAjMWKuy2LMdP65JSlh4Rrbv_8i9Xccf1zwh_35-4p0SzjnVSQzAD76-9cvLbkHNypL7Sg-RcFXA3JnmmU8eZ2f2EVAUqsG0H3ZISGgrTLP6Ru3QGPgHsrt1u3RFEejVecehreHMdqyveLJ7i39hHsh4Rs_b6PH22p0rbWIrjPXPLucyUTkSj_AipY6S6sKiwmK9pQmFP9D52bihdWufwRuoHFUFTfYodFMCoTqaqkJ5jH_2b5jMT6Rt3ezLka50pcmkKj8AFLbE59OVc_ahhVAPUUfPWyCvLKjYprAXtoouamR-cPa8xFNUOdEIB_NeKlh4APtclAyFsp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c2812772.mp4?token=qH9v7jDAjMWKuy2LMdP65JSlh4Rrbv_8i9Xccf1zwh_35-4p0SzjnVSQzAD76-9cvLbkHNypL7Sg-RcFXA3JnmmU8eZ2f2EVAUqsG0H3ZISGgrTLP6Ru3QGPgHsrt1u3RFEejVecehreHMdqyveLJ7i39hHsh4Rs_b6PH22p0rbWIrjPXPLucyUTkSj_AipY6S6sKiwmK9pQmFP9D52bihdWufwRuoHFUFTfYodFMCoTqaqkJ5jH_2b5jMT6Rt3ezLka50pcmkKj8AFLbE59OVc_ahhVAPUUfPWyCvLKjYprAXtoouamR-cPa8xFNUOdEIB_NeKlh4APtclAyFsp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/آسمان بحرین، دقایقی قبل/ظاهراً مبداحملات به جنوب کشور بحرین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/133332" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133331">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری/گزارشاتی از شنیده شدن صدای انفجار در دیر و کنگان شنیده شده است/احتمالا اسکله دیر مورد حمله قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/133331" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133330">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری/گزارشاتی از شنیده شدن صدای انفجار در عسلویه و بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/133330" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133329">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/العربیه :
هم اکنون تماس وزارت خارجه پاکستان با دو طرف برای کاهش تنش در منطقه در حال انجام است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/133329" target="_blank">📅 02:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133328">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری/اولین تصویر از موشک باران تنگه هرمز
مشاهده فوری</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/133328" target="_blank">📅 02:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133327">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
تابناک مدعی شد: گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
🔴
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/133327" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133326">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9lP7YmL0dh83dWEDq7hFyL_H2iahCPAUtjFqIEERtYJX6HMV1psKRKBa_csTGkpHccgkjfkdV3wZr6Tse6hDYMVTqP2Jp9glUuDy-YjnAC2kBMbcPERUs8l0vUiTqTj7e5GQfBL9WMgORKCJDPAQeQcT-wLSc2ZRGt8f_2Yd0YeFT_8g-gmpLE7i0EyuREea4ajDLJFWRxw5V79WB5phB2dEstb0ZrhBZsd0lcGm6vb4dap9Ut9bniWo3-a2gWCF552Tae_qvBo9LM2-Vpet_MgTzRxD4trAlNaa9YpOlWlc1MzPXRRc3xRh6spDfoUbtyA89FtJ30qTrBahUkUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل :
مذاکرات به بن‌بست خورد؛ ایران یه پیام جدید برای ترامپ فرستاد و گفت: از این لحظه تنگه هرمز رسماً بسته‌ست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/133326" target="_blank">📅 02:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133325">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">💢
فوووووووری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/133325" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133324">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
فعالیت های رادیویی شدید در خلیج فارس توسط ارتش آمریکا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/133324" target="_blank">📅 02:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133323">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
کانال ۱۴عبری: پس از اقدامات امشب ایران، ترامپ ممکن است هر لحظه چراغ سبز حملات به ایران را نشان دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/133323" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133322">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLMVH5knlCyuam4L2ARcoV1a8O2ixUtB36wO18PvQdVGkjAeTv3UpQYKNS-UGte8DTKQHxIglKBSu-5jwkvJ_pFWwSBpXWpfwRC9bSu14BhXu4SKDERVGwxsy5FSN8WgkpaSM1ZNBHIy2Ags8EmC_Y94SXQohl31hcrJmj_2_gUG61kSEknDqx_ZkLByV-fNbS_u91ZLLssCuVHgiQX0JU4VkH3epr6rrmggoOOf7AjaQVuDOwJtx36tZ1aLSP_ToKsOf2gkYNAfQEE7SEXFFS0ndtxczHrLTdl0TZrialZ4PVcv9FqK9-uylOJa41S-4x9tEKG4-yhucaUtMKX0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همین الان ترامپ که رفته بود گلف بازی، بعد از شنیدن این خبر زمین گلف رو به مقصد کاخ سفید ترک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/133322" target="_blank">📅 02:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133321">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFhc_uGOb57QSAqvC_-Uv0klZhUGvKDQyOxfs4o9VjgqGquyQToTQ_nfXdiwWSv9vhRJo6dovICQXJPzHnu-T0eLnqAI29tqG3DSDlubBqN6U3sw3AyOFrqd6EjuGzKmqBcgOFgROcoKDHYJa0T5MbchuDH-EEyCGgT1GibDcxX4pDNabE86B6eLCYx4Z0PI3yw8PAkchkFXx8vf0--H-__o5xOm35nD8--72h5sIOhyIqw_MmNWiAkbNq1kW-9Y5BHh9VKPVano52SwNnlGoe-10bhsX0GzuV7R8hjtO9LLRnfJd3VnKdlufSnCvQ_Rc4Epah7-NBq2DMBKlYDp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون زیرنویس شبکه خبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/133321" target="_blank">📅 02:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133320">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
آکسیوس:
ایران ساعاتی پیش به یک کشتی تجاری در ورودی تنگه هرمز موشک شلیک کرد،
موشک به کشتی اصابت کرده و باعث ایجاد خسارات گسترده به کشتی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/133320" target="_blank">📅 02:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133319">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
منبع عبری: رهبری و نیروهای مسلح ایران مانع بیانیه تسلیم تنگه هرمز شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/133319" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133318">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
شبکه خبری آمریکایی «سی ان ان» به نقل از یک منبع: عمان اداره جریان کشتیرانی از دو مسیر جداگانه را پیشنهاد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/133318" target="_blank">📅 00:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133317">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
کارشناس فاکس نیوز:ترامپ ضربه اصلی به جمهوری اسلامی را برای بعد انتخابات مجلس آمریکا (آبان) برنامه ریزی کرده است و تا آن موقع تنش‌ها در همین سطح باقی میماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/133317" target="_blank">📅 00:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133316">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9_tv91Df3A4Qd9aLTDX3ASLfADfJeA16-zXDH5hdVw4lh34c-ChZ-RPAmMjDH6jfeYqQhaVrH7t59gvSz9KRpMdFW8-OTCgJ-ZyqBGg4K1lHgBgr1nFxw8jmJ1h-dNU4bS6gV37d2EJnxB0jXiJJGLLmCsI_0p2e3aBJG2huJLvxAXo38YMJevNatQ78S-4EY0R1F3BtDPN8GogOyeiaLJhFU5sGsg5aEmBTeAkQtbEiSARHr_5x6E5c-Y7-Izt1HdbC_QQkQSRxn5b5wReoc4yxN45uQg6dvQGTUmyXAP95R17dObnLQdyqL6mYZsm71Sy8HKWeXxkQ0MPoV7lbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری C14: ضرب‌الاجل ۲۴ ساعته دولت ترامپ که جمعه ۱۰ ژوئیه صادر شد و از ایران می‌خواست حملات در تنگه هرمز را متوقف کند و ناوبری آزاد را تضمین کند، ۳ ساعت دیگر منقضی می‌شود.
🔴
این توییت برای 2 ساعت پیشه و 1 ساعت دیگ مهلتی که ترامپ داده بود تموم میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/133316" target="_blank">📅 23:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133315">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نیروی هوایی و فضایی روسیه، در یک حمله به شهر چورنومورسک واقع در استان اودسا،  با موشک های کروز حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/133315" target="_blank">📅 23:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133314">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / گزارش هایی از فعال شدن پدافند هوایی در اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/133314" target="_blank">📅 23:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133313">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQQqqWM71mXFpxLhqy5XvJ2cG_fIygoHtVdKZ_IFcWjA5tJ3fAzb2BluDkLm2OmAk_3HBwG0QhCu3_BQjGa0BhhD1J9L1xBghqo_qSY-moWH1Fk-VdMXHsMOZygR0ZoHaVEsRj7AWM84hgx4mRYnTMtAizZCL7HAOGQ7OGC8wWOgGuAr8caRB29AnOC5XLDWlBmoF6ygsK7XZCAZmxeTFT1RUm5aafIyeOVmThREm52B1Qs_p2Kx4HBurUErCcxu9ElU-8-1wh7iNWFlUDhe0BF5SIob60JDKkz_5Yy2aJCm6N81-tVU62lW5r6eED_YtBaBOGo2F_QhPGZPheolKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واردات LNG اروپا از آمریکا
🔴
وابستگی اروپا بیشتر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/133313" target="_blank">📅 23:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133311">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obg6-e3T9TsXTmfok22vZIzIC_tC5eMGKWviTDX2W51Gny9Rne5rY6w0ggEWw3bqQgy0HyYkpCl7vKNmqV9V9qosApQ_bpB-ZW64ma6dxJ52EA6v_2mQmKninArrs3Z8RVlvBSz-zUiiEZiAr1okSuXzTq8axy2qyCK2Y49TbGthmSGDRnbyh-meJzmQ3shBk6bxcb65cSyo_ykejA9cIANS_HAx-D3G_w2Dp7xTtlhAssAq4bvhd41YniSGGgoEwcbQHSvgr3Y1U0lxAMnE1aJePe0zHXVONE_GZ-XY5XNFcg2rset2wnQCTS64uD5JhIkiosBCVauYNqsUY9K2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های کپلر نشان می‌دهد تنگه هرمز قبل از درگیری اخیر به سطح قبل از جنگ برگشته بود و تانکرهای پر توانسته بودند از تنگه هرمز عبور کند و نسبت تانکرهای پر به خالی به وضعیت تعادلی برگشته بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/133311" target="_blank">📅 23:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133310">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سفیر آمریکا در اسرائیل: سرویس اطلاعاتی اسرائیل به ما اطلاع دادند که ایرانی ها توطئه جدی کردن برای ترور ترامپ.
🔴
اونا 47 ساله شعار مرگ بر آمریکا میدن و بنظر من تغییری نکردن، اگر یه نفر بتونه رفتار اونارو تغییر بده اون فرد ترامپه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/133310" target="_blank">📅 23:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133309">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
شرکت توانیر: از این پس اطلاع‌رسانی مربوط به خاموشی‌های با برنامه و اضطراری، با هدف ارائه خدمات دقیق، سریع، شفاف و هماهنگ به مشترکان، صرفاً از طریق درگاه‌های رسمی انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/133309" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133308">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
مقام‌های آمریکایی ابراز نگرانی کرده‌اند که اسرائیل اطلاعاتی ناقص یا گزینشی را در اختیار دونالد ترامپ قرار داده باشد. این موضوع ممکن است به ازسرگیری جنگ با ایران منجر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133308" target="_blank">📅 23:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133307">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjK50ChA7WJtAm6VA_TsyBRI2c8G2axYpMUhZpjWHCNkdHQfFf3XL1OojlP0WdDrWqZBOIjnqRXZp45q68Mmgux_uXXHHPMtAVZlgNNkJK64owo63l1iXWhnv-sPMuo1CkNYpbfxzL2BNqCEMpoIAcYlT-QI0gXdriErc8EK1jgUV-LSbI0bc8CWNo1eVo1wB5Ri6BXXK9FvlayvdCSdFiOzKAtQ4i9upE4IqC1VmURuGIrgGUM2AO1XrxkfNATwuboMcg-gN4jCG_Oc1WZ5-HiG7kaY-913STMeHXYs_nsSNYmS7yI3G6vw1cAotoogPKCsh54Y5DuBLfDnqT_lGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی تقویت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133307" target="_blank">📅 23:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133306">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lG1LREhNIjeIf_mcByuvmuWjE5-J51XdR2XZyB2_-erxZD4S5DK2zLPXtbKniLgxTV7bstoxN0U4Ub5_vQTpH62Z1BWu00lJO0MmEPq2Hj7eihpUwCsc_eiL0j8tYPTkc9xB_sArK2lPjBnj1wqO0RY0MT81IY2FJseTG6wxxtMg-0vugAxnFOkpAd9plRCq4bZxukQkZy9zYpIPGTLELlaUHb4BlOn_QE8ihRIPz7Z678rPWPXGlYQA9NkXq5PrQQmXAaGHYZzi-yumh_fGPl2EfP1Xaj45A8qUSvS1iT5aNL132HysCv6JBO97Px0FNtVDgcuvRudxheMCK_YKMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدول اطلاع رسانی خاموشی لارستان منتشر
شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/133306" target="_blank">📅 23:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133305">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مهر : اختلال در شبکه بانکی همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/133305" target="_blank">📅 23:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133304">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
شرکت برق منطقه‌ای تهران: بر اثر حادثه فنی در یکی از پست‌های برق، برق بخشی از مشترکین ساکن مناطق شرق تهران دچار قطعی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/133304" target="_blank">📅 22:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133303">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سخنگوی آب و فاضلاب استان تهران: هیچ برنامه‌ای برای افت فشار و نوبت‌بندی آب نداریم، چون وضعیت پایدار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/133303" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133302">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری / نیوزمکس:  ترامپ در حال بررسی ازسرگیری محاصره دریایی است
🔴
دولت آمریکا دو ناو هواپیمابر و بیش از ۲٠ کشتی جنگی را به سمت منطقه هدایت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/133302" target="_blank">📅 22:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133301">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19bcae33a6.mp4?token=Ig5by9JLHJ87u8Cv29N2tDv2voKymtj9U37uzciHsz4spG3j_ZEuBEOs_Iy5mTWRYLoDZ15LKSLaN2E6cwTuU2b_F1xPOlCnFXborUWxUbVZqg_6YGCs6FiBrB1jpSYv54K_6eVlgu9ydJXaUr-HuF1EmHI2Mr9rdKrOueH_bLKrfqvRms2Tj5r7V_khfTzFTnWcKsUkGpQoBHrOwfgIexM3nPjZE2InHQdgOScu4Lgneh6OGr17ps04fQqwSfm9mDaEQxQTHb2gtQYAWK7yYQgLXw3VdlIxN0-dnsKNEkU9l2CfGB4Qv51uxEDneOjw99tbd-LSMYYBWLS6SWPhyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19bcae33a6.mp4?token=Ig5by9JLHJ87u8Cv29N2tDv2voKymtj9U37uzciHsz4spG3j_ZEuBEOs_Iy5mTWRYLoDZ15LKSLaN2E6cwTuU2b_F1xPOlCnFXborUWxUbVZqg_6YGCs6FiBrB1jpSYv54K_6eVlgu9ydJXaUr-HuF1EmHI2Mr9rdKrOueH_bLKrfqvRms2Tj5r7V_khfTzFTnWcKsUkGpQoBHrOwfgIexM3nPjZE2InHQdgOScu4Lgneh6OGr17ps04fQqwSfm9mDaEQxQTHb2gtQYAWK7yYQgLXw3VdlIxN0-dnsKNEkU9l2CfGB4Qv51uxEDneOjw99tbd-LSMYYBWLS6SWPhyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ضرغامی: این مذاکرات مانند خوردن گوشت مردار و میت در مقطع اضطرار است
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/133301" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133300">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFE1Xfq2lVDMBkTtK7rhhw5RPNMruf9rCRCZsRczZ7lHvVdZahVxPgNsQ7UXvP6pOeRYMMMjqnYQLI1M7clbpq9owvweoBVXBLJ6JUo7hMFQuBSOovTF29T0jiz840wa2Zh17SKyPHPNSKlPcEkQJz8kbPRLHQSuRLIUg9RpeqYi7OGYvcxlmBczLckD8jyc6LPflGhqVwRo2jaR8TGpLpIHMMC-VXUqHD_fi3o_MYNYyFw3kJX0oQJWbdtTTctUq6W9k0XC-iuSDQrYG59SnZ3d1n2ZWyokKMdZW_0mmfHS68wYTN8is4Luhup5lT2GWaID6Y8HlntMuR2dzc473Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید : یک دیپلمات آگاه از مذاکرات گفت : در جریان مذاکرات امروز در مسقط
عمان گفت مسیر ما مانند قبل باز خواهد بود
🔴
این دیپلمات گفت : ایرانی‌ها نتوانستند این پیشنهاد را در جلسه تصویب کنند و مجبور شدند آن را برای بحث‌های داخلی به تهران ببرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/133300" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133299">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
آکسیوس: ایرانی‌ها طرح عمان برای ازادی ناوبری و رایگان بودن عبور و مرور را برای مشورت‌های داخلی به تهران بردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/133299" target="_blank">📅 22:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133298">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سی‌ان‌ان: پیشنهاد عمان مبنی بر عبور آزادانه و بدون هزینه از هر دو کریدور شمالی و جنوبی در تنگه هرمز در حال مذاکره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/133298" target="_blank">📅 22:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133297">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9bf0823137.mp4?token=u6ZrQBuU7V86pKEusXmhfR0x9cQkiG6iSYqSIuGUIvXv8PZ5is8Av6yotkuRZMBOUXWtSOex7G5bRZ99BC0PzIU4CTZH59lY3pz7S4EOZUWovKAAMz04UL5oh9MKgDa2p1C9Y3fGweE-vdGZWDXjvDM5myRNxc1Dputdv7voH-7DNWA9LEkGa88axlyLsEjDu7Td9EIYVQCxihepcCDLT7HQN_oxqCei0WoqIvukdqCbY3m66yI0Uuk6lQ9fck318yZXT7Jw864bjqYG03KbmUMkkpJSwPIMKqbxQRwIUKLaQiEnD5K41p5IbUpYutsjQXwvcqzQMxjhmqZkgTurKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9bf0823137.mp4?token=u6ZrQBuU7V86pKEusXmhfR0x9cQkiG6iSYqSIuGUIvXv8PZ5is8Av6yotkuRZMBOUXWtSOex7G5bRZ99BC0PzIU4CTZH59lY3pz7S4EOZUWovKAAMz04UL5oh9MKgDa2p1C9Y3fGweE-vdGZWDXjvDM5myRNxc1Dputdv7voH-7DNWA9LEkGa88axlyLsEjDu7Td9EIYVQCxihepcCDLT7HQN_oxqCei0WoqIvukdqCbY3m66yI0Uuk6lQ9fck318yZXT7Jw864bjqYG03KbmUMkkpJSwPIMKqbxQRwIUKLaQiEnD5K41p5IbUpYutsjQXwvcqzQMxjhmqZkgTurKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استیو بنن از نزدیکان و طرفداران اصلی ترامپ : موساد با مطرح کردن موضوع ترور ترامپ قصد دارد بار دیگر او را فریب دهد تا زمینه برای آغاز یک جنگ جدید فراهم شود؛ جنگی که این‌بار ممکن است به تهاجم زمینی منجر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/133297" target="_blank">📅 22:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133296">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEyMcSg3rpX4ezEagpQBaVuHPgOIzIZCJgMJ5CYNYpAEk5MGJbl03xppLGwuAyIe8CrVSX7rc2H_-_pFIOLiWjt7cAh1u-g38O3siIRAB_dfnF6AhzRd2GmKgaYUyRmEXj00fv7n2oFA_56MbkhSolH1-6eUTsKD9gEvAXw3dUrw2_haJKj4FotVcCO6d40mBXmIn8RiiupPdL_FkeV7DuE7HCkg-Ip6RxMW0dWIG_jEGE1ioSTo_P3-5Jhy5HmO9ZCyYyriIQLc29rkrwGlDnyjxtfjD3OBBVY4UZhqkop_hsWmVZE5me_bB_l4jPGPI4Wzn6FfhQcPpU3n4C1L0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضرغامی: تمام وجود ترامپ را ترس از تهدیدات ما گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/133296" target="_blank">📅 22:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133295">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
روی خانا، نماینده دموکرات کنگره آمریکا، در جریان سفر این هفته خود به کرانه باختری، توسط شهرک‌نشینان اسرائیلی مسلح به تفنگ‌های ساخت آمریکا متوقف و بازداشت موقت شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/133295" target="_blank">📅 22:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133294">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزارت خارجه عمان: امروز در مسقط، مذاکراتی میان عمان و ایران درباره کشتیرانی در تنگه هرمز و تضمین امنیت و آزادی آن، با توجه به تحولات و پیامدهای ناشی از رویدادهای اخیر، برگزار شد
🔴
دو طرف توافق کردند این گفت‌وگوها را در سطوح فنی و سیاسی ادامه دهند تا بر اساس حقوق بین‌الملل به توافق‌های لازم دست یابند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/133294" target="_blank">📅 22:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133293">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
بانک ملی قطر: پیامد‌های تشدید تنش نظامی میان ایالات متحده و ایران، مدت‌ها پس از پایان بحران نیز بر اقتصاد‌های آسیا سایه خواهد افکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/133293" target="_blank">📅 22:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133292">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رویترز: فروش نفت ایران ادامه دارد
🔴
ایران در طول تفاهم‌نامه با آمریکا بصادرات نفت خود را افزایش داد.
🔴
تولیدکنندگان رقیب ایران در غرب آسیا نیز  پس از بازگشایی تنگه هرمز در اواخر ژوئن، برای ازسرگیری صادرات هجوم آوردند.
🔴
از زمان اعلام توافق آتش‌بس در ۱۴ ژوئن، ۵۲ نفت‌کش با محموله‌های نفت و محصولات پتروشیمی ایران حرکت کرده‌اند.
🔴
معامله‌گران نفتی انتظار دارند فروش نفت ایران در روزهای آینده افزایش یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/133292" target="_blank">📅 22:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133291">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یدیعوت آحرونوت به نقل از مسئولان امنیتی اسرائیل: تا این لحظه هیچ دستوری مبنی بر عقب‌نشینی نیروهای ما از مناطق حضورشان در لبنان صادر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/133291" target="_blank">📅 22:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133290">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
کانال 15 اسرائیل:
ایالات متحده منتظر پاسخ جمهوری اسلامی به درخواست‌های خود برای توقف حملات به کشتی‌ها در تنگه هرمز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/133290" target="_blank">📅 22:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133289">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
قطع برق خانگی مشهد از فردا آغاز می‌شود
🔴
سخنگوی شرکت توزیع نیروی برق مشهد گفت: از یکشنبه ۲۱ تیرماه به دنبال مدیریت مصرف برق، خاموشی‌ها در بخش خانگی اعمال خواهد شد. کاشی تصریح کرد: خاموشی‌ها در مناطق مختلف شهر از ۸ صبح آغاز شده و تا شب ادامه خواهد داشت. زمان خاموشی‌ها ۲ ساعته بوده و برنامه خاموشی در سطح شهر توزیع شده است. اگر مردم بتوانند در مدیریت مصرف همراهی کنند، قطعا جداول تعدیل می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/133289" target="_blank">📅 21:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133288">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا : اگه ایران به رفتارهاش ادامه بده، پول‌های بلوکه‌شد‌ش رو آزاد نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/133288" target="_blank">📅 21:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133287">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فاکس‌نیوز: مقامات آمریکایی تهدید جانی علیه ترامپ را جدی می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/133287" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133286">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=oTHraeJCK4bfRLWIa5JSNd3wRq4C1F3HohnOJ9grs0C9vQxV9dCeM1QSNQ5feycBNYGokQEZFwsextxl9_JDF5vNC5EXXkzvPCasGtLHuQw_p4sgj3We17XrM3xE6ZMMKWpn_hsARcDmc02qW-Zbx-3LDPA1DuWlh_V_lcLxm6676CN3p8TXx5BT1sbFZOXBGj6LDEqAEvHk7fYWNDD1hep7lpUxsN6jTF0xsTnUoSyqvOZNhxq-787iGNNByrDbWxvpm65Y0FNBa3kEu0ZemLiE8LemxBw6FsFUbHp0nSS7ayXMc08Dgb_zBtNe2SA0UliynyaDrdJTzFfttWD1mYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=oTHraeJCK4bfRLWIa5JSNd3wRq4C1F3HohnOJ9grs0C9vQxV9dCeM1QSNQ5feycBNYGokQEZFwsextxl9_JDF5vNC5EXXkzvPCasGtLHuQw_p4sgj3We17XrM3xE6ZMMKWpn_hsARcDmc02qW-Zbx-3LDPA1DuWlh_V_lcLxm6676CN3p8TXx5BT1sbFZOXBGj6LDEqAEvHk7fYWNDD1hep7lpUxsN6jTF0xsTnUoSyqvOZNhxq-787iGNNByrDbWxvpm65Y0FNBa3kEu0ZemLiE8LemxBw6FsFUbHp0nSS7ayXMc08Dgb_zBtNe2SA0UliynyaDrdJTzFfttWD1mYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرباز روس خودشو به موش مردگی زده تا پهباد اوکراینی شکارش نکنه
🔴
اپراتور اوکراینی میگه: "نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره :)
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/133286" target="_blank">📅 21:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133285">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AffApeHd28amBv23w_dBr5WWUa2Dvj8nSNhLQDV6n_eOV6COIHS5TvR57GME4b9hhV7xJ-9FsTeqeQkf8ShvE28Vhs47azgfit4wKcS1cAzauOU6Lb4APrQqx5hlqAvOYN8I--Cj4aXiM_OOxjuhYkN8i9UWpi9-xOqebGJovYjrrkOLvq0IqVTB3SIFi05FB4jnLRo443zE4pDzqryZ_rzDrtJXkJeIODtvLJzgByky9lLQK5dg_FNORaHkNYAm-VFG0qnsIysjtl0uRKHXNV3EC3HoNoaVFQVx5RpBbs76IKrBwafSpaGm1dpjT8aXkaAm-lnV3vskDd_NeS4phA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام در مورد حضور ناو هواپیمابر جورج بوش در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/133285" target="_blank">📅 21:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133284">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کرملین: اگر موجودیت روسیه به خطر بیفتد از سلاح هسته‌ای استفاده می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/133284" target="_blank">📅 21:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133283">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ارتش اسرائیل ادعا کرد که ساختمانی را که عناصر حزب‌الله وارد آن شده بودند، در داخل منطقه امنیتی هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/133283" target="_blank">📅 21:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133282">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c328913ad5.mp4?token=Gg7-t7uTbOQXx5jne_U9Gsa11-HNiP_irhEYcfHhKotELYk0jjfeRgOP0cdah8ive-uF6Q9kp1QZ8BAph1M5sxw9RjIvSxSbz1h-tWzBHBpJpAkj43mtvrg0Izqdi7SLdGXwYV7ryg38uPXLDioPQuPvRfQTNxf9NdKCP85sjXZgCnNnAZ2OBeHxJFfHwrS54lLOODBs2JKCiVgpM4iBwDHcjasiMgSF9zuiW-9GA5oz0d1GOtWjW8HiDSp-4o3z3tRK_K3isEU8VxGn_jRc8ih0EEFf_HSPQvr39zDcDwSHx5wyevhTX1fJlr04ZkYgriwYy9BGVI0cKHeUwfkoTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c328913ad5.mp4?token=Gg7-t7uTbOQXx5jne_U9Gsa11-HNiP_irhEYcfHhKotELYk0jjfeRgOP0cdah8ive-uF6Q9kp1QZ8BAph1M5sxw9RjIvSxSbz1h-tWzBHBpJpAkj43mtvrg0Izqdi7SLdGXwYV7ryg38uPXLDioPQuPvRfQTNxf9NdKCP85sjXZgCnNnAZ2OBeHxJFfHwrS54lLOODBs2JKCiVgpM4iBwDHcjasiMgSF9zuiW-9GA5oz0d1GOtWjW8HiDSp-4o3z3tRK_K3isEU8VxGn_jRc8ih0EEFf_HSPQvr39zDcDwSHx5wyevhTX1fJlr04ZkYgriwYy9BGVI0cKHeUwfkoTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیرعامل دیجی کالا: در سال ۹۵ پرفروش‌ترین کفش دیجی کالا ۶۵ دلار قیمت داشت و امروز پرفروش‌ترین کفش‌های سایت تنها ۶ دلار قیمت دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/133282" target="_blank">📅 21:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133281">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یدیعوت آحرونوت به نقل از مسئولان امنیتی اسرائیل: تا این لحظه هیچ دستوری مبنی بر عقب‌نشینی نیروهای ما از مناطق حضورشان در لبنان صادر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133281" target="_blank">📅 21:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133280">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEMyZy_bIQcBIJM_sz_qgWprXX8_scca7Y9akoTFIBLfuXMVAQQ_xrmIRBBazAg7KetgKiYyzZY3A2qDRAGbBXjOELuCN8azcQprPR7ADPW8EmYdqax8n_KoyoNJIb5jWhM9maztH0HR-pKe4lPTx5yZ0Ved0MVw_Bq4whmad4tlLm2MIDi08TdtXop0sJAvfq-LbH8VWZP-0TBOZe-NDrmB1TwStbZGjIz9Ow7Tvw5LeO-dHL7WKDV9jtZoVkKdpnVcgt_urwqVB8tL3U9mpToYq7jBFjFQhfGMHhmtuTp3KVdMyxGGeshMoXigSmACC73YBAi00rERreRT7SAT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون 6 فروند سوخت رسان به همراه یک فروند آواکس در منطقه در حال انجام مأموریت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/133280" target="_blank">📅 21:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133279">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8c10b060.mp4?token=V0zmt0JMAAYYbmkw0Rk1u6Ra4WPef2ItwY4Uahn7Z8iGVy8Wa-qJs2cNncxsJJCpV2hs4AL7QeoOGFZCPX0gM8vtoziiInKqnEfauyrO_I_3WdRDQRfHAPPiNxWLycf5X60Qn0CUBj9prSi7YzWk7nUIWp8eTW5Nibz7Lu7GxdEE55cg_QTmLH2tKasCLpoA37AGy8Hrw4paAncVtpwKEkr2wwIjPegrF5VcK6Fel8NnTaVAHTWfP3LMrcbZgBw1kSXORlHPlhgw7WQTDKgkgFuDaLoHQCBM39ZKPt-fTcKbTd_jfvPQrE9rJdu8gfVSZsdRE8KSmUgZn8242oJjeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8c10b060.mp4?token=V0zmt0JMAAYYbmkw0Rk1u6Ra4WPef2ItwY4Uahn7Z8iGVy8Wa-qJs2cNncxsJJCpV2hs4AL7QeoOGFZCPX0gM8vtoziiInKqnEfauyrO_I_3WdRDQRfHAPPiNxWLycf5X60Qn0CUBj9prSi7YzWk7nUIWp8eTW5Nibz7Lu7GxdEE55cg_QTmLH2tKasCLpoA37AGy8Hrw4paAncVtpwKEkr2wwIjPegrF5VcK6Fel8NnTaVAHTWfP3LMrcbZgBw1kSXORlHPlhgw7WQTDKgkgFuDaLoHQCBM39ZKPt-fTcKbTd_jfvPQrE9rJdu8gfVSZsdRE8KSmUgZn8242oJjeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند در صدا سیما : بیش از ۴۰ میلیون نفر در مراسم تشییع شرکت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/133279" target="_blank">📅 21:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133278">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/393888a333.mp4?token=ZqTAB1lGT5X3cDmvICPVsAri690ObgxigTNBaMFeIFHl82mSRdwTsxcEaWDLuJ6tsJWhBp92z-nRDMdVLYbBH4QDIqjLyKtnfvAqt2X6_9PLkaAxHWcIwJrjw2sojj7WZBLYeRCMtyQe5lsGsVXLuznjcUBbzsHQG0BXB2D8V1oHHYf2zeTZmSgP3R8qmKvz6l595veoSTZl-vX_jfiOH8gidCL3VJSVYYLP6y8jRHVUQoA3ScH8SrZMRCAPPDL5i_Vdr5pzjjrCAUaJ37xjPrFL_vO8ubKeisE5rrexZVolHzhGnQktv_pp-eqV4G8crEwuqVTAE-z6qkp7Ix-5EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/393888a333.mp4?token=ZqTAB1lGT5X3cDmvICPVsAri690ObgxigTNBaMFeIFHl82mSRdwTsxcEaWDLuJ6tsJWhBp92z-nRDMdVLYbBH4QDIqjLyKtnfvAqt2X6_9PLkaAxHWcIwJrjw2sojj7WZBLYeRCMtyQe5lsGsVXLuznjcUBbzsHQG0BXB2D8V1oHHYf2zeTZmSgP3R8qmKvz6l595veoSTZl-vX_jfiOH8gidCL3VJSVYYLP6y8jRHVUQoA3ScH8SrZMRCAPPDL5i_Vdr5pzjjrCAUaJ37xjPrFL_vO8ubKeisE5rrexZVolHzhGnQktv_pp-eqV4G8crEwuqVTAE-z6qkp7Ix-5EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر باورنکردنی دوربین مداربسته از شمال ونزوئلا که نشان‌دهنده فرو ریختن چندین ساختمان در نتیجه دو زلزله قدرتمند در ۲۴ ژوئن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/133278" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133277">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750f49ad82.mp4?token=XrtJFQ0WuN8Vyseo3cPSk46PhByDyrhllbKOzP66gVrApGi8QVVsyDcGdWvFP_NOrrH3kF4rk0Itf9aJ0p2GPezSVkVoz5bMDbbGe1u93y0b-HlsOyWKfbOxX0TcNYGNpAgDrMiRn2LZZTVTGrn5UwivcTebxrrHJb8-9NP-L0m68EMJcR7KUJESL0Ygncej7qe7PTjBEvFDUoYVQXNKBWdiEOQYhu5kcAnMPoMv5luVJmPoHwqkbxwc-b6McEdZNogzHAiKLFZbRsa9TSzk6m9a3omEG0WqPypLKTm96LbzyjcUC6AP1Re3yMZABfH_f-UWyunNiLFxu72IKQnz6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750f49ad82.mp4?token=XrtJFQ0WuN8Vyseo3cPSk46PhByDyrhllbKOzP66gVrApGi8QVVsyDcGdWvFP_NOrrH3kF4rk0Itf9aJ0p2GPezSVkVoz5bMDbbGe1u93y0b-HlsOyWKfbOxX0TcNYGNpAgDrMiRn2LZZTVTGrn5UwivcTebxrrHJb8-9NP-L0m68EMJcR7KUJESL0Ygncej7qe7PTjBEvFDUoYVQXNKBWdiEOQYhu5kcAnMPoMv5luVJmPoHwqkbxwc-b6McEdZNogzHAiKLFZbRsa9TSzk6m9a3omEG0WqPypLKTm96LbzyjcUC6AP1Re3yMZABfH_f-UWyunNiLFxu72IKQnz6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ناصر هادیان، کارشناس روابط بین‌الملل: ول کنید مدیریت تنگه را، فقط بگویید تنگه مثل قبل؛ میترسم تنگه را از دست بدهید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/133277" target="_blank">📅 20:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133276">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
العربیه: ایران با عمان به دنبال توافقی بر سر تنگه هرمز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/133276" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133275">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
روبیو : رهبران کوبا باید پیش از آنکه خیلی دیر شود، به اصلاحات واقعی، صلح و رفاه متعهد شوند.
🔴
واشنگتن به‌طور فعال با تهدیدات امنیت ملی که ادعا می‌شود از کوبا سرچشمه می‌گیرد، مقابله خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133275" target="_blank">📅 20:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133274">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea5587a6f9.mp4?token=o97ZxE1DY6lCtZuNiBHi14ZeaREQ3uNfOPd9u9YKA5ow4w71NO0C5dm6QkMxXK6IJTjx7q_ZwMlCV86oL_ZuFmuMck4zpSOdPuGHRNUBUXmoDSsXfEFN5BC-1Y0Z8Nfsi3cqsp3tcEE2cAHRp5TsVnuYgs4Ad95lDZhQ_M4yamwq-SoH_JpXlY8PtEWTiQm-_qR12FuK2qZneZn40pM-Bq5tzKsZYuYNnuRVbarC_QjTRLJVxXvLR5qvGdWxcAO1C-c_F4OTXj_jXMn71MTb6w5VjtrUMxIcPZOero56pH09P2J47IC11pa-3PWccNgEnH2YA_-8iRIOqUgW1Sn62h3JTf1VS7POD3aTIPLLlnvWhualyhHZC9AwtuqVhurS7p2bjPHIYJO6SlTVgKMVTYp9pvfcMV1XTy1jeFkJYaeK6pKxaH0GjbEzfIxLVh-npAIPT4qCPz4qNApRQ7-Hxfj6kVTOP7fN5SeLVRPlYpPtzX4OVcUF3lDqadZIRCUSynk774gAjAi2HhQ8csLR8nTah4LOUn3M9po3YbE9kYc31JA3ZxA0GPDoHvCeV3PbXs0TgrhvXc93yRs5h-TSsUXaGunE63deNhTtr276X4eKZtG6smG1ilmow1dp5Yw0CwGjBGEklILrI02vXMHyCbq7ZbFDKuEeio9It308vho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea5587a6f9.mp4?token=o97ZxE1DY6lCtZuNiBHi14ZeaREQ3uNfOPd9u9YKA5ow4w71NO0C5dm6QkMxXK6IJTjx7q_ZwMlCV86oL_ZuFmuMck4zpSOdPuGHRNUBUXmoDSsXfEFN5BC-1Y0Z8Nfsi3cqsp3tcEE2cAHRp5TsVnuYgs4Ad95lDZhQ_M4yamwq-SoH_JpXlY8PtEWTiQm-_qR12FuK2qZneZn40pM-Bq5tzKsZYuYNnuRVbarC_QjTRLJVxXvLR5qvGdWxcAO1C-c_F4OTXj_jXMn71MTb6w5VjtrUMxIcPZOero56pH09P2J47IC11pa-3PWccNgEnH2YA_-8iRIOqUgW1Sn62h3JTf1VS7POD3aTIPLLlnvWhualyhHZC9AwtuqVhurS7p2bjPHIYJO6SlTVgKMVTYp9pvfcMV1XTy1jeFkJYaeK6pKxaH0GjbEzfIxLVh-npAIPT4qCPz4qNApRQ7-Hxfj6kVTOP7fN5SeLVRPlYpPtzX4OVcUF3lDqadZIRCUSynk774gAjAi2HhQ8csLR8nTah4LOUn3M9po3YbE9kYc31JA3ZxA0GPDoHvCeV3PbXs0TgrhvXc93yRs5h-TSsUXaGunE63deNhTtr276X4eKZtG6smG1ilmow1dp5Yw0CwGjBGEklILrI02vXMHyCbq7ZbFDKuEeio9It308vho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دوربین مداربسته از لحظه اصابت بمب های گلایدی پرتاب شده از جنگنده‌های روسی به شهر زاپوریژیا که متجر به کشته شدن ۵ اوکراینی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/133274" target="_blank">📅 20:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133273">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سفیر چین: چین دو بار پیش‌نویس قطعنامه مربوط به تنگه هرمز را در شورای امنیت وتو کرد
🔴
در دیپلماسی چین، به‌ندرت از حق وتو استفاده می‌کنیم، اما هر بار که وتو می‌کنیم، تصمیمی بسیار جدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/133273" target="_blank">📅 20:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133272">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کرملین: روسیه آغازگر جنگ جهانی سوم نخواهد بود، اروپا بحران را تشدید کرده است
🔴
سخنگوی پوتین ضمن رد قاطعانه قصد مسکو برای آغاز جنگ جهانی سوم، تأکید کرد که حمایت نظامی گسترده غرب از اوکراین بحران را تشدید کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/133272" target="_blank">📅 20:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133271">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
کیهان: یک نفر به وزارت خارجه اطلاع دهد ترامپ هفته پیش تفاهم‌نامه را پاره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/133271" target="_blank">📅 20:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133270">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l96TZ48pMwe5Z5ZxO0FANxFaxJ94xmzqceCzkyqJrhdZ_ybH-hgh7irsOdASu65E9JxDnQ9IUyUk1TVqtD3mTOm3_JFjYQ7CaDiZCAvcdog7u9aQTgXPh5qcw60HGXHGf6992pJmRXCw1xDKzdjITYpHjR9_0ErdCse2-Zv5Je8sQC5umgqetyRCg7pp7FJrvRpFLRPI_PmokX6nuafY5iqm3dOmrimiUVVpkKawDFhHQ4GDuZTVS_3cwvSDYbJ3pdvD-SqMOSIlzWjmLQ8MrspkCiEMu-JatVfeIHgUwpj6pdcDgHVBZzXCz7KqtD8PQZBdqlzvpWowC-MDIoSokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور ولادیمیر زلنسکی در مراسم تشییع قم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/133270" target="_blank">📅 20:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133269">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
‏منبع اطلاعاتی ایرانی ارشد به پرس تی‌وی: ایران در حال اجرای ترتیبات مربوط به مدیریت تنگه هرمز طبق بند پنجم از یادداشت تفاهم است و تسلیم فشارها یا کمپین‌های رسانه‌ای که طرف مقابل به راه می‌اندازد، نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133269" target="_blank">📅 20:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133268">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فاکس‌نیوز: تهدید مرگ رژیم تهران علیه ترامپ واقعی است، نه نظری
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/133268" target="_blank">📅 20:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133267">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR9qULeAPUgwyWOv-u7378vWNyk3ULcaErSs6cTeqdsuUGvVnVrmmSZRn5LsF0MjJdKIXUXeFHfFRUlBEYbqy2tzZ88AvByYhvo1sAC87GqKGrSId1uvCAUXtnk6CKNbCjsXW_HdhEgSQkHBp6crk-E8yTv-cASF63ZYK6qnRF6xjPnQ-wRtavk2y8KPRFMvtEJefdYgLAG33Kh1RAz-FoOgHOZOi7NFOElaPprwzOI1jAN0BDygnsL2HOR9PeVsqNXmuliOnbiL77iLIKZpeZqVgWPIzKA1cOj6tdJ2bQkrp1uNqAveJyxEoR7jfiOCJsuWoPYdBIT0tzk9bTKBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، به مجی هابرمن از نیویورک تایمز به خاطر کتابش با عنوان "تغییر رژیم" حمله کرد و گفت که او یک "معاینه پزشکی کامل" را با موفقیت گذرانده است و درخواست انجام یک آزمایش شناختی دیگر را داده است:
مجی هابرمن، به مدت ده سال، مطالب نادرستی درباره من منتشر کرده است. کتاب او یک شوخی است! ۹۰ درصد آن، اخبار جعلی است. او از طریق گزارش‌های نادرست خود امرار معاش کرده و باید تاوان آن را بپردازد، زمانی که دادخواست چند میلیارد دلاری ما علیه نیویورک تایمز که در حال فروپاشی است، به دادگاه می‌رسد، که امیدوارم خیلی طول نکشد.
🔴
من با انتقادهای منفی مشکلی ندارم، اگر درست باشند. اما از گزارش‌های نادرست، مانند آنچه در کتاب خسته‌کننده‌اش وجود دارد، و مانند آنچه که او در طول یازده سال گذشته انجام داده است، ناراحت می‌شوم. هدف او فقط این بود که ترامپ در انتخابات شکست بخورد، اما با این حال، من در حالی که در دفتر بیضی نشسته و فکر می‌کنم، این کار به خوبی پیش نرفته است. مجی یک بازنده است! اگر او واقعاً داستان واقعی من را می‌نوشت، در واقع بسیار خسته‌کننده می‌شد، اما پر از موفقیت.
🔴
همچنین، من به تازگی یک معاینه پزشکی کامل در مرکز والتر رید انجام دادم. من این کار را هر شش ماه یک بار انجام می‌دهم و درخواست انجام یک آزمایش شناختی دیگر را داده‌ام. من تنها رئیس‌جمهوری هستم که این کار را سه بار انجام داده‌ام و در همه آنها موفق بوده‌ام - به تمام سوالات پاسخ درست داده‌ام. تعداد کمی از افراد در واشنگتن، دی.سی. می‌توانند این کار را انجام دهند، از جمله مجی و همکارش، جاناتان سوآن. من شرط می‌بندم که آنها نمی‌توانند حتی ۵۰ درصد از سوالات را به درستی پاسخ دهند.
🔴
به هر حال، کتاب آنها را نخرید، این یک زباله است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/133267" target="_blank">📅 20:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133266">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3140609d71.mp4?token=WLZHd8F3BmDmxtQmAIx01PN-t5WNA2izy70NmfxoxJj_BtztNRwfjDE3nWJVrlOVJyT7-DJ3uG6QDFZhHOhUXhQM9jw9fRWoA9Jg0Gx3vu1c55UTlxHTfSU_zUR_WrMvqWUoVLYHSVuy8Pjjt1M_CU5eQbOJci8OZkmilHesbIf_Lhn85Ff65oKY3oRjifmOhNNfHlH61dyp_DkH9DYeX5rcEsy8ZFmRJ21FBsBvdEjvqSyezdH3pRPpByHcbd9I2SCcqtVUv5LhwF5bxVYnplCuhmkL2iivRDMNg-IedGV8hvJdMQB0AY2RTNcYB1Lxrqs5VjclJAwsHfPExOMqrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3140609d71.mp4?token=WLZHd8F3BmDmxtQmAIx01PN-t5WNA2izy70NmfxoxJj_BtztNRwfjDE3nWJVrlOVJyT7-DJ3uG6QDFZhHOhUXhQM9jw9fRWoA9Jg0Gx3vu1c55UTlxHTfSU_zUR_WrMvqWUoVLYHSVuy8Pjjt1M_CU5eQbOJci8OZkmilHesbIf_Lhn85Ff65oKY3oRjifmOhNNfHlH61dyp_DkH9DYeX5rcEsy8ZFmRJ21FBsBvdEjvqSyezdH3pRPpByHcbd9I2SCcqtVUv5LhwF5bxVYnplCuhmkL2iivRDMNg-IedGV8hvJdMQB0AY2RTNcYB1Lxrqs5VjclJAwsHfPExOMqrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای زمینی سپاه، منطقه کردستان عراق را با توپخانه مورد هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/133266" target="_blank">📅 19:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133265">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزارت امور خارجه: عراقچی و البوسعیدی درباره سازوکارهای مناسب برای تردد ایمن کشتی‌ها از تنگه هرمز، وفق ماده ۵ یادداشت تفاهم اسلام‌آباد تبادل نظر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/133265" target="_blank">📅 19:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133264">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
بانک ملی قطر: پیامد‌های تشدید تنش نظامی میان ایالات متحده و ایران، مدت‌ها پس از پایان بحران نیز بر اقتصاد‌های آسیا سایه خواهد افکند
🔴
بازگشت تولید و تجارت به سطح قبل از بحران، پیش از اوایل سال آینده میلادی محقق نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/133264" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133263">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/214dcf40cc.mp4?token=cjQvEFtS7cH40aRjU3y98BJsMfLg1eHrJJxdHp_vN_mVaNgj5sOmZgv9FpdRovkRgJOoABiLaDmHbBhyPdm57y0BUr1x27YvJ9Hvn2mdEtSr44AAK70ONc3nky2F0rU3S4iFKFYdsgNSFE0aJfWc-f3X2KJAZ3qQ1O7uHwrxaM6WdqssLxfzLxndtoyTL_H0HdHzqmMt_dRIlVCa43FGvG8gV3qMXms9hFSA2Hypp46sEBmrPYBG95xrVcNecd9Pat-UgRZtKVOrewlfoXFPU7PSl4notcuWwEiMM37gA2WsY7lQKPwIY1qWaRNGLNOAWgG1xJqTA87andPqQkCzJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/214dcf40cc.mp4?token=cjQvEFtS7cH40aRjU3y98BJsMfLg1eHrJJxdHp_vN_mVaNgj5sOmZgv9FpdRovkRgJOoABiLaDmHbBhyPdm57y0BUr1x27YvJ9Hvn2mdEtSr44AAK70ONc3nky2F0rU3S4iFKFYdsgNSFE0aJfWc-f3X2KJAZ3qQ1O7uHwrxaM6WdqssLxfzLxndtoyTL_H0HdHzqmMt_dRIlVCa43FGvG8gV3qMXms9hFSA2Hypp46sEBmrPYBG95xrVcNecd9Pat-UgRZtKVOrewlfoXFPU7PSl4notcuWwEiMM37gA2WsY7lQKPwIY1qWaRNGLNOAWgG1xJqTA87andPqQkCzJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چین و روسیه فیلمی از رزمایش مشترک دریایی خود را منتشر کرده‌اند.
🔴
این تصاویر بر افزایش قابلیت همکاری نیروهای دریایی چین  و روسیه تأکید دارد و نقطه عطف دیگری در همکاری راهبردی دریایی رو به گسترش آن‌ها محسوب می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/133263" target="_blank">📅 19:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133262">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ایهود باراک، نخست‌وزیر پیشین اسرائیل:
«اگر بنیامین نتانیاهو به این نتیجه برسد که در حال باختن است، ممکن است برای به تعویق انداختن انتخابات کنست، اسرائیل را به جنگ با ایران بکشاند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/133262" target="_blank">📅 19:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133261">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
نیویورک تایمز: روبیو عملاً ونزوئلا را از راه دور اداره می‌کند
🔴
نیویورک تایمز گزارش داد مارکو روبیو، وزیر خارجه آمریکا کنترل مستقیم سیستم‌های مالی، مدیریت منابع طبیعی و زیرساخت‌های دولتی ونزوئلا را در دست گرفته تا همسویی کامل با واشنگتن را تضمین کند.
🔴
روبیو معمار اصلی عملیات روزانه دولت و مسیر سیاسی ونزوئلا شده است. این راهبرد «حکمرانی از راه دور» برای بازسازی اقتصاد و متمرکز کردن تصمیم‌گیری‌ها در واشنگتن به کار گرفته شده است.
🔴
تحلیلگران این مداخله را گسترش عظیم سیاست خارجی آمریکا و تبدیل وزیر خارجه به مدیر عملی دولت ونزوئلا می‌دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/133261" target="_blank">📅 19:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133260">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
تعداد کشته شده های آلمان بخاطر گرما از مرز ۵ هزار نفر عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/133260" target="_blank">📅 19:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133259">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خبرگزاری فرانسه به نقل از یک منبع آگاه گزارش داد که یک هیات آمریکایی برای گفت‌وگو در مورد عقب نشینی اسرائیل از «مناطق آزمایشی» در لبنان حضور پیدا کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/133259" target="_blank">📅 19:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133258">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
فیفا به ونزوئلا پس از زلزله ویرانگر، یک‌میلیون دلار کمک خواهد کرد
🔴
بر اساس گزارش وب‌سایت فیفا، این کمک‌ها از یک صندوق ویژه برای ارائه کمک‌های فوری بشردوستانه به آسیب‌دیدگان، کمک به مناطق آسیب‌دیده و حمایت از عملیات امداد و نجات اختصاص خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/133258" target="_blank">📅 19:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133257">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
منابع عراقی از شنیده شدن صدای چند انفجار در اربیل در شمال عراق خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/133257" target="_blank">📅 19:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133256">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bs3xjGMA6_bYuny5WpTtcT7ZxctwqapSx63NowpXj4nWLcnTraas406GGXyI6y-fcRKwl_n7EqMB026SnG6Ubp80kk-ZH0sdN5xhO-wItK7PLtaZFGPXJ_BIonD5to9ewYjqje2T-lW_j2BGWm_0h8YZzrKOrQgr3pRPZknpa43oWkrqUzEqu3EI6ueeKJsI7MzjUMaRLZ611lIy4Ie_e-H2TwdXB4jjTsdLEPMQvyB6v2sE0u4cbaw9UHZ3MuHhqh7NR7DiEK2i-Zmj5Yt_ff3vQgW20cwMvcutcxWprOp065Lyj-Lt_wbZ6DVjDeJ0LMMexAwZyp9G0SiIJboyKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۸ فروند هواپیمای سوخت‌رسان هوایی KC-135R و KC-46A نیروی هوایی آمریکا هم‌اکنون بر فراز منطقه خلیج فارس در حال عملیات هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/133256" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133255">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
یک منبع آگاه: تصمیم‌گیری برای تنگه هرمز فقط توسط ایران و عمان صورت می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/133255" target="_blank">📅 19:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133254">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
العربیه: ایران، ابتکار عمل را در پیش گرفته و به مسقط سفر کرد تا درباره تنگه هرمز گفتگوهایی برگزار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/133254" target="_blank">📅 19:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133253">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
شبکه آمریکایی سی‌بی‌اس به نقل از یک مقام آمریکایی مدعی شد: ونس به عمان سفر نخواهد کرد و روبیو، وویتکوف و کوشنر در مذاکرات آنجا شرکت نخواهند کرد.
🔴
ما به مذاکرات از راه دور با میانجیگران در عمان و قطر ادامه خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133253" target="_blank">📅 19:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133252">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8pe4XVaqJJG88t3LABDd9GREVFMFGEL0T2JtWJpCGqU77wICpENSEV5Li6XZeFDShN0kao3pb_nj7_Nq9WX8a6364f3un2MUs5_wBHM5XkC99lTwsvU6_9sFtMWGBtkfcBpn1ip2glTqKMBfSqtZLftjpxL_DuUXjGrj46IlQJ4LLnX3umGWlUh4AzLI6BYN96Z47uB34TmFetkRVr7asFV03tL5Y-9cEcQ_mCpY7fKT5yNHlMIZiwQrPvjoAdJjbcltlyMWm-ZTxDwbt43E2fYzcJh3whuzbR5UN79fLVKGBxbQtxGdoiJEF0sYoA7QvUcc84dT-alGFlmwyfDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیمی از سوخت‌رسان‌های آمریکا در پایگاه شاهزاده سلطان عربستان، تخلیه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/133252" target="_blank">📅 18:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133251">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
گزارش رسانه ها از بحران شدید سوخت در روسیه!
🔴
بخش بزرگی از پالایشگاه های روسیه در پی حملات اوکراین از کار افتاده است
🔴
تمام صادرات سوخت روسیه ممنوع اعلام شده و واردات سوخت به صورت اضطراری آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/133251" target="_blank">📅 18:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133250">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
شرکت برق تهران: خاموشی‌های منطقۀ ولیعصر و قائم‌مقام رفع شد
🔴
خاموشی‌های پراکنده در محدودۀ خیابان‌های ولیعصر و قائم‌مقام به‌دلیل افزایش بار شبکه و بروز اشکال فنی در یکی از خطوط برق‌رسانی رخ داده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/133250" target="_blank">📅 18:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133249">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-X5WH122bsH704FsjGn499ec7JTkK-_0ipG3InATLanx8tVGusMcCyjwvEowHFmU1q5TA-RCP4ez9R2rfV-jkPW5lQNos46q0i2_F349fvjgs3Kdytv_rYbhPNSmOOmKk_SfxhF2M2rLmSLWfnbItmjO4XyYALtw1FL51_G9MQOp1aueYtGUK2PDCcHnwU6JdmGqqairBYP89bmvKbQfokC2htp-pZL-Hg_eaIHKCAhL7DD-vu_Rs_WazRdF9YqBUg_wb1XxqoM6X8fUCvETB4XGICKvltE_ldX0TmpVi44M8lR_BZBZkbILuibr88tDfAHWB8dCRC05tAS4rzZxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اهداف انتقام جمهوری اسلامی توسط روزنامه همشهری منتشر شد !
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/133249" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133248">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس در نشست مشترک با سرپرست وزارت دفاع: مجلس با تمام توان از نیروهای مسلح حمایت و از هر طرح و لایحه‌ای که به تقویت بنیه دفاعی و افزایش توان بازدارندگی کشور منجر شود، پشتیبانی خواهد کرد
🔴
در تامین امنیت ملی خودمان با هیچ یک از کشورهای همسایه تعارف نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/133248" target="_blank">📅 18:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133247">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
خبرگزاری AP به نقل از مقامات آمریکایی: ترامپ به مذاکره‌کنندگان آمریکایی زمان محدودی برای دستیابی به توافق با ایران می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/133247" target="_blank">📅 18:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133246">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
تا این لحظه، نتیجه نهایی یا توافق رسمی از نشست امروز اعلام نشده است. آنچه از گزارش‌های منتشرشده برمی‌آید این است:
🔴
دیدار عباس عراقچی و وزیر خارجه عمان پایان یافته است
🔴
گفت‌وگوها عمدتاً بر امنیت تنگه هرمز، کاهش تنش و ادامه مسیر دیپلماسی متمرکز بوده است
🔴
هیچ بیانیه‌ای درباره توافق، لغو تحریم‌ها یا توافق جدید ایران و آمریکا منتشر نشده است
🔴
بر اساس گزارش‌ها، عمان همچنان در حال انتقال پیام‌ها میان تهران و واشنگتن است و انتظار می‌رود رایزنی‌ها ادامه پیدا کند
بنابراین، نتیجه عملی تا این لحظه این است که مذاکرات ادامه دارد، اما هنوز خبر رسمی از دستیابی به توافق منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133246" target="_blank">📅 18:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133245">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
عباس عراقچی: ایران تاکنون به تعهدات خود عمل کرده است و تنها راه این است که هر دو طرف به تعهدات خود به صورت متقابل عمل کنند.
🔴
اعمال مجدد تحریم‌ها توسط آمریکا، نقض توافق‌نامه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/133245" target="_blank">📅 18:29 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
