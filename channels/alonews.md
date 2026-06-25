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
<img src="https://cdn4.telesco.pe/file/tdn0nNdQz1I-CRPn6gpL4ftYOHYtPunv4G84ObMTusyPIA4YKEfQs2t_CkkPj_bDR8O9lPJcotI3hyY219t-45s64ebtXNg2AbSICPhrp9E4lZfvz0hGPTDpcj-0mbriKuzbtvzlHoyA17VTchsYLFNA1kjh6kIgWk9SAP5y6-CC39pLAk6mUwEssv-ln6JqaTIcW7hw7mYEfYCSfm7of37GOErcym20yquEQHiRzkupaJUq8Z6InLkjz9vjjSHjDkQyXQn8_d61c31-GskcUv7n2Mm31dyhScHtppgiJRda2fQtiK4rm-UMzp7HPEA2PZe2FO0psAl7kELalLz-Eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 07:27:51</div>
<hr>

<div class="tg-post" id="msg-130109">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ترامپ: بعد از 3000سال من صلح رو به خاورمیانه آوردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/alonews/130109" target="_blank">📅 06:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130108">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ: قیمت‌های نفت به شدت کاهش یافته‌اند، اما ما در پمپ‌ها چیزی متناسب با آنچه باید باشد، نمی‌بینیم. به نظر من، قیمت باید در حال حاضر ۲.۲۵ دلار در پمپ باشد، اما ما بالاتر از آن هستیم. ما در حال انجام یک تحقیق بزرگ در این مورد هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/alonews/130108" target="_blank">📅 01:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130107">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ:خیلی وقت ها وقتی با اردوغان مشکل دارند می گویند می توانی به من لطف کنی و با او صحبت کنی؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/130107" target="_blank">📅 01:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130106">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ درباره زهران ممدانی: ممدانی دو بار اینجا بود. او مرد بسیار خوبی است. او مردی جذاب و خوش‌تیپ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130106" target="_blank">📅 01:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130105">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ: کشورهای ناتو خوش‌شانس هستند که روته را دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/130105" target="_blank">📅 01:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130104">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237a076aa9.mp4?token=vRvNl68wDmBDAzH-sGjZIaV7aXO8ZqsVURk25uaX-i31ZeOP4-YrYZn-vo7JRXsXMFsaDolMPMzorRgdqS_E5heoEduVLYk3u2DV2QGmbAPM2QWj_cKwe-ZiBRPXll-ErWR0c9OaN1eRes0pCeDQORlK1iR8HWu193FX5AMTvUW2WBC5FY0tdHRsZiMF9ONhLZhcYezKUhZ0Ub-LUS82-N4e2R0TpLyH4avaZPswXwabxbQiwNxljEDQtz2viEZBWkchLc580sSPbJ2zyh_unJ8LIgjV65CaVqgWtNCYdO7_MlNKoBR06UHO4f1cHaSAYup1YHuWQsPQ1v5aiG-utg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237a076aa9.mp4?token=vRvNl68wDmBDAzH-sGjZIaV7aXO8ZqsVURk25uaX-i31ZeOP4-YrYZn-vo7JRXsXMFsaDolMPMzorRgdqS_E5heoEduVLYk3u2DV2QGmbAPM2QWj_cKwe-ZiBRPXll-ErWR0c9OaN1eRes0pCeDQORlK1iR8HWu193FX5AMTvUW2WBC5FY0tdHRsZiMF9ONhLZhcYezKUhZ0Ub-LUS82-N4e2R0TpLyH4avaZPswXwabxbQiwNxljEDQtz2viEZBWkchLc580sSPbJ2zyh_unJ8LIgjV65CaVqgWtNCYdO7_MlNKoBR06UHO4f1cHaSAYup1YHuWQsPQ1v5aiG-utg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا می‌خواهید اولین فردی باشید که در لیست نخست‌وزیر جدید بریتانیا برای بازدید قرار می‌گیرد؟
🔴
ترامپ: خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/alonews/130104" target="_blank">📅 01:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130103">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ: درست در میان یکی از موارد کلیدی: «ما اخبار فوری داریم. سنا رای داده که می‌خواهند ترامپ جنگ را متوقف کند.» ایران این را می‌بیند و می‌گوید: «این همه ماجرا چیست؟»
🔴
من احتمالاً کاری انجام خواهم داد که اردوغان را بسیار خوشحال کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/130103" target="_blank">📅 01:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130102">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4db3d1db8.mp4?token=sUjtczzYivZzmlECHNemVzeS-3h6w_tlf4wcG1aKv8Z7NGW7DdWKMmJDD3MAfYCzQCe6eWSRt0hNLxrbLQ6Ndh4cuKjX5AZgAC-O9eAVDTYPh_RhYzTPlLJ1oZwYcQjocw6EHyV7JosbrWqrac6dumevoWWIQINytz6y-IJfv74VrTjhy1k4Y4mnEIF3jPnBPNV5p5bsL9n1njdBXqFEKyZ95Sh-I7eGqo0Hi_Dedi6YEb897VvcdWROZTqwvNjS-AFOcVTdQgoRQrBGQnMRXzssHaF49WxJLSR2GU6IRvMt7FtGRIl9GD5iRS1vL19oVzGiJ792mdlhRavG79j-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4db3d1db8.mp4?token=sUjtczzYivZzmlECHNemVzeS-3h6w_tlf4wcG1aKv8Z7NGW7DdWKMmJDD3MAfYCzQCe6eWSRt0hNLxrbLQ6Ndh4cuKjX5AZgAC-O9eAVDTYPh_RhYzTPlLJ1oZwYcQjocw6EHyV7JosbrWqrac6dumevoWWIQINytz6y-IJfv74VrTjhy1k4Y4mnEIF3jPnBPNV5p5bsL9n1njdBXqFEKyZ95Sh-I7eGqo0Hi_Dedi6YEb897VvcdWROZTqwvNjS-AFOcVTdQgoRQrBGQnMRXzssHaF49WxJLSR2GU6IRvMt7FtGRIl9GD5iRS1vL19oVzGiJ792mdlhRavG79j-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا اگر یک توافق نهایی با ایران شامل هر نوع هزینه‌ای برای حمل و نقل باشد، آن را می‌پذیرید؟
🔴
ترامپ: خیر. برای من غیرقابل قبول خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/130102" target="_blank">📅 01:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130101">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e8734849.mp4?token=kQD9n0nwoxNgTTnK8stDCBKA-WYsCeSdQwF-N5WED1AHOVyRnYJGbRR95Q2mNPijCM7y5qUEWtxPfrogv3UsZSZ1a2ngy0IorObcd9MXgOAdbCrWjfukG8Xzl7MMTY5TiD2co8In9D1ElUAW76oGUAJ1w-Z_SbC2cmUxzUA_j9TbVukFLVllraw55cMbUrf50zEavtRNfPCif-XYI1Tx0Q32amscqQG1dTqBhlKV9IacjgesSJC5DbX8wZckGmUMQYEXTRdUg97d_Hp0fAeJKfwzx1nVasHlrLpujUmeeHJAJEzBDFUiTO9mCsG3CiGXjwK64BATfHbHaSVyXZ_yaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e8734849.mp4?token=kQD9n0nwoxNgTTnK8stDCBKA-WYsCeSdQwF-N5WED1AHOVyRnYJGbRR95Q2mNPijCM7y5qUEWtxPfrogv3UsZSZ1a2ngy0IorObcd9MXgOAdbCrWjfukG8Xzl7MMTY5TiD2co8In9D1ElUAW76oGUAJ1w-Z_SbC2cmUxzUA_j9TbVukFLVllraw55cMbUrf50zEavtRNfPCif-XYI1Tx0Q32amscqQG1dTqBhlKV9IacjgesSJC5DbX8wZckGmUMQYEXTRdUg97d_Hp0fAeJKfwzx1nVasHlrLpujUmeeHJAJEzBDFUiTO9mCsG3CiGXjwK64BATfHbHaSVyXZ_yaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا فکر می‌کنید زلنسکی در حال حاضر برنده است؟
🔴
ترامپ: خب، او کارش را نسبتاً خوب انجام می‌دهد. ببینید، هرطور که به آن نگاه کنید، او کارش را نسبتاً خوب انجام می‌دهد.
🔴
او حداقل از پس کارش برمی‌آید - بسیاری از مردم در هر دو طرف می‌میرند. اما فکر می‌کنم او کارش را نسبتاً خوب انجام می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/130101" target="_blank">📅 00:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130100">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ درباره ترکیه: مردم نمی‌دانند که ترکیه از نظر نظامی چقدر بزرگ است
🔴
ارتش بسیار قدرتمندی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/130100" target="_blank">📅 00:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130099">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1dea6d4d.mp4?token=YRx5_JnQGeZL68yJ7WOKDvOaxu3t_kO1sJdd8MiNK0-jM5tQN7dJdXJc_BRQhcVXN9YlBlEQZuq6JedCrwk7goREMsY9xQRE6iwKwA_zRRoqeQPrOzZuK-oU6WOQXEUCcSedut6C42uxw7oOKFFdhfP8Wn7fw-M9lp9xlLY3khWiyYX_FXjIhgrVKkfYekF5-gdtwt2xCWgjiEhK2YYczrsYPlyWEyyJWDei3k1mKavvtz4l_erYXFoeiFkSXG5koWIsw0lVfwToxvuRneYpz2WghLqbFHydr1JJtATum4VWzLrfl4QCm1SznduxwT07vytkIImF90RF5RcVr42zFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1dea6d4d.mp4?token=YRx5_JnQGeZL68yJ7WOKDvOaxu3t_kO1sJdd8MiNK0-jM5tQN7dJdXJc_BRQhcVXN9YlBlEQZuq6JedCrwk7goREMsY9xQRE6iwKwA_zRRoqeQPrOzZuK-oU6WOQXEUCcSedut6C42uxw7oOKFFdhfP8Wn7fw-M9lp9xlLY3khWiyYX_FXjIhgrVKkfYekF5-gdtwt2xCWgjiEhK2YYczrsYPlyWEyyJWDei3k1mKavvtz4l_erYXFoeiFkSXG5koWIsw0lVfwToxvuRneYpz2WghLqbFHydr1JJtATum4VWzLrfl4QCm1SznduxwT07vytkIImF90RF5RcVr42zFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ: شهردار لندن ناکارآمد است، یک فرد بد و نماینده‌ای فاجعه‌بار برای کشور شما.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130099" target="_blank">📅 00:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130098">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ درباره ترکیه: مردم نمی‌دانند که ترکیه از نظر نظامی چقدر بزرگ است.
🔴
ارتش بسیار قدرتمندی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/130098" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130097">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afbb8ef64.mp4?token=jXy4kK5xG7Fo8gm8o5EOvviBBNFg5TDFhDlW9l9IvgPD9r8-N5TEvWDPqd_AgYHG5DfLdvryNf1igZveAoMRMcwxOEGbTcXfdn7y0EfQeBTxkebt9x8zDZ1TSWIl_3s2EDAh-ITw1As7BQnWOG9F1IB7-2cB7_p27gQ1Rlr7kqt_3hc5lxFnG7c_ljdjtwSdz3IYvbCgWzsWPx_25Aev5KYnB0Btx8IzDeO0GoaN5DzUZMATYwAM5olY2g1-j1KMnh2YP4ymBRGlnQ_IeEZRC4Qmz4NXmZZsodo_9CnL4qIfMlloaorCwWWYJASBH-SUWQNfO6QSpV46-tnL7LnCC19HVQWe6DjjVQ-I03CWhNiH3dDyGEM0GCzGrW5WEbwSmrc-6e_3HcSgs9MeIQb7yhuH4tEzb2Sbo-INyZOwpSuTfYHeH0qoZyDfUg3UaGc_c8SqDehJ1RSj_t4W8J4Iad_P850d7S2mcqRbaECcJBXFUhGwp2wOdgnU_vzPEHvgCq2GvAkQXgUK5NdBUS2DAA5YifZiHOiM-Qc3TDr2srHwu6m-1VzMxKFTUCv7b6Wo3q8VzkbngJwD1JEGCnuEUcBFd38qHA_qPjyZ1mZZ4NIxn8MJ7VWMXFZv7B6A40YrKwUr2kfFXWhKmlryTpJmiEjHiPyVQT3OH_hlxoVFsUc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afbb8ef64.mp4?token=jXy4kK5xG7Fo8gm8o5EOvviBBNFg5TDFhDlW9l9IvgPD9r8-N5TEvWDPqd_AgYHG5DfLdvryNf1igZveAoMRMcwxOEGbTcXfdn7y0EfQeBTxkebt9x8zDZ1TSWIl_3s2EDAh-ITw1As7BQnWOG9F1IB7-2cB7_p27gQ1Rlr7kqt_3hc5lxFnG7c_ljdjtwSdz3IYvbCgWzsWPx_25Aev5KYnB0Btx8IzDeO0GoaN5DzUZMATYwAM5olY2g1-j1KMnh2YP4ymBRGlnQ_IeEZRC4Qmz4NXmZZsodo_9CnL4qIfMlloaorCwWWYJASBH-SUWQNfO6QSpV46-tnL7LnCC19HVQWe6DjjVQ-I03CWhNiH3dDyGEM0GCzGrW5WEbwSmrc-6e_3HcSgs9MeIQb7yhuH4tEzb2Sbo-INyZOwpSuTfYHeH0qoZyDfUg3UaGc_c8SqDehJ1RSj_t4W8J4Iad_P850d7S2mcqRbaECcJBXFUhGwp2wOdgnU_vzPEHvgCq2GvAkQXgUK5NdBUS2DAA5YifZiHOiM-Qc3TDr2srHwu6m-1VzMxKFTUCv7b6Wo3q8VzkbngJwD1JEGCnuEUcBFd38qHA_qPjyZ1mZZ4NIxn8MJ7VWMXFZv7B6A40YrKwUr2kfFXWhKmlryTpJmiEjHiPyVQT3OH_hlxoVFsUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ترکیه موتورهای جت F-110 را می‌خواهد و همچنین جنگنده‌های F-35 خود را. آیا با یک کیسه هدیه بزرگ به ترکیه می‌روید؟
🔴
ترامپ: فکر می‌کنم بله. او عضو ناتو است. برخی افراد او را به عنوان عضو نمی‌دانند، اما واقعاً عضو است. او عضو قدرتمندی در ناتو است. بله، احتمالاً کاری انجام خواهم داد که او را بسیار خوشحال کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/130097" target="_blank">📅 00:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130096">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39188d729e.mp4?token=AuqCJCQ4W6F6NbaFO9nz0nA5FQxWllM6EFXX8KKt-_Nc8FC3C_sVsqVC9gnukwwxNZkq3m_M2xHg-HHvztTpBt_wZEuKojJExDfIuHwRyBd3hW9oq2qBUav9vj-1_85O1inTRwlwlJvdkqhCxtSpUiZD09h2ke6ZNoXVtb5TR6Ez2vUOEcK0K0y8PYj6_UFmSQsCrtxfxDeI7FIk-S2wbHLYQJSvQDQq1If5sSbIcPmKkMohF5quVoXuQGGxOMO2kottebSSGeejr85sUfVDo9lnCgLTHB1Xqc740B88JcYWfvvpAz63xRI_RtzeO_ljP7E9liHRaw9Tjly90l2rFhRGSWARn6KTv_bXQqQ_sRuUrTskpWBQZ1xswyNn2ZW0ry5GlkpeYedBVk9vJLN2PMcA1WR2NSlIfJAc7iY5lMccb3jNTTjG-GsHzraaSbNAwYaMp0NY3Xraa7Fz4rLVWv1Mt2PcD2RCeJ3h-thj9gOvj0EXShUssuoXgSSrUkhOPOQkHSOMHTCrWtAIQ8cZ6iVNBYN5e-MXkO1ZcB-lhn9YJalRoFBVoGei8kr15wuW-S8RFgTR5TgY7W-D2FYR2uPKHegWBFSTsb4jNumGMfQklz4j2wxwTH5JqqE2FGUqBXYee0xMlBn13waM8zfKUwb5YdSXrrQgSZwpKoJn53w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39188d729e.mp4?token=AuqCJCQ4W6F6NbaFO9nz0nA5FQxWllM6EFXX8KKt-_Nc8FC3C_sVsqVC9gnukwwxNZkq3m_M2xHg-HHvztTpBt_wZEuKojJExDfIuHwRyBd3hW9oq2qBUav9vj-1_85O1inTRwlwlJvdkqhCxtSpUiZD09h2ke6ZNoXVtb5TR6Ez2vUOEcK0K0y8PYj6_UFmSQsCrtxfxDeI7FIk-S2wbHLYQJSvQDQq1If5sSbIcPmKkMohF5quVoXuQGGxOMO2kottebSSGeejr85sUfVDo9lnCgLTHB1Xqc740B88JcYWfvvpAz63xRI_RtzeO_ljP7E9liHRaw9Tjly90l2rFhRGSWARn6KTv_bXQqQ_sRuUrTskpWBQZ1xswyNn2ZW0ry5GlkpeYedBVk9vJLN2PMcA1WR2NSlIfJAc7iY5lMccb3jNTTjG-GsHzraaSbNAwYaMp0NY3Xraa7Fz4rLVWv1Mt2PcD2RCeJ3h-thj9gOvj0EXShUssuoXgSSrUkhOPOQkHSOMHTCrWtAIQ8cZ6iVNBYN5e-MXkO1ZcB-lhn9YJalRoFBVoGei8kr15wuW-S8RFgTR5TgY7W-D2FYR2uPKHegWBFSTsb4jNumGMfQklz4j2wxwTH5JqqE2FGUqBXYee0xMlBn13waM8zfKUwb5YdSXrrQgSZwpKoJn53w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ: آن‌ها توافق کردند که ۵ درصد هزینه کنند، و آن‌ها آن را پرداخت نمی‌کنند.
🔴
روته: شما نمی‌توانید آن را در یک سال هزینه کنید.
🔴
ترامپ: تو میتونی. تو میتونی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/130096" target="_blank">📅 00:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130095">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ: بریتانیا در حال مردن است. باید دریای شمال را باز کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130095" target="_blank">📅 00:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130094">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ : تو مذاکرات، پیشرفت‌های خوبی به دست اومد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/130094" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130093">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ درباره اردوغان، ترکیه : خب، من باهاش رفیقم و ازش خوشم میاد
🔴
توی جنگ هم قاطی نشد می‌دونید، اردوغان یکی از محتمل‌ترین آدم‌ها بود که می‌تونست وارد جنگ با ایران بشه
🔴
حتی شاید سمت ایران رو بگیره، چون همون‌طور که می‌دونید خیلی دلِ خوشی از اسرائیل نداره. من ازش خواستم وارد ماجرا نشه و اونم قبول کرد
🔴
یه نفر دیگه هم که خیلی خوب رفتار کرد رئیس‌جمهور چین بود
🔴
اونم می‌تونست وارد قضیه بشه؛ بالاخره کلی از نفتش رو از اون منطقه تأمین می‌کنه
🔴
کاملاً قابل تصور بود که بخواد دخالت کنه، ولی ازش خواستم وارد نشه و اونم وارد نشد
🔴
خلاصه، کارمون رو خوب جمع کردیم. اون هم کنار کشید. اردوغان آدم فوق‌العاده‌ایه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130093" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130092">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
خبرنگار : گزارش حمله به مدرسه دخترانه در ایران رو دیدید؟
🔴
ترامپ : نه، ندیدم
🔴
خبرنگار : چرا نه؟
🔴
ترامپ : باید صبر کنم گزارش کامل بشه
راستش نمی‌دونم اصلاً هیچ‌وقت بتونن این موضوع رو حل کنن یا نه. می‌تونی از پیت بپرسی. شاید اصلاً کار موشک ما نبوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/130092" target="_blank">📅 00:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130091">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: هیچ حمایتی از سوی اروپا در رابطه با جنگ ایران دریافت نکرده‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130091" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130090">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/130090" target="_blank">📅 23:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130089">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98be8e64b.mp4?token=KYFez1R1nHe-y6d_wzsB_xMzE7HkVz1ToTh5gZZLuvi4vYcWr4DtcYQIkL0f_nx4Rl4QPg2nCcPttNjXy8oeM2aF9t3PYdy8LKeVX4IVSbyL4EI3dpgOr0uSQsYsohw6iyG5JwAx8GZj2-UA4Hw_xWEC463ys-rNcZg5ztnc7_Hxu4hARx50V9ElUExLLRBWqVNkUiLGeDREz2udXfjclpoerhl-wi10BSO3r6cbD_6oYx7FYMb_7LM5iiuLqabjpVAGn0altW5UyZ3vkZYwMtPBAfCMKI82THO7qFKP6QNjtknZ6Q06F77cIlQwALdaoFcV8XipKoD35bC07kulUR-6BUVGmp1zE1ZG0vsl_2zChKdIw_dZqRtbDxUzlh4_nSzk3VcHaYwxFRLO8N__fbnR5iEyHGwVgexQUQQGuwSNTGOrTuuN7Ge-cYEDfsog1vd7tIdlwnhsfrz3eWeL9fep5_ULd6fDbIOT29lEyXqgN7G6DMFrcPvbio4srq4ezna1qBNrGWCNrwBX9mTOn65jYegbaaPfJyVyGqX0WycdOLuhdGno8aTLT_cxZ2HdqlX41pn037UDle7a1RVYgkftqyeeXC3zailOZd87xIMm-iMS_4MNxvNKIYHyiToCJc_svIyyPjEX26p8s3D8WGgLnWyIPY8qOxUEE-IRmy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98be8e64b.mp4?token=KYFez1R1nHe-y6d_wzsB_xMzE7HkVz1ToTh5gZZLuvi4vYcWr4DtcYQIkL0f_nx4Rl4QPg2nCcPttNjXy8oeM2aF9t3PYdy8LKeVX4IVSbyL4EI3dpgOr0uSQsYsohw6iyG5JwAx8GZj2-UA4Hw_xWEC463ys-rNcZg5ztnc7_Hxu4hARx50V9ElUExLLRBWqVNkUiLGeDREz2udXfjclpoerhl-wi10BSO3r6cbD_6oYx7FYMb_7LM5iiuLqabjpVAGn0altW5UyZ3vkZYwMtPBAfCMKI82THO7qFKP6QNjtknZ6Q06F77cIlQwALdaoFcV8XipKoD35bC07kulUR-6BUVGmp1zE1ZG0vsl_2zChKdIw_dZqRtbDxUzlh4_nSzk3VcHaYwxFRLO8N__fbnR5iEyHGwVgexQUQQGuwSNTGOrTuuN7Ge-cYEDfsog1vd7tIdlwnhsfrz3eWeL9fep5_ULd6fDbIOT29lEyXqgN7G6DMFrcPvbio4srq4ezna1qBNrGWCNrwBX9mTOn65jYegbaaPfJyVyGqX0WycdOLuhdGno8aTLT_cxZ2HdqlX41pn037UDle7a1RVYgkftqyeeXC3zailOZd87xIMm-iMS_4MNxvNKIYHyiToCJc_svIyyPjEX26p8s3D8WGgLnWyIPY8qOxUEE-IRmy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره دبیرکل ناتو روته:
او در سراسر جهان مورد احترام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/130089" target="_blank">📅 23:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130088">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: پول آزاده شده ایران صرف خرید محصولات کشاورزی اضافی آمریکا می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/130088" target="_blank">📅 23:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130087">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9wL0-i3SjYh-XKJOtM3QrP5ILFClxgsH0e9DFmw081_FOPdek9W7wUK3MVbTgh_w1OgRqYu2TgKC5YanBD15aqsFBlaFqYjgphE4_vRauHFESnWP4Fr1V6arzln3zNcFxjE_XLU3-62i0YibSws_gHyHeddOyGMUt7NF4NzWyqiC3oj_kT_w1BhcEcHdNxPnaVWLwBMLyIG1R7j5EO-2IKgmkfMSoe-u0noI4EfyTGPXALzvOCt57bF0PcrKRZH69sfZjRE8jPW0A9oMRPoaJuYxkg_dVqCS4JLrg8kyfWRRx22hzegQcr3QlyDwblmfxqPC6jjCAFzng12q6SVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/130087" target="_blank">📅 23:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130086">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نیویورک تایمز: سبک ترامپ این است که نتایج مطلوب خود را به‌عنوان توافقات فرعیِ کاملاً مذاکره‌شده توصیف کند، به این امید که ایران را به هر بخش از توافق متعهد کند
🔴
ایران این موضوع را دریافته‌ و استراتژی رسانه‌ای خود را دارد؛ اظهارات آمریکا را تکذیب می‌کند تا در تنگنا قرار نگیرد
🔴
هم واشنگتن و هم تهران درگیر یک نبرد رسانه‌ای برای شکل‌دهی به روایت و پیشبرد نتیجهٔ مطلوب خود در مورد عناصر خاصی از مذاکرات هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/130086" target="_blank">📅 23:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130085">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پزشکیان: امروز هم در سران قوا، هم در شورای امنیت و هم در مجموعه سیستم یک نگاه مشترک داریم
🔴
اگر دستاوردی داریم دستاورد این مجموعه، رهبر بزرگ و مردم عزیز است.
🔴
امروز ایران را در منطقه به عنوان یک قدرت می‌بینند
🔴
فکر می‌کردند کار جمهوری اسلامی سه روزه تمام است و مثل سوریه یک شخصی از خودشان را سر کار می‌آورند.
🔴
سپاهیان و ارتشیان ما با جان فشانی کاری کارستان کردند.
🔴
من نمی‌توانم مسئول مملکتی باشم که مملکت شیعه و علی باشد و یک عده بیکار باشند و گرسنه باشند. خدا از من نخواهد گذشت، از دولت نخواهد گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/130085" target="_blank">📅 23:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130084">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9TfnyoYI63UbTGAp0ialz2jwzTQolJ_-rKEb8DvlXzuf7fz1kE-jn9NL4B4UkjB0eQO46SMfUBInlCUOklxvM4l6zWhB1enG5E4DjtM4GbBS7EmYNyonfyyKvzGpkgnsp5CJ9oUuSAQ8siuRsmd7lm40YPLIJ-cdtj2MlohpG24hqnUk0UyO79QPQ07gVWkCSYo0DCXN6DgTflXX63VHW1VShyRGF6P_EIt0wKdahOGzMYcgVKEFFjTjv2ZSpvOhIgnc2h3Z5JSejOwx3NWwsRcHDPhD6lY6tlJP24JFiY187zRnzQiqrFxqXNmfivu4FbrV6lsgU928ZWLYKTD-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدراعظم آلمان فریدریش مرز:
پیام ما به روسیه روشن است: اوکراین قوی باقی می‌ماند. ما در حمایت خود کوتاه نخواهیم آمد. و در ائتلاف ترانس‌آتلانتیک، ما به‌طور نزدیک کنار هم ایستاده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130084" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130083">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
بقائی: اظهارات ضد و نقیض مقامات آمریکایی درباره تفاهم خاتمه جنگ تحمیلی، کمکی به کاهش بدگمانی متراکم ایرانیان نسبت به آمریکا نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/130083" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130082">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کانال 14 اسرائیل :اسرائیل در حال آماده‌سازی برای احتمال حمله دوباره به حوثی‌های یمن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/130082" target="_blank">📅 22:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130081">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0DGaSLjgxdxnqSn4OugbEFnQYTxNSCsC3qUACuKUckTQmFpfYRkUOr8Q6tnv1pAFhl6VLVHgEluM2EGArTCxk2eyc0IcXxRUyhvumu1hlSBm7W5ME1Xd_h9Jvzh2M0z_l4rAcbDGOIMC2xIqOyCmgIuZ_WE7cwUVf3bd2j6mOUfBNaYYoDSTz1J0ew9-oqfpnSIP9_sqm7Ay4YyS0CdlJb86-e5jvD-BS2GjCgkaYQUEKOO5n8PX8dCqihIlvhsBnvPjMTi77w3ABC4oLonrAx4BmLnXC80JJVqT9ja7tNICTqdipg1MeYmsCfOP2ujr39IN8d-1qJMHv6wItRyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ مشاور وزیر ارتباطات به معاون آقامیری(دبیر شورای عالی فضای مجازی)  که از مخالفان بازگشایی اینترنت بودند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/130081" target="_blank">📅 22:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130080">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
در نشست ناهار امروز ترامپ با سناتورهای جمهوری‌خواه در کنگره، بیل کَسیدی بر سر تفاهم‌نامه مربوط به ایران با ترامپ درگیر بحث شد.
🔴
به گفته یک منبع، لحن کَسیدی آن‌قدر تند بود که عملاً سر ترامپ فریاد می‌زد. این خبر را MS NOW گزارش کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130080" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130079">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ: ایرانی ها خیلی مهربان بودند و هر چیزی که خواستم موافقت کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/130079" target="_blank">📅 21:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130078">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOfsLKAFk-hX-zlitWiLvP63hLZzHF22ph3RgSkDx43_glQfg5J4rJ0usweCTuEAuj70iw6sN-DKoe0Exk6zPA8Sb3laI6KkYODHeKE3j50a42dvbD44g9KHBunpPfEPV5hnLXTx4Nub1-uroOAm_TwPvyUtsEshjtJDcuGquzo-XkFm7GuUGZHUZ2vJH15iGRP_pzyBy30-SNufUcqYUXbbA1Pdec1G4eR7M8gN6Vih9f_oA802nKO3aIOGQWPeKy2Y5JzDXqNXEEtTyfUBYXCJu0eHkXCfIn0L9QT_iV0KAQt60qHMdo5N0qCySR317zQrmmkbXDE5_FyX8xjoAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارشناس صدا و سیما: باید فرعون زمان را سرنگون و تحقیر کنیم و دنیا را آزاد کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/130078" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130077">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
مارک روبیو  در سومین ایستگاه از سفر به جنوب خلیج فارس، بعد از امارات و کویت، وارد پایتخت بحرین شد.
🔴
او در فرودگاه مورد استقبال همتای بحرینی قرار گرفت. بحرین میزبان پایگاه دریایی آمریکاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/130077" target="_blank">📅 21:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130076">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیر انرژی آمریکا مدعی شد: بازگشت جریان نفت به حالت عادی به دلیل مین‌های ایران به تأخیر افتاده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/130076" target="_blank">📅 21:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130075">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
یدیعوت آحارونوت: فرمانده سنتکام به زودی وارد اسرائیل می‌شود و با وزیر جنگ و رئیس ستاد ارتش دیدار می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/130075" target="_blank">📅 21:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130074">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/450a87f549.mp4?token=D9DrBxqcxbSNCjNgVNbNsRQd91WMxhR0Vg1c5_toOdlrKWgJn1IiYkiu63uvG1KxQuuKGk96wEIJVJezArRxVMfKTIDM8vGzQju9oyPR2ofJXkxUW40_GqiC8cA0B9vcBUuLd56BddYKXqImNA7rcDzGVHtUheULAiUU1qNW1jDK6mOcrVhEXiDbjClcfylUWY4lx0xgNwvX_bh08Pnw_yZ3P0P4lYbnA8EcCNRz92hx4QZMkY5z_5uf9-zZBQS9k-p6iUHf2rJLqyOiGDc0srTOZ4WVTI1v2cs74J2Qr8AmXguyr0FVcxUBysNgkpByHoma76j69hIdfqEyhMY5nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/450a87f549.mp4?token=D9DrBxqcxbSNCjNgVNbNsRQd91WMxhR0Vg1c5_toOdlrKWgJn1IiYkiu63uvG1KxQuuKGk96wEIJVJezArRxVMfKTIDM8vGzQju9oyPR2ofJXkxUW40_GqiC8cA0B9vcBUuLd56BddYKXqImNA7rcDzGVHtUheULAiUU1qNW1jDK6mOcrVhEXiDbjClcfylUWY4lx0xgNwvX_bh08Pnw_yZ3P0P4lYbnA8EcCNRz92hx4QZMkY5z_5uf9-zZBQS9k-p6iUHf2rJLqyOiGDc0srTOZ4WVTI1v2cs74J2Qr8AmXguyr0FVcxUBysNgkpByHoma76j69hIdfqEyhMY5nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دسته های عزاداری تو انگلیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/130074" target="_blank">📅 21:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130073">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
تانکر ترکرز: ایران از ۱۵ ژوئن (۲۵ خرداد) تاکنون ۴۰ میلیون بشکه نفت خام صادر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/130073" target="_blank">📅 21:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130072">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز گفت که برای دسترسی به آن مواد عجله‌ای وجود ندارد، زیرا در پی عملیات «چکش نیمه‌شب» در زیر زمین دفن شده‌اند.
🔴
رئیس‌جمهور آمریکا ادعا کرد: «آنها با این موضوع موافقت کرده‌اند، با بازرسان موافقت کرده‌اند.»
🔴
ترامپ به فاکس نیوز گفت که بازرسان آمریکایی در بازرسی از تأسیسات هسته‌ای ایران، به آژانس بین‌المللی انرژی اتمی ملحق خواهند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/130072" target="_blank">📅 21:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130071">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
آکسیوس: اولین دور مذاکرات اسرائیل و لبنان در واشنگتن بدون نتیجه پایان یافت و گفت‌وگوها در فضایی به شدت پرتنش برگزار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/130071" target="_blank">📅 20:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130070">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
یک منبع آمریکایی به العربیه گفت: «در مذاکرات مربوط به سازوکارهای اجرای خروج اسرائیل از لبنان و استقرار مجدد نیروها، پیشرفت حاصل شده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/130070" target="_blank">📅 20:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130069">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
خبرنگار: آیا شما هم مثل برخی از بخش‌های نهادهای اطلاعاتی آمریکا معتقدید که اسرائیل به دنبال تضعیف یادداشت تفاهم فعلی است؟
🔴
روبیو: من نمی‌دانم از کدام ارزیابی اطلاعاتی صحبت می‌کنید؟
🔴
خبرنگار: این موضوع گزارش شده. آیا واقعیت دارد؟
🔴
روبیو: نه، من اصلاً نمی‌دانم این حرف‌ها را از کجا می‌آورید. اسرائیلی‌ها دقیقاً می‌دانند که ما داریم روی چه چیزی کار می‌کنیم. تمام شرکای ما در منطقه هم باخبرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130069" target="_blank">📅 20:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130068">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ : ایران امتیازات بسیار مهمی می‌دهد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/130068" target="_blank">📅 20:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130067">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ : ایران امتیازات بسیار مهمی می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/130067" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130066">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
تلگراف: ترامپ ممکن است پس از انتخابات خواستار توافق جدیدی با ایران شود
🔴
روزنامه تلگراف به‌نقل از منابع نزدیک به ترامپ مدعی شد که رئیس‌جمهور آمریکا احتمالاً پس از انتخابات میان‌دوره‌ای کنگره، توافق فعلی با ایران را کنار می‌گذارد و به‌دنبال توافقی جدید خواهد رفت.
🔴
به‌گفته این منابع، ترامپ برای مهار فشارهای اقتصادی و حفظ موقعیت جمهوری‌خواهان در انتخابات، به توافق کنونی با ایران نیاز داشته است.
🔴
منابع آگاه به تلگراف گفته‌اند بازگشایی تنگه هرمز و دستیابی به تفاهم با تهران، نگرانی بخشی از جمهوری‌خواهان را کاهش داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/130066" target="_blank">📅 20:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130065">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مارکو روبیو : کمیته فنی در تاریخ ۲۹ این ماه (پنج روز دیگر) برای ازسرگیری مذاکرات با ایران به سوئیس بازخواهد گشت. به گفته روبیو، گفت‌وگوهای فنی با ایران دربارهٔ تحریم‌ها و مسئله هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130065" target="_blank">📅 20:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130064">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
روبیو ، وزیر خارجهٔ آمریکا: تمام دنیا با هر سازوکاری که برای استفاده از یک آبراه بین‌المللی [یعنی تنگهٔ هرمز] هزینه دریافت کند، مخالفت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/130064" target="_blank">📅 20:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130063">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkRiDDKJjn0nDBQ9fyGuWvBQk_ww9CbsvGRt4bqLsaspbG-km-q2U2zK_g9NXy-1DuA0BrdVGCuKfbucRFXFD2o3KMiFslmE3L1xrmBeds7RJdBCTSaAq87K5NGZGJqr9NS6S7_yPyRQZGUuggLg1eI-mGlJddmANs173mTsEE69H_HQvrNWqhLDpr-lV6PYe1GyWBIVDwrQ8smlEedEl8WxVXCcw1lVw4m9Ss-N3DmqEiL4iQCGrAH9YnwY1BQUeq4wB-S--81kFIstzILySnfAjS-rXsto_e0K-AyEY9v-_p_WYPu1vGpx1WGVuE4jKU4MtXfweWu-mab2YLCpIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی قبل زمین‌لرزه‌ای به بزرگی ۳.۴ ریشتر و در عمق ۹ کیلومتری زمین در منطقه انابد رخ داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/130063" target="_blank">📅 20:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130062">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZq0z0jg6w24havMeIsXRHwDSh2BSQ5Aq6iYI-9Xbl49hMYRFM-LQL0vWo9pdZzGOpXigVUwVIGDJl9S-9_-Cv6KXYxCKgiqui7zZt2bEBnob9fpR3IqbuDMtcz-0RyBmfbaaUaG3uvZqcob31gucVBXLLK-94odiRvOcUgk7ayIbvZcIgqeaetxVvvdsyU1Ani68cVoaDbgcannEGzNbtU7-37Q-Ootv8mAotABeW156ooEA_ji57VnNBivKd3l7rLQrL2HqQ94uFeujaa3PuAXApe_1Ejj7DGOzGU5zrhM1UJ7qhilgJ1TOLRc_ZEJcF1qC6oshM8ecku9lR1vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت تتر به ۱۶۶ هزارتومن افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130062" target="_blank">📅 20:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130061">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس: ده‌ها کشتی پس از اعلام عمان و سازمان بین‌المللی دریانوردی مبنی بر گشایش مسیر موقت برای خروج کشتی‌ها، از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/130061" target="_blank">📅 20:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130060">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
دبیر انجمن واردکنندگان گوشت و فرآورده‌های دامی: با حذف ارز ترجیحی شاهد جهش قیمت گوشت در شهریور ماه خواهیم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130060" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130059">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtC3f8RHTfNrq2g1BNBg0ZVrrxLuqNfF7Rbz3V_pJVdQuL9iikOpPYsMj10t4F4NBFfvV40UV4eqxXZPRDjEENJlHeqDlhTvBpLwNl9xxU_Ir3AfPF_DpYTs7lGkrlXOyReZZhOMThTZZ72FUuXvSeJvIIDgcvXUGQmCo3D6SsZmS8zUCPBvBH4eXo7TtKYjvH3uWrxYXbX36m0QfNhKF7LqnJxXsXOJPIK1uVw5waXvDnEN-7-744m7JjSPx5Z0jY4v9eVhRC-4BkCS0iwtKH0ZNA05bPPwOGUJCmLz6UUKVY8e4gn3NL7DsrFAGNlYj1he48G1Byr3lNZxaG0HSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در سال ۱۹۹۰ میلادی، اسرائیل و ایران تقریباً سرانه تولید ناخالص داخلی یکسانی داشتند. امروز، سرانه تولید ناخالص داخلی اسرائیل تقریباً ۲۰ برابر بیشتر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130059" target="_blank">📅 19:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130058">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
روبیو: ما گزینه‌های زیادی داریم، از جمله اعمال تحریم علیه ایران در صورت عدم پایبندی به توافق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/130058" target="_blank">📅 19:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130057">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmJS6DQwq0zS9BqVcKHQ1RBByxQ1OoeA3xq1EyidFUTi3XeRoSPLnvjEug3f2db_H_cwo0av8JSUiNYWYVHb43Jkx2ds2RqsjDL5_G2lapXLIWr3lqwMITZJvfdWiHVrHzI9xTR-lM0lL382HkWfDwAXUJRw-U8nDAdU46lvA6rAQpmw2xA4pj8OZk6V4WdahiSGMrlKKhQYkhHvK_i3m-b8qjV_8Pm5lOqg-UWTlmvwUlS0ulmeLNPw_Opfb2isrO5K-gsFK5zfrQjDX2wn9zoHdVzBbdAVelyU81gPWfjEvcoiPFBN_KbPft6ZTrHHeuGkdTdLZY-scQx6_Tofjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه حمله پهپادی اسرائیل به النبطیه الفوقا، لُبنان انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/130057" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130056">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: نتانیاهو امشب جلسه امنیتی در مورد لبنان و سوریه برگزار خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130056" target="_blank">📅 19:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130055">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4FJQ7ONHsiR6cdmKomKI9rrp_9ig9eE_mxYdlEwI54mjycW7gdA2S4Rq8xV_Jg7db9W-xfZhfqfn1aj_aZeDg7xVBNqYywSIJ2WOlJjlK6qYKHf4qy0DjNUQIEi4ifjTvgX8HnmYs4sYfBjNPfpyMW-o3PCyL-dko_adQFL8g-DSadjgwyAVF-s8APkYLRLEhNhbHUhn-WjZP4uM89dRdoxnNM_yhPh7oqSCOlankj_bLp6yxWW80g6zk3_Qnu6NCVApqEg3NyafLRWLA2IwQZI3cq3zj60jTPBxv1Ij3Uuaqg5pTSelJS5LCEzdCuUpOSnvT26TU9Vj05YeYckdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ جونیور: قیمت‌های آتی نفت اکنون به زیر ۷۰ دلار رسیده است به دلیل توافق صلح رئیس‌جمهور ترامپ برای پایان دادن به جنگ در ایران.
🔴
قیمت‌های پایین‌تر بنزین در راه است برای آمریکایی‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/130055" target="_blank">📅 19:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130054">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ابراهیم رضایی: تنگه هرمز را با مذاکره فتح نکردیم که با مذاکره واگذار کنیم
🔴
تنگه هرمز تا ابد ایرانی است، ما این تنگه را با مذاکره فتح نکرده‌ایم که اکنون با مذاکره واگذار کنیم، والسلام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/130054" target="_blank">📅 19:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130053">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وزیر اقتصاد: در جنگ میدان پیروز شدیم اما جنگ اقتصادی تازه شروع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130053" target="_blank">📅 19:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130052">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY6MTSCVm0CA5siJgEcQaDMVgxN6B3UjIaEhFwrm9n253s36spxrLAkyQA2yQSOHsOzCNuSPkRvyX-8p_PjI7VMcgmh3mLsYlPbRfr0E9QGDYITiHXKU-L1NyYXBMnudCpmg1bEesvOEG13ZIl-yI4t2YWElDTSFtDFW6tec2NsxhVTau1na61nXQU5J2KVKpBBjHNuLRCq01I_XlJits5p582fGZ8ONwJpJ1skREZ9QSLDT_baR2xgIISvdKUZYZj7bHatchekhepjwxG-jyB7py70nTB7u0XJ29hzp58szhTQcOGP2EsJOHPkmlnFu_awFDH_cpJx8NuB8lHbj6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: برنامه‌ای برای دسترسی به تاسیسات هسته‌ای مورد حمله قرار گرفته نداریم
🔴
معاون وزارت خارجه نوشت: هیچ نشستی با گروسی در سوئیس برگزار نشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/130052" target="_blank">📅 19:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130051">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a25fe3090.mp4?token=W8mPHyhHKM4OQzOoSx9Jptd9TPqSFRTJgT1Wr9BktHte7Om-p3on_Eu7eeCyhMt76myPmuh20TXqSnxD3I3vMvag1_xqFoKfXGUuGkUTwlWLNm1oOmrRWQSqagCn3RziG2ai9kGDmXrwqA44a2GVIcM77a6SuV5IyQNNIMbXHNowwdHmAdOl-BKEhFdqsNqQGeiWELqals4C3puc2AkCDa2V8CMTRQBQYIuVRP4OGE32csXkWRomJYsuJQmlMnJwjsjAIBMVzKNxqzH-1ewl8yuUQnoe_djymJKIMk_K0iJUf2k3CgoERNbw7ZRVUsEOeo20pygLxKp9a_tHQYcA8yYM0D7dpwKOHHD4SjnzAPmp7tNY7aDb0xLvx-wc2vkkA7eYAr78JA7qzfEMDLaDK1vaelMqSfebyCsQEe0Zuv1oTzan0xI3zTnAPX_4TEIIC7Psx3pvbpoR03rV6bVUNYIQZ6NKXc7QfTWn3XlurUbkrA7ebJhHFOtRUOJPNG1pjr-N2jHGvPYkD65V1rXgdM9-YaDhKgemIwDwiIOGiFpwn4j6cvXtAGQrKJxf8wIhRmj_MG-FHDL3_uRoqQYXw5P0erLyGXyEJiZIsZc4GulnfY8M3buywWd2QZjKR9t-GyXfz-2foHKerH-cWgl-q3GXxWniHZkWEKo6o2iFoKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a25fe3090.mp4?token=W8mPHyhHKM4OQzOoSx9Jptd9TPqSFRTJgT1Wr9BktHte7Om-p3on_Eu7eeCyhMt76myPmuh20TXqSnxD3I3vMvag1_xqFoKfXGUuGkUTwlWLNm1oOmrRWQSqagCn3RziG2ai9kGDmXrwqA44a2GVIcM77a6SuV5IyQNNIMbXHNowwdHmAdOl-BKEhFdqsNqQGeiWELqals4C3puc2AkCDa2V8CMTRQBQYIuVRP4OGE32csXkWRomJYsuJQmlMnJwjsjAIBMVzKNxqzH-1ewl8yuUQnoe_djymJKIMk_K0iJUf2k3CgoERNbw7ZRVUsEOeo20pygLxKp9a_tHQYcA8yYM0D7dpwKOHHD4SjnzAPmp7tNY7aDb0xLvx-wc2vkkA7eYAr78JA7qzfEMDLaDK1vaelMqSfebyCsQEe0Zuv1oTzan0xI3zTnAPX_4TEIIC7Psx3pvbpoR03rV6bVUNYIQZ6NKXc7QfTWn3XlurUbkrA7ebJhHFOtRUOJPNG1pjr-N2jHGvPYkD65V1rXgdM9-YaDhKgemIwDwiIOGiFpwn4j6cvXtAGQrKJxf8wIhRmj_MG-FHDL3_uRoqQYXw5P0erLyGXyEJiZIsZc4GulnfY8M3buywWd2QZjKR9t-GyXfz-2foHKerH-cWgl-q3GXxWniHZkWEKo6o2iFoKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
یک چالش خاص وجود دارد—آنچه من «پروژه منهتن» می‌نامم.
ما اولین کسانی خواهیم بود که مشکل پهپادهای انفجاری (FPV) را در جهان حل می‌کنیم. این یک مشکل جهانی است.
اما ما آن را حل خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/130051" target="_blank">📅 19:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130050">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbc84ad96.mp4?token=eLA4c_3i5eIw2jGAqm6a96rAgz47VEwgXzk0sQ1OCWd8y9Fgy7VYD2jhg94G7vxS-xeFj_Ja-eFmgnRqb1nZeNeugePd4hVU6niM2Vw5Jcent6ruZM1HP6kZjghKjsIMaVaSm1jHbNLeFCdMWt940bI3FXfpK0HUDHy2icfydhKoLXvT3VEGkUu_-55lPmjCH4hAlKuvw3yoW1ylTJET1n4zQukRB7fQ9NP3RyxOExbT_XHNhVZGSsEggp1pv71aBiNz9zpzCyj65_WxL6I7bI4vNYJF23BRaUERW0ZANk144NTWuV8xRmS6ZDpPrwVUlkjtZ91ELZE2NPlIhpOUFld8a1bfu3PFnllYbWSGrLgAR43giXTJHwMdlNLXmWLsU6nYeTgyRcT4k0KRzDIuq1GD3merXu3LQpSi9feQ3hnBETmK51PT9TWx_1Xpaj9T-OV6LB8A1QuPDBJD20bixot47iP8hbrHpVCEXfKue4goE-_-4tmankMoc3YlyPuZMuIgliHZmURWcHTAjF9UPhJCTCn2v8_PnzF-I_Jcjz_to_ISyVAVvbsL1UDmUseN8gGXqBklK2xlBpnDf8x-c5ik9hOpSQ6HtxILY4bj0g0VrzUzErE9Sbm-vtPjJkGKzrP9LO1C8FSTMuXFMECaVjROuTPEEeY8Oon6aB79kkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbc84ad96.mp4?token=eLA4c_3i5eIw2jGAqm6a96rAgz47VEwgXzk0sQ1OCWd8y9Fgy7VYD2jhg94G7vxS-xeFj_Ja-eFmgnRqb1nZeNeugePd4hVU6niM2Vw5Jcent6ruZM1HP6kZjghKjsIMaVaSm1jHbNLeFCdMWt940bI3FXfpK0HUDHy2icfydhKoLXvT3VEGkUu_-55lPmjCH4hAlKuvw3yoW1ylTJET1n4zQukRB7fQ9NP3RyxOExbT_XHNhVZGSsEggp1pv71aBiNz9zpzCyj65_WxL6I7bI4vNYJF23BRaUERW0ZANk144NTWuV8xRmS6ZDpPrwVUlkjtZ91ELZE2NPlIhpOUFld8a1bfu3PFnllYbWSGrLgAR43giXTJHwMdlNLXmWLsU6nYeTgyRcT4k0KRzDIuq1GD3merXu3LQpSi9feQ3hnBETmK51PT9TWx_1Xpaj9T-OV6LB8A1QuPDBJD20bixot47iP8hbrHpVCEXfKue4goE-_-4tmankMoc3YlyPuZMuIgliHZmURWcHTAjF9UPhJCTCn2v8_PnzF-I_Jcjz_to_ISyVAVvbsL1UDmUseN8gGXqBklK2xlBpnDf8x-c5ik9hOpSQ6HtxILY4bj0g0VrzUzErE9Sbm-vtPjJkGKzrP9LO1C8FSTMuXFMECaVjROuTPEEeY8Oon6aB79kkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
امروز ما در تقریباً ۷۰٪ از نوار غزه حضور داریم. ما حماس را خفه کرده‌ایم. یکی از آخرین رهبران ارشد آن، عزالدین الحدّاد را از بین بردیم. او دیگر نیست.
و می‌دانید بعد از اینکه او را از بین بردیم چه اتفاقی افتاد؟ هیچ چیز.
نه راکتی، نه موشکی، نه حتی یک شلیک.
بله، حماس هنوز آنجاست. و ما با آن هم برخورد خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/130050" target="_blank">📅 19:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130049">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YpcH4NRUK3BRn_ZppsIHltHeN1plXms4OuJDS1oJRwhJJNQdjTcFYBOI-YouJdMT4bw9WFf2GTKMTUWu2dqhp6dZ-v4cVnNumQWhXtuwT8sst5cfVZQ6_laRlmTLsmneIVj1s7QRAMjL30fssUryEHbE1Jf_-ofqpqfzI3PXQSYBga-GNuK6FwDVM_34p5RVQHOWUDOUOjZQZUjfqaQzd1oZxn7jNByM1QHSWccw61CT6NW_cZINhz_Hd8CNCYde74kC31h5cs9LHukKz6vEZ7R-E3FQW7LI4O8DRp_yX_UGGPHEXYBFHf_DCwMsdH5T-zRkDR_POSp5psUK7UlLOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت هر اونس طلا که در آبان 1404 به 5300 دلار رسیده بود، امروز با افت شدید به کمتر از 4000 دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/130049" target="_blank">📅 19:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130048">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
الجزیره از حمله پهپادی اسرائیل به خودرویی در نزدیکی شهرک کفر رومان در جنوب لبنان خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/130048" target="_blank">📅 19:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130047">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت خارجه پاکستان:
مذاکرات بین آمریکا و ایران هفته آینده از سر گرفته می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/130047" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130046">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vu-1rbctnylFAmw1pextHFUjsD2jFp5gBqXXP0-XbMj6Rvul4S90EZ_CJ-eJnVx2CYcq2rWZuOlJDGRNr1mlcO9xUGbRC1RLerp3rGx0hLbI1NqfuarELLt0xvJLF82EyDaFyP4c8fywyuuq3-rA3HNPeyaeyrjqu6Skj_3YNkXEeb9N6ag8REgnh013uwpcoMZDt5bsW1D8bvt-KwHu2hLrQc0h7VSBmT7Tbhwk2ucYg_0kZPNCFIllCxdMcxrMGPtCsCxZ11ozoxHw5GXz28v6bAklnF9G4yU8qXF76IXLV168gPdTfF6pKavNY0R9iv5SWV0eITq0JmGfLyb6eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: داماد ترامپ به جمع میلیاردرها پیوست
🔴
منبع اصلی این ثروت افسانه‌ای، همانطور که در گزارش فوربس آمده، شرکت سرمایه‌گذاری "افینیتی پارتنرز" (Affinity Partners) است که کوشنر در ژانویه ۲۰۲۱، یعنی درست پس از پایان دوره اول ریاست جمهوری ترامپ، تأسیس کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/130046" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130045">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130045" target="_blank">📅 18:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130044">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
تنگه هرمز رو با مذاکره فتح نکردیم که با مذاکره واگذار کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/130044" target="_blank">📅 18:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130043">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130043" target="_blank">📅 18:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130042">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/130042" target="_blank">📅 18:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130041">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130041" target="_blank">📅 18:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130040">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/130040" target="_blank">📅 18:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130039">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWOry3Qx4PoDay0oxcnvxoE96_yPc48Kc3GzDWXy2F-SfUqSusNsnZsPcwcPEM30Z1FnQ6Q4cuO29pNB-2owwR8clVsQT-L8fd2aQkNv0NxjV_TVFjk5s4Nb9YOF0gihP8x-W4ZUu4cnwWyZ__0_Ie2bPZsCySKRpGV0jDMdfxRQ8f-FHmUpP8nTrQZEi05BQsnrbGmDJJJaImtIkCEDrJ7j2iX1ppURlRbjRHFpdxs262ucC7wNesNSrkxMgpznEnN5Bt0wkElm5dqOUaXMnuTMPIoZPWWLnovtVqUAx4rBb9EyF-XynZYgdVvgOKACjBZejfDjnuPRLKj0KfDc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/130039" target="_blank">📅 18:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130038">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز
: اوکراین در میدان نبرد عملکرد خوبی دارد.
آن‌ها هر ماه حدود ۳۰ تا ۳۵ هزار نیروی روسی را کشته یا به‌شدت زخمی می‌کنند.
این اعداد واقعاً شگفت‌انگیز هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/130038" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130037">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3c9d8282.mp4?token=RrREUHoJF1yngg5DOgpYIZk6T3kBFihNuqNmtE7LHlctlBoBHIUM2tLERqXQRoxkoBwx9n6riG-EIYUBiddtflnngx8FJ009yrwRJ3pJFH5bSKPqu6NkEBeTBUsu05Y7JKskowVqiRlkw0jd5SCDdfCuFN_oEZR3j_HwqPyOQ5JBo6GUQOqbDE7RVA9d-fevlc1lYXoWtJ-LW2J5dUB35im1jlBNL3pEk2B2V8QKSmCOKCxrrr12uSEIsQ6s9v4PUOu5aqGV5ar2Uu9BR9tjRQjlhKMWVuiY3OrE6-xqCTviKKjSWHGgteGYyLQ2aK43izao7mwIMF9A7WNdUMWMk4IJPD5dv0PqT3A9HM8baES50x23rc5gwwzaBfExqn1DqVsgJSyvo4XQLN5MNDjlI3-KEZLQwtH-WSuwS6aSbDbdBFgKspUahX-zM7lWFqpOENIow3TvxkvnStG3-LqMS2XuAMzP_Ujwm4RocThDKexbd79uckaPmDtz52-m3XPpW-HGAYcKM8ULiegm9Ba_vpeSiAM68zmi0-Dr7cbE-ghz6LmjCBtl2en8RGCbNzIG7HOZPihd89dOJDBB5wOPjyTT6QY5PjnLkOvQH_jBXrdriZh9t9VZbG7PP5xl41OOSCLOYxa_c7D2J8zL2TIvhrKyWEUQ7bg_BnnSQJhv3VE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3c9d8282.mp4?token=RrREUHoJF1yngg5DOgpYIZk6T3kBFihNuqNmtE7LHlctlBoBHIUM2tLERqXQRoxkoBwx9n6riG-EIYUBiddtflnngx8FJ009yrwRJ3pJFH5bSKPqu6NkEBeTBUsu05Y7JKskowVqiRlkw0jd5SCDdfCuFN_oEZR3j_HwqPyOQ5JBo6GUQOqbDE7RVA9d-fevlc1lYXoWtJ-LW2J5dUB35im1jlBNL3pEk2B2V8QKSmCOKCxrrr12uSEIsQ6s9v4PUOu5aqGV5ar2Uu9BR9tjRQjlhKMWVuiY3OrE6-xqCTviKKjSWHGgteGYyLQ2aK43izao7mwIMF9A7WNdUMWMk4IJPD5dv0PqT3A9HM8baES50x23rc5gwwzaBfExqn1DqVsgJSyvo4XQLN5MNDjlI3-KEZLQwtH-WSuwS6aSbDbdBFgKspUahX-zM7lWFqpOENIow3TvxkvnStG3-LqMS2XuAMzP_Ujwm4RocThDKexbd79uckaPmDtz52-m3XPpW-HGAYcKM8ULiegm9Ba_vpeSiAM68zmi0-Dr7cbE-ghz6LmjCBtl2en8RGCbNzIG7HOZPihd89dOJDBB5wOPjyTT6QY5PjnLkOvQH_jBXrdriZh9t9VZbG7PP5xl41OOSCLOYxa_c7D2J8zL2TIvhrKyWEUQ7bg_BnnSQJhv3VE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز:
۵۰۰ هواپیمای آمریکایی از پایگاه‌های آمریکا در ایتالیا به پرواز درآمدند تا از عملیات Epic Fury حمایت کنند.
این یک عملیات بسیار بزرگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/130037" target="_blank">📅 18:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130036">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95dd83e81c.mp4?token=AsPraGxAGnlqJGE5qU-57zAiJTyI4bOUe7osjJBuktFgzTR3VaOb9K_hNAolXSs9VBYtlAL3c_326_qOaZOXxRxM2NUlzVFPyXKppmv8hmhDDIhof-NUBWPFBTz_rXTumb4qjIeMhdTlHWSMLq8z1IEp79HRGMjIvY6gUo4zLIs8se2xuVrRczf_vbIVWtbyN7nZbEshVtmUBjOEXbNWpqSzF4e-my4EdVUINIRfYaJwvzFzFc5EHTCE2NtSzIZGA_465CW-0-AqXuelb2DgIITBlZsEWRIfAVqDaXQYjelSknZpL4BMN_Y5qNsRb5xSr9I3CwQ893cZwnScKAOqXnxSHkx264Ei2LHqdShicmAukFAS8-kCsJNyGEPx2YMp4d2pstYwgcHmfJLRdv278u5KSovrSZhtzB-J2Y4koiHy3gYfuh7qX8EmrvuxI41egZW3aURKCKEandJJxar1K36MsoPfHigTdqQ7afNy7q7z0yqLRkmnWG9VTVVRV4mwNbrkXv3dH9vwZ_7IzgI37L8e9bYNY4KCPszJ0nSJ_7AGWm1vSDtZgTe2GxARkVBZAQ5OwIf2ZSmUW74kr8Nr-rizVvksPvD-B5yCPMRhkCyVv-797hY3WfuEaCtLHwOgQJADRDXyG6WalypuZyIJ76Q6aiD3WPHMweoaZrxRd_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95dd83e81c.mp4?token=AsPraGxAGnlqJGE5qU-57zAiJTyI4bOUe7osjJBuktFgzTR3VaOb9K_hNAolXSs9VBYtlAL3c_326_qOaZOXxRxM2NUlzVFPyXKppmv8hmhDDIhof-NUBWPFBTz_rXTumb4qjIeMhdTlHWSMLq8z1IEp79HRGMjIvY6gUo4zLIs8se2xuVrRczf_vbIVWtbyN7nZbEshVtmUBjOEXbNWpqSzF4e-my4EdVUINIRfYaJwvzFzFc5EHTCE2NtSzIZGA_465CW-0-AqXuelb2DgIITBlZsEWRIfAVqDaXQYjelSknZpL4BMN_Y5qNsRb5xSr9I3CwQ893cZwnScKAOqXnxSHkx264Ei2LHqdShicmAukFAS8-kCsJNyGEPx2YMp4d2pstYwgcHmfJLRdv278u5KSovrSZhtzB-J2Y4koiHy3gYfuh7qX8EmrvuxI41egZW3aURKCKEandJJxar1K36MsoPfHigTdqQ7afNy7q7z0yqLRkmnWG9VTVVRV4mwNbrkXv3dH9vwZ_7IzgI37L8e9bYNY4KCPszJ0nSJ_7AGWm1vSDtZgTe2GxARkVBZAQ5OwIf2ZSmUW74kr8Nr-rizVvksPvD-B5yCPMRhkCyVv-797hY3WfuEaCtLHwOgQJADRDXyG6WalypuZyIJ76Q6aiD3WPHMweoaZrxRd_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز
: می‌دانم که درباره ناتو انتقادها و نارضایتی‌هایی وجود دارد.
اما باید توجه کنیم که این موارد، استثنا هستند، چون واقعیت بزرگ‌تری هم وجود دارد.
کشور پشت کشور، متحد پشت متحد، پایگاه‌های خود را برای عملیات Epic Fury در اختیار آمریکا قرار داده‌اند.
هزاران پرواز عملیاتی از پایگاه‌های اروپایی انجام شده تا از این عملیات حمایت شود.
بنابراین اروپا عملاً به سکوی پرتاب قدرت آمریکا تبدیل شده و امکان اجرای این عملیات را برای ایالات متحده فراهم کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130036" target="_blank">📅 18:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130035">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acce89e784.mp4?token=r5BOORIgk23xItBsNkENfthAfvprmsOU3UH48QGIzM9ow_EJCvqGjucYHcm4Aemyo6lF7T4oUKbMksZS157orD0pqPa365-ZLshrCG5PXJsVlvqR5LOu8d2cDX8x8j4kVWNdABkBRGLG6YjFOEj_gpgULXUnNYuhc07fm9tahDNhcMI0454vBol6NILXCZaQpGoRrYKWBsAYQzM5b6COdIzkf9TCTL5ckRb5a3DISj-tRmgGRXUCUQpt8e4jMndzt7IaCfPVFnKvMo1N6tLIuk5Mhd6fcEzq0AcbgYdxCJ_A17Pl0P3ooxfrfz2541eUPn9mmWs3tcw9IihqF6MYCHeoWTh515AV0GHRO2lr-i64M3qDpjPluEWZnQ5myNSxm0dngzwLFuao7vhwxiD6vvwQxxQrPMo0v-BJFYHF8h7HJesqdOLCUQGmDqp1JEWMnzytgrIKkNKzVagXQdN2uU8uujpMlkjxacaxHfNDBEqSPPJlGDbh3MPy686lqjk7q54e2NtRDhmLgCpDZcZuXqYjq6ASOBV2kYR62dLAOv5q6P8btskKvXtcx3RyVBmOJkSXJHX4jUgKpW09zO1ere_feCEi-8CzCgx7jA9KYdveeUL6Slf_gYqqyrQrvv0EqDb9ur1_IZfXC8-IrIjNJjDLFPz0qwQGMXUQthdngag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acce89e784.mp4?token=r5BOORIgk23xItBsNkENfthAfvprmsOU3UH48QGIzM9ow_EJCvqGjucYHcm4Aemyo6lF7T4oUKbMksZS157orD0pqPa365-ZLshrCG5PXJsVlvqR5LOu8d2cDX8x8j4kVWNdABkBRGLG6YjFOEj_gpgULXUnNYuhc07fm9tahDNhcMI0454vBol6NILXCZaQpGoRrYKWBsAYQzM5b6COdIzkf9TCTL5ckRb5a3DISj-tRmgGRXUCUQpt8e4jMndzt7IaCfPVFnKvMo1N6tLIuk5Mhd6fcEzq0AcbgYdxCJ_A17Pl0P3ooxfrfz2541eUPn9mmWs3tcw9IihqF6MYCHeoWTh515AV0GHRO2lr-i64M3qDpjPluEWZnQ5myNSxm0dngzwLFuao7vhwxiD6vvwQxxQrPMo0v-BJFYHF8h7HJesqdOLCUQGmDqp1JEWMnzytgrIKkNKzVagXQdN2uU8uujpMlkjxacaxHfNDBEqSPPJlGDbh3MPy686lqjk7q54e2NtRDhmLgCpDZcZuXqYjq6ASOBV2kYR62dLAOv5q6P8btskKvXtcx3RyVBmOJkSXJHX4jUgKpW09zO1ere_feCEi-8CzCgx7jA9KYdveeUL6Slf_gYqqyrQrvv0EqDb9ur1_IZfXC8-IrIjNJjDLFPz0qwQGMXUQthdngag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز
: فکر می‌کنم ترامپ دقیقاً همان کاری را انجام می‌دهد که لازم است؛ یعنی تضعیف توانایی هسته‌ای ایران.
می‌توانید تصور کنید اگر ایران به سلاح هسته‌ای دست پیدا کند؟
ایران صادرکننده آشوب است. صادرکننده تروریسم است.
این مسئله برای منطقه فاجعه‌بار خواهد بود و برای کل جهان هم فاجعه‌بار خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/130035" target="_blank">📅 18:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130034">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgvcoenvQlQTiTFthRzTIrSJaUOJqewwvTZG33EmnOhft6J6fsNDUzSIAK5gdk5_nMSk1JNCPf9t1EPGGai82Y3GzHhrijZ0m7kEJ9Up_YkIRYLYEPJv3uSo_m-jvekYlG6n-0USnsXxG3Yt-_HpFIvGnI7XdXxj5C03MURP6WWMtgMp30clP4yljw7NsZgCCAGBL6mY35h5PYCZgwsCo-PMaTkdKcjkhnMhUkx7jIOt9k3_ZKFIrBSo7PWLSDT8CzaE8IyPmOhjo1clgHlsLQNVJnDo-K86fuESmBDLur8LKSTRP5CtVlEIEQ00QkAQUfIEhauk_AVpr1NXkRwQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ
: کنفرانس خبری و مراسم امضای مربوط به مسکن که قرار بود امروز برگزار شود، تا زمانی که قانون بسیار ضروری SAVE AMERICA ACT تصویب نشود، لغو می‌شود.
من این موضوع را یک وضعیت اضطراری ملی می‌دانم.
از توجه شما به این موضوع متشکرم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130034" target="_blank">📅 18:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130033">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCrrLFprbtpln7BiaSACkO3O073-DigQn4JExVadCqb-T7pzoMtaxMmDKMzQp8nNGiPzOzGo71HHU2fZ8WwQ-o0t3iFaDc2sZ8y4vOtdydy7jB3qbgEQS6wGg-L2uofPLRRszPFlo4Gz_A4eHXlkMj9wSFWD0UwHQAuLmCcIArgzopK2Zcifbvn4OfT072X-VCGx9-gPco6UmNNv8OlxnAGIMkcUOUcLvfFSB16fkgkbdXwkojM1WOM3B_q5CbMJyuBa6jsucq1dCapFtrJiAhbQbfLudj4NOqaXFYE0UsN08XWUojsl8RAN2wRJi1yBYGNTAki1kQkGYoXv8uQU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت انواع سکه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/alonews/130033" target="_blank">📅 18:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130032">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gusq6CVou8G49rtRFE3eqBEQ-Cbbl4nKOihKVD5rXWnW1xKam87h-1om2Xi4JbTq0-N0PhyZskQ4_11DgOlcEdIXHiY5VHTMT68N8IAe6_XXAcBuhwZfWF-q9mRVsPW5ov3wghChlmN1TmnsGql-rX1VF8Afzn95g-QXaby1Ad46w8uVBrMRFj4r01rSvdVCtfbaY--xiHiJQ_mSaoMm-3fTonwMNSY9dCf7AeZXvdMnhy5Dl-yXe6ae69Bsv4fLxlAlAt_7382rItmREkVdns__TR03pvicECtQKKlVW2ZqPuysdZGnqQDD3uFsBvpo7bT8aG1nQraJiZ8h4nLTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت طلا و نقره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130032" target="_blank">📅 18:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130031">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Db2KeTy21zmF-tJHsPhEAnqss-NT9FPm-5syWE0VDFSo3XV4XqCiFWnFfAiei46EAtK06nuG_MBDxdh7z5M5XeH9_U692hYS654ZDI61I-vSu710N9GfxEIegOA2VYhpoqJGO18hnJ4PF5ukEyv37zvUNR0nxlAsPFeoOIyRSZCjYdDfNjprLYb69L1v9o_r3Z1EQlDrrRieyTpt2R0pNqGyHpuCdaav6tqKi9kC8fk35FKphWrzgJ2G1n6tOHhF8iXlGV2Jj65XggCEZCihB0OR9ijISl7fOWUovTDx_PNk8vAtMX6TwzTCy1kxDgWa72iLejSjO2dIukl0oEDrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت انواع ارزها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/130031" target="_blank">📅 18:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130030">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
جاده عین عرب به الوزانی در جنوب لبنان توسط نیروهای ارتش اسرائیل مسدود شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/130030" target="_blank">📅 18:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130029">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdVCqr5OT7ojg3-KRshQJGc1HpyRfX_qu7FsS6PlwBVDhYbT_CAKHE_rFPGJomSAWxZbA8EqwSGhME3Q0fR1wHhsUURpjDgCpWBAFlIICmtpj-PkRL9M2XIB9NXgeL3shqOgbzDwHwJD_PzSHN7ZEsAt9PgNale-8gEmU3ttElXbhDGV3VntaXrWTvRyqNUUBMg_fJ9jo3nGZZ8I49tsOUhchdIs7obyRLNgoSsRlXocsa6IDVOW_2BVur3xErXblZZXiQreg_U5BmFa2lf-u_5DuzS9EH3TQ_95GEHct1UBFcWKOUIkoEHrz9dYTV9Pf5z47DHE6je9dmmiXGztvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شماری از مناطق گردشگری در فرانسه در سال‌های اخیر به گردشگران هشدار می‌دهند که اگر با بالاتنه برهنه در خیابان‌، میدان‌ یا مناطق تاریخی شهر دیده شوند، ممکن است تا ۱۵۰ یورو جریمه شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/130029" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130028">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUjfVRUtr-2zp-mJACar6XLjek4Tn0ovupugSVCNHIyba2Uj0SjmvbN5LS03fcbCSb_IcKSrsvCuLnnJNRnECGfJ-sFOwSokKc0CkpCxKVl_Yc_xcnmmXvhn5kVTq5jFwFZTUKt5X5Sw-4Ev1GuZV9qMePfTDVaoCFdxGq9w5xP1ZpBAkrlmC6t1Ko5n9CJz_PfN0KrQW3c4Q9uXWJiiE4HPW4aTDA-QYZYbWAvilXOQJo20ErNWwUv7YfUx9sgFd__1wUUQi1fb17nCexH83lUlpA-mk5qPewShZTvMPw54MnPcRo3yx6nkRpO-iIw2pI7tmLTDrxJbMZ6bsXENJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کامران غضنفری، نماینده مجلس:
دیدار نخست‌وزیر پاکستان با رهبری، برنامه آمریکا و اسرائیل برای زمینه‌سازی شهادت ایشان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/130028" target="_blank">📅 17:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130027">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmoeTRvsAqwkcCxVHVN6eMilU_41CFxIcQrApkuJQdRN59lSgp9kIuSvXn35nDtFrJqkhOTI4IdwdmHB-gnqz9caGb0_Bn7cNfPyK207WlvUud6Y-OuKTfchxCpdCrh9FgXaLl77AHD-vxfA99aUzTkA-H3hQPDE1iA9zDFfmljr0r5q2PtI1qOYi-3FWFpLEQGHPuXgNijwX8ANI9vx16dEAJnclEg1IiB850wWjlkIkOxYXfcwfNBt9xPQYQvRA7IHFbTlm3lgMlfMrHRPZsSuRGM-wa1FLxz2KTZP28WT1ygk_v6HPRyu-WPcUaIWTADhegx2tOaP-H4mpSIX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: برای دسترسی به مواد هسته‌ای عجله‌ای وجود ندارد، زیرا در پی عملیات «چکش نیمه‌شب» در زیر زمین دفن شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/130027" target="_blank">📅 17:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130026">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYna_WYzDDLmFQpc5hnuaXpq6ow-UUYDQE5vEM580eWrZStNeO6j08wrXIZ8If0mZtaofF9rCwvYmrzzlMRWTem9vxkHWonfPWBYe593C3M4UDhyKWvkHO8fxnrR0FAdKzQg7FAZgiZjV9HOzsV7sJa1sn3M8ymvuC-ekMCJgFsiAgvjPgNcUDo2lFWwKkYWS_uyRpH3tRSOHZqkS2oRP-Y907UT4AC9OicpJY71ctEsl9pmr-7VGtIhQ2CUKCaKky-2F89JI8ASAb5FunXiBJfNnpTfmVv62spgyLryIjCUx5W56dMcZO24zu-7Dt88xLCMscMGXVKmTyiFVMDRsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ایران و پاکستان در آرمان‌ها و امیدهای خود اشتراکات عمیقی دارند؛ تلاش بی‌دریغ پاکستان برای گسترش صلح در منطقه ریشه در فرهنگ غنی این کشور دارد
🔴
در سفرم به پاکستان به منظور تقدیر از میانجیگری‌های پاکستان، درباره گسترش تعاملات با برادرانم آصف زرداری، شهباز شریف و عاصم منیر صحبت کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/130026" target="_blank">📅 17:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130025">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2T-sCj5bOzBZ0kl8UQ7yboX8oOkzUdJxRkXxJAIpQOQgpVub5vk0wl5Cx8yAbUdL48OALr756Pf5Ol4CYNc5O2lytHssucifPjk2drTv6I2mElX9VmYnAmRAmH7bU9IL0Mw_fIRRGa2ahwRoCZtfyYRQrQD5K2VclDV6D4X8XIxUt-1nAGCFMWQpsL8sv6i3iBPMEpgCJgu4NrEIkgngujM6zqrT3lTnEA01WNGzc6gc9ymF8z1l5A2UejpqDubPzjJrCnEgRJfhCE4LtmDpFx5o4QXxqp8fNPgs8P5x2sw4XNNbQIaSvK1JzkjnJ4GhKh0tXR9QPCY7jEFCeMFJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
رای های من اکنون به بالاترین حد خود رسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/130025" target="_blank">📅 17:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130024">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa7u-noVoZG07qt6Uny9R9nwHxba-KQiyyUXfErkJ9-D5zNiLAgkiD4kygPwQ1HSVSie7oYrEGIzwowzzQP1IajzSQi_BaePC1UFJcI9R1BEA5xkQiek4x3kc-dAdrdk1F194SUL80MV4Q87TELyy_PrXyuTvdnRfCknw-TIkwwbGwaRgkEyt0oKwaGE5YJMYBN2_XOlpb4I8FvR7KK-pnS5RxicCk0ZUa0gZ7aAzcKsM6sXi2qkFNOLq60aTEH_uR092n0skzVM6OqG2mhqeqOM6JOeXARfOM1JTcvAhjaieQxjdo6wEaykYrFDWwhKRr6o6t7giQnZ_Eyi0iCaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت ترامپ:
شهردار ممدانی با حمایت سه کمونیست تمام‌عیار به پیروزی رسید و رسانه‌های جعلی هم با سروصدای زیاد و به‌صورت یکپارچه برایش کف زدند. تبریک آقای شهردار!
من دیشب ۱۶ برد از ۱۶ داشتم و به انتخاب میهن‌پرستان فوق‌العاده آمریکایی کمک کردم، اما رسانه‌ها حتی یک کلمه هم درباره‌اش نمی‌گویند.
در دو سال گذشته، حمایت و تأیید من باعث ۲۵۹ پیروزی در انتخابات مقدماتی شده و تقریباً هیچ شکستی نداشته است، با این حال هیچ توجهی از سوی رسانه‌ها دریافت نکرده‌ام!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/130024" target="_blank">📅 17:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130023">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
مدودف: اختیارات زلنسکی مدت‌ها پیش منقضی شده است و این واقعیت او را از هرگونه مصونیتی محروم می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/130023" target="_blank">📅 17:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130022">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC_TroEkRpL9b8x7JCZH72ef1hpGvNVJ3CQPsjr_The5k_13aV6aosF8yB7p2rD97u2hury5tQ2wwr76eQsI7UDoSAnmWmx-4lgyprV-MQOnCXU9fr5R38OF26rI_KF5ga6MHmf3_osGjbj7GTUViHiM6p09yXF6tyfInYfW2lYdbkStv5flaQDZr6ePRnvj_zGmFmmIxt0y9Co2ttm6AKrH5BsZ7ML_-SfRwQaeDpz0wzMZRkN-Blmi_xeMW8aVgXtrR_DLIGHZklXRwokUtWW8BcHHE85uhNW9nfI2kt0kJ-Gf3PzmTUCCNDt003hdVEbUhD5llljQAgNzQptWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تو این مدت جوری پالایشگاه‌های روسیه رو زده که نصف روسیه درگیر کمبود بنزین و گازوئیل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/130022" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130021">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSUYQdc_oFCbE_uCn5SsUcsAhEao1OeVPfNeomysAOPtyPrV4dixy2CrqaaYZUetAt96wOqLqllvM6O87gp9WloGmVeAeOc-HwTYbKQSyGfsgVKtgeICFA7w4-FDzWhNgW_eOfIkB4sYBuNrA0kmgiSEpwHIVaFtSNWISatab_W4DimyRZwNrt4de-0dfnmZYnkGC-fM0xqwYs-xy7f4y1wXY4lx9XHivR6aFltXPWjjvmN3QBbzgcnk-GW676UA9kWfpBn03-9tc2U_WAr8qf0TZXFj0WVPF3Gb2wvIwwYJD4YZ9V3qmCmya_yUKq4P3n4l2RRROxpPTE4XcgRmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده روز چهارشنبه سوم تیرماه اعلام کرد که مارکو روبیو، وزیر امور خارجه این کشور، در دیدار با شیخ محمد بن زاید آل نهیان، رئیس دولت امارات متحده عربی، درباره یادداشت تفاهم با جمهوری اسلامی ایران گفتگو کرده است.
🔴
بر اساس بیانیه این وزارتخانه، دو طرف در این نشست علاوه بر بررسی مفاد این تفاهم‌نامه، در خصوص تضمین تردد ایمن و آزاد شناورها از تنگه هرمز و همچنین اهمیت حیاتی برقراری و حفظ صلح و ثبات در منطقه خاورمیانه به بحث و تبادل نظر پرداختند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/alonews/130021" target="_blank">📅 17:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130020">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUTmf3BDDhFk9agLCcCzrMgrn-2HgbruwQZeQNsz7HQKXgUdXj4GqWeZo3k53vphXmKLhQxVTwFpehNnacgYPMpySP25vN8bsO713Pzf7kiItG-KCsz0dbiHJK6Z2x-QgWexTcdqdhAAKCmoGljIVwimc5x355IXz70QYkLZ3EM5Ni25rYEu5jBVZVwYrRwAAIPbz2pomQRl_vgGASQK9SOdcd8iYRlDdkyGFDXRyykTWT_7nuZlgVW9SdfNGK7rpud7hi8s_faw0oHGRUsm_pBv1PJk5vHYNPDL9UgPOL5wA0_RyBjuXduFilNBi9b_JtIhfobmxOswzr-N6NdAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط عجیب طلای جهانی/طلا به زیر 4 هزار دلار رفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/130020" target="_blank">📅 17:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130019">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFKPpYMBxjlJSAW1BuFA9XIWBdtsR0gI3uqA2-LgxFX9BupBntbvsqu7RzJaoLUXw8Q1m00g7xx7tKgeg8GgfSBj_QhMpzR0wmh4mYzX3u4ne0z4loETNP4OT2ol8N5K-PmT2JnH6DOUL7W4IvT0s5RWaYYPYGhfSJNI7T-_LpaBpgu2BKG2pfkGE9NztXhBNoLbNLr9_Jl9PXTHGOGXHpu0UmKWbxWE31Aw67nmFdcZMAPI7qhtXh5jr7Zy-ZKdUZW9_sTjjfU5hFkArcSRC4lHEL9HGQP2HZ7Og1iEAcMlLm9N4-uigublIDmuk7nb4vEi85jR4OMpLGTu_-0TLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قضاوت جنگ صدرنشینی گروه K به فغانی و تیم داوریش سپرده شد
@AloSport</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/130019" target="_blank">📅 17:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130018">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db753fb80.mp4?token=N4XIv1bw2gIxTh2rk_-us-_5RlgErAFWrsYQZXof-6Bu_dkxgfZq2_Mu5nOjbieTjGLWG-aC9wq_ayo0Q7p-CAgAyKutkfsbRTz5iIE2NCo1g7D2X7KmhXhi4A8yiUhW0FxGlBoINScFwwpcLf5HD_dOD_TNIsNEBP2zHzancFClkoz58uA3eZU8HzErLw6DJ2Bi5xfKt-pnLppI21rdvTNC_X96BAMQHmumQL-q2YzoLuQiYlfev2gt-vll_e32ACZaV9eZY4oQj4oawb6OOTSIbQ2uTvt71w99_AbD033cfzKBrOveTDixIH3CVzUfOKNH0yAbxgPXB69JrQss-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db753fb80.mp4?token=N4XIv1bw2gIxTh2rk_-us-_5RlgErAFWrsYQZXof-6Bu_dkxgfZq2_Mu5nOjbieTjGLWG-aC9wq_ayo0Q7p-CAgAyKutkfsbRTz5iIE2NCo1g7D2X7KmhXhi4A8yiUhW0FxGlBoINScFwwpcLf5HD_dOD_TNIsNEBP2zHzancFClkoz58uA3eZU8HzErLw6DJ2Bi5xfKt-pnLppI21rdvTNC_X96BAMQHmumQL-q2YzoLuQiYlfev2gt-vll_e32ACZaV9eZY4oQj4oawb6OOTSIbQ2uTvt71w99_AbD033cfzKBrOveTDixIH3CVzUfOKNH0yAbxgPXB69JrQss-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از حجم بسیار زیاد آب رودخانه سیمره در شهرستان دره‌شهر ایلام
🔴
نیروهای امداد و نجات هم از پس سیمره برنمی‌آمدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130018" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130017">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6001bc8d37.mp4?token=r62g6-86bk7iG5ghxcjlbq9gz14Muf62Z07770AqBwYrBoYIMCvVqGKq8vi65BglPHf0I7OsILtfTdff2jLWw8giezZH-IrNJgG9owskir9F3w5WUUvC0LicYY-OkvCRWSzhGd8bwg2hwHG-m2ZIUOiNRsFpELRZ1muwtBtprdLSawFL6M6PhuSgIYEZJODDsFFkEeAwk4ZhHelVd14p2Pd_cqZv7ZRp21Y9BrrpTnDtp_xsMgzBhMPmqb7dcRjLWIjdlch04gQb0hbC5MIPQqqW8Zn6eW9hbMdWxGF26oXrEUu9WpO9S06iE9dQmfXvriZIv7vRbbB7eBLLB4M4JYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6001bc8d37.mp4?token=r62g6-86bk7iG5ghxcjlbq9gz14Muf62Z07770AqBwYrBoYIMCvVqGKq8vi65BglPHf0I7OsILtfTdff2jLWw8giezZH-IrNJgG9owskir9F3w5WUUvC0LicYY-OkvCRWSzhGd8bwg2hwHG-m2ZIUOiNRsFpELRZ1muwtBtprdLSawFL6M6PhuSgIYEZJODDsFFkEeAwk4ZhHelVd14p2Pd_cqZv7ZRp21Y9BrrpTnDtp_xsMgzBhMPmqb7dcRjLWIjdlch04gQb0hbC5MIPQqqW8Zn6eW9hbMdWxGF26oXrEUu9WpO9S06iE9dQmfXvriZIv7vRbbB7eBLLB4M4JYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا، بسنت : سلطه دلار خیلی مهمه
🔴
همه کارهایی که ترامپ داره انجام می‌ده، دلار رو دوباره محور تجارت جهانی می‌کنه
🔴
تو ونزوئلا و حتی مذاکرات با ایران هم می‌بینیم که معاملات قراره با دلار انجام بشه
🔴
در کل، همه این اقدامات جایگاه دلار رو دوباره تقویت می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/130017" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130016">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/px0plryF_U9qnMVsu_E-zrffZ3C5kfhaksmrH2WsH8sF7qphwhANJjdQBsY7_ytERso5fuXSNNDbg6DDU9jGaFHCV0pX1GfdY-triO0A_r6Ja6U7Aw5aJf7jGF-l_kZ3IMwzhYxa8FatHkdSQyvn4tDmPan4AIdng4ouSX85mihehW7pHPqwKPoukfA2J-VvBvXBa8VjDot-QAPOoOaqGW4jYAmvgmietmVyLwIDjeU0dy8sMa0KJ0mM3VqGO5X9zsDKU7EXULrOhcvop81NRuFNfzfYHDwirbPvNLxvJPvMZKmya383ZDxbEXHJFeKN3UWxq387q8w6umA76K8mLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت آمریکا به زیر 70 دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/130016" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130015">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
یک دیپلمات آگاه به خبرگزاری AFP می‌گوید که مذاکرات آشتی کشورهای حاشیهٔ خلیج‌فارس و ایران در عربستان سعودی برگزار شود.
🔴
این دیپلمات می‌گوید که پیش‌بینی می‌شود نشانی سطح بالا با هدف ترمیم روابط میان کشورهای خلیج‌فارس، ایران و احتمالاً سایر همسایگان منطقه‌ای در پی جنگ، در ریاض برگزار شود، اما تاریخ دقیقی مشخص نکرده است.
🔴
او می‌افزاید که این نشست‌ها مستقل از مذاکرات جاری بین ایالات متحده و ایران خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/130015" target="_blank">📅 17:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130014">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjBK61Z7Ej16tkn2pnz1pWGhMPRT5j_kfCrjr5aTIRDkdzjxtGf01glQ2TenSK4dZZhrWJut--ID9oAcOxxrT5OrJDTieL6ZdXUvvjePN6zY2gD8S7DRjZ36kC-OqNfmpAS0IMbTEHN0M7Mxg7O3AsL7CEpNlvOEWY_PaBPtFK0TghD15y2MC0LXmmXvb4NQ2cL-pvhSqp5RlWhCLXKdy-NTTJE_5Xdl7-we-vOPolNFEJHZl4ZVbtqy8ceK4ewXaB3erLVmw2x8aTWSBys0XNNxabidB0NBUK056U9uuXxwonWPyHQWFSdNrat00eOx-Pusteny_1MC6iTl7l37ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکسی از اسکورت هواپیمای پزشکیان توسط جنگنده های پاکستانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/130014" target="_blank">📅 17:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130013">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTGhP26m8GW0qVLsy7SoaabX_9ZX2Mun-mGGdVvvnFB2PU5PMelczJfvWf0mfPIVfxvocnJTc6s6pOhBpm4XfxAhjXAUVgE81t6AiVrYBm_WlK8CtTmHZP6pn9C2Ts0Tt1Qyz62KPtDS7hYt4E-cX-_MjaHu71pAi2Jxz1mKUIAVON6VEhxaE8jwHGKKPTaTYM9dNR2QVShPt0H05SuwuCO_0IgkkalRlBVRxb0ahxHMQL4PXT6zvgnSoH7KAmtGVrqjWIo-j1K0fDf_DMDuAs8hayHgydj6LZDAIblu-Zz8euv0IGyO-DTEEsmWqg8wBd4Z9zC-G9ZeZVY--WBdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شواهد نشان میدهد مدیران دفتر انتشارات مجتبی خامنه‌ای دقیقاً امضای ابزار یکسان ، نسخه یکسان و سیستم عامل یکسان دفتر انتشارات قالیباف استفاده کرده اند.
🔴
در‌نتیجه هر دو نامه قالیباف و مجتبی خامنه ای با یک کامپیوتر نوشته شده در ابتدا و بعد از اوایل ماه ۶ میلادی، اوایل خرداد ماه، رایانه را از مک به رایانه ویندوزی تغییر داده‌اند.
🤔
قالیباف همون مجتبی خامنه‌ایه. خلاص
🔴
حالا طرفداران بیت رهبری محکم تر بزنن تو سرشون
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/130013" target="_blank">📅 17:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130012">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc80afd3b.mp4?token=Q7SOIqYwdQEASwyQYSGEzDRVIuE73CyhSHNiE5UV08o5C6J4sEA0ysJi6mwMb4EjE2_SDdBlWD846MBOh0q3km0LQeDL3qDrUphwy6eOwBwEz1rfuoXrcUCR_hUPqKRX1o8jerfmh0IxsMXrmh0aeLLrNGCNKZ35dZ42jDrRLXBjbSUfWfLxrIZ_xbi3qAl0frqlWGaGEwg-JTHK8BTviQqQdDbwZce6QAQib7qTpzcnTGBxl2R-g_YxRq6GjEaTKMSnHsjBIm3MStUQOWBZfF6WX5XP8-QyS0amvMRdH_KqydMz6umS5covatM7mjWqHzM5swkLf6ImoOpkQTSqDjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc80afd3b.mp4?token=Q7SOIqYwdQEASwyQYSGEzDRVIuE73CyhSHNiE5UV08o5C6J4sEA0ysJi6mwMb4EjE2_SDdBlWD846MBOh0q3km0LQeDL3qDrUphwy6eOwBwEz1rfuoXrcUCR_hUPqKRX1o8jerfmh0IxsMXrmh0aeLLrNGCNKZ35dZ42jDrRLXBjbSUfWfLxrIZ_xbi3qAl0frqlWGaGEwg-JTHK8BTviQqQdDbwZce6QAQib7qTpzcnTGBxl2R-g_YxRq6GjEaTKMSnHsjBIm3MStUQOWBZfF6WX5XP8-QyS0amvMRdH_KqydMz6umS5covatM7mjWqHzM5swkLf6ImoOpkQTSqDjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، برای دومین مرحله از تور خاورمیانه خود به کویت رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/130012" target="_blank">📅 17:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130011">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I98JIi5IfEf-yht2E3trfVyPXpsqBDjdJedWKF1GEYHU2sulIRP8lazuv-8AdAsPUOtUMxXVfMzoHcUKcC6QDc35IUJp7sx8KYLCxKmAN-Dm-obUr3K0vUu44gf2AXlYBB-Lr3PFtjz36pgUbFRlklbp_0pZGMTsuaK6kDirrflq9Ap5qMsXwWYQsuiTy0ukcD1beFUDcX_6gYrP9rYCJTu7O5a1v_lzBLEwocAH1yF27OmBRwAlUqV6WVnuMVnM0xEKndtg-nLz9f44utlEI5U3v3Xt2IQfiDCTzXXnEwSiQWZ9OYMG1s4OTAVo4h2Spjtyu29HL1Y7mvVtwlT8qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی کتاب جدید وزیر امور خارجه عباس عراقچی:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/130011" target="_blank">📅 16:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130009">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41470bf010.mp4?token=BtQ72a8fMMXg35VcvKkCHS53AUb9agMXLHRVXtYYpWGSnQBk3quCoooY2TrCZ4rL4mz7pp3NNAdimJZo7jvO9pSajBKXlL_EbGkiYFr-8kfeo-tg4LmUsTFUeNuNGG8h7BnjBMgfN0CzEeUNkEXzUkM0389rcc4krgprYTp-kNUpTK1PNvry0-6g0PvRwo553-ElwNDOsWEwC1t6ntXHBrXDEqfRhTANfMvWFHvj8jkVh3me8OHJ_yXr7jnvdRoUUI5iC8oHXfnGk9SBgwgvEVrS5_RnevSwbGDDI1PQfC72JsfQVTAcbN9Bl0IkTLPDqvk5W3D89Rw_APKwj0oD2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41470bf010.mp4?token=BtQ72a8fMMXg35VcvKkCHS53AUb9agMXLHRVXtYYpWGSnQBk3quCoooY2TrCZ4rL4mz7pp3NNAdimJZo7jvO9pSajBKXlL_EbGkiYFr-8kfeo-tg4LmUsTFUeNuNGG8h7BnjBMgfN0CzEeUNkEXzUkM0389rcc4krgprYTp-kNUpTK1PNvry0-6g0PvRwo553-ElwNDOsWEwC1t6ntXHBrXDEqfRhTANfMvWFHvj8jkVh3me8OHJ_yXr7jnvdRoUUI5iC8oHXfnGk9SBgwgvEVrS5_RnevSwbGDDI1PQfC72JsfQVTAcbN9Bl0IkTLPDqvk5W3D89Rw_APKwj0oD2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عزاداری‌های زیبا در سراسر کشور
از خون جوانان وطن لاله دمیده
🥀
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130009" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
