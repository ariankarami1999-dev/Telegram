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
<img src="https://cdn4.telesco.pe/file/Gu6Hu8AZdNVofx05Txp8WwpBA64Cn9EFg5tLfgP0N0c3ax_GJB-AMqRCTP9z2dE6zHFZ2G967S6hC68ebaLE0Je1AeToMZQunVlXYCpRuEFBNjHxRX1nY_hMyQ3BxpXiOGGoCc16z6kkEBMSFQU0_cfhmN4yb4Udr8xcZkv-Sgu9Qpa-kDN_nXL64CggiqXamFIHkYdWYOzAsE9U4gZ8ppgquGCSsg-VKLoa3UsWaiaM6FM3SZfdKXw-mtDAEA52LODWnwthZxiqho1EjUTeupJxXlqdEXnhE-U2ZeVFxVttKSG8zPvCPLuEwNvGcsiY_b1TM-_8FLURzgyTSH0y6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 136K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 20:14:56</div>
<hr>

<div class="tg-post" id="msg-69475">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebsK6Fo6QmpuaXUmycwYB3ax_590M-EsSjPAzWyWHO6qDjKNO2TsC0srUZSdJ-L17JptfVYt2mHMMaOYaAWkr4_RH_vwzIMCW0JlDBfqLcZQ7akhAPysiPAyZ8csXYFJR7Uv8cNdWtD4A6gLmEBMwilOTMDpNHWcHTjEjSFlRAl-diviESTzoRvTUVxgy-ZmPl77RiwPqvo8t0UM9ZF4um70xOLQtshcmF0C6vCbGUbuCK3LYVchEuT1nTwJatoTq6W29wv2QSYVdYA_2A_MTowtzdM08i_UhTBlX3G4b67FBnT387qAwMAlvTdEo4FzQFQNy7yF9hL1NAIm4X_QBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ : رهبری ایران واقعاً یه جورایی دو‌رو و ریاکاره که باورنکردنیه؛
خودشون می‌خوان مذاکره کنن، بعضی‌ها حتی میگن التماس می‌کنن، مذاکرات شروع می‌شه، جلسه بعدی هم قراره به‌زودی باشه، بعد علناً و با افتخار میگن که هیچ مذاکره‌ای در کار نیست، هیچ صحبتی نمیشه و فقط با «عمان» کار دارن!
بعدش هم همون چرت‌وپرت همیشگی‌شون رو تحویل می‌دن که می‌گن تنگه هرمز رو با قدرت خودمون اداره می‌کنیم، در حالی که از قبل کاملاً تحت کنترل نیروی دریایی آمریکاست و همون «محاصره» یا همون‌طور که بعضی‌ها می‌گن «دیوار فولادی ایالات متحده»!
هیچی به ایران نمی‌رسه مگر اینکه ما بخوایم، و هیچی هم نخواهد رسید مگر اینکه یه توافقی بشه یا اینکه کامل تسلیم بشن.
فرقی نمی‌کنه ایران بخواد قبول کنه یا نه، واقعیت اینه که ما داریم درباره‌ی راه‌حل مشکلی حرف می‌زنیم که خودشون دهه‌هاست ایجاد کردن، خیلی ساده‌ست:
ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/news_hut/69475" target="_blank">📅 20:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69472">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4129d878df.mp4?token=hA6wNbI57NIY3sOiWUDWyhICJVMlEVB1b9_0lM1etRkNKHk2zlDZjQt-rAhdwjDKIboRzigVFpztCfe1wL1WpvpzkTiMcg5V0pRau-FmFo34ajMRkcQPSSi5Nb9t1e4saGLJxyVfxcwc8gq221NbFRatvnaL8WmNrPMGEVu-gplfkzjsfsNvN8DaUyWrWzoEWV-vThrslFe990h_GWjJojxW6JtfaQsd-4Do_zJ34pwU23g7kMbkTtXChQaf3F-QNRfOmJRlfCwOZaS-WD1LZ-e36yPQpE8U_9Xd33zncSEzYv-NGumLbKJ8zPBjsIuim3xWybQww81niEMCkQAnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4129d878df.mp4?token=hA6wNbI57NIY3sOiWUDWyhICJVMlEVB1b9_0lM1etRkNKHk2zlDZjQt-rAhdwjDKIboRzigVFpztCfe1wL1WpvpzkTiMcg5V0pRau-FmFo34ajMRkcQPSSi5Nb9t1e4saGLJxyVfxcwc8gq221NbFRatvnaL8WmNrPMGEVu-gplfkzjsfsNvN8DaUyWrWzoEWV-vThrslFe990h_GWjJojxW6JtfaQsd-4Do_zJ34pwU23g7kMbkTtXChQaf3F-QNRfOmJRlfCwOZaS-WD1LZ-e36yPQpE8U_9Xd33zncSEzYv-NGumLbKJ8zPBjsIuim3xWybQww81niEMCkQAnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
درگیری عرزشی ها و پلیس عراق در کربلا:
توی عراق یه روحانی به اسم صادق شیرازی، مخالف جمهوری اسلامی و خامنه‌ای هست، اون معتقده که فقط باید گفت لبیک یاحسین، نه لبیک یا خامنه‌ای.
حالا عرزشی‌ها دیشب افسار پاره کردن و هجوم بردن سمت موکب این روحانی و شعار مرگ بر آمریکا و لبیک یا خامنه‌ای سر میدادن.
عرزشی‌ها شروع کردن به کتک زدن مردم عراق تا اینکه پلیس وارد شد و با شوکر و باتوم عرزشی‌هارو کتک میزد.
طی این درگیری بیش از ۱۰۰ نفر به بیمارستان منتقل شدن و عراقی‌ها میگن دیگه نباید ایرانی‌هارو راه بدیم، غذای مفت میخورن و مارو کتک میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/news_hut/69472" target="_blank">📅 19:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69471">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=nkgMgChftkYryBhblIfyUjsQl5Y0bazNUyZ4ay-DXKspKxazLo4c5l1UdQBEE0lc3hnOxXjMmZFvwA8y95XuqDUdKyha55dnwbWDiX2g-mlofSWqO-pIseXUEmRsoRWjOKU1PjggLk4NOozAo-Y9W_zii4b7AsTLNhkv1iJCct_0a25CTk1xuQxgcpvLZCetFolD5H8VU3RcYcc1sxbLUef0xRn8i4m-SKS83kKH61CxbnzOVxB72o9SaSJGt-Fe8nJLHMOBWlOQe-8tb8PBTs-QGUAVV7RLPRVaOWomirZo9Fcc6AFWG7Prs0GmTySXHUNJdUciwxJhllkfvLFTi2BDA1OTSbjUYA6rnqKltORtfweGaImxyMgvRt7PRmk-8ICCTG5cwgudDI_v8yudL9Ye8D7QtH0cC1IX5BFNUeHjgeEezq3HLSwzhUqHNjU7YOFfeeYM7enF6nQfuVM4OevqP8mw6uZdf2-kG1Rl_-A4jICuJB0FR12hheD9d4Mc8JaRUkwcm_vVv2bd1VCoolMwThs71BXPmXlTPUCYyeLFqNDnNkBqBB-PYoGv-ltvUWrWef9gYAknlalt1iYVECKIkd8_uiWZOFayb4zvLugIk11O4x9J3y6ckQRfARgG87U7-6JgLyOA5IAEzUXS3e9e9MPcjE-JU0y_BXhhIgk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=nkgMgChftkYryBhblIfyUjsQl5Y0bazNUyZ4ay-DXKspKxazLo4c5l1UdQBEE0lc3hnOxXjMmZFvwA8y95XuqDUdKyha55dnwbWDiX2g-mlofSWqO-pIseXUEmRsoRWjOKU1PjggLk4NOozAo-Y9W_zii4b7AsTLNhkv1iJCct_0a25CTk1xuQxgcpvLZCetFolD5H8VU3RcYcc1sxbLUef0xRn8i4m-SKS83kKH61CxbnzOVxB72o9SaSJGt-Fe8nJLHMOBWlOQe-8tb8PBTs-QGUAVV7RLPRVaOWomirZo9Fcc6AFWG7Prs0GmTySXHUNJdUciwxJhllkfvLFTi2BDA1OTSbjUYA6rnqKltORtfweGaImxyMgvRt7PRmk-8ICCTG5cwgudDI_v8yudL9Ye8D7QtH0cC1IX5BFNUeHjgeEezq3HLSwzhUqHNjU7YOFfeeYM7enF6nQfuVM4OevqP8mw6uZdf2-kG1Rl_-A4jICuJB0FR12hheD9d4Mc8JaRUkwcm_vVv2bd1VCoolMwThs71BXPmXlTPUCYyeLFqNDnNkBqBB-PYoGv-ltvUWrWef9gYAknlalt1iYVECKIkd8_uiWZOFayb4zvLugIk11O4x9J3y6ckQRfARgG87U7-6JgLyOA5IAEzUXS3e9e9MPcjE-JU0y_BXhhIgk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
عملیات آزادی عراق؛
در ۱۷ مارس ۲۰۰۳، جورج بوش بزرگ رئیس جمهور آمریکا در یک سخنرانی تلویزیونی به صدام حسین و پسرانش (عدی و قصی) ۴۸ ساعت فرصت داد تا عراق را ترک کنند.
او هشدار داد که در غیر این صورت، حمله نظامی در زمان انتخابی آمریکا آغاز خواهد شد؛
پس از پایان اولتیماتوم، بوش در اتاق وضعیت کاخ سفید  او در آنجا دستور رسمی حمله را امضا کرد.
بیش از ۱۰۰۰ بمب که بعضی آنها ۱ تن وزن داشتند و ۵۰۰ موشک کروز تاماهاوک را به سمت مواضع ارتش صدام شلیک کردند، بین ۱۵۰۰ الی ۱۷۰۰ سورتی در ۲۱ مارس انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/news_hut/69471" target="_blank">📅 19:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69470">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=BmA3nJQN7mFXD-7a8rc2_mRBtCJlUid1z1gU14xf82G7dxbJUw0YiQnDqzBHc6mDfLrNRDSq50kt3LBMxt7MY6mOEmMm-U_xeI8U_I-Mhrs3S9NI2PzIRY1OoDLY4CZLRnCN3G65TbMwWsBLSpIJ3dECcLPDNbKy4PKgAbWD_wJqNnUrgHPujKmg2N4CcKNiU81-ROFXjDeoCOArl4DCc8mod2CC8YGHAOsZqMD8SC5ZzveB3c9mLAFOuQQJNTKfsXEKDMj4RUHORUEMRYwnkHW0GLcjT1eZkdhm-nyLn7o_P3nhHD4-G01LTweMm36r6TnhxwOC-CiSMYWWLAilcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=BmA3nJQN7mFXD-7a8rc2_mRBtCJlUid1z1gU14xf82G7dxbJUw0YiQnDqzBHc6mDfLrNRDSq50kt3LBMxt7MY6mOEmMm-U_xeI8U_I-Mhrs3S9NI2PzIRY1OoDLY4CZLRnCN3G65TbMwWsBLSpIJ3dECcLPDNbKy4PKgAbWD_wJqNnUrgHPujKmg2N4CcKNiU81-ROFXjDeoCOArl4DCc8mod2CC8YGHAOsZqMD8SC5ZzveB3c9mLAFOuQQJNTKfsXEKDMj4RUHORUEMRYwnkHW0GLcjT1eZkdhm-nyLn7o_P3nhHD4-G01LTweMm36r6TnhxwOC-CiSMYWWLAilcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
اکثریت قاطع ایرانیان، اسرائیل را تحسین می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/69470" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69469">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=MAVmGpWapRqkcAeXFk0PJMcnmQphyqun1VR4bOTEd_UaFW_EgpXtRBcUxKJdHqpCMKIA1YvEZc6AvoVRdvHO0zHxGtoZDITqzvw36dJZJwQwxd7XxwauCShN5yzgbUEl7jjmxszP6aPvRlIyrrg4HtzmuRT5FJmzVQeu015C4Y8mUFfMwQpbFQIZpWGhuSxpKd4ul0N316SHf6uPK-GASuQdWFgoO-xc5jDaqKGdo_-FpOIAZawdFowGYAqsUhp1TQJlvwxmZS0fQY-yl5l9FpTGJe1kq9iy1SgtRA-CJspxHbeFfhZue3s-QSRzHHByeEYRQUSI14qinguIU8NnBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=MAVmGpWapRqkcAeXFk0PJMcnmQphyqun1VR4bOTEd_UaFW_EgpXtRBcUxKJdHqpCMKIA1YvEZc6AvoVRdvHO0zHxGtoZDITqzvw36dJZJwQwxd7XxwauCShN5yzgbUEl7jjmxszP6aPvRlIyrrg4HtzmuRT5FJmzVQeu015C4Y8mUFfMwQpbFQIZpWGhuSxpKd4ul0N316SHf6uPK-GASuQdWFgoO-xc5jDaqKGdo_-FpOIAZawdFowGYAqsUhp1TQJlvwxmZS0fQY-yl5l9FpTGJe1kq9iy1SgtRA-CJspxHbeFfhZue3s-QSRzHHByeEYRQUSI14qinguIU8NnBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
خاورمیانه دیگر آن خاورمیانه سابق نیست. ایران هم دیگر آن ایران سابق نیست. ضربات سنگینی به آن‌ها وارد شده است.
آن‌ها همچنان توانمندی‌هایی دارند، اما به یک ماه گذشته نگاه کنید؛ آن‌ها به سمت ما شلیکی نکرده‌اند.
چرا شلیک نکرده‌اند؟ چون می‌دانند ما می‌توانیم چنان ضربه سنگینی به آن‌ها بزنیم که بازدارنده باشد. اگر به ما حمله کنند، متحمل ضربه‌ای بسیار سخت خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/69469" target="_blank">📅 18:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69468">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=taw5MPHXKFMHpGNL6lHRb_WLFRegE-5GuSmATvqWmZ1QOfyaB2WTR1SJm0QMlIsGU1fjy00zYXFaYQ1WxprWGdPNEo5ba0LybI_x97pL74nFfk8whqf3ocY2WK9zJhYBEvAGix_e1hQSpFSkYC6Y_d1bHta1ChYp4pSCecd9tpl9WSyyrQHxaZ7ci2npmBNXMwDIdJtplbKxQ2G4ijoqIF701UUY9Jb4sjzgvvPYQh4ZjYK9om3Mz9-KgFU16Zov-Gy2KmB_Ap_zNFLGmecrgb-Bi3blUO2RfwbCcLPixsfNLtJyAAoUsDLjLu3mPRZwf4LCKHYsiHmG7r9wCDagnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=taw5MPHXKFMHpGNL6lHRb_WLFRegE-5GuSmATvqWmZ1QOfyaB2WTR1SJm0QMlIsGU1fjy00zYXFaYQ1WxprWGdPNEo5ba0LybI_x97pL74nFfk8whqf3ocY2WK9zJhYBEvAGix_e1hQSpFSkYC6Y_d1bHta1ChYp4pSCecd9tpl9WSyyrQHxaZ7ci2npmBNXMwDIdJtplbKxQ2G4ijoqIF701UUY9Jb4sjzgvvPYQh4ZjYK9om3Mz9-KgFU16Zov-Gy2KmB_Ap_zNFLGmecrgb-Bi3blUO2RfwbCcLPixsfNLtJyAAoUsDLjLu3mPRZwf4LCKHYsiHmG7r9wCDagnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دیروز روسای دانشگاه تو جلسه‌ گله کردن که چرا حقوق اعضای هیئت علمی دانشگاه رو با تاخیر دادین؟
پزشکیان هم تو جلسه کلش خراب شد گفت:
نامه نمیخواد، اون گوشیو بده من بینم...
📞
«سلام؛ حقوق هیئت علمی دانشگاه‌ها رو ۱۰ روزه ندادین. خداوکیلی این درسته؟... بده دیگه... دستت درد نکنه، خداحافظ.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/69468" target="_blank">📅 18:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69467">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04343db3da.mp4?token=fpd0YViaD0r26dMOaAuxTjyy9JxjWQpiMInIRAyE-DwDIde3loID_2NCrS12FdGldxD5SFQTdWnR0P6swY7xN1IqB_rXHzz9SyR2bHs_b2bAsoftsSPVjQvAFCwR_5sXStaqiULHqcR3CgdPgX_ovHd5iBxFJ9HSQCzc2qSkZcrIXDw8WEMMjlwwah8zAoFEFyQLfzagRKKj4ac3D6oMChXxkUz4-LCve0clW_Jh0ca-744qHNspAm6u1BiiyRgoIBbC9RD2o5QEY2rDiqjvuIoL43ZPx_sRroY5gUjcMrm7e_gn8BYuU3nk-nKPbXf-DhUJDY7simNi_2-g2s8XOkdp5WNtAmf29MRg8ZxeyEnX8g07iNH60U0_7tPMvO0FWyfPjrHOHIdsJVL3Ebgxn6gzuDysAAHlaFcLSwFqouyW2BMzwTzJNOoXcHYxvi-3VeOi1uHEjzmeLUqepB0XN1pEwFqIcFdxoiT3vaM1IbvcuOdQAXIfTOpEwgGooRM7Zbxbb3v3QKND1mE-20BDlYqy98lzhHWdzzwTpJfKaZM8m6As9JGmICMPtBj9t04H4PDrMy4RnMmoKn_liDkhq7OhgW8sSyWA2wFC2ahPF888kwluAljgXYT_dDvRO_SQ1ljrGbzgf0VovBHQJnrKGudGqDQDVG8bpKl2CL4eTQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04343db3da.mp4?token=fpd0YViaD0r26dMOaAuxTjyy9JxjWQpiMInIRAyE-DwDIde3loID_2NCrS12FdGldxD5SFQTdWnR0P6swY7xN1IqB_rXHzz9SyR2bHs_b2bAsoftsSPVjQvAFCwR_5sXStaqiULHqcR3CgdPgX_ovHd5iBxFJ9HSQCzc2qSkZcrIXDw8WEMMjlwwah8zAoFEFyQLfzagRKKj4ac3D6oMChXxkUz4-LCve0clW_Jh0ca-744qHNspAm6u1BiiyRgoIBbC9RD2o5QEY2rDiqjvuIoL43ZPx_sRroY5gUjcMrm7e_gn8BYuU3nk-nKPbXf-DhUJDY7simNi_2-g2s8XOkdp5WNtAmf29MRg8ZxeyEnX8g07iNH60U0_7tPMvO0FWyfPjrHOHIdsJVL3Ebgxn6gzuDysAAHlaFcLSwFqouyW2BMzwTzJNOoXcHYxvi-3VeOi1uHEjzmeLUqepB0XN1pEwFqIcFdxoiT3vaM1IbvcuOdQAXIfTOpEwgGooRM7Zbxbb3v3QKND1mE-20BDlYqy98lzhHWdzzwTpJfKaZM8m6As9JGmICMPtBj9t04H4PDrMy4RnMmoKn_liDkhq7OhgW8sSyWA2wFC2ahPF888kwluAljgXYT_dDvRO_SQ1ljrGbzgf0VovBHQJnrKGudGqDQDVG8bpKl2CL4eTQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو ای از یک طرفدار حکومت که میخاد ترامپ رو بکشه:
میرم خون رهبرمو از ترامپ بگیرم یه دهنی ازش سرویس بکنم از یادش نره
از لحاظ دفاعی یا هجومی همه جوره دهن ترامپ رو میارم پایین
حرکت های رزمی‌شو ببینید فقط
😳
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/69467" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69466">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEP1e1phef8bjK2_8JSbUrwIUou7ZRtCRZ7vhFzRGU1c0kzsJFeZVHcCq4xUCIhitUjOii-NbT7b_p64lDqNHgYZADWXUaIOaJyHChejy8mqS6a7Da01JP5V--KaAOga4MHnR84sqVbP5wvLbgJoeBD1NRowYqCocnW9DFW-O2bdzCVwN9bckoYzLms7OLzzaXXRE4Qr23qbTNnmA-hxlnnZq0i-R1lcv97t0LI2zT5u9t7TH_F5HT3YFS1JH-b2a_Sb4rzvCQMMIj-7bJk6zqfjWccz5zaxE9s788-V0ewcIDu3-XaS1GEl7Vu7xCVL9FX5auY8ASITWxKGg64_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛المیادین به نقل از یک منبع ایرانی:
ایران در پاسخ به آخرین پیشنهاد آمریکا، با بازگشایی تنگه هرمز تا پیش از پایان کامل جنگ مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/69466" target="_blank">📅 16:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69465">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwH2G1Ia-eVL17uC9sfnHZ-by5nX_-Np6adpyoIS7aKYDu0dqrLFZsSeSDiPRxM2T9ykhAeVYX-CWD2cNaVs8F8Ym3arh3TvTX6kLk4hcuLvVDWnZNaNxApHmEED5ipn9TqiIsI1IRzlthvytAvuDlG5lZxKpnk4uDCG7jz36e72CqI-YTV7iiVtnTDoCJgRbIeTO3cnNGXy9B2NVmUKS7ygR32GQZdiuFQfaWuBzsmI0lWwIbFXZM4vUWndIUY9Mor2mIdoGiyu0PQOpggIcB9K2iDEhE68ZFJm7umzyFax92kJobJbeY3n2hHU5LcSW3CVZp7JfBkvzfK2EAKrag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست میانگین IQ کشورهای مختلف تو سال 2026 هم منتشر شد
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/69465" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69464">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863fff3357.mp4?token=a3G2Lyr9B3VSKVN1cId4oWiaeY3natpKsLRL3-3OsAP8xQ9mwYuC2Hnn2nmJbKOoeGPdqIrsP7DCrkghXpbVA5uIiE1VeooYze_hRsjMpvKz9OphDmiD5PnWZicPoViiqYCOVJJvHiUg_PNcA5Jipcgtgu2xLgfBzW1vQeYytEcPdZGKAGQBgRQxryoWRL_yAcFBl8htVYnbNzPk76KT3_CW9_ZJanXs4BSIrizWJAAL5C561mAY_VLOjOQFjPihIWhartw39jm3cT3C6rUchIBIPFOp3bTNP9R8nS7PLoqlGG3VvIvZAtSkkZs2AwDszoPajuYsDQA2MNr4UkzMuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863fff3357.mp4?token=a3G2Lyr9B3VSKVN1cId4oWiaeY3natpKsLRL3-3OsAP8xQ9mwYuC2Hnn2nmJbKOoeGPdqIrsP7DCrkghXpbVA5uIiE1VeooYze_hRsjMpvKz9OphDmiD5PnWZicPoViiqYCOVJJvHiUg_PNcA5Jipcgtgu2xLgfBzW1vQeYytEcPdZGKAGQBgRQxryoWRL_yAcFBl8htVYnbNzPk76KT3_CW9_ZJanXs4BSIrizWJAAL5C561mAY_VLOjOQFjPihIWhartw39jm3cT3C6rUchIBIPFOp3bTNP9R8nS7PLoqlGG3VvIvZAtSkkZs2AwDszoPajuYsDQA2MNr4UkzMuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مشهد یه دوره‌ی آموزشی گذاشتن برای افراد بالای 60 سال که توش مبانی اولیه‌ی استفاده از موبایل رو یاد میدن؛
موضوعات آموزش:
آشنایی مقدماتی با برنامه‌ی بله
آشنایی مقدماتی با اینستاگرام
وصل کردن فیلترشکن
ارسال لوکیشن
تماس تصویری
ویرایش متن تو واتساپ و بله
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69464" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69463">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda203069a.mp4?token=amAzFujkqtaFWjrQDf_-_yA-rkkT5FDudEo1oNATqkwNdjoW6vBZ4eUi31c_SqNVH1gQ7CdT5seusrix8FWYClusmre3SAEQsJOMNwEgfDTF1KdwPrLu84HwPt8OKBExdiUljvf5jO0Xe6MWs8AiypxkwoLYri7i8XsdDeXe4VYUiPsk3sxhPqDJVnkct1xqSsefSSiHXNhLqr7EmV8Tat6vJnKv3cjzx5AsJIH1_E3vCXmWBT7rjPfaG7TA1aPxJTljkei41RCVeX0KorJyy6Aeas13qBnglml7FmrN-yPPnW_5DTA_QtlhToL8q-eEcEYPAWKuR_YSx2i3vbFvzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda203069a.mp4?token=amAzFujkqtaFWjrQDf_-_yA-rkkT5FDudEo1oNATqkwNdjoW6vBZ4eUi31c_SqNVH1gQ7CdT5seusrix8FWYClusmre3SAEQsJOMNwEgfDTF1KdwPrLu84HwPt8OKBExdiUljvf5jO0Xe6MWs8AiypxkwoLYri7i8XsdDeXe4VYUiPsk3sxhPqDJVnkct1xqSsefSSiHXNhLqr7EmV8Tat6vJnKv3cjzx5AsJIH1_E3vCXmWBT7rjPfaG7TA1aPxJTljkei41RCVeX0KorJyy6Aeas13qBnglml7FmrN-yPPnW_5DTA_QtlhToL8q-eEcEYPAWKuR_YSx2i3vbFvzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
میزان شانس بقای جمهوری اسلامی از زبان مراد ویسی:
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69463" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69462">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b293a286.mp4?token=jOp4EzRoxa_ToUclpUrGXmjmWYGmPoMCl2ExupTg61EbRw74hYqbD-ulFnc_p32hXQnTO9o9-s4Fa8Dr0Ua2FzGDsDX8AwGHZE5xb2x0ybUAL42vaIwz7lVauQ30E1lfafOsL2gCS8DD9UYWFz0cMQ5dODieMPLa6V2q8cX-gRbWGNQw6YgD7n8S6UYqjcvfYRmOjZiCsBRMxC6mbHM_nRgIMjjsU0Th4KSp7k1StD3kKfDFRWA9ZtR_Mg5G0LdUozoxEeJWcBbGzF3Ec5BzsFMzA12XaaggwwZ8hOyJ2Wn8Bsoi2XmwBioYEN1RcYyQiGvZ7pmFu_JwXilwEybddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b293a286.mp4?token=jOp4EzRoxa_ToUclpUrGXmjmWYGmPoMCl2ExupTg61EbRw74hYqbD-ulFnc_p32hXQnTO9o9-s4Fa8Dr0Ua2FzGDsDX8AwGHZE5xb2x0ybUAL42vaIwz7lVauQ30E1lfafOsL2gCS8DD9UYWFz0cMQ5dODieMPLa6V2q8cX-gRbWGNQw6YgD7n8S6UYqjcvfYRmOjZiCsBRMxC6mbHM_nRgIMjjsU0Th4KSp7k1StD3kKfDFRWA9ZtR_Mg5G0LdUozoxEeJWcBbGzF3Ec5BzsFMzA12XaaggwwZ8hOyJ2Wn8Bsoi2XmwBioYEN1RcYyQiGvZ7pmFu_JwXilwEybddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعترافات عبدالباری عطوان (تحلیلگر سرشناس جهان عرب) رو شنیدید؟ کسی که همیشه به مواضع خاصش معروف بوده، حالا لب به اعتراف باز کرده و از کابوس کشورهای عربی پرده برداشته!
عطوان در تحلیل اخیرش (مارس 2026 )به صراحت میگه:
اگر پسر شاه (شاهزاده رضا پهلوی) به ایران برگرده، با توجه به اتحاد استراتژیکی که با اسرائیل خواهد داشت ،ایران به چنان قدرتی تبدیل میشه که تمام کشورهای عربی منطقه باید جلوی عظمتش زانو بزنند و عملاً به نوکرهای ایران تبدیل میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69462" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69461">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=cA-Eag6gaUCeq76vInKMgi0Rw8z8rZ1NhSsanho9D66z-AM-ydujHkM-BuO9UNyF8bV8ZRW4DKxPz8ThW1-jAhwD1XvaBog2BLXG7Ps3DRKmzeALqmpfipoRFH-M4Ib0Meip2vBQoVrEnHoR-5lKm85b2xE2cjKoAC-f4rp4OBPQRwpQX7sd4VxbL00OPy_n0Bo30C51mzviCRD8oXLDcOPhdgly-BSk0vnxG9jLfm5gXFyxiThQaCF8zEY8H1Jpxjfv-7VYhGFAO8FTYO4WZMZEbtAx0MAt7y0Debzl_hr8qLS-6Zq7lUkIq53A2lJqYpC4Qi5TwavR35S2URvyew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=cA-Eag6gaUCeq76vInKMgi0Rw8z8rZ1NhSsanho9D66z-AM-ydujHkM-BuO9UNyF8bV8ZRW4DKxPz8ThW1-jAhwD1XvaBog2BLXG7Ps3DRKmzeALqmpfipoRFH-M4Ib0Meip2vBQoVrEnHoR-5lKm85b2xE2cjKoAC-f4rp4OBPQRwpQX7sd4VxbL00OPy_n0Bo30C51mzviCRD8oXLDcOPhdgly-BSk0vnxG9jLfm5gXFyxiThQaCF8zEY8H1Jpxjfv-7VYhGFAO8FTYO4WZMZEbtAx0MAt7y0Debzl_hr8qLS-6Zq7lUkIq53A2lJqYpC4Qi5TwavR35S2URvyew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
عراقچی داره میره اربعین و ماهم توی تهرانیم.
دوشنبه مذاکره ای نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69461" target="_blank">📅 13:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69460">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
از فرصت تفاهم‌نامه و لحظه‌به‌لحظه آتش‌بس نهایت بهره‌برداری انجام شد
در این مدت، واردات تجهیزات جدید، تعمیر و بازسازی سامانه‌های آسیب‌دیده و همچنین تولید سامانه‌های جدید در دستور کار قرار گرفت.
پهپاد‌های جدیدی که اخیراً از آنها استفاده کردیم نیز حاصل بهره‌گیری از فرصت ایجادشده در دوره آتش‌بس بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69460" target="_blank">📅 13:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69459">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08375903ec.mp4?token=ctwo5ZKLKIevmxe_9jZ8wV2-2KMPwHcbcBTMI6Hf8ygHQajX_sHBkJBLc4vvaIVPl3ryBXIyoSgKkhS5A02MuDe6FcIRrJvK_A116Iz17EKQHlrZKdkdHz3rz1ZvtwHqc7rAEb3lGVmuYppMnhwU1IxFc39BfKm-SW4sHdZTlOKeaAgVzyNUlhDWOByoW5fQTfGMP7yHUUPENeVzyFuqj1rItmd87df5lhPEiVTMqgSzXELVCNC_GJl79rXWoG0kapltWiUmzvmTyTMa-hnJz-6bQgs1peg-Mtf10s1_Yk-VeQJwepRB-e9P6w7oHvWlTOCBZOaCOJ82dr1lGniHZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08375903ec.mp4?token=ctwo5ZKLKIevmxe_9jZ8wV2-2KMPwHcbcBTMI6Hf8ygHQajX_sHBkJBLc4vvaIVPl3ryBXIyoSgKkhS5A02MuDe6FcIRrJvK_A116Iz17EKQHlrZKdkdHz3rz1ZvtwHqc7rAEb3lGVmuYppMnhwU1IxFc39BfKm-SW4sHdZTlOKeaAgVzyNUlhDWOByoW5fQTfGMP7yHUUPENeVzyFuqj1rItmd87df5lhPEiVTMqgSzXELVCNC_GJl79rXWoG0kapltWiUmzvmTyTMa-hnJz-6bQgs1peg-Mtf10s1_Yk-VeQJwepRB-e9P6w7oHvWlTOCBZOaCOJ82dr1lGniHZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نیروی تفنگداران دریایی آمریکا ویدیویی از تمرین‌های تیراندازی نیروهای خود منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69459" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69458">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyhlkY8AYq9funs8NOug4tksYtptTfekwBFpUOZwlUjaNEsaVdwRMkeffOk_UrREB1qm5_5dV06QtRpRbvhdmSsH2S2imrcWRFAeFKXN9Whm5hmVT86B7bdrn1IyqtpHpVyK8-m0Qh9fSaSaleSDkiaanCXaH9PB76GMs5N9VIbZ1W77mKkZ3HS2-Pb_HkfQIeTHST2hZ0kpDfyPDq9_UMC74SfwHBRJQdiGICF10Zhk5J-UYCJ1rIQKYo8idGJ5flwDikH3_Zl77hvJJ0yUiKVa71SS_Y4vWuFCrJ_m1SaKP9jGhQE8Xz5Lf9xGFwveBQlFYbyX0pxESdMXc32NVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی، سخنگوی وزارت خارجه:
ما در حال حاضر هیچ‌گونه مذاکره‌ای با ایالات متحده نداریم و مذاکرات با عمان بر دستیابی به توافقی پیرامون عبور ایمن کشتی‌ها از تنگه هرمز متمرکز است.
هدف، تعیین مسیری موقت است که ایمنی کشتیرانی در تنگه هرمز را تضمین کند.
تا زمانی که محاصره دریایی و اقدامات ایالات متحده ادامه داشته باشد، هیچ تحول قابل‌توجهی در وضعیت تنگه هرمز رخ نخواهد داد.
🇮🇷
اسماعیل بقایی، در واکنش به ادعای جلوگیری عربستان سعودی از حمله آمریکا به ایران:
اینکه همه کشورهای منطقه اذعان دارند که از تحولات و شرایط آتی منطقه متأثر  شد، امری مثبت است.
جنگ ایالات متحده علیه ایران، جنگی علیه کل منطقه است.
طی پنج ماه گذشته شاهد بوده‌ایم که حضور ایالات متحده در منطقه، موجب افزایش ناامنی و بی‌ثباتی شده است.
طبیعی است که کشورها برای جلوگیری از تشدید ناامنی تلاش کنند، اما تجربه نشان داده است که هیچ‌چیز جز قدرت و توان بازدارندگی ایران، مانع دشمن نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69458" target="_blank">📅 12:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69457">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=qg_5UzcXVRCXktS90XlIXy2NHWCEvKXEzlp1dBRMvjuQVJn-JvlZP1366oXK_cD-8gvc2EVLUIfKZVQGydIOIsSle0hXweQOHjDGIhgfddhdbevLL2ldiLE2syAlD07hxFCDjHsh7UWqnT4QPToe7ZDcesWvUBECw6QUXArHYG1VZ2dUKn0-MygOWsh4W-rS1OaXNrt8yP7rtVaQLcRRrFJpOtDZtrlizG5m9NzBDmiaG-kz6SazoMFbtqZ_uUknbBnX-jpziBfrSqfbS6zmvrgHXF6lteFGkKtdKjlsjOvdga-z4-or8RUM5dWoeS0YxS89RRn-De0Ek6Ee0Xx1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=qg_5UzcXVRCXktS90XlIXy2NHWCEvKXEzlp1dBRMvjuQVJn-JvlZP1366oXK_cD-8gvc2EVLUIfKZVQGydIOIsSle0hXweQOHjDGIhgfddhdbevLL2ldiLE2syAlD07hxFCDjHsh7UWqnT4QPToe7ZDcesWvUBECw6QUXArHYG1VZ2dUKn0-MygOWsh4W-rS1OaXNrt8yP7rtVaQLcRRrFJpOtDZtrlizG5m9NzBDmiaG-kz6SazoMFbtqZ_uUknbBnX-jpziBfrSqfbS6zmvrgHXF6lteFGkKtdKjlsjOvdga-z4-or8RUM5dWoeS0YxS89RRn-De0Ek6Ee0Xx1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله پهپادی روز گذشته به مرکز لجستیکی عظیم شرکت وایلدبریز (Wildberries) در نزدیکی سامارا.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69457" target="_blank">📅 11:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69455">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGUpokH7Ij-jtv-FwGsKpEjaEQ2VKd8pWFrmxDhSIODySUd-toCiPCEgxHhd-cSz7zbh5tK3dUbtUL1p6k2B5BOayKmoy8LLhgbqoqrdSGiSzVJ5i635w5K6a6kAGXa84sb2A3WzxMIxqHjK5LuLS21mlSA83aMsGn2YoySGkDuI1bY_xMvMkhnDgmBGVJIoYkllxzcuSCshH1Ct-zDeASshi9rpBVfMFBxIO8evp-m4aXGLvAtNrGBS0rVtzEJMIkYFFF71SVQYreJg9Lkv1a41kOkC-e4PH_VpbxlLQ2OFIChZAIIsHh-BxnNeKEv48XA0Dmv61AvR32PQ5ACUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=NfMJxKI86r_p96HQ7FEYIcVj8ecNwbrQWb63spYYUPHYdHxBdYkceppoPPuG7zxRdBR5u2S_OhEgejHu2RdgmQjbf3_3v31VIHd2jHXemwihnpE_onaQhAsiNOlRby5EGGwi0ufKu4MpGmVDu6CqagSMFwITAMyyaPPcuIWDmzwr8cgrfy81z6XF2A24rPvZghuJQABCnFWLL-eOk1oxHbWhMbZOCwxUbIKXkPgkJCBE5dq8SZWykatMCq2PsC8yhbntW08HzMYX5dY881-jLgbU29O3WbKbEgtdD7oZB1vA5LZn783JOKmcYvXvCFA5aM3QUDgv0Yeav-TSqW87GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=NfMJxKI86r_p96HQ7FEYIcVj8ecNwbrQWb63spYYUPHYdHxBdYkceppoPPuG7zxRdBR5u2S_OhEgejHu2RdgmQjbf3_3v31VIHd2jHXemwihnpE_onaQhAsiNOlRby5EGGwi0ufKu4MpGmVDu6CqagSMFwITAMyyaPPcuIWDmzwr8cgrfy81z6XF2A24rPvZghuJQABCnFWLL-eOk1oxHbWhMbZOCwxUbIKXkPgkJCBE5dq8SZWykatMCq2PsC8yhbntW08HzMYX5dY881-jLgbU29O3WbKbEgtdD7oZB1vA5LZn783JOKmcYvXvCFA5aM3QUDgv0Yeav-TSqW87GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده مردم در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69455" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69454">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=XtJaBmYfF_6Xdio9FJjElrpA5kAAdQM0eeiQM_sLKmAblUKxajjbSpB59AsVJof2HGtrVT78XKn5VhOK-N4J0E8wc7RdTTzDXLNcEVswn_YviXNUD8UJkjaWoR4UFREI0-rIraIdAeGF-o1_Ya-dgNplP0QI4uWihuIdAvwRDqZuCTmHuOvvoRDBUEIcu7twrEo30KwATDVClG0adM0SXemcLMQ7DBecrlgJ2oJoM4jTnJKiW-GhUY0SiqniMnUAX0T9_Lxd-Yd03GmX0IhLoUf18uh5XPubaeTwHkvLJZcH1HLrmyoNPyDHYe0qAnLOUYMdhYiFo6yaUE8Pk6EnGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=XtJaBmYfF_6Xdio9FJjElrpA5kAAdQM0eeiQM_sLKmAblUKxajjbSpB59AsVJof2HGtrVT78XKn5VhOK-N4J0E8wc7RdTTzDXLNcEVswn_YviXNUD8UJkjaWoR4UFREI0-rIraIdAeGF-o1_Ya-dgNplP0QI4uWihuIdAvwRDqZuCTmHuOvvoRDBUEIcu7twrEo30KwATDVClG0adM0SXemcLMQ7DBecrlgJ2oJoM4jTnJKiW-GhUY0SiqniMnUAX0T9_Lxd-Yd03GmX0IhLoUf18uh5XPubaeTwHkvLJZcH1HLrmyoNPyDHYe0qAnLOUYMdhYiFo6yaUE8Pk6EnGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای ازجواد موگویی که توی برنامش داره خیلی شیک و مجلسی جای همه فرمانده‌ها و مسئولان رو لو میده:
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69454" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69453">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVFmW8vr1PjKY43PaiTvD3nQkELpD5Z5BD6gnXhLqBrtL1-uWe4quTmAeRKaoHcCgzUaMszioy-IFFvmUoBOJTvFo0mimR8hPwicoUHJ0rgqM12u_yMQzLkKt4ZLMsdVEs_OjoJknJ-KFukh_fWwxhRQ4xlUPKzTLpyQ_42q20Y0wB3NagJKOcATzwghn6IAORUXL4ZbNtW0MqzTTZC8KbqUP1T-CDhYFanq0TlIXQ71DxmLau5N7UWpAHstldpPJNAvO3ZPjKc-c4tkuALgsyobP-XkUfZ5c6b2J4OFARqSYGR_djsfR0kM1pbrUpvQCIpmFy7fKKAm5oMFuseUr8Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVFmW8vr1PjKY43PaiTvD3nQkELpD5Z5BD6gnXhLqBrtL1-uWe4quTmAeRKaoHcCgzUaMszioy-IFFvmUoBOJTvFo0mimR8hPwicoUHJ0rgqM12u_yMQzLkKt4ZLMsdVEs_OjoJknJ-KFukh_fWwxhRQ4xlUPKzTLpyQ_42q20Y0wB3NagJKOcATzwghn6IAORUXL4ZbNtW0MqzTTZC8KbqUP1T-CDhYFanq0TlIXQ71DxmLau5N7UWpAHstldpPJNAvO3ZPjKc-c4tkuALgsyobP-XkUfZ5c6b2J4OFARqSYGR_djsfR0kM1pbrUpvQCIpmFy7fKKAm5oMFuseUr8Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مارک لوین:
تداوم توقیف دارایی‌های متعلق به ایران
ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
هدف‌گیری مستمر فرماندهان نظامی
حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
حمله به بانک‌ها و مراکز مالی
دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69453" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69452">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998caf4317.mp4?token=aIXm5xWibsa_RPwJlHvk1xWy0hmboMDss-87RH7Yexf4WcSulX7IAMh-KFPM0BrtSTvrglh86buNOy3T5nUKTQvPrrx0Kj66DNWWUUPIOeinKC9zIfeu_09E0eTL8WQkfBBQcBFcGsuX5XWIG-tQWd4Wl12_yX43twDZyR3fXmJZiuOTqv5T1hlcDEZ6GEbpShXLr7qp3cmU5JYCmLA7HxuQ9PzmJA8iSS7piLTvCjiordTWyLgHNZda4uQ79G56cXAAMVnJaVl8bU7TBbSKSDtkrzobwCP2NxYz5fdtb4RJLgU82LZuefrbPV9NIHz6-UsPTxUP_5Ig2cDqn2tskXqIS0_oVw7UWkDFIzKlmKkQoVh5VQuVYX3H5UcTRl_bltBA0xLgrZEkwBr84pNLkanCU6D8_9S-Ao3DuPb57x0BjniGFtvw0ULfyPVSQIFqy4TtPNaMMSCHni81RXkdveMO7Ixobs2lsx7vP7asib5WwZ8GycI-jtyJ0OKU08mHr2wt6R8tOLsG4Be0dClFWgjC1SDRAgOdVz2jz9bobKw3fYJBpSOvFXS8qHN_Vq-LYIgLdGgEQvf6vv6C1BGDbp784T3nwXMaCVq6jm1sNRga-gLEWeMjfH7ff3u775AG6U0WsS1i6t4rS1k_9IV5kaqZAWnAMKUFygk6PRYG3BE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998caf4317.mp4?token=aIXm5xWibsa_RPwJlHvk1xWy0hmboMDss-87RH7Yexf4WcSulX7IAMh-KFPM0BrtSTvrglh86buNOy3T5nUKTQvPrrx0Kj66DNWWUUPIOeinKC9zIfeu_09E0eTL8WQkfBBQcBFcGsuX5XWIG-tQWd4Wl12_yX43twDZyR3fXmJZiuOTqv5T1hlcDEZ6GEbpShXLr7qp3cmU5JYCmLA7HxuQ9PzmJA8iSS7piLTvCjiordTWyLgHNZda4uQ79G56cXAAMVnJaVl8bU7TBbSKSDtkrzobwCP2NxYz5fdtb4RJLgU82LZuefrbPV9NIHz6-UsPTxUP_5Ig2cDqn2tskXqIS0_oVw7UWkDFIzKlmKkQoVh5VQuVYX3H5UcTRl_bltBA0xLgrZEkwBr84pNLkanCU6D8_9S-Ao3DuPb57x0BjniGFtvw0ULfyPVSQIFqy4TtPNaMMSCHni81RXkdveMO7Ixobs2lsx7vP7asib5WwZ8GycI-jtyJ0OKU08mHr2wt6R8tOLsG4Be0dClFWgjC1SDRAgOdVz2jz9bobKw3fYJBpSOvFXS8qHN_Vq-LYIgLdGgEQvf6vv6C1BGDbp784T3nwXMaCVq6jm1sNRga-gLEWeMjfH7ff3u775AG6U0WsS1i6t4rS1k_9IV5kaqZAWnAMKUFygk6PRYG3BE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇱
🇺🇸
ویدیویی جدید از لحظه بمباران خیابان فردوسی در زمان جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69452" target="_blank">📅 09:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69451">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHXFvf14gxyCa4uwNuBQqigDbSZzwNcjl1mJFtV7IGcNhqxvC10N5K8IMeXM60ImltRYxepGipdvhht0CAvehqlBLEvZe3KDySK4EMpMxjZvzqYBgPHAi43gb82cV_mm7OzsUf87hX3knls0mVPWFJGXHkRZBjvYyft4vPvrxlcpqUMBG9rTtb-nUywdk81D2OZtBox8_GTnoc3fA2eKbIQ7we4WESep6zLwe_go5Rf2o0KOIiPo4rNe9Y77mVSr5tRu1NTzM7SC59lZrhgTLx2nasRDcqzsFU456llWY44auYqMy2Y8j3Q4t8JE80yRtzx8XdIdQ16B2STBdYelXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هگست وزیر جنگ آمریکا:
واقعیت.
وزارت جنگ آماده‌ی حمله بود - و همچنان آماده است - در سطحی که از جنگ جهانی دوم دیده نشده است.
قفل و بارگذاری شده(آماده اقدام).
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69451" target="_blank">📅 03:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69450">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TCzMS5UUZ1BMM78etqNXzlE-bpbage7ASx2FXjT3jLDmTJmxAkw52oijgqgkKCAgrnMAv9Yd6-Gdz4Kael2sVxKK1C9LQeMkVMA3Lh9Pis2J_nCcLYl8pL_0Oj-iXHVxzEaKrqvoOAa9__c2KTcEwnDd3p_QbIOaXLqEeKRUDKRtiQ-ysXRFdCaIeaQeOAs359YaNGkJiVcu67e2z8KMtIXSu_KD52vTTMF2leN0_UpT_QfHepGBKUlO8Gb_ZQ7J42mUHyboIu5XqeIpa-u8XPcyMkoRA8U17FlPb6LcRENNrM4TmF-brNMQQy3tNPjsF9A97TfApSiRRBzZ0rd0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پست جدید کاخ سفید:
به ترامپ اعتماد کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69450" target="_blank">📅 01:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69449">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQlVjXNY8AM4H02TICyOvXO1FH2DQwXnw5hL8qqGuG0KSTwclleQhVKJ15SYLTLz4ZKwI5ViwirfotJ6J-zhvfkVQvz1E1VwvdI-3eFpe9kAE3uC09FTRB7rMabVcA9zCherditXwJgkJvI031ipfPaINukqX9IESz9HO6PLDc9N1cRnedyVppG_kyzI-ZMvcQVoncgj6j3cGuRBFVNGKQH5_a8LjRYTxo4GPHtgq6xxHSF63pmnVy6imp1Nh19cy77E0VudCLx7ptSSFEEA5xSfr0zH68cqpFkSTO5uFd5GZDscBr9FQGAss0gyK5jX11s8zrYHbirolD2shN2nvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرقی خصبِ عمان دریافت شده است. مقامات در حال بررسی موضوع هستند و به شناورهای حاضر در منطقه توصیه شده است که احتیاط کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69449" target="_blank">📅 01:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69448">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
وسط حرفای ترامپ یه کشتی تو تنگه هرمز هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69448" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69447">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=AWTRENLFkXwEotFpTmvoNi7qoRMUM5PEUmHMUeH63hLgFxykxZmWMPoQJ0dH1zfLu9RMby-y3cDJKl6fgYy8TiivGaxIq8ODnFKUnB8dpiSF2CXZ2ADKL3jFDJpSJ7xQAEBzE-OHYfpegpEKT_-7ggcCxmSocj0hcXZeK2KPmgwiCobP5yDB9TfXzBOUmdHc74L5khuzfZ4IvYtF0oZZJC7rGdrMuQy549Ru4GZSESdhDzVN67MtR2jPel9TW_FYjO0uAedPm1sNwWSPm2zRoEewgmAfgvAkNJfoyL2bGkUF9qhNoVYYixQhndg8A8JrvlY3YZywK_eOOT98mGEDXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=AWTRENLFkXwEotFpTmvoNi7qoRMUM5PEUmHMUeH63hLgFxykxZmWMPoQJ0dH1zfLu9RMby-y3cDJKl6fgYy8TiivGaxIq8ODnFKUnB8dpiSF2CXZ2ADKL3jFDJpSJ7xQAEBzE-OHYfpegpEKT_-7ggcCxmSocj0hcXZeK2KPmgwiCobP5yDB9TfXzBOUmdHc74L5khuzfZ4IvYtF0oZZJC7rGdrMuQy549Ru4GZSESdhDzVN67MtR2jPel9TW_FYjO0uAedPm1sNwWSPm2zRoEewgmAfgvAkNJfoyL2bGkUF9qhNoVYYixQhndg8A8JrvlY3YZywK_eOOT98mGEDXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
نمی‌دانید این حملات به کجا ختم می‌شود.
منظورم این است که آیا همسایگان ایران با هجوم سیل‌وار جمعیت به کشورهایشان مواجه خواهند شد؟
یک فاجعه. اتفاقات بد بسیاری ممکن است رخ دهد.
ترجیح می‌دهم توافق کنم. به دنبال کشتن آدم‌ها نیستم.
آدم‌ها می‌میرند؛ خیلی‌ها می‌میرند. ما چنین چیزی نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69447" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69446">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=CVp1UQY7NOZO-G5buANGUMaTS6H8ZdCjPQEaXS7JvGT_X7JdaG6J0bGPv3mwCl4y1XM_K-4vXSTaZt0wclSn_xHKegoEIt7vbc75uY59g6BVtPhd80bdTBZ-8hTf-Fiotr19x4prKo9HjrUxs0r4u4mlUl4pK2TkHRr93Ud_wQnnMoOv1vw8YHamsiNcNcmTg4FYoce4OkGUxfXnRxi6wtuapbIZPW_eUOeEoDyFCtiqHyFZ9KDO9q9s_w-JzLcERKLIHK8OA13HrhPJlYfiQW8RfVlCbyb6-9VnXhFit8fy5DPTqkg8hvTiirfHcRvy5Wf0juGU3lDRZnID2eZ6rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=CVp1UQY7NOZO-G5buANGUMaTS6H8ZdCjPQEaXS7JvGT_X7JdaG6J0bGPv3mwCl4y1XM_K-4vXSTaZt0wclSn_xHKegoEIt7vbc75uY59g6BVtPhd80bdTBZ-8hTf-Fiotr19x4prKo9HjrUxs0r4u4mlUl4pK2TkHRr93Ud_wQnnMoOv1vw8YHamsiNcNcmTg4FYoce4OkGUxfXnRxi6wtuapbIZPW_eUOeEoDyFCtiqHyFZ9KDO9q9s_w-JzLcERKLIHK8OA13HrhPJlYfiQW8RfVlCbyb6-9VnXhFit8fy5DPTqkg8hvTiirfHcRvy5Wf0juGU3lDRZnID2eZ6rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست.
آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69446" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69445">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=qU-GdSz8BNNHbwIAeFDz8HzugE1SnQ0hAtURh7qg_bcfmycoLfSXchL9ej53DAa1mzjCGBJOpbmOtJcTCgLx1tQinitxUusez8ybN4GH3rY8g886sclcfbD78mPOFTdwXCJq3QRWJIXgRLolE6-2HTGwoZzfvn7rJCq1yaaDuTAW-7HbQ5bd78e9wW7VdY18YKYaWJ35CM5niyqVMsBIsD_hq18ZVcYm7zfFyuY4xWYQqF1HznYZ0D_rHheD_NR3D9Zhnx0l-Z5bEr4ePzZYHHHZMgDsZ66ThgXv3CGSxvXEtizNy0aT03_zoxFGSx4dxRG1ocdACeIjOjSi06sTDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=qU-GdSz8BNNHbwIAeFDz8HzugE1SnQ0hAtURh7qg_bcfmycoLfSXchL9ej53DAa1mzjCGBJOpbmOtJcTCgLx1tQinitxUusez8ybN4GH3rY8g886sclcfbD78mPOFTdwXCJq3QRWJIXgRLolE6-2HTGwoZzfvn7rJCq1yaaDuTAW-7HbQ5bd78e9wW7VdY18YKYaWJ35CM5niyqVMsBIsD_hq18ZVcYm7zfFyuY4xWYQqF1HznYZ0D_rHheD_NR3D9Zhnx0l-Z5bEr4ePzZYHHHZMgDsZ66ThgXv3CGSxvXEtizNy0aT03_zoxFGSx4dxRG1ocdACeIjOjSi06sTDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای گسترده باشد.
آنها از ما خواستند که این کار را نکنیم. گفتند: "لطفاً این کار را نکنید."
همسایه‌هایشان هم همین را گفتند.
ما فقط می‌خواهیم ببینیم که آیا می‌توانیم به توافق برسیم یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69445" target="_blank">📅 01:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69444">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=K8ARUyN_azeqFM_MKRHk1okislVINMm99jAacN9ebJ7R5Za3S8fm8rTky9b1JS_CtD0fWWuFD_yFN8loXREr2jfx6dgWM2uuHGdF7bBta4P_qZ0_qVPZun0tmVZiTCbkZeYkiHQCft2MHQjZBMa29aI9_QNwldb8fd7c1ztpzKH3Eks8RLkT92VJLczGZkVzqQWjGQNEwUBxuUVCvIWkeGlKbc-sh9vsIlUSEsPg_9OIQ15ZamM2okjSzBg_aMG4sRU6ZOIIc-vxLKKTOpl83n13NszXEq4_ZP6U0vW8ZsOOh1yIXUJbVbARjaW3U6adWetKk4sBeBBvurywTuiLcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=K8ARUyN_azeqFM_MKRHk1okislVINMm99jAacN9ebJ7R5Za3S8fm8rTky9b1JS_CtD0fWWuFD_yFN8loXREr2jfx6dgWM2uuHGdF7bBta4P_qZ0_qVPZun0tmVZiTCbkZeYkiHQCft2MHQjZBMa29aI9_QNwldb8fd7c1ztpzKH3Eks8RLkT92VJLczGZkVzqQWjGQNEwUBxuUVCvIWkeGlKbc-sh9vsIlUSEsPg_9OIQ15ZamM2okjSzBg_aMG4sRU6ZOIIc-vxLKKTOpl83n13NszXEq4_ZP6U0vW8ZsOOh1yIXUJbVbARjaW3U6adWetKk4sBeBBvurywTuiLcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره بمباران ایران:
گروهی از افراد هستند که خیلی دوست دارند من این کار را انجام دهم—صرفاً انجامش دهم—و گروه دیگری هم هستند که نمی‌خواهند من این کار را بکنم.
🎙
خبرنگار: آیا ایران برای دستیابی به توافق ضرب‌الاجلی دارد؟
🇺🇸
ترامپ:
خواهیم دید. من به دنبال کشتن مردم نیستم.
از ولیعهد عربستان سعودی پرسیدم: «ترجیح می‌دهید ما چه کار کنیم؟»
او گفت: «ما توافق را به حمله ترجیح می‌دهیم.»
🎙
خبرنگار: گزارشی وجود دارد که می‌گوید شما در حال خارج کردن نیروهای آمریکایی از کویت و بحرین هستید.
⏺
🇺🇸
ترامپ:
نمیخواهم در این باره اظهار نظر کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69444" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69443">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=NomW06NuG-SA8x2-gsb7FqI41deodzj4op0YriP3LENSrGSGUwJ-7wv16OfFkvxVHr5oHvxtWmYVwB9M2l5FyfJZurFOwL_FXeEnTOfOmntUpG1fn3la0Kfg5TkilITrHj7OLaDQyX1bCDW2O0cDzNJKtifcv1FNtiCImvEt_-AzgHVq8bKLcDrTnedSTde75npcSgBZCAUeWA5R0mU8AV0CJb208w2CIY2YMl3c9TpyVJun4j5TcDqW07y0jZGdgjEz4kMrHL_l5utYSm6VPfOcNGSWi2Yr8klKbZY0CL2GqJ9CjgKG4lLezpQLhkAz4GN-hhRFDeHPsIiagmo88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=NomW06NuG-SA8x2-gsb7FqI41deodzj4op0YriP3LENSrGSGUwJ-7wv16OfFkvxVHr5oHvxtWmYVwB9M2l5FyfJZurFOwL_FXeEnTOfOmntUpG1fn3la0Kfg5TkilITrHj7OLaDQyX1bCDW2O0cDzNJKtifcv1FNtiCImvEt_-AzgHVq8bKLcDrTnedSTde75npcSgBZCAUeWA5R0mU8AV0CJb208w2CIY2YMl3c9TpyVJun4j5TcDqW07y0jZGdgjEz4kMrHL_l5utYSm6VPfOcNGSWi2Yr8klKbZY0CL2GqJ9CjgKG4lLezpQLhkAz4GN-hhRFDeHPsIiagmo88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: در مورد ایران، حالا چه پیش می‌آید؟
🇺🇸
املاکی:
ما در حال گفتگو با آن‌ها هستیم. این گفتگوها از بعدازظهر فردا آغاز می‌شود. این کار جان‌های بسیاری را نجات خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69443" target="_blank">📅 01:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69442">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=PPcQndbI2jLrYmbbRkFn_Cv63l1zycGafZy1tGtN0bdvjjXEWwlQGY9e6q2slhE8X-aU2-YLdw8Vj4ioEnQ1ljwYFbdLcOT5kY1G4fLRA6mfR_k_BiOy1lRvpsTzsdPjFyYchUj-n9t4UohvvH60wk6Yo9nmUIS3mRqE2psryiPOWzAs9mGe1syNMQvB_Up49toWCVD1wwO86rrfrhsLHkeiS53pYERPmg1CGg3WS9rrTFv7NB-ShSJdZQc_ojRHDYKZMk9mcRgh9SeVKrDs0DJRL3VRJiqamUg1vPZmsH2y9BGI-BzwdWNl5NrLFXDP7bNVUO9z_B7iAsHjuK1OWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=PPcQndbI2jLrYmbbRkFn_Cv63l1zycGafZy1tGtN0bdvjjXEWwlQGY9e6q2slhE8X-aU2-YLdw8Vj4ioEnQ1ljwYFbdLcOT5kY1G4fLRA6mfR_k_BiOy1lRvpsTzsdPjFyYchUj-n9t4UohvvH60wk6Yo9nmUIS3mRqE2psryiPOWzAs9mGe1syNMQvB_Up49toWCVD1wwO86rrfrhsLHkeiS53pYERPmg1CGg3WS9rrTFv7NB-ShSJdZQc_ojRHDYKZMk9mcRgh9SeVKrDs0DJRL3VRJiqamUg1vPZmsH2y9BGI-BzwdWNl5NrLFXDP7bNVUO9z_B7iAsHjuK1OWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد ایران:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند که حملات را متوقف کنم.
حمله بزرگی می‌شد.
وقتی متحدان خواستند که آن را لغو کنیم، باید گفت: "خب، ببینیم چه می‌شود."
متحدان فکر می‌کنند که توافقی حاصل شده است. توافقی در مورد هرمز وجود دارد و توافقی در مورد هسته‌ای خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69442" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69441">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=gYm8Zwq2tlYclVz707nAiGsy8GhAs2CUEGHYFVi6iPtLynS1I3XR3crZI8ZKrjQ3aOQBPM3nXT8UcQ3PsNhc6r9aHnfHlwOiKozwgyLf7cm7sjETk4fxPK7elk4s3uYhfl62KiTln-2w-CGwfM2QaI1NlTc0XsElrtBEBPM_snWIpb7OMr2CYCk4ImbWiznVFbFT6cQh8wK6oQldzQuvYDqdjO4r0TuQyHXqRORAtbWNuju4tG0SfenWVaXsWyNr9ToSQCpc2diN00Nwnu_-OHcvNCBXA-UGtTqhGEwL-tbBzFSf1LNPQWmrFB6jLlscGHZjYPJ9-kP262CV645iPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=gYm8Zwq2tlYclVz707nAiGsy8GhAs2CUEGHYFVi6iPtLynS1I3XR3crZI8ZKrjQ3aOQBPM3nXT8UcQ3PsNhc6r9aHnfHlwOiKozwgyLf7cm7sjETk4fxPK7elk4s3uYhfl62KiTln-2w-CGwfM2QaI1NlTc0XsElrtBEBPM_snWIpb7OMr2CYCk4ImbWiznVFbFT6cQh8wK6oQldzQuvYDqdjO4r0TuQyHXqRORAtbWNuju4tG0SfenWVaXsWyNr9ToSQCpc2diN00Nwnu_-OHcvNCBXA-UGtTqhGEwL-tbBzFSf1LNPQWmrFB6jLlscGHZjYPJ9-kP262CV645iPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی وقتی می بینه دلار شده 190 هزار تومن و آب و برقم هر روز قطع میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69441" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69440">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93362f281c.mp4?token=Y5NJuv7jOcFx52BWy-W5lW9nBKeO_qRyQ2kjwHvGKfDwcu1KspCPXAnMuaVN926gxkY3ZrEaELfyfT11-ZO2mExiRp4ri_4q7tR4XtuPEGirsGU_air3aGDxeowLRi1rhPn56uVxyd55XjPeD-y9npyX57XKmeklCIT1mf181OqzEY0LXBafYiJvaqM8_HIo4y6ATB2cuSdCHwNPiultJxd94ZE-zxs0NnVn1645QIuC5V3j7ofpBRvH3_JrOjh7wIcyC_de2AYfJoNdAKN9oLHs1SAoVJ_Y5hkSuCsOevYbLpIZz6sG3cI13LiXVVyqx7FTh_53FwD5oX9hzgZ5hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93362f281c.mp4?token=Y5NJuv7jOcFx52BWy-W5lW9nBKeO_qRyQ2kjwHvGKfDwcu1KspCPXAnMuaVN926gxkY3ZrEaELfyfT11-ZO2mExiRp4ri_4q7tR4XtuPEGirsGU_air3aGDxeowLRi1rhPn56uVxyd55XjPeD-y9npyX57XKmeklCIT1mf181OqzEY0LXBafYiJvaqM8_HIo4y6ATB2cuSdCHwNPiultJxd94ZE-zxs0NnVn1645QIuC5V3j7ofpBRvH3_JrOjh7wIcyC_de2AYfJoNdAKN9oLHs1SAoVJ_Y5hkSuCsOevYbLpIZz6sG3cI13LiXVVyqx7FTh_53FwD5oX9hzgZ5hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
شوت برنده در مسابقات قهرمانی باشگاه بدمنستر! از تمام کسانی که شرکت کردند، بسیار سپاسگزارم.
من با امتیاز 70 برنده شدم و از این بابت بسیار مفتخرم، زیرا برخلاف سایر شرکت‌کنندگان، زمان بسیار کمی برای تمرین دارم، زیرا تمرکزم روی مسائل دیگری است.
این را "استعداد" می‌گویند و من آن را دارم، در حالی که آنها ندارند!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69440" target="_blank">📅 23:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69439">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsLd-lYl8htLb5cAZrksQQrvay1Lv9EBY74jh9Db94QYFkh6XjqyKYn0_hdEfzaEwVK7D-lOiVhQTt2fnA_vCzrpA5bvl-gFQ23IWGxaFKKDHqNiIn2PvmfOlx5pfChD1FvtdvhKRAJd1C5VZnl1X-Ywyk0Y0Z-mkkjUNKZtP55aGd_4t46C50r1pY-JoFJ087J727rsB0uLXTlXVJq-4pHTxaS1f_pjps6_XZ99aVciXsHHYCJ_jpACbdtTC_5g3Wt7Qhm_stACSFgTVcML8PJ3K4o8839ZtwvY9uZyMoiHflQIn72mBuU7va0OAjksIc4KO-TXabpxxTEYOU7Q8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پزشکیان:
تفاهم نامه که امضا شد حاصل خرد جمعی اعضای شعام بود
این تفاهم نامه ثقل روابط خارجی ما توی آینده هستش و باید دشمن رو وادار کنیم بهش پایبند باشه
امنیت کشور و منطقه و هم‌پیمانان با این تفاهم نامه ارتقا پیدا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69439" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69438">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⏺
شکار و هدف قرار دادن ۶۷ سرباز روس توسط مولتی روتورهای اوکراینی در اطراف پوکروفسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69438" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69437">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=rK8JWYgmHB_Bs9ViQ26L9b5GNCli_-ulgpQ0PUbNwJQNVT_lPtq6DEDl6VIIvw5lAAljIMx8LzsYOFevIgnBpyPwUJVMn_xDwnJWC-AU-6Jp0Eb-ZuSohxMKcBmxR9ak_5tRXuQ4kqYEna4UclJFOx-Obzp7du3IhhmablvgDJRfjxTrIvFQ2FsM6TrcIlqcuv76rzTFy9BdhfWlxOOjNH9H5uU9SNeBJoEVn1etdhJKArorV1jnWGLnKIFSag2k7mVfmJIOseePrbKjoegqncKAFNpoxM3013spqBr7PtV_zf82ftF6biI4R5BDFc7m-EFWIpO8ZhXokaiuk-HG5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=rK8JWYgmHB_Bs9ViQ26L9b5GNCli_-ulgpQ0PUbNwJQNVT_lPtq6DEDl6VIIvw5lAAljIMx8LzsYOFevIgnBpyPwUJVMn_xDwnJWC-AU-6Jp0Eb-ZuSohxMKcBmxR9ak_5tRXuQ4kqYEna4UclJFOx-Obzp7du3IhhmablvgDJRfjxTrIvFQ2FsM6TrcIlqcuv76rzTFy9BdhfWlxOOjNH9H5uU9SNeBJoEVn1etdhJKArorV1jnWGLnKIFSag2k7mVfmJIOseePrbKjoegqncKAFNpoxM3013spqBr7PtV_zf82ftF6biI4R5BDFc7m-EFWIpO8ZhXokaiuk-HG5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
‼️
روح الله قرهی رئیس حوزه علمیه:
«وقتی ماهواره به فضا می‌فرستیم، می‌توانیم سرش را کج کنیم و خود آمریکا را بزنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69437" target="_blank">📅 22:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69436">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4MEqkCzjjRRxUQUKTk4F5FCbtDXfSFKRCnFGl4cC-sDvN8UXMCxUCGjUPxkepV3cq65zN8CAD2glBg-1-BQfm3w_UH2EcmZ_etJ4r11LNVlzhOH2c43RxzEZRACq8QTIV4IdjYoWEbzYmy_FpHFIr98Y7qhEQ0Kz3CKv9kqcjDBICrj1ugCPZnZDMR4gAQf7mP1aXsD3YmQfJGWv4PylycqG3IxrF4F6VIooIH9UEDcBgBgXZT8KuupQJI0zyJQ1cbXu-FIub4Qt8_v5HBMKjDZwFr0mXmksvWOsNTlg_Co2Svjh86Xqr7KXbr64ZHpHQFOhlKC29ezIVgmNUHQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کان‌نیوز به نقل از یک منبع امنیتی:
رفتار دونالد ترامپ — که منجر به لغو حمله گسترده به ایران شد — به توانمندی عملیاتی آسیب می‌زند و آن را تضعیف می‌کند.
این مقام امنیتی گفت: «این دومین بار در طول یک هفته است که ایالات متحده اسرائیل را در جریان حمله‌ای برنامه‌ریزی‌شده قرار می‌دهد که می‌توانست خاورمیانه را تکان دهد، اما آن حمله در آخرین لحظه و بدون هیچ توضیحی لغو شد.»
یک منبع اسرائیلی نیز افزود: «با وجود رفتار رئیس‌جمهور ترامپ، آماده‌سازی و تدوین جدی برنامه‌های آتی دشوار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69436" target="_blank">📅 21:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69433">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Dd87kvz72qdAtWSt8xWvTqEzo89w9nH7ZQDBJDlP32Aqe0m_G3dNvVZj2STggXDP_oeh_IEFhd89uXhd-piXa_atmFWrgaR8VNWhNKyFXgAyHsCZJ2COa05BszJ7zT4puq3nNtm573s3y7WhpM8uvJ14ZCt34TJzQAI0gYk3P8Dfdj4spXfg8_be8kZVT4pvEvFV2Res_rU98DCUczlZK6qPMJPGYcO39RbjhT10jT3izJVWtNipaRTFieYdqHYqC1uhwxBt4Lx4z_OeCHLT4pjjje-dPOOqBk2bpD6oVecKfKFINdaxAighfzkaM7zKbgyq8vaCbM7Ej3tdfZb5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=XnEwoNsZ03YX0Z-sAg9F95uBj9FOLVnAPJm4gsKmypLsPulKdjs0NcWI-sTWvSHqHoUO0kVUBmADMofhjV3RmYB9ftRTly_LtwtCLRC3QSRFO-eh_0jDMbYO7kxkzORxBZze8Y6SrQl2Xgst2UMz_cuXWo-rkFX1cQAhvc7EJiP5MhsWhhLaU1xxO2RI66ssLZ93ERzWbrMSCE-aE9bu0uMMeBBpAu5x1T40frc8eH-CRIGhWeRXXWlVAOnepJvVoR15dJoj8ChpWy46bgqooHe7Q2YTeKK0AWVx_Hw-TmBQ4zyyOoi1FERNaHFOsEDAjmTVV2Z8hx4z6HeSPjXbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=XnEwoNsZ03YX0Z-sAg9F95uBj9FOLVnAPJm4gsKmypLsPulKdjs0NcWI-sTWvSHqHoUO0kVUBmADMofhjV3RmYB9ftRTly_LtwtCLRC3QSRFO-eh_0jDMbYO7kxkzORxBZze8Y6SrQl2Xgst2UMz_cuXWo-rkFX1cQAhvc7EJiP5MhsWhhLaU1xxO2RI66ssLZ93ERzWbrMSCE-aE9bu0uMMeBBpAu5x1T40frc8eH-CRIGhWeRXXWlVAOnepJvVoR15dJoj8ChpWy46bgqooHe7Q2YTeKK0AWVx_Hw-TmBQ4zyyOoi1FERNaHFOsEDAjmTVV2Z8hx4z6HeSPjXbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انبار شرکت Wildberries در منطقه سمارا دچار آتش‌سوزی شد، این اتفاق پس از حمله اوکراین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69433" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69432">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5208110eae.mp4?token=XbBcsf17yCuz1FT8w_LVkwbVvnseEdycyrDJv0fpQ8BrV_n46Znl5KCqsO9GRS7dNh5og60Fb89h2QzGTNIsdHa2jgkSbRQuvcxadW-DS-MZvyJw3Y89CNDPHc_pes6-TsDytw7qz63JIpybqXm9N49_qLeVK3lh-wYTjYZ9fbnBImK7SYi7bxB67JOGicrKW8sl3z86GGD4eLJbNwXqQ7ivODiokPa3bN8b9pI9U26qiLfkVXr7b2nRGgk3n3bPvD33xTn0rWOM_6qewFhhpyyZfzcaYBANnTe-L6DrdTFJb3f-4c2HI7EuK2lnxJ-l0mon7GilvHxi2BZxP0pdmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5208110eae.mp4?token=XbBcsf17yCuz1FT8w_LVkwbVvnseEdycyrDJv0fpQ8BrV_n46Znl5KCqsO9GRS7dNh5og60Fb89h2QzGTNIsdHa2jgkSbRQuvcxadW-DS-MZvyJw3Y89CNDPHc_pes6-TsDytw7qz63JIpybqXm9N49_qLeVK3lh-wYTjYZ9fbnBImK7SYi7bxB67JOGicrKW8sl3z86GGD4eLJbNwXqQ7ivODiokPa3bN8b9pI9U26qiLfkVXr7b2nRGgk3n3bPvD33xTn0rWOM_6qewFhhpyyZfzcaYBANnTe-L6DrdTFJb3f-4c2HI7EuK2lnxJ-l0mon7GilvHxi2BZxP0pdmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی امور خارجه، اسماعیل بقایی:
مدیریت آینده تنگه هرمز توسط ایران و با مشورت عمان انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69432" target="_blank">📅 20:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69431">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04acf28261.mp4?token=XEcZSALoPXZIAs2oWloLRMOIXAZ1JFxhGQdbUBPLN8sL6hqNEWYMeKS-YFNAzh_N2WKHGZEq58LGH-whfMsF17GhQNDvUgDEvUrDc0TxCUliY-ptJT20WqwtYRR4tyjbov3WSd5XeO6oNwCZPKJDbZFCIQWbjtq8CFhCQRRo0lUjaO_TzfBVWZZ0keSPut9nVKg3-FyqhbT_4P_yxBhszGfOKS7JgksE0jKe_TJoXVydb0R44u84DNo3MLYewCk2QHRP9MhrjIy2jh1oZkUKCg7W-_X9XatKEf-gn0lWKWDC5a4TuQmkcdFbUpW_DGPqhdOVs3yQCGtvghy1YdqGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04acf28261.mp4?token=XEcZSALoPXZIAs2oWloLRMOIXAZ1JFxhGQdbUBPLN8sL6hqNEWYMeKS-YFNAzh_N2WKHGZEq58LGH-whfMsF17GhQNDvUgDEvUrDc0TxCUliY-ptJT20WqwtYRR4tyjbov3WSd5XeO6oNwCZPKJDbZFCIQWbjtq8CFhCQRRo0lUjaO_TzfBVWZZ0keSPut9nVKg3-FyqhbT_4P_yxBhszGfOKS7JgksE0jKe_TJoXVydb0R44u84DNo3MLYewCk2QHRP9MhrjIy2jh1oZkUKCg7W-_X9XatKEf-gn0lWKWDC5a4TuQmkcdFbUpW_DGPqhdOVs3yQCGtvghy1YdqGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی وزارت خارجه اسماعیل بقایی:
توافق ایران و عمان بر سر مسیر جدید هیچ ارتباطی با بازگشایی تنگه هرمز یا حفظ بسته بودن آن ندارد.
مسیر جنوبی از طریق تنگه هرمز با ناامن کردن منطقه و آسیب رساندن به منافع ملی ایران همراه بوده است و تهران آن را نمی‌پذیرد.
مسیر مورد توافق نه مسیر شمالی و نه مسیر جنوبی فعلی خواهد بود. در عوض، مسیر جدیدی خواهد بود که هر دو طرف متقابلاً بر سر آن توافق دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69431" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69430">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=qHrwsL4q7QRa6IYFQclkZbZplXSbXpD37XinxsgRsQeTVunD8e51-ge_Ag3azoPyXOPvgdetRuawnZMzO-uMrOMX0LSutd1M3Ls_8UrcWNmQ9yZCSOK0kzdXYUUUeyDt6VZy1gMZKoV0SnRZh0ZX4Pjk-Jc4bnOwZK5_3k4lzMN8au6ZmeFNhk9_ayreLAH_udu8GgAXTLXFgOpss-k9DBTm9zRAsEJ2ZpY_O_gzqVBO-WtuReiznlc9P95WVawS_2W_12eO083zBRU8VQ-c0Ne-jZT1Cz2GMVk1UEPaBdR4r1zef_SCHow3YtLZyI8mXnPIC9YFKmQsilw97QF2nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=qHrwsL4q7QRa6IYFQclkZbZplXSbXpD37XinxsgRsQeTVunD8e51-ge_Ag3azoPyXOPvgdetRuawnZMzO-uMrOMX0LSutd1M3Ls_8UrcWNmQ9yZCSOK0kzdXYUUUeyDt6VZy1gMZKoV0SnRZh0ZX4Pjk-Jc4bnOwZK5_3k4lzMN8au6ZmeFNhk9_ayreLAH_udu8GgAXTLXFgOpss-k9DBTm9zRAsEJ2ZpY_O_gzqVBO-WtuReiznlc9P95WVawS_2W_12eO083zBRU8VQ-c0Ne-jZT1Cz2GMVk1UEPaBdR4r1zef_SCHow3YtLZyI8mXnPIC9YFKmQsilw97QF2nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کارشناس صداسیما:
مسعود رجوی (رئیس سابق مجاهدین خلق) فرد باسواد و کتاب‌خونده‌ای بود و قطعا خیلی باهوش‌تر از رضا پهلوی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69430" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69429">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=r1uWiQVIb8Mybv-uzD9bZeYRKurBMWpAe3ntC4Emn7ew20p2XHSBFvgu73Szdt4o0TtfOb32MW67TkcWh2JpYKGS4bxNd5dVjKVzyEXLthm9VKtpjbnRllucwrlK8GwfNxHRFGYOYDtO7tm6qiJztfaqrNYMmoe8lhLa7NUUWBD5CAynZRqlgbmk7PFGo5PHQQ2Pz0bOp07u_x0mI_Y_mzSQDzEWkI_vWA0yUDhVN7ooLPvNRf8xFyoHc5aIvdImC6Bn7ETxMYQE9NossF5IEJKl10etBE1tB9tcnIMqg8VJ4PSwAlo2cU83eIfc4YAJh3B6X49fEYd65_m71HIHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=r1uWiQVIb8Mybv-uzD9bZeYRKurBMWpAe3ntC4Emn7ew20p2XHSBFvgu73Szdt4o0TtfOb32MW67TkcWh2JpYKGS4bxNd5dVjKVzyEXLthm9VKtpjbnRllucwrlK8GwfNxHRFGYOYDtO7tm6qiJztfaqrNYMmoe8lhLa7NUUWBD5CAynZRqlgbmk7PFGo5PHQQ2Pz0bOp07u_x0mI_Y_mzSQDzEWkI_vWA0yUDhVN7ooLPvNRf8xFyoHc5aIvdImC6Bn7ETxMYQE9NossF5IEJKl10etBE1tB9tcnIMqg8VJ4PSwAlo2cU83eIfc4YAJh3B6X49fEYd65_m71HIHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
من یه مشکلی برام پیش اومد که گفتم نمی‌تونم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و غلامرضا رضاییان، رییس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69429" target="_blank">📅 19:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69426">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=sS2i73m4UTaBSVYvPdUh06QJFFGtTf9Q-BLmEyFjJk8eLA5hxlq22lqWu8OUs9mMT2jJLPd-frs4q_bJin2iqISiO8l9JT_MdP4WATlpAHaUGhIEpCO35z0J0-b2f4UMDuH2uZ-tN_ceV44tkQ_RnQd8aZ26nM8qOZk8063p4gKhRIIB7JjuztDhZX8m_yaY8AJCaP6P7_FDlsnsCN5mp7ksfMnhL2BcsbsZ-b-x9HFjF_oi1YbS94PR25EVyiZN02Cw1OWU-XhJ9KOXbSLhBwf8ZLXUn5zUDdYfru-fO1c4YCzRwMoOkQBdTt7CH9YMlndHl4579b8UsVf9u_b1Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=sS2i73m4UTaBSVYvPdUh06QJFFGtTf9Q-BLmEyFjJk8eLA5hxlq22lqWu8OUs9mMT2jJLPd-frs4q_bJin2iqISiO8l9JT_MdP4WATlpAHaUGhIEpCO35z0J0-b2f4UMDuH2uZ-tN_ceV44tkQ_RnQd8aZ26nM8qOZk8063p4gKhRIIB7JjuztDhZX8m_yaY8AJCaP6P7_FDlsnsCN5mp7ksfMnhL2BcsbsZ-b-x9HFjF_oi1YbS94PR25EVyiZN02Cw1OWU-XhJ9KOXbSLhBwf8ZLXUn5zUDdYfru-fO1c4YCzRwMoOkQBdTt7CH9YMlndHl4579b8UsVf9u_b1Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💋
🇮🇷
این جنده‌اینستاگرامی که خیلی ماجراش وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های
🔞
عجیب منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69426" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69425">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=Ae-BUkEfKmg6g4RAR-ixJbntcz3pfQ2lJBh3wCeT9IfrcTX7t7siMHx_tLoUJPg1qrcrMOakulvCHMN5vXHyI_S8Z4y40W0jf9mw1IQDRLfKbJKBRgM8UuHqISGyia-DUL60oCdzg732_fTH5vWnMS8z3_Yz3SzoxHzdmBIkL_igZn_mWWlw4H564I4abULNyul-E_PMoCm4eUCAyMWyhjluAZOb14nCCzM56qG8aWC2jdowq9gOfbDHepu8xuq1RMFAYnZgO0KPBO3fqCNy50HBGLEut5I5-zGanF-u_QWXalYk9q2kr_6R3XMWxyZb4LLaQ1m2t6NlSPqMajUUSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=Ae-BUkEfKmg6g4RAR-ixJbntcz3pfQ2lJBh3wCeT9IfrcTX7t7siMHx_tLoUJPg1qrcrMOakulvCHMN5vXHyI_S8Z4y40W0jf9mw1IQDRLfKbJKBRgM8UuHqISGyia-DUL60oCdzg732_fTH5vWnMS8z3_Yz3SzoxHzdmBIkL_igZn_mWWlw4H564I4abULNyul-E_PMoCm4eUCAyMWyhjluAZOb14nCCzM56qG8aWC2jdowq9gOfbDHepu8xuq1RMFAYnZgO0KPBO3fqCNy50HBGLEut5I5-zGanF-u_QWXalYk9q2kr_6R3XMWxyZb4LLaQ1m2t6NlSPqMajUUSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند پناهیان به پزشکیان و قالیباف:
همه پیامبران را مسخره کردند؛ از تمسخر نترسید و با عظمت صحبت کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69425" target="_blank">📅 18:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69424">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇷
بیانیه سپاه پاسداران :
انتقام خون رهبر شهید و اسماعیل هنیه اجتناب ناپذیره
پاسخ این جنایت بشدت سخت و قاطع و سخت گیرانه خواهد بود
توطئه خلع سلاح حماس به نتیجه نخواهد رسید و از همین الان شکست خورده بدانید
دنیا بداند اراده ضد صهیونیستی ادامه دار خواهد بود و پیروزی نهایی فلسطین خیلی نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69424" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69423">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=KZH8XVmKyNSwyJHKDQe6jQokkebTkiQgtyDyyjgD5SaRENb6DPNrc_j4fVe0GTlFbNCp2tfVIsPfn651nBDWoRqkX7pNkgI-1qVzRuMOFRoLNzPS1Lkf27NLBnjWxT0iNe2BvPl_BYqjYDhrImchAHhaz8vvH-VU9OdB5Eq1g2v-nH5iTPUgQgu1x71Vbj_wlnk0uSaICAuwge531CAHs9OVxKoIhAggLGUxEjh3SfW_PxX1RJazpO47iKIAt37LqiBelwB9AyomDp45h9cL4rOMH_GqqH8WlQiq7xeTIDZFIApvjGVqXjyyGJSYVs2Yyal30mnaKdUYIw3mGfeExA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=KZH8XVmKyNSwyJHKDQe6jQokkebTkiQgtyDyyjgD5SaRENb6DPNrc_j4fVe0GTlFbNCp2tfVIsPfn651nBDWoRqkX7pNkgI-1qVzRuMOFRoLNzPS1Lkf27NLBnjWxT0iNe2BvPl_BYqjYDhrImchAHhaz8vvH-VU9OdB5Eq1g2v-nH5iTPUgQgu1x71Vbj_wlnk0uSaICAuwge531CAHs9OVxKoIhAggLGUxEjh3SfW_PxX1RJazpO47iKIAt37LqiBelwB9AyomDp45h9cL4rOMH_GqqH8WlQiq7xeTIDZFIApvjGVqXjyyGJSYVs2Yyal30mnaKdUYIw3mGfeExA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو هلیکوپتر آتش‌نشانی در حین مبارزه با آتش‌سوزی جنگلی در نزدیکی پساتا، یونان، در هوا با هم برخورد کرده و سقوط کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69423" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69422">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=nT6V2m_3IYqUiZU4fq6WpfpZQlqAHJ_NMF97NDWX2NDk_eF3BCs4PUBukjklXNTfF7OVq_c6qYGhiDVGZlhsSA1DC_IrabIBXJntJJJBwRDIKKMr8xeiwwXZq91cgtxEUKCrxi4YS-4k7AQQPXIkkd23VVi2NgXmdPGB-2WomwhhZ3qXHZV6UtmAbERYxPkQx7QV-d_lGFUEiowAxUs7HtVhJGdSVPrPl1aCwgCm4PkGJv-7vah_gbjWMan0d50BwG_xpBwhU1NKREDb5t5ELfuGP6hlUHJyXPUyo0xn6lG64xdtzeuI0pjmvaTxBtpAL5BGPnfs3DVN5iweUuYr0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=nT6V2m_3IYqUiZU4fq6WpfpZQlqAHJ_NMF97NDWX2NDk_eF3BCs4PUBukjklXNTfF7OVq_c6qYGhiDVGZlhsSA1DC_IrabIBXJntJJJBwRDIKKMr8xeiwwXZq91cgtxEUKCrxi4YS-4k7AQQPXIkkd23VVi2NgXmdPGB-2WomwhhZ3qXHZV6UtmAbERYxPkQx7QV-d_lGFUEiowAxUs7HtVhJGdSVPrPl1aCwgCm4PkGJv-7vah_gbjWMan0d50BwG_xpBwhU1NKREDb5t5ELfuGP6hlUHJyXPUyo0xn6lG64xdtzeuI0pjmvaTxBtpAL5BGPnfs3DVN5iweUuYr0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی اینو ببینید توی پخش‌زنده صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69422" target="_blank">📅 17:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69421">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejQFmhGmwjoFaHbOO-KlHaTTQrG6QWDgiiul6reAI3rHfm2pAAs3xHRtMTPqlSW5WUHBY7dADIJwekXT5GdSR_Jc8F_9QtOqOJS4sE9FZWRu3cEJm21wye3p5fJNhsWX-Pk_NecsuoRwOP4hV2DQ4ms4Erjel8x8Wxdh3zoA1IKm_L2fH5qx49D74EMwEPxHoOk5LFWXc73N-vHRMOT9cg78JfcClC7GBspGctn_ff8znkd4Qr57URXlQqjfZHkCdCd5-P4liEry3MhHm_QYC8YP08KoqtrDmHPWxHmymcsZ535yWEnO_psYKdpHIjtBGqC5NotXFfqgIpE9AT6vsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
نیویورک پست:به گفته منابع آگاه، در حالی که رهبران اعتراضات در تلاش برای دستیابی به سلاح هستند، انقلاب ایران ممکن است «هر لحظه» رخ دهد.
چهره‌های مخالف حکومت در تهران به نشریه «پست» گفتند که خیابان‌های ایران به دلیل اعدام‌های در ملأعام، فروپاشی اقتصادی و جنگی که بیش از پنج ماه است ادامه دارد، به مرز انفجار رسیده‌اند.
یکی از رهبران اعتراضات با اشاره به سرکوب بی‌رحمانه ماه ژانویه توسط رژیم — که به گفته رئیس‌جمهور ترامپ منجر به کشته شدن ۵۲ هزار نفر شد — گفت: «انقلاب ممکن است هر لحظه رخ دهد؛ مردم خواهان انتقام هستند.»
یک روزنامه‌نگار مستقلِ فعال در جریان‌های زیرزمینی ایران گفت که تدارکات برای خیزش بعدی هم‌اکنون در حال انجام است و فعالانی از تمامی اقشار جامعه مصمم‌اند تا ضربه‌ای نهایی و تعیین‌کننده به رژیم وارد کنند.
این روزنامه‌نگار گفت: «ما در حال بررسی اعتراضات ماه ژانویه و تشخیص این نکته هستیم که چه تاکتیک‌هایی مؤثر بوده‌اند و کدام‌یک نه؛ همچنین نقشه‌ها را تحلیل می‌کنیم تا امن‌ترین و خطرناک‌ترین مناطق برای تجمع را شناسایی کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69421" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69420">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OL8JgMDTqgs8xkZfBBAuXDY7aPdYqDZmmZ9Jev0Y3_gvkyGYBuJQ40QfQXKpy8Ieyd84rhO0Od-Ei0bvdaxUkjH-N0Pb3gNREll8kSfbvyZLLsTt3BK4igotpgE5Ji0IUQh-vsAjett_5_-AO8hzjM0chlsj7QP8d6djl38dslEBCLV85p5tTRSCuaZSzrUTRdopyXv-Uydn3Vj7ol4FM4UNi-9vSTxXKzlvIPVzQzNj_JVNs0mTwr5UYmeTTXOAEMdSd9vHAq5Pvz5ydG7IxQRJrO8QXQBU-CH9snnxKG93lpdarD31GZ9eyafuggOU5RSZiDsfwCgf1Tmi9K_Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
صفحه فارسی وزارت خارجه اسرائیل:
هفته خوبی از اسرائیل برای شما آرزومندیم!
💦
اسرائیل داغ‌تر از همیشه به نظر می‌رسد... و ما فقط در مورد آب و هوا صحبت نمی‌کنیم
😉
🇮🇱
☀️
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69420" target="_blank">📅 16:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69419">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=EanpQtv0q9bybcWhhO15qM12gKtdFDb--eLAzrK6cBmow5Jen2SOm_sJo05kid4s16rcAhxged3aSVfnmHmmbDs8Fq7VhmuDTi5FgZkV8PgeBsjsJcSTyVgfDGVbmI3XGGG2cSrRhwCvlpKgrzphXaSGjzc31iWNJQ5r7X49S6faWVtc4p6lfXzHrO3wZ7cQejPLIoEbJ24RBll33ZTKQsj4CauH3_kV9irfrPxR_PW3wZzaxfU8myEYkIZH6gc75hpXDnEZB1NVD2oRtexGeZlHkZr-WKYK0DNaf1mpPydt9LU5pYur99EQuZ28NxQpqtEpTTdlXrjnJvfnMxkVrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=EanpQtv0q9bybcWhhO15qM12gKtdFDb--eLAzrK6cBmow5Jen2SOm_sJo05kid4s16rcAhxged3aSVfnmHmmbDs8Fq7VhmuDTi5FgZkV8PgeBsjsJcSTyVgfDGVbmI3XGGG2cSrRhwCvlpKgrzphXaSGjzc31iWNJQ5r7X49S6faWVtc4p6lfXzHrO3wZ7cQejPLIoEbJ24RBll33ZTKQsj4CauH3_kV9irfrPxR_PW3wZzaxfU8myEYkIZH6gc75hpXDnEZB1NVD2oRtexGeZlHkZr-WKYK0DNaf1mpPydt9LU5pYur99EQuZ28NxQpqtEpTTdlXrjnJvfnMxkVrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از نیروهای سرکوبگر: تا تهش پای حکومت وایسادیم، بازم بیاین بیرون بهتون رحم نمی کنیم!
چون داریم دستور خدا رو انجام میدیم، شما اصلا کسی نیستین جلوی جمهوری اسلامی وایسین.
کل دنیا هم جمع بشن نمیتونن کاری کنن، پاینده جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69419" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69418">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f215b551.mp4?token=tKhq9ffstUGDMWPJFXO6paUusvexcXcqVDlqsgDh9DJW1b3kGF1hL2440riBWVV_cOCurapQoF0F4se13hzgkBbGQp4WbHtvXjb5zB4UzsfDMNpAq_QkrfFcGdN7uQSQvyOvp0glBfJkMWe9iynunbMz47b884_XLrqSSiHSIw0E25D2Qs5Dh-EH2IZk5pEuDGsVQs-5H0eOULx3lP2qddIU6JDAvp40OK-zKbgBJ6QzqA41-qzpzT3488yDpdTNs6vvw6in47gHH2tvh8Nyq18GueJlzBDbfKKB3UYW5Axu7GXfDJD-gxgueYehyuaCCh137Ovy_xCqaCIQ4w8_xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f215b551.mp4?token=tKhq9ffstUGDMWPJFXO6paUusvexcXcqVDlqsgDh9DJW1b3kGF1hL2440riBWVV_cOCurapQoF0F4se13hzgkBbGQp4WbHtvXjb5zB4UzsfDMNpAq_QkrfFcGdN7uQSQvyOvp0glBfJkMWe9iynunbMz47b884_XLrqSSiHSIw0E25D2Qs5Dh-EH2IZk5pEuDGsVQs-5H0eOULx3lP2qddIU6JDAvp40OK-zKbgBJ6QzqA41-qzpzT3488yDpdTNs6vvw6in47gHH2tvh8Nyq18GueJlzBDbfKKB3UYW5Axu7GXfDJD-gxgueYehyuaCCh137Ovy_xCqaCIQ4w8_xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدئو با اختلاف زیاد عجیب‌ترین و دارک ترین چیزیه که تا آخر هفته می‌تونید ببینید؛
هربار یکی از این خانواده رو دنبال کنید تا متوجه عمقِ نفهمیدن بشید...
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69418" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69417">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d8743494.mp4?token=OKYsWOwR489U6hnU_VZS6NmVWerCDItK3HWhMt6uxWGzx0NOZ0XlY9WSOZI6RksRnaX72Z7hArkNv5kQl_Jy07PuaZZpIkxLboKUkhl68rng2FDpALSnzYAfvTeuLKhqjlLvviGAwa4KkMpF1JD-x1P6HR3ohJFdo2TPeWGhNqioRw817POgptOcEpCtRiDHxx1Gzx29gwMhCbeIZVwbuLG_WstiMz4JLuO7_rrYc33SAixhRJ2_O46URaq8EPJ6vQ90pMKa_IUuI-_b8qdlt8m3DoTVh6B6n7SfdWON2WoLc9TqTUphAqr68i_-dScppowPAAkevb4Osre4fZRdnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d8743494.mp4?token=OKYsWOwR489U6hnU_VZS6NmVWerCDItK3HWhMt6uxWGzx0NOZ0XlY9WSOZI6RksRnaX72Z7hArkNv5kQl_Jy07PuaZZpIkxLboKUkhl68rng2FDpALSnzYAfvTeuLKhqjlLvviGAwa4KkMpF1JD-x1P6HR3ohJFdo2TPeWGhNqioRw817POgptOcEpCtRiDHxx1Gzx29gwMhCbeIZVwbuLG_WstiMz4JLuO7_rrYc33SAixhRJ2_O46URaq8EPJ6vQ90pMKa_IUuI-_b8qdlt8m3DoTVh6B6n7SfdWON2WoLc9TqTUphAqr68i_-dScppowPAAkevb4Osre4fZRdnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بر اساس تصاویر ماهواره‌ای، پایگاه هوایی شیخ عیسی در بحرین که مورد استفاده نیروهای آمریکایی است، اخیراً تخلیه شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69417" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69416">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=lQqOMfB8bESa76kBCwQ9y5U01vodcxOZZ9-JIkGbjF_5OT6PxDQ_EGCFsGQ9b7UFavAUdAgftyXZjgAXy7kUbZd9sfC8lJH9GT2xMzY_s5iMaQ6al7x9bBauoyUVmB8AV5R_mx20hc_qnyXh7Mz_1pBhj8al9622O8aOp2LRU1AP1R6Ij-H8tDgY5jraa3O3GKG4Hv02iXCUJdLAn5GMaNif2zbGLOiti3XZMFeapZGrHi1e_MHIdN1xH0fVuvVDZRR4j-F0v5PEvLSk4HWCrkXYZqcRYBJ5S_9uDYIHSdwdB4_JIYbA_rZHOMuWFHK9PW9PzHcoSQqv9nhLDFKmWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=lQqOMfB8bESa76kBCwQ9y5U01vodcxOZZ9-JIkGbjF_5OT6PxDQ_EGCFsGQ9b7UFavAUdAgftyXZjgAXy7kUbZd9sfC8lJH9GT2xMzY_s5iMaQ6al7x9bBauoyUVmB8AV5R_mx20hc_qnyXh7Mz_1pBhj8al9622O8aOp2LRU1AP1R6Ij-H8tDgY5jraa3O3GKG4Hv02iXCUJdLAn5GMaNif2zbGLOiti3XZMFeapZGrHi1e_MHIdN1xH0fVuvVDZRR4j-F0v5PEvLSk4HWCrkXYZqcRYBJ5S_9uDYIHSdwdB4_JIYbA_rZHOMuWFHK9PW9PzHcoSQqv9nhLDFKmWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر مارو خندوندی حاج اقا دارم پاره میشم
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69416" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69415">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🇮🇱
بنسالل اسموتریچ، وزیر دارایی اسرائیل:
رژیم ایران در جریان جنگ سقوط نخواهد کرد.
مردم ایران در شرایطی که هواپیماهای اسرائیلی و آمریکایی بر فراز آسمانشان در پرواز بودند، به خیابان‌ها نمی‌آمدند؛ چرا که نمی‌خواستند در نظر دیگران، همدست دشمن به نظر برسند.
تأکید اصلی باید بر این موارد باشد: اقتصاد، اقتصاد، اقتصاد و باز هم اقتصاد. این همان عاملی است که در نهایت موجب سقوط رژیم خواهد شد.
به گمان من، رژیم ممکن است به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی چنین وضعیتی پیش بیاید، ترس دیگر مانعی نخواهد بود؛ آنگاه مردم به خیابان‌ها می‌آیند، قیام می‌کنند و رژیم را سرنگون می‌سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69415" target="_blank">📅 13:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69414">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
خبرگزاری فارس، وابسته به سپاه:
گزارش‌های حاکی از موافقت ایران با بازگشایی تنگه هرمز نادرست است و هیچ تغییری در سیاست تهران ایجاد نشده.
منابع نظامی گفته‌اند این آبراه راهبردی همچنان بسته است و عبور از آن نیازمند مجوز صریح و هماهنگی با نیروی دریایی سپاه پاسداران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69414" target="_blank">📅 12:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69413">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835653bd72.mp4?token=WIMh4SPCwXuJXyDj0eJIzi3jRH7Oesr3SMuJMjVx7XTmL3QIBaoNl_aSOW1bnKQLBbQ2F8XmuEcKCKmiACRA14Eppi-AjqpmZx2Lix-80_ZbVf8d3T5k6WdvA8XdaL15DDfjXk_zG-6ASeaPAtMFFrH3CCknbaCJnlFCpWhA9QPuo9SXhD52APhzQBRCaiMmHy7GNMytIEjN3uw_j_DTpGV50Cafj7xeZP38MhpyhxuuCiJ0NszfZ6eGxRdGppZTOeJUPP7lUymJ48soGemK1UjtxAdyRBf6YGGGvpjBMAFdrP-24kp2zKT619rvQF5v1ZtLqxsxjpyEmWdojfknXTmeovVvTuUZTrWiiDDSyyG5CwNyimAueHXdhfql-yQbdhpUDgNqkR-6lrof9MEtHQuySkJUkdAwWM1f2k-_XcstveA52OXj7v_wy4ATZT-EW1i6ELAvEEYeTUkmo8cHTNgx5UkHbh2uKUjDQgGn73_2FlLuYMQP556YPT0GQ8SDf8yfYCj6DG5w8jEgK1cPlarP-hVtKzohu3F09PdeNqT6xDeWtq_HZoEj100IN-nRCO4FaWIKTFAUXET3CcnebLJx31nf-ZP0J-DBf1Jt1Aw34hYjYAIznfYULsUDinPCq6SCckc7HfovUaeNJkuKT_kkzXR9KtMtXMGCa9P69S0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835653bd72.mp4?token=WIMh4SPCwXuJXyDj0eJIzi3jRH7Oesr3SMuJMjVx7XTmL3QIBaoNl_aSOW1bnKQLBbQ2F8XmuEcKCKmiACRA14Eppi-AjqpmZx2Lix-80_ZbVf8d3T5k6WdvA8XdaL15DDfjXk_zG-6ASeaPAtMFFrH3CCknbaCJnlFCpWhA9QPuo9SXhD52APhzQBRCaiMmHy7GNMytIEjN3uw_j_DTpGV50Cafj7xeZP38MhpyhxuuCiJ0NszfZ6eGxRdGppZTOeJUPP7lUymJ48soGemK1UjtxAdyRBf6YGGGvpjBMAFdrP-24kp2zKT619rvQF5v1ZtLqxsxjpyEmWdojfknXTmeovVvTuUZTrWiiDDSyyG5CwNyimAueHXdhfql-yQbdhpUDgNqkR-6lrof9MEtHQuySkJUkdAwWM1f2k-_XcstveA52OXj7v_wy4ATZT-EW1i6ELAvEEYeTUkmo8cHTNgx5UkHbh2uKUjDQgGn73_2FlLuYMQP556YPT0GQ8SDf8yfYCj6DG5w8jEgK1cPlarP-hVtKzohu3F09PdeNqT6xDeWtq_HZoEj100IN-nRCO4FaWIKTFAUXET3CcnebLJx31nf-ZP0J-DBf1Jt1Aw34hYjYAIznfYULsUDinPCq6SCckc7HfovUaeNJkuKT_kkzXR9KtMtXMGCa9P69S0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گزارش روزنامه همشهری از دلایل عدم انتشار صدای مجتبی خامنه‌ای :
از طریق صدا میتونن پیدا بکنن چون هر فضای بسته امضای صوتی منحصر به فردی داره و از بازتاب صدا از طریق فرش و دیوار میتونن مکان رو تشخیص بدن و ارتفاع اتاق و فاصله گوینده رو از محل بازتاب رو پیدا بکنن
همچنین از طریق تحلیل شبکه برق میتونن ردیابی بکنن چون همهمه ضعیف الکترومغناطیسی در پس زمینه صدا ضبط میشه و سرویس های اطلاعاتی میتونن از طریق شبکه های اتصال برقی مکان رو ردیابی بکنن
هر میکروفون و دستگاه ضبط اثر متفاوت داره و مختص خود دستگاهه مثل اثر انگشت خود شخص لذا از طریق ردیابی دستگاه میتونن مکان رو پیدا بکنن
صدای پس زمینه مثل خنک کننده ها یا ژنراتور ها و حتی توی مکان باز صدای ترافیک ها و صدای محیط و نوع حشرات و پرندگان میتونن محل جغرافیایی رو لو بدن
😳
😳
ویس ابعاد فیزیکی نای دهان و مجرای صوتی رو نشون میده و حتی فیلتر هم باشه با دستگاه هایی میشه ردیابی کرد و تشخیص داد طرف زنده باشه محل حضورش کجاست
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69413" target="_blank">📅 12:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69412">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇺🇸
ویدیو ای که صفحه رسمی وزارت جنگ آمریکا به تازگی منتشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69412" target="_blank">📅 11:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69411">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=F-tBatqkKy5fjfXwEt_dgareuPXuV0owMZr39WCn3PxstSH_k4dlsRkbhHdWwvhvkoXFX_vyiNIjRhG4NNnDSyAxeGHotLyUWxygZmV1h8z49OwROGArUn_nyqD3P0RIaL6LLBuwenK28i5FhtY3Tk3WZNbZ8rmAt6EiOUfgdC2nL5szuH1weoxN91_td2Fx2kwdsZ7l064mlnSr29KLF9AsE-2kZvOuarVM1-t2vT7cGQGLYQ3Ir69bXTn59ruu1IjhAZnwOZHMAakFYsoB07cTlaF1M5TxbgGUeKRwu9QIDAdhuwtjfY5HTsJ3WYSvbBlUt4TjSobexH_ReCuIWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=F-tBatqkKy5fjfXwEt_dgareuPXuV0owMZr39WCn3PxstSH_k4dlsRkbhHdWwvhvkoXFX_vyiNIjRhG4NNnDSyAxeGHotLyUWxygZmV1h8z49OwROGArUn_nyqD3P0RIaL6LLBuwenK28i5FhtY3Tk3WZNbZ8rmAt6EiOUfgdC2nL5szuH1weoxN91_td2Fx2kwdsZ7l064mlnSr29KLF9AsE-2kZvOuarVM1-t2vT7cGQGLYQ3Ir69bXTn59ruu1IjhAZnwOZHMAakFYsoB07cTlaF1M5TxbgGUeKRwu9QIDAdhuwtjfY5HTsJ3WYSvbBlUt4TjSobexH_ReCuIWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واکنش پزشکیان به تاخیر ۱۰ روزه در  پرداخت حقوق اعضای هیئت علمی دانشگاه‌ها:
این واقعاً قابل قبول نیست، کاری کنید که اساتید بیش از این ناراضی نشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69411" target="_blank">📅 11:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69410">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل:
عراقچی، وزیر امور خارجه ایران، شبانه با یک مصالحه میان قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد؛ اقدامی که باعث شد دونالد ترامپ، رئیس‌جمهور آمریکا، حملات تلافی‌جویانه برنامه‌ریزی‌شده را لغو کند.
بر اساس این طرح، کشتی‌های عازم خلیج فارس از طریق آب‌های سرزمینی ایران وارد و از مسیر آب‌های عمان خارج خواهند شد؛ هرچند عمان خواستار تأیید رسمی این موضوع شده است که سپاه پاسداران از این توافق حمایت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69410" target="_blank">📅 11:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69409">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66dc919056.mp4?token=a_sBGNZuZ_P_VdUnD8Mzxrj5hEskfFzLsVydDltHwhjoh1_m9sgoqLXL5MhGc1ZJ4spdltkA1Nc77V3GO9WAO6utqXY33pqPEstIVJgo7XXdWahboby2uRNn4JpO8U_eeuwI48nHiCtHr3Nq6PgU8xCqeVuMQHJh3mubCbRQcmjU5SmdFU_PQ6EonEKnLC_04WBpCXYBpBAmrMg_Nmv-165c0a1i03utlfw1SAqRDtlpL0dfg-p7gIk87lNuHJ0CDZEqB9ofZBeBk0llUbVns6vvUzU2ug0QVL8UBlCvZim57xA9ahwCE97IB0VOuTOBIt-Dxnj7_935L3n6gIm1hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66dc919056.mp4?token=a_sBGNZuZ_P_VdUnD8Mzxrj5hEskfFzLsVydDltHwhjoh1_m9sgoqLXL5MhGc1ZJ4spdltkA1Nc77V3GO9WAO6utqXY33pqPEstIVJgo7XXdWahboby2uRNn4JpO8U_eeuwI48nHiCtHr3Nq6PgU8xCqeVuMQHJh3mubCbRQcmjU5SmdFU_PQ6EonEKnLC_04WBpCXYBpBAmrMg_Nmv-165c0a1i03utlfw1SAqRDtlpL0dfg-p7gIk87lNuHJ0CDZEqB9ofZBeBk0llUbVns6vvUzU2ug0QVL8UBlCvZim57xA9ahwCE97IB0VOuTOBIt-Dxnj7_935L3n6gIm1hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
با این حال، تغییر رژیم هرگز هدف اصلی نبوده است؛ هدف، خلع سلاح هسته‌ای بوده است. آیا می‌توان یکی را بدون دیگری داشت؟
🇺🇸
مارکو روبیو:
هرکاری که توی خاورمیانه و جهان انجام دادیم کسی مانع ما نشده و موفقیت بدست آوردیم
رژیم باید تغییر بکنه شما شاید تغییر رژیم نداشته باشید ولی باید اینا تغییر بکنه
اونا میخان
انقلابشون رو به کل دنیا صادر بکنن و باید این تغییر پیدا بکنه
ایران تابحال با رئیس جمهوری مثل ترامپ که مرد عمل هست رو به رو نشده
اونا هنوزم موشک و پهپاد دارن میتونن صدمه بزنن ولی خب سپری ندارن پشتش قایم بشن
از روی قدرت باهاشون مذاکره میکنیم نه ضعف
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69409" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69408">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=ovJbxgOI7eISAb10PlIdR5VnUMP-WICvs16avyVlJSLC9Wb0PswNBtVT6qjL-mve5l_0Od_nIuTPlzRhstJwk02B6esrCdSS-GqsYj9sB2K7TuWQ5C5b5G1gFIrqK4W1hii2DLMAYXcu9bxT_08CQHRc6mTL47uyohNOvZtNQnCOd5Z237rByH-Oib5T4bDMyz4GzGTSKEFwV_XXS3_TL8r1agWQHAM8w1n-VtJ4Cbpqw2iKY2Od6lwXQF9KHNe7f7KpPfjcMrdfBpReZ5DmKgXRPK9H-FJ5HfHuspRqjHtcP2im1nx-IHDwXz-b9I55ZtixBuoUj7tvjTZXIQPoew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=ovJbxgOI7eISAb10PlIdR5VnUMP-WICvs16avyVlJSLC9Wb0PswNBtVT6qjL-mve5l_0Od_nIuTPlzRhstJwk02B6esrCdSS-GqsYj9sB2K7TuWQ5C5b5G1gFIrqK4W1hii2DLMAYXcu9bxT_08CQHRc6mTL47uyohNOvZtNQnCOd5Z237rByH-Oib5T4bDMyz4GzGTSKEFwV_XXS3_TL8r1agWQHAM8w1n-VtJ4Cbpqw2iKY2Od6lwXQF9KHNe7f7KpPfjcMrdfBpReZ5DmKgXRPK9H-FJ5HfHuspRqjHtcP2im1nx-IHDwXz-b9I55ZtixBuoUj7tvjTZXIQPoew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مرادویسی، تحلیلگر ارشد اینترنشنال:هدف‌های احتمالی آمریکا تو جنگ جدید میتونه شامل این موارد بشه:
1. مراکز نظامی سپاه تو جنوب کشور
2. شهرهای موشکی و پهپادی تو عمق خاک ایران
3. تاسیسات هسته‌ای "کوه کلنگ"
4. مراکز نظامی سراسر کشور
5. سامانه‌های پدافندی و راداری
6. پایگاه‌های هوایی ارتش
7. مراکز و نهادهای حکومتی
8. ساختارهای سرکوب (سپاه، بسیج و نیروی انتظامی)
9. مقامات و فرماندهان ارشد باقی‌مونده
10. مکان‌های نمادین مثل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/69408" target="_blank">📅 09:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69407">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=Xqp-MK1zfQYNUyGfZPTlEVFcXSiOKgyrz8YTjUPuViQUj8MjG4bxIAVTZkG-Xz0yWMiHNiNPwfbdVNvnhwfCNgUj6JYpr_teTXlB3BzVemFnrduo_C2wssD0-2mQQ0AGJIr-ZtFbomLCCulwN8n4hC8CunQfhoj5fhc44YrumeIqh4U99pXq6ZFUrLihfxxZ0or5lqQPsbO3GqVhC9VvdKP4FsXyny65JDC0MHWvOvOl6fQsiuL-cLNQuTMeLVzIUVL189FwDWDIw8AP1fjQlqD_jXdNr8R15r1ewXJ6DkW08hDuoOFH03p5h1X4NEM7DLVr0dQFJmV2QwhWnVhG1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=Xqp-MK1zfQYNUyGfZPTlEVFcXSiOKgyrz8YTjUPuViQUj8MjG4bxIAVTZkG-Xz0yWMiHNiNPwfbdVNvnhwfCNgUj6JYpr_teTXlB3BzVemFnrduo_C2wssD0-2mQQ0AGJIr-ZtFbomLCCulwN8n4hC8CunQfhoj5fhc44YrumeIqh4U99pXq6ZFUrLihfxxZ0or5lqQPsbO3GqVhC9VvdKP4FsXyny65JDC0MHWvOvOl6fQsiuL-cLNQuTMeLVzIUVL189FwDWDIw8AP1fjQlqD_jXdNr8R15r1ewXJ6DkW08hDuoOFH03p5h1X4NEM7DLVr0dQFJmV2QwhWnVhG1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
حاکم بحرین:
حضرت محمد (ص) پس از قرن ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگه به بحرین حمله نکنید.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/69407" target="_blank">📅 09:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69406">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYbpU7LuVvrFqyHUhpVe-iyJ5IP_FaGpk0KcHhe5Bw9Oo9Z9S57bRsz7zpJipAZMKxL4LO4osRJ8ArJwUxdNj1y74JdYBWv_KW_XJIJgwpICcoceXOw4lZu4GvWL-TpvmJ0C9X24X8dOZTCd_r09J7Yy6Oap2F3-hdEZRMCcKvTI00j2F9BCTVh7x790bFvfKKH_UTtphUiTkQIpBA_r1slhooqBnmM6HhqLFgWawOekvp5Q9C-LFVBk_Q_d3l8l1H9vYohEfiZUt0A7puE4F12vvGHTlN4mjphgQMNEC1wcnkmIsvyJADQAQ4k0IvBfaGa1I43wilV5Km9NZw9ZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حمله رو کنسل کردم
!
ایالات متحده آمریکا آماده و مجهز به سلاح است تا علیه جمهوری اسلامی ایران، در سطوحی از ترور نظامی، قدرت و صلابت که از زمان جنگ جهانی دوم دیده نشده است، اقدام کند. با وجود این، ایران و سایر کشورهای خاورمیانه از ما خواسته‌اند که هرگونه حمله‌ای را در چارچوب توافق‌نامه‌ای که مورد توافق قرار گرفته است، متوقف کنیم. این شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران می‌شود. بر اساس این درخواست، من برای منافع آینده جهان و همچنین بقای یک ایران موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانم به سرعت به توافق‌نامه‌ای دست یابم. کشور اسرائیل در این تعهد به من می‌پیوندد. همه دست به کار شوید و آن را انجام دهید. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/news_hut/69406" target="_blank">📅 06:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69405">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMpf0qdZMfELibX7EVHllyKNK5Bj71llwjhAUB7KEQ2pZ1ELT1-mUizk5p0CfCApRUkzG0TddYTYAP9B_dxIcb5GLgwliTrCBfLGsFIRR0XEShrJwUY-bfvOVIzquAzSDvAshIe8MzuLkfLDy0fX8ucvWG7gDUF587SWCmJ827MhYv6_UzSa44z81NDfL2bINpiImyTX_dehqEbazi7gEGOtzBbz2Ci1t4KU-H6yEXT9dh47moJK7A9EA6FHkR1VyjI16tECrGf_IpPBs7xAcmmVLOmS_6PGYiSQXhvvsc6UQQSIy1irKjcwo1hMvjyr6rKGky6gggxUQyY7XU1JRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیکه و ترامپ چیزی نگفته.
#hjAly‌</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/69405" target="_blank">📅 02:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69404">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=IAMn2FO4vxf2U7lkNp5IZlFUmYHNYaTlNs88Q9Hn2v-HNBegES4FWQg3pS7wmPlzQO6uxNmupuboV8johoJ-sZVb9VSbadWcHdErug-QIeLb0bqM6z3j7wrfGUSp33Pe-nEmEtLoL03wwsg3q9brs_BjZtqPYDZSw1wsXYLNHyDUWzEHb4g1CcQshS0yzXwFZuY86zgyFKkIUKsk0VZDR6et0BRoQ9umfRy1SweVVa9_fijG0uSht_4S4f34xqFMy9DHD7PEQVoA2MselbYJNWAltNztYF1QKoUd3zgAlf2h1N_IeP_AxY33OV-Iew_Rxrr6mNIFZVzu3exomVQADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=IAMn2FO4vxf2U7lkNp5IZlFUmYHNYaTlNs88Q9Hn2v-HNBegES4FWQg3pS7wmPlzQO6uxNmupuboV8johoJ-sZVb9VSbadWcHdErug-QIeLb0bqM6z3j7wrfGUSp33Pe-nEmEtLoL03wwsg3q9brs_BjZtqPYDZSw1wsXYLNHyDUWzEHb4g1CcQshS0yzXwFZuY86zgyFKkIUKsk0VZDR6et0BRoQ9umfRy1SweVVa9_fijG0uSht_4S4f34xqFMy9DHD7PEQVoA2MselbYJNWAltNztYF1QKoUd3zgAlf2h1N_IeP_AxY33OV-Iew_Rxrr6mNIFZVzu3exomVQADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان سلیمانیه
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/69404" target="_blank">📅 02:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69403">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=ORgOsSl4uIBZn9ofAwDsQQk4gd6IxcJnpgDBtrS5YkvJjuEj1XS2Z09kh9HlZW9qinCKV_cZzJMham4NyvluYgV3oFTxBaCFsnHtfiMW6MHe2o7sFi0d2hH4Aa-qmHDmmQWsHFmKLGH3VKC-1ktia33BjT0WngOTmOvNipMx6XqhPVaOhFJPtz74PLFzfHxefVH1BP2lXGC3WBdrZ7W4FCH93yLrACVTQ7GobPXaFrB_WFq95eOlfRbCqJNd6kDMc8lHq6qremSqzxBdWS7ldDiHD0CZ66mVCJDlJjJ6Ob6qkwDeKPEVpwIUUpytr7KuYiKOFmpnY7nFbYCZfju55g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=ORgOsSl4uIBZn9ofAwDsQQk4gd6IxcJnpgDBtrS5YkvJjuEj1XS2Z09kh9HlZW9qinCKV_cZzJMham4NyvluYgV3oFTxBaCFsnHtfiMW6MHe2o7sFi0d2hH4Aa-qmHDmmQWsHFmKLGH3VKC-1ktia33BjT0WngOTmOvNipMx6XqhPVaOhFJPtz74PLFzfHxefVH1BP2lXGC3WBdrZ7W4FCH93yLrACVTQ7GobPXaFrB_WFq95eOlfRbCqJNd6kDMc8lHq6qremSqzxBdWS7ldDiHD0CZ66mVCJDlJjJ6Ob6qkwDeKPEVpwIUUpytr7KuYiKOFmpnY7nFbYCZfju55g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات سپاه به‌ سلیمانیه عراق
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/69403" target="_blank">📅 02:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69399">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NK78fUs7cNzll8pkQco4obJXU8iCXmZ0fjd2tPKnC_mlyl8f3Ch4nNiPjqLBzbGl_3M_oETajG--rV0aSR5qb4m4EBdrjegvit1UwNhvL_KhaEtC5krUQIfdiKeiW5ndfsr5S_DUTt8Vc2-0p_UamJVvA5G4Pd9JPrg42uDHKemhB1FdFonLTUfzQOIIq-qdljA2W8RR1BH1cg5WkMAR08aC4TItQhduSpX31tXhzoooYu02_BrGtn-SYyEd2vAz_hFF4Cc8l1t54OjdngzG7fDy3ogGwr3pOhPXTiHu8UwEMUEoBHmB-qRgWFecJInGBZ4uHEQ03kjCH94N0oaN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZW-dInFGgVGOg4mPm-UaB-HMp8Bd5NT6rJsxAmebsU1FpEsfUUx3aybyoLKzS0P8yx0okXJ59TOyQNjv0S_S7yI9lK3geD2jqspsAoMrSIFYMsHKx2kHyRudslTj4MZyHlHuoW4a3Jn2iRjP2MGtNWEj19ndsFaivIQexZwnRIT2YwcSXQZAkvteIP-cY-pq-EzHyChb5-4kZhAvUuIF9cLVXKrZlqYiidQRfvfXZ5nlTXv-j2lSzg8v4QDPiNEbrCckzveXMnGdfWhpE6D_yEWhC22YxNjPBMcdot-kFWmb87I5NoG_Pr5Dpvd6c_TXqk5sutEicCVIcENun3Ar3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=b0AyiA2YqcSKloQfum6Vw7ZC_BjOwZ-zr03aO_Uc6ZQ5zugIrPUPNbioy8Fy5sutA76KTCJmDE7x0qfzVw5n2RY1O_ibXFJPVGSnt2HtIKUak64W-uEBy4paO2CZyyi30zPU0ps3h3WNHVoYwxomAiL6b_u-BAfEmSM2Bwj5Vq2ndNd8jEmM_-yXpyEIPGvNb7E6oAF2U-coZZFwfbyzNkFNOpfx9PMxBy70h9HDLtpUaoEzVrNCDNfu7sq8MwRZ47N3GDxxIGP3SkWrMSQHPrIpNhkSlWC4ewmqaqrZ2Vxc-ADzQofAz0J02x7_WpuxfSoyq7CriDcfSw22Sa-Ltg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=b0AyiA2YqcSKloQfum6Vw7ZC_BjOwZ-zr03aO_Uc6ZQ5zugIrPUPNbioy8Fy5sutA76KTCJmDE7x0qfzVw5n2RY1O_ibXFJPVGSnt2HtIKUak64W-uEBy4paO2CZyyi30zPU0ps3h3WNHVoYwxomAiL6b_u-BAfEmSM2Bwj5Vq2ndNd8jEmM_-yXpyEIPGvNb7E6oAF2U-coZZFwfbyzNkFNOpfx9PMxBy70h9HDLtpUaoEzVrNCDNfu7sq8MwRZ47N3GDxxIGP3SkWrMSQHPrIpNhkSlWC4ewmqaqrZ2Vxc-ADzQofAz0J02x7_WpuxfSoyq7CriDcfSw22Sa-Ltg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇷🇺
ساعاتی پیش یه انفجار تو یه رستوران تو مرکز مسکو رخ داد؛
جایی که به گفته منابع روسی، مراسم عروسی خصوصی با حضور چند نفر از فرماندهان ارشد نظامی در حال برگزاری بود.
کانال‌های تلگرامی روسیه می‌گن "الکساندر چایکو"، فرمانده نیروی هوافضای روسیه هم بین مهمون‌ها بوده.
گزارش‌های اولیه حاکی از کشته شدن دست‌کم 3 نفر و زخمی شدن بیش از 20 نفره!
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/69399" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69398">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⏺
المیادین:
بر اساس اطلاعات بدست آمده، گروه‌های کرد حاضر در خاک عراق در حال آمادگی و برنامه‌ریزی برای اجرای عملیات علیه جمهوری اسلامی ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/69398" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69397">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/69397" target="_blank">📅 01:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69396">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=vstQXglx-Uh_rMqPPIyXZ4VOtD0Ctl0MeYHq36UJ7UTeycpg98DT-Mjhue8iKuD_N4-woLfohcta144REmAss6wmbuMC0n25bIqe_yb1xSwk2hKFX8z-Xf2Dj7-lkKUhFHNJ9W0KXIXkgCIaD818g66MG_Lc_COQMeHIF8yfY36ZXOtVl42NKze9GrnZPIdpetW2NmuKLw_hda1nzJYJVDdeznrd5z43XwwDvA5CuM4Q499NJ1kpKJPGwUFHyPeWo2VkDR41fRPIfxxFNxKNY63EoCDpl6M6RcCrwnZIuX4X-cEZVIrRp8U8f2vOzCiOhMY0Tq4e635Q8ASzTWksDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=vstQXglx-Uh_rMqPPIyXZ4VOtD0Ctl0MeYHq36UJ7UTeycpg98DT-Mjhue8iKuD_N4-woLfohcta144REmAss6wmbuMC0n25bIqe_yb1xSwk2hKFX8z-Xf2Dj7-lkKUhFHNJ9W0KXIXkgCIaD818g66MG_Lc_COQMeHIF8yfY36ZXOtVl42NKze9GrnZPIdpetW2NmuKLw_hda1nzJYJVDdeznrd5z43XwwDvA5CuM4Q499NJ1kpKJPGwUFHyPeWo2VkDR41fRPIfxxFNxKNY63EoCDpl6M6RcCrwnZIuX4X-cEZVIrRp8U8f2vOzCiOhMY0Tq4e635Q8ASzTWksDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/69396" target="_blank">📅 01:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69395">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQVAr2fuJtTzjX4coX-rRYVdUA6BQD-odBcvF-E9miHduMHDjSgBoZcCwReVSIUrDiEvoRnle52oD83xdejuRrLCNH-Jgp2tvF5by3oj_wHAJ7OtJ8TQeSGrvTukj3ccCMeBrKSK790iZqmWL8L9EBThpRwQAVz8WZ5t6yFpQ6URXhNsvtnFZHI_UaYUhWa1PfJtMymrw6Ve4mZw13a96QjIk4_NsgHMGrrw_tFLXmAcFoxBtxEiRxFVHfBwSJsgu0EttgjMvEWdrHzqFgzH-AYa8KMgtjT0tF88yTJn794n-U7UohuJwVaEciqFOxcRdkQ-ZWrS-dcbwRwTOZBqmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
توییت اتاق جنگ اسرائیل و اون ساعت شنی معروفش
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/69395" target="_blank">📅 00:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69394">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=vlekYDCGPnPcO3P9xX1czBFoRj0Bk9WN0k56siWq4dfRgn2BzsuwZNZ0YstVCEXYGT3B5NSNIamaNgFRsQp6rI7JM8vTirAcT6XPwnLiG7ZKty6VKjhbkTW9j9RwWhCvY_VA7aZzM38YmFaV3_39Ufg0FyGSVRFhG38SIgPTMCU-4pRlxlREKR6aVjx751eKAJ1pPH1vFW6gJny0ZpWi654z2tWLviD24vsHEV0wfrW2mv91jdyrYai8NHzNa76KaHDh41ATCwWMhXRjH2O1PZ2EEmi2Y8z89tUQO-ktjrhbrGwAOb0kmBTKqgURD49oHxmJ5b9OUJyvulZR63GYqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=vlekYDCGPnPcO3P9xX1czBFoRj0Bk9WN0k56siWq4dfRgn2BzsuwZNZ0YstVCEXYGT3B5NSNIamaNgFRsQp6rI7JM8vTirAcT6XPwnLiG7ZKty6VKjhbkTW9j9RwWhCvY_VA7aZzM38YmFaV3_39Ufg0FyGSVRFhG38SIgPTMCU-4pRlxlREKR6aVjx751eKAJ1pPH1vFW6gJny0ZpWi654z2tWLviD24vsHEV0wfrW2mv91jdyrYai8NHzNa76KaHDh41ATCwWMhXRjH2O1PZ2EEmi2Y8z89tUQO-ktjrhbrGwAOb0kmBTKqgURD49oHxmJ5b9OUJyvulZR63GYqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمود احمدی‌نژاد درباره دستگاه سرکوب جمهوری اسلامی:
نیروهای امنیتی خود افرادی را به میان معترضان می‌فرستند تا با ایجاد تلفات و آسیب به اماکن عمومی، بهانه‌ای برای سرکوب خونین فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/news_hut/69394" target="_blank">📅 23:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69392">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/magwDLtRjJkQdgAqRF3Y8d3BHigsSwpqA7m_ByLDtrcrLRn7tSBJmGqkqu-mkPfAdwb3Xg3K13nZnfYBPBA3uaPp9cy4bdc8Nb5uVk12D2mT7M1g5WScGc3XpWOnPQPNuek5378FAr5tnu3wU6yiV4Gr-2FPxWILlgb-nHc0ijvsi8-PHP7bICKFSadWNBuK1bMHr8A2Bmwkd4uu2YncHW5cmnBB-lOHCdsHMMbagzzmJ1cMue4BGIEyhiT0YBLSA6Nq4GDUfskmB42GntiUTOaCV10dBe-1zgLrBl1GsgN2f7kSPsZdPN9p0zMQXJWN7bWKV0tvQWSwE_pu94UqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=vegZlZI__WnQrOOk7gGs3BaQ8db3p11fqLluulT_cC96mGAGKYtX8y5AAL8FVW_NeJaxAjj15LkXSF4k0gp3WJA1TZtbRaD7N7nB8rAt_HaV_enR9_uOt_FsqpdNh3bSuCj6OxOMJt01Uj79zbF1CKO80njcjdzQ-LSzFKnATm_f9qBeDrrFalE7vHXMx8fngNaWjIYJeKXP4O3AkdSgLMlxl7MiX8V5zCWo-SprWm-ODFqjwi5jykXH1cOFizTb6c8LrmVsPia_qYlQOWzdACW2uewrqBENTGefKmG_is513tZG_XzULdw9MOFx1LURsn-b0KmbFXSEV6osAUan9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=vegZlZI__WnQrOOk7gGs3BaQ8db3p11fqLluulT_cC96mGAGKYtX8y5AAL8FVW_NeJaxAjj15LkXSF4k0gp3WJA1TZtbRaD7N7nB8rAt_HaV_enR9_uOt_FsqpdNh3bSuCj6OxOMJt01Uj79zbF1CKO80njcjdzQ-LSzFKnATm_f9qBeDrrFalE7vHXMx8fngNaWjIYJeKXP4O3AkdSgLMlxl7MiX8V5zCWo-SprWm-ODFqjwi5jykXH1cOFizTb6c8LrmVsPia_qYlQOWzdACW2uewrqBENTGefKmG_is513tZG_XzULdw9MOFx1LURsn-b0KmbFXSEV6osAUan9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا کاظمیان از حامیان جمهوری اسلامی در انگلیس که کارش زیرآب زنی مخالفین رژیم بود، دستگیر شد.
حالا فیلم لحظه بازداشتش رو ببینید که پلیس اومده بازداشتش کنه، میگه تروخدا بذارین زنگ بزنم پلیس
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/69392" target="_blank">📅 23:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69391">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=RUYbP9xQvRM2VPCUn2xK5jUYS9kNOfvRBcZHwM1eVgA-o47Izm2H08uA1H0VFaSlsg_ejfzI9dPjxtN99zW-dbB1BlvN399P0oaXZ_atxJbF3EsWFuc2LwQD3TnkcM0t3HHYh1MzBlLMs8Ukup3vm8oQR5zQJNshleCW33Vlw8hQJw-QYemtuDckpUUYceEPUt-EVBSH2VEVf3IH6U_McOBm7pd6Q91lAwEpNSWJeGE0LduWSUI1xkBQPfrfveynxoPfwq1T0ZkeCADEcoJFVvJW9Q9TodBrA_F2RVQry_N-RTfD2Lr6GHQfSESHYAQvJDbHI1OyiMOTSuzSnwChdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=RUYbP9xQvRM2VPCUn2xK5jUYS9kNOfvRBcZHwM1eVgA-o47Izm2H08uA1H0VFaSlsg_ejfzI9dPjxtN99zW-dbB1BlvN399P0oaXZ_atxJbF3EsWFuc2LwQD3TnkcM0t3HHYh1MzBlLMs8Ukup3vm8oQR5zQJNshleCW33Vlw8hQJw-QYemtuDckpUUYceEPUt-EVBSH2VEVf3IH6U_McOBm7pd6Q91lAwEpNSWJeGE0LduWSUI1xkBQPfrfveynxoPfwq1T0ZkeCADEcoJFVvJW9Q9TodBrA_F2RVQry_N-RTfD2Lr6GHQfSESHYAQvJDbHI1OyiMOTSuzSnwChdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کانال 13 اسرائیل:ترامپ تصمیم خودشو برای حمله گرفته؛
میانجی‌ها که آدم‌های خیلی خوشبینی‌ان و همیشه میگن راه مذاکره بازه، حتی اونا هم میگن حمله‌ی آمریکا از هر وقت دیگه‌ای نزدیکتره.
آمریکا هم از طریق سفارت خونه‌هاش به مردمش تو خاورمیانه هشدارهایی داده که اینم یه نشونه بزرگه برای حمله مگه اینکه ایران همه رو سوپرایز کنه و برگرده به مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/69391" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69390">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⏺
🇮🇷
نیروی هوایی جمهوری اسلامی هم از دیروز تا الان مشغول آماده‌سازی خودشه تا در صورت نیاز، بعضی از اهداف تو خاورمیانه رو هدف قرار بده:
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/69390" target="_blank">📅 22:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2RqPhSkZBesxuJtZTNAHB3MczejiF2ModGBCrOC36V9eZOeP_5kXGpJratXaJrj6UXDG4IDrIxxLaqIMJXwmRwqKvgWk0m2bkSyN5nPXyhpMtFAzwWqtslYtiow1CclgPiA6jf2KKI2bWC4D322iXuACffHJ1v1Gow8dIWPf73qDPR73xGGJHcYW5vGukGRZn7UKs61HEB6nZ8Pqlk0f6mZYMN7RukQ5XIHMgi5crcHFj7trNCyuWK8ydOdl1tJKrxiNqwJsaDvg0YMuQTxrwnk6avzq2GsDCg7LlM7_Rpftp3CXO6QS-ptdZ7jzU-ho3Kiu7I732rNUse5CyKcfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/69389" target="_blank">📅 21:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S31mTaPi_PJDrR1ue7xpXUhQk4l6tFn6bJriskGXldSlfI1pBNIfEuZepnzhJDkB7w0ah4bWHKvhzov6KsO64g1yRDdfd_joWjJjS978yLUUsdhLRqmE1cHpLRiwo5p4jTgYHerwgQn7HSroQTf4LSZ2JqOEgthHc51yabcuMqyInbitJl-jef3okv1eus1ZiGhTPYwsiA1GUQ7328JNDO4zI2uHPlFbvQ7Qbo6T9apHBhu6qKJCoPjXzge5Eh2n4kEKx0Lt3BrFaFGc40xTQLiaPq9B0x4t-NeV25t8RpShgwdEgPLHkrsdZ42q2QVoYs03SJ1XKw59dWrfbumWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/69388" target="_blank">📅 21:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69384">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0r0wYug0I9Qpu9oBxw2jyAUz6bgoMd8ZYOeDWfh1Mz9PBh742lPsgqZVjK2pUNyqp5PvtKd9aiEVmFek9UoNz3IYNH133asKtHfjotWm8frGAJeWbXjm_U35mj58vGRZmn-tMoT00bddM-PMgy80VmCNMG9XKzn7RLzmhgrppdIahu1hxW-pChBkr3yIuYcs1WWM9SGFusjwVpAL-2v1E52EK1_QfCG_SYKavGG737sTwsq92AR8rREfs89j0lx4QDYCngjBv95wJGN99djzyG0ivePNMafZyyN9w790Q31-3kMYhhWTPZv9B7To01yIoMtTWG6GekNlv9EdYjJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DScUMX8-X-OWIU1ag38r8sHVioNpReXzexatAzjLwQTj-BsW8VVUevj-0-_VVXn32Hcn6I6dnZA7gv37h9BmjCaadFO3K5E6mDyJvHY_6qyUUsXbJk6n8NTF8I_8bqv2r55k9eeS3DQsHoPJWNqzM0YDTBLXdV_uZd39LE59dOXE9nK4th8zG87OyIclCXrzWGI4RKK4UG6WXMMItfDmCluX7Kt4xpnz4Zfg7JQWaABk8TBHgjY1ORz8860uOFk8u67SKY9KD1CZlPfBrB51GEK1QbC4jUOr9jrFQlbXAW7GGfSi6iHCcgRB795myrBCIn3ZDhTZHMVOm3v85uodHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BR4KnMvT-v49gbtzgt1IrygfujoXpk5PYbGjBii7lhjdd8vn8tv8VmGmY_tSjTYMy_6EOXD6dfKisd7SIugDd7P0OkINptnNorZvQwfvKDNE_oYGfFQZY4wwxm0CeG47vwIkpxLdg1pcisBDscCD6H0QLQ5xcYR0RhxUcs8CFKyFCkHjNb3IE0bsk5svDtGnIF9IUkWXyEhUMabN7-Y5bgXv_G1x3nhXo_S1QZBq8a6SCRKT-PqOff5RoOXYmkQRgYNB1w6BQ-FgU3PSftq4814QUM4F8SMTn8Q_PwOZ9JDjIEgcYy12SLCZQ7O_dJmxZ9UDhmM8xMP6evxUFbwZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iKaotTL2Z0ZgzjEC4Ap_MUrTPoMYjFMzjAB9GiqaWgfVA4osjE32KkKraJJpV2zQ35ACif97S5Xmve_H56YtRdamGo4tzFFqw5u1mgAkwrY0Lk0hOfvz-wlFsq95gfHT47u3BkGhybQnDKZ9PQbuhCoT-VvFudElU5q-giVGpwxJSsy_a29OE41GAuSFrPhqs2wrnVRZkcUvNuXId_6oGHl01MegGdWq_bm0ZqpvxLzk6lQvvAAWjjkDWud9x7D1Zvr5ARbPzvueFwR4uJbFfGHt7wYZjiGbD0AbYWNekCxfOdLx02AElWF_2k2gfSxeA24QCorNyWqkKSye_B8PhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
پست های جدید ترامپ
از تصاحب گرینلند تا جنگنده و انهدام ۱۵۹ شناور جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/69384" target="_blank">📅 21:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69383">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yi3a-jS7GabYqmqoPTXdRLzTicpjPI9hcayT7eZh9qByDXg-Q51iD9uOjI8ZyeiVMfFChP5GPQ2AwBBq9OYBYZNOGSNE16YGIzWgm-jEeruC8lBKpWfcnCYPtllIVEDNavA13Yz0aX3O8Ts_nbxoYXNBPT5jZGSgAa5nD785hOFp627RglUtGQNsfKMPqXhSnlT1jlpFhCSw5WRMH3Rz3J9D49mobgKwrDs5mRW1SEDf9haSsHg550dorWehou2RBHpz_f6h188yMbR8dpewFGd5D6zniEbFVL_-lMVsA7HyXfSLd8FHjl8QITNNiDp9ihaeiUdjMkmXNnW9Xi8v_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/69383" target="_blank">📅 21:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69382">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KT3RXILDUTM0oegWt5cERDSA6byI1z8k6qGLZgYbwgV3ncSsMBnS0k8EybUKJktGtD-lTOjcDubv3zDr1l-mQgaGSjSCcY9jhYn_WnfLp-OWt_jkQXT6FbzHRHvHJ5AuW50ifbE9c83rf2hMRdVKxeCZaAyn9Sfrj_-KsnuEMk1t7eCmVbk23DkVWCbKAOuFVE9DYRfD9hKdMqKVN6H-GBG7EiiUl6RVc5YagxRRFoM2gLiFUdv6wIWzzJKJWXEzhdSAnPkHfLJJbSSK1jYYUS0Di43YaVHsRIrPCt5hHS1f7QqRSF10sCkZy4M45xuNjjQnpdTvOozbgoTWRnm2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
بر اساس اظهارات رژیم ترامپ، کاملاً محتمل به نظر می‌رسد که پس از ماه‌ها تهدیدهای وحشیانه، امشب آخرین شبِ وضعیت عادی در قطر، عربستان سعودی، کویت، بحرین، امارات و احتمالاً عمان باشد.
اگر حملاتی علیه زیرساخت‌های غیرنظامی ایران صورت گیرد، زیرساخت‌های حیاتی این رژیم‌های همدست — به همراه زیرساخت‌های رژیم صهیونیستی و شاید اردن — ویران خواهد شد.
مردم ساکن در قلمرو این رژیم‌ها باید فوراً برای تخلیه آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69382" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69381">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل:
این کشور در بالاترین سطح آماده‌باش قرار گرفته و مقامات ارشد سیاسی و امنیتی در طول تعطیلات آخر هفته مشغول رایزنی بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69381" target="_blank">📅 20:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69380">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcE5cssq_VLWURV2gjWCzeeusZHPFy8S-rXnfSvaLM3TKkC4BaGftGREMfQguld8jEuv6sb2az0XsSEGQY5gBiRY3L6k9SyJHcfO4cF5bqctsJh95RMnRm8aRSZRPCpVpsVB_lEqpYgEDX-NCR08hV9omFI0aJX4mW3STlMxlhDlgNwwoVDxwnDgYLPvG_21xvVLoDLzTGi0ZmX-7T1MESNHXL3xiUjLkGpLJCzb_GESxwvsj99XrcFDAMqFTPgg8AwT8ZOVvCBH15psgYWhd-i0RVyTm8AUqr0NeswX_KmeONs3_0XPqtVct2JEBveAALqWr6DoJj08X1J6W-Ihqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
کانال 12 اسرائیل:یک مقام اسرائیلی؛
«تنش‌ها به بالاترین حد خود رسیده است؛ ترامپ بیش از هر زمان دیگری به انجام حمله‌ای بزرگ علیه ایران نزدیک است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/69380" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69378">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799177ea92.mp4?token=VKThWmuUof8uhPlWxY2Y0l3FLbjyqLJuPOlL9OLfgFn-hRyK720lWCF6YyB1O1o7CzSQpCdBNlqJWqwsLk_ZLaxcMNrwnwPTagMD5DmYYukElf2nfXL2jA5y2Q9n1h_Dt82SoWe3etKyGRhlVpF_XX4W15uubnYOSeD2_90iEXvIX0jYfMO3GK-WnmixRXxktmPm08S7Zu18B8jMNI15g7TRd6sBAy_VZGofqjslc-8eTHmy1D44tVuAegmHkMADP2FOJQafR7-n4d_gCqiyBeY-t8qsTqbB3MKQagEizpe1fspS9I-au-pWohwuBfxpfQN2BXOci9epa6fnHLZl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799177ea92.mp4?token=VKThWmuUof8uhPlWxY2Y0l3FLbjyqLJuPOlL9OLfgFn-hRyK720lWCF6YyB1O1o7CzSQpCdBNlqJWqwsLk_ZLaxcMNrwnwPTagMD5DmYYukElf2nfXL2jA5y2Q9n1h_Dt82SoWe3etKyGRhlVpF_XX4W15uubnYOSeD2_90iEXvIX0jYfMO3GK-WnmixRXxktmPm08S7Zu18B8jMNI15g7TRd6sBAy_VZGofqjslc-8eTHmy1D44tVuAegmHkMADP2FOJQafR7-n4d_gCqiyBeY-t8qsTqbB3MKQagEizpe1fspS9I-au-pWohwuBfxpfQN2BXOci9epa6fnHLZl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تخلیه پایگاه های هوایی آمریکا در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/69378" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69377">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483837b794.mp4?token=n-Wd9ifLfirVZYw9AHiz2ObJKj_zFkAZUvY0TVebEmykwIS4mv8t1VJf_iLWPur-iFL9PBZV8j_CZeWZBEHrMKLHS3f0Dy8Gtqy1FYd-nrSRejwD8b5FtcCW6eEpeCRMvxANmCpmRzrgPEcFgqzeX-XMc04UiF8JnRbMZ_qFnQGQUEVmRAd2PAamFX7mbPZMxpEPfxgIaZRSuQeN8YoF_EJLl0jrSy4lqCE8gXAnF-02ypjQlpWEk04fObK9r6FxGEQPnKcUcsthlHAcGQlbptU7X9tNM3lUFbvSBcpN6_5V024TIN8AAEb6FtOvWvrZtG71b3lfR1zSJsOjAOrbmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483837b794.mp4?token=n-Wd9ifLfirVZYw9AHiz2ObJKj_zFkAZUvY0TVebEmykwIS4mv8t1VJf_iLWPur-iFL9PBZV8j_CZeWZBEHrMKLHS3f0Dy8Gtqy1FYd-nrSRejwD8b5FtcCW6eEpeCRMvxANmCpmRzrgPEcFgqzeX-XMc04UiF8JnRbMZ_qFnQGQUEVmRAd2PAamFX7mbPZMxpEPfxgIaZRSuQeN8YoF_EJLl0jrSy4lqCE8gXAnF-02ypjQlpWEk04fObK9r6FxGEQPnKcUcsthlHAcGQlbptU7X9tNM3lUFbvSBcpN6_5V024TIN8AAEb6FtOvWvrZtG71b3lfR1zSJsOjAOrbmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاخ سفید:خداوند سربازان مارا حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69377" target="_blank">📅 19:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69376">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746862829.mp4?token=Fe37d2wUFMubecWXVAY03CG_UsJ-C2daaQA_OVfFL_brt5y68ccPbADrj627BNE_0UbgI-BvJmalQUmQZXv6fmUPDxd9pHC1YV9XgL_xqvZP6_OLqqv8LDNRipuRrclTGMdFH1Up7CPNCfyU4PDZEh87k8GM_L6asYBmIIPp3-glS6HaL4HRebsTHuXXO9K0I2UeEtS5lkJKpx6hUZSf6erF6BB3eD8nmkr6YXoLCxSqBgY1ke6qn6MmgRLmayoGHu6LWWoxcRhpmlbhlq2zbeEyAsAlPKieFGmp-HK1QTC7Kyus3VG_xMVbluaCxGXBcp0cXHaaKe8OHLbaNNpJHUOxiOAcXQqqYUJjbgaHFzCi77kIbQuwDNOsR9IEPzLHhJ9DHZS7wXfzIzgeVIdaLcgryMi5JByuYtrG2EIVTGZCfZOWefaZKHt8HnEbEIKV5mZ0v6mNjlpoDRBc7rN9pn54QpWUUsiRR9mHMf9xYCtzG-v0XTGXKOvEJFEh8Mejp6iwrPgUUvyvKlzI2CABlzUH9FGq3DqCY39aX3BuRIFy8KsTzmY7u157Bzvz_DsHT4wq8dT-iA8oMukqmIcjAxxuqHEI7vwKTPmZH6RuzthHqcyPH460ZNXRHW5B4Cibw9_eEo2nrziqWsCNklgEjO93EP30O6gF8pi60Ic8nyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746862829.mp4?token=Fe37d2wUFMubecWXVAY03CG_UsJ-C2daaQA_OVfFL_brt5y68ccPbADrj627BNE_0UbgI-BvJmalQUmQZXv6fmUPDxd9pHC1YV9XgL_xqvZP6_OLqqv8LDNRipuRrclTGMdFH1Up7CPNCfyU4PDZEh87k8GM_L6asYBmIIPp3-glS6HaL4HRebsTHuXXO9K0I2UeEtS5lkJKpx6hUZSf6erF6BB3eD8nmkr6YXoLCxSqBgY1ke6qn6MmgRLmayoGHu6LWWoxcRhpmlbhlq2zbeEyAsAlPKieFGmp-HK1QTC7Kyus3VG_xMVbluaCxGXBcp0cXHaaKe8OHLbaNNpJHUOxiOAcXQqqYUJjbgaHFzCi77kIbQuwDNOsR9IEPzLHhJ9DHZS7wXfzIzgeVIdaLcgryMi5JByuYtrG2EIVTGZCfZOWefaZKHt8HnEbEIKV5mZ0v6mNjlpoDRBc7rN9pn54QpWUUsiRR9mHMf9xYCtzG-v0XTGXKOvEJFEh8Mejp6iwrPgUUvyvKlzI2CABlzUH9FGq3DqCY39aX3BuRIFy8KsTzmY7u157Bzvz_DsHT4wq8dT-iA8oMukqmIcjAxxuqHEI7vwKTPmZH6RuzthHqcyPH460ZNXRHW5B4Cibw9_eEo2nrziqWsCNklgEjO93EP30O6gF8pi60Ic8nyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیستون؛
جایی که سنگ،
به زبان تاریخ سخن می‌گوید.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/69376" target="_blank">📅 19:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69375">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=vuZXoRWUZkyff0kynx15SFojvIKJkoJrFVM1lMwn7RBrqp15makTY4ilxXMZTnYpw7fHTGl-a3isTiFTZJFaqQjniIqRuoq6IW-scupMu3x8VPKDrXsuMO4ODtrV5zrhdznjhC_0XaEBnS7YussS8A2LtOiLRAsza6j1McmM5vP1tM19mKtUXdOGILRp9BzKPWmYkM8Lbkl3sa5hKex2B-h4cX_UqTFdgyZEkXFQFyCZTznuF7mTB4a4oFo3eVnDzeh0qqI9PH6IrvJQxGoMOSW4IyHFqGf9ioKkcjs2dk3LkySopXs-9Wk1n9e3zUAnWrDtYTl5Snvk6p-6BjPB9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=vuZXoRWUZkyff0kynx15SFojvIKJkoJrFVM1lMwn7RBrqp15makTY4ilxXMZTnYpw7fHTGl-a3isTiFTZJFaqQjniIqRuoq6IW-scupMu3x8VPKDrXsuMO4ODtrV5zrhdznjhC_0XaEBnS7YussS8A2LtOiLRAsza6j1McmM5vP1tM19mKtUXdOGILRp9BzKPWmYkM8Lbkl3sa5hKex2B-h4cX_UqTFdgyZEkXFQFyCZTznuF7mTB4a4oFo3eVnDzeh0qqI9PH6IrvJQxGoMOSW4IyHFqGf9ioKkcjs2dk3LkySopXs-9Wk1n9e3zUAnWrDtYTl5Snvk6p-6BjPB9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
دونالد ترامپ، رئیس‌جمهور آمریکا، و ولادیمیر پوتین، رئیس‌جمهور روسیه، در قالب «زوج در حال بوسه» در رژه کانال‌های آمستردام:
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69375" target="_blank">📅 18:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69374">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=IgzvcMb3PBhDp9c1J7JsertzZDmX0ymeI6g8RZDpPW1N-mRGr8iRA2wvTLZwft7qnKF3PIOpvoHAkZWWSDw9mud7U-xEHjQ-0duf3imVvqIElpe90jL-RePCMR8po314Ez1-cFijKTdFn1nDUZv4KnK9kJVyTiCo79g1_cwcKthQ0xqAS9Jcsp4Hk2b6qXYsptL99R_soOoM1z0CJX2y4GuoW-kY2oqMSJOptmqeP2gQPDG8RuY7f7EfaH3u6pMpITFRVzHgqSbPycbFJIGixcIgllVrQery6LqGjzimJVIf_4p3thtoeEwnZfwbSkRpDJiyYrSlhgDKW_HtX70Rag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=IgzvcMb3PBhDp9c1J7JsertzZDmX0ymeI6g8RZDpPW1N-mRGr8iRA2wvTLZwft7qnKF3PIOpvoHAkZWWSDw9mud7U-xEHjQ-0duf3imVvqIElpe90jL-RePCMR8po314Ez1-cFijKTdFn1nDUZv4KnK9kJVyTiCo79g1_cwcKthQ0xqAS9Jcsp4Hk2b6qXYsptL99R_soOoM1z0CJX2y4GuoW-kY2oqMSJOptmqeP2gQPDG8RuY7f7EfaH3u6pMpITFRVzHgqSbPycbFJIGixcIgllVrQery6LqGjzimJVIf_4p3thtoeEwnZfwbSkRpDJiyYrSlhgDKW_HtX70Rag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
فاکس نیوز:
رئیس‌جمهور ترامپ در حال تشدید فشارها بر ایران است و می‌گوید در صورتی که مذاکرات دیپلماتیک به نتیجه نرسد، انجام حملات نظامی جدید همچنان یکی از گزینه‌های روی میز است.
ترامپ پس از دیدار با اعضای کابینه خود در «کمپ دیوید» اظهار داشت که توان نظامی ایران به‌طور قابل‌توجهی تضعیف شده، اما این کشور همچنان از برخی قابلیت‌های موشکی برخوردار است.
مقامات آمریکایی می‌گویند این حملات ممکن است حتی در همین آخر هفته انجام شود؛ در مقابل، ایران اعلام کرده است که در صورت هدف قرار گرفتن زیرساخت‌های حیاتی‌اش توسط آمریکا یا اسرائیل، آماده پاسخگویی است.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/69374" target="_blank">📅 18:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69373">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=oc2-pcr624zbq6sUhXLF6OMJmNs5gCWtG6dIZAIc9LUMALO951-dwzjSIK9rTI1UOZttXbqlEVxlOBHSExI2mqn48yWVqCs694bVqS3QkHIAZABWiQuRhnSW8azVjwbg39VfTxtYms_rHa2QcTXrbl0HM3_nPFdZwbrnAOdbPesSJG3NCEDTYdEm-E82Qv74LrNta51N-lzTpJLPUaIaNZiumz6Q9tOGZOl6RnyjOePbcbhPrZeXE13stdtzU_DQE1FAHizLYDTmZFhG4GEpzUWtTfXD4rEAEvcbexlSHjpRrOpdQSnZsFiZa8PZ_uyx-bUiOoCbJm1PyDJl8IIMJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=oc2-pcr624zbq6sUhXLF6OMJmNs5gCWtG6dIZAIc9LUMALO951-dwzjSIK9rTI1UOZttXbqlEVxlOBHSExI2mqn48yWVqCs694bVqS3QkHIAZABWiQuRhnSW8azVjwbg39VfTxtYms_rHa2QcTXrbl0HM3_nPFdZwbrnAOdbPesSJG3NCEDTYdEm-E82Qv74LrNta51N-lzTpJLPUaIaNZiumz6Q9tOGZOl6RnyjOePbcbhPrZeXE13stdtzU_DQE1FAHizLYDTmZFhG4GEpzUWtTfXD4rEAEvcbexlSHjpRrOpdQSnZsFiZa8PZ_uyx-bUiOoCbJm1PyDJl8IIMJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک هواپیمای سبک قاچاقچیان کلمبیایی در حال فرار از رهگیری توسط جت جنگنده ونزوئلایی.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69373" target="_blank">📅 18:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69372">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=PGd1t_8GWnfX8nTaVwXP6YhRvPJ4byhQ3LSHT57UsRL20eEAe34X7_kBNoUyxFAj3876tUQchEwYvwdJPSZqKGaPIEyIWmxEfc_z1vYHFZtG6256OmjT7M_deWdaZ4B7yoNgALipaxnzanWBJlbWmpx0LF5OM0ck1MwaIk0-B_tca36vjsro_JJPXI-oJxqq_nHlxnLplkuhOZ4k7Z5dblvCXimCvUWtska1ZGUzMfV_yneAr7Qhp7Fa0L3LuszSJ5pbu0f3CxHSwLnXoi6ZFFVZ2rdqw6754OkSazcW9DPcuoYq16EO6eQa0hJGzdD5PrGOCVKeNqGxuPUD3QyBJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=PGd1t_8GWnfX8nTaVwXP6YhRvPJ4byhQ3LSHT57UsRL20eEAe34X7_kBNoUyxFAj3876tUQchEwYvwdJPSZqKGaPIEyIWmxEfc_z1vYHFZtG6256OmjT7M_deWdaZ4B7yoNgALipaxnzanWBJlbWmpx0LF5OM0ck1MwaIk0-B_tca36vjsro_JJPXI-oJxqq_nHlxnLplkuhOZ4k7Z5dblvCXimCvUWtska1ZGUzMfV_yneAr7Qhp7Fa0L3LuszSJ5pbu0f3CxHSwLnXoi6ZFFVZ2rdqw6754OkSazcW9DPcuoYq16EO6eQa0hJGzdD5PrGOCVKeNqGxuPUD3QyBJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح تو یکی از حوزه‌های امتحانات نهاییِ اردبيل، 9 تا از بچه‌ها مونده بودن پشت در و داشتن گریه می‌کردن؛
طبق ادعای خودِ دانش‌آموزا، مسئول حوزه ساعت 07:03 در ورودی رو بسته!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69372" target="_blank">📅 17:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69371">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
ویدیو وایرال شده از این هموطنمون که در زمان شاه حضور داشته :
زمان شاه به دانشجو هایی که میومدن اینجا درس بخونن ماهی 400 دلار حقوق میداد
اون زمان صدتا نارنگی یک دلار بود
یه اپارتمان سه خوابه تو نیویورک میگرفتیم با سه تا توالت و حمام اجاره اش 210 دلار بود ما ماهی 400 دلار اونوقت حقوق میگرفتیم از شاه
شورلت کامارو یکی از ماشین های اسطوره ای امریکا بود سه هزار و صد دلار
با یک سال تونستم ماشینو بخورم
امریکایی ها میگفتن کجایی هستی میگفتم ایرانی همشون میگفتن شاه شاه شاه
کدوم شاه شما دیدید بیاد تو امریکا براش با کلی عزت مراسم بگیرن که برای شاه ما گرفتن
چه افتخار و عزتی و لوکی بود شاه واقعا نوع بیانش و لباس پوشیدنش هرچیزی نگاه میکردی لذت میبردی
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/69371" target="_blank">📅 16:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69370">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_GFOAg1ahQPyzdWXoWTNp1fN_hu9UeNpg5JK_E28yf3sxu7w-096mco7TNQCUHrBnMU4gFN5kK6Cz1YmBzI4G-r7nfQ66841Cj9LcLkQUY6xd2LKKJVCAw4HrUrc3DNbup9cd-VlDJS_W4-hFhhV_0q63oCdH-2gGtcB-qS6xCUAWZCKFOQsa9U-l9smTMZ-ifnW49rMdsUI0VhFg72jia-9XcGaEh1xfkV61rezcr1bp-05mCUm6tzBJC18eQ7h_NqvJ4sjxF2nxj1R8YidA8OW1PvE4jZvTkkDurSsEmdpWh0nY1yuY9z9CRyWX_n4E_sSB6mP_RK6k4ChGDaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سفارت آمریکا در مصر هم برای شهروندان آمریکایی هشدار صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69370" target="_blank">📅 16:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69369">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=vIMLZfn98L0je8bL9AVHRDqotA75esHy2O1l1-cz-OCSxxPyvAh81NF8IwyqoN1JXw6u5Kmwx_plC0Z3i9pURAyH1ZNLru1R-MUlfCwh5VdteoB1G-1Rs9aBpQDqK4senj-wgnkFq5A-zD6PHzXrPWbJGxDVQUmEEm5yEnTmmgqyQgBAYmjw98ZuW856Yt__TAwQeaGHeeWVvdIrbjQsFfWusWBfnK7r3w78CRV-xTzco2sLfZVGRUVxr_32D5_RpUdLZdHytRyueYz2SwisCIKPkf4C3j2JIXDYHNVIbMSH5eSsYWwCs8pCmAZaezF9OCH-brQVH3vmw0RRErhP4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=vIMLZfn98L0je8bL9AVHRDqotA75esHy2O1l1-cz-OCSxxPyvAh81NF8IwyqoN1JXw6u5Kmwx_plC0Z3i9pURAyH1ZNLru1R-MUlfCwh5VdteoB1G-1Rs9aBpQDqK4senj-wgnkFq5A-zD6PHzXrPWbJGxDVQUmEEm5yEnTmmgqyQgBAYmjw98ZuW856Yt__TAwQeaGHeeWVvdIrbjQsFfWusWBfnK7r3w78CRV-xTzco2sLfZVGRUVxr_32D5_RpUdLZdHytRyueYz2SwisCIKPkf4C3j2JIXDYHNVIbMSH5eSsYWwCs8pCmAZaezF9OCH-brQVH3vmw0RRErhP4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پیرزن ایرانی توی مراسم اربعین، برای اینکه از یه زن عراقی صندلی‌شو بگیره، بهش حمله‌ور شد
😔
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69369" target="_blank">📅 16:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69368">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حالا ما کجا بریم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69368" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69363">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRZnQPHteFSOJhSOQFIFcCvEYDo3dGBoDlCQFdS6T11yClrlffTwNRjDSwA1VHw2BwEGEh30Mnp0CGq-RXqmQw8CKrFObqE1CXGF1_Kw7ULee-4hKFIdTVmlADulg-m9046DBHTX64we-stnYJeBg8rDnqSXWMr54xhVBeKA0Hkv4NxuHI4MFm8MN9hkLif6S67a8RpchKBZ-kIJ_tEr8He6u6RG1CP4XR_9HTEF6WmwtSLp7or8YtHYicJ5TSRI83gkwFULPWm8Ac0Hcow1nidug7CUDeBkxCbi_anrvasf0i6kil5m4j8db9l9RQdkaS5KuQtrobBD3mDeMDUKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-Iy2hDmxVk28bHLZzWQNTdxt5ut3mag_E7_Qpi74_ivsC9jtn3HPkfv0ay-JO25fYe1j7fIPUPxeJnH-Cuuhdo2oQTa7eEaeoUZP4xpnJr9XELRBkFLoUyCei8hlc7359MaoV1pYgVdU0i2kI4oxY4WvBtVlOtxZSNBbr3F4vXoVRyvSFPxjoM5H7f60lah84ZZeawZoFza_Ju9eSRIjDpZUXQ5ZoxwGzNYfM9rV_tICg9sMhmPwtZYgRIS1TZr-4tSxX43M-RVz9uQhJR4dFzS8Ycpcd0Uim0UDzevE8chIhCFifknCvRFOCs_N_ORoPdvUXsV2dtbs3DlJj561w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnQgd_qaLhoNKzn6KfbXAUJjc_KQvD1bewfAuG-JSTkN8jKvLdkz1nh8wstjsoTKWTCr-XWHU8skr218ZU89e_Rp9l4gLc4uOOd26xy4NTCB5oYo8DtbEDxN9kgz38nxNGobD27NI04gNkmcj8J7TD26TogaiqfdZM41NQkEqoZ4FybeQ_5Ruk7oK8ocXIy4kINepFhS1WOgj1Z9WUjs9iv7b6wdPC-qp9w1Qou2S905M4r5FIjvCfiIiFg9oTkwBRPRwTOZ1usTNuDd6rCGOXkYaIt7xDf-wpcuSb5kOZtO6lCnYTtgPaSHIa9f4IaAyUC-fANWLJQoT3PRcuVYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLblHhXBIF3TRCK9M_gKLKz6y-dB0pXnfDdSulIFL7LigsraEhsmLnGBoMDe0N3b_CBZBRVJDuqaYzsv5thwMpo4CHCPNy4VgY8oGwmN79J0-zOSa9CWIkzWuyYKSBO00D2NofH2493PiH4qOIuOdA114lLMOd_jCKpHrwvRhlrs0hH6J9H3OZ2-k_e6Onb3BjF90RlQ80uSv3HuuigYWS15TR8LuCdIM_m3zWBPupBse-YX6Cm98nwOsf7vPScxAkdXkXyc_16UA3ItxOA51g3kT3sJ434Lj8lCdLBJFbmnSpqeuo2FSLcBh-OG2ipazjwA4L9THqp_oLDWfrZWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTAKFACUFsFQkapTYnsdk5mM6ivOLF0N0Zb7bpM0ELN5J6NPKY0UkX9lZiVA_STpRQ4ayMONDJZ42NohL6MG1_L2KC2ThAkkDYLVoa-ybaQzfWS0qeoAIHMfPBGWhjoDQeBxooRGp44Ien0LhWY_jJ0kzcYuwxj3WZPuloosYOoDuVeAucQW775nezyzCxsLJN_VS2xgmGy4bbt4Z2luedoQp8fh_1TBBqKVgRWUs7I_y_Dxaa5ZhycD2E9cPqRAUGpAOm7DfRBLB6p_yZ8-8dRd8XkgupJtmQ_AyejBmsGmS_dVxPm3fhscJSpgUFGONUcjjSwi98tl5lGqm9OnVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارتخانه‌های آمریکا در خاورمیانه یکی پس از دیگری درحال صدور هشدار به شهروندان خود هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69363" target="_blank">📅 15:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69362">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=uTSrhoCyy7W8aXklCWkdusmYbsEpMTff2odNrHPKGICB8qWPL7DxVBxq9CCecwTjvyTamw1FjTko8TTOAQQx8lVKBNBU8ecfFbobkGRAjKkj7elYErLtlLZpuRDc_1NEFAn-X1JHO0AeD_jb6m3rSxju_19Y8gGHqPyOouT1d0JUcYacrDrsOfkIlWwrxWzkfNhC-Kn3DrEX3BhZ1x57kZSvD7HjFbKX2oG0y68yjnNo5lA1XSTJa53HNIrjwK87NN_WPXhR7Ezxt93tUw2Wh8LXaPFAF1X6r_YUuZTYlmj-GNWIAA6yllMDFdI950qCY_68_2kxR6mTCjir1__QNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=uTSrhoCyy7W8aXklCWkdusmYbsEpMTff2odNrHPKGICB8qWPL7DxVBxq9CCecwTjvyTamw1FjTko8TTOAQQx8lVKBNBU8ecfFbobkGRAjKkj7elYErLtlLZpuRDc_1NEFAn-X1JHO0AeD_jb6m3rSxju_19Y8gGHqPyOouT1d0JUcYacrDrsOfkIlWwrxWzkfNhC-Kn3DrEX3BhZ1x57kZSvD7HjFbKX2oG0y68yjnNo5lA1XSTJa53HNIrjwK87NN_WPXhR7Ezxt93tUw2Wh8LXaPFAF1X6r_YUuZTYlmj-GNWIAA6yllMDFdI950qCY_68_2kxR6mTCjir1__QNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده‌یاد مانوک خدابخشیان: دو شعاری که کار این رژیم را تمام کرد؛
رضاشاه، روحت شاد.
اصلاح طلب اصولگرا دیگه تمومه ماجرا.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69362" target="_blank">📅 15:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69360">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzUgi4gsL2sDagLqmhlCd2n1SE1ksmlXJ8GO7wC0YrM1NzERbu_oOaYGySoyg-N_CrSbfzI9S6dTYZQ5fm5Rllz0OpJ4A-h4w6p48saA5oFyejkRWFW1SfrUhYZyExDvAcU_7yHNhyilRRdBPtzVp8VpiFigGaZ6fc94lq4ct3qTw79U5zW1h9u3_XnLgmW_iwzkM-Ej8Gkmo94mS4U6QMXLISfIrUHL4Vjd6hM7H68_f_ujF4GYIIGFThKE0gAmNSk8yurZSNprycFcTbAMwx1-gXsKKtvXXBICGGp3aS24V5SqIoP_1dJa7QmIRcE0e-16TwefCJZBY3CUbTfqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gV-dSLrWoTZyAM5QJ_Sb9ej_FOwiD8BsT1S9wwvZbWAcjYGVzJTwczVbMAIBiu0RDMakZkriKwcTOEzgyMLzhLWYI6HU4rbMn2-5-sRgaXgZuzGzJwAxj_3DD_M8UCSDjRU02ZinxfOPIQJVC2S8NQ35VXP5bO7_1XAkb1iVInFFgxKQyhkGkG0CkXxbYMe8IrJPs4SSahdFmb7jUQjn5nWOADHxjYUY0wVzHvv82aaZpNksIAIMjU2xbEZkjdldD2siOkYSWUeEXTaa_xFAi7bS8H2p-IDrY20xK1WEiJo_gy8bwRZ78Ka-wnjw8rsDL6tLxRgWG06d7HiE02Rctw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارت آمریکا در اسرائیل و عراق:
آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69360" target="_blank">📅 14:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69359">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFFGIjz6Rwr1oaaL00YWy8OcXxBJjiepfystgt-a5kDirLAXaoqOmjtKKiiJb55Xl-3dJhpuA4tu4FQR2_OkB4fSiZ6UVA8BlDMEC9b5fFR2aXypkRqgct-y0yAJGGW0edRkNwUqcKw6RXmSWA52TLctY3uZHEWJnmgV7-BWHULzG9dE88Bm1hyNydO7xTWMbhwxQFNsvaWWCIaLhWsnBCbDCEA6WLw4jfhV67v2sygCfTe1EDaQlMDPbz7WcRMUPeCVLd1mNViCYEl7WwhcS_xc6cXjcX4-qC5U_oC5eR7rUNjRSoP82C1A3CTVk5-OOWgkjJ2eg5aHcmf_JxeQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:  بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.  @News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69359" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69358">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
تسنیم:
بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69358" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69357">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
دقایقی پیش از حوالی اسلام‌آباد غرب کرمانشاه، صدای چند انفجار شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69357" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69356">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=YonaERuz37hU4qDDNq-popSLKviQLZtN8rvsAdRYXwMTdHecg53_X7uFY3nLEYPIr27dVgQa2NyFvId3oHLZVZLj_l5XXos0dc4aKpZfyhOLZDV1NtIBaRQAWXxPaaaB9VIZL9YeXqQWVbiEh166N_4SvRJ14jxG8KzoM_pZ6CQNpdz2uIWx7ONcUTEfUNLQEmEoijGBV9PJvS-YCOJwJ6B3z9gs8-gmpfRJGFIwAUqNplQJfVoTMgl8ipOqVrvclbclxK40mvDo-oNAiguusYWTsS_K3t-8OrphQdneSTFaP54MskE3RSsMm_EcGIC6TPT91wZSSs5DODdIySbT0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=YonaERuz37hU4qDDNq-popSLKviQLZtN8rvsAdRYXwMTdHecg53_X7uFY3nLEYPIr27dVgQa2NyFvId3oHLZVZLj_l5XXos0dc4aKpZfyhOLZDV1NtIBaRQAWXxPaaaB9VIZL9YeXqQWVbiEh166N_4SvRJ14jxG8KzoM_pZ6CQNpdz2uIWx7ONcUTEfUNLQEmEoijGBV9PJvS-YCOJwJ6B3z9gs8-gmpfRJGFIwAUqNplQJfVoTMgl8ipOqVrvclbclxK40mvDo-oNAiguusYWTsS_K3t-8OrphQdneSTFaP54MskE3RSsMm_EcGIC6TPT91wZSSs5DODdIySbT0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه جوون عرب داشت به زائرا میگفت بیاید آب انگور بخورید که یه ایرانی رسید و بهش گفت:
آب‌انگور نه، بگوآب‌شنگول
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69356" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
