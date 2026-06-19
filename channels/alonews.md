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
<img src="https://cdn4.telesco.pe/file/cWt925GrnxF4zF43HIMG6F-JqYuH6Z0sAzTmmTaqoXb4CrSNVDqz5amntQOmdLjz8xuCtyorfO32Zl5AeadZ-YmkYx1u3hvpTzKepk0xB33qSgIOc3irTnE9qRIkWZu-obe-qOG0HFTxtncJaoL7xbbg0UxPZg8GXqOYjmtGIVjLr-XUMi-Z5LKqhR319AyEnDJogkFJJfV-BEmEoaF7thlVpR2AYrmGaJVf8hU9MJ7SSBjXQlxEkNs_6Gm0FbiERGkdnQAyapB7PdtdH3kqfV773y9Hh2snooNJVSDAuJ1Atjjak2Rz61WYxxmz_diX-EKUNPCbd5cghMbUib9iLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 963K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 13:44:06</div>
<hr>

<div class="tg-post" id="msg-129109">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ترامپ به اکسیوس: رابطه من با نتانیاهو خوب است، اما باید او را کمی منطقی‌تر نگه داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/129109" target="_blank">📅 13:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129108">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزیر امورخارجه پاکستان: هیچ مانعی برای آغاز مذاکرات سوئیس وجود ندارد و مذاکرات باید ظرف مدت ۶۰ روز به پایان برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/129108" target="_blank">📅 13:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129107">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
قالیباف، رئیس تیم مذاکره‌کننده جمهوری اسلامی: مذاکرات با ایالات متحده همچنان در چارچوب «خطوط قرمز» تهران باقی خواهد ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/129107" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129106">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان: هیچ مانعی برای شروع مذاکرات سوئیس وجود ندارد/دلیل تأخیر در مذاکرات سوئیس مربوط به مشغول بودن مقامات ایرانی با آیین‌های ماه محرم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/129106" target="_blank">📅 13:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129105">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: دقایقی پیش زیرساخت‌هایی متعلق به حزب‌الله را در منطقه بقاع را هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/129105" target="_blank">📅 13:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129104">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ارتش اسرائیل: بیش از ۸۰ نقطه تو لُبنان هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/129104" target="_blank">📅 13:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129103">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
شبکه سی‌ان‌ان به نقل از منابع آگاه اعلام کرد که پیش شرط ایران برای شروع مذاکرات در سوئیس توقف درگیری‌ها در لبنان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/129103" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129102">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2bd4028ca.mp4?token=N31xzFyfrOncev6SN4B7pXnnwjD2-bRyW2vfAEAC2PJbXyK0VQIVpM-dzjv47owkaTcJTUv_Hff7PSe0iug-OXjzarhg4L7Bb6SqPPUq0WQysh91pykxuZj4PyD2OIFfuKMfTrENllo8oD0RW1Z3wg9pcKl0yGiqBHoezjZl164igx-spBgZquWzd5sFNw5dPr3ntpNQIuskmy7-tR43cmmE0z3StTlCA5ovADb544VwwsoDz1m-AnkZ5zYwGFGIL_p72ZcYAULLeXcoi69ro8pedYGErrNovnIqYWoEBcOVaacPRkKXX7vWUiSIoMy4wNQUcAcEt7fNHhSKDISr6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2bd4028ca.mp4?token=N31xzFyfrOncev6SN4B7pXnnwjD2-bRyW2vfAEAC2PJbXyK0VQIVpM-dzjv47owkaTcJTUv_Hff7PSe0iug-OXjzarhg4L7Bb6SqPPUq0WQysh91pykxuZj4PyD2OIFfuKMfTrENllo8oD0RW1Z3wg9pcKl0yGiqBHoezjZl164igx-spBgZquWzd5sFNw5dPr3ntpNQIuskmy7-tR43cmmE0z3StTlCA5ovADb544VwwsoDz1m-AnkZ5zYwGFGIL_p72ZcYAULLeXcoi69ro8pedYGErrNovnIqYWoEBcOVaacPRkKXX7vWUiSIoMy4wNQUcAcEt7fNHhSKDISr6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
چرا ما در سوریه در طرف مقابل هستیم؟
🔴
چون باید آنجا باشیم تا از خودمان در برابر آنچه در سوریه می‌بینیم محافظت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/129102" target="_blank">📅 13:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129101">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c80f50a64.mp4?token=JoXQP90qShE7SWlTaJjt9m3TtJtFnrzDxPy9hHfN4dbdu7UrjjW_Rn1eDujmeYKyYRd4K8Q8fCP404pOKg14okotkViuF3sDjUjXoqHkd3OTP3Qa7NhbMVwJIERcGOAXruHQ2zFcbMeaRyILinRfjOeLKBDiQtH8o7o3SW61YGVAcqYLRJmoYQMsL30ipNgK-AkRnYGLYInmUs1UeFKKuJUWqDRYo8wj7Xq_TqgB8yDFyei73ReHMk5UaeTIZdhhoXhsSRZNamP4GGCMKFAgSz8hTU0jBZjYIuv3P2dYIiVyOQzSfAriXWXFJMHzWhpQrdJ-ig0GkqXVVI5ltAxq0L1yUaB6XM4-IMbeM2OeL3hBwMIERyMvcwZ--SFfajPCPz1IRziiH-3Ge5mexEj4tt7XxeDIXaSwxQebAqaS63H5ZwW7axTbRKRrVU6aqP_Gs6lugayuOcd9td67J3s0eGaJk2gMBcVbINpapO_2afoICDByxmPKMVDH_vMKiC-DANtEYRgq7qwexQ1RDqc_KzzJV4rKuPfun1doYn8vpXy-kee6FxfPw9YVj7oKuF5UaYAY0aLKWEVVSSShzuFsBbtSzkwpAH4IH6JelI-YgTm87ULI41SAlvJnZfYlUomav8nu7fa3RVziDxKjhOxb6TNwGqdBrnbbdgfPiNLzrMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c80f50a64.mp4?token=JoXQP90qShE7SWlTaJjt9m3TtJtFnrzDxPy9hHfN4dbdu7UrjjW_Rn1eDujmeYKyYRd4K8Q8fCP404pOKg14okotkViuF3sDjUjXoqHkd3OTP3Qa7NhbMVwJIERcGOAXruHQ2zFcbMeaRyILinRfjOeLKBDiQtH8o7o3SW61YGVAcqYLRJmoYQMsL30ipNgK-AkRnYGLYInmUs1UeFKKuJUWqDRYo8wj7Xq_TqgB8yDFyei73ReHMk5UaeTIZdhhoXhsSRZNamP4GGCMKFAgSz8hTU0jBZjYIuv3P2dYIiVyOQzSfAriXWXFJMHzWhpQrdJ-ig0GkqXVVI5ltAxq0L1yUaB6XM4-IMbeM2OeL3hBwMIERyMvcwZ--SFfajPCPz1IRziiH-3Ge5mexEj4tt7XxeDIXaSwxQebAqaS63H5ZwW7axTbRKRrVU6aqP_Gs6lugayuOcd9td67J3s0eGaJk2gMBcVbINpapO_2afoICDByxmPKMVDH_vMKiC-DANtEYRgq7qwexQ1RDqc_KzzJV4rKuPfun1doYn8vpXy-kee6FxfPw9YVj7oKuF5UaYAY0aLKWEVVSSShzuFsBbtSzkwpAH4IH6JelI-YgTm87ULI41SAlvJnZfYlUomav8nu7fa3RVziDxKjhOxb6TNwGqdBrnbbdgfPiNLzrMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
یادتان می‌آید حملات را؟ آنها وارد می‌شدند و بیرون می‌آمدند.
🔴
ما وارد می‌شویم، نابود می‌کنیم و ترک نمی‌کنیم. این کاری است که اکنون در لبنان انجام می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/129101" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129097">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLyRYeDm4PG4US-NI9g8NEml9EQegaWs-d8dWvVVF2Tur9Hsnnq4eV_2c0X39j-yufkvVy7vrmMxFHKfjVqvkYS3dwU1BJ5_PHl9jm1zA4d1k2VdARtKSeX2Pitmu8bUaV9Vc-2SNj4HKbZ2FWj67yLgV2-lWJgwvVTJWR0czVnAj1l82oSnjTos9ZgO5JXl4l-S5NZln2rjD-z5v5NiFhrCbQX41BRAISMstzPOUQoer-o2fCKut4AEtoDXbQf_OWbw5QrUOd-tiNyBa2qFtxoh2ItbmTPPwuiMDHMlHQG6Y01xGQLwrigQOV5e4oWNaRDS5vfJTWmSGN_5bKxyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giqU8MHTkGWmUJ3g7AZZ8MVSMf6ye5n_JcL07iHGojwQZ_K5QJzEhklg0ZaxFEFF8IMdzn6P7wiwKVL-Bpv_AfUoxI0qf2FEtgwdze2aa4Ap8JELpAIrvgtwL2wv_YVSFPADuMEgKoA9oVFJhMkzl6KCgP5Qckm1LbTVwhvwb5JjF5yZAe7JRSJ1YtgCEC9HS6useB_37CDWF2gyvEixPbFZhi780qgdCaFDhSpL6NMskpPAI0E2OLD7dsLuyfMVzB3sqbMixaiDArT7hZijxjK5qmwnYi-wpIjcApptD7z0TsYVhFtGh6wVnTxUGSwqP9Xfw4tGBunFjoKhuATsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N77VtiXDOJUC9fV2FQtN49S_LAlslixlmpF_wrZ2FJ-ZyggRqqwtF_YT1AEijETQL1E8Zpy_p6DMuZEjCWofYZz7NaJPjCnV0RZHRWngtIBoDoAkIY9AKYape1OjbkBUk9JHgwVrsT__a4q5xNCO7fnWPXsXl5-cqXiy5dJ-1w3cIWVTEFpdKO_jMUwq09l7xmdvGEjGSLsji8XFm4DVm87hJT9zM6hwZZQk4U1rhRj-ja-q4bjjJPLCw42Qj-UV4n8RmHVVgOqgLLlGMSzRsW2_4dxuJaO9ZwcCizwjvwEssf3oo5Zjqbfp3oTOV1vc9Ndbv4Vb6GAJ5DxkiOzALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuCsy8jd9G8Z3FitXEVWYuk4sTTd1BnRGOFSPfQj0L5-PbdoJB8JeZrbf19DpTa8wGQgkfBCK2Gp1DLldzGg7AbjVKwPLJDWY8Y_MryiVMgc44SQAKxNfQ0cK1N2tdRrf9bC2TNa0HH-zGBrnHqQy2C8dPH_exI1G5tuKs_1OV8qY4mb1pTo4haCBIOM4NWRsNTZZHT5ekYJlV4rwJWS-1jmLe9F5-gs9GCLIulL7yTdK8lVEqfo4vdsZf_CwU7OjjWcr7qHAlrbO_htxICNFMYu-gKvpXRn8E2Bz_UDsR34hPzMShahNkofpTxonjlA14vFCAUDgEUqsCbLOp7IdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات شدید به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/129097" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129096">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
بعد از پیام دیشب مجتبی خامنه ای دلار ۱۰هزار تومان و طلا ۱میلیون تومان گران‌تر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/129096" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129095">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba0R5Bzrx5I9gRN5nGsFsichSxn8PObGJARTGUCOZnKqeUsRSHcT8Vj4-WpDji6WepuItR58B_8u554107jvEJbHWyljo1tJ2-fe02kEVR20NSHksyWefJaJ3aAwHJ8b-EKdwNenjyOcnii7pk2Wc1YKvyRRxfZxmhqMoWkd0mNThxVlZFxpDGrvr0BXvbBgR6CMw9J2x9a61ATSE7duku-zyICo0-Yt1E96qNEXvT1_Hu7lntuZiQpVnM0oLnzqx6xlLQLzIua31FpfMGYckDwq0UfJ8Sct-E0OJG3B4Ab9a5mFiZ4ljaUIgmQ3M17V4exxo8wawxsCwOgSNF4otA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسموتریچ، وزیر دارایی اسرائیل: «وقت آن است که با آتش سخن بگوییم. دروازه‌های جهنم را بگشاییم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/129095" target="_blank">📅 13:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129094">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
در لبنان، ۲۰۰٬۰۰۰ نفری که در «منطقه امنیتی» زندگی می‌کردند، بازنمی‌گردند.
🔴
هیچ‌کدام از آن‌ها بازنمی‌گردند.
🔴
نیروهای دفاعی اسرائیل آنجا هستند، زیرساخت‌ها را نابود می‌کنند و روستاها را ویران می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/129094" target="_blank">📅 12:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129092">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d19bde11aa.mp4?token=lU9oLrZ1hga-xXTPbOBH5MVpv9BJneTXMnuMLuvKKTg7brr0N40J4OGiHQPQMpUu9zXiOla9j5eiMqJZWCrlTrzXFSC07ES30iezTpG27tPTIKbDzRIYst7ixhwgOvNVTuXbbMWoCOhCAt-vDxNQ_3YhPVVj3cUWN1Up6OqSv__Yr0uuW0Jmd2Dai-ysuKbeaZsXaQHdFbYLt0VhRDFiQSnxJjGHgeLSc-q3TT1ogt-6hQOGnEFelWG8QHbPqDzl0FE9OM1GVBTdwqnifmOk4cgXqm2aDy-UCnNsfSKEekNQsH9NmepGiYXh4klU_Nfe3uog1qc2UV9SZ8xj6-BtPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d19bde11aa.mp4?token=lU9oLrZ1hga-xXTPbOBH5MVpv9BJneTXMnuMLuvKKTg7brr0N40J4OGiHQPQMpUu9zXiOla9j5eiMqJZWCrlTrzXFSC07ES30iezTpG27tPTIKbDzRIYst7ixhwgOvNVTuXbbMWoCOhCAt-vDxNQ_3YhPVVj3cUWN1Up6OqSv__Yr0uuW0Jmd2Dai-ysuKbeaZsXaQHdFbYLt0VhRDFiQSnxJjGHgeLSc-q3TT1ogt-6hQOGnEFelWG8QHbPqDzl0FE9OM1GVBTdwqnifmOk4cgXqm2aDy-UCnNsfSKEekNQsH9NmepGiYXh4klU_Nfe3uog1qc2UV9SZ8xj6-BtPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل علیرغم اظهارات دیروز ترامپ و ونس، همچنان به بمباران لبنان ادامه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/129092" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129090">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/278b037b53.mp4?token=sCoeC_lQ6CHhuyhqTn_2nY9WYqJ95gI7IdjYH2tt6-253nPwj75tCxX_pzqlc5cHPC7GlU6m2LSWo0jMImTnLTF7PDAKwbBfnjvsGr2Ky2y7UsW4St12k507vMTEHG4scLMHL-adzO6legQ-M3mcLKsvcxmjXXrm4Zjqv1gX1GMp5k_Xgw3D7rSlwm1XI1LYHxEaaSvuvgvyJMtsQBQEN6HOl106Phf1r7wdEeNTyMyk1TlULIj2UxNzlQM-jV_Qdf2lQnL7-ZZw0GbWSgYVJ36wyp118xTEPgiYBzuvDPaiwhNFwORuuFkFSPkCjPfffPSEsErVM5163wKOa3p4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/278b037b53.mp4?token=sCoeC_lQ6CHhuyhqTn_2nY9WYqJ95gI7IdjYH2tt6-253nPwj75tCxX_pzqlc5cHPC7GlU6m2LSWo0jMImTnLTF7PDAKwbBfnjvsGr2Ky2y7UsW4St12k507vMTEHG4scLMHL-adzO6legQ-M3mcLKsvcxmjXXrm4Zjqv1gX1GMp5k_Xgw3D7rSlwm1XI1LYHxEaaSvuvgvyJMtsQBQEN6HOl106Phf1r7wdEeNTyMyk1TlULIj2UxNzlQM-jV_Qdf2lQnL7-ZZw0GbWSgYVJ36wyp118xTEPgiYBzuvDPaiwhNFwORuuFkFSPkCjPfffPSEsErVM5163wKOa3p4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهر نبطیه در جنوب لبنان به ویرانه‌ای تبدیل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/129090" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129089">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd73e104fd.mp4?token=S0RULzFeZHuVdEb3p5Jc8h0WwhGW21pTDhiDqKc2ixoyCQoxB09Ktig5bpEAIL17uer4nCwdCDTDGGBI9FXs3VAqoNffDBgtmIslMBhVdIHMP_LyyPE97UO6bgkx1yeS_tpM5tSK1fAx1vJZYYsTpYZwe-1ZLAXh-5wCQDpF6rLopLc-JXAin8prNr1lNb1lNXEycyCuNqAKUcM1dySoyHdPZdVEmzKHcF-Nuj3eXZD1OO9Au2FsLmLrPbbJOLQVYr0-AENeKz1LVMWhZeYsafYvgCLgi6CdQ1uweM6xJU2dT2eEqccwPm-6YsGRw7q-yymkUvb3iFGIHryW45ME-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd73e104fd.mp4?token=S0RULzFeZHuVdEb3p5Jc8h0WwhGW21pTDhiDqKc2ixoyCQoxB09Ktig5bpEAIL17uer4nCwdCDTDGGBI9FXs3VAqoNffDBgtmIslMBhVdIHMP_LyyPE97UO6bgkx1yeS_tpM5tSK1fAx1vJZYYsTpYZwe-1ZLAXh-5wCQDpF6rLopLc-JXAin8prNr1lNb1lNXEycyCuNqAKUcM1dySoyHdPZdVEmzKHcF-Nuj3eXZD1OO9Au2FsLmLrPbbJOLQVYr0-AENeKz1LVMWhZeYsafYvgCLgi6CdQ1uweM6xJU2dT2eEqccwPm-6YsGRw7q-yymkUvb3iFGIHryW45ME-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.ما از «مناطق امنیتی» - نه در سوریه، نه در غزه و نه در لبنان - خارج نخواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/129089" target="_blank">📅 12:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129088">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
فارس به نقل از یک دیپلمات آگاه: ایران پیش از بازگشت به مذاکرات با آمریکا در سوئیس، خواستار دریافت تضمین‌هایی درباره پایان یافتن درگیری‌ها در لبنان شده است.
🔴
تهران تأکید کرده است که توقف خصومت‌ها در لبنان باید مطابق مفاد توافق امضاشده اجرایی شود.
🔴
میانجی‌ها در حال حاضر برای حل این موضوع و رفع اختلافات موجود تلاش می‌کنند.
🔴
مذاکراتی که قرار بود میان ایران و آمریکا برگزار شود، در پی حملات اخیر اسرائیل به لبنان «به طور موقت به تعویق افتاده است»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/129088" target="_blank">📅 12:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129087">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">چجوری یه مشکل رو از سر خودمون باز کنیم؟
اون کار رو استارت کنیم و اگه دیدیم داره خراب میشه بگیم علی الاصول نظر دیگری داشتم
اینجوری همه چی رو میتونیم بریزیم رو یکی دیگه و عزیز بمونیم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/129087" target="_blank">📅 12:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129086">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfddaba168.mp4?token=tWgxDFswQs1rETnxwqx09jl9Rmit5RnCN-z6XEmcUQ5fnARm6wkWc826HpExgJDDndhtwEHNCedL94EoGGR41rQO5KvCYcV_OHzpDvecSMy60nMMKObuN2wUGRD_ohFtoZutD4v9JVTud48NLb4WSZ2wvgBsHB1W8ed5_UsO3ibAU8K0kavSzNTt4YToZY0w5UKOx-0Ola-z1GSwrb1GnEPt_FB0HYtGXrlSQYbi7FqMblFMIwGyZxH2ZhpUl0blVI_Ydrq49lgFXp0Y4oRhDf_bdK6hT92kJiA8sooT-gMoop47NPuBZZp8rfsHVeMDuHfRv6cot0-nZlOf4R4YXBX-KiGvJwvlpSfLoYZg7Cx92YTe9RH1mx4tqmHX8kMu1HaOBItA2BNqqKOBXvQBANgmFDQgPhdS_wo43wtZ3EgvegpIO0op8-oNhNLjcopkhJTwwDQUsvvWjRGfNp6r00jv7oZslAro2eIcLlQKTnw8nqhPUpz0u5izBnYKKrN9eRFrpfG_VxLSatJX054BWikVa9WbKIQpbk2fP3XF7qyknlKDn8VgIGRf0yo2UYp79EbcKw7Skp_2HXrSxc663ASiHulnyHpwNeZlMCu9KqR1aavmhpZLSrmQ_hWcvkNI-CGVRO3bd-iLwKRr4Hejq-9Y80V8HNzauhZ7hq3BHsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfddaba168.mp4?token=tWgxDFswQs1rETnxwqx09jl9Rmit5RnCN-z6XEmcUQ5fnARm6wkWc826HpExgJDDndhtwEHNCedL94EoGGR41rQO5KvCYcV_OHzpDvecSMy60nMMKObuN2wUGRD_ohFtoZutD4v9JVTud48NLb4WSZ2wvgBsHB1W8ed5_UsO3ibAU8K0kavSzNTt4YToZY0w5UKOx-0Ola-z1GSwrb1GnEPt_FB0HYtGXrlSQYbi7FqMblFMIwGyZxH2ZhpUl0blVI_Ydrq49lgFXp0Y4oRhDf_bdK6hT92kJiA8sooT-gMoop47NPuBZZp8rfsHVeMDuHfRv6cot0-nZlOf4R4YXBX-KiGvJwvlpSfLoYZg7Cx92YTe9RH1mx4tqmHX8kMu1HaOBItA2BNqqKOBXvQBANgmFDQgPhdS_wo43wtZ3EgvegpIO0op8-oNhNLjcopkhJTwwDQUsvvWjRGfNp6r00jv7oZslAro2eIcLlQKTnw8nqhPUpz0u5izBnYKKrN9eRFrpfG_VxLSatJX054BWikVa9WbKIQpbk2fP3XF7qyknlKDn8VgIGRf0yo2UYp79EbcKw7Skp_2HXrSxc663ASiHulnyHpwNeZlMCu9KqR1aavmhpZLSrmQ_hWcvkNI-CGVRO3bd-iLwKRr4Hejq-9Y80V8HNzauhZ7hq3BHsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز، درباره لبنان:تمام خط اول روستاهای لبنان ویران شده است.ما در حال ویران کردن تمام خانه‌ها هستیم. ساکنان دیگر هرگز آنها را در مقابل چشمان خود نخواهند دید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/129086" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129083">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZagvlion9UGU2hPIIx4_8tt5sNeqdIPoJCeU5m96zeN5VIoUwkCLs-F3DONgJe5mVw4-tNjw62lUjtXWpPO6F1rtUL3m-vEDTRf11YkP2lNi7BUUqPR0NG6UiWYV5NmLB36u2Oe_vOOui1F3ECGSAAiq7vQeUcPph362HkOV9R76YnroIoqro0HHps7xaplxZYJZDtQXesDjD3qR5-Lss0lnQeVoiGsbMqYnITRO2MaxqaFWEwyyJ1H2s916bp9wrW55R-1NMubVZb_bYAOJPdgGux7KuFD8989DVHvRdB3Ocgl7a0A8xjDAxjrvsJBHyh76kgcMSGnUGCMBPkqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رهبر اپوزیسیون اسرائیل یائیر لاپید:
اگر سریعاً این دولت را تغییر ندهیم، روابط خارجی اسرائیل نابود خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/129083" target="_blank">📅 12:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129082">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=IzNegGwC4HAYeynOIfF9o1iUnbLp7FKTSfv3jzdcyw3z_zgqAd246JvYzhKYcxAsdDiRzMPruCxQSrNnwvddXL0nuF3SJGnddJD42VlLKbpABxNp-jCpXFZo_MuWIkPUz2Fz31to_46uQEJs07krba7gwkVWwXzI2pgQ-VGs1_X_ZdPqitgqqhGeMMJJe6_fHBTN436nJbBJtZQM2VCg__jba1CoIB2z1Lw8fazubydP8-LwT7ZWYQN7WTZcCrOOlGxPDSOPxzQZB6iKyC5Jg5NcL8420aVTSXQg9s1EeFc56kMUUIkpsatQVJvZl61f425E7oTDWST-ejwEodvKIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=IzNegGwC4HAYeynOIfF9o1iUnbLp7FKTSfv3jzdcyw3z_zgqAd246JvYzhKYcxAsdDiRzMPruCxQSrNnwvddXL0nuF3SJGnddJD42VlLKbpABxNp-jCpXFZo_MuWIkPUz2Fz31to_46uQEJs07krba7gwkVWwXzI2pgQ-VGs1_X_ZdPqitgqqhGeMMJJe6_fHBTN436nJbBJtZQM2VCg__jba1CoIB2z1Lw8fazubydP8-LwT7ZWYQN7WTZcCrOOlGxPDSOPxzQZB6iKyC5Jg5NcL8420aVTSXQg9s1EeFc56kMUUIkpsatQVJvZl61f425E7oTDWST-ejwEodvKIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران شدید نبطیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/129082" target="_blank">📅 12:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129081">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5Lu0hLdV3mT-XOJljzngsk649z_OsYrfq6gSnqRfmPgsX7kuX6rMeZBGY3W3TJyYzE-UJSGnQhmDJA5TP1K8sLneh-ErEk4t2RUXtCPSFHhSyWc_qLa7Ui5KSgVKoPTWef9HrXAcrDmW_TJsHMXnE8lgAc8_8K78-7QaOTKva2_sw1AT1BiQBjGDT3wmuIs7SLuZ-tgZwBTjgjTBG4vdRykC0uHb8OvqJVI4Rqv4UwiqFvaanwwVHfdKjgdWnOgO_XHR-t8AhKBMbXMGWYjk9bdARXJ0rXfho7V8JJMOoGnVNQPwyuMnsg_OFI1PV0AHCHRjaqYUFa2gbPGR2vC9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لاوروف: خطر رویارویی مستقیم ناتو و روسیه به‌سرعت می‌تواند هسته‌ای شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/129081" target="_blank">📅 12:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129080">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل اعلام کرد که فرمانده یک گردان زرهی و سه سرباز دیگر در جنوب لبنان در اثر اصابت پهپاد حزب‌الله یا موشک ضدتانک به تانکشان در روستای کفر تبنیت کشته شدند.
🔴
انفجاری که منجر به کشته شدن هر چهار عضو خدمه شد، کمی پس از نیمه‌شب رخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/129080" target="_blank">📅 12:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129079">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
کاتس درباره درگیری‌ها تو سوریه و حزب‌الله : ما اونجا داریم می‌جنگیم
🔴
ما به جولانی نیازی نداریم
🔴
جولانی، همون تروریست کت‌وشلواری، لازم نیست بیاد و به ما کمک کنه
🔴
ما سوریه رو خوب می‌شناسیم اون قرار نیست تو لبنان به ما کمک کنه
🔴
بهتره تو سوریه بمونه، تو…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/129079" target="_blank">📅 12:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129078">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / هم اکنون منابع لبنانی می‌گویند:
ستون‌های زرهی اسرائیلی در حال پیشروی به سمت نبطیه، پایتخت حزب‌الله در جنوب لبنان هستند و درگیری‌ها سنگینی گزارش می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/129078" target="_blank">📅 12:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129077">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
شهباز شریف: از طرف ملت پاکستان در مراسم تشییع رهبر سابق ایران شرکت خواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/129077" target="_blank">📅 12:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129076">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/129076" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129075">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
حرکت گسترده مهاجرت از شهرستان‌های صور و بنت جبیل به سمت صیدا و بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/129075" target="_blank">📅 12:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129074">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=DfDrSudnNgbGGpQfSKB6q7ASOvgMUhGom7A2t0Fgc9epmANDAqUOcmLYXT_xMNyMnoj63w_wsa0_bQtkX4CdDoXzWOpmxS5mRceYB9GvimcN2KfNH7o-uzOamfJr9HnDHp-I72PAjvRNYKoI-vBdLN0DjuwzZajgpODNLbZczerQJsIZh1SRvDgFEmQQZxDnzUT3W_5qptJ68TQRKrJsMEB0uPs1TgWTRchp2uxzyo2AChz-y7Ua78Eu9C0_nSCf6FMNiIBE8ZtZoamvrevlkQySIvBsBgSLWfqZ9cRrJtTTvOipGeTAC9hEjoqPNb2s22cgMC0qTVn0aGYLoeVANg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=DfDrSudnNgbGGpQfSKB6q7ASOvgMUhGom7A2t0Fgc9epmANDAqUOcmLYXT_xMNyMnoj63w_wsa0_bQtkX4CdDoXzWOpmxS5mRceYB9GvimcN2KfNH7o-uzOamfJr9HnDHp-I72PAjvRNYKoI-vBdLN0DjuwzZajgpODNLbZczerQJsIZh1SRvDgFEmQQZxDnzUT3W_5qptJ68TQRKrJsMEB0uPs1TgWTRchp2uxzyo2AChz-y7Ua78Eu9C0_nSCf6FMNiIBE8ZtZoamvrevlkQySIvBsBgSLWfqZ9cRrJtTTvOipGeTAC9hEjoqPNb2s22cgMC0qTVn0aGYLoeVANg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/129074" target="_blank">📅 11:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129073">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری / معاریو: مقامات اسرائیلی نگرانند که اختلاف ترامپ و نتانیاهو از سطح حرف فراتر رفته و به اقدامات ملموسی مانند تأخیر در ارسال سلاح، محدودیت در کمک‌های نظامی و حتی گام‌هایی شبیه به تحریم تسلیحاتی تبدیل شود.
🔴
اسرائیل معتقد است که فشار ایالات متحده برای خروج از جنوب لبنان و حرمون سوریه تشدید خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/129073" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129072">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، در گفت‌گو با اکسیوس دربارهٔ ایران:
🔴
«تنها راهی که می‌توانم سخت‌گیرانه‌تر عمل کنم این است که دو یا سه هفتهٔ دیگر آنجا بمانم و همچنان به شدت هرچه تمام‌تر آنها را بمباران کنم، درست است؟
🔴
اما آن کار چه نتیجه‌ای برای ما دارد؟ تنگهٔ هرمز باز نخواهد بود. ماه‌ها نفت نخواهیم داشت. تا وقتی که بمب می‌ریزی، آن تنگه به طور خودکار بسته می‌شود.
🔴
این از آن دست مسائلی است که می‌تواند باعث یک رکود جهانی شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/129072" target="_blank">📅 11:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129071">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
بعد از اینکه سوئیس اعلام کرد مذاکرات امروز آمریکا و ایران لغو شده؛ قیمت دلار مجددا از ۱۵۳ هزار تومن به ۱۶۲ هزار تومن رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/129071" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129070">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل اعلام کرد که از زمان توافق آتش‌بس آوریل گذشته، ۲۳ سرباز اسرائیلی در لبنان کشته شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/129070" target="_blank">📅 11:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129069">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
طالبان مدعی شد که شب گذشته حملات هوایی را در داخل استان‌های بلوچستان و خیبر پختونخوا پاکستان انجام داده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/129069" target="_blank">📅 11:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129068">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-POpOj7Oy0KWflfYQVt9PXq67M2ISJ40j5gwg6ldFe0_jhuLSiAb4qFDbRzMFBnQ3gBNCIYCs8o7OjbyZ3zjtzQPLoV4AkLK2q4-YcMETes3if1vcg1en_iOUIUn5HyrJrCzcuWs3pZbX-x4wm96NJnnvqjLJs8PZmieGuZo4ldBI5YQzt9Fv4V5SJLjYjwkpqGOoE4J_9MV-PhuCkyD989ORG7HIM7jeGhUzfm4nT4xE-yDXp_yK4frvdeiA2N3wJIDC6dX1xGyi70qEjMwKSLwDK8Hrq1ZtrdoKx3HtLpFmcVJ-QzcDeuK8nqXV_grAzbuGWMu4qkpnDC2fTakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت به ۸۰ دلار در هر بشکه افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/129068" target="_blank">📅 11:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129067">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رویترز: سپاه پاسداران انقلاب اسلامی سلول‌های مخفی در عراق ایجاد کرده است تا حملات پهپادی علیه کویت، عربستان سعودی و امارات متحده عربی انجام دهد.این سلول‌ها که از جنگجویان شیعه نخبه عراقی تشکیل شده‌اند و مستقیماً به سپاه پاسداران گزارش می‌دهند، بین آوریل و مه حداقل هفت حمله پهپادی از جنوب عراق انجام داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/129067" target="_blank">📅 11:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129066">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXIXBDZuBZZ7AOuz4QQO4DxoTMkG0bq3K5epF5ak_kpnW7-G4pNYKW8a_8QxrObBR6oXUGbqZwLWY9Ab544RKU9_TXxzAWjgfWR2kh5eR4R5R-5zCiP7mgg8k6k11MBujuU-dUHvEncPznpvrCY0YyfsYLziqNfc38J-3EZ39g54xV8PFLbNiVa_YsY7ejWnZchmcelSKpoaC_sVxEvpPjCUSvOU3UHiqqqTylVeimKXiFAMN0X1TmFpxAYk0fYL31ZBZVmhuojdIYvrnpFO0dgQOfePAIwZQfIMdV0FXXBfEKq1RZ5ePGJjKcjGhYAq0RO5rLXuvCM4I_4x1L6-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل بن-گویر: برای هر اشک مادر اسرائیلی، هزار مادر لبنانی باید گریه کنند. تمام لبنان باید بسوزد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/129066" target="_blank">📅 11:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129065">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTMwI9gbJh-5KnQBGiu2XPFR4H8tTg6c2vVJyf7GCBGcjaUIdZ0UI-BukyAsigCTMbx-ec27gSRPYu5L05lhRj-3oilvlAZkQAYfN5FEBX5CkbT1rErJlSj8wGYp9b5rBS6r_EOdMEZdow3qCQuIKq2dwXacUj4duTxXRYlfqwO5ocBZzNR1Y4FApe89Vqeob-d09p4VOnTdvE0-Iq9CBXSwo78DIDOHz1OaAxM8Nc7Ufbn871W7RLd9JCDF-9rnyvzXVGK11r35NqadM_qMzG0Y9GXJBdcIRKXGx7CZTWOczwJ2GpShykw9zegX_J7Sll09bHLAR9yIcIeDplCeIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موسسه HFI: ارزیابی اولیه نشان می‌دهد؛ سپاه پاسداران انقلاب اسلامی تردد کشتی‌ها را به ۳۰ تا ۴۰ فروند در روز محدود خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/129065" target="_blank">📅 11:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129064">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3affd3cf08.mp4?token=AoJNsFDAGF--BHWoB74PZajz8psjf6Nh1EDc-gg-fPG73xdcVYmKW-MXpmMOYgOTtnaI_rbyITc059UfwP5i4c8WZb-f6FjoZ5ir0YmP1-qyndFEfAahJpEEnPBHlIR8MybHEj8rDt9A1mysoQoPJPoCVbSg65KmDi8ZXehBSxhseNHiGsX-Kj9knKKxrDDAYuJBEjR3TnzBj-jzxvnW3RZG02m772GdJEAti6OSOIZtNzVaT2SFIcMktEBFcEVak-fpnJvGt60rersQeE6oaaoOwMAfthk3FHGQ_AYljFaJkLgCZhEIxkxW0mr6vavRkXGqbTLoFxUDtlxDLXzMNpqEcEkXE9hriXDkjnZiwiwKq_k_XRFylggJmMeiVkCxZrHPhjHLvfXJg2nuike8TYQe8I8MzCUgcty0b6e5TvrcErUvlDJcN-qHVVVqEwHBFhMZek7FfJEBj7GbREovVGyaAd2CU9pHGkvxC1nivuaf0Ii1lE-9Hu7jxL0GrQe0Ny7tcTWcZVC4hEagVZG8M_FOerITeK7Kr7oXxIzx_u8F5nw4A7mnPf3CbktrhmHqtdTH8CMerSPXMHpbQgGnY7ZqhsdPpFMm1Q8DhuLlH4YFD8dgf-1L5qS3WCB-zHrA7wmGpftasdxcTyC58qjbhMuStUss9WqQEJBcu1PbMew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3affd3cf08.mp4?token=AoJNsFDAGF--BHWoB74PZajz8psjf6Nh1EDc-gg-fPG73xdcVYmKW-MXpmMOYgOTtnaI_rbyITc059UfwP5i4c8WZb-f6FjoZ5ir0YmP1-qyndFEfAahJpEEnPBHlIR8MybHEj8rDt9A1mysoQoPJPoCVbSg65KmDi8ZXehBSxhseNHiGsX-Kj9knKKxrDDAYuJBEjR3TnzBj-jzxvnW3RZG02m772GdJEAti6OSOIZtNzVaT2SFIcMktEBFcEVak-fpnJvGt60rersQeE6oaaoOwMAfthk3FHGQ_AYljFaJkLgCZhEIxkxW0mr6vavRkXGqbTLoFxUDtlxDLXzMNpqEcEkXE9hriXDkjnZiwiwKq_k_XRFylggJmMeiVkCxZrHPhjHLvfXJg2nuike8TYQe8I8MzCUgcty0b6e5TvrcErUvlDJcN-qHVVVqEwHBFhMZek7FfJEBj7GbREovVGyaAd2CU9pHGkvxC1nivuaf0Ii1lE-9Hu7jxL0GrQe0Ny7tcTWcZVC4hEagVZG8M_FOerITeK7Kr7oXxIzx_u8F5nw4A7mnPf3CbktrhmHqtdTH8CMerSPXMHpbQgGnY7ZqhsdPpFMm1Q8DhuLlH4YFD8dgf-1L5qS3WCB-zHrA7wmGpftasdxcTyC58qjbhMuStUss9WqQEJBcu1PbMew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استاد دانشگاه تهران: یک لیوان آب ۱۵ هزار تومان است یک لیتر بنزین ۳ هزار تومان!
🔴
نیاز به مدیرانی داریم که جسارت تصمیم‌گیری داشته باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129064" target="_blank">📅 11:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129063">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
العربیه: حملات اسرائیل به جنوب لبنان شب گذشته به طرز چشمگیری تشدید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/129063" target="_blank">📅 11:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129062">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سوئیس رسما اعلام کرد: مذاکرات ایران و آمریکا برگزار نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129062" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129061">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ونس، معاون ترامپ: ایرانی‌ها مثل یک کشور عادی مذاکره می‌کنند؛ آنها با ما به گونه‌ای صحبت می‌کنند که فکر نمی‌کنم از نظر دیپلماتیک با ایران در مدت بسیار طولانی، شاید هرگز، چنین اتفاقی افتاده باشد
🔴
احتمالا افرادی در اسرائیل هستند که دوست دارند ایران را به لیبی تبدیل کنند، یعنی اساساً یک «دولت فرومانده» با ۹۰ میلیون نفر جمعیت؛ اما تبدیل ایران به لیبی برای ایالات متحدهٔ آمریکا قطعا خوب نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129061" target="_blank">📅 10:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129060">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ارتش اسرائیل مواضعی را در مناطق «حبوش»، «تول» و ارتفاعات «الجبور» در جنوب لبنان بمباران کرد. آمار رسمی دولت لبنان نشان می‌دهد شمار کشته‌شدگان حملات شب گذشته اسرائیل به فرمانداری النبطیه به 16 نفر رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129060" target="_blank">📅 10:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129052">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cd9xwl72yb6W7c02TwfC-y2PxCRqISeyIZ_fskQhj6R4ixQESDopJmOmTU2hd2vwZCnQUik15Clmx95Ts0w3ymg0ntSlOgqiPkAGNoyQ30wrbLiQIMMJ0XNKWfv99oaI2vuS-Z5PWzl4X2n1aGFmaRr9Ivbmf-IKwTavmaDzUydGQ1AbHdWlLo0SUpeehiitJAaxQDDEsE5Uc8ohgQ2jT43rVuGQd3qkkuCT19k0tkP-LEndVuY3XFCyoiJUGY0NnAqaEmV-MRyWo4hTn89KQ2c6JFbqlBWRLDp4lUP8veoDjpvVUAeMSQrWkBU4iOf_m3CPG1o-0mamQ_RmrfXz5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azPaEkrzTg7WF0nUvVQ0fcY4IiW4_SOqmK4agjldY8t4ONuyjnMR-i-YhNQd9X1R4Qs8ZXyEIoW-789g8b2dUc-lXBFrBvfd-v-ypCf4shKPU__q4Z6Lw4hgrhi813NaGIE5VP9wKbprHukbZVN1_RPbzzCKE5mWh631cYP6fCh28CnJyawAsKuEzjt4az_aEEgY9CieV_ZJRLQugW-vJOasL5UFZPVIYkWIv-gpgbrADVspYWO8IXgoqutPO9yKev9Y844q4VtB1T7VPaEbss6jKzcYd0u31PPb3EJKsANn0dbw9KYvy8wCqY2ydaNV5-H6ExeGysjQN03YPjsdOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYBYMcvz3R-FHdt6gCKmp_9_uSfhElhN_BxB_uq30FOaLTlp-ykkLugRjDoBoMwicQSsIaVp1Gt8MSlYwaroH7ksdQeB1ImTHoOGmYK9Rm-4k3fyrQof1pt13z8Z4Hs4Bik_kUGODuAomAgq3RXsrGEkvAdvlTTcbetXj81kMwvVbnq9fpBMTvPm-j0fOHD3IBHzjOj3jTgusBVZZnTkoNH9eBbZFSsYevneNId-yd8sFGtJNqO1TPcvYgbNgt1yiQtx97dR3mWRxP140n7YEd39B0QDdBTw-nF6D7TKa6RaJUjR_BGsdnFTn8lYNiq55ewGOefBswi4beL7F6dgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vs9nMUTQbZbbBBM7H3LQt77OqloDx879rHCpsxNQQIVXq0j-VJN4FyCwkEf80xKlUzqf3slzqKm9pmTPhiMMBD4lDKe67CwtRd0Ix33qBVfQmybM_UJ6PK5hi-NmVTomdiIFGDOr5rwjILPPYkSc87wr__bZNYQZsFiygcRpxdcpIvRuZKyLnNqjFh0siL81e1lWDEYPag5UXTH_p8lE76ytxLKDRvH8aqOq2kmdTGZHZZ5bXw8VZU_6ce8ZfIEYjL3hLiYS4A1Zk3nBvkhmZ5rGzJyZFchAOFQti1JiVzkTU6vMytEtBGY8N4YIcg1cmNlimzGwfhI7BcT3r9ZbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bprDVxHZg1q454ZoXJp89VN7hDDQtL-OucAhmGJqkNW4Cm5P8dQ8RwN0O-jp4CVcPUkMkiS5ycGngAlw-m-DZHBnSur0H9X7RYcrTmkOAwlV2TIENeIm7Q9JeD5Il4ruYZ7r_uhrC3ZZXz49X34uT2FOXoU9ay_1_xhJQE-aeTDzpCafv_ox-hWDdFPtyByp_JK9bVzQw3LToFkXSg9JUMvodzLkFCoEviKnpXBHiHQLraDaRKkZ75r3YqPTGmB07QmNxg4wyd-jDHg2qAaKqsnxwANyaxAK8dsUMGfi-egTHzVKLBz1ocJoXpSjw1SIILsK3b9KMDmBtiKLx6Vd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OwWbaOrYzpkQNea35lyZm9U_rioOrmEd4KaUmuOiWrC_wlP2Df2xtI3p3p0DuDm7g_Ex-cBexLLIHtnUbEIXNTXjmMUhC76KnUPHwBC4dnugFD1YHM8LF-Oe9LIHlr4JVsKC3Uj82fdpnb15KhxFDrKCR3pN8t7wXOu6uiR-e3T4UDuvtv2Hfv6eO0sZjbQPIuHQG8XUsmS0mKtU03zzNoh6GHjNpnyyeSjXf8BbNmfYkV8eYkghwGdNvzkMWZ9f_mxe8QFQ0wjKYv1zCg7Wdk0KwE2-PY2w0eO9rYqbTfDW9BvK6zejYAXtS8aJFYENz4JLO9yWa7hjeEa802uCNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gPO-56ZQtoTWYFXMAvKNbXVqddvQPV6em5W8XZ2HQp6UGTV2aJiuji2NnYVoZ5xJRTksEhV5uoubxaCHZ8MuGorUgWUGCKAiuZsTTqiKgy_Vl7frn1ZtdgzTp_gobaMNWt2agjSy5W-_Lhjag3VuJvXb-QZkl1AFf9T4sZtA-43-RDSXEGMnYMpV2HeO2CZB_LlYOZzWWNKlSv0-xatzsaOMz7cCGPrJYRaY5yrIdmvL9bYhkWd17qGRUbBvxRhhIqIKYUQs63TJvgs2zD9ZU4P9v3-GAR232PlLUzKPlGjyB1sjJeLi-7U7pL_JjDdNzUCtfQwWWgf7_RpxwEzKpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQF7xB9ziRuwyph1Rha7rh5iJ9UTULwCYxAjuzbB48qcaYJteofpOzzSLUyW6Dbh9xNO1Rn37s1TEbB5BCHy-EcsDUMh6sOaNtKWCpIJTmvRHA48sDryxdifBeAyQQVNA43WobaKIVDyW0exdvc0cNEouaxp-gd7b6fVXqLHbI2It3_XAcMYAdT9S4vS_w5BBIXSqKzhXwv2rAv8nSlqEpl_eW8hfZvEyKDfUDmzcZcvOCRc3rjJU6C72NP2wFEnxmgDxMgoh2iFCLRqbQqq-jTjA1ADfdzcZCrNXc-xDS_sqbhqEYLVIZy3n0WjCYWBWQL7vATwcME6EmkF-GSwMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات هوایی متعدد اسرائیل به نقاط مختلف در جنوب لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129052" target="_blank">📅 10:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129051">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یک رسانه آمریکایی: ونس سفر به سوئیس را به دلیل حوادث لبنان لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/129051" target="_blank">📅 10:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129050">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZJfjOhgOK9gak2kc8DNeErP8n8k3ef5BGQl5buHT_TaDEkcOGM2UI5nMAyGZB7w5YXDjzezgzOVb5w1Fy56oyfs17ue9ysgRBW_355uGG4uynVS0qizXXln_X7jrHp9GP4332wblL3ptuaxvi8NQI3p9lUwoJsEXtKLInwWUnvGxYaEgS9DuKs4z5rQ_OIBqrBbsIhsHx9to7nLIgN4YY8tlvosGLLjuyBnCGXJ6Gp-Nw2cFstOpdKxE9JfMzNgxQ1IWzbmp5lnRXJuZl96JWAu8_k7_-O7CdCWxAMnK69Wmx8dJWJHAzCQc7JV1vVsQXaxKNaDc342pQ0YIgtXgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش ۵ هزار تومانی تتر با خبر لغو مذاکرات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129050" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129049">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63aa3bf462.mp4?token=FyfxWOtnNHWPPQDBZHniBoN9i8fHUzMBH_AfZfrJQKlhR5QrCMdqpgaj_0ZwyP6NAdCv2l4L_09AS1ExR6fSA0wGKUP-auM0AQ_AD1NMlybyI8_iQRSKnTtkkGOHcY2sVTd-ULFFWwAehyiwlvVtOobRwTPqcRThcSXSh1SjpwNTjh6L4mcNWfGADgDaxnfc4b6vMoU1jBgsSCW3_4rS1b33hPpLCyXcmP-HopNpKN9zA52SYyQTGH7WQQQtHnaJrDO-aUShGGl95pawnj0-n7X8GEp_JqXWSnwPbnn6_A9ep4efMiXDgipoYLiK-Qq81URO1a7zA0TuEg5N242_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63aa3bf462.mp4?token=FyfxWOtnNHWPPQDBZHniBoN9i8fHUzMBH_AfZfrJQKlhR5QrCMdqpgaj_0ZwyP6NAdCv2l4L_09AS1ExR6fSA0wGKUP-auM0AQ_AD1NMlybyI8_iQRSKnTtkkGOHcY2sVTd-ULFFWwAehyiwlvVtOobRwTPqcRThcSXSh1SjpwNTjh6L4mcNWfGADgDaxnfc4b6vMoU1jBgsSCW3_4rS1b33hPpLCyXcmP-HopNpKN9zA52SYyQTGH7WQQQtHnaJrDO-aUShGGl95pawnj0-n7X8GEp_JqXWSnwPbnn6_A9ep4efMiXDgipoYLiK-Qq81URO1a7zA0TuEg5N242_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت خوب سد کرج ۲۸ خرداد ۱۴۰۵
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129049" target="_blank">📅 10:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129048">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3578fa102b.mp4?token=cKtt1VWas50SKR1ELTCmmbBunaTfZDoVgHZaYhlashdTvKQjCesyJvqtAGL6lT-5Y0eQ3P7iI-9GtuWeMtcDaHVjWyJCu8iCPUQFUrQdqdjCGBpLM36PQdO8gQXbmGrB4otIlohDlnbMgZhpVfd3Cpjl5GdbFsyi0Ckm9vyH66EtbC0zGVmSeJ5SCLFmdYBKumM6tIKOJQMK_u-K0i9BOFi6HUCXcrS2sWFCEVEYm7CR7-DYYtPm4CyPqsYlbDUmXUNwOvS1ojuJSAvcR3hV_tk1ycwcNlJwEWYKOXdx9mBZQOA29e1Zxe8uER0MqB4h7_CqtrPAysgcRKzJb2L9IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3578fa102b.mp4?token=cKtt1VWas50SKR1ELTCmmbBunaTfZDoVgHZaYhlashdTvKQjCesyJvqtAGL6lT-5Y0eQ3P7iI-9GtuWeMtcDaHVjWyJCu8iCPUQFUrQdqdjCGBpLM36PQdO8gQXbmGrB4otIlohDlnbMgZhpVfd3Cpjl5GdbFsyi0Ckm9vyH66EtbC0zGVmSeJ5SCLFmdYBKumM6tIKOJQMK_u-K0i9BOFi6HUCXcrS2sWFCEVEYm7CR7-DYYtPm4CyPqsYlbDUmXUNwOvS1ojuJSAvcR3hV_tk1ycwcNlJwEWYKOXdx9mBZQOA29e1Zxe8uER0MqB4h7_CqtrPAysgcRKzJb2L9IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لغو تحریم نفت ایران به نفع آمریکاست چون چین پول بیشتری می‌پردازد / برنی مورنو، سناتور آمریکایی:"ما اکنون به آنها اجازه می‌دهیم که نفت خود را بفروشند. این چه فایده‌ای دارد؟ این به نفع آمریکایی‌ها خواهد بود. این باعث کاهش قیمت نفت می‌شود.
🔴
و چین را مجبور به پرداخت هزینه بیشتر برای نفت می‌کند! و همچنین متوجه می‌شود چه کسانی نفت چین را می‌خرند. بنابراین ما را در موقعیت عالی، یک مذاکره عالی قرار می‌دهد و در نهایت، من به رئیس جمهور ترامپ اعتماد دارم که تصمیمات درست را می‌گیرد."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129048" target="_blank">📅 10:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129047">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر خارجه فرانسه: آمریکا باید بر اسرائیل فشار بیاورد تا حملات خود به لبنان را متوقف کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/129047" target="_blank">📅 10:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129046">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ارتش اسرائیل: شب گذشته شاهد درگیری‌های دشوار و پیچیده‌ای با حزب‌الله در جنوب لبنان بودیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129046" target="_blank">📅 10:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129045">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ارتش اسرائیل تائید کرد: چهار سربازش دیشب در درگیری‌های جنوب لبنان کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/129045" target="_blank">📅 10:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129044">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXwilRD4XNHug8wmccw_htbM_zDXReng1lf-54XBKwloR0QRo74KWwCs6HJ_4E0E8FFKnJfFP17g6Dyl1C1PjujYgMomV4zjWmHd4zX3_vLU8kBXqoUUPQ3ET_mo-BZGjUGZbDjwIYSsOjspGk29HUTGagElcsAarZt7LK_0Qwo7J-PtvnpdCyLdaKHzLV2wos_H6HmLIopfAs18NymHd_mmOkGIXVjuEdnI0kHKXKTpleJsk6gHGfTmSjOtgeR6DHrdh5nK0C1wOz6xNpX3P9FSXDgqC3yq-lUzTXXBu8_I9kXzSPZWZ2gooKBxZntM_FJp5zRP-g90PmJ_eBGVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در پی حملات هوایی شب گذشته اسرائیل به منطقه النبطیه در جنوب لبنان، 16 نفر کشته شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129044" target="_blank">📅 10:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129043">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۴ ریشتر در عمق ۸ کیلومتری زمین، صبح امروز اشتریان لرستان را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/129043" target="_blank">📅 10:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129042">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udQlMpnqEKw6D9LsgnTHHWXA8tg-Slv4R_O0Y3BZKtFLOHxo_ttoQTJzLrFanh0UxTXe79qkdLYhYzJrTiUQzGlKx0Xiq8XO0m1xrz4c4ZstH0inI_6JEyKq2jj6yeS5Tx1zepX8SypONcHUpMbR0K3oCUuvfw0OVgoNsIxrgmvOEnA8kt7uik9-mn_IwJbCHwleK_Tj3pD2FNxD29OUE6s2-HuxmcP7GOPRD3gUsf0fLh9qT71ewmOfNg5PvghstjzN1lOUC5ugzLwc7Zfd3_TG9wy6p7LbzDth3D5duAIToycXFlaF73jmdpUW4u2D5HXk8RJGxL4D685MnMeheA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دموکرات‌ها در یک چیز از جمهوری‌خواهان بهترند - تقلب. آمریکا را دوباره بزرگ کنید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129042" target="_blank">📅 10:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129041">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: حزب‌الله باید خلع سلاح شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129041" target="_blank">📅 10:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129040">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پاکستان تردد تجار از مرز زمینی‌ به ایران را از سر گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129040" target="_blank">📅 09:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129039">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رهبر اکثریت سنا: توافق با ایران گامی در مسیر درست است
🔴
مشوق‌های مالی برای ایران به اقداماتی وابسته هستند که تهران باید در آینده انجام دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129039" target="_blank">📅 09:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129038">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
عضو کمیسیون اجتماعی مجلس: انتخابات شوراها تا قبل از شهریور برگزار می‌شود
🔴
اینکه این انتخابات همزمان با انتخابات مجلس یا ریاست‌جمهوری برگزار می‌شود صحت ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129038" target="_blank">📅 09:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129037">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sw4Y667vOGULaoY917-G3vH8d-kbyS8wONuRgi_TGBJRrqlBx-RqNykIFpmmfThmEYg_ESZlprADGm-IK_tVkkoK4w8qeDZ9wYacjBqSokkUNldCWakdNTHrGKq-uPBWWFglVH79AdG_KdWDIbgA1OuAiVPjNaLX-sDvwmxG3gwc5zLTNYRmG-6BIvrAxTndk1KYFdJ8kbfqwABOzlHdsfglBvXP0UIHQCDgBWbcIHVzqLk39l-WtJ-ieuf6IyVccBFxKXlUpdlIV7QtoiRdtP4iGhC_wU8YGVfEbnbgHRp1MT4ZDwhy7xcwhUaCTflELJc106hFBU72LVbPrzd2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه X تیک آبی معاون عراقچی، کاظم غریب‌آبادی را حذف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129037" target="_blank">📅 09:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129036">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFb1jDF5MFyRhjuRddDE3ZX7XFJyBIs4dnVsFUClEI2ELl9e2B-9Mrr1PnW3ls1ts9JDD9Fb9z5gW14uQyjgTHIG8rWPcZ7kauJ40OU_LzEIFz9d2OXhrNijAFZNLN26QqE3TczGrY9_DAsJhwqoMzjgokw-SfjRoN4Yf0tJh0_qeO6eilGsrf1OkMvkP-RBMZMcffW76odbSU-FGEsANMU8d5Y_5-fVDRnM9v_JdwB64o2UBogGCFmw01QVK4LO_p3YIjlgQIQ-Hb6bKlfwbg-OxkFzqOrn9gYWnhr1DlM-faLWa8csbVJB7e2lduAinwgeHJuEukv8gOnNaGmpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آپدیت بازار کریپتو
🔴
مارکت کپ: ۲.١۶  تریلیون دلار
🔴
شاخص ترس/طمع: ١٩%
🔴
قیمت تتر: ١۵٨،٣٠٠ تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129036" target="_blank">📅 09:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129035">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزیر امنیت داخلی اسرائیل خطاب به معاون ترامپ: هر کس به ما پشت کند زیان خواهد دید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129035" target="_blank">📅 09:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129034">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40d193a76.mp4?token=cUG3x9FamR3xUef4cAfm9MbyrOduzs_V1Lwdsq9TSgC4pbOSMBlASfYXvV04rz6S22bG-F_DeKK0XiGjLOLLfdriSTg-qy792qjTEVghFWIe02bHh96LcsSI9L8tzL5wEliJ7AtFNxd3co2YFEHofBkJGxNgMx3qSW0KGYQyRyAQvmlk5G5sjIGBSW7vYu-tDLC7VzaYl2sm1Hd8VHPCxk_Qclmm1syTAYIKssrP8f26O5WQ_7kpZjJ9cNaIXBHflEIB1pYtTsF4TQXgM-YvnFKvo9PpiEFjgurdYsRRne53nXTNCD707Cp_enCwzn9QlCBQ9Z7pdb1luoWvjaNItA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40d193a76.mp4?token=cUG3x9FamR3xUef4cAfm9MbyrOduzs_V1Lwdsq9TSgC4pbOSMBlASfYXvV04rz6S22bG-F_DeKK0XiGjLOLLfdriSTg-qy792qjTEVghFWIe02bHh96LcsSI9L8tzL5wEliJ7AtFNxd3co2YFEHofBkJGxNgMx3qSW0KGYQyRyAQvmlk5G5sjIGBSW7vYu-tDLC7VzaYl2sm1Hd8VHPCxk_Qclmm1syTAYIKssrP8f26O5WQ_7kpZjJ9cNaIXBHflEIB1pYtTsF4TQXgM-YvnFKvo9PpiEFjgurdYsRRne53nXTNCD707Cp_enCwzn9QlCBQ9Z7pdb1luoWvjaNItA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اکسیوس: در مورد نه تنها اعمال قدرت، بلکه محدودیت‌های قدرت خود به عنوان نتیجه از درگیری ایران چه آموخته‌اید؟
🔴
ترامپ: هیچ محدودیتی وجود ندارد. من هنوز آن درس را نیاموخته‌ام. می‌دانم که وجود دارند، اما می‌دانید، هیچ محدودیتی وجود ندارد. ما آن‌ها را کاملاً از نظر نظامی شکست دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129034" target="_blank">📅 09:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129033">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e1da86bb.mp4?token=bLe2xWT5WCoRpmkhcwVj6StbAyE8tDax_5aCYNnsBO303Iwa_clDAxXaKMeksFbaao19UBd62joYMKBZFsXzdvaY-iMt8VZ-FHCR3EIVdIlgf-LdsWzwHlSGUVgawf9xUxDhtG8CPbTvXISr--JjCa4FKqlU-ptXA4k09zGoWj0WZjuoLvSqah2KnghjWkm9uxlay9JyaA5C-TRPLa7iBJyL7JTyrLEPhdJkFPVND1zjIjeU8XqPglXRRQqIRU4YphdUL5wfkq4y77LM0a2Ia7VotwmixKKNtk9DZia2-_p6TvMXlbboppxkG3V4gDmeA0idEb5TV_003AyJGE0a1IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e1da86bb.mp4?token=bLe2xWT5WCoRpmkhcwVj6StbAyE8tDax_5aCYNnsBO303Iwa_clDAxXaKMeksFbaao19UBd62joYMKBZFsXzdvaY-iMt8VZ-FHCR3EIVdIlgf-LdsWzwHlSGUVgawf9xUxDhtG8CPbTvXISr--JjCa4FKqlU-ptXA4k09zGoWj0WZjuoLvSqah2KnghjWkm9uxlay9JyaA5C-TRPLa7iBJyL7JTyrLEPhdJkFPVND1zjIjeU8XqPglXRRQqIRU4YphdUL5wfkq4y77LM0a2Ia7VotwmixKKNtk9DZia2-_p6TvMXlbboppxkG3V4gDmeA0idEb5TV_003AyJGE0a1IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: در آغاز درگیری ایران، شما صحبت کردید که فقط تسلیم بی‌قید و شرط را می‌خواهید. تفاهم‌نامه شبیه تسلیم بی‌قید و شرط به نظر نمی‌رسد.
🔴
ترامپ: واقعاً احتمالاً تسلیم بی‌قید و شرط است. من اینطور فکر می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129033" target="_blank">📅 09:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129032">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9eb76e443.mp4?token=E-L0PAKiPspTvzof9VBluEo-rg7iBa-NbIt22FykApOMiAxYLg3tCHUTo0l8vsue1Ik5UzDLoSLsV7cq2HGBVTWXdl003adxqwpugvp3u0Vb0a8RlOC8Ywul2hAPKWohgaCdGxBaCTqVunmvXTX5I68k8oSYqB9yHGFhh5L0qFQ8QnuyMzm6Wl72G-fsTD25SJkA4XU1KnA0xMz6ZOcbv46tA7WFQ-OyOQ7bbMDbGj2XU2On6-4eTxNKIYzQzUq_vbSuCenC0DhlUOHi_lzoLpw1OAzJ-FICmLU23bpFCeJ6HETodC5v9BVycNj0u6JTMVYhCR5z8isGN-f7LZ165g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9eb76e443.mp4?token=E-L0PAKiPspTvzof9VBluEo-rg7iBa-NbIt22FykApOMiAxYLg3tCHUTo0l8vsue1Ik5UzDLoSLsV7cq2HGBVTWXdl003adxqwpugvp3u0Vb0a8RlOC8Ywul2hAPKWohgaCdGxBaCTqVunmvXTX5I68k8oSYqB9yHGFhh5L0qFQ8QnuyMzm6Wl72G-fsTD25SJkA4XU1KnA0xMz6ZOcbv46tA7WFQ-OyOQ7bbMDbGj2XU2On6-4eTxNKIYzQzUq_vbSuCenC0DhlUOHi_lzoLpw1OAzJ-FICmLU23bpFCeJ6HETodC5v9BVycNj0u6JTMVYhCR5z8isGN-f7LZ165g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
ما قدرتمندترین ارتش جهان را داریم، به مراتب. چه کسی دیگر می‌توانست چنین محاصره‌ای را انجام دهد؟
🔴
من یک محاصره دریایی انجام دادم که هیچ کشتی‌ای نتوانست از آن عبور کند. برخی تلاش کردند. خیلی طولانی نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/129032" target="_blank">📅 09:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129031">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbwBW8nYNjjGRBBZDoQUPjoe7tm5LtfHVgFNPoXEHmnX03twq6hNYOX59kpWj-8wS4FaNISIY6G8QzScb1-6mCj0_se9Qd8jSrpR2R41JYDWQZpBBtt1RUvxm9kQv6pmClPn9DBW_aW_Eo2nEVAKhWvfl-JoPRQQjq94GSybp7AcuT2QytCRLgPw04vJXa8KPmRjS1og6jwYXkTDch-hif9hm6EF8ae43EUFlMfikDJbrDOeWeC8UgiEcgWluZDsNBX0EqIS4IgvlaC0pmv3JTn5iVhw1hue5suAWUMu_0-rcgSSc3l8wYMqIzDCR6O8ZXsBFLZFTdOJz7aS0y0GJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لارنس نورمن، خبرنگار وال استریت ژورنال: اگر مذاکرات، بعد از چندین بار امضای یک یادداشت تفاهم، باز هم لغو شده، واقعاً این سوال وجود دارد که آیا این آدم‌ها اصلاً می‌توانند به یک توافق نهایی و کامل برسند یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/129031" target="_blank">📅 09:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129030">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5caf5451c.mp4?token=G53bm8TfwnDXxCP0GUe4RQ3nYAx9sUt0kB_MkT8eLTTv88UxhGt1DZcS27cNrvrYxENnvH0aM3E2S3W3iZpNYTbrb1xEOsWO_mzH6fdp9UsKGwJUGV2Oj58NmaXnr-rLLClBzGBqzvioq9hvhaattFChh16DdVSgAXf2UOu-DPTeSN1rHEPbtOZxCbGV8rqF4Sf7TIxviT6vWZDgNuAj0oTa5jDK5hghcAlbjzwxX8DhLmfIPI_mcC-U953-IsHJj4FbnvhMpQ5l412DaoPQpILPVxSyLwyATnsV2xjwIVpYUg4Qaja83T8iCc6-Ht9kTlCQG_YUOFyt7NhDobYyE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5caf5451c.mp4?token=G53bm8TfwnDXxCP0GUe4RQ3nYAx9sUt0kB_MkT8eLTTv88UxhGt1DZcS27cNrvrYxENnvH0aM3E2S3W3iZpNYTbrb1xEOsWO_mzH6fdp9UsKGwJUGV2Oj58NmaXnr-rLLClBzGBqzvioq9hvhaattFChh16DdVSgAXf2UOu-DPTeSN1rHEPbtOZxCbGV8rqF4Sf7TIxviT6vWZDgNuAj0oTa5jDK5hghcAlbjzwxX8DhLmfIPI_mcC-U953-IsHJj4FbnvhMpQ5l412DaoPQpILPVxSyLwyATnsV2xjwIVpYUg4Qaja83T8iCc6-Ht9kTlCQG_YUOFyt7NhDobYyE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیا موجودات فضایی واقعی هستند؟
🔴
جی‌دی ونس: نمی‌دانم. این چیزی است که به خودم قول داده‌ام — حالا که یک سال و نیم از این شغل گذشته است — که از تمام اطلاعات فوق محرمانه‌ای که درباره همه چیزهایی که درباره یوفوها می‌دانیم، عبور کنم. هنوز این کار را انجام نداده‌ام.
🔴
این یکی از آن چیزهای عجیب است که وارد شغل می‌شوید و کارهای روزمره بر همه چیز مسلط می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129030" target="_blank">📅 09:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129029">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وال استریت ژورنال، با استناد به «افرادی آشنا با مذاکرات»، گزارش می‌دهد که وزارت جنگ ایالات متحده درخواست ۸۰ میلیارد دلار از کنگره کرده است تا هزینه‌های مربوط به جنگ ایران و همچنین هزینه‌های غیرمرتبط با جنگ را پوشش دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129029" target="_blank">📅 08:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129028">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suGaZfbl1W3swyxcq6Gi2rcjb5ApFuLAgI-1Q-YMoxwsy0523zCjutzryzkfNd0K14I413t5VJ8D6swgPMbLKQKQOXeb1RivN9w8SFWdV9U1JbGMtvXFpYzqpfvfRiLeTr291HA2igff2jzkKAXycbq2WORXPpNCeQTX2AdM00RNLFUt_Rg2jSISFHH_q_bsVsgqfjtyn0SpjhXf0IUoFt2rdpmKIqKGBMvs6z1mfhWx5-7CzgjYW5KkCEbkxkoPXIXG_sg6aJPdNPbJyGpCI2ygcc2FcxiqMZ8axwI24ITzKzLb7youdsqLRDhd0qLvkNSFtNnUzR97Wb-_7iGfJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: رهبر با این متن موافق نبودند ، شروط ان محقق نمیشود . امریکا بعد جام جهانی از برنامه اصلی رونمایی میکند . اگر اسرائیل پیشدستی نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/129028" target="_blank">📅 08:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129027">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سخنگوی کاخ سفید: معاون رئیس‌جمهور امروز به دلیل نهایی نشدن برنامه‌ریزی‌های لجستیکی مربوط به گفت‌وگوهای آینده، به سوئیس سفر نخواهد کرد
🔴
هیچ توافقی فراتر از یادداشت تفاهم وجود ندارد و تنها درباره گام‌های بعدی گفت‌و‌گو می‌شود
🔴
پیشنهاد‌های مطرح‌شده شامل تفاهمی درباره موضوع اجازه دادن به ایران برای غنی‌سازی اورانیوم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129027" target="_blank">📅 08:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129026">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ به اکسیوس: من برای جلوگیری از تبدیل جنگ به رکود اقتصادی جهانی، با ایران مذاکره کردم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/129026" target="_blank">📅 08:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129025">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdFNr1C3dZOM3Ziib22EDqN-zEjaBUcBbd5acYF4teo7X0el3q2UGfhUKWDeMSQ0K8uSjKNGWceRUMvNHOukoFOqc9uZmGojVz1TXRngVlq4gmyArajoBO5ktmmQrNVKikVmSKHg-3zf6wAKc_VYYk3cMBjm4aGnTkfvWQV3S1hznBSDRCw7ghQDoCwc9zfT5UCb4AKl9i5TZbQhqTn2nLOBH5fxa2r9kF8iFd8_DuA7F2gV-Z9WvVGHJ3m9MRAiXsgRcBiLyaCuRh4uufVFt3GdpvM4jqzyLIma0VMJX_xpoecNPXWOFhCTZIj8aZFVYZ53swMTmP-fhrQBZSX7CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکای نیوز عربی به نقل از کاخ سفید: ونس به دلیل مسائل لجستیکی برای گفتگو با ایران به سوئیس نخواهد رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/129025" target="_blank">📅 08:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129024">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikhwRUwfkdl24gn9AcpMea_f3s-F2ikCsvYECg2mcNCpH4d5CI2MrTNwNtU_q9RgoTQZQKl4P9k5z9E627aQONgoQNGmtfgj7O3NYWSMnw8CC9pO66NIFDukAErXm2QuKb9EcSZSDcxX1rnN3HZBAoVsa55DNO_MepfvfAgmKRSwRXpPtly8kTR-8IxucjjPQ4oGXwWRHZrGQR64CXP7Q4ompCUA1LPGNJx-Bpf1eyzz_AFzvIZ08X1rBQVzm3liQ7BDj2UPC1TG1gcJUlzNvr2uEa4t37WVtrcGlkWQx9Cq8s4NBBERj51y9sYvjPy6qZJtYZIFzgOPyiPwT6E26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که ترامپ همزمان با لغو سفر ونس به سوئیس منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/129024" target="_blank">📅 08:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129023">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ به آکسیوس: یادداشت تفاهم اخیر با تهران در واقع نشان دهنده تسلیم بی قید و شرط ایران است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/129023" target="_blank">📅 08:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129022">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ به آکسیوس: یادداشت تفاهم اخیر با تهران در واقع نشان دهنده تسلیم بی قید و شرط ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129022" target="_blank">📅 08:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129021">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64fe1a0123.mp4?token=Z5adHSZjSR3haWllUcN9NP9WNuqwZKldRSD5ZoSpvYhfcHLS6uTaVBC5WWfO7s75AplSg8RENbY1g_gawHA5UcNBhBi-SqlChzHxoTsx4q9M9FWSmRowSk1qp0j_bMydaw-EvWo7ChyVCyO8uOSbkXvFENRJ5XJoKudnnqeX50yGzx8qlGjeg64hrg8qK7OGUjY0G2KcDhbPEDtD-7HKGitCcz_F9uxl__aaa51iaaz-8lKkJuG-nlcSeks-YSV35U9eWlIejLqvq816myLEcVtHysCkyjYqt-l53HszpQbWomvK5S9p59yeZaVjO4Cr2OiiMzU45VqQLaFn8Qq3MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64fe1a0123.mp4?token=Z5adHSZjSR3haWllUcN9NP9WNuqwZKldRSD5ZoSpvYhfcHLS6uTaVBC5WWfO7s75AplSg8RENbY1g_gawHA5UcNBhBi-SqlChzHxoTsx4q9M9FWSmRowSk1qp0j_bMydaw-EvWo7ChyVCyO8uOSbkXvFENRJ5XJoKudnnqeX50yGzx8qlGjeg64hrg8qK7OGUjY0G2KcDhbPEDtD-7HKGitCcz_F9uxl__aaa51iaaz-8lKkJuG-nlcSeks-YSV35U9eWlIejLqvq816myLEcVtHysCkyjYqt-l53HszpQbWomvK5S9p59yeZaVjO4Cr2OiiMzU45VqQLaFn8Qq3MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی وانس در مورد اسرائیل:
گاهی اوقات مردم رابطه را به اشتباه توصیف می‌کنند و می‌گویند که اسرائیل و ایالات متحده اساساً همیشه همسو هستند.
این اصلاً درست نیست. ما کشورهای متفاوتی هستیم. نیازهای متفاوتی داریم. جغرافیاهای متفاوتی داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/129021" target="_blank">📅 01:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129020">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c34df45c9.mp4?token=jF34ZIFy4xcD2iQW92hZaBm8OmcqkA3FMrMi21aD7buyCYil-IckdWG2jTJ6W0e315SgxkctS4_h63sMJl5evXHDt1JD56b3NzcG1dkdKTsC8hozYFgEk7Jni9vqhHQD6MpaEW9L228nNbg0EODSIyCPVu8diDy8m4VRyW1KkW8qb170gFq_PrSn-WW8dZSxaCG-R04eMxBUI4v95usmLCwcE8xCtOmhDaRgAbiwUj_st1HxUnSVrlAsfJuRpLh44jEDeURV8_-9TRHZK5S8PlFA9mysFzQZpxj6YKJkRcu3dMBAVjAVMaorq8t_yr5rAfNs8FsZGBDtbk78I2KtMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c34df45c9.mp4?token=jF34ZIFy4xcD2iQW92hZaBm8OmcqkA3FMrMi21aD7buyCYil-IckdWG2jTJ6W0e315SgxkctS4_h63sMJl5evXHDt1JD56b3NzcG1dkdKTsC8hozYFgEk7Jni9vqhHQD6MpaEW9L228nNbg0EODSIyCPVu8diDy8m4VRyW1KkW8qb170gFq_PrSn-WW8dZSxaCG-R04eMxBUI4v95usmLCwcE8xCtOmhDaRgAbiwUj_st1HxUnSVrlAsfJuRpLh44jEDeURV8_-9TRHZK5S8PlFA9mysFzQZpxj6YKJkRcu3dMBAVjAVMaorq8t_yr5rAfNs8FsZGBDtbk78I2KtMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
: آیا به اسرائیلی‌ها اعتماد دارید؟
🔴
جی‌دی وانس
: من به هیچ‌کس اعتماد ندارم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/129020" target="_blank">📅 01:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129019">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVJ4vlMmWssMzwZ5D8llSEtkfXW3apjxO2bfok--FbQHTPMSr2ZBbsqaj-i6cMhEbO7bSzJsOUMPINbjOxxpb20o4OU9jF8t-9BuUupkKVid01gPBfII8WbFVEEWwfFTMS09I8jDCtFBAYhyTMH1Tw2HuO-N2wQQfGF5zUImZgyyWtLqnEWDMKWaL0UhB4yjCYbk62F49DEKCTQ6JDsnl-l1ifJPUAjPdIhvrZT2T_LZXWO8Vkc7jaSoXlh3NpybPk5b6-Y4dBijDBUXeZA56lhDdHFdHbRdLYB_uGG9CzH2KybaL8EQgLl66okwYfBxsh5rsD7wTuEFy_YTAtt-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) در یک قدمی شهر مهم و استراتژیک نبطیه
طبق گزارش MTV، تو محور کفر تبنیت درگیری شدید بین ارتش اسرائیل و حزب‌الله جریان داره با سلاح سبک و سنگین و توپخانه. کفر تبنیت هم حدود ۴ کیلومتر با نبطیه فاصله داره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/129019" target="_blank">📅 01:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129018">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44ee1e7683.mp4?token=R-eJqBo-NnB5sNowKpEERrroObUT2wA7_L3LLal3Lvj4es9v605GF6E469WLHTKODXxdzxxrzBmpdDXvZsj3Rd7VMLe5SxXmqpyTmy2HOBO4t8vrBzcKcj879LJmOaF2MlLKHhSIjzp2TrrPpM-HNJCuyC4xUb2jfsDyfZfsWr41JUxJYKMU2XMFAW-4dcS0FlgfQ6V2DqyJTD8j76n8M-eJKbBAF_mtoe4-UPG0KOd9oZtdXkv6HJbL7_83NOxXExrdiHYW5T7vh67OPxNbpYjTH4s11aSW0DI1ZXz-7hZVDwHRmxb4ZEk4Bf3PuhMMlV6vQdgwiaKmH4RS1z8MmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44ee1e7683.mp4?token=R-eJqBo-NnB5sNowKpEERrroObUT2wA7_L3LLal3Lvj4es9v605GF6E469WLHTKODXxdzxxrzBmpdDXvZsj3Rd7VMLe5SxXmqpyTmy2HOBO4t8vrBzcKcj879LJmOaF2MlLKHhSIjzp2TrrPpM-HNJCuyC4xUb2jfsDyfZfsWr41JUxJYKMU2XMFAW-4dcS0FlgfQ6V2DqyJTD8j76n8M-eJKbBAF_mtoe4-UPG0KOd9oZtdXkv6HJbL7_83NOxXExrdiHYW5T7vh67OPxNbpYjTH4s11aSW0DI1ZXz-7hZVDwHRmxb4ZEk4Bf3PuhMMlV6vQdgwiaKmH4RS1z8MmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در راستای اجرای بند یک توافق، حملات به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/129018" target="_blank">📅 01:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129017">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رئیس‌جمهور فرانسه امانوئل ماکرون درباره ایران:
شما نمی‌توانید از طریق بمباران به تغییر رژیم دست یابید. آنچه من مشاهده می‌کنم این است که افرادی در اطراف رئیس‌جمهور ترامپ، هم در حوزه سیاسی و هم در منطقه، او را به پیشروی بسیار بیشتر و قوی‌تر ترغیب می‌کردند.
🔴
تغییر رژیم در درجه اول هدفی است که توسط خود مردم به دست می‌آید—حداقل این چیزی است که ما باور داریم.
🔴
در غیر این صورت، نیازمند عملیات زمینی گسترده، ماه‌ها یا سال‌ها جنگ است. به آنچه در افغانستان رخ داد نگاه کنید. آیا تغییر رژیم پس از بیش از ده سال موفق شد؟ خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/129017" target="_blank">📅 01:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129016">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHokiCxGcMGG2EITx20hFBBlEwj0ogzH6X_PWs8KsbEDj3MZyw1dE56eCSd9y175mxGwDaogAky-PMDFHamI1wk1m5u0WULPGeYPHWcwkfhXc25Gm-eLASOsu_la_ZyFnvbCjRNbPZGwrc-D993tEyxXLG9kNTKMeFnCIHjuES2prFf4hNOUhds2jF7igcHu_-wURKj__WJrW1psUNMAFClEyTmOY00ZZiygMkCXUqmRCQJUL9_yge4B0R8JY23jrzDJfJmTwsFdqUuBhocsru9e_6ddNnGI5B7dJBhiLz2PCcF2yD8ltHCjavoVMKK8Y0fIyS3IcmxLiFDCYzXKZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکی رفته ویکی‌پدیا و نتیجه جنگ رو پیروزی ایران نوشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/129016" target="_blank">📅 00:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129015">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f21d642d.mp4?token=mMEGOy0d1RHhRJ1eO4Tlufe5f9iK6wjIiYOLvYf00WE-semNw-mmW7TKbcKsYc7x8Dig5aeCnpppEfunXP7-l-OGlA6Gg2kUUONhCwm8d2CPyqG4f7Am_l6MtkNoR1Hj57l75sfiGZd3Gi2vVWD986h-K4m6DtPUkIGpWS5CrrPN_gfwPWxKVGMXKD2vysmfKLbS7riyZOLKH1_bNtxfNiSTSbCilKHABXW66s_h0gTHV-KgbmjQ5zmnyDTEojlflXciwSfyLCk92Tf1IHB7bEprV7nU-x534Ts80I2cWc07p4LDkF8FuSfJVHXmoI-1wnCXhVEG5SPifIHfDVeIcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f21d642d.mp4?token=mMEGOy0d1RHhRJ1eO4Tlufe5f9iK6wjIiYOLvYf00WE-semNw-mmW7TKbcKsYc7x8Dig5aeCnpppEfunXP7-l-OGlA6Gg2kUUONhCwm8d2CPyqG4f7Am_l6MtkNoR1Hj57l75sfiGZd3Gi2vVWD986h-K4m6DtPUkIGpWS5CrrPN_gfwPWxKVGMXKD2vysmfKLbS7riyZOLKH1_bNtxfNiSTSbCilKHABXW66s_h0gTHV-KgbmjQ5zmnyDTEojlflXciwSfyLCk92Tf1IHB7bEprV7nU-x534Ts80I2cWc07p4LDkF8FuSfJVHXmoI-1wnCXhVEG5SPifIHfDVeIcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من فقط از طرفدارهام خوشم میاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/129015" target="_blank">📅 00:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129014">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b055dff63.mp4?token=Q_Zq9Agp-GFyJsl22nQ1Tieivx5k3U36NSTzzIeROOADpzYHh8QZPLM2wQdmiZIDVUuAhi-w8r02nE17BK98_-wTx3vfXZuPYMnT-uGkQhEdDCVJK4SMch6xCFySEvp_5H60tW7_QWsW5F3q9nnNZP_w1azDVPlm3HYsNPowHzvr7N3r0gp3mBxTz22MzhCNNFHou-_FCxM-4cSuOQXp_k8c1a7dA0Aj64EHMTkKn5GBUfXTluJ4BqefB2kiHwhJw9uqmuRDDMO1XRaBHTRam25L3-N6ygIR4gvNDwJvp-NiNOEeibwpfhHAl3Cooyvx5E-QxgWzwZ7_JQXm-RLCdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b055dff63.mp4?token=Q_Zq9Agp-GFyJsl22nQ1Tieivx5k3U36NSTzzIeROOADpzYHh8QZPLM2wQdmiZIDVUuAhi-w8r02nE17BK98_-wTx3vfXZuPYMnT-uGkQhEdDCVJK4SMch6xCFySEvp_5H60tW7_QWsW5F3q9nnNZP_w1azDVPlm3HYsNPowHzvr7N3r0gp3mBxTz22MzhCNNFHou-_FCxM-4cSuOQXp_k8c1a7dA0Aj64EHMTkKn5GBUfXTluJ4BqefB2kiHwhJw9uqmuRDDMO1XRaBHTRam25L3-N6ygIR4gvNDwJvp-NiNOEeibwpfhHAl3Cooyvx5E-QxgWzwZ7_JQXm-RLCdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ: مدال افتخار کنگره رو میخواستم به خودم بدم، اما بهم گفتن که نمیتونم و چیزی پیدا نکردم که واقعا ارزشش رو داشته باشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/129014" target="_blank">📅 00:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129013">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f440aeea74.mp4?token=pDWCDGcdsNOnUWB9SlHgO2D2CmpM-Q-LfL6e4bpob0tjdnYTsAfGcJTJihRiU8pjZnYmoy-Bqjmx4N1l0csFbjSMBo39TV1jw3Lu6ZbB1my6t7UgRpYhgaG2UA00yGWi6VstLPFzuo98MG7_lf-gWP2mdGe2XvVYqLBv6Ka9xpshUEDbG-sgzmulcPRsj7np52hGJdA1HtISNAzZh-VfEJTQNx14NeaX4sz-xYe8FY3TXXaNz0IEhjDIeQu-hxexiZsX4_4iUhXMdBPyWc2GThd7DRKYO-wZLhnEQ-Nw9jv3zA2VBy0sZHrf0WnpWc9MQVHwZ5GPQzYzTM4nxKAcfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f440aeea74.mp4?token=pDWCDGcdsNOnUWB9SlHgO2D2CmpM-Q-LfL6e4bpob0tjdnYTsAfGcJTJihRiU8pjZnYmoy-Bqjmx4N1l0csFbjSMBo39TV1jw3Lu6ZbB1my6t7UgRpYhgaG2UA00yGWi6VstLPFzuo98MG7_lf-gWP2mdGe2XvVYqLBv6Ka9xpshUEDbG-sgzmulcPRsj7np52hGJdA1HtISNAzZh-VfEJTQNx14NeaX4sz-xYe8FY3TXXaNz0IEhjDIeQu-hxexiZsX4_4iUhXMdBPyWc2GThd7DRKYO-wZLhnEQ-Nw9jv3zA2VBy0sZHrf0WnpWc9MQVHwZ5GPQzYzTM4nxKAcfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ:
پيت هگست ، اون اخيرا چند تا پيروزي خوب داشته اون قراره خيلي بيشتر از اين داشته باشه‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/129013" target="_blank">📅 00:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129012">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618be4eaea.mp4?token=M9MfPikSdzB9BLlDpWLWCd-z3JGflgAz4BDUcjV4nn5X7Gt0ern8lRFwaQRcewH8DgzV--87YN1A4m29o1826Yg9zL1_m5oJbP_qElDu_qEJI99RDMGksKH40kAY3nEtyiNbJG05q-KvH_Cp6mrFLCVqCKEUmKM8Eukoh5UiZc-FdmGweoJf210NQGe-bLT-WhXisF_PIQeGXBToSf5L6iVc_7bMwNlwWbv9z1UJymirJDkoQ1oz6-47p0h91HC8fM1oJl6Yh7wVNOG2h0wB6IbNxDkdhKJZjFQtfJkL2oplX9PfwA4q-xWSJChS_iUIYqHQhcqEHPgF7eFxEgNSw2yrIVTRDON17B4l6sSdojTUXlRnHHGxCvfliH7thkBzifbZ5UKC5i-afQVnaKHOQXZvCeHPrcslqKQJHSbCTdIF7XKOIn3o5PZJLdK46dbfRm7WKA1LprjmdNWg9hynH8EBePe0Z25MwpbXv-EE-FjJlcoXw7wMBFTnouPCTFq8Bo-dkWZEF3aYxpgcynwmISDefl-kUy30GRymbBguYL0OBX7hme3Wt_dDUa2yTznVvliyQOztdU2N7W84rqRIlPasZCv_mTLyseCUYLCsZqrGfk3_mGZ333eZppz-1t5I8Wu7HY-9ooDy0SFwLXIc9dihWT34plZyCE4IqxSNnsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618be4eaea.mp4?token=M9MfPikSdzB9BLlDpWLWCd-z3JGflgAz4BDUcjV4nn5X7Gt0ern8lRFwaQRcewH8DgzV--87YN1A4m29o1826Yg9zL1_m5oJbP_qElDu_qEJI99RDMGksKH40kAY3nEtyiNbJG05q-KvH_Cp6mrFLCVqCKEUmKM8Eukoh5UiZc-FdmGweoJf210NQGe-bLT-WhXisF_PIQeGXBToSf5L6iVc_7bMwNlwWbv9z1UJymirJDkoQ1oz6-47p0h91HC8fM1oJl6Yh7wVNOG2h0wB6IbNxDkdhKJZjFQtfJkL2oplX9PfwA4q-xWSJChS_iUIYqHQhcqEHPgF7eFxEgNSw2yrIVTRDON17B4l6sSdojTUXlRnHHGxCvfliH7thkBzifbZ5UKC5i-afQVnaKHOQXZvCeHPrcslqKQJHSbCTdIF7XKOIn3o5PZJLdK46dbfRm7WKA1LprjmdNWg9hynH8EBePe0Z25MwpbXv-EE-FjJlcoXw7wMBFTnouPCTFq8Bo-dkWZEF3aYxpgcynwmISDefl-kUy30GRymbBguYL0OBX7hme3Wt_dDUa2yTznVvliyQOztdU2N7W84rqRIlPasZCv_mTLyseCUYLCsZqrGfk3_mGZ333eZppz-1t5I8Wu7HY-9ooDy0SFwLXIc9dihWT34plZyCE4IqxSNnsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: بازار سهام به تازگی به بالاترین حد خود در تمام دوران رسیده است. حساب‌های 401K نیز به بالاترین حد خود رسیده‌اند.
🔴
و قیمت نفت مثل سنگی سقوط می‌کند. به جز این، روز دیگری در بهشت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/129012" target="_blank">📅 00:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129011">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9fx2Iws5B1SOnfUTfE9Ii9KaUTC4VDyMAwydDwf-EwNqZ46sUZXfGAMRNda6aE8MPRAWMiWTNIFyIuvj_0QzNDI8ZOw1S45F5W7-bSvkwT35rFr9vjgLKtxItFiYGx8BViU9stroawDQT2rIoKA6Xca1OXK6Jpi9NhhzuYumKb9xwt3QRBZuZLS3ydSqyAyVpOtTHWeBJs-XdZTfK9iXDG7hhTquC7TrUkFoE04il-E0VfNHTx5GZuAN8y9qngRkPQCEHyfzRsbAJZl45yIQird47T7dXI6q5D27IIhUng3GlHNVmrDi8bavNCMy5e83AhXfWMBzjYEbvuH_Nkw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس نتیجه میگیریم با جابجایی کلمات در اسم محصول میشه قیمت رو ۲ برابر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/129011" target="_blank">📅 00:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129010">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekmj780GuazYBWdm1BNWF2Jyc4xD1e1EFuu74DpyhkNKSgVQMjzZ8FXHty9gGWMmMc-jIhchngjQJt7iLzCJGgSA7VYZ2krkMqxGlH07drLEm129ESBHTb3hXAc3zhMIZV8PRhqdOybEu-RiuUsIiixlEfnackSxorHw2nEFXU3p334hr-5UeJB3ATqL9U5u3xcFHT84hd4o4HRBQle3PjjZN6R6kaojFlqjbegH2LN0i3gQw8divou0PIqJvPDXokhUVACB5hI0BbJfBHXn9A5BgA7EowwBZwBaHuSZpLU-_6foq__OUcKgiPs30KNeM2vK8W48JCF2A1dYgGDeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله عظیم پهپادی اوکراین برای دومین بار طی ۲۴ساعت گذشته
🔴
تا کنون در این موج بیش از ۳۰۰ پهپاد شلیک شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/129010" target="_blank">📅 00:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129009">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره مستقر در تهران: «اطلاعاتی حاکی از آن است که دیدار ایران و آمریکا در سوئیس برای فردا جمعه دیگر برگزار نمی‌شود، اما مذاکرات طبق تفاهمنامه ادامه خواهد یافت، هرچند ممکن است به سطح کارشناسی محدود شود و احتمال دارد بازگشت به پلتفرم قدیمی در مذاکرات صورت گیرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/129009" target="_blank">📅 00:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129008">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
معاریو : مقامات اسرائیلی از شکاف عمومی بین ترامپ و نتانیاهو که ممکن است فراتر از کلمات به اقدامات عینی از جمله تأخیر در ارسال سلاح‌ها، محدودیت‌های کمک‌های نظامی و حتی اقداماتی شبیه به محاصره تسلیحاتی تبدیل شود، می‌ترسند.
اسرائیل معتقد است فشار آمریکا برای عقب‌نشینی از جنوب لبنان و حریم سوریه تشدید خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/129008" target="_blank">📅 00:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129007">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: اسرائیل در هر لحظه برای عملیات مستقل در ایران آماده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/129007" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129006">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10a67b46ae.mp4?token=RaioeafvovgwxYo1F507tSEQhnDxqJhKsiQgwK4gN2wrXQLCZ1ZCxzH2oUnPY0gc_DU4eajBFUMe6ZDIL9UCkXF3JevVVyLtYr9dbGjFwy0lLKOS9WKu7gKdcrCteDw_fs1n_gig7gsMUoFCAUuqIafFo0I2KcngI2EGx1ycqXnSOoPSVIogn_qbyeAOnT1yFaw310GRIF7oA2CbFnJCN3R-YOT82Q5BnXPAeEhYBpNSIXBC5gnuyiw5E6pHfN1zBmL8gDSpRCbBSZsog0eAwRqrq9T8y8PpOOOgmI6mbi95FbeQbzO2ifacda3NuB8IIBT8ihsp8c4eKQQhN3QvqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10a67b46ae.mp4?token=RaioeafvovgwxYo1F507tSEQhnDxqJhKsiQgwK4gN2wrXQLCZ1ZCxzH2oUnPY0gc_DU4eajBFUMe6ZDIL9UCkXF3JevVVyLtYr9dbGjFwy0lLKOS9WKu7gKdcrCteDw_fs1n_gig7gsMUoFCAUuqIafFo0I2KcngI2EGx1ycqXnSOoPSVIogn_qbyeAOnT1yFaw310GRIF7oA2CbFnJCN3R-YOT82Q5BnXPAeEhYBpNSIXBC5gnuyiw5E6pHfN1zBmL8gDSpRCbBSZsog0eAwRqrq9T8y8PpOOOgmI6mbi95FbeQbzO2ifacda3NuB8IIBT8ihsp8c4eKQQhN3QvqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوباما
:
همان‌طور که بی‌قراریم، مردم به دنبال خشم و تفرقه همیشگی نیستند. آن‌ها به دنبال انصاف و عقل سلیم و احترام متقابل هستند. در اعماق وجودمان، می‌خواهیم راهی برای بازگشت به سوی یکدیگر پیدا کنیم، نه دور شدن بیشتر.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/129006" target="_blank">📅 23:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129005">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / ویتکاف: بازرسان آژانس راهی ایران می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/129005" target="_blank">📅 23:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129004">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_Khgl8tqNT_vCKS8qZkPYHVJgEdU5UwTBOmUdOL1EnMKHgEoWJVqLb4vXwLH5N0dDPQ8hLI7H0ztvaO20Kw1sOsFrItrvyYLIGe31qKSZzh4N55Et06nkQXHC4RWwUx3TpokEdb7UWbE01qw5BlP-09ObEWctoTOqmHP9ygoFI_YddvYAXlSFSWoC3g_A9EPjj0Wk9p84gfOTtZC4L-S9Am5CnhZRwE7QX5RenvGBOlL_xyBreUqTt1ORHUMLklbM4xMbTxxln6jLVVgB8lZeI1H2lrIFjZTfQu5PambQUCTCnJCBd7cPtos_jnrMLii9tCSBQhq-EIVOU5ioLaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اداره دریانوردی بریتانیا: تنگه هرمز اکنون باز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/129004" target="_blank">📅 23:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129003">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">مردی در یک شرکت بود که همیشه پشت صحنه همه تصمیم‌ها را می‌گرفت، اما هیچ‌وقت نامش در میان نبود.
هر پروژه‌ای که شروع می‌شد، یکی از کارمندان را جلو می‌انداخت و می‌گفت: «این ایده خودش بود.»
وقتی کار خوب پیش می‌رفت، آرام‌آرام خودش را صاحب اصلی فکر معرفی می‌کرد.
اما اگر مشکلی پیش می‌آمد، همان فرد را مقصر نشان می‌داد.
همه تصور می‌کردند او فقط یک ناظر بی‌طرف است.
درحالی‌که نخ تمام ماجراها در دست خودش بود.
سال‌ها این بازی را ادامه داد و همیشه چهره‌ای پاک و منطقی از خود ساخت.
تا اینکه یک روز چند نفر از همان قربانی‌ها کنار هم نشستند.
رد همه تصمیم‌ها را دنبال کردند و فهمیدند فرمان از کجا صادر می‌شده است.
حقیقت که آشکار شد، دیگر کسی حاضر نشد سپر بلای او باشد.
آن روز برای اولین بار مجبور شد خودش جلو بایستد.
و تازه فهمید روسفیدیِ واقعی با پنهان شدن پشت دیگران به دست نمی‌آید.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/129003" target="_blank">📅 23:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129002">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
دبیر کمیته ملی کنترل و پیشگیری سرطان وزارت بهداشت درمان و آموزش پزشکی: ابتلا به سرطان در ایران تا سال ۱۴۴۰، دو برابر میانگین جهانی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/129002" target="_blank">📅 23:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129001">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سفیر پیشین روسیه در ایران: یادداشت تفاهم ایران و آمریکا یک پیروزی تاکتیکی برای تهران بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/129001" target="_blank">📅 23:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129000">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSUA0yP4nhFuhiMiM5vBcPq4_nXtEPw0yF2lGpo5eGnHm_Mk-R1PN8RwcMp8TlzonLW9tqJ7jmoZcEnw_ynGsw7mlRRw3Z3lgcNsDdwqOrA2qubS-ym_4SPtEoMDreSB-HmqK_cNWGmItLm9K9BWIr4vcFNWK7LAqu3wwqvDEg4BMHVbYfRaK9cRKJZVVTC-9O-WrrcL07Qf-eDKCMTbFJRT9ji2mlVx7XRLijFS8TRdgb8OVtVq19qbv83u4iIIJOSrI95hHfyvV2d8_ryieDU9oKZHOD0dN_Vf61aGJAL_lNjK5F7jH-AytRxrAxP8BDZLQsaMOC8AsIwEU1dmKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: شهید لاریجانی دنبال این بود که حساب گروسی را برسد؛ اما جنگ شد و کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/129000" target="_blank">📅 23:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128999">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s4cMs13fg-QidMOiCEQJUqeCJ61tnN0GqmYR_XSmLHqaF3CzhtUw-wO3hJ7MUjJITL-Lx4jC__lgB9itclmORxkYlhcgXv-fu4_h-vcsq3dFl0d4PPOyyJ5j8gbpzVL0LgylUnm13mcyA0lZ-fc8byXXRf1b7sRCnYHh1R3YpdNMQyis8XI6sQJmNP6BXbko2ZBCzGWjR1k6jGJ4kroEfYVi-aQDYG1YAj6-shW7h2xkVSAFW9RAUC8-khjaCvRgQTmzOzYIlgCHhskt9kLzjuOUXyKIcjX5CfVOCXGXWGWKQsQxBUzBkbp8f3YtXVYUEoKb6zc8qQQnJRzcTa3GLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه مدارک تحصیلی معتبر از «دیپلم تا دکتری»
🎓
مدارک رسمی و معتبر  هستند و قابلیت استعلام  بصورت نامه نگاری و آنلاین از سامانه های مربوطه را دارد
قبل از پیش پرداخت ثبت نام شما انجام میشه و تاییدیه سنجش دریافت میکنید
سپس پیش پرداخت واریز میکنید
✅
مؤسسه راه سبز تنها مؤسسه صدور مدرکی هست که رضایت ویدیؤیی متقاضی هارو داره
صفحه تلگرام :
t.me/+2yeLgZeivDkzNDYx
وب سایت :
Rahe-sabz.com
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/128999" target="_blank">📅 23:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128998">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مسئول سیاست خارجی اتحادیه اروپا: ما تحریم‌های مختلفی علیه ایران داریم. اگر توافق هسته‌ای وجود داشته باشد، فکر می‌کنم کشورهای عضو اتحادیه اروپا در مورد این لغو تحریم‌ها بحث خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/128998" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128997">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08672f5757.mp4?token=VqvvUoXqf5NHKFxY3pOyhloy88q2v07CSfwReO0ayb59qqGQdk4P9sytL_dzOS3gIW63FxKC5xooemjcBF5bslIbY4ovBH2Zw2Aii_DH7Avp8-sTccuK_vlP3r8LfSLD90lMVPE0XH4ka8FHhH94z2Zc4j3EeRs1_2U6EpqC1UaAR8t2JICzHkykSchCEcSGqaCcZ3QFVizdajOVpFLqYPslUXHRKNCO53v8XkU7an6aMjSnlp9PG3S1xrFly0BHb98dRaNSUbn7lSoVa0wvv4k8KBL6Q5QNt0nirxvlcixZ9qZg105ZLKgO3zNjsPovtOujnqQBEnLUXWZpjKaSyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08672f5757.mp4?token=VqvvUoXqf5NHKFxY3pOyhloy88q2v07CSfwReO0ayb59qqGQdk4P9sytL_dzOS3gIW63FxKC5xooemjcBF5bslIbY4ovBH2Zw2Aii_DH7Avp8-sTccuK_vlP3r8LfSLD90lMVPE0XH4ka8FHhH94z2Zc4j3EeRs1_2U6EpqC1UaAR8t2JICzHkykSchCEcSGqaCcZ3QFVizdajOVpFLqYPslUXHRKNCO53v8XkU7an6aMjSnlp9PG3S1xrFly0BHb98dRaNSUbn7lSoVa0wvv4k8KBL6Q5QNt0nirxvlcixZ9qZg105ZLKgO3zNjsPovtOujnqQBEnLUXWZpjKaSyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در جریان حمله امروز صبح پهپادهای اوکراینی به پالایشگاه مسکو، یکی از موشک های پدافند هوایی عاجز از رهگیری پهپادها دچار سردرگمی می شود و بسیار دقیق یکی از از مخازن سوخت را منهدم می کند !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/128997" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128996">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
شریعتمداری، مدیر مسئول کیهان: با مصادره اموال آمریکایی‌ها و متحدانش از طریق تنگه هرمز باید غرامت بگیریم از آمریکا
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/128996" target="_blank">📅 23:10 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
