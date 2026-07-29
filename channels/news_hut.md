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
<img src="https://cdn4.telesco.pe/file/tii12tyDIUX0tYNVbOdNprZNALc3QaI_S2unNAZ9L21VapsfkSipwbXxvhKrncfo_g2jQCGjqRjlS1jtsKijNKHsEBYdpaPdZTttcFwIJ_oRLzDDeZwxMvWrGTaQqpwbUVbA5O-zN9hXSwDgJx-hPmgWongNbmoDpKI-Tw2lfUSsxs7sJvovM_ZvQZQrRKmq429lKt9_mEmcGoGrfZc8BfFsWyTEhixEprGRegjrgyvvWZZRWDdGy_HGDyQOTz4vU2XFhGP58vWonSBrfvPwN9aakEUgBMjsaZg7q6M8ltyX8Qg3iw4AhNKN9zVoPv27jzMKxc_SKkxbcHMS1crInQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 142K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 20:16:35</div>
<hr>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA2dEwq0WLoQ_8QFAaYMdGzLbmXI8PiQ9iuWeUFS3q0f9T50rpv8d0oaPhISJ-fmBtJK3TAg8MajvCsWBqDfasrZk77dbSN_JISlo1ueysptnKIDpJaR4lLcOBN7PuIzGBfokIW5WFWnXBfuIWnvEGBwo1Wv5knQtgJhyHxkOpMPWGFCtx952aqjtkjZ0Q2Wi3c6xEzdSwWxzm4-0tkP58tiuSBOe1Tq9F1StYUxV9uLmpidR5jBRWX5VbYiL4OvcTpSrwz--qEADxQa_AvAelLPUzfSqgLUa4WIPwdOl0kmKT_-H679yb3xcl9kw2tM5dZzYGxTOzAQaz1ari3_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=dc0vCJ3XS4z3pRzzzl8Umrbcwgw8QQH5Szurizwbiroaz_ZjW3wTRNYPMceOhOocTbVMOq19bEdiUQkYVnPbNaLkw7ADyt_4k775o-VdLrdib7pB14Q6DvWldrSWdU4oDNVq8TQYcOMeCX9j6Jg8DphcAxX2SRtT3E7rynQOXAIiNLBPAagKdzj3MhW4dpjCEZI_Cyq-GwFkvhDaPgLxPk-kwFf3cWVnSAIvkJaWVGI6Qm7z1LHLUtpAZflYtVscVuIOSolHpTrB7wA02DTkES0fyffNeVLR6byjXlX7VC8fZBJ5yxSStM_4RT9oFZAIyzxx8B2z1F4y177DODV3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=dc0vCJ3XS4z3pRzzzl8Umrbcwgw8QQH5Szurizwbiroaz_ZjW3wTRNYPMceOhOocTbVMOq19bEdiUQkYVnPbNaLkw7ADyt_4k775o-VdLrdib7pB14Q6DvWldrSWdU4oDNVq8TQYcOMeCX9j6Jg8DphcAxX2SRtT3E7rynQOXAIiNLBPAagKdzj3MhW4dpjCEZI_Cyq-GwFkvhDaPgLxPk-kwFf3cWVnSAIvkJaWVGI6Qm7z1LHLUtpAZflYtVscVuIOSolHpTrB7wA02DTkES0fyffNeVLR6byjXlX7VC8fZBJ5yxSStM_4RT9oFZAIyzxx8B2z1F4y177DODV3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=uJwZxi91e-S8nvioUP0RB16AC85GtHnDasgH60oqb_HDo8OX7X-GC8Rf6crko_7fEP6N5ERSOZNevM7P7Xw6aCeC_ukbbne5sUfwYFZwrXl5Fzb8iM-478u-MZov1qt70Z9CR0wAR_MRQ8kxQp0nybgDG_nmefq-4dliHqU66Bp72icFksSYuCLmlv4FN4DXrM7C5hQw9j35Okj1mVPEA0UDMSEkgCKD6WXCctqebmJFQX1ID9RLJ10i5925mQawHHxUirXvop8Dpr4dzRW5MgY9E9cAeMYbglRjIdDoZvgjE1FBcTZNQhA8pOFz5cIRcHjRD2xZzU20pt-7Dnrv8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=uJwZxi91e-S8nvioUP0RB16AC85GtHnDasgH60oqb_HDo8OX7X-GC8Rf6crko_7fEP6N5ERSOZNevM7P7Xw6aCeC_ukbbne5sUfwYFZwrXl5Fzb8iM-478u-MZov1qt70Z9CR0wAR_MRQ8kxQp0nybgDG_nmefq-4dliHqU66Bp72icFksSYuCLmlv4FN4DXrM7C5hQw9j35Okj1mVPEA0UDMSEkgCKD6WXCctqebmJFQX1ID9RLJ10i5925mQawHHxUirXvop8Dpr4dzRW5MgY9E9cAeMYbglRjIdDoZvgjE1FBcTZNQhA8pOFz5cIRcHjRD2xZzU20pt-7Dnrv8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgRtorgWp9Ci8LaGTgdJtYeXlOEuDbcOA6IqKUe_ZOl-tcVaW8KR3DUYRDVoo7VKjQG1mu7h-6wKbo48XCg2tz4xw0d2w2tftc9XP5P43sKZrh6Lz_U3TbgjYk0VKDeKRiTD1g8QS5SWqKXomDEkzhYswL6zzRLUnRBar_j5Z-i_r7_IRRmtQ-oIf4fDte1xDueJyaPuRBmGn7gYqMrvA6KSKtqPMBF-uDB0a1t4H0bfveuURWegx-uk5lspP2D16rYRjQ69DeipOU5iabznGYOaZJ8LGwzrRHrREQqWGUYirlnRVXmX2iGWCrd04ddKDnL1Ra97uqYpofKYQ-upHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNX_bokSQAccR6kVHVtR474LHqOT503rw5_BHNFmPDgh-9onXXhj4aWTaYYIJJLk4BkUNuNCAoi0ESrGTI_mbG5uYdXIYrkXoAp1m56DaK3aG1PmlwP2bbO_NU3EKuf4dfvjRnALafAdSojIP13HA6vouFLQojtPpJBZ2AAQ24ntS6WIZ3qD_e0008met0oMEqQ7lFkiPll4ydg8oqCOwMaGJXAwyLTnZtSc0Z-gnPFERsFsZu8X728rG1hnBNxmI5LD9rNVeE9x4L21LF54tyAxhtHqP9iTt23U4sQHYh7VFkg_fRCCgnMXgQqA6koJV6qwBnS8Bl6C_aCwdyXl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MycRyAoWngXUzyWj0oKSRjEdj5Ia7IYP1qltZbNyVIOMuNAYJqcMe6smIG2tHabEUl8DjYhIyHs-uQ9C9y-Z0IO96hquwxW_mVdV8putds-RXuGe8UJQcRf6o8yfYwa2wqbnr4Rh4wpLwtu6h50IBrmfvbs623i0zqP8csCd29jsp2KHsf3XN_yCjT7LHKVM5eVtxGxJdBTTX3Mq88izNe0xZWpKpTDhKxbkU9qe6AFqX33erP-wh4PPp_IQu_PgTd7-nxjlkI3_x0Z0CZPRH6B_wJRcw50twa3whNPwQ1rpDF3IaKh45Efme3dPLmrzzfVXFDvar95UPql_Xg1NHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5BUkmqrRa0MpGi5ErXFKI-wILaVTYNDACrYEzty5lLiIfhJ28SgufF_b0M21RRnsrAM3lm5ZXFziEYt0wakRTbOyhjd3cHDZ8HtfB4VVndnDijytM9DZnpXjkfZ3UZczy3WeQsxDHah8z-20Gi61rDnKBVrjuPTNVqPgWDiWDdSrp8eam1SDkn9It56TYRWe2EhfpCuM_2Al4MMglpBMn5Mxp8lF9cm4dyuKza_KmPlZ8FhQMPLFP3X1hAoDIgJ-xwoAt1htOvI6FKgAQ0U_l0zmKyRjfEU3dHoauQkLoagCDLHW8Wg8U1qpwOS1njgQdxN6PqC0tLsQ7ZRWeNJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=T-a4B4LICphF-fuepJ8qVXVMUJsDcimtEl20oCpu0wYxHEfO_B5GpefiCEx5Oawt18OS3wSgVhZTrpbZWfNtDH-1CxVQsX8nrPPG8TE5JwZaFgn9hs_RKIDvjVbI1_L97SBdKZpdTlwiK_N2YVXRRwCBku50IYWbutlbZDKXwnDvYUlOoadMLnwX7k9ZXrvQGBM_qnp_pr0_5h6iqVpfdXac-kXSk160W3B4a24QsrOmATIyskX-EjLHFK4-ExJedHOLKfy_hEBWFMX3gVv3jdk2-U3WnALVp52wFUBpN9MIbXnWy5N0IY1U9KSPiiI0apYQUAeywlDDsicnTUYkTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=T-a4B4LICphF-fuepJ8qVXVMUJsDcimtEl20oCpu0wYxHEfO_B5GpefiCEx5Oawt18OS3wSgVhZTrpbZWfNtDH-1CxVQsX8nrPPG8TE5JwZaFgn9hs_RKIDvjVbI1_L97SBdKZpdTlwiK_N2YVXRRwCBku50IYWbutlbZDKXwnDvYUlOoadMLnwX7k9ZXrvQGBM_qnp_pr0_5h6iqVpfdXac-kXSk160W3B4a24QsrOmATIyskX-EjLHFK4-ExJedHOLKfy_hEBWFMX3gVv3jdk2-U3WnALVp52wFUBpN9MIbXnWy5N0IY1U9KSPiiI0apYQUAeywlDDsicnTUYkTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czrVqqFWjtdfPIgvGzUiYT2jcyD1s5TLFmmPkm42TnjfI3rs6JajebJzsPcpC-zVl_8vnxNqhhuUGTYZccnRuxDnuDRpqxNSm8DVj_Q0zS2IfnEJDTRDr8r1w74QTvxQ3s81LnAhO0EO_EYzbcwRjdDFzN7AeXJMEcyk3xbeHUspQYy7YJ664jEmAAluQxm7wl8hGLIcHVkZnfZFxjzjifkuIpQeXJZ_sjvEuCWbVV07cmxd9o-hO3djJz32czoa15uf0qq-kvbZu7lRjTP81GQY8KQD_9wsX-msG_pM13irT1zFJHpos57jbc6Spqr7Uw0ls5nn-VoDE3VFJdzL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=o0hf31UDR4vAvJi8fWk4DKLiOirMAlhmlS-Apq87P_6q_W6JatOfbv08I3i7d2l4wcq7l-jJ4iZ3nEJY5Ity_nQuNyv3lCzr7uDERsUS2LfaESZ4TxdV6Pt73pRKec4GCGpr84mr_Zj1BYO2PxvaupWGpGmkmXRVabUGWvCfXUf-3ri8xYPn2L_AGNWHsFCHsBrcR2Vtnfxqv14DeDQ3xBuJT6vMsesN8OCfOY5uelGpF16hC9DZ7FC2DS6Z-33JnRo2afu3cqhoWj3jycEv7eGQ6kEU-gqmydCtRVADugdrxA73dgfy5mYcklJLIuqFcHDw5mdXJHbCcBDFA19c_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=o0hf31UDR4vAvJi8fWk4DKLiOirMAlhmlS-Apq87P_6q_W6JatOfbv08I3i7d2l4wcq7l-jJ4iZ3nEJY5Ity_nQuNyv3lCzr7uDERsUS2LfaESZ4TxdV6Pt73pRKec4GCGpr84mr_Zj1BYO2PxvaupWGpGmkmXRVabUGWvCfXUf-3ri8xYPn2L_AGNWHsFCHsBrcR2Vtnfxqv14DeDQ3xBuJT6vMsesN8OCfOY5uelGpF16hC9DZ7FC2DS6Z-33JnRo2afu3cqhoWj3jycEv7eGQ6kEU-gqmydCtRVADugdrxA73dgfy5mYcklJLIuqFcHDw5mdXJHbCcBDFA19c_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=axBO2XWuaCc8uJ1rkPCrz8s_6Yo1TVdnQWZofAQIpAv7PLv9-fzqKGda0HcQ2yyvzcd53FLDbe_RBbtu2gHO4j6Yz6y8gFLtuI13YddLgmxzwv5Ut5uENZ9fNEHtStj97aBz3pIX5EZCyOdWouPwbHinzvA3y-Fr62UQhCA7gJmGTQL6FiBUUs-_Ugl8iT9G3ehTKJGsvMp_yNEkXiQIQ-A-1JU0sfUWtf9gknRMh77DS6MzW3afgFbrb8LIKqFOccGYvy3xmDgOqG08qSl4u74JsZZEWQgvJeZ6jZaUqgvwkp0-1OF0_Tc1vSQXtyP3NiSHbRkmdwGF76nLaj49Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=axBO2XWuaCc8uJ1rkPCrz8s_6Yo1TVdnQWZofAQIpAv7PLv9-fzqKGda0HcQ2yyvzcd53FLDbe_RBbtu2gHO4j6Yz6y8gFLtuI13YddLgmxzwv5Ut5uENZ9fNEHtStj97aBz3pIX5EZCyOdWouPwbHinzvA3y-Fr62UQhCA7gJmGTQL6FiBUUs-_Ugl8iT9G3ehTKJGsvMp_yNEkXiQIQ-A-1JU0sfUWtf9gknRMh77DS6MzW3afgFbrb8LIKqFOccGYvy3xmDgOqG08qSl4u74JsZZEWQgvJeZ6jZaUqgvwkp0-1OF0_Tc1vSQXtyP3NiSHbRkmdwGF76nLaj49Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZNIaNZz0Oy6Lm9J6RG6BdrpZiRj5dD1OBhv766NuxrZKYvBWbcR4Nn7TOZIXz5yusN3Wvr3s3rYY_al4h1kQtitZvIJ5vonjj24XYBBVKFSEOdOmJCJFmmG6TXVBRbeUqFW0w8CVTktKgmrYz6NBe7cLO4Zj7FAtaw_HFviIf7e9KM0M2VSmK8avbf061BeDV49m1j854gIw0ca1QTSoOgE_f1S-GBOu56YEExnqo-iGk7-4N_XUKxPV7UxSXV7mRjDoGACS2pbZsp-uooFFSijSa-SDgdAqIuCSWvzC4NxRKRHrYlmsDu6dbOVv98pkGsQlptRwmbz5nmxkUB-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=rWvjkMjZH_yH8hutcze4z4ihEwq0mTWfe87xGKHgpRpJYwmXD5bFK9iZT7fiP5pMmTqB5qdGK75YcP-W4_ha4ety-QQfTF_XQlj6yYLqI_gd__SLlt7y-1BiNVL-iNLihVAGRW744RpIDSVXfbVzhlKgw7IXCTUFYwUZVw77R_wrWzuPeFc_cDvgZCTUbpCck7Eqjw1ZCU9tf4qUwZWjIMNRsVJTsX4374Zm6r_B3ASkYTbK8zzU67llcoaYHyhSEwYTFnrb3sv6u7uSFMbj_4tPr2c7zUDR18fmhNdcw5rzvR5Sd_GiYrHGfyzJcJgDjqX1sc1ZdxDiQd-XmfZnBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=rWvjkMjZH_yH8hutcze4z4ihEwq0mTWfe87xGKHgpRpJYwmXD5bFK9iZT7fiP5pMmTqB5qdGK75YcP-W4_ha4ety-QQfTF_XQlj6yYLqI_gd__SLlt7y-1BiNVL-iNLihVAGRW744RpIDSVXfbVzhlKgw7IXCTUFYwUZVw77R_wrWzuPeFc_cDvgZCTUbpCck7Eqjw1ZCU9tf4qUwZWjIMNRsVJTsX4374Zm6r_B3ASkYTbK8zzU67llcoaYHyhSEwYTFnrb3sv6u7uSFMbj_4tPr2c7zUDR18fmhNdcw5rzvR5Sd_GiYrHGfyzJcJgDjqX1sc1ZdxDiQd-XmfZnBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHaZ4pTdSy8L4GDtzgq4GnqLZhHPz0n8DygUwG-GZjHu90UeeXueUQf1FbK35nA2hz4WnU2e7MS9NPvbrPamhfVP8FBnsmSAjmqsFmejPSur9ROAz3ynT_T8O58XYYWelTFf3-OLRdvQSqDQALz40pq9XMRLOB5ErZUseDcQa97p0F_R-_LENZrL0VYP-1NlEZjbbjiyWP3WZObfwCcRtLJ9JNgsJDprDUJpT5q0S0BNALmi_cU55E6SSf3U_EPblMYThI2y_u0-IDXW0Q721w_aTjxipSy--jD9A-IW0QM5aVCunJ1z69KunBYP-PoQd0MNtbS1-odawd_NrXRVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuKddmUeErh1O8tH7ywLcdMiQPhTBbnMySB2rxAqxlp9L4xDfHda4E4xbc4YpyHJD37ue3W7S89RalUt3pLDppSgygmzcHUAvY5Hfu59iFbCl2rB-hKpOrugDMJOgI8aM15kZpxIwDRV8j1md-Su8dxcuD0ajhmItndLImYahpWcHIkxmOcDdYFGNTFwGYf-D51VlshM6GF4rPUDWHO4FMSW76tMNJdbsHThIJA5Ei70qtz4rIW8YOuI7nWcZA90WFbQAgYy3I__EpwvOwArZOTOSdrcdtfAV5HZucp2iQXuThxKyz9luc9LxAqXWRXnixpWtJxoKNFVyawPN0vY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
وزیر خارجه اوکراین به من اطمینان داد که
حمله به کشتی ایرانی عمدی نبوده
و اوکراین هم
دنبال تشدید تنش نیست.
ایران هم قصد تشدید تنش نداره، اما
به‌صراحت اعلام کرد هرگونه حمله به شهروندان یا منافع ایران غیرقابل قبوله.
خسارت‌های واردشده هم باید جبران بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=X2996PbZI241PaIn25W1YiTQPgIDmu2uJGDsM5ATid3YVhcTMxyFBBk9SpiAZ_iqMIQDOb6mLm5yMQyQpshqX0vpMWiUvR8Rf1MQmcXqIDg0gGwXL59Y0xJzMEHvWu9sAEeWXJoPa_DiJuZXG5j9qGFavj90O2Z4_B7ECM0wnenmK381cihqNm7mFHpJDxoigK03cfULKZC_gSM4ayOEv09_oC1kMZ_qebWDxk3ISeR09kV129BCao6fKABL4q398JM48RnGN6MuQ49oF_4KpqXIUsR47wIdke8r0oNfLCeMPvfR-DVd82qQWQ3hCw3DAeihZf6QO3nRDTAiDcCVxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=X2996PbZI241PaIn25W1YiTQPgIDmu2uJGDsM5ATid3YVhcTMxyFBBk9SpiAZ_iqMIQDOb6mLm5yMQyQpshqX0vpMWiUvR8Rf1MQmcXqIDg0gGwXL59Y0xJzMEHvWu9sAEeWXJoPa_DiJuZXG5j9qGFavj90O2Z4_B7ECM0wnenmK381cihqNm7mFHpJDxoigK03cfULKZC_gSM4ayOEv09_oC1kMZ_qebWDxk3ISeR09kV129BCao6fKABL4q398JM48RnGN6MuQ49oF_4KpqXIUsR47wIdke8r0oNfLCeMPvfR-DVd82qQWQ3hCw3DAeihZf6QO3nRDTAiDcCVxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuQfLyQa76fPWCwu5JFDBEu5ufsePzg4B0sWoEDceRPmUwECyevkcubRKElyU6SGU5BAHaDr5hmrB903DBXj59UMQ0C-1Efdra_bQrL6mY-MxxkGmIP7PTkLOfMWtDNdhbpcypfnnXvVndXtww5NtSHtc4Hwjjh5exkFNnATEB_N_NDZ5LEQvBKeS4idLsxZ67YE43o80pqGHzVU9YMLfWcAZPA-QjIWGJZv7qee55fu1OwkFgNK0ofZy6bt8DkdQsxlrgZRrQOMtMZdYR9PwVCSyPfSkrRx3xA4Y0253zKmp2mJ_sX7ZfFds1dmXiw8XlPldr6PO5lG121PJ40ySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f04q5kr_inKjUkXA-fAxRCi0JXJ8pFOnyfaxpcUVLtAEaapfW6xO1J-ybL8cy7MV61pV1JjZYBX3_spztVUk4ry2-YukezZvrzcrmILosGPB30bOq99FFnpAbtWeB_FnibaePcLA8ou8LplY6mL6WE21iOUTs2c9XBmgM-dICtCsVKqOHhyElA7Iw2HWO3ljXLNOJa_hmLcZBtsghbWMwsl7kjL__FRCH_D-DFw27yZbJpe668F5RC59DMEFkxscUy2Z5PrKjkRH3aQBNPP3QhzrcObB4NuYt-ekpZfJQjsOQOR9SR9ruT6Y4R3kruCnCisqmYDap9SnsURVsSW1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
نایا
:
موشک‌های ایران، همسر دوم رو لو دادن!
یه زن اردنی میگه موقع حمله موشکی به پایگاه موفق السلطي، متوجه خیانت شوهرش شده
😳
ماجرا از این قرار بوده که هشدارهای یه
گوشی دوم
که شوهرش داخل کمد قایم کرده بوده، موقع حمله شروع به زنگ خوردن کرده و همین باعث شده بفهمه اون گوشی رو برای ارتباط با
همسر دومش
استفاده می‌کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=nDyxe39lrg97YNMLWT-XY4i9OL0qdyr3HQPxFyBLWRxyA_aDZTHgDCyD-xs8FVw9JlNU8DbaWLBuFfnpqlVCwK0DLJFBTXQheGw6KhqokszQgWYtPebsw81arUbh6026juJHHP9aBrSodnfDn7qF39TfIBvTVLte5Zq0TOz0Vw1rxwNww_eFLCMqJjsrT-rFOO-z-JarDrs9RZbjABfS3gsT684JtRgh_42cicc2DteDs-mRYD2muRkc34BOEv30PnPhXJh0ICGcydeTBwXYm26pKz4hOE5h9IfWtlPv-7UQtbyVhDLWlYsOxK7WhWbrGPoNF_k2AdXsTFnk2jnV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=nDyxe39lrg97YNMLWT-XY4i9OL0qdyr3HQPxFyBLWRxyA_aDZTHgDCyD-xs8FVw9JlNU8DbaWLBuFfnpqlVCwK0DLJFBTXQheGw6KhqokszQgWYtPebsw81arUbh6026juJHHP9aBrSodnfDn7qF39TfIBvTVLte5Zq0TOz0Vw1rxwNww_eFLCMqJjsrT-rFOO-z-JarDrs9RZbjABfS3gsT684JtRgh_42cicc2DteDs-mRYD2muRkc34BOEv30PnPhXJh0ICGcydeTBwXYm26pKz4hOE5h9IfWtlPv-7UQtbyVhDLWlYsOxK7WhWbrGPoNF_k2AdXsTFnk2jnV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=dNMPk1r9DhONkAz9W9O30NEI1dsyiaCgaZb4MSXO3DVzljop7c5ANlkcnEXyILDEf2c_PlTU1idyP5VNkx6UBf5cRJHhcKm1hQAzmqsCFkGVUE2wxzFI3C7pnjTNMO-fHVD7Zqt116yu_CcFoygO8p1l9qu5wzCVnWsjkGnw9yM_gHy3VnOUR2RiWoLU5slgc9V63yKQGqbllD7KbmMm9eq4JVSv48pCCNVw3ZgKlXHax3xRxIov9jfGGssn35i7P1anCTDRBOBlsuDKyaG6MoWEaVZEMehjgzOpJvb2Z1BMk1qVi-r1YXyZ95Hlbh6P0dnQheXz2NEHGiYO2T3ONg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=dNMPk1r9DhONkAz9W9O30NEI1dsyiaCgaZb4MSXO3DVzljop7c5ANlkcnEXyILDEf2c_PlTU1idyP5VNkx6UBf5cRJHhcKm1hQAzmqsCFkGVUE2wxzFI3C7pnjTNMO-fHVD7Zqt116yu_CcFoygO8p1l9qu5wzCVnWsjkGnw9yM_gHy3VnOUR2RiWoLU5slgc9V63yKQGqbllD7KbmMm9eq4JVSv48pCCNVw3ZgKlXHax3xRxIov9jfGGssn35i7P1anCTDRBOBlsuDKyaG6MoWEaVZEMehjgzOpJvb2Z1BMk1qVi-r1YXyZ95Hlbh6P0dnQheXz2NEHGiYO2T3ONg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTGZyj8yLFc8tJ52ej5C2aIR8eLS-flrwkPArKO1nSj_64cv4J3N3ErQe_vXPXoCi4qRYRny3BtG1rKgaYy-76M_8tw1f5ltJctqAD93n6f25xJ4uMc2jaaN6kZN_U4qPRlUUVitfqqnKQ6uCAvOzmX1AHEQ10HT5PMCm1SYJ3G-eagNmpy40PUF8HCIzTslbcimV-RyVrpQj8WRdrVMme4ZelcwGu-rGXI1E9DPp-CxpyvSWwQk5tSibS53hWDN2iJjymLwfedb2dAVcKgxpJy3ypwHJY3DKva93lCd6rtxRHPLdKrpoyu80f89m3rLN4oj-ZpUdhWPUM1Uv33MfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=dPDzxlahuMJpkafG2r7kU4ZUQrdCS-rsoO8CVwB0phJK3PaI9BTIS5Yc9Ti6WJZpCV7RMAa9wcA-fbNyzKR9ihctP-zV8U8bynavIjFIF61qnppJk1itucCnVpHNisWleX--YD7nEMAEmygeEGNlgUc2MetEkXaZ4rzr65NWyhbNK9qjUGL5XUbVqiUj2YBlHVNS3WT-TvdV4X09yPuFgJiz5nhGE7VCDlWmZZUFzCSmsKhLJMeqsIMUO35ZMsCxFNHb4iulpYhPUDMMvIkcvIyrQBFvncOx7M-pr6SqwKiN1a7Wkw-Zs4pLlY-CASO9XCXmXA8Sy7ag4xiMzxrnog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=dPDzxlahuMJpkafG2r7kU4ZUQrdCS-rsoO8CVwB0phJK3PaI9BTIS5Yc9Ti6WJZpCV7RMAa9wcA-fbNyzKR9ihctP-zV8U8bynavIjFIF61qnppJk1itucCnVpHNisWleX--YD7nEMAEmygeEGNlgUc2MetEkXaZ4rzr65NWyhbNK9qjUGL5XUbVqiUj2YBlHVNS3WT-TvdV4X09yPuFgJiz5nhGE7VCDlWmZZUFzCSmsKhLJMeqsIMUO35ZMsCxFNHb4iulpYhPUDMMvIkcvIyrQBFvncOx7M-pr6SqwKiN1a7Wkw-Zs4pLlY-CASO9XCXmXA8Sy7ag4xiMzxrnog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=Nb4-OcNK3kHKYx8GJB-aAajx_ZnT47-kRMy4vTukQ9ysOSGr21cIaIA7-WCKEG8qES3-azIwmnbDmpZTCi7Wx5LLPZTPlIVG2Ld054N_EPhpflp8iJtpThE0B56kvbB9J6fbB3R_YOq547KH22En-oCHSq8b6liUB0Y60Q5IbR4pHu9CTzv_gmNq4S-H7lwaVMSeGLxcgWHhAoLw5RuOa_rghKLiC6NzRxa2JO2JIruJB7Ms0UcR3TfyG8dIYz4NzH6tY0odvUGQYKB0Jo5tXOAxS4KXbycYlQ50WvTqCD4HW1bcwE4Zp_YPW8lDkKOmP_iH4BkNvcytCXE7XQZu2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=Nb4-OcNK3kHKYx8GJB-aAajx_ZnT47-kRMy4vTukQ9ysOSGr21cIaIA7-WCKEG8qES3-azIwmnbDmpZTCi7Wx5LLPZTPlIVG2Ld054N_EPhpflp8iJtpThE0B56kvbB9J6fbB3R_YOq547KH22En-oCHSq8b6liUB0Y60Q5IbR4pHu9CTzv_gmNq4S-H7lwaVMSeGLxcgWHhAoLw5RuOa_rghKLiC6NzRxa2JO2JIruJB7Ms0UcR3TfyG8dIYz4NzH6tY0odvUGQYKB0Jo5tXOAxS4KXbycYlQ50WvTqCD4HW1bcwE4Zp_YPW8lDkKOmP_iH4BkNvcytCXE7XQZu2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=CpOTl9Ru1q4IqhLZGxv1sesR8YvEOwpXufgjM-tGHx--5zkqpb7hTJ18fx_PDzf0mDk-gB5osE6k80iGnGfVE9ypUBrVLFOGxftw3BJ3f2cHTbZYNQjEzZOnt5AVq4-JPL5_Bp33cnRmL-1b0mYNEpTQKlNo211jjL26EUhr5vKl7-2WiWpLG03gBenKit5MYnVUhA6VtyiYvcDOU0FKKqBTmjzMjO7sTpez1wcAcJHWvZMb4OScMloh6G1xXHWEZ-TFooKjVlrXGjtzYR2JLEO9KVg_DAAOz5HE1saGghCqTpKKCUFKmZWXyq8ZGRLPi-BLvQUvqc5T9Kjvi62e4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=CpOTl9Ru1q4IqhLZGxv1sesR8YvEOwpXufgjM-tGHx--5zkqpb7hTJ18fx_PDzf0mDk-gB5osE6k80iGnGfVE9ypUBrVLFOGxftw3BJ3f2cHTbZYNQjEzZOnt5AVq4-JPL5_Bp33cnRmL-1b0mYNEpTQKlNo211jjL26EUhr5vKl7-2WiWpLG03gBenKit5MYnVUhA6VtyiYvcDOU0FKKqBTmjzMjO7sTpez1wcAcJHWvZMb4OScMloh6G1xXHWEZ-TFooKjVlrXGjtzYR2JLEO9KVg_DAAOz5HE1saGghCqTpKKCUFKmZWXyq8ZGRLPi-BLvQUvqc5T9Kjvi62e4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=GjgLMCfY_w8YgKl_1-_0HBxvOuRkSlvW1uhN9swgXJxAhFE8AWsy6aiYgomR_6JV0NWgbYyiUGNHr6bxyZNeI_b5WlI6cvILmcRWu-GuXfMoDDnQrwzrHS6tjLekxMRHCmyBCbbCJLg202vZOvUYhj2WSTiw4ei3hZ8xsmY5FSr0i0n9yiOOkVVq7OXKC26J3kevOe1H7Vf-urxDaaM2E7Lg22KvS1ioUhhcqwmypTH8Mf_DwJrfSEj5ClnnwwXYmvTmlzw-36hPYtmrH7zIsWvpSiyY_LRwahEvSFoZorpV31ky9Q7M84lksr_5ni4lUDC-FrXuE0EPJrDDd0YISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=GjgLMCfY_w8YgKl_1-_0HBxvOuRkSlvW1uhN9swgXJxAhFE8AWsy6aiYgomR_6JV0NWgbYyiUGNHr6bxyZNeI_b5WlI6cvILmcRWu-GuXfMoDDnQrwzrHS6tjLekxMRHCmyBCbbCJLg202vZOvUYhj2WSTiw4ei3hZ8xsmY5FSr0i0n9yiOOkVVq7OXKC26J3kevOe1H7Vf-urxDaaM2E7Lg22KvS1ioUhhcqwmypTH8Mf_DwJrfSEj5ClnnwwXYmvTmlzw-36hPYtmrH7zIsWvpSiyY_LRwahEvSFoZorpV31ky9Q7M84lksr_5ni4lUDC-FrXuE0EPJrDDd0YISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opqO3KgW7-SX904MfPJ42at06ovJGvcOFB1QIP0ekmvac52IULmIl8kCSOqNYUrJEIyRyeKBQhS-RKhEgMtgVyFDioRzGC8iRnTjRZX5iHLkupJ-DMZUxoNjnVM5pM_nH3Hl0QNii05khV1TG0K2Nv9rpRBXbPgUebeG-RYnmOqnICfk5-aTlpiHVAiFYh3klZS40F8wuDpxARvPdV1kd6ZUFYZ3A6eWjnof5tBVfIwSxRo-LB1d71haoMiFgQYdXT6Ewbz9Ev_sUGK61RD5yCVmqL7XxJEfGmr0u3EDkcDx-guMFVnZS0Qa9Gv7o8NKbWk4Io7uHqZ3Y494sYutQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4px_G-eLizeSs8TH1BMHOpQjDLQtqFl35jfBcf6jZuG91gTRxs4cEI8K79Y8nWkc7lDx4sCTSnBs9SKaJIhocIDeW4CaWAGo-wIF6PIcF3yLAUSgRHMMaSaJID197PZbR6rp48u3kAqG7ZxRv4J9NVeb5qeTHyzbP0OcFlGWBT9fk4XnlaDS_5M0fz9o-Qt8CI1tULpnMNaeYu8I3Aw-NNbAlgPXWec5OhBkiukdnWfv9A4K5hf2ju6HEIdyjTgJhGJfY6u6SPvKMNqXLcEfFnzJmEp8k_olSMsUul8WWP2iou3lkZHD1tWUajIVwjAs2wYeb_9Fcd687Rk33uh7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=ahP-whn2zJ5kQkK_aw3Z_N4xfOLqXzoQlIKHySyLhG_CCGblTXuRPgJNf1xDwwsCnisfbWKmtPiAOf1K3r37-_N4K8dITWuLcS9OM8fBev7l-oa_jNkVLT07BJMSBaCIOwWXuqP65zdaWgN8ndPPUSNXfNWzoZ3Ah_nAGzPUd_TzoHeIhZPPdsN97MgTtQjWFQ1_xSNx8e_-KJSyORY2bpnXaD9FedEDH0x59UKuS_iNZrWMCnIh-A2N6lWyQ7Ir4GUdThYpw6XsyNeYS6kmtGQmipogJaC90Z81OPFp59mzYiZFtOJke8eWZ_kTKcM9nwTF1POUjkChI00uh1DtsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=ahP-whn2zJ5kQkK_aw3Z_N4xfOLqXzoQlIKHySyLhG_CCGblTXuRPgJNf1xDwwsCnisfbWKmtPiAOf1K3r37-_N4K8dITWuLcS9OM8fBev7l-oa_jNkVLT07BJMSBaCIOwWXuqP65zdaWgN8ndPPUSNXfNWzoZ3Ah_nAGzPUd_TzoHeIhZPPdsN97MgTtQjWFQ1_xSNx8e_-KJSyORY2bpnXaD9FedEDH0x59UKuS_iNZrWMCnIh-A2N6lWyQ7Ir4GUdThYpw6XsyNeYS6kmtGQmipogJaC90Z81OPFp59mzYiZFtOJke8eWZ_kTKcM9nwTF1POUjkChI00uh1DtsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXqwJdEvcREPpHgpEL-H8UU_fB5vrtQu5zEiIlpQL3VObbeUNEGuli6WgbXC4yOujZhvj6BRZMMHteAWuFBkCQgAH7Uzq3xCi0feEQCxW2oGyMLr8sNUndsKABC_gXs1KYs22LEKMXmwwCWlOemVf2CZEXZuCelUm8clks3UjbrBFqGR0CM7BYFOJzNALDbEXP8qtvoVqfsejtKURDf-L4IHhWZuBTaGwBYpRzZt_kQu2pmzr_1EUPSfD--SNy2JBXR5wj_Im7p2bmZNg50b6KU7Wsvsqil6Ucl81zzQjh1YVlrkUNDi3vOYaElpXumUcdU0UXjWAxQr4gnvMRZ_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrhkueXupZNEH_hojESJ8De-hJlgOK7srqnLRmWZXDVOFjO1Jocc_MLH3GwV_30Ja1kkT-S_BDB-xq-LOMhUlc4EXhoMiJdJm0ofJdIzlI9LILqAMhh1I8VYu9x8GGlwvBAUvLC0AuKLmpqBZOf8-xVg6F3uWSzTwa5_KMkt-6bUO-BbDxe4TH_LOKPGisoglNWE8mqZkmx0KqmdD1giHxNGJej3B4Zq0aK-5c49ygbDglFaBgBgxwijChEagbbvEfd4Bsv_6fm3frGFaGr2FqsBE_c2a-1JEGBdNVwNT19qvF7cuaKmz3nBI-QlmbF6p1s0EYIYMApaISnzjwhcGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QU5Yi4Icdk-VB4GOiVQ85xpnPwyf-DwEdRU-0jsBArB8Vz8zOu9t-wK6vgbG8HP3N-t_dxzYHWbMWRSFTAkeob7rsR8EQ-o9QPNrJ6RYVib-VLrv_oR26ots8Ei52oo78IuULXPRcC4dwtrTpZ0RoVnOmMZKjwVqxa_p5wstnwQlN0kVixfBs_o600m6toKVePmoKhFwpqotiXhaGAmqQKAASpFVgIEr8jaAjm5XdAR7xTb61t60HLSjiCAfhelg0Eom4w3n-vpuLFLis5MNJw1eekqkYBww2VhUeX5qtpPE8bn43ZVjtSgdzxXkh5xQTdwqUq3wf9Io9XMkWm04Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TSVKnySOb4iVOaaAK17Ng1SsRVk-iDZ_c1FZrIXFbmMtEq4AouOO2B7U_MMA_Ok35fyf7RL4LZaAfiap283uzuwvOi9eoSc43sFcj-bb7D_epbYfNUOGiG4QTEUfDCDsqk0dERRCTG06TccptUyDjRhK5zCHdAkojS0OQZuh75-VMCYq8g2t8ZhQSAfuSDhp3bNsXHjf9M2fPds3qZcXr-YOnMc_KuI4LqhO6aNfUyIW5I9_lbrljpyEYTP28PuXHL4jSt_2hFe3240caOwqQcBnDPcMq8o_ISI2JngZLasVDtRMNzSe28y69M7T2lrzP0lPzzw7WDAIKKnbloRk1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=utjI-x_m-oAeLG5m0NV-VKzvbYYNNcOvsdp2fQxduutTJ7eYGB6YMfuSC72vSnbi-UlCys-qFzQBAwg-uhgFcHySZn2eBze8IfpEjwfeNI2ouJqqBkgRA0cr1irlEErW0-fiDDYPPu_-lWw8qNmWjW6pLpHDCBmxR2Df3HhHmmG-Dl4uBZVsyA0q9hu_cSyCxr675sK4ukP5nLvhSgqZz001SiUfBERJGaERC4QT5d6MbmgBBdUyQmZemG4gr7Nb6ZjcIWd734yq_C17MJavOV2a6a4-X97MG3M7JuR5w5JgLISA4J3L5FqIZrsLuZJ6iniCGAE_TMsucCAX8o_TTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=utjI-x_m-oAeLG5m0NV-VKzvbYYNNcOvsdp2fQxduutTJ7eYGB6YMfuSC72vSnbi-UlCys-qFzQBAwg-uhgFcHySZn2eBze8IfpEjwfeNI2ouJqqBkgRA0cr1irlEErW0-fiDDYPPu_-lWw8qNmWjW6pLpHDCBmxR2Df3HhHmmG-Dl4uBZVsyA0q9hu_cSyCxr675sK4ukP5nLvhSgqZz001SiUfBERJGaERC4QT5d6MbmgBBdUyQmZemG4gr7Nb6ZjcIWd734yq_C17MJavOV2a6a4-X97MG3M7JuR5w5JgLISA4J3L5FqIZrsLuZJ6iniCGAE_TMsucCAX8o_TTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WxxiCJiFpejrin1J7SVD5ENyIQkv10DCBbGzJjYdl7d4uvpKlVpp3g-kz45w8rPkdEu8xDG-DwbpT_XrJ_ZfX8TDTZc2WXbHaPm3BZ-JQaDKMqLQT9tBvPMJ_IuT6Uyi4w7fE6E8Tf8HcMqI_YsYmDJn3fkON5rC1oeCUoqjJIrp6w43CUuY4fHuN2Ou_U6o064MjJbTCqOpheaM3scIaQREMjyU5tRHVhPbag7TexdtQR_3tPXt_KUeVS_LdQfSCtLa8sIm_tCbZOfX2_RF-W5LigR2UDbD-x-3NUCIDFjn10Joa_FSFkkBQ40K876TGtYSLbgiSfVqOWGIClgl2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=YeSwN59txENLUemFOYJgKYBX07ez1w82TC7-pAXsjgYScJxq6eVE9prJYDWPlQUYyHEkSFVW4nIK0jHm0q5xujwEM2HrBhlD5y9i2H-GdELyMI5LjuTG7feEa-8bdEhr-BQKTxOpt8Uqq2LQld5RrjeNmSxGMwVftCBcTq48AVP9uIFptNdXsIPg1egiNB8w4Z62GYtS7NP7puMsAOrCcXURfRbYTsGrzmWfWfuBlUe9BqqRaG-pyDuFKg2lACS1M3uo9y8LNFistg6ydynqdx-dFZn5Xs13wY3jlIZijxOjx2tLwktgyyB8SRTxnt4ZOleM5eDO14mHr4rcvlcafg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=YeSwN59txENLUemFOYJgKYBX07ez1w82TC7-pAXsjgYScJxq6eVE9prJYDWPlQUYyHEkSFVW4nIK0jHm0q5xujwEM2HrBhlD5y9i2H-GdELyMI5LjuTG7feEa-8bdEhr-BQKTxOpt8Uqq2LQld5RrjeNmSxGMwVftCBcTq48AVP9uIFptNdXsIPg1egiNB8w4Z62GYtS7NP7puMsAOrCcXURfRbYTsGrzmWfWfuBlUe9BqqRaG-pyDuFKg2lACS1M3uo9y8LNFistg6ydynqdx-dFZn5Xs13wY3jlIZijxOjx2tLwktgyyB8SRTxnt4ZOleM5eDO14mHr4rcvlcafg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX7iN_O2dEDNIsdynC2qPOuIV4NVaFOTIjvhQ9vfSUaj4kYzTGkQ8QfwHgs2Tl8309mCUHr8VB3U6Pxng3BmC6-sRRaKcI1_LK9ANvmKD8_caeh7-YsOT22_Vb6ON6dz9UnHTPaWwncKsw3qSRQkiHk7WvdTU27IPrHl2FoOIXZTywtmPw2KWjjgYz32oV8xpdm0rhdyDX-sLdXol1qMmsg9JsyJx03S2flHB4AJMzszJ2owqGhQKFt_zU_A1vNGNUbobl53OD7wMOyQe2kEm6Ewx8iutfuEi6Zpz71G1gFVu-1ojOKp2dvcim7Eqfa_NwJbey-W9jdzM3Qfet7iKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJeLKotjcwGYjWIpmeCANvBq8-cjwjAQD8TCmw-bd0JWcF6eivkGTE3b1Urxt7wq6pyEtj1BN58V4grec-T2CPFi-6KhFu2gp38daalH-So512yZ8IopAr5Quj-nN-04LQcNp0_ejVRaQlFXHlhgdsvXdDbIg4kJ9R5_0LsXRgjZUqoTdVYrF1N4Uoe3WWkY7ZRyokq_hNhPawhOAxSUgBki1HmM1iPJegobfeEL_aJWfyiIafosg5o4_GtFCY001lcCjQ7-MbdvhTSeq-2lpO6S9jG8-8uvUwQ2zEFurjl0Lvua7LdYjynVPSSFeHso-At7xJ7eevfrdmBK6TcmrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=mjARlRs8xHpUE6DMtpq5c-AGoht32PI_-H9HGGoTmH4Iz1XbtpootBnCGphIW44GPRyluWH0fe-4JJq3eVTp_PUzHx8UALPNdRai_JRfExhjW_xCk94hIlbF90CY1PJwZ0DQcPch4WXV-t8zpx1-9vKLwCMK9VnU6gjVvM-lIewxCUDjf_nwTMVPuQLuUtj8MADzQXWCdxwcc-O4rHbghbM10HkcnxfSclz9vJbdVHzk4qctpFyDrx3UJ6iLJ6IsEMpOb8W16tBg_EmGvE90IYV3hXN7D3NYL0RrIyjBn1fKHVsG3bJJzEspncKpRzO544Qs7E5dj_oVl0IUHtMqFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=mjARlRs8xHpUE6DMtpq5c-AGoht32PI_-H9HGGoTmH4Iz1XbtpootBnCGphIW44GPRyluWH0fe-4JJq3eVTp_PUzHx8UALPNdRai_JRfExhjW_xCk94hIlbF90CY1PJwZ0DQcPch4WXV-t8zpx1-9vKLwCMK9VnU6gjVvM-lIewxCUDjf_nwTMVPuQLuUtj8MADzQXWCdxwcc-O4rHbghbM10HkcnxfSclz9vJbdVHzk4qctpFyDrx3UJ6iLJ6IsEMpOb8W16tBg_EmGvE90IYV3hXN7D3NYL0RrIyjBn1fKHVsG3bJJzEspncKpRzO544Qs7E5dj_oVl0IUHtMqFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLSZjs3AnN-db-S8jJrHuM5S8O5yAsW_Hjbz3Z6Wojv7dsFyBOieCPKOh0tKrBcDGKwQKPG0GPBI5JfvHWDMdXnO6wQ_kEXcsyrUyw_iqWUXVQ1soDFI-MePkFqp79D_nV1VoNVep4ygyenXDYPx03GSnsEQwcGvIi8kktioQIjAaL81QRrxwKdu4684Q-vykmpTPMReoU1fmU5a8xlkmyLi5Wgp1oEF0VaP-jpv9q0qVVskg1CGDuEBK0RECkpio4DzehkUycpBSXnSuPQYFLvhUQDWzOtWrlGd9lItsLwkxyF7-K0jVuEejeLoPwR01HSfGc_xT8iOMqxkao1w0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=hGjHUoqPdeT1HXjs65iqabFbqM0FbdflaVcRPOdwzDvczRmSLX4MBQS-Qmh3SBiB30kA50UG9j3oRO8KF84Ki6ZYkYWYj31xwZ-sU9PzVmAOb59CQvKFr8sALaw0I2_gZZC60Gf8x2sYsVORHRN8y9AMADtOc7BsiEbDmW2yhXTynsUA560uAsyLwPZLNvCVGgCN8UeGgCdH1GSpqKw7xRvCBtmTa59E9tvmUFhJqlOF-j4ypQDHZotUOamibL04TRp3Dlv5yABkuNVBEGlIjh5GRd_BnPdNh4kxDqEKPTzshiSuB1aR_KHbpVkjFCX4kU8C74Bds4KxX-u6wWNKrEjEc8OERHm_UlOsrAic7EI_9bHgqEL-7VY3sAvCzDiEKS-9lpDck3xS98Bu0jxWTuYyS6DE66QdUqQTkF8jAUb0NzEW7PpeEwtRoSU20iL8Rq0CYDe5FJHrwLOqka53vA5Hrvv9pRs6qoo_yN8nGJ-pgsuKVzWR904D5rMlR2Ngk0qyBuzsh4M-21QRJx4vB-v10EHCTSeQv8owQ0gc8bwnil2_d7ZXZyYTXSF41ASzwMqmHqJSx2akJZj4fWWANPyenA4XgdgEd0rCUipp3ZEDf_zCM7Atkvcefr9TNgUBDNZWWF5tGOv1C_3kPK-4_GTjd4ElXjfrfadPH_LKacY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=hGjHUoqPdeT1HXjs65iqabFbqM0FbdflaVcRPOdwzDvczRmSLX4MBQS-Qmh3SBiB30kA50UG9j3oRO8KF84Ki6ZYkYWYj31xwZ-sU9PzVmAOb59CQvKFr8sALaw0I2_gZZC60Gf8x2sYsVORHRN8y9AMADtOc7BsiEbDmW2yhXTynsUA560uAsyLwPZLNvCVGgCN8UeGgCdH1GSpqKw7xRvCBtmTa59E9tvmUFhJqlOF-j4ypQDHZotUOamibL04TRp3Dlv5yABkuNVBEGlIjh5GRd_BnPdNh4kxDqEKPTzshiSuB1aR_KHbpVkjFCX4kU8C74Bds4KxX-u6wWNKrEjEc8OERHm_UlOsrAic7EI_9bHgqEL-7VY3sAvCzDiEKS-9lpDck3xS98Bu0jxWTuYyS6DE66QdUqQTkF8jAUb0NzEW7PpeEwtRoSU20iL8Rq0CYDe5FJHrwLOqka53vA5Hrvv9pRs6qoo_yN8nGJ-pgsuKVzWR904D5rMlR2Ngk0qyBuzsh4M-21QRJx4vB-v10EHCTSeQv8owQ0gc8bwnil2_d7ZXZyYTXSF41ASzwMqmHqJSx2akJZj4fWWANPyenA4XgdgEd0rCUipp3ZEDf_zCM7Atkvcefr9TNgUBDNZWWF5tGOv1C_3kPK-4_GTjd4ElXjfrfadPH_LKacY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=amrmvVTTu-00SQ20wpGPpAWR3gG3DcMmyk3lqieIBgRUKT0mA150yEFqkRWbZpBQ9BirrHsrU_18AajPa4CCclkfo-N7P5VkZymDcTQUkkpOgCwvh-A4ceJRZnCbzeLfU2TXMQhtqPM0XzTTb1C_NjLQaADbUzdREWGyZOvjWT682dq5NcWbnhgsFBP5cWUBL3TQcd-d0AWGSAZx3c1L-9r-yugD6XFI4sS23NBWjyksRunZSWEy7n9aCMMxNu6XIJCNE5RVDXha3eCu2TT04UL8GBAz6lYXctDI0XLtr8lTwwxcBHxWWZg7GIC1OiI_X2qJPLoAV2s3JwwS4ry8pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=amrmvVTTu-00SQ20wpGPpAWR3gG3DcMmyk3lqieIBgRUKT0mA150yEFqkRWbZpBQ9BirrHsrU_18AajPa4CCclkfo-N7P5VkZymDcTQUkkpOgCwvh-A4ceJRZnCbzeLfU2TXMQhtqPM0XzTTb1C_NjLQaADbUzdREWGyZOvjWT682dq5NcWbnhgsFBP5cWUBL3TQcd-d0AWGSAZx3c1L-9r-yugD6XFI4sS23NBWjyksRunZSWEy7n9aCMMxNu6XIJCNE5RVDXha3eCu2TT04UL8GBAz6lYXctDI0XLtr8lTwwxcBHxWWZg7GIC1OiI_X2qJPLoAV2s3JwwS4ry8pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCyFB6R8SNI3QLR6qCk_M4hYLNK5ZS7bxTc6w4zGNpKVKiCSzaRpbiFGSuDXjsDJMCqoo6RyIs1UtU-Bh6va6FBkUCOQa8VLBVJbbVhkS3mzR96IC2KepwNnGEv13PS0Wr-4UdZo3v5vhef4vjvOcqH9ta8ttuVuOAULU183e6qJRyh74MH-pU4oli-MAR3PbAUbW8T-yKbbiHHtXWOedBJqHm8s-ktSmTTgqi9iTy7B-mRazGkAHwtlwgpLcHJo9tLlWoiI10QoeEgUfFp35kd94IH28nWmuSso8qxVyK4HTrGg781YK0Fd729t1f9_Dl3Bo2ke9Z7ZqIBe3YJDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=ZMykjtpC12Ny6RGI2bejmfxKlC4c9ZO6FrB9Fh6bY3--H2dqRmDf2R_hw3yhyq_clWFHXrvG7Gl_q9ETvP1qW2gjLkv3Y9fcgge8ZvkQnX6pLRJGTC-GHJYxVvb1YP42mOxVhVPA6l_AB5bcC61C02pRKBsq2wqwCqholJBjZosBYd3dF2imea227NhSxAL4VBsezJLU80TOYiDDfd0Q8KbOfBrQlthZUntOgLForivBPip5QrCzAwMhkdH3sf7EoUJw3Ckfnx56OXTu2jTLwOl1E4PyLQp2a-S--5EfkTpDQ0oMYam3jpu2PmtaJEXTS6ntn_1AE2ViP9nNd4D6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=ZMykjtpC12Ny6RGI2bejmfxKlC4c9ZO6FrB9Fh6bY3--H2dqRmDf2R_hw3yhyq_clWFHXrvG7Gl_q9ETvP1qW2gjLkv3Y9fcgge8ZvkQnX6pLRJGTC-GHJYxVvb1YP42mOxVhVPA6l_AB5bcC61C02pRKBsq2wqwCqholJBjZosBYd3dF2imea227NhSxAL4VBsezJLU80TOYiDDfd0Q8KbOfBrQlthZUntOgLForivBPip5QrCzAwMhkdH3sf7EoUJw3Ckfnx56OXTu2jTLwOl1E4PyLQp2a-S--5EfkTpDQ0oMYam3jpu2PmtaJEXTS6ntn_1AE2ViP9nNd4D6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=eE8hw3r4V705030InC16cAocmS6nPj2F71z-QHyhXfoLhCSPWS7-1vcUKAI8NZxJyKKOhUd3e0UgY24o1avSTRmvcYKUovzlwyGyJFtdFw78pIpHyrqWK73I0TC7as7xWN3qzJ2uZ3D2VgHp_hEo4n3zBtokGPbRv8nkiXIErEtG6G6SG8jin85iwDZ9TdJpPA-D4OARPNbACOUtY5g3Hcd7m4gXesLTJ-vcJGq3DT1-E2LYrbjnIFTcUIssnzWUlXIFVDoJIHAtHKX4eehGrvFbbN4OIZ0eVtJruq4ethF0D2_oe1jLH0tovd7m_hV5PYBhSLma9Gc0BnvDD-DQ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=eE8hw3r4V705030InC16cAocmS6nPj2F71z-QHyhXfoLhCSPWS7-1vcUKAI8NZxJyKKOhUd3e0UgY24o1avSTRmvcYKUovzlwyGyJFtdFw78pIpHyrqWK73I0TC7as7xWN3qzJ2uZ3D2VgHp_hEo4n3zBtokGPbRv8nkiXIErEtG6G6SG8jin85iwDZ9TdJpPA-D4OARPNbACOUtY5g3Hcd7m4gXesLTJ-vcJGq3DT1-E2LYrbjnIFTcUIssnzWUlXIFVDoJIHAtHKX4eehGrvFbbN4OIZ0eVtJruq4ethF0D2_oe1jLH0tovd7m_hV5PYBhSLma9Gc0BnvDD-DQ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSEyyxOnB6xgc5K83AUMps7QNyd3oK22mvyUtQTEJy_iNZ-q1mfo2DmzxeKy5BiY9-N0rCXIQjFWF0CdkPtAl4VeR8aMlqSI75YrwUY2h2Q46fHrGFz6pQf2dIfHIS4z2qFYdDO3PdrTTyvLftEalC5YCFNrVEgGWD9Q1QJ8SqbZf4wHkh3dhBwVW44-zHKUqhr5XuVqwnhupGsPxEJy_dcvbtfi6rcviNtrqR05yf1ZrKriZA_WWf_1j5_bj5e7j2FckksVS4KD-E8E6Ja_Efz93bm1RpDvGV6ncsco23L4y6sXsg3Ss58psQ6g0EQi2o-xk9UmR16R4TkM6HLo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=ak-1PESDi_hwm86pDeLXjecf8x889veMBQfyObfCPA0Yey02nKPhU-2y_sCM6thRoyA3rTRfFpC8aXzxARBwtyKiw2Jbs0zPVlxeivXuIpFhT-7lkXq4DQLskaCOW2mdC6xvZBELvTMOPcJzasYOxbnCEZ97R8-CzvBG1V8hqkWdSlrD5IPMD-lTxJZ13AXLdewVuBJ-ALYWu5TWijYj_6MH5d0w5bzMJLhaQPMVO5jjHDCx3mYX3yEdKcUUERO0DVsWzk4bz1E0jHifwMgMiEVmPdqRubLAQievw5EHllip4626fpZNtnZfB11x56qyvQbxStaoAMN3pBjRj-3xRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=ak-1PESDi_hwm86pDeLXjecf8x889veMBQfyObfCPA0Yey02nKPhU-2y_sCM6thRoyA3rTRfFpC8aXzxARBwtyKiw2Jbs0zPVlxeivXuIpFhT-7lkXq4DQLskaCOW2mdC6xvZBELvTMOPcJzasYOxbnCEZ97R8-CzvBG1V8hqkWdSlrD5IPMD-lTxJZ13AXLdewVuBJ-ALYWu5TWijYj_6MH5d0w5bzMJLhaQPMVO5jjHDCx3mYX3yEdKcUUERO0DVsWzk4bz1E0jHifwMgMiEVmPdqRubLAQievw5EHllip4626fpZNtnZfB11x56qyvQbxStaoAMN3pBjRj-3xRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1hEYY01zLQYSCXaMrWXAcjY4ZyzaqXe_2sqbf0iXNpbOEN8WSp83CDZLd7k8VmRvJJMo31ql0l1udEkObueggYHBpnSerbFfGgUiBJO9Q7Wzm2vl6AgYPK016oPJJB5Eis8q14VOYLopwaOCXR5AVgbj4tOmvq2UBVvv7AI4kSUtfC9JB0vCQxWfu7GA2sOv6FMsW-vamfJxQWL2Bfnt-GMoY3o3F3dJp-XmmgEsJX-P0oGVf-CCN4Ge-TylEbVgqzdusk1qJEeErH8reKW8UIlobD7oPs2UWGNWrqgvUKPKKjMWnBEqupbcgvDbDWDK6SS3RSyKMt9F8d1YD_w2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6FogaGldPACdMPnnjpkfznLStLrxV_aQxDdmRF5yeJjB_L48ph1Hb7KRy4jSjYtJR-sYOfwdIfTcQFyHUYCVv8w6nb48LQL-uJPt08OPSE3NdDFn9RU1xBfY-U_ILUEj2DsxpgFJKzhTnFSd9-wmnOFBlZhCSO0wg-r7OKE2KuCYTnTa22QBhv0iSIEch1y80oKOvhMCzQwJbJL-mGkkglDteeAJXaxi9_IsIKWIP1lnKvpY-MfymhhdVatbmVddGexC5yl1OJaEWJ8WVvfOculljIjioQZlkyNsYFTm9VYDB38FVvtZxOh4o4ophax0Nwdkh1chke0YqYtP7pGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MW_VPrdPORgQkfqJvumb1KoHHMRv3mr1ELEbphy27sSTgxDyMXPfHSev0xWai7eFjnNjYcwwhbkn3xdkVVs8keZWVSLVWrGC8MRYQw-r_QN5xIETxRsjqvVCcHKSOEI_kMGRxqww_wLSDAKemR-wesXX5w5FXJHxiPk4JjtUNEktW7eG2cjG8l5ZZd29bBBJWgdUHyRvfrD6e10gZecBxVSmrf89abDfbFqwqTPLGZO80OUuPEaRQRShnMEqZ3ZtooNzdzEq36t62lu6CcoaTWLwovkOq8Mkd8MQ7AdQ8BftoE3BGre4t4LRtcGzsjuD1BeP_Sbem54jk4WNAkI7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آمپول لاغری زیکورپا(
®️
ZCorpa)
؛ وقتی درست لاغر شدن مهم‌تر از کم شدن عدد ترازوئه
در لاغری با آمپول زیکورپای عبیدی، هدف
کاهش توده چربی بدنه، نه از دست دادن عضله
.
📊
مطالعات روی تیرزپاتاید (مولکول موجود در زیکورپا) نشون می‌ده:
✅
منجر به کاهش وزن بالای ۳۰٪ می‌شه
✅
عمده این کاهش وزن توده چربی بدنه و سهم کمتری مربوط به از دست دادن عضله‌س.
✨
برای
شروع لاغری با زیکورپا در کلینیک ویهان
، پزشکان ما به صورت رایگان شما را راهنمایی می‌کنند:
مشاوره پزشکی تزریق زیکورپا
کلینیک ویهان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGFTfHaeWKgIq3JWK8u1DWpXqwON03uO-EaJU7AdDzPuTisvCZKsTHtjvpr082XgBtwMEcR340hWyUbVJNrXNEGUCWYEsPMhh16_LbAgEThPApBFCCDMhs27g8tt-xvXYsX-lp9qGAPw-r6QzwD2b5q7SFA-3n1mMTt2_4aueIW8Z-zBJX5uosL43lpt4CpMBgq8o9nzBxUt2D0jtZl6vsSkFbZyXFgJk7UBn33PESCW8XQfXbp0tWb2Nb4Ba6JTfObm1Xjqz8geNCNDgx4EfYNVRzN8oT0vS9rI9nT40djvBsQdc0gN9Wup1JStRvpaln3QvF8I18sxxCbuR7boqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=WVVJJ_2Sm-fxf01QVZEVvTWMNnH6aiTyPYAd4p-JRUY3wzIBe2lnYzfLa-yQDAy2i2_lQOwxFrkF44MvljXdj_VSlEvrgBCLeXr6DhWxep1gY5KYpc5kw_7znX4iOdCEceeBJhbpRoCxME2r8OJNPi6V35ARcY5GKmUcADsZfNcxJNV6mzufo7ShElDvFreQS6oE34FEwCJP39Bh0yXFNPShlE0xya8WgtoVlISG_UYZOutn_zYykx_0HFAq2ZtyTNAyKW8QTPUBjSAgWg50H1ip_BMaETfmBQq5bgoOKLyNkPiod6SCqZaFlICL3QylPPF_1lTbZSLqNW70g7dC1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=WVVJJ_2Sm-fxf01QVZEVvTWMNnH6aiTyPYAd4p-JRUY3wzIBe2lnYzfLa-yQDAy2i2_lQOwxFrkF44MvljXdj_VSlEvrgBCLeXr6DhWxep1gY5KYpc5kw_7znX4iOdCEceeBJhbpRoCxME2r8OJNPi6V35ARcY5GKmUcADsZfNcxJNV6mzufo7ShElDvFreQS6oE34FEwCJP39Bh0yXFNPShlE0xya8WgtoVlISG_UYZOutn_zYykx_0HFAq2ZtyTNAyKW8QTPUBjSAgWg50H1ip_BMaETfmBQq5bgoOKLyNkPiod6SCqZaFlICL3QylPPF_1lTbZSLqNW70g7dC1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Abpirtz7C4jdKkWjamfEdX6iQe1v4wsxv0gwL1T0OvJMylc9hhOrEQuMdJsIAl4WcYnzEShc-7SKqevvpbZA35flKcIVHAC7M7S3f1Dq4rMTTjlu1BAfrD0YPAP_TokQ6J19YyRq9BBweWass3ezN_nqXPyEWYjm5bJS9-C4Iy1nteZnzC9AdoOUIpxWwxvhxp8MEHHq5ZG8MS0sJJkZwEbNCPmnoyCllkgeXBpHQn-oPekXb6_xuz4TyTDGGJORJS_zFHCpiaE2JSonoZ-TcZq6Mnm5pDZHYj-A-q6kdkGXSGbXmdSjtcsOtuR7ylokUl_fssBdNSGJJEPX7IFoMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=EdDXz4lkcWzlsCDeSqh6bb10gNRHUbDipA2Af8NhN6lzc-0zsjcRKQBmvf-6AyBuGw5CwJptuBW6WtDimYMNBIoteaw5n2SohRYNLQjX52JXgN_YvUbAmIF0GHE1xxitcF9VYazl_YoO7N7KNUb4w82UJDJcIeh4RNohXBdXQ6UHuU_MKfWWYHuaAKz884VkRw6NxTZ-6pk20JCTRjZiJqk1QPk-zRPjNvQrKG5mjIHuoOoNu9-TUezpTCY-q4ma56yvd_sNTXiNx_lnaomybxF87RRpaKbVd-pjdGnXJlBi6Tk2_zDqRhJcTI5rfsX9watEutLUWXts4r8xifYsSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=EdDXz4lkcWzlsCDeSqh6bb10gNRHUbDipA2Af8NhN6lzc-0zsjcRKQBmvf-6AyBuGw5CwJptuBW6WtDimYMNBIoteaw5n2SohRYNLQjX52JXgN_YvUbAmIF0GHE1xxitcF9VYazl_YoO7N7KNUb4w82UJDJcIeh4RNohXBdXQ6UHuU_MKfWWYHuaAKz884VkRw6NxTZ-6pk20JCTRjZiJqk1QPk-zRPjNvQrKG5mjIHuoOoNu9-TUezpTCY-q4ma56yvd_sNTXiNx_lnaomybxF87RRpaKbVd-pjdGnXJlBi6Tk2_zDqRhJcTI5rfsX9watEutLUWXts4r8xifYsSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F8kb2YYpEQepgZaDpSNJYcfl06UJspuLQ9ctAX-8nIYxrrqaJ6hDsWi9t9e9jyL4PMvASZqvSv8pari6pPXPSHqAV6paEvCVr33WHy3xryW4vL-y-smE-6yfPA9kp9TBqzfU8KXc98gT36z1hrkLgRQH37yEVXEcC1Fs7kr9qSqO80oPtjjqyxUqOcV-uh_k0SJiTvAL7pksO_71xYcj5GChvSwKLWXoD8M_yTybEWI4JuTf9Q18WsKshqhoOMQHwwGPdRa-S9QYCqNT9K5J6VwoS9iMFnPIZuugW2ZEni1ck92dm-EgeZKTjq-cBuZXyWbP70o2YfRDaSlCE5p7ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgerBP6tyXBUaA3bEGR5TcgknSAcWFfUFOywBNRcY0YYnlURhzXKTR_5tZYrTzejl4lTzF346fYzFVToAyKgu2PYbZvQ7Rvd-rEgGOlpdDlLlL2IZ9IW_sYnJcFa1KCCO0ADEdxp0lx2PntTEIFCvCFJzs9Vh_MJ2JpXhpddCqVRimbBDTMR0x0EJgxC87P18Sm7em8GJKdgTKUdjurd1izYTwClpNb7oNVtu2GScw7VHqXY6KGuIAz7-NzIb_wjyydkOmlNQecdHgCcd8euCpWKvlj3-9t4WZfLgCBYp02KjzrD43oaLvA-XWt55JAcdS6QBqsJR8VO8obB8-IP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTs7x7QWhbquO_pG-2T6LcLdTHbimbB9Hc5ZQlA4IBNXMhm20Pb2i9sN3PqLA02eGLkJQJ8IiEgsWzsscaa56Gw5FrAPb51LbcUs8XAe_M3E10-2Z-82oya5rI__3GAviS-rcuc7V0wAYl7SFCz3ZZEOfdYjcW4o2zjOM-Dj5wTNLrQm-FHV49oOHzk_hWxe_-GpuxYIFhNscrlYvlG0Ch054Xshe7xfP2UqIY3G_ajPMFZnkoIllY1vivhNQqRo3UPx0GjTqIOCd21JrjJFeF85Xt83yyGb9iAfbxDlQA_5jkUwWyNKg4mhol23DpJp8ZbV_YswoBjRyz-P7oLa-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lkSqMkc-9aHqvBRFpjf8PHDb_EzSwaDDloBDUeZCWFP_6Z2YZLFHdEWzo10VhISvOh_mgJ3pHZee8qTw_2y7hhQGIDFXajA-Qtb1Ifpb37CGT3sr2qCPGINvdoU_AP3cq1RmRq_ihjN36KdkAuAS0Xz0KWNVrCXCv-rGB05etcDt0aAuhILNGLE2b7q3NHHHYh7Gg8fs1EELmJ9H_LaSl7Z1ez155uByf8ciLCGYwFLKi8isBkWK0g4ZEE7XeBar9Qf3JeZ1_lcX4KdN2ca_m08bJ8VdebZosY8JF57DI-q7rkww7eA2rF8NRsgAk3T4XwOq7twpqxqu7ZOdHcR9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F5C-qZbcyvowaVjZrB-g-GFP1zu3mJmGnXpEOtWRSC948jCrL7pCf9t8EtwqfYcU31z3EeQRKJmZFLBM5oMn8zH6kBSPxSw91fVE-Y-6gmKcyqJn8oQuv0LXDqKXP0KyEmV4erITnE92QCdUa04df6Si6JB8GArG0jEg41k0O9LwRxr1mWIXoPRKQWwFAVTWk7iTVqhcFUkXyp3WizcHery8GWpUsRDe9y6WylfijfTU3HhO_Mt8ep818-RSME1g-fNIa97sRPosbgcvSs_4MXDByFuYxu64e10qphnz_o8Qw5MXrMJ_FI3_BT6tOW6MO_BcN2mLeJhbURgXlwaZDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69131">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmdd01URe5W64w3JlZ9sdkBh4ThBQzd0syGSHK64wWElmuN-XE278OE-UTLJvBMBAfM5sP2WQDBWePwEeVyY1zWWQlQJdwVckPxPd_xFVg5J8Z0JMAf1kXCWUCQphvMlYa5VoYIFYFe-5-tPBHPFUdtXtBdGpq4lEaWPa6oWh1Y3xCer-2vTlBhh_WLw83zHMUa25Me-V-gatjyDSwE-NlBidMH9d7o8BwBcB1l7oAAvEly9dtrcjJcGYzmuYVR00Br1hJ4Dcmas5gs9GY04iILPsKHzl3Za3lj0-uKBkgrL4PJ3aTjL4XDmnhyYC7NIw3bY0osKvvY82BQhw6B_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GoHzPY_L4pORV7okMIedTHU0EG2KK-pK-mZjoXfoTdBkyyK4GKAAx_aUcsSDL0iOCfFL6AWSrwAslDrijHqrqHtPbYpwDpLTEsdP4jct6LfN9zXE2oO-B0Lv8xl83ZcN_KBKvdbVaiiMK-jgu5EjPjylph_jBdERZgoB_jueO3shvFHW_isCpBnuyyYis8kUQ4yYnm7WkIf21-kyr8EfNRNxZo6WejPQvhRNg1Tlrk2l3JEOYl600Zn9iJ8Iwy-95xAAHZxefozBwlqiwlb5LGjydWiP9F4rOZiu653-kXGlrAij1yGn2SzQL-HTvGPjd_72VJfcIMuMmoc2oCKi2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69131" target="_blank">📅 19:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=r6lYuiTg1CFv-1DqhXpyKjZMZZSQqgzFSZC6az6EcVgZ1y5QWet6j_HeX6in5c6tQ9bJOy8RtIh7KCR0QD4w49WzYdM3Tfr_vYp34platzSwPkK1kelXnP_NxRscVhI5bwzd-E4nrZO3v5fHlycSt07VoVLSfVBky7faJPifVFLf6UlGlJHVFgy0ULfqR452VXT_LyyMlipfVmYSm0rtWTZhdFHkXNZp_yQfQV4atDiIYtmFhISMDotT6srq1nZMIblqRV6r2A8bdhHCy6D0Rn70jMV8tMAevvDHXma0MJ1bpvHXs1ypYw5G6TK36qS4rfCZIP2fxUGsZ-vcZyMx-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=r6lYuiTg1CFv-1DqhXpyKjZMZZSQqgzFSZC6az6EcVgZ1y5QWet6j_HeX6in5c6tQ9bJOy8RtIh7KCR0QD4w49WzYdM3Tfr_vYp34platzSwPkK1kelXnP_NxRscVhI5bwzd-E4nrZO3v5fHlycSt07VoVLSfVBky7faJPifVFLf6UlGlJHVFgy0ULfqR452VXT_LyyMlipfVmYSm0rtWTZhdFHkXNZp_yQfQV4atDiIYtmFhISMDotT6srq1nZMIblqRV6r2A8bdhHCy6D0Rn70jMV8tMAevvDHXma0MJ1bpvHXs1ypYw5G6TK36qS4rfCZIP2fxUGsZ-vcZyMx-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت بحران تهران: این بلندگوها و سیستم های صوتی که نصب شده آژیر خطر نیست
اینارو نصب کردن برای پخش صدای اذان و ما برنامه ای برای اژیر خطر نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69130" target="_blank">📅 18:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpswulgQkA5fIO0a9hUHGtjHwHhJQDqdHObbjC7DE2goy6bSbfechTbhq0ZDET540zI0cR4RMwedO3Qdzwfosa2ih-9pPUfuplbv0G49UM5IdTaK_ajwO6eD4KARcC35MPsl9qUwPcXaM2jBIb97r7kVsk40hTtm13glCqZegcd2H4bbdpr21r0ZQJpS43iTDPpnMzvrL2Orv5aQlrPOD_BM0OIq6z3wlFYA-rw2fUm5Lm73RDMiOda37Xgo87CE58z0i64j64JKsluzcGXrhqIqqghTmtvJwXFc84xQ8NSoDPobmz7muLT8NDF2dM4I7s-lJwwvVkWIYHoQ97YB6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69126">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=Qt8K4SN2kVg77AfFwqKVIqLgGTqtdO8jgd9ru5DIjUUJo3KsTMKj9Fd-sU8z5KkaJvomrO8iZzMDVjA9nYMt2SBXW41EqzLs02BVPFOhhiF5EAKiUr-XuqCcRnSazdBLVEcdVnFhqckjyK2NtuAufUkRnalxn44sODplLqXUmGGqLjf-SEGpQjUbivGwm4eSTmOZ3nf0vN6Yhd3_wGS8da93tKNj3etk7IWbixzSA7OWMVRF5CVkHnTs5Tr8HEV4y67lt9zaaKR_p_3l7wXO90QwutvPuaR6PX9YQwuwsVdJ17kMBkerL6VL1XDzrAQNBZI3EZ-6rHRnkl_i0rF0cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=Qt8K4SN2kVg77AfFwqKVIqLgGTqtdO8jgd9ru5DIjUUJo3KsTMKj9Fd-sU8z5KkaJvomrO8iZzMDVjA9nYMt2SBXW41EqzLs02BVPFOhhiF5EAKiUr-XuqCcRnSazdBLVEcdVnFhqckjyK2NtuAufUkRnalxn44sODplLqXUmGGqLjf-SEGpQjUbivGwm4eSTmOZ3nf0vN6Yhd3_wGS8da93tKNj3etk7IWbixzSA7OWMVRF5CVkHnTs5Tr8HEV4y67lt9zaaKR_p_3l7wXO90QwutvPuaR6PX9YQwuwsVdJ17kMBkerL6VL1XDzrAQNBZI3EZ-6rHRnkl_i0rF0cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇺🇸
رئیس‌جمهور اوکراین، زلنسکی، امروز صبح به کاخ سفید رفت تا با رئیس‌جمهور ترامپ دیدار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69126" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69125">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=dcWJboCzWVXkbg53lDOgBrtYnU4rnFJGQ-DBQwPEoI74svyPBUIQz3IvMCFpD_T6tWb4RXlltOSK6tHdPw9a6My_izLx3aurWshAgWglVqjSS_FF8ZqKnzk9XJhXTCYP4DZsxHryqT9ChYHn2GLlXYc-XQROiAL590wNjzN7cJ40_tt110Z801KIemyvQ_k9_-xtsnvYju1RHIOk98_ZVAk47buCvrpZyHS7A2OLTdSus3aY7suDjEmUdELVWVEqV6Y1gQLqNwG-ca7S5-arrtE-k5v-0M6sPjrxfUaMd59_L_ToQVGK7gaqdt7MhBV06k6zAiuXKACzc9tlM7DHAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=dcWJboCzWVXkbg53lDOgBrtYnU4rnFJGQ-DBQwPEoI74svyPBUIQz3IvMCFpD_T6tWb4RXlltOSK6tHdPw9a6My_izLx3aurWshAgWglVqjSS_FF8ZqKnzk9XJhXTCYP4DZsxHryqT9ChYHn2GLlXYc-XQROiAL590wNjzN7cJ40_tt110Z801KIemyvQ_k9_-xtsnvYju1RHIOk98_ZVAk47buCvrpZyHS7A2OLTdSus3aY7suDjEmUdELVWVEqV6Y1gQLqNwG-ca7S5-arrtE-k5v-0M6sPjrxfUaMd59_L_ToQVGK7gaqdt7MhBV06k6zAiuXKACzc9tlM7DHAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سخنگوی قرارگاه خاتم :
هر شرکت یا کشوری که از دارایی‌های بلوکه‌شده ایران پولی دریافت کنه، دیگه اجازه عبور از تنگه هرمز رو نخواهد داشت.
همچنین به ترامپ هشدار میدیم که هر کشوری که از پیشنهاد آمریکا برای استفاده از دارایی‌های ایران استقبال کنه، شناورهاش از این به بعد اجازه تردد از تنگه هرمز رو نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69125" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69124">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=HwjGtYDkYDMf2G55kVRYUwsN9Pv5eLlZscDJKjMH17qB1cmUR8FosokHSGqg2S9Os7RWIWphv_VoREklCd4s10FpDW5LnuWWPcqpbwrY56D0qtDfZIDg9HaxjYqxck489X6R7HNGD-ulc89MUWnVu_0b-dJCnTYoi8P2FxVmBrYLaNxhVVmyW4SyLu8cYudjq40slj2ztKwxO79p9BC9haeY_96fs0q2bVvme4yPhQXKoAlk6XSUjc_piLsPFac0vJ3nVg42g8dZJXSIbJXJfyiaqVEOfV13J_YG1unJGIwxFauijU6V6703-4r5nKLgClo2RNzfYvmoiYoxXpn_Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=HwjGtYDkYDMf2G55kVRYUwsN9Pv5eLlZscDJKjMH17qB1cmUR8FosokHSGqg2S9Os7RWIWphv_VoREklCd4s10FpDW5LnuWWPcqpbwrY56D0qtDfZIDg9HaxjYqxck489X6R7HNGD-ulc89MUWnVu_0b-dJCnTYoi8P2FxVmBrYLaNxhVVmyW4SyLu8cYudjq40slj2ztKwxO79p9BC9haeY_96fs0q2bVvme4yPhQXKoAlk6XSUjc_piLsPFac0vJ3nVg42g8dZJXSIbJXJfyiaqVEOfV13J_YG1unJGIwxFauijU6V6703-4r5nKLgClo2RNzfYvmoiYoxXpn_Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما محاصره رو برداشتیم، اما چون اونا توافق رو زیر پا گذاشتن، دوباره محاصره رو برقرار کردیم.
اونا مدام توافق رو نقض می‌کنن. دیگه نمی‌تونیم اجازه بدیم به شکستن توافق‌ها ادامه بدن.»
«ایران تنگه رو کنترل نمی‌کنه؛ ما کنترلش می‌کنیم.
اونا شاید بتونن چند تا مین دریایی بندازن و اوضاع رو به‌هم بریزن، اما کنترل تنگه دست ماست.
حتی یه کشتی هم بدون اینکه ایران جلوش رو بگیره از اونجا رد نشده.»
«وقتی قاسم سلیمانی رو از بین بردم، ضربه بزرگی بهشون وارد شد. به نظرم اگه اون هنوز زنده بود، ایران جور دیگه‌ای عمل می‌کرد. حتی ممکن بود به سلاح هسته‌ای هم رسیده باشن.»
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69124" target="_blank">📅 17:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69123">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=nPuXbLhqL3lcrLsFTjfQtUBtsxD64rC46JXDifKO_daP_rmvfzJXR3u8q0cVqdUyssi-jwFj5qn_IWGjWZkRpr9XOV4bXLkXKuUpEdbvu3awlhMU8tivKT1Nqr7jcMfVQks75n-ZrcrI9XomCRUgn0WsohP9HM5Nibp8Q8pnZDWlP_y2dT-vwBdTosKE8eAl7L74JMP-tnLSbrQWzalxbZFEdffc79HsxPZWwye6bMvETxvyWb1Pd8kV2Mws9ReV3uU2CEq4FJCZGpVOcUwLX734EGlxt2ggyNavxpkhhJFSa2BJzRmvnYqy98Me4j25RPyVBvDZ91byHeA-gBgdYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=nPuXbLhqL3lcrLsFTjfQtUBtsxD64rC46JXDifKO_daP_rmvfzJXR3u8q0cVqdUyssi-jwFj5qn_IWGjWZkRpr9XOV4bXLkXKuUpEdbvu3awlhMU8tivKT1Nqr7jcMfVQks75n-ZrcrI9XomCRUgn0WsohP9HM5Nibp8Q8pnZDWlP_y2dT-vwBdTosKE8eAl7L74JMP-tnLSbrQWzalxbZFEdffc79HsxPZWwye6bMvETxvyWb1Pd8kV2Mws9ReV3uU2CEq4FJCZGpVOcUwLX734EGlxt2ggyNavxpkhhJFSa2BJzRmvnYqy98Me4j25RPyVBvDZ91byHeA-gBgdYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه من رئیس‌جمهور آمریکا نبودم، امروز دیگه اسرائیل وجود نداشت.»
«اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، با ایران دوست بشه؛ اما بعدش رفتن دنبال توسعه برنامه موشکی و هسته‌ای. طی 50 سال گذشته، همه رؤسای جمهور آمریکا یا کشورهای دیگه باید یه کاری می‌کردن، ولی آخرش همیشه این آمریکاست که باید وارد عمل بشه.»
«اونا عملاً قبول کردن که سلاح هسته‌ای نداشته باشن. فقط مونده این توافق رو به‌صورت رسمی نهایی کنیم، اما با اصلش موافقت کردن. چرا نباید موافقت کنن؟»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69123" target="_blank">📅 17:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69122">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه دوباره برگردم و بخوام کار رو تموم کنم، همون‌طور که بعضیا دوست دارن، خیلی راحت می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهم ایران رو نابود کنم.
ساختن یه پل حدود 10 سال طول می‌کشه. پل‌ها سخت‌ترین زیرساخت برای بازسازین و بعد از اون هم نیروگاه‌ها قرار دارن.
من می‌تونم ظرف یک روز همه نیروگاه‌های برق ایران رو از بین ببرم. اون وقت حدود 91 میلیون نفر بدون برق و بدون پل می‌مونن. برای همین این یه تصمیم خیلی حساسه.
اونا می‌دونن اگه به توافق نرسن، من این کار رو انجام میدم .
پل‌های اصلی واقعاً از بین میرن؛ فکر می‌کنم تو کمتر از دو ساعت بیشتر پل‌های مهم نابود میشن و نیروگاه‌ها هم ظرف یک روز.
ولی اگه بشه از انجام این کار جلوگیری کرد، ترجیح میدم این اتفاق نیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69122" target="_blank">📅 17:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69121">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=UnNC7Gr4DC4kA--kf-Q4dkXfGO5bo0IB9YOhyqtDyFf6iZrBnSlMbiCtj2bnLnfbHX3eIxvoKyNTwUV03pN7_4VrkZTibrg6oOSbgClYj_AzFngZTDDC633QnzSnpjqPOW8E4D9QesEnYYoUKlAGVMf2ADh_P051Gsxfyq8oadcaxR39EVQQkQYss8upz8hEgPaJlW5fXmkiV7fJKQS-BrYeMpR0LfyF6uicCf7JQhYRkeEWIRSXH_INQyFInAwsYlWbnvEBr_OM9eYzm0VrHm8Gv8Ub0fOamiLO0GdIGnhCSsTArHW8bdtwA7I8IP0w4RzLdi3acFRwblEGS3Ab_CL3OSmU8nh1VMcmijhY-WSu0JFdO2Ty1hRdmrut_8h0u6FdpnwTcqJnDao_JXCgdW-kRyxX2bXfmjIp9E0vUpGWnc_Ttt-k8zPE2jLnJRvfobUtboUCKrPLDes76NQIh4OQ1N3NXBOfHVJneajLoQhWtvosl7AkZlJPHm5oRjAkOw_B22HgGjscA4PVgWF4l0TRN3Jip7ViW4l8CgsyhWTBAcea2hsh1Wl7e_PwxW6thKfiTeFfjhfpe3bggnq0s-_NV-0RSniby9g6XgX68sF7Nl3dpNBy7PX27CMMqsiPI9IHFJHnSZIUSNNKD3ZJFWAv4PcqCAEJYTjmtgTTELw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=UnNC7Gr4DC4kA--kf-Q4dkXfGO5bo0IB9YOhyqtDyFf6iZrBnSlMbiCtj2bnLnfbHX3eIxvoKyNTwUV03pN7_4VrkZTibrg6oOSbgClYj_AzFngZTDDC633QnzSnpjqPOW8E4D9QesEnYYoUKlAGVMf2ADh_P051Gsxfyq8oadcaxR39EVQQkQYss8upz8hEgPaJlW5fXmkiV7fJKQS-BrYeMpR0LfyF6uicCf7JQhYRkeEWIRSXH_INQyFInAwsYlWbnvEBr_OM9eYzm0VrHm8Gv8Ub0fOamiLO0GdIGnhCSsTArHW8bdtwA7I8IP0w4RzLdi3acFRwblEGS3Ab_CL3OSmU8nh1VMcmijhY-WSu0JFdO2Ty1hRdmrut_8h0u6FdpnwTcqJnDao_JXCgdW-kRyxX2bXfmjIp9E0vUpGWnc_Ttt-k8zPE2jLnJRvfobUtboUCKrPLDes76NQIh4OQ1N3NXBOfHVJneajLoQhWtvosl7AkZlJPHm5oRjAkOw_B22HgGjscA4PVgWF4l0TRN3Jip7ViW4l8CgsyhWTBAcea2hsh1Wl7e_PwxW6thKfiTeFfjhfpe3bggnq0s-_NV-0RSniby9g6XgX68sF7Nl3dpNBy7PX27CMMqsiPI9IHFJHnSZIUSNNKD3ZJFWAv4PcqCAEJYTjmtgTTELw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران دیگه نیروی دریایی درست‌وحسابی نداره، نیروی هواییش هم نداره و ارتشش هم ضربه سنگینی خورده.
اگه توافق نکنن، دوباره اقدام نظامی رو از سر می‌گیرم و کار رو تموم می‌کنم.
می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهمشون رو نابود کنم و ظرف یک روز هم همه نیروگاه‌های برقشون رو از بین ببرم. این رو هم توی مذاکرات بهشون گفتم.»
بازسازی پل‌ها سال‌ها طول می‌کشه؛ خودم سال‌ها تو کار ساخت‌وساز بودم و خوب می‌دونم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69121" target="_blank">📅 17:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69120">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI6RsiSE9nwpP5Aci1yryixeuuYkxAA82OoXHF6XNbe7SPo0y1uv2SzHQrvNTY5M8FKZJdNsJAP1MENP_fDCs6yTtu2OgDX550lVvA4Ma5Zv0whdjLd0sbqTMFV0o-3y-TthwJSD6O4iolgOTm13vcmyym78PYxu3TmHB8gN2GHJRBrD-B6Q8eZVM9vD17J1simpF8Ct4M10Pu9VDL9DKRE9C2_NPSEI1ph107EOG0vzANRHhJVZKbyFVaApeU_LY37gSWjovi1tedHA_ke4kd2UbC9Xrdoo1XuiD_PEwWzLwwCQmhO-FVCBNavXAPxQFIIg13vRjfySOlNn_6hA3chU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI6RsiSE9nwpP5Aci1yryixeuuYkxAA82OoXHF6XNbe7SPo0y1uv2SzHQrvNTY5M8FKZJdNsJAP1MENP_fDCs6yTtu2OgDX550lVvA4Ma5Zv0whdjLd0sbqTMFV0o-3y-TthwJSD6O4iolgOTm13vcmyym78PYxu3TmHB8gN2GHJRBrD-B6Q8eZVM9vD17J1simpF8Ct4M10Pu9VDL9DKRE9C2_NPSEI1ph107EOG0vzANRHhJVZKbyFVaApeU_LY37gSWjovi1tedHA_ke4kd2UbC9Xrdoo1XuiD_PEwWzLwwCQmhO-FVCBNavXAPxQFIIg13vRjfySOlNn_6hA3chU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما دقیقاً می‌دونیم تو تأسیسات هسته‌ای پیک‌اکس چه خبره؛ از حفاری‌ها، تونل‌ها و جاده‌های جدیدش هم خبر داریم.
این اصلاً مشکل بزرگی نیست. بی‌بی مدام این موضوع رو به من میگه، چون می‌خواد همچنان تو این قضیه نقش داشته باشه. اگه به توافق نرسیم، پیک‌اکس رو از بین می‌بریم؛ اونم خیلی راحت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69120" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69119">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=e371lLCd4_uaRcBWwnils4EYLYgEM7sOa9xwuKgQ-cH4_OAijq9xHjYiGhAUb90kqnsUGQl94wedW1Nw_jjFm75-WATPQ3wLJ2JugiNz4tLOqWfKb4ZqkxK8qpCSAW8Nbr9z5Gz6FU0xBRjx7UFURwqooMPppvyc0y0NXq-YLb8fojfTKTYmP4hxRB5-bemO4RU9rsCZRhDn5K5QLC8S0Ks8v4dq9D1FdFFWbAFOQSXuRmmhvd4crlQbY9OfABuL2ecaa7KVvnCkMcPiQQoNtT2yC7cslRPLFFpWtuoXBbcmJqjKPlPlaYGXEdW35-7XFPnds4Rwb6HXww4Y93ueaKN5LFi4xSR3ZMQ8cBOAvlWBNQFbtF19QskMRA03Pv5y54Q0bQb9gpNQvTV5qVNx5Zyn3nUb5O-OF8uIOjoe7X6oj0T7eav-eVcn3t5cSu8pjczz-J8agvcuxYSwgeWR-AuMA09PZ984q5jqmZX1Klkl-IH1gb-M5mvgUahdvDQuPCDLkJR6Ksto73e3zVgqpDpUTOD29wIVbB9VcPtVbzOY_4Ryr1WoNetNcDWvJln5hWrW17ymOCeDqCODdGhXPrRn7enWsKhpP1fWnWGDhpZi0jmMLWKDgZq0oZ7WFah6vYhZYHUXRSMDJ8svyPNosv2fct3jNK80L7IxD6wkZqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=e371lLCd4_uaRcBWwnils4EYLYgEM7sOa9xwuKgQ-cH4_OAijq9xHjYiGhAUb90kqnsUGQl94wedW1Nw_jjFm75-WATPQ3wLJ2JugiNz4tLOqWfKb4ZqkxK8qpCSAW8Nbr9z5Gz6FU0xBRjx7UFURwqooMPppvyc0y0NXq-YLb8fojfTKTYmP4hxRB5-bemO4RU9rsCZRhDn5K5QLC8S0Ks8v4dq9D1FdFFWbAFOQSXuRmmhvd4crlQbY9OfABuL2ecaa7KVvnCkMcPiQQoNtT2yC7cslRPLFFpWtuoXBbcmJqjKPlPlaYGXEdW35-7XFPnds4Rwb6HXww4Y93ueaKN5LFi4xSR3ZMQ8cBOAvlWBNQFbtF19QskMRA03Pv5y54Q0bQb9gpNQvTV5qVNx5Zyn3nUb5O-OF8uIOjoe7X6oj0T7eav-eVcn3t5cSu8pjczz-J8agvcuxYSwgeWR-AuMA09PZ984q5jqmZX1Klkl-IH1gb-M5mvgUahdvDQuPCDLkJR6Ksto73e3zVgqpDpUTOD29wIVbB9VcPtVbzOY_4Ryr1WoNetNcDWvJln5hWrW17ymOCeDqCODdGhXPrRn7enWsKhpP1fWnWGDhpZi0jmMLWKDgZq0oZ7WFah6vYhZYHUXRSMDJ8svyPNosv2fct3jNK80L7IxD6wkZqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
هزار سال ایستادگی،
نامی در میراث جهان
قلعه الموت، افتخاری دیگر برای ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69119" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLh3RhyNBEUK9eeatTbiBWqeDZWMCw3J6XKJrW0ZKotB-SKKVh0SYPKZJvCeB-2YA6tlJPY0Lu--0MaVijJL5dtHZw5fWnuGz4VuS5HpzxO4bfocwguRH1m6TQ29Ef8SQvC4uCK4NofoqQqfEopG1reKA8Ldu6gdFmVG22fBXLLUvXCQQaRGLBaHtpAOJiPXmyU00h_Cvxfyu5R6gqU7rRwsrn1tDi2ZoZcNSu5o7Z8NTDxPS6ZyiEMBFBeBxD3X7FlzAtclEbtHffe4m0BklFmzTRbbvF47IQYq9oY514jpBaEIWLfwl0Y2-o3BBkv1reY24cxfCPwxJKedqBM7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cayHNT7xZH-KX49QOiKtClFYppXXQU7ojXz1udK2mJhDc4x5qXzZ1zhz24E13BSZejxFRXRqIN-ccsdn_XGn8UIS5S260O40QMIegXs17zKf2dtnMus7xoQM-I4uOap-oIJhq5RQaSBOqoQPi74tvZfv4PMxRpD7QSd7byOeT05zAqZTh1yVMP-7bvtUMIErZYdlveXMIcVXFv0s5M-mwoWC6dnEF-khLq2kJ2hoBf4JYMS-PWkILEYIdmPoTMYKHzHPlAi0s9Gqhkl4x4q2Qnm0hM2lwoN-r5Qad0OsiihMkk2_ohXQbvzhfiiMNuK23Qr0vDUTHO3g4i3oMQGICA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=CQmiFmDFCvzlX1cWIgAvYX4-Qzbs4OEQD5NDlVLNx4idVB6drwfR65486rash3WjGHpw1Ymb95Vaf8tQH9GigrJFPCLIYn8bXfksK6zY4ffN-YTq9FmsRo4a4rGp70HypK1MXSP5rYKSrMQiaJLkfUndD0zh45XYEJvd-IQddRhFLCZ72EHVYoowHGJLJR1PMbyes1WN19X54H2v6nKeW4Flq-c752RNdwqlNFd3K4PlCmYjUEkKm6rl9OkGzerOBl86MM7E_oSXnQTShtDOS55f4jP2MLbQLXkSAJJ91K252Lb83q3qh0Om3z-BYBAe4SRiZZiJpHvBpe5pQ__Xjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=CQmiFmDFCvzlX1cWIgAvYX4-Qzbs4OEQD5NDlVLNx4idVB6drwfR65486rash3WjGHpw1Ymb95Vaf8tQH9GigrJFPCLIYn8bXfksK6zY4ffN-YTq9FmsRo4a4rGp70HypK1MXSP5rYKSrMQiaJLkfUndD0zh45XYEJvd-IQddRhFLCZ72EHVYoowHGJLJR1PMbyes1WN19X54H2v6nKeW4Flq-c752RNdwqlNFd3K4PlCmYjUEkKm6rl9OkGzerOBl86MM7E_oSXnQTShtDOS55f4jP2MLbQLXkSAJJ91K252Lb83q3qh0Om3z-BYBAe4SRiZZiJpHvBpe5pQ__Xjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=r63BdZLxN9rEK6i3eNIVauz7s9UDa1UoCItWdq0QQYIGYBWmjVuifMaN7eTf5Dd3j-nYUhmvbGVBbB9fmE7HsPEB6vbt4PSw9YptQvHM8fHxIwcZOCCykxPP55bHnlbAW5MC3ER9KsojsT9U1981o0sau_VdH4J04S_L2em3OGv105TupboDWl3FeQlF5-R8nJyLaKqt4piEfRQnvev8MY_wzEz7dCAvuvcxysE2ZbKI6Mdxy_4Qi58N-ADQqV8Tf3OuWzD8WoPum2K7HR_1-HbMwTQByOZ9kt5akysjlN693gasTYGNQWH4MJzv9TNd5Zr6hXZOYQINtDjFZ9nPog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=r63BdZLxN9rEK6i3eNIVauz7s9UDa1UoCItWdq0QQYIGYBWmjVuifMaN7eTf5Dd3j-nYUhmvbGVBbB9fmE7HsPEB6vbt4PSw9YptQvHM8fHxIwcZOCCykxPP55bHnlbAW5MC3ER9KsojsT9U1981o0sau_VdH4J04S_L2em3OGv105TupboDWl3FeQlF5-R8nJyLaKqt4piEfRQnvev8MY_wzEz7dCAvuvcxysE2ZbKI6Mdxy_4Qi58N-ADQqV8Tf3OuWzD8WoPum2K7HR_1-HbMwTQByOZ9kt5akysjlN693gasTYGNQWH4MJzv9TNd5Zr6hXZOYQINtDjFZ9nPog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c00215915.mp4?token=AB8_ioZB82SVcH0vtrZ_1Tx1J2-VUP12VXdi7UWUIRwBSnq65aWZweGGVOBTGLNCn0QSG67857nweqRgp055ykzwkW8Nr_vgLWVVGK3uGI16m9U6tkJOaxwoBOkD1NvzHQMEZwfpJxxrqyOyf2vGZlLtA5BybRw0C5Rf7E6In3tYS4LoL9jxt59NbWFDjCA0KgeCK1caFqYGQIVHIm6-crnjL-v4-EuiOS5ePS3cCEyNjlvdn507g15KQHuJKJzr16j6r_lxl8DdBHm4W5KTn35lyYGks1W_dMHH6xEnKwCzdFBvmycr7DCmQc105KUVkU-qX1ypxiP5qoYIADG9tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c00215915.mp4?token=AB8_ioZB82SVcH0vtrZ_1Tx1J2-VUP12VXdi7UWUIRwBSnq65aWZweGGVOBTGLNCn0QSG67857nweqRgp055ykzwkW8Nr_vgLWVVGK3uGI16m9U6tkJOaxwoBOkD1NvzHQMEZwfpJxxrqyOyf2vGZlLtA5BybRw0C5Rf7E6In3tYS4LoL9jxt59NbWFDjCA0KgeCK1caFqYGQIVHIm6-crnjL-v4-EuiOS5ePS3cCEyNjlvdn507g15KQHuJKJzr16j6r_lxl8DdBHm4W5KTn35lyYGks1W_dMHH6xEnKwCzdFBvmycr7DCmQc105KUVkU-qX1ypxiP5qoYIADG9tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مهاجرانی، سخنگوی دولت:
تو بنزین سهمیه‌ای فعلا تغییر قیمت نداریم، ولی هر وقت تصمیمی بگیریم، شفاف به مردم اعلام میکنیم و اونا هم همراهی میکنن.
فقط مقدار سهمیه دوم بنزنین (3,000 تومنی) از 70 لیتر به 50 لیتر تبدیل شده که اونم بخاطر حمله دشمن به مخزن انبار نفت‌مونه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69114" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=mH-8IOJghhfPo4tKjU5cT56J44oMj7xbfryVUGXPPraybGeWHTr8FjL6qhkR9KJUFKL6I0DwFcTH1gA0XeVdGwArkL36Uhl13JTDVT_Y5WqONm-FmYh2Ll7s_zoJbBSWj0xakp_wt4ysjSLJFfJxDzUWTUB1MVPOAUZ0XW69kZB-0Ndu9XAKdtwZjIHCEboRU38-ZP6R4YpOaLZETri8xkU_Hg3_tTMz-fB3UMqb8WQfeP9xXmVSyw4km7TBXXeJGKDMWQVQDkNzgzHphJx6IPir32iXjnduIIBUYkkobS5Id4KfNEM7WCq-M5FR9TFMi8vKfsSLLwTiuRUZBwh6Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=mH-8IOJghhfPo4tKjU5cT56J44oMj7xbfryVUGXPPraybGeWHTr8FjL6qhkR9KJUFKL6I0DwFcTH1gA0XeVdGwArkL36Uhl13JTDVT_Y5WqONm-FmYh2Ll7s_zoJbBSWj0xakp_wt4ysjSLJFfJxDzUWTUB1MVPOAUZ0XW69kZB-0Ndu9XAKdtwZjIHCEboRU38-ZP6R4YpOaLZETri8xkU_Hg3_tTMz-fB3UMqb8WQfeP9xXmVSyw4km7TBXXeJGKDMWQVQDkNzgzHphJx6IPir32iXjnduIIBUYkkobS5Id4KfNEM7WCq-M5FR9TFMi8vKfsSLLwTiuRUZBwh6Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
نتانیاهو به دستاوردی رسید که چرچیل نتوانست به آن دست یابد.
او ترامپ را با ما همراه کرد تا به ایران حمله کنیم؛
بدین ترتیب، پیش از وقوع یک «پرل هاربر» دیگر، ایالات متحده را به اقدام نظامی واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=FviRb7FcGLNqc8dJD1PPCIw3etFcNwp9R1l-KywamRDE4eXz_EtrZkjfmqeTlqYRrlbdtZhMQE5V8dSYwZJB9itCPjxvoAYdBx4-3FzEahUHd0t_Iw6iWW2_8xlOAZ0NNSe3b5QxFqnGFJJJxQEQr5_iKlepPk-zQlE4QZAcfcBeeOl_Usbbtc1ikpIs618BqDRZ5X8kp-KjIFJ1mFLfo68aWyUQDfMaGZvS8oyHnVCgclX-gCZAzLfv46m-uCXmzmdXUEEN--80yEVehq6z_8VyztBH_JZUZ25mxG0YZ_UAxiQpph-IIAdy1hDhRHMRAJ2wHdBk3W03BdvcbB6PfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=FviRb7FcGLNqc8dJD1PPCIw3etFcNwp9R1l-KywamRDE4eXz_EtrZkjfmqeTlqYRrlbdtZhMQE5V8dSYwZJB9itCPjxvoAYdBx4-3FzEahUHd0t_Iw6iWW2_8xlOAZ0NNSe3b5QxFqnGFJJJxQEQr5_iKlepPk-zQlE4QZAcfcBeeOl_Usbbtc1ikpIs618BqDRZ5X8kp-KjIFJ1mFLfo68aWyUQDfMaGZvS8oyHnVCgclX-gCZAzLfv46m-uCXmzmdXUEEN--80yEVehq6z_8VyztBH_JZUZ25mxG0YZ_UAxiQpph-IIAdy1hDhRHMRAJ2wHdBk3W03BdvcbB6PfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
ما بسیار مشتاقیم که به تأسیسات انرژی ایران حمله کنیم.
ایالات متحده در حال حاضر با این کار موافقت نمی‌کند، زیرا نگران است که ایران به کشورهای همسایه حمله کرده و موجب بروز بحران جهانی نفت شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=rZ3nEgdepAqsiHUtVnRuR4J4qfbOh3fqt6BU9DJHqpKg8aYTfGsX0UJySHps8ziC0JyUO86WWUvFOJXG4-vGwc7XV-4qAfZlBgnKwKAMPouqzNINhi-RSrWtIM_v-3RY1avttFw_naxYqKw5uRaH_9XfCu9nqkTIKGVG86vVO4l2rcDsbQ4Pw7RdvcievQNWjbIS55XHnKIgtRE_VUY4G-SaF64fAQso8P_k1TMmoN53Rt1Zv9eHP5HwT1zCo7ah87IA4aFMVCGYXGZwcZNrEOJ_g-rxiF-M5GewOO4Z6duQppsTp_jHX8yMdblpEM30P_ghIHwK5DKvQDiz5ki2Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=rZ3nEgdepAqsiHUtVnRuR4J4qfbOh3fqt6BU9DJHqpKg8aYTfGsX0UJySHps8ziC0JyUO86WWUvFOJXG4-vGwc7XV-4qAfZlBgnKwKAMPouqzNINhi-RSrWtIM_v-3RY1avttFw_naxYqKw5uRaH_9XfCu9nqkTIKGVG86vVO4l2rcDsbQ4Pw7RdvcievQNWjbIS55XHnKIgtRE_VUY4G-SaF64fAQso8P_k1TMmoN53Rt1Zv9eHP5HwT1zCo7ah87IA4aFMVCGYXGZwcZNrEOJ_g-rxiF-M5GewOO4Z6duQppsTp_jHX8yMdblpEM30P_ghIHwK5DKvQDiz5ki2Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJlTjU_jrsIvcD0DAuQZvGW1NCP8C4-pgT3krbMFLFD5kcP6CC0rSZj30rJTEUeeGLW3EA_id9X2bQAGA8DIZXwkRRKgGFP7Sstdbsx9hboJEmASDL4Tip8tdvF_2nWds1Fq86t02Ow_CrsrNjYz9iYcK44A6RCDB-QTwIyD-LoUdvma-vqFld8fKamiHeb8Wc-O1m2CUvfpWpdHW6nszu2tHmtn0KPSPxcYYqOlK0IE4tmHyTmQw2gyGUjDDPHYRNRh2Jmd6mIFrBzBWPvn-jUIxdRr_rfeR5JQeIUw67eSfA4K-bij9vDr2nLDdtgN4_bNvntpA03qRiPA9g-HSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8ExvDZZWkR1g1DpRc2U-tv0gCZyqSuyi6MVSwfTH5Hi46SsRNnvJxXIT8qT7DkLMFGFPsElaZtx-cNhbk-0UVGLVf_EdbjSV6e-s16qp3J1fu-TBMGaLwdwpmqA3dGoCRrwglfUuG2pI879mfSeetc1D9g_SWSLesEYK9RgiVq5zlambgIpgkzX-u4VY2wCsDBLB98hKqj0hHGCp1SBuZlTV4MHUHWlBUJg9EuGeR6bONMgweRV7jCphv58PFefRMWOHy2FFH4V3wE3dVUp581LbSUBUQx8WaZq2XkhODV1OcahD6o8eSM194VSMNnDsrEBxR1hNSpF4uo6bs49Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛
زلنسکی
🇺🇦
درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69107" target="_blank">📅 12:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69106">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=MLFHVASvREdvF3UPIOv-cpLDpomcdfdEZahcz8DHgfqYl5njrhqwcCa0n_H21NfJmPeI3xb6mAFSZq0zbMKkmzETLIlVFQzt9LDBcc8a1wjrmh9Yi-jr5ZaShCh8Wu26ToJbuUYj_2-G0mbDniIMMGrYYbIruckkpmEI3IodwhCDcQN_iTRxlO8QvPxPwx1Le8IXnnbkyf6Wxn3FC0lI9oLVIxvf4aCGmMXA9fKv85A4Ian1lZIk33D4F6d5hqYxD-UijmzrATIsJMkpPG-La6--6cs1e2WKFbd-665-dUp2oJfIYSnVxDEt0BqXsklpv6K5T7K6WLDx6GX6zKB6fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=MLFHVASvREdvF3UPIOv-cpLDpomcdfdEZahcz8DHgfqYl5njrhqwcCa0n_H21NfJmPeI3xb6mAFSZq0zbMKkmzETLIlVFQzt9LDBcc8a1wjrmh9Yi-jr5ZaShCh8Wu26ToJbuUYj_2-G0mbDniIMMGrYYbIruckkpmEI3IodwhCDcQN_iTRxlO8QvPxPwx1Le8IXnnbkyf6Wxn3FC0lI9oLVIxvf4aCGmMXA9fKv85A4Ian1lZIk33D4F6d5hqYxD-UijmzrATIsJMkpPG-La6--6cs1e2WKFbd-665-dUp2oJfIYSnVxDEt0BqXsklpv6K5T7K6WLDx6GX6zKB6fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=MPBSwoWY-nYaizgu1hUzGZqKow24AFB5bfDUcXjLZSzgONCKJt5eSfPBEMgTozJeG0e1ClMH-01IPlGBNtANFADQSeBuOchHx0HVWTqcvy8aPMEKpOtQEDkVxZVNlMatwGJxvhhV0_m1H4RWTQCu_3ijeog_Sfg1BNF8PhW-53HTIPQQzvO4v7v43YlvRYp7F__2L_xvodR3foBa8nVudrD44fKEMs2grNz8bLq_x4q2cCTxGgMg9VHo1vL97aTkyQ7CjBWQ1g9pqgsaUdej3K4xOp8X2JNFce6YJYIsGGla9kV-lge1DvXx2jHIVcGTnoaWSQf-RUThaDnIXNJlwRDGb7TmwJ2icW7g-I5_yK7JvUzMeceLXTkZIsnjTrQfTINi7eJPXmUO_QlmGa_xc35ckd6fGve2WW1oaarKT0KS0A4bcG3TORL_eS8xFVrGPg99qa2HSMbV00WWwPEi5l-snvA4IWhICwACCVijOK01FqSTTsKbJf-QtdMbqkuaXLGiBrYpKOnZKOC8_D1i9Kwtn8MUJ-TfPz-yBVhRuvM-dm0Mgoe8OdR5oS5x9_z161pRdb6RPJJYwLZtYzZe5GN_LaAVCptl4IU_IbtG5rdnwgK6vd9xuQfHpWvK_1RFWtPz4Sx_OmkpyahtUhPUn9R6HEeZBjXeP0BOKW7tqw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=MPBSwoWY-nYaizgu1hUzGZqKow24AFB5bfDUcXjLZSzgONCKJt5eSfPBEMgTozJeG0e1ClMH-01IPlGBNtANFADQSeBuOchHx0HVWTqcvy8aPMEKpOtQEDkVxZVNlMatwGJxvhhV0_m1H4RWTQCu_3ijeog_Sfg1BNF8PhW-53HTIPQQzvO4v7v43YlvRYp7F__2L_xvodR3foBa8nVudrD44fKEMs2grNz8bLq_x4q2cCTxGgMg9VHo1vL97aTkyQ7CjBWQ1g9pqgsaUdej3K4xOp8X2JNFce6YJYIsGGla9kV-lge1DvXx2jHIVcGTnoaWSQf-RUThaDnIXNJlwRDGb7TmwJ2icW7g-I5_yK7JvUzMeceLXTkZIsnjTrQfTINi7eJPXmUO_QlmGa_xc35ckd6fGve2WW1oaarKT0KS0A4bcG3TORL_eS8xFVrGPg99qa2HSMbV00WWwPEi5l-snvA4IWhICwACCVijOK01FqSTTsKbJf-QtdMbqkuaXLGiBrYpKOnZKOC8_D1i9Kwtn8MUJ-TfPz-yBVhRuvM-dm0Mgoe8OdR5oS5x9_z161pRdb6RPJJYwLZtYzZe5GN_LaAVCptl4IU_IbtG5rdnwgK6vd9xuQfHpWvK_1RFWtPz4Sx_OmkpyahtUhPUn9R6HEeZBjXeP0BOKW7tqw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=LQzTuf7GvSYrOr7TAvDBnQ7biEvcXE_yBR9v3QoT9p5IfsnL4IsrmRxh_z3ZNgWf7y5RU-AK9G3RxxOfXv68lMWQKsg9W5b6u-LLu0pmpfeQyTLjaWDBaanbmNS6zEwXulLuILDnhvFeJBeYKuRvX88EJ2iTaD9mRKtV_9t_Z82KG-SknlDueE7dsp2dM4XMNi00--8ltuQBBLg5IOvhOFOL2v44nHBxWHu3IHOToXJCRMwhTOcH3Wj7Eviv7E6HhJnD734TZoCEVsUfWZkr8K0F7DKQrgC6UJ_w6fUGmXMbd0OhVszSSHlfgvtRjdFuPCJ22_9esRBqekrA0ngxtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=LQzTuf7GvSYrOr7TAvDBnQ7biEvcXE_yBR9v3QoT9p5IfsnL4IsrmRxh_z3ZNgWf7y5RU-AK9G3RxxOfXv68lMWQKsg9W5b6u-LLu0pmpfeQyTLjaWDBaanbmNS6zEwXulLuILDnhvFeJBeYKuRvX88EJ2iTaD9mRKtV_9t_Z82KG-SknlDueE7dsp2dM4XMNi00--8ltuQBBLg5IOvhOFOL2v44nHBxWHu3IHOToXJCRMwhTOcH3Wj7Eviv7E6HhJnD734TZoCEVsUfWZkr8K0F7DKQrgC6UJ_w6fUGmXMbd0OhVszSSHlfgvtRjdFuPCJ22_9esRBqekrA0ngxtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6zrITkEs6yqnBCvjHB4vadcHeY9Hb6DM9HRpD-iko6melg-p4wBtC83DtiGiRKJkwYE8k82x1pCCkjujE_de4Nmi1eZdu-lQADOVF4jzfNE09QUPpeDE6vcUortw2DV33cEQhFJavBdoTQrvYlRqSAWDeHJxWliQPnGliPP8M8dtV-fvKd8-pfEDLV_BBuuJSNK_H4SYY124vNR6vG8pFOrn9ZcV0dNEyUtSPE9EqTomV6BP7FoKcgSzEDsP7kU3Dh2PTcu1RmmZ5IAxwvzZw355pWWG_AOOYq56BGRzmd7xrc5cRB4LD2aPYXQ8tSVmckLWY4fwrVlIZi7typGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=Pt_mBNaYYcmP4qSBzAzdcY25xVHBuGdNv-t7-a1ZbtT6Dqnvz7Ic-6jxe_5sV_qaJXB0YBNGQMlPp4JW0HkG2O22S1EIxbuqSwCoak8vHEn7lnJkLjGRswp_LiSzxlD6-o0sccRRJC89ZH3zxzao7Blz-PULPmRMOsoOhKQod8ihWZCaKaSMSRz9EfFZlseaBuc_8KvtOH2i8uR3kO4v2aPQZVgf6Rr6GBDdKjIxs8RyqjVKd77lR04XyRUIxhfrX8G7YkSdULB1IuNTDNNcYJyqqaK0Q9R9_nwCObYfCRmlZNJbGkafcMrtdve_tLcyu6IjLbfFFECMkR0SVOJZtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=Pt_mBNaYYcmP4qSBzAzdcY25xVHBuGdNv-t7-a1ZbtT6Dqnvz7Ic-6jxe_5sV_qaJXB0YBNGQMlPp4JW0HkG2O22S1EIxbuqSwCoak8vHEn7lnJkLjGRswp_LiSzxlD6-o0sccRRJC89ZH3zxzao7Blz-PULPmRMOsoOhKQod8ihWZCaKaSMSRz9EfFZlseaBuc_8KvtOH2i8uR3kO4v2aPQZVgf6Rr6GBDdKjIxs8RyqjVKd77lR04XyRUIxhfrX8G7YkSdULB1IuNTDNNcYJyqqaK0Q9R9_nwCObYfCRmlZNJbGkafcMrtdve_tLcyu6IjLbfFFECMkR0SVOJZtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgmZNJm7T4Bt-bn-hQgDHGF4OqtsI_dMiQ_NCr99FaBkC4uTX2RUaBaRsR6-5TWRp1Qlu412qo-R1q5dT_rvSabhUrU7ZM_lYB_hG9kz4YKs9M8mGqBlMYo_n3_mFJpOc2ViHWlUb4xvLf0vgdG0mMKbXC1ROY91GgggtjksqVRAy5ZYmmD_5yA7rufgD1TGgL-xoqVLtxgKsLs0FkpyQoELT7LFKyXFJ7e5uLcMk7-AGFnTNWdAWQ6OnlI9u7IagnAMK-xFkOz53XxOWaPjLQdwPELf6CT1PBbvTV6WeWNC0nKcvh-LIFZSkdRNlsA_krdvzspnN4Z2aTt88Ol0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JByPKB_KwCzI8Pp3oETuT7soOgGm6YiBzU7vvT-mKmg1mY8xch-qKGGRbXhGnOhRCBESaOmtTy81WBFlvCE-dbU-sn4vI_Bkq4xha3iae_MWCm86QUypBiDWaKpiSiwIjyf7RN5zRl6vsZ-2mF-QWbKcaGlKyj7lsxUE-ZoAo-UQYABSGFEmcC2CFOlR4mFlFYKl-SMYv9KwjMwkpjlhOAymNKL6GqFhK3wtkPbgxXhL23ZeExAfNG6uk2u_51A3d4R6vz2_x8hgtRsC6lDuyL34NI1cuPX5BafmbNBNIot4ERllvgdNyXp92S9GIjXpyfM76sWINX0Tw3hPQeHgIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=mXHLGz9kXk55MBcYqY0ZbQBGogQhzgACbzhqlCotnVp_0iA6WSo9uBYhfkOSh5rmbUDKZab8JdYJmAU4RAf3XJF26bgBXx3wrGjDu_Ox5G3yHvlPW5c0vHXqVKA2Y0eUmg3edPuhKvd3ZY-iBbwCcxui_ksiBxk6yLU2SzlLsq8Y0muzlda1hqC9Rq-wusUxG-UvZSDpQKjid7G03QE5O7O2B7Fq9q-93lOBCk6FqKwabkGdWwioiPOSWJ4CfzjlJYZNdfEtO8ph3HczaXScHqOLu6nL3VwiGSytJpV7LxhVcuDi61PNhylL1JxO03gIfxNKOXNKaDd5Ih9Fj1Tr-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=mXHLGz9kXk55MBcYqY0ZbQBGogQhzgACbzhqlCotnVp_0iA6WSo9uBYhfkOSh5rmbUDKZab8JdYJmAU4RAf3XJF26bgBXx3wrGjDu_Ox5G3yHvlPW5c0vHXqVKA2Y0eUmg3edPuhKvd3ZY-iBbwCcxui_ksiBxk6yLU2SzlLsq8Y0muzlda1hqC9Rq-wusUxG-UvZSDpQKjid7G03QE5O7O2B7Fq9q-93lOBCk6FqKwabkGdWwioiPOSWJ4CfzjlJYZNdfEtO8ph3HczaXScHqOLu6nL3VwiGSytJpV7LxhVcuDi61PNhylL1JxO03gIfxNKOXNKaDd5Ih9Fj1Tr-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=Az8uBklwXw-EocNCEch_ifIFVBR0HfL4HuOr1ebH3cvPWTJh3Ywk7WnW9yFmzVGYoatNf4tH09IVVzlywziT2XW6dabg5FEKsCV0JrlOgBsWDztQBqnu_iEXLEBacfO3PkUl7fEZT3IB6vIwWS1ZDQfrQHx0H8jb_bwcspc7opmcojiCAuVviQX3nVOucWVWHyL3Uais_sbll57-dPHjTCFyW9hanHGYbolAYG6BLIze0HAxlFEF1NWsBepYTYhnBF5WxacgkwW-f1E14WVwUCPUt44jQkB45zzNdmwdRek01xHaOjsTfSxZKAY86X6KRwy33jJ4WUccyE2lAEtdAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=Az8uBklwXw-EocNCEch_ifIFVBR0HfL4HuOr1ebH3cvPWTJh3Ywk7WnW9yFmzVGYoatNf4tH09IVVzlywziT2XW6dabg5FEKsCV0JrlOgBsWDztQBqnu_iEXLEBacfO3PkUl7fEZT3IB6vIwWS1ZDQfrQHx0H8jb_bwcspc7opmcojiCAuVviQX3nVOucWVWHyL3Uais_sbll57-dPHjTCFyW9hanHGYbolAYG6BLIze0HAxlFEF1NWsBepYTYhnBF5WxacgkwW-f1E14WVwUCPUt44jQkB45zzNdmwdRek01xHaOjsTfSxZKAY86X6KRwy33jJ4WUccyE2lAEtdAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
