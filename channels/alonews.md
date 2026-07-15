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
<img src="https://cdn4.telesco.pe/file/dwZbFyAdL54vlTBLUUxV0mghyeE0dOLbv4XHH1_Xn9lDEwb1L5yhzv_wRnHqPIUeyhwzm6zpPthsNI7CFw6_XDqJRb8wux9jU7TVh3DxkptjTWRGIWr0Td_fFn_F1_QCIHNoz8fF3KDaGSVH2aL0hfJAdZH-rLqyrnrnN2bEk1yYRmNSnGNmd-xdEcrruSd5d-I0ARstqwRkSI-R33_jmQb-neA9CxYGiFuSy5d2_sgXA8hPXa1-Ko7f0fjTCvgh2evvfTTlzlsjt0gewOaM4uCabowKDnxwpMVgOSWmqeMmQIXdwfgmIzYDuvGcorpwJqHrjEBZSHUGASY9YDiFvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 944K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 12:35:10</div>
<hr>

<div class="tg-post" id="msg-134350">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
اینکه توی شهرهایی که هر روز زیر سایه موشک و گلوله‌ان، هنوز امتحان حضوری برگزار می‌کنین، یعنی جون بچه‌های مردم براتون هیچ ارزشی نداره.
🔴
اینکه سرباز وظیفه‌ای رو که با اجبار بردین پادگان، نگه می‌دارین وسط خطر، یعنی حتی جون همون جوونی که خودش انتخاب نکرده اونجا باشه هم براتون مهم نیست.
🔴
هدفتون کاملاً مشخصه؛ می‌خواین کشته‌سازی کنین، می‌خواین از خون مردم روایت بسازین، شاید دوباره بتونین فضای داخل رو کنترل کنین و مردم رو پشت خودتون نگه دارین.
🔴
این همون کاریه که سال‌ها با جنگ عراق کردین. از درد و مرگ و ویرانی مردم استفاده کردین و هر چیزی رو به اسم امنیت خفه کردین.
🤔
بچه‌های مردم، دانش آموزها، سربازهای اجباری و خانواده‌ها سپر سیاسی شما نیستن. هیچ حکومتی حق نداره برای حفظ خودش، مردم رو قربانی کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/134350" target="_blank">📅 12:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134349">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwZSv5hWCn6CmwiSq8kEwirhx63WN1yhaJvQ57lRFjbcpp5v6pAojx6M4NIugdDqRSbEIkFd9x0s2TVFIyO8KQBtmDWrh0tAcm-VKcD24Nw0VveJkRN-fx4bNvtpXmqgwM-5G73_5hVRee3DAcyP7kEHlH828kpZe1f5sf2Oa2lIpLFSdDUMbS8eKsLsix_lWuTzkFeMF20qK8jDOS2S6aO7jS537qvWYet9zIgI8s_1SDlSZ03qXTPN5kiY48GUwpWJjl1teYjU36EAWZRpYAPjoEfYY5pRB2Khzm2lQ2FE_FU2jyB2-TdH9t9RS71HgZnHB-RLD3DYqLC0oVkxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فواد ایزدی: قالیباف همون روحانیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/alonews/134349" target="_blank">📅 12:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134348">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0869c470e4.mp4?token=nuRuXERGtml95HiaBuD_kUGoYxwR7WsdaqWD1VDUFZ2yrBHUT2Z-sSl0Yv655K5prnYfqlqoPLozne5sa8O1pPGx3GKzQ3lWNK6gu_nhn5Tr_BSpikWQQdaMgzgG4dbEui3lffAsqmrbU4708uXSQA8GN-ww6ddms6qx5FlmGdyRMl4co5N3r07Dxy9jmHuT00-vwsNFUCwCCBcC6xgcv-jZlnxYMbTE1PJtVAG8tsUJjtykqSc7vZSO_cfcHGB3iLHp5wmK96nJfQbJv77wIbfx8WZTNla9LUrBWMSKaYlMJSSbdkD5XF5svbVQ7IOh0d26ewzgpD78y1Qg3_IIBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0869c470e4.mp4?token=nuRuXERGtml95HiaBuD_kUGoYxwR7WsdaqWD1VDUFZ2yrBHUT2Z-sSl0Yv655K5prnYfqlqoPLozne5sa8O1pPGx3GKzQ3lWNK6gu_nhn5Tr_BSpikWQQdaMgzgG4dbEui3lffAsqmrbU4708uXSQA8GN-ww6ddms6qx5FlmGdyRMl4co5N3r07Dxy9jmHuT00-vwsNFUCwCCBcC6xgcv-jZlnxYMbTE1PJtVAG8tsUJjtykqSc7vZSO_cfcHGB3iLHp5wmK96nJfQbJv77wIbfx8WZTNla9LUrBWMSKaYlMJSSbdkD5XF5svbVQ7IOh0d26ewzgpD78y1Qg3_IIBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز "
F-18
" آمریکایی، دیروز تو چابهار، با ارتفاع کم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/134348" target="_blank">📅 12:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134347">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
انفجار در اهوار
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/134347" target="_blank">📅 12:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134346">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csbG28ZCcnio8-l7X2-JJ3vFN9UxlpEd6YVUgQEnbSjfr96tJ_VyLMyOpGY3OK-D8_phIIRsFRqjb5ie9ViRhP48LSt3i6DCvupWfQvOCOmRaJrNwLg-YRpIqzABpBMuH3G0VZ_TtB_JDrPokL5D_sCLow7M2wGm1_YpHGFCLEqpuY5MOOOhMltpY3lDkqmt_w3vqGBgtOk73foTt1VjPqeWc65VBP_rpnlkwrO2gqIi3bEzFzvtjR1a0rDDSEkpGzKVLXFvwv0gemuDUjvv_2K1spQu_O6jVLCAiaQxJ9VMMh46IAEU-1ajqkrlz5WyKuySIgkwQ4ABqMQlbZHJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعلا برنامه‌ای برای واکسیناسیون رایگان HPV نداریم
رئیسی، معاون بهداشت وزارت بهداشت:
🔴
در حال حاضر، واکسن HPV جزو سبد واکسیناسیون رایگان کشور نیست و برنامه‌ای برای آن نداریم.
🔴
اکنون تمام تمرکز بر تامین سبد فعلی واکسیناسیون است.
🔴
برنامه‌ای برای افزودن واکسن جدید به سبد واکسیناسیون نداریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/134346" target="_blank">📅 12:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134345">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be3919ab6.mp4?token=WPJC4RkcKgTOxouR4oRrfGQiYx2cAfMxHYgRbjBoQ7UvKqJ1S1kI-l6tAkhjbaxrHZHgrQ8CzvdoCeVZtFTKBfwgiIpTA2jkyHRcSkvwLCHW-ht_v6D-5Cv21ZVEkmoTeSejbFHZJzW5cdwCTReRcJxSDkhEPluueyONrsGYUzPNGG8m6cGrK7HsdnViBvhmRiuzLRpNHntCaagT085ySLutheOSvnZg49YYzcjw69hqBnd1dpDZjDyrG_5NiqypoIRpS3P_zaFjbUGsMjyTF5u4DkFYyGinhwwYVhMj3IjCAdcw7Sp4YzEVnceGLaS25iZ1PLb_s302H6o4mK2jgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be3919ab6.mp4?token=WPJC4RkcKgTOxouR4oRrfGQiYx2cAfMxHYgRbjBoQ7UvKqJ1S1kI-l6tAkhjbaxrHZHgrQ8CzvdoCeVZtFTKBfwgiIpTA2jkyHRcSkvwLCHW-ht_v6D-5Cv21ZVEkmoTeSejbFHZJzW5cdwCTReRcJxSDkhEPluueyONrsGYUzPNGG8m6cGrK7HsdnViBvhmRiuzLRpNHntCaagT085ySLutheOSvnZg49YYzcjw69hqBnd1dpDZjDyrG_5NiqypoIRpS3P_zaFjbUGsMjyTF5u4DkFYyGinhwwYVhMj3IjCAdcw7Sp4YzEVnceGLaS25iZ1PLb_s302H6o4mK2jgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
این ویدوئی تاریخی اولین لحظه ای هست که آلمان نازی سرنگون شد. یکی از زندانبان‌ها به دست مردم افتاده.
🤔
حداقل از تاریخ درس عبرت بگیرید تا سر خودتون نیاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/134345" target="_blank">📅 12:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134344">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
طبق گزارش کانال ۱۲، یک سرباز ارتش اسرائیل به پنج سال حبس محکوم شد به دلیل ارسال ویدیوهایی به ایران که شامل تصاویری از رهگیری موشک‌ها و همچنین تصاویر حملات موشکی در طول جنگ بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/134344" target="_blank">📅 12:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134343">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
چین: با اعمال هرگونه تحریم آمریکا علیه خرید نفت روسیه به شدت مخالفیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/134343" target="_blank">📅 12:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134342">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بحرین: ما هم اکنون تحت حمله هوایی سنگین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/134342" target="_blank">📅 12:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134341">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
جنوبیا چقدر مظلومن! هم زیر حملات آمریکا هستن هم بهترین نظام دنیا برقشون رو تو این گرما قطع میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/134341" target="_blank">📅 12:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134340">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزارت نیرو: هفته آینده خاموشی مناطق گرمسیری و درگیر جنگ کاهش می‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/134340" target="_blank">📅 12:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134339">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EryiyAZty21W1XL--ZgvOfMit7Tn_ZHo5FRgZmk6zpDgbOM0W_3heOT7vREnjZ_2FqqBFWK_CFS0dB-USpHnhI7gyYlHOAoO-n2_DE3ydytJmd-HAK57VjaT5f4Fqfoyr0OfN43-cm5jEhw5HDM_gm3krQcxmhUAYLjSCNs1DQdHUSZiQWnjOI2QCAcFytY4SdlPcJTjExpF7Ic5PWz5YhVqMDsTBYGG9L1CE6a6T1l4Bx-ByQDt34nc5oAEsIw1Gr7X6Hv7A5kjK_oEhuubZqnq3THLMC8nnT129Qbo7WuWAKVyGcER-fjqjV7sXSHBuAp0-OZYQ5Bsnd2svqNdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ام‌جی لاریجانی : مردم خودشونو برای یه جنگ 3 - 4 ساله آماده کنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/134339" target="_blank">📅 11:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134338">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بلومبرگ: ۶۰۰۰ دریانوردی همچنان در تنگه هرمز گرفتار هستند.
🔴
تنگه هرمز همچنان برای کشتی‌های تجاری بسیار خطرناک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/134338" target="_blank">📅 11:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134337">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
استانداری خوزستان : دو انبار غلات و آرد گندم در دشت آزادگان و هویزه مورد اصابت پرتابه های آمریکایی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/134337" target="_blank">📅 11:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134336">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری / سپاه
:
اگر صادرات نفت و گاز ایران متوقف بماند، مسیر صادرات متحدان آمریکا را مختل می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/134336" target="_blank">📅 11:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134335">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYJM22WjBRMZ850O9URoHz78wJ3kEX4-iQyQF8qViSkqnMUCSJWdvb9Q2JFUtcP5N55WwOm5LR7z_k6IYfk00KDmkMdhBqghdsDsoVLnKV6wxlpgDhWrjzNmg6OtbQALn9ytlNsDO3s_kwBn77VREkiA43BtmybgkHOQdR0Jgoc8os1wWeMuaCF6cdctjhSkk8FSyBlDV4sJ4Y6Om096R3Sws3ngPV1djpjz9PS3AD52TbmHkRSN8D-Njk7o3501i_YpgQvubzhSTvswGBAdF9dKcCr__etRmdWC9iIZQJNz7OilhL7Tdfzzs-oQGDiOSxo3ZHR_bFANHA4KyHcVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طرح جدید دیوارنگاره میدان انقلاب با  شعار "ما ترامپ را می کشیم
"
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/134335" target="_blank">📅 11:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134334">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
انفجار در بندر کنگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/134334" target="_blank">📅 11:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134333">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72056fdffd.mp4?token=ezkm7O-SFcS7FB4DqsvjDTvr4aXajpYge3mMubQg3-l0iuPoJnrPNeFVBYp2son_cuzC6Z_th-LrGzUKtHgFqNz2Z8Hlm_2N-ScRGO3XPq56ej7aVcDDNiSfjbn9tXWqql_ofrhqpUJ6kspO6yUs_zNHLWX0gNFA4fwisNto3vqlX3-JQIJj2fqJeVr0WnVHGMkXlzy5AJnIsVdpsNQ66cJu7--Ca88hrdA0wxBMcuuBG_hdmVK-5ffNDWrDb_RCXJ6GY0LJKFPWgf_Sh9NYfGvyuet8SS2RHU3NvGJIB7Jt_ypbgzqFlxg353JKSiq-5aGBOtoU49basHQfG5pRzq4XgZRp7L2kFjyNO3StWpsuDScw-N5NsJ1w6P-dlGkosnAhxRinmpkJ-r18-2oT89M9rkFd7pk6WxDC-v7HtXPNbPrhXvvtDdIPGq0yQ2lPFuhBp2ZduNw3Ush_4BuKJnRmeTHRz_NsLGGTdKfGBuEo3_XRUyAaXdfn2Mg4CZt0EJquNy7PV2XISqL7pBT9-0SBZOS-lZvmuefw-MTqo1H950FgWb7wSok0DJNvMmgjSBsQgH6jOwoKjOKO7peO-2n-VLv0_R62Py4y3tvgHlIXc-PDhkTWvNS74Qig0IZCLPwFk2iiV6GgYjH7F42Y18G6wQfTuzoKJFDZ9uMO4PM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72056fdffd.mp4?token=ezkm7O-SFcS7FB4DqsvjDTvr4aXajpYge3mMubQg3-l0iuPoJnrPNeFVBYp2son_cuzC6Z_th-LrGzUKtHgFqNz2Z8Hlm_2N-ScRGO3XPq56ej7aVcDDNiSfjbn9tXWqql_ofrhqpUJ6kspO6yUs_zNHLWX0gNFA4fwisNto3vqlX3-JQIJj2fqJeVr0WnVHGMkXlzy5AJnIsVdpsNQ66cJu7--Ca88hrdA0wxBMcuuBG_hdmVK-5ffNDWrDb_RCXJ6GY0LJKFPWgf_Sh9NYfGvyuet8SS2RHU3NvGJIB7Jt_ypbgzqFlxg353JKSiq-5aGBOtoU49basHQfG5pRzq4XgZRp7L2kFjyNO3StWpsuDScw-N5NsJ1w6P-dlGkosnAhxRinmpkJ-r18-2oT89M9rkFd7pk6WxDC-v7HtXPNbPrhXvvtDdIPGq0yQ2lPFuhBp2ZduNw3Ush_4BuKJnRmeTHRz_NsLGGTdKfGBuEo3_XRUyAaXdfn2Mg4CZt0EJquNy7PV2XISqL7pBT9-0SBZOS-lZvmuefw-MTqo1H950FgWb7wSok0DJNvMmgjSBsQgH6jOwoKjOKO7peO-2n-VLv0_R62Py4y3tvgHlIXc-PDhkTWvNS74Qig0IZCLPwFk2iiV6GgYjH7F42Y18G6wQfTuzoKJFDZ9uMO4PM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بندر فجیره امارات که مهم‌ترین مرکز جابه‌جایی نفتکش‌ها در منطقه بود، پس از حمله موشکی سپاه به دو نفتکش(VLCC) از چرخه فعالیت خارج شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/134333" target="_blank">📅 11:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134332">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: نتانیاهو شنبه به واشنگتن می‌رسد تا در مراسم خاکسپاری سناتور لیندسی گراهام شرکت کند.
🔴
وب‌سایت "یدیعوت آحارونوت": زمان دقیق ملاقات نتانیاهو و ترامپ هنوز مشخص نشده است، اما انتظار می‌رود که آن‌ها اوایل هفته آینده با یکدیگر دیدار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/134332" target="_blank">📅 11:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134331">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
قیمت دلار آزاد به ۱۸۶ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/134331" target="_blank">📅 11:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134330">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFvtCRj3ub0qhRtZ3kk8AXNvB485NbhGXgYt7-Ee4-xrCG7qoPviagO3JiWkxBy15G0cmF0NvH_stHWWezjDJwl1joKH2pnK4S8OCmy3LjYENZLe8XGaPHZ_2AfsKWKJ8yvrJoWIK5G_RUigp3uiBY3keVMsYiVO7-Rj685Z0OnDuZZ3S4U7xFj2MDgeD-DCNdVuGiVie3cTZZ9Z48N1d4WjCWjhoiMlH9a9eHt6VcdoKCg3u9zf_lHCGS2ec2dcvZ3SowVV7mfJMTQy8zEx1Phrjfn1ZcNCF2Pf_rVNUc4ylJpp-gNFUPOSa5ZfuHwABWDjxbllVg9jsnrxrSS7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش روسیه به دنبال نصب رادار بر روی بالون برای استقرار بلند مدت آنها در آسمان کشف پهپادهای اوکراینی که به طرف آنها پرتاب می‌شوند است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/134330" target="_blank">📅 11:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134329">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa0f0b984.mp4?token=m7-bpSh98MiAYp3pkxC3JdWoQKxjmeSgBD0Y7E6x3zBHCNTAKi08BFHWgaq_YKAgJcXPxEbp75OreX9K0-2Q5Onj-H03J9LQL8UtsDLWBQabVUySGfPxu8tvvbw93W8iumkJH6A6lRuInj4tGjnwKaAVcZMQr0mqXKweoIxCYGnfWmUoDsYYbIfq7UFwTOOAjKr-yY0dQ1ttCvzQ16wrsQOAoimehsalPmm64ekFMu_mSC42mzVs5dviSoThxcLQ8pLC5I80ZAdPXfCtxy0mRaV6oJpOCvFnv1ORanxuMIw6YMfJ0wZabzMCpbTZv3yNJ-u3n8TYTuMZ_18qXUGVHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa0f0b984.mp4?token=m7-bpSh98MiAYp3pkxC3JdWoQKxjmeSgBD0Y7E6x3zBHCNTAKi08BFHWgaq_YKAgJcXPxEbp75OreX9K0-2Q5Onj-H03J9LQL8UtsDLWBQabVUySGfPxu8tvvbw93W8iumkJH6A6lRuInj4tGjnwKaAVcZMQr0mqXKweoIxCYGnfWmUoDsYYbIfq7UFwTOOAjKr-yY0dQ1ttCvzQ16wrsQOAoimehsalPmm64ekFMu_mSC42mzVs5dviSoThxcLQ8pLC5I80ZAdPXfCtxy0mRaV6oJpOCvFnv1ORanxuMIw6YMfJ0wZabzMCpbTZv3yNJ-u3n8TYTuMZ_18qXUGVHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره رئیس جمهور ترکیه، اردوغان، گفت: من فکر نمی‌کنم اردوغان باید هیچ سلاحی تهیه کند. او خودش سلاح می‌سازد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/134329" target="_blank">📅 11:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134328">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4285afbb6f.mp4?token=Mjh0SG6qoOip4SxqwaAi7Rsq-dlGpPtlRmchZW_TVVCrkvYsDM7OuJXiCtmfd5JuhEFKSMiPMxyqcdnyrI94bWkcRrUG8XOQJsmNTjzZrk5irvp-YR7j6tYT4jRzSL19JKW1fiTwcxnQYVWf0mj5f13_kVwZeMkaKC_U7-X3KPvz33dPWK-wmHzDJ3shFys8c0NOj8DtoV0eH9QTBpq-ywuSeldEyhyi4t_MM7auVy8AVoeNHib1PrkM_QvYhk_nxwAFvk4-v268Ua2e21FRSTdKjAeogVYpU7CX9WpezzvYlynAbGBTmI0Xijvebaab6A3kJI55R0zZjo5z5Ua_wDdl76xFJCqBmF2-hdQvxRg49CIrpMHeZ-y3vj8ChJwYq3T8YSsRemCwP0oTxkQRCcTmBJKar1jMI69Kua2XdYObkhQ6818GBDcWJ0KAXvxq2sDfcsBJeDVGpdxm-VbwkYaNBOiB4RvDeEd4T5DnWxz9SR8WnBkIwehXmn2St4JVokZ0_yqmvcUcZlyhDGYM9ueD_D05zgSfEcyV8iMizle_T3Kkc9JoJbyZa1YqSh4TIoeiAipS-jy45eQmcwEzAA_oCNTlIlOWmqipLl4oI310S2zWySoBTNAADyRwIGPHiOtiqflpirlCMow_Nw-ucN6G6t0Isczd6uNAPE5HjsM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4285afbb6f.mp4?token=Mjh0SG6qoOip4SxqwaAi7Rsq-dlGpPtlRmchZW_TVVCrkvYsDM7OuJXiCtmfd5JuhEFKSMiPMxyqcdnyrI94bWkcRrUG8XOQJsmNTjzZrk5irvp-YR7j6tYT4jRzSL19JKW1fiTwcxnQYVWf0mj5f13_kVwZeMkaKC_U7-X3KPvz33dPWK-wmHzDJ3shFys8c0NOj8DtoV0eH9QTBpq-ywuSeldEyhyi4t_MM7auVy8AVoeNHib1PrkM_QvYhk_nxwAFvk4-v268Ua2e21FRSTdKjAeogVYpU7CX9WpezzvYlynAbGBTmI0Xijvebaab6A3kJI55R0zZjo5z5Ua_wDdl76xFJCqBmF2-hdQvxRg49CIrpMHeZ-y3vj8ChJwYq3T8YSsRemCwP0oTxkQRCcTmBJKar1jMI69Kua2XdYObkhQ6818GBDcWJ0KAXvxq2sDfcsBJeDVGpdxm-VbwkYaNBOiB4RvDeEd4T5DnWxz9SR8WnBkIwehXmn2St4JVokZ0_yqmvcUcZlyhDGYM9ueD_D05zgSfEcyV8iMizle_T3Kkc9JoJbyZa1YqSh4TIoeiAipS-jy45eQmcwEzAA_oCNTlIlOWmqipLl4oI310S2zWySoBTNAADyRwIGPHiOtiqflpirlCMow_Nw-ucN6G6t0Isczd6uNAPE5HjsM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه‌کننده: زهران ممدانی (شهردار نیویورک) بارها و بارها شما را تهدید به دستگیری کرده است. آیا نگران این هستید که وقتی در ماه سپتامبر برای مجمع عمومی سازمان ملل به اینجا می‌آیید، او این کار را انجام دهد؟
🔴
نتانیاهو: نه، نگران نیستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/134328" target="_blank">📅 11:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134327">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2a6279b60.mp4?token=J-wwJyljvd6dsB9ECb6Kl5pdXcyl7_kjWLkWTDw3kw-p4FBHv7IZB73Di9zNk5HXaqeWD_C1H9DOiuQORWp5g1_RoaRcJlb2oS8moL0xehB1v3DRY1--BbvbjJCwlbHSDXemAAGGcKqXJy98XwhZ4tz-f9gZZL-e1VxoY3sDVNpi1avR8U-NgxQ4DWxJ6cyD4UCMdGjjwZWYWn6Wizw6KE8krfZA1VuRrDlG7nMTSJ8evT4U2xlf_np9xPD3yhqLq44xQ89n9LwfQ8z3Z_VqKpQ34vcUsPbhZk5VUHOscEYp_m4pprP8z87CJtEDe7VtSyjhyE7igsFoeAF7OybS6Tx_xLJy28h_xu7YM_Tnwqsf5AgroYjoK3VJVUoDNlv3YNjgLG37sWgGx0JYyNW_LkuphHSUYGu079m1eWUD3e_Sy07tAz8z8UU4b93WqW9syow4Q7QfG-8UlxpUSfGdYi7sd5uba39ZbV6-vU3JTbpcCE_NZCgDBbwSrd0vLe2fQaIVkRWekHVZkI7Ot6qiksS2pw6gzrz_pr7GJUX-ptHIa_geWHtuYILbCW4Xj_IoARaV8UD9Dnay0D4V_I4q5EpRIq1fcLTbawqph9VgDx0njns_L8occ7nFOPv1jEktombpZyxF_n_MbqGg-opEwaLoj1mQWDtHxT9K8SR1xlI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2a6279b60.mp4?token=J-wwJyljvd6dsB9ECb6Kl5pdXcyl7_kjWLkWTDw3kw-p4FBHv7IZB73Di9zNk5HXaqeWD_C1H9DOiuQORWp5g1_RoaRcJlb2oS8moL0xehB1v3DRY1--BbvbjJCwlbHSDXemAAGGcKqXJy98XwhZ4tz-f9gZZL-e1VxoY3sDVNpi1avR8U-NgxQ4DWxJ6cyD4UCMdGjjwZWYWn6Wizw6KE8krfZA1VuRrDlG7nMTSJ8evT4U2xlf_np9xPD3yhqLq44xQ89n9LwfQ8z3Z_VqKpQ34vcUsPbhZk5VUHOscEYp_m4pprP8z87CJtEDe7VtSyjhyE7igsFoeAF7OybS6Tx_xLJy28h_xu7YM_Tnwqsf5AgroYjoK3VJVUoDNlv3YNjgLG37sWgGx0JYyNW_LkuphHSUYGu079m1eWUD3e_Sy07tAz8z8UU4b93WqW9syow4Q7QfG-8UlxpUSfGdYi7sd5uba39ZbV6-vU3JTbpcCE_NZCgDBbwSrd0vLe2fQaIVkRWekHVZkI7Ot6qiksS2pw6gzrz_pr7GJUX-ptHIa_geWHtuYILbCW4Xj_IoARaV8UD9Dnay0D4V_I4q5EpRIq1fcLTbawqph9VgDx0njns_L8occ7nFOPv1jEktombpZyxF_n_MbqGg-opEwaLoj1mQWDtHxT9K8SR1xlI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره زهران ممدانی: فکر می کنم زهران ممدانی پنهانی از آمریکا متنفر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/134327" target="_blank">📅 11:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134326">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نتانیاهو: مرگ لیندسی گراهام ضایعه بزرگی برای اسرائیل است.
🔴
اسرائیل تنها کشوری در خاورمیانه است که خاورمیانه را متحد نگه می‌دارد.
🔴
ما از تسلط رادیکال‌های اسلام‌گرا بر شبه‌جزیره عربستان، اردن و مصر جلوگیری می‌کنیم.
🔴
اگر با جایی که ما در ۷ اکتبر بودیم مقایسه کنید، اسرائیل بزرگترین بازگشت را در تاریخ داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/134326" target="_blank">📅 11:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134325">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
جدول خاموشی مناطق مختلف تهران منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/134325" target="_blank">📅 11:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134324">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
قتل ۲ زن سالخورده به دست پرستار خانگی / متهم: من کلا اعصاب ندارم!
🔴
متهم ۵۵ ساله که به قتل دو پیرزن زیر شکنجه اعتراف کرده، درباره انگیزه خود گفت: من اعصاب درست و حسابی ندارم. وقتی می‌خواستم به آنها دارو بدهم و مقاومت می‌کردند، مجبور می‌شدم آنها را کتک بزنم تا داروهایشان را بخورند.
🔴
وی درباره قتل دوم افزود: به خاطر مسائل و مشکلات زندگی‌ام ناراحت بودم و حرصم را روی او خالی کردم. فکر نمی‌کردم فشار دادن گردنش باعث بد شدن حالش شود و او به کام مرگ برود.
🔴
متهم که سابقه پرستاری ۱۵ ساله دارد، درباره نحوه فرار پس از قتل اول گفت: وقتی خانواده پیرزن به من اطلاع دادند که او فوت کرده، ترسیدم و گوشی تلفن همراهم را خاموش کردم. با گذشت زمان، وقتی دیدم کسی به سراغم نیامد با خودم گفتم حتماً پرونده بسته شده است و دوباره به سراغ پرستاری رفتم.
🔴
بر اساس گزارش، این پرستار خشن پیش از این نیز در سال ۱۴۰۰ توسط خانواده یک زن سالخورده دیگر به اتهام قتل شکایت شده بود، اما به دلیل فراری بودن به نتیجه نرسیده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134324" target="_blank">📅 10:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134323">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m81HXdykCtWwOjOgWB2yEPk2OaMI3gfuirTFbTACYzL2ske11E2SWM-sIoY_bFoHvYfS-8nPh5TGaBpidaXAGSwroBXVtLJdfmrLCp8s418M0iYjsdk6DqwM3-CXfV0HSLyKZy816RRYAnjZjsSUZ6BvgU4vkzo4vcMeYqRLWe_8_qfm41xGfJ11an-MyaS2vHAE-NLaArzyX93X1Ofep0rMogYPhgsG4zhkAc_dhlUGuvATyhQqZdpIHs8htYv2RQoShPf3QegeQJ1jkx6cDL4v6ySiRwg3o4JMjWq_H1Q3c_5zlfhuzPy_0TnZVW99P5J1uZD5S7uQUeAk98jhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت با ازسرگیری اعمال محاصره دریایی بر تمام بنادر ایران توسط دونالد ترامپ و پاسخ ایران با انجام حملات در منطقه، افزایش یافت
🔴
برای دومین بار، نفت برنت در بالاترین سطح از ۱۲ ژوئن و نفت وست تگزاس اینترمدیت در بالاترین سطح از ۱۵ ژوئن بسته شدند و در معاملات صبح امروز چهارشنبه نیز به روند صعودی خود ادامه دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134323" target="_blank">📅 10:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134322">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqkKVGpKof_JmKm8PSq7t2bvbbGi5oxxQZ-M4FuR1hG125CY7Vw4Ppc53CavVsEcYHu8lwLr-32xqxRuMlfQ_9FW08SCnCQKmrS8lOQeUZ6Hsj8fdz3ImNvpjIH8yPNjQ-95cqi9b-BI8TehSixcpquRwGoX-k2YdDnUFous4E7riR-sAZ8X7oCi1LnBxr8eXL2NqVMpZ1cjD-upPtDELEuiLpUJKlq5g72rrcXzehr0hEIazG03LWIBU7dCXb0DtL7eP_6GgMFskXl2_R6nbbipIkxxVmlJdmzi1-BeuqKZDQUfk3ISUeGocjLnaovEW8nl3qLC6Jn0D25KwEpQ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: امارات متحده عربی، پس از کمک به آمریکا در جنگ علیه ایران، از طریق انجام ده ها عملیات هوایی علیه ایران، به مزایای قابل توجهی دست یافته و به دسترسی گسترده‌تری به تراشه‌های هوش مصنوعی از سوی ایالات متحده دست یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134322" target="_blank">📅 10:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134321">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رئیس مرکز ملی تغییر اقلیم هواشناسی:با گسترش پدیده النینو در اقیانوس آرام در پاییز و زمستان امسال بارش های خوبی خواهیم داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/134321" target="_blank">📅 10:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134320">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3194c525fb.mp4?token=FzOrmgxQ1O5fMgr1Nad4764IoS85_O-9Wd54qtbtRH_0OzWVCciejckxXrLH20z-GbwxGx5kvF6rNy6V8Zqwn3TGv1O3Yth3kiOcXN7PDtvbgBIeraB3d0aQda03CnkjARRmY40RM9dESuivk6OKNWk9se_Zu7VnCNmL9VU9dDjG95jjbleNMpHdvtOk6pFleLnFUXaFV5Y1bChVPBTtZJ0j39eadKrCgwCicGeSxq0ZYF7xJVTfwv7Aic9NOf34iH3sXVYnrclsfWqZEXcCkQuBLqQ_J9lrOoPFwX4ny94bmmrwuhl8H71CY6WatRbuBJzG8uy1eweiQyjVTE8U_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3194c525fb.mp4?token=FzOrmgxQ1O5fMgr1Nad4764IoS85_O-9Wd54qtbtRH_0OzWVCciejckxXrLH20z-GbwxGx5kvF6rNy6V8Zqwn3TGv1O3Yth3kiOcXN7PDtvbgBIeraB3d0aQda03CnkjARRmY40RM9dESuivk6OKNWk9se_Zu7VnCNmL9VU9dDjG95jjbleNMpHdvtOk6pFleLnFUXaFV5Y1bChVPBTtZJ0j39eadKrCgwCicGeSxq0ZYF7xJVTfwv7Aic9NOf34iH3sXVYnrclsfWqZEXcCkQuBLqQ_J9lrOoPFwX4ny94bmmrwuhl8H71CY6WatRbuBJzG8uy1eweiQyjVTE8U_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قطار باری در محاصره آتش‌سوزی مهیب جنگلی کانادا
🔴
گسترش آتش‌سوزی‌های جنگلی در استان انتاریوی کانادا، صحنه‌های هولناکی را رقم زده است.
🔴
در یکی از این حوادث، یک قطار باری در محاصره شعله‌های آتش گرفتار شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134320" target="_blank">📅 10:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134319">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiraWxcroMkJpvcmCGnl3HsSc7Uc4iEfTNymj0IQOC6ilbTeliKZ3uh9XW8zDYNXL73QuFxudJXB4gZ7BPXhHnuJ2hnttj7uvLFTjB9rR78cELf0p5Nb8vR6po-GiBDeM6UjEc12Dwzdtdc3F2zJy5F_8sFSJ29jtfbyuN2S5IFuue43p46nJa0zqb26RomWf3wimK7B5v_3N_L_XpkdyjVviAft9VCdM65QL1UXgBPk5PHxiwyh5EHkS6Z8zUp7Stxpylx9ihm_RWaT-BV17HrU8uhLOKzbOhFmwiHbqQEW1y8c3-hJNU_BYrqGKRS0OKqmzZsKOeVN8mMdZkQSSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی دولت: در حملات  آمریکا به جنوب کشور، بیش از ۳۰ تن از شهروندان غیرنظامی جان خود را از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/134319" target="_blank">📅 10:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134318">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
فرماندار بوشهر گفت: ساعتی پیش سه نقطه شهر بوشهر مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134318" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134317">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9JZp_R0gQOoXqxRfjgpFj8wakVbtTCwgngkDmCTxros_PKO5J9pn6zRnsqTPhDmK3auN3o7R73aTke55Ffb7kNbJw-E_3R7puygj1AsR-p64UbGglxtLeNOE_CFWFsygqPKQG2xNe-ZolREEu2sgyGa5KZ8CP6DhtO0LPhNFjYQNQ-IBOIM-KC6DnoqIcBCHbK2DWnfItPyZ-XaGwg9GwxCY3zPN3UFrnMVeFNnm49urDzUeb5k3fGgfTOB9tUa8wlvwok6wh-nHOKuCI3rt4gW6OqArZSxhqTVq8ZqGWzlP9YZItzQmq2KrZ530z1m3whPvpsV5jMXboB0ZOGiAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدول خاموشی مناطق مختلف تهران منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134317" target="_blank">📅 10:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134316">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
دموکرات‌های سنا به دلیل مخالفت با جنگ ایران، لایحه ۱.۱۵ تریلیون دلاری بودجه دفاعی آمریکا را متوقف کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134316" target="_blank">📅 10:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134315">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635b715ae7.mp4?token=e2tmpAD0gIu93NCGCcaEvCvZEQPSGGWqlKToaG8RnhdoNGLuc8Q4LPKprRN2-vsnOQDAO_7UPCZbdohg4dkt-_-K8jgBaSjdqzCxeyK4_c54ztQVGZs8n15yeRQHthD3NiuCjYFSjI7v5kTI6TrU1pX9HYceA4M9sTWOZHEPSISwW6kUAZz0dz4PIrf0Zr1HSUgq_a47l8NVHk7WId8ngSYuZ5e4cGS8kWeZDv4fCRPp_uRKFQpl8S3iHRMlQjqqQryD8w0zx7VotP6AenZ4AdUbREDLOnN0zfn3gHUHe4G3LqddnCUHobhg3Tu3z9Mw3BmJhcWJQFB3IMyU6IftFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635b715ae7.mp4?token=e2tmpAD0gIu93NCGCcaEvCvZEQPSGGWqlKToaG8RnhdoNGLuc8Q4LPKprRN2-vsnOQDAO_7UPCZbdohg4dkt-_-K8jgBaSjdqzCxeyK4_c54ztQVGZs8n15yeRQHthD3NiuCjYFSjI7v5kTI6TrU1pX9HYceA4M9sTWOZHEPSISwW6kUAZz0dz4PIrf0Zr1HSUgq_a47l8NVHk7WId8ngSYuZ5e4cGS8kWeZDv4fCRPp_uRKFQpl8S3iHRMlQjqqQryD8w0zx7VotP6AenZ4AdUbREDLOnN0zfn3gHUHe4G3LqddnCUHobhg3Tu3z9Mw3BmJhcWJQFB3IMyU6IftFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از انهدام دقیق مرکز تعمیر و نگهداری جنگنده‌های پایگاه العدید قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134315" target="_blank">📅 10:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134314">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCEJpIpoP2gu7sWAyaLzMatRUhbobIY38e5nlnBXb0tK5Pmv9aGdFmGhhjMnENlLil_o7aJn0Yp5RnuA0FS32L2i8PWCH0P_BbkwTneb3CmsRL1dxPIb2dJttUOzIi5IJT27hXeg-UYWWSRK0vC2ZqYR56Z2Rr7Z8BlCqpR_my5SFh4TOELiIe49wBvystGa5KYW-RQvZ7SnHC97nxt-3txnjVmcCqLmO3xR9BUtT0YOjFYsgs7YLPXXUstVYIpL9SUX5BYrTs2BAuMq0RoIu5S8yQTXGP5QiwYF4AAphDctfJ9BVzxnITSaYxQ0eXDoGyi3Gh0F792t6PkpD8IHOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به حملات آمریکا به چابهار، صبح امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134314" target="_blank">📅 10:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134313">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رویترز: بر اساس داده‌های شرکت ردیابی کشتی‌ها، تعداد شناور‌هایی که روز سه‌شنبه از تنگه هرمز عبور کردند، افزایش یافت که بیشتر آن‌ها به تجارت ایران مرتبط بودند
🔴
هیچ تردد قابل مشاهده‌ای برای تانکر‌های حامل نفت و گاز از سایر تولیدکنندگان خلیج فارس ثبت نشد
🔴
۹ فروند از ۱۱ شناوری که روز سه‌شنبه از این آبراه عبور کردند، از مسیر ایران حرکت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134313" target="_blank">📅 09:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134312">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
استاد روابط بین‌الملل دانشگاه شیکاگو ، مرشایمر: جنگ با ایران وارد مرحله «اقدام در برابر اقدام» شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134312" target="_blank">📅 09:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134311">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21e369331.mp4?token=Cw6m6Uk2iqmULyimSJ15jabVLZVhSnRfhAwS0LrbOpaax909TnnfTNq3yrpOWeLvjIUCVkL_HxZCBwRkGWi_DzNU_zBLhUgDEOKj2OLZ_1jNNkOy8DcvAR_v0J3-lmeMvV4DRI-tzFQNuNmye2DDfqRpdkiOSOA_imLej91hIS_4Ne6jY0VUUbVRpneI6FBdcK9zaywg5zhNe5sh9iYUJt5xVp1Sq91_lUS5-R-ksa-QFA7S8IfTBciJLx-fnJHMKJvvQha01VH3J5XQpv-PCgGFh_Ymuy7bMU7siwFcwq3qr3Bvz3pOdonvKSJru9b7yyq-ilKxTvEexwCluEz8t4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21e369331.mp4?token=Cw6m6Uk2iqmULyimSJ15jabVLZVhSnRfhAwS0LrbOpaax909TnnfTNq3yrpOWeLvjIUCVkL_HxZCBwRkGWi_DzNU_zBLhUgDEOKj2OLZ_1jNNkOy8DcvAR_v0J3-lmeMvV4DRI-tzFQNuNmye2DDfqRpdkiOSOA_imLej91hIS_4Ne6jY0VUUbVRpneI6FBdcK9zaywg5zhNe5sh9iYUJt5xVp1Sq91_lUS5-R-ksa-QFA7S8IfTBciJLx-fnJHMKJvvQha01VH3J5XQpv-PCgGFh_Ymuy7bMU7siwFcwq3qr3Bvz3pOdonvKSJru9b7yyq-ilKxTvEexwCluEz8t4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منوچهر متکی: باید برویم زمینی، پایگاه‌های نظامی آمریکا را تصرف کنیم و صدها و هزاران سرباز آمریکایی اسیر بگیریم
#تریاک
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134311" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134310">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
الجزیره: افزایش قیمت نفت
🔴
قیمت نفت با ازسرگیری اعمال محاصره دریایی بر تمام بنادر ایران توسط دونالد ترامپ و پاسخ ایران با انجام حملات در منطقه، افزایش یافت.
🔴
برای دومین جلسه متوالی، نفت برنت در بالاترین سطح از ۱۲ ژوئن و نفت وست تگزاس اینترمدیت در بالاترین سطح از ۱۵ ژوئن بسته شدند و در معاملات صبح امروز چهارشنبه نیز به روند صعودی خود ادامه دادند.
🔴
نفت برنت با ۱.۴۶ دلار (معادل ۱.۷۲ درصد) افزایش به ۸۶.۱۹ دلار در هر بشکه رسید و نفت وست تگزاس اینترمدیت با ۱.۱۱ دلار (معادل ۱.۴ درصد) افزایش به ۸۰.۴۰ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134310" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134309">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ارتش اسرائیل امروز صبح عملیات تخریب گسترده‌ای را در چندین دره و خانه در شهر بیت یاحون انجام داد، و همچنین جاده‌هایی را که شهر بنت جبیل را به شهر مارون الرأس متصل می‌کرد، تخریب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134309" target="_blank">📅 09:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134308">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
مهر: برج مراقبت دریایی چابهار برای دومین بار طی روزهای اخیر مورد اصابت موشکهای دشمن آمریکایی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134308" target="_blank">📅 09:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134307">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
کیهان: دولت رسماً و علناً از تفاهم نامه خارج شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134307" target="_blank">📅 09:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134306">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a9d2a5de4.mp4?token=B_AS7Fug_aUkNUibSPfqYomnMWFgpNwtgOfvu2a06rkXKhzByacetHTefPO8TiAXLS169paDy5s_gDVHf8k9KLSO6Afba3ckoEGmAJv0lPVbOOHLxADGEXZ1wxb_p-HL0n3W-tG9LafKrQ6vTaeGUCyvdQTKEzh6KkSf161DIsZO69DIqqh-POfVzaUzJpR9VE823jS1vobefrWvckh05cZdTl1IvQYuMiWDL9PtLTAaBHHOfAOhAQ4rqIr5RXgSYeN05jhW4vZb_bOkgO8zlNO48u4n7ANESd28XdgjW0Nqxmd9RqANt8ebCV6oUhpv6Deid7QyjPyJJ8I2QrmkEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a9d2a5de4.mp4?token=B_AS7Fug_aUkNUibSPfqYomnMWFgpNwtgOfvu2a06rkXKhzByacetHTefPO8TiAXLS169paDy5s_gDVHf8k9KLSO6Afba3ckoEGmAJv0lPVbOOHLxADGEXZ1wxb_p-HL0n3W-tG9LafKrQ6vTaeGUCyvdQTKEzh6KkSf161DIsZO69DIqqh-POfVzaUzJpR9VE823jS1vobefrWvckh05cZdTl1IvQYuMiWDL9PtLTAaBHHOfAOhAQ4rqIr5RXgSYeN05jhW4vZb_bOkgO8zlNO48u4n7ANESd28XdgjW0Nqxmd9RqANt8ebCV6oUhpv6Deid7QyjPyJJ8I2QrmkEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از بمباران صبح امروز در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134306" target="_blank">📅 08:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134305">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
آکسیوس: ترامپ روز سه‌شنبه جلسه‌ای در اتاق وضعیت برگزار کرد تا در مورد حمله‌ای گسترده‌تر از حملات فعلی به ایران بحث کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134305" target="_blank">📅 08:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134304">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سوال فاکس نیوز از ترامپ: ردیاب‌های داده‌های کشتیرانی نشان می‌دهند که روز دوشنبه تنها ۱۰ شناور از تنگه هرمز عبور کردند؛ کمتر از ۱۰ درصد میزان معمول عبور و مرور از این آبراه حیاتی. وقتی می‌گویید تنگه باز است، منظورتان چیست؟
🔴
ترامپ: اگر مردم بخواهند از آن عبور کنند، باز است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/134304" target="_blank">📅 08:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134303">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
یک کارخانه تولید آب معدنی در استان ایلام اوایل صبح امروز مورد هدف موشک های آمریکایی قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/134303" target="_blank">📅 08:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134301">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqybb-ol-Er11TVAADBjXzfg6Pw5irpmdkv5kK0P3zsHlU3rGs1gJA-xFEWfZrc137o4wV76aLC-7Vs4ELX295rC_KCqN2qYunEjXs-tlOtpBUYadqldm_DNzMlkcNn6ksaPBeQfIJtGrbCfKmmQDWU_IvSwR2PQheDu65MSaxcKcvRAM588KRVfj9K7bXrn5T6HvuSUlrdBMNxaZ3ijx93mw_XQeVmlaavvOU2Fqdmm-yUaQ_BNNpo91fyXIZVPNb6e_GD72k3G4vCrY9yvKnrFO5tLrAyOVO8tPYZcGUqBCuBscrz4t2yLPrYBqz5EFFBe8YKXywS1AG2gTdgMJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKgwrze--tvQb5m7rmlt8Gy9rB6OQuLB5HQ-qN9jcCMhAm7d0EQdFHqvx3nhBICGYiIsgD77DpAJCOdacSXroWyoPQ4GzpU9cyGbGqs0K0FbOA_uJxQ6hAZyec7ozRkU9sb347IFvuyVj0FMkl_7szVWP4WQX5gE3HeYZSPlRoyKnm3tFEu8kmHk7F0AX7nmZeVKM8EBEKVgjwIUTyuhJHpKDZaKgNrsVmUllWIqaGLn14nbXMRJYlY4tildNZhbthZsFc20nSfgmzbe3goqhZvMpm1rVNkWrTrit3B7jlT_aPUgo-yIjPqoA2UTpHrHiSKYYV5XN0i_WjX75pHWIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره ای از یک انبار متعلق به شرکت «کویت و گلف لینک هلدینگ» (KGL) در منطقه «مینا عبدالله» که مورد هدف قرار گرفته و به طور کامل تخریب شده است
🔴
این انبار، مرکز اصلی لجستیک و پشتیبانی ارتش ایالات متحده در غرب آسیا بوده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134301" target="_blank">📅 08:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134300">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ایندیپندنت: ترامپ ۳۲ بار اعلام پیروزی کرده، اما امکان پیروزی ندارد
🔴
روزنامه انگلیسی در مطلبی با اشاره به اینکه آمریکا توان لازم برای پیروزی در جنگ علیه ایران را ندارد، گزارش داد ترامپ آمریکا و جهان را وارد بحرانی کرده که خروج از آن دشوار است.
🔴
ترامپ پس از حدود ۳۲ بار اعلام پیروزی علیه ایران، از جمله پنج بار در یک ویدئوی ۱۳ ثانیه‌ای در اواسط ماه مارس، اکنون عملاً بار دیگر وارد جنگ شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134300" target="_blank">📅 08:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134299">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBKyyJJtSHj-d5StT89EwpAhn8z9GfcJnu_cEo-476lFw0M1gGhbmOS2J7WBsp5EBx1LBhH_lqvOKfnfd4D4sKO8Gi5qqiyehGpD8a4Ld9tFkgf9uHRyd6dTgOjcMrxN38XZ-wqJfncrgFsclqSpVA1DEanup0zrsIa30jhKyvEXl-T-hJJmdMaqkdSb43kVM-oCbfMuf80n4L-IpYHPw89qhyN98WfFA3JyMkFFqa67L-X9DtRPEwq3gOMdQTzkfZ3zgdb36Nl0idAPZYBARt0-5njbA9yHr5YgCaSyhfHDz7XIaG-BunIAq42ICedG1Mpp0bSQ43nBbvO2e4LdXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که یک موج هفت‌ساعته از حملات علیه ایران را به انجام رسانده و طی آن، ده‌ها هدف نظامی در نزدیکی تنگه هرمز و در امتداد سواحل ایران را هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134299" target="_blank">📅 08:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134297">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e63b2cfb.mp4?token=wCQSWXehEsuRWfnZq7j_s9H9x6lUJgpnh_ZlwOTocfYrUhaPav_IIF_o1LI4SmRkpdNe_d4pVdNLoXRGxS4itde-ocBGfc-SLcfSAeSuU9-F-d4W0Inko3eBZawCNho9QWUekgqB7JP9ZtwMN93bYBe_kL7uxty3UzzeG48zqTNxpJDRIrHpgH2hm_lC4sujXBoGI3ie7ay44vekHHTECTGVnDGiT_hv2rcqA-BmnDBaNCy4smDDM7TuxzHDlx4OvOFd8UoFpa0X9hMtnr7q2FTt7iobVDJbYn1c8f97J7meYadrTn_zd2OZ3KxH3GUbXRDHzygIg-ByzdOjVCL1bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e63b2cfb.mp4?token=wCQSWXehEsuRWfnZq7j_s9H9x6lUJgpnh_ZlwOTocfYrUhaPav_IIF_o1LI4SmRkpdNe_d4pVdNLoXRGxS4itde-ocBGfc-SLcfSAeSuU9-F-d4W0Inko3eBZawCNho9QWUekgqB7JP9ZtwMN93bYBe_kL7uxty3UzzeG48zqTNxpJDRIrHpgH2hm_lC4sujXBoGI3ie7ay44vekHHTECTGVnDGiT_hv2rcqA-BmnDBaNCy4smDDM7TuxzHDlx4OvOFd8UoFpa0X9hMtnr7q2FTt7iobVDJbYn1c8f97J7meYadrTn_zd2OZ3KxH3GUbXRDHzygIg-ByzdOjVCL1bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات پهپادی امشب به کویت و بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/alonews/134297" target="_blank">📅 04:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134296">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
استقرار ایست‌های نظامی در مسیرهای منتهی به بیمارستان خاتم‌الانبیا ایرانشهر همزمان با انتقال کشته ها و مجروحان حمله به تیپ ۳۸۸ ارتش
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/134296" target="_blank">📅 04:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134295">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/134295" target="_blank">📅 04:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134294">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
اونوقت 4 تا جاکش مثل ا.ث و ح.ر و س.ج زیر کولر تو تهران خوابیدن و توییت میزنن میگن انتقام انتقام. بدبخت مردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/134294" target="_blank">📅 04:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134293">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وقتی پدافند نداری و نمیتونی دفاع کنی، نباید سربازای بدبخت رو تو پادگان نگه داری
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/134293" target="_blank">📅 03:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134292">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک زده شده است تعداد زیادی از سربازان وظیفه جونشونو از دست دادن و امار مجروحین هم بالاست
🔴
همچنین درخواست فوری از مرکز انتقال خون ایرانشهر برای اهدای خون در شهر بمپور برای مجروحین ثبت شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/alonews/134292" target="_blank">📅 03:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134291">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/563dcb40c1.mp4?token=Tj8t4GcMyMRXD2hPqhkHj0KqO5_zX8onpXAwPOGK3UcP5YfMckOjKj7CTIzMrYBNE87sQsk6_lSHkhFmA-sK65JIh72bnZ-K2C1TZHNm4Lf4A5jVqv6-h2nfkyVk-wDcOzdFKHMX6-2GF6PbDDPC-7M7urgU4aRNtRQ4WCvMYjR4d5F7nVYyXgIOGymwEgHmJIghRxcjQjLqDt-uVxmaQYzHVn6TpEpihvUD9yW7jJwwoR2qDjzw_TIUejY4kS4TUOB9NEgpxR-JrqpUz6ePCvuCGXe36GipYVWWFPyPEOnpN1hAF1nrgpt1uMv4svgH0LLxHH9thdUy-nc1F8kPBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/563dcb40c1.mp4?token=Tj8t4GcMyMRXD2hPqhkHj0KqO5_zX8onpXAwPOGK3UcP5YfMckOjKj7CTIzMrYBNE87sQsk6_lSHkhFmA-sK65JIh72bnZ-K2C1TZHNm4Lf4A5jVqv6-h2nfkyVk-wDcOzdFKHMX6-2GF6PbDDPC-7M7urgU4aRNtRQ4WCvMYjR4d5F7nVYyXgIOGymwEgHmJIghRxcjQjLqDt-uVxmaQYzHVn6TpEpihvUD9yW7jJwwoR2qDjzw_TIUejY4kS4TUOB9NEgpxR-JrqpUz6ePCvuCGXe36GipYVWWFPyPEOnpN1hAF1nrgpt1uMv4svgH0LLxHH9thdUy-nc1F8kPBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقرار ایست‌های نظامی در مسیرهای منتهی به بیمارستان خاتم‌الانبیا ایرانشهر همزمان با انتقال کشته ها و مجروحان حمله به تیپ ۳۸۸ ارتش
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/134291" target="_blank">📅 03:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134290">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پادگان ارتش و سپاه شهر بمپور که کوچیک ترین شهر ایران حساب میشه کلا ۶ کیلومتره با ۱۰ موشک فوق العاده قوی منهدم شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/134290" target="_blank">📅 03:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134289">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
۴ماهه دارن میگن پایگاه پنجم آمریکا تو بحرین موشکباران شد، مگه وسعتش چقدره تموم نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/alonews/134289" target="_blank">📅 03:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134288">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
حمله هوایی به دهلران
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/134288" target="_blank">📅 02:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134287">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ: همون‌طور که میدونید ما در قبال غیرنظامی‌ها خیلی محتاطیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/alonews/134287" target="_blank">📅 02:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134285">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ویدیویی از پرتاب موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/134285" target="_blank">📅 02:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134284">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf2e032d2b.mp4?token=XkRCXzA380rPlt5Z6R_H5YTuxv_rXJRftYBSg_p6JTnJNpK6vZPD--OjT9w3Wy2X0igMPOBkfoki6-rxYWPMtEGsTxNI6upAgdMBjAw6k-VM-TFIf7_DDK5VxInCZWTj02kAT-Dy8jgeAeGh8u6WizaN88wKErXhsqIwApUq5k2QPLiMbOPv9LOfwiu1v752ps0naw2i2h0JOx-3ZcptfQ960ze_tp2s6Q43VCJfpmvCgQeVUouD-efkAwBWSC53se9tI6Fiq-IUUwfHwEOrpT-GEbzF4hFF6mq84dU5XwJjkWsscYOT9oDyGJENoLE8vYDb5U1NtBTaZmqK1TpPEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf2e032d2b.mp4?token=XkRCXzA380rPlt5Z6R_H5YTuxv_rXJRftYBSg_p6JTnJNpK6vZPD--OjT9w3Wy2X0igMPOBkfoki6-rxYWPMtEGsTxNI6upAgdMBjAw6k-VM-TFIf7_DDK5VxInCZWTj02kAT-Dy8jgeAeGh8u6WizaN88wKErXhsqIwApUq5k2QPLiMbOPv9LOfwiu1v752ps0naw2i2h0JOx-3ZcptfQ960ze_tp2s6Q43VCJfpmvCgQeVUouD-efkAwBWSC53se9tI6Fiq-IUUwfHwEOrpT-GEbzF4hFF6mq84dU5XwJjkWsscYOT9oDyGJENoLE8vYDb5U1NtBTaZmqK1TpPEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از پرتاب موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/134284" target="_blank">📅 02:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134283">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ: رهبران ایران شیاد هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/134283" target="_blank">📅 02:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134282">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a85771210.mp4?token=kQbAfSzqyUr6FEXFSFkY_LoG3u_0kPq5RuS-V96NgRthZKgL7BfMYvTEVqn6h45cbzAeUJOER6EefpFqglIjUvfMMRy00-0S-gFclUEChAPSrfMjosDKwir13Uc3TNhDmggCtxyiTzV4nkXBBbYmE2BHqjNC3blVgXofSdf4DHn8SQZFlCsEclVviQsQvNJw9EE1OztKrd3yrknDX0uGJETlU4YdSmyzfUIg60mlMn3xjHN6gqWBONRV-jA0TTT2MXVtgFJf8n-TcaCOuFVGAxVl2f0fLpWVV2dJUxkcK8D5vabNAbhj1hh1ikU-xkGVRIaW6TTF9VuPcOWddkQ4Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a85771210.mp4?token=kQbAfSzqyUr6FEXFSFkY_LoG3u_0kPq5RuS-V96NgRthZKgL7BfMYvTEVqn6h45cbzAeUJOER6EefpFqglIjUvfMMRy00-0S-gFclUEChAPSrfMjosDKwir13Uc3TNhDmggCtxyiTzV4nkXBBbYmE2BHqjNC3blVgXofSdf4DHn8SQZFlCsEclVviQsQvNJw9EE1OztKrd3yrknDX0uGJETlU4YdSmyzfUIg60mlMn3xjHN6gqWBONRV-jA0TTT2MXVtgFJf8n-TcaCOuFVGAxVl2f0fLpWVV2dJUxkcK8D5vabNAbhj1hh1ikU-xkGVRIaW6TTF9VuPcOWddkQ4Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :من در حال حاضر نمی‌خوام مذاکره کنم بیایید که مذاکره نکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/134282" target="_blank">📅 02:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134281">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
گزارش شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/134281" target="_blank">📅 02:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134280">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=LJ46IGH4yBMWLier9tNT-HcqWpFouV_uk9WAaK7pTns7iz1Nqjepjnkpzbf6Z42tXjy6N8lpDccRKHdA-pdiS3pLWZ39Hd7WfUl0z4IFkbVS7-Vdom3BhIt1Iu-W68aBao2mqLaag3ctei1zcszmgJeccFC171QvQ_4LPhAoFL6TCXWDcy1Q5b0sAy_qYo9851bs-pvxeYelpiWHC-xPQL47l23YIxrM3xFz_A3o0l5nw2Qn7lQSQa4BnahWHV-SlYCUphjFnkP1dH-b6B6Y6fxv7jsA0lUQNuJ1HQvq0nL3QtQoh3L8LD-Q9ilruxTXAw13F-JkiwgfgLTV6UuB2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=LJ46IGH4yBMWLier9tNT-HcqWpFouV_uk9WAaK7pTns7iz1Nqjepjnkpzbf6Z42tXjy6N8lpDccRKHdA-pdiS3pLWZ39Hd7WfUl0z4IFkbVS7-Vdom3BhIt1Iu-W68aBao2mqLaag3ctei1zcszmgJeccFC171QvQ_4LPhAoFL6TCXWDcy1Q5b0sAy_qYo9851bs-pvxeYelpiWHC-xPQL47l23YIxrM3xFz_A3o0l5nw2Qn7lQSQa4BnahWHV-SlYCUphjFnkP1dH-b6B6Y6fxv7jsA0lUQNuJ1HQvq0nL3QtQoh3L8LD-Q9ilruxTXAw13F-JkiwgfgLTV6UuB2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در حال رصد «کوه پیک‌اکس» هستیم، چونکه گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کردیم.
🔴
ما دوربین‌هایی در اختیار داریم که قادر هستن نام و نشان شناسایی افراد رو حتی از فضا تشخیص بدن؛ این دوربین‌ها تمام بخش‌های پیک‌اکسررو پوشش میدن. اگر اونا کوچک‌ترین حرکتی انجام بدن، ما بی‌درنگ وارد عمل شده و هر اقدامی که لازم باشه رو انجام خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/alonews/134280" target="_blank">📅 02:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134279">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: آنها هنوز مقداری قدرت دارند، اما خیلی زیاد نیست. و میزان تضعیف سلاح‌هایشان فوق‌العاده بوده است. هیچ‌کس فکر نمی‌کرد که این کار را بتوان اینقدر سریع انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/134279" target="_blank">📅 02:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134278">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز گفت: من روی توافقی امضا نخواهم کرد که تضمین نکند ايران سلاح هسته‌ای نداشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/134278" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134277">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d738632e11.mp4?token=hv2KN15yc09EUXvYFQhEpY8Jtw9PUm2aMLj8-2pDhUtIPd6tev3W8Ej3hfxYUtXm-slNH78GlCpsL_TpGsIHmVkIDIBarppkTKvpzZI9LVC1Z1n_nM4WC59RzOKkHsM0ySUbrZKnlDI-Pc22rTsldvW4ya8fo13zNeX0QL3FK-k-w-0YBt0Z9T3V86PmU2P-9CUf96pj6V1FqHrsW3cGIrVxRsZyNUpGbBemp37b7Jml2AeEm8NxHNqYkoYLSAikgrbRlQaVFjfnZC_gdi3-B4Y_E1suwQJuw5qQB_P2ndnijgaWLzkGFaVvglugHPgA3TUYdPs0siI7KR45DltKFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d738632e11.mp4?token=hv2KN15yc09EUXvYFQhEpY8Jtw9PUm2aMLj8-2pDhUtIPd6tev3W8Ej3hfxYUtXm-slNH78GlCpsL_TpGsIHmVkIDIBarppkTKvpzZI9LVC1Z1n_nM4WC59RzOKkHsM0ySUbrZKnlDI-Pc22rTsldvW4ya8fo13zNeX0QL3FK-k-w-0YBt0Z9T3V86PmU2P-9CUf96pj6V1FqHrsW3cGIrVxRsZyNUpGbBemp37b7Jml2AeEm8NxHNqYkoYLSAikgrbRlQaVFjfnZC_gdi3-B4Y_E1suwQJuw5qQB_P2ndnijgaWLzkGFaVvglugHPgA3TUYdPs0siI7KR45DltKFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره ایران
:
‌اگر به تنگه هرمز نگاه کنید، پیدا کردن جایی که آنها چیزی دارند برای ما سخت است. باید جلویش را بگیریم.
ما باید آن را باز نگه داریم. من قصد داشتم هزینه ای دریافت کنم، اما در عوض آنها ترجیح می دهند پول زیادی را در ایالات متحده خرج کنند، که صراحتاً بهتر است، زیرا من ایده هزینه را دوست ندارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/134277" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134276">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ به شبکه فاکس نیوز گفت: ایران دو هفته دیگر از دستیابی به سلاح هسته‌ای فاصله داشت و اگر مراکز هسته‌ای آن بمباران نمی‌شد، این امر از وقوع آن جلوگیری نمی‌شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/134276" target="_blank">📅 02:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134275">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: آنها دیوانه هستند ولی ما دیوانه‌تر و قویتر هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/134275" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134274">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">گرفتار قومی شدیم که اگر نزاع کنند مزرعه را به آتش میکشند
و اگر صلح کنند محصول را به تاراج میبرند
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/134274" target="_blank">📅 02:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134273">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: تمام زیرساخت‌ها رو میزنیم و ایندفعه هیچ رحمی نمیکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134273" target="_blank">📅 01:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134272">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری/ترامپ: نمایندگان من یک ساعت پیش با ایرانی ها صحبت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/134272" target="_blank">📅 01:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134271">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f90678a516.mp4?token=ZU0svw6fkJoPXVpCjolXOTirlfSRYvihhMzFqd_l1UDaga0zsGns4CovsmQARtngTCjv7IcrSvgkQrS_pV6kH9vj_TnLR4mvBOlp88Nzb_8sTOI5xYC7qMmug7sczkw_5gXorOLYOQLZk4_DKRCN8J9O-St3b2XRRZXbqLgTym1ZsykvqG8nOIyhiqqrKz4MQsJhgFSRV7Xg9Vmmdx40jOBUvg3g9PXHsZD5Y4dnzfoP-ucBcqZEMsheII6i7IC7b6R3l8tKwnrN_ZMqUwvk_8DYaDebdCpyIhJsCzclUxxSQEmx7nsE51dahIMKBBpYG8MXmeavi0YokCF38rNHEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f90678a516.mp4?token=ZU0svw6fkJoPXVpCjolXOTirlfSRYvihhMzFqd_l1UDaga0zsGns4CovsmQARtngTCjv7IcrSvgkQrS_pV6kH9vj_TnLR4mvBOlp88Nzb_8sTOI5xYC7qMmug7sczkw_5gXorOLYOQLZk4_DKRCN8J9O-St3b2XRRZXbqLgTym1ZsykvqG8nOIyhiqqrKz4MQsJhgFSRV7Xg9Vmmdx40jOBUvg3g9PXHsZD5Y4dnzfoP-ucBcqZEMsheII6i7IC7b6R3l8tKwnrN_ZMqUwvk_8DYaDebdCpyIhJsCzclUxxSQEmx7nsE51dahIMKBBpYG8MXmeavi0YokCF38rNHEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : بهتره تسلیم بشید، چون چیزی براتون باقی نمی‌مونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/134271" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134269">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوووووری/ترامپ: هفته آینده نوبت پل‌ها است! تمام آنها را نابود میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/134269" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134268">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فووووووری/ترامپ به فاکس نیوز:
امشب، فردا و پس‌فردا به ایران حمله سختی خواهیم کرد و در مرحله آخر نیروگاه‌ها و پل‌ها را هدف قرار خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/134268" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134267">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری/فاکس نیوز: آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
🔴
ادعای ترامپ: «نه. گاهی اوقات به عملیات زمینی نیاز است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/134267" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134266">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: اگر آن‌ها با بازگشت به میز مذاکره موافقت نکنند، تمامی پل‌هایشان را هدف قرار خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/alonews/134266" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134265">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری/ترامپ:
حملات به ایران تا زمانی که من بگویم دیگر کافی است، ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/134265" target="_blank">📅 01:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134264">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8222026cf9.mp4?token=bTgVks_fWJftyl4gpeb1T_mDZbnaYcvfXqTOlDQMYhtDoEAWq9zux4sjs9Cl9DpqsjsO14b5wB7pKjoS1soBgMyxHgasmYt7ZxlwpmxfrBm7YpmOdDvnlt5uKVcjGT70l_vrO8JH_MCliWX8Aw6JYHJNnGCC7la_338-IYJqFB6OeSyDe08Xn1oo4CW2DrOmFiykONEUDZ5q7oEeTrvajOsPTAvqq1aPIG333jdTZPykWYTVlSMLc7sNW8yNMK23dsbWvh5urNyEOq0tjjv3E6eGkUYdh52hkkxhS6nZeoxmne6aQYYhdZMDT_rJ_44qFAGPArZRnKNxQ2cYhtSZBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8222026cf9.mp4?token=bTgVks_fWJftyl4gpeb1T_mDZbnaYcvfXqTOlDQMYhtDoEAWq9zux4sjs9Cl9DpqsjsO14b5wB7pKjoS1soBgMyxHgasmYt7ZxlwpmxfrBm7YpmOdDvnlt5uKVcjGT70l_vrO8JH_MCliWX8Aw6JYHJNnGCC7la_338-IYJqFB6OeSyDe08Xn1oo4CW2DrOmFiykONEUDZ5q7oEeTrvajOsPTAvqq1aPIG333jdTZPykWYTVlSMLc7sNW8yNMK23dsbWvh5urNyEOq0tjjv3E6eGkUYdh52hkkxhS6nZeoxmne6aQYYhdZMDT_rJ_44qFAGPArZRnKNxQ2cYhtSZBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستار هدایت‌خواه، نماینده ادوارد مجلس:
اگر هر ایرانی ماهی 1 دلار بده بعد از 12 ماه میشه یه میلیارد دلار؛ یک آمریکایی پیدا می‌کنیم ترامپ رو بکشه.
🔴
بعد کلاهش رو درمیاره میگه خانوما طلا بریزین تو کلاه من!
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/134264" target="_blank">📅 01:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134262">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2joaz8GPtBXCWYUaex9sHeDuonIHjv-lrFshayeZDrid2PYtwGDZ6SWnhBh5W7DBjtwq0wglmzdk-iySFy4S3b6-aQEZx6iVw3PJz8pYmogYgQJnaoSihheeUPucs0RUUZj-4ibCEkmLyENSn2ztlngpBFdxzFy6v5O7Z-BikbNZ_-l8xBc7EVD1TU3G87-_OtdVdNRmYjNpvgIA82sLAnoB7FmaWBy_1e8avWtlh619hrDOnV51pMddjY-fzvg97J9qthTC1vIgnbh1DNeBNdpL4VOSM6KbtDW_7XfJSfQPvpIQluT8Q-CpJrhff-KaibfEqXY7lXlW9BTTy59cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مغز عرزشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/134262" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134261">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
شلیک موشک به سمت تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/134261" target="_blank">📅 01:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134260">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
انفجار مجدد در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/134260" target="_blank">📅 01:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134259">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سخنگوی ارتش: تو موج هفتم عملیات «صاعقه» محل استقرار جنگنده‌های اف۱۸ در پایگاه الازرق اردن رو هدف حملات پهپادی قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/134259" target="_blank">📅 01:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134258">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/134258" target="_blank">📅 01:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134257">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4784c0afa9.mp4?token=piMDef5cXJXp5GSBY_9zT-NWgeW2BrsEg8Zq4a3LUK276OrlWENh4ucDyE3cZHLWc72UaoXEDCWHdmM2QJ1-PcyUvmi0ATWcp7OOIZghXUnYcvtxl9nhCjaAkA9fxDXvqMvIcui9keKTcjnmDIt5svsAO-J5inrX5TceRfyG_8OBnkmuLaU7F9R9K3UqPe5ZoPI6yO6X-Ubxx0LHHvQRyC7f4y6laten66aR8owBUETmwmLgSwBaXYdSqwy-owULHxDqFvfqwfD85Ks9-1Jm4KTqIS4kNxl2VpU0K4sf9mj2k2DXvH8PcbuqRsABTDfiQGKqpEdgCH1mIYL2VgonnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4784c0afa9.mp4?token=piMDef5cXJXp5GSBY_9zT-NWgeW2BrsEg8Zq4a3LUK276OrlWENh4ucDyE3cZHLWc72UaoXEDCWHdmM2QJ1-PcyUvmi0ATWcp7OOIZghXUnYcvtxl9nhCjaAkA9fxDXvqMvIcui9keKTcjnmDIt5svsAO-J5inrX5TceRfyG_8OBnkmuLaU7F9R9K3UqPe5ZoPI6yO6X-Ubxx0LHHvQRyC7f4y6laten66aR8owBUETmwmLgSwBaXYdSqwy-owULHxDqFvfqwfD85Ks9-1Jm4KTqIS4kNxl2VpU0K4sf9mj2k2DXvH8PcbuqRsABTDfiQGKqpEdgCH1mIYL2VgonnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دریابانی سیریک بمباران شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/134257" target="_blank">📅 01:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134256">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
طبق گزارشات تو چیتگر پدافند فعال شده و پشت سر هم صداش میاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/134256" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134255">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
پادگان ارتش و سپاه شهر بمپور که کوچیک ترین شهر ایران حساب میشه کلا ۶ کیلومتره با ۱۰ موشک فوق العاده قوی منهدم شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/134255" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134254">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نکته جالب اینه آمریکا این روزها فقط داره پادگان‌ها میزنه و گویا داره شرایط رو برای یه سری کارا و تحرکات آماده میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/134254" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134253">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
گزارش انفجار در تفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/alonews/134253" target="_blank">📅 00:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134252">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
انفجار در جزیره هنگام
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/alonews/134252" target="_blank">📅 00:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134251">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
گزارش ها از فعال شدن پدافند پارچین
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/134251" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134250">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
فرانسه هم باخت و تنها ۴تیم تا الان نباختن
آرژانتین، انگلیس، اسپانیا و ایران
🔥
🔴
باز بگید قلعه نویی بد هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/alonews/134250" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134249">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/torvpIseY5fEKlMAPZ4shXmOBxlbq6XIqy-U5-kSooA-5S_WoXPJnJQypcRPqrGc7JJbzlmSdRyey1pkQM53i1ZWUTasQl-gzUqRcgYl2JtEMqe2QG003Hc5lXB1ktzMs9Ae_QXlXYrjsB_WAizeBGApnSGbKxd2rjw-0HIo5ESjVdFjmAqFovYIdC1rwu2DuO7Fr4L67aExCH_6pBOb_J73NI2SFvAn3mOiZM5Q8aIGlZtH56dQB3FszkjeF8TVrOt9WvjKlfHehkVh7wt8BatyLFWE2KzH-1YzGpyT31LDCcJFCVLrfTU_aLyh7Lh6DrBTM7Ox-3qNZjjzAl_NRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانالای ایتا نوشتند که دست خدا عیان شد و این عکس باعث صعود اسپانیا به فینال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/alonews/134249" target="_blank">📅 00:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134248">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/134248" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134247">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WBS3u4nCDrxC9dhyVfY9gbqunc_CZ42HGhRcN2os9Iryveuz6Kn1lwjEv3toSQsLhyPEl6-As-e9yiF1LNHhX9pFBALHhBU7Mx7WvlZ8HONC6FVGy65j_TeDv-Oza0PSgWDV4tsUUE0id_S6tsbze7R26RZ4kimEXUfrBe9sLs26MrU6BPFwyb4fkp8mSr_R3HoA00dQXq99clmoFOWdkdEtXwqYG98ml9E-ehWPjDaOlgV2JwO4BmBgvTaQ6fwHAlXHquYP0M-Na8_A2_8Kxv1KFhNuJu77AfXn1wb99lLOEzn9ThesqXZOxJOLX9BdyTWJktn43FjjRhxTZHFVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و اما بشنوید از کشوری که در جنگ پشت جمهوری اسلامی بود و به فینال جام جهانی صعود کرد.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/134247" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134246">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxBI8hSSWAc73DhEfy_gNYQaJIrJ4_plzfqvBpD1IDlw5uqk5p71lKg4csb4-MP0tu8u07_mmYcsgMB9X9TP08xaFHXkSwpGeJ74LqLrOEX5M3FbngvBLSwUOLZ-HHvuYcPfopVk6EhckWJB5FTYdfaDQH5Zu2ylAPvdIh2Xq8O_LPFw-9orMUYQDTmI0G-Wt3fzoIiHhKxacQXhk7Muv9fAJQSbOqpoOntWjNmB-eJ7x31ULhBMF7N2J7_9IXf25LsqJkKfZk6_-BgpS1nQJ0duGsEfVWyyg3VD_2ZdH2NAXATkL5EpPdRWadai96kTgv37CGUl2dlYvA6Iqs9BwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا
2️⃣
➖
0️⃣
فرانسه
🇫🇷
اسپانیا رفت فینال
🔼
@AloSport</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/134246" target="_blank">📅 00:32 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
