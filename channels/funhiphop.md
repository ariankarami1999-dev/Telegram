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
<img src="https://cdn4.telesco.pe/file/fxibIMi-HLzfU5Ye3DlVNumLiD5lXY5fiOBwkNADAy-Kx6hEcbs6KRn37RfYde4nxQ-a4LrhZ7GhaIWaKPnn50WXQlR-WrqqLUW71XrTr4HvAZqZ0f0ud4STxAy9bmt-qxI7DNeai8QClt5p3b-LhpaY-9_ZhWSFKNCw0AeUd3azo6lm02ialKLQsCIGFNc3L5z8FVgElTwbL4nCgr-03zz7zpj9RUIakuz-BS6iZcflH46fBMj4kd3Qg74ZLkCQRqecobXEeXakDgHceEQyGMI9m06KH505iOxSVXuFPhAlNrcxBkmk0PsEGPnnMiOvBXnWq9NIbRwfq9jKVHys2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 169K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 22:41:32</div>
<hr>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هلند تو این تورنمت همه رو سوپرایز میکنه
یا با قهرمانی یا با حذف مدعی های اصلی
این پیام بماند به یادگار
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/funhiphop/78303" target="_blank">📅 22:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گل پنجم برای هلند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/funhiphop/78302" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سوئد یکی از گل هارو جبران کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/funhiphop/78301" target="_blank">📅 21:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حساب کنید ژاپن چقد سوپره که ازین هلند مساوی گرفت
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/funhiphop/78300" target="_blank">📅 21:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الله اکبر گل چهارم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/78299" target="_blank">📅 21:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گل سوم برای هلند
سوئد پاره شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/funhiphop/78298" target="_blank">📅 21:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گلر هلند عالی بوده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/funhiphop/78297" target="_blank">📅 21:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سوئد زد ولی رد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/funhiphop/78296" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اسرائیل آتش بس لبنانو که پذیرفت الان شروع کرده غزه رو میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/funhiphop/78295" target="_blank">📅 20:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هلند گل دوم هم میزنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/funhiphop/78294" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هلند گل اول رو زد به سوئد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/funhiphop/78293" target="_blank">📅 20:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGfWcI2yeYLYaHftHZpswNfTgjVDwBz5wEhRtlCqMwkW2HSOIsxcD05qcVWCOngkeY40Qd_Hvy8818UZ3pLPaX2u39x6Ro1oJO2xfEYVYkQCAIev8nOyFAXFtCVro_u4U-lb4--8bUi-j_6TSalJ794W5-v9bgKZdOqQF6FsVR6qB7rcnBdEyTCjqiEAzAfb_t1NZ_SCEmMejs1Av8sP7Ehqc9NKsHyIhyXLOkm2O7pwhkY8lkx3QFd0ouyQh-s05IOvZ_wGdmzO2f0NfTkRtbilSYmCSsdvq81M_Ol0hABjnV6Si5RmFs66TEBkqUf5Op3gN6SVqaKBtn3VjmY70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه هم با باخت امروز صبح از جام جهانی حذف شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/78292" target="_blank">📅 20:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaVbpnZaYNYsLA2xaVnsRO6PNbrs2H0SoD-DJZKtsNnFkc9wILGvbOcWgV4WJgATdRNU7e5_Mp3I-As-ZhxFg7aJV-PG-UfzDojqGSzC2Knwo5F2lYJkC55rSlkY-k0ZYmPMe73JnwxhArplbPfy2WoO_Qh_5cmScb3zt-hYSGhLFiBgIELYXUKFKdYYFh353kVO8igZPeiaQ_bdmCl9XxwRUSBUsCZ22hbb8ROag6LneFdXWHzn5wZXEfzCq0rvozkh6cMqkKLcWI458nd-dZiyBIKxCAqi1EWrmwRNQWeP5nP_U-K8Wa_7tdX07QnuYaDuk6HZSg5CAjEaD6Qg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPKoXYIvgDu9o12hiUUqIRifih2OBVk4xWfBxLlatfNJsvMLXhE2JFAxi8DL34HszcyiokQuj4K6WlWVOkSyhlkH75845SKcslm0AHscXiY-Nk4yI2o1ZNg9yDp-7gVrmPrqGXDwfXr83dvVHsijYPKvNoCC4izCGqWZ03IvlVLZ84qKXqIKvtqyYEnlojO6cOUvqw1QuEzFQW4BNMUtERN-YdFzyQkZt8_FTXTOllwnGh3eCLhZUO7ShqnCbIuGEX75PBCkA3348zznqqTEvIvhMBUPvL1aenAV3lUbNMZwzpkqb-cIs180BzYErXo_2Xzpot1NY0o0SIoZ02FsyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب دو تیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/funhiphop/78290" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-IOZVb7vnE9zYidljHQz7aAaHcmACrTMUESnHYnXvqnZJ65ixxWAYMd6INSUnXaAHs3OvLkjX42976iRcFlX8KMuI4KUXgX_pQQ5PCwwY269os3UPBjaoxgiWs-482E-AVzpkMzCfsxxBW8-tdIYbJIW49e8HJJxB5YmnVqYFyfzZ8Gymq0ZMC1BPKsfF0_u5kwFIqtqL1YMGLc0Gvn4A5fTB6crMmEf6mL9wqFi-uBc3xrpPYrVO7Ry2YQyuLuTYKHBHzCWa3RkN95fgLs88WIh4dWF0zOwsITMP8j_gZzWYc99kZdUiZsFZe1eKwhQlM6dSrWIZai6Wnb-APkDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/funhiphop/78289" target="_blank">📅 18:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcHnPy64UYPiM_rS5gBvMEF2AZfvCsfpjXUyv9cHBx1fn2y6POovFi3t8KWE727VJnNz_TwOQCwHN08V4K12xApHogZh_fQDAYzHU885eqLwi5GlYyPpzI__xkHt_MJN5PxqKQhwxcGVIpeLurkMUGJMFpx9SxPUYz4o2A2UwnVOgGnySn1aC7UX4-AS6JkIALI8tEUZlHaUCTj-PJ9koJbh9yQ0G91yn-3gcAz26VpholBP6T3M7Zrtn3xV5O3VODzGrZQhxLrrYLJw4Mmsm8fukNfBWqKu_p3KN0s68eSYyw0Cmt9Fsfwl4nEXBkQC14ONq4zz-UaCMjCik-L32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداشاهده بمب خنده، فرانکی دیونگ و تیمبر تو تمرینات هلند شاخ به شاخ خوردن بهم و الان تیمبر مشکوک به ضربه مغزیه و دیونگ هم احتمالا بازی بعدی غایب باشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/funhiphop/78288" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/funhiphop/78287" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCURw633-WlvQx9xOc31kHHY_EvPjsjFNSPRcgCHUu9Vm-XwRQ4mVtGubITDcvfGQnvMVB69HPnaFWztPgwWpVQl_OLCBE34CISifKEZoY6qmH1gX5U8ZdeoUjifcszFePLA4LJKx7gmp3fmfqhmkpzmO2wUCYJILbX4pp0o5IylboAQdCqw7-NnVQ18jw1D0HIb0pPYFuRpYmFIxjF8GaLwrzbeNSazPT1njdR_RIxPEsgideHIt79gb8RzQW7TEjQz7axdRUilIYz9VpanE2p_rd7npuKOgss99ZG9wJXmZfIhqlIVWeBIZM6VXomudITwy1wV_HC4tPrz6kapug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
G30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/funhiphop/78286" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8k3B03QqqFtgIuReTj6heX9bsKzpyWkqjTZLZuJXD-P0lJTti7fzkB0jjwv_27I0q3K5mcu8PeTcK-acs1uAOHbDNA8vgIoZHkK39RGtCbcHftH-sKOaQFJDv6Q7njPXhZojxdQd2K49ncXqsM3xbCywHNtRf0oOW_8JKZSyMHsHVI9gSKRILWbUwns5LmUOBtWbeTn0A2jUZTylJ5X40cW11A4Vjf6HjV7FYwpFTlRGVavcgOCDndgW-NH0GjF_pB2aFIgiDM6BWLjE0fAM1a8kp2KyZwzf1E3Cax1jiQjmVwuQey97Q56ubm5dnR3FDQbYsFeDlWTuHE3aOEIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه نتونن تیم ژنرال رو متوقف کنن حریف احتمالی تو دور بعدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/funhiphop/78285" target="_blank">📅 17:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLKglPph_Frox4bUTgYoK2VPwXwOM_AQ4gVLoQ_pbKqo2HnvacDw_y1TEcNl5qmPO0TcaPc3mZWP28b6BEjJjh2EQ8ytbxR_-56VSk1N1rVLMG3itwmdlsEy3ywATlLnd8fdflYpT3c-aYpEzsY5hdp7XNkTjgZpejmI7pR0Q1G3Pq2UNQ-0fp_FBCEivSiaugNa1xlGMTyMztyyyNiv82Kx9sDLzr84Yj2guz3RfAaSNxVVhm03_CQdYcrQ-QETieFPBTYujjIkRkoMfLvlua84nawC8wqzzruD0abI9Hdv1jUD3CGYcK-MhvrX7b1ZEBmJOEh9ODk9_6PibTzudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فعلی تیم های سوم جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/funhiphop/78284" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/funhiphop/78283" target="_blank">📅 17:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ546SPYDOnPVAcGrMpIvSWB9jVjjFjh_mZ3y8YQMQDJP8xsZ-erETJdoiLRN2oKFmw6XCIIoubWu5_TYYq8Gk3gA_Ki05KlJNgiwj5vsrL6DHOgt4lE1IXtt-1bMOE-MgzpY1d9Pe3-icxjcl7dSY6tN6JFS69WZwgiWE7A0V7ESAcmF3G9uJMX_ISxqjGmoz2jV-YQqdpa9XBxYtdJx37p3C_cRlm7I_TedAMDZ7l_iddj1hAsZpyCDyoATIzT9iPj-BY9PJ2Abm8NOex7kCiPzTlEBBbQ4ninwedZs5vOCMV9MweHUBMaazvglvIiyMU3sYBQnZUBp5chdF48nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم بالاخره افتخار همبازی شدن با بهترین بازیکن تاریخ نصیبش شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/78282" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سخنگوی وزارت کشور: کسایی که به مراسم تشییع پیکر خامنه‌ای بیان، به صورت رایگان تحت پوشش بیمه قرار میگیرن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/78281" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/funhiphop/78280" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/78279" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دولت عراق مجوز استفاده از استارلینک و صادر کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78278" target="_blank">📅 15:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhe04G0qF0TAV3GymFjeMjTkKkSOgTDhY_THmQWPPh-x_DL3KrX5Lyvv5_hTIIJXOV0wikAAcFBF3rLu-IJwiWi_8l2HHCsX3WVgNUNbJYNHejtZHPEcrwU9bxiz4aQgr9CfH-iWK0v62LuEOzMnghxTEnUdVVb2HVJmj7Cf4D6aCczGqVQ7_JPVfgxA-jNzZxRN660YaIadnp2c4E3lEIUTi0rGD0wUREQtGR9QqNTlmfvczpEBsRGg6WLj_GE1j3JkDAJE79BLQXh76yymU_umRuNPRmvSrg9km0lSIVO7Kr1F7KneIE1zVGbEuCWS8_LjuwL5fsT_iVuCwFBFnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدینیو و طرفدار گمنامش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78277" target="_blank">📅 14:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78276">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv9niYtcIAT0CelmNIgBEtmUoVp3zMSGCJfyqa0GITBLe7vxnJw3VUCLKpOnKP4rAMazQptCVrB2NrTniD5hECfZYsNKawPEMeN8AuGOntdy-wK81D5_UqJicOgm87qWtkeDYzrTO235SAfDSN34mze_ehMJwgoymkEr2WoYX-wXRJ2WNzqJZ5WHSukVQc-s7YX5gez0TmHaQOi6nFi-miaBM7nMY3rwWdAUW98yHPwCXynsDMAa-uI37OH8WFBl_BMZiBWxVqgDxO9lb4rzybbxdIIza-eurt1Iy7ytYYuMuHfEmm1Fu-TspEmiDUPfkM4buVSOS2b2pv8k7RZKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باهوشا جواب بدید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78276" target="_blank">📅 14:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تو جنوب لبنان داره نسل کشی و زمین سوخته سازی انجام میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78275" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIVOT-iQ9vo3vqbAO0Gw2DHHnS6FzcmmdbMLJdOtbJrObZHMmTMXxa3SYk7iL3opw3EjUHVf-JhRh7aebY9wz5FbQAOfntGv3zOmalKoJAcl1Y6tlmTizte0KnRx9s-RQN_5ohPC3NyFhj-WOC13yuo6_mSQ4WAW9j3pOis598suLSUktxq_FZBh278H0df6XrsRQ04zoPK8HZ-5bQ8FsAZ2vvPaC9GscUegFFA4QCZmyWsHTYpUen9AE62N7UuwEgzlIBq-4CDaOevaFQrdvNGNj-13BJKYnAy6-2mfsEj2UeV9U71ZBYtLnFJEyg4x9LnZb3JpO_skkvTJ3YuXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخواید اعتراض هم بکنید لااقل یه متنی بنویسید که با عقل جور در بیاد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78274" target="_blank">📅 12:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78273">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4X4rVzSepZ2dBxExb05esSqrKW333rk0dwBMOdQKv5rUw3fR-BgiXQNWxliwiSG_JD67hCZYDxwI7J1Gfj1xnjurT4ZDODs5Td_3iuvawCfGz0WUIrwrBKUnxE_9OHekuMdlZ_CpKyIVIjE2__a3HpbdDTaUN24fO6ZfEsrAM0NHv5Y7n6H0-NGKIR4vDnClr0aBccWqpStaNDFwIRYkD9UpU6p1v92kj4ZmJldPt7Q6qRsf8Z-pE1VUjbuAi8r0pPI93XrNlysiHKTMyH3fVHfoJX9gbMAEdNT-YQjt5uuYZlS8sycGfjQl4RARuhayG39VV7AmTteuGDleuXVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیک‌تاکی ها هم کم کم دارن آدم میشن
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78273" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78272" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWr8lWHltcBk-Sdi_0ZKqoM9jyOSY6C7zQLmmQV3fYCPe80p4q7ChKQylFY_u1UWctjFsEx3KyFni4RY2xELslYIK-5HUJUFzvv6fEgailUynemUbSvCy1Q7jmKwK-eSkLprRpgQ7PZomrPQngHgWSU5ggf9kfcYUhg0Y0m4RTqHPKKuciJlsKZUSB0XhjzxAPMMpBH4P5FKsYbbymVszkQGYZ3QsN85EdK5NBii0hZKZIY5t0uvNUKlAVpzrI96FUlyszrk8cTnStkomcBaKEuuHywSEFkH-WfLqsCfQoPPfrOkJKE6jR7qFoQ71qCfCFyL9BvqNjp8twnV5MoYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
R30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78271" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78269">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نمیدونم چرا بازیکنا برزیل نزدیک ۳۰ که میشن با هر بدنی تبدیل به شیشه میشن، من دوسال پیش اون بدن رافینیا رو میدیدم میگفتم این اصلا مصدوم نمیشه، حالا ماهی یبار مصدومه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78269" target="_blank">📅 11:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الان وضعیت جوری شده فنای مسی دارن از پرتغال تعریف میکنن فنای رونالدو از آرژانتین
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78268" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78267" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گل دوم برای آمریکا
پوچتینو تیم خوبی ساخته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78266" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ دوباره مصاحبه کسشر کرده که به خاطر اعصاب ممبر های عزیز ترجیح میدم پوشش ندم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78265" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کشور جنایتکار آمریکا گل اول رو زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78264" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بازی استرالیا و رقیبش هم داره شروع میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78263" target="_blank">📅 22:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78262">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcvs5vUGzgvmz7jDKpLJaFsLK60w6d7nEPGH8J_E9V_pb2JQv3tGo4g_rZ8jh63li31-RowDTfe0E9K0epyjNSVrkE5xMYugkbpZhofJ3Y9ENIJG8QdubQysdSv2FoZnT69sDKlrM_5jEzcgWuWrgmovGjSjs82TjIrK6jNRzj-frCvBGYB5afRUZAol4wK0KjBEtXe2h2b_QobVykoN0pkOWvFL7FL6YNmxxERcYergKQc9QWyUKWbWStOE-TlWwizmYB3w4ByU5IFeOwnYmPjRNCIye4ANuiQ9jbA7JreMSNTAf4I386boxsnMmjBUgULJ8JVRbcnH0A6yMeh01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین رونالدوی موجود در جام جهانی 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78262" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifffpWl9jdiw7hJ9GW5ijKPr0NOn4D3bEg1N5x5DPNz6-Kid8UmhdQD7f3jEk9tN8kpm3NltfFEOfer6MKkU5y9gTW_7gex2l7wXzS2ZhUqKxfWi_ETXFCZLvPZtuujiEjNtkzx0JHmbRvmiLtmqy-RpYF8mmucQeI60rO8r-UFD965iVn8AVpP79B0YE1MxOMyJkTqbxolGBqVLWxcplxrHolmV5CjSjY1B9fJkz0qr-WBkrhyqqNJh_emhsRayCUAUc8-UjoAnYEk6-sMm3agy9b1lMP0xlhLlNl4vBLYwuDX-cxldE_dO9I2b-QdRpU1J4N_a-0tYv1pkV8wZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید کون میداد تا بهش 10 بدید؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78261" target="_blank">📅 20:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فنای رونالدو به پیج کل بازیکنا تیم ملی پرتغال حمله کردن دارن فحش میدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78260" target="_blank">📅 20:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kse_yNLF36XzjYJFL_WAHOyTwJ7_XNzq0p4wVpxNWvtWh8uSZRsJrRAteHIeQX8-s043rAFQLPVxJPZ2I9g_SnnipbvS-Dh3VFH9L8AAVL4vGobB5F33fCojHjXEN29LlX2Rt6FTq7_FOT7eIBB3ShAAuv_ZlCz0vfa0pyohqfTbDe0M8iX_4yZvUhM8XCia0VVNsLnSDbsSR_AI6idiObCTMUSxFd0lDTz56O6f9IM2TPgwyHpC_TvzCeS4t8ulkWeVIYgsibzcay6RDSDf8xD8CkZfIEgbiyLQvq3q87Kbn8kVqcMukqY5D84-6-Y4lEObHyUdJ-96wF-Ha0MYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید شایع به نام بلاتکلیفی منتشر شد.
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78259" target="_blank">📅 19:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شایع ترک داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78258" target="_blank">📅 19:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUTfOvnFkTLPywQmGDSUf1pVaM1u3zGQkjuB7PFMMDQAGB9o6VkHwnJ5ujZAWAIAAMvf3-kOfW7UE3nvAIQlCJAdKMw23bE14nfSrGGYXjAL_NSll8012SxYvEA02NwiOQ-JVZCPh_21FgEEFHpr-fkWHrmW4tK9G_ub9JnVllNI3rvuQDgAJ6oBETYa57DSLulxQ1JBrtbM6WPCz9CeXc6li-3uBkixPljNOOJ9MBPOa3gR-cY_CgI6Q8OBSN-2GRWFLprLQyS5xjkW1sdx8hfehwwJUeD1Pm7Sy_nTYRaiuJ0cSC2xD0r3PpTixH9GB7FtWS265BQGNDffe1__cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنیف عمران‌زاده: یه شب تو باغ با برادر خانمم مست کردیم تصمیم گرفتم از فوتبال خداحافظی کنم، به خانومم گفتم یه پیام تو پیجم منتشر کنه که من خداحافظی کردم از فوتبال، فردا صبح بیدار شدم از تصمیمی که گرفتم پشیمون شدم ولی رفتم تو گوشی یهو دیدم همه واسم پیام گذاشتن داداش تو ادامه مسیر زندگیت موفق باشی، منم دیگه مجبور شدم از فوتبال خداحافظی کنم با اینکه دلم نمیخواست این کار رو کنم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78256" target="_blank">📅 18:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg5q6P1qKI6OMgUUx9bJWUwOcoGkk_QmNSfNHFksUGKJ_tlgrGmFxu8ehJEeV40aXBj8fJHgTzJsq2nXqCwpLeZPY0wK8IcXoc7YKXfP9hJQrTRuNgWYzYO65uZFKF0_DUg_ZxKOjelmbzvidAm0SJ9-O6DqIRwjiGKNN2oyNVIt9h5TOc0CXgg_DJIa8AKs9PhPcvcv2yK2N-5_mIbfBDVkf6E77m35d-jJ4eJPI0cSTLuKFGS7WdsbWol7mNUqX1mG9iA3o80MYjl4Dv71MzJ8VZs7parYa_83-78UFhUUhx_iAAxzjQHHBNx5ZWkFXqlwhzYzNWasV1WnEh6Eng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78255" target="_blank">📅 17:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78254">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo3-BhYh3VyEqaV_64v9QoBmKQF1--Av3NJRTBEEjtkTzOXr9Pz9ZV_PFPx90-Ttbq7AhIj4FoB9NvOt5dC3sZKMiVY7kJ1L24FHOFFkr-pTArhMc3iEeH5cxuW7pcD5KsAAqzyzGWAeD3QaXo3eQsrOugJi7n7QYfd1CFh9FJKLFio3BXi0ypoSv3ddiuVtki2xUjDBtytZvV7oXBe6jY58YV9uKE6okcVGXLLalripPtnTTE7wU1ZPUCKBzMntvqe_zL28m7js7Fg3P6T8j_w2fdtGn0d7XuIJ1JS4WBv7VCkUqloYaUCtY3iU-QnYyq3kqerXCsL1G0UYHkwugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78254" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78253">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جام جهانی ۲۰۲۶ با بری بت شیرینه
🔥</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78253" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78252">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎁
🌳
جام جهانی با سوپرایزهای بری بت
🌳
🎁
⭐️
تورنمنت 1،000،000،000 تومانی
⭐️
✨
شارژ اضافه
0️⃣
1️⃣
🔣
برای واریز کریپتویی
💰
🏆
5️⃣
🔣
کش بک روزانه ورزشی
🏆
📱
همین حالا در بری بت ثبت نام کنید تا بهترین‌ها را تجربه کنید
✅
G29
🅰
🔴
ورود به سایت
👇
🔴
https://gfyweuuchsa.shop/fa/affiliates/?btag=914641_l303106
☑️
کانال رسمی ما در تلگرام
👇
☑️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78252" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78251">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiySquM0zmNM34TlB95LdcmD3cOvma2VwobWu7MtdvP7HWlEdn7izWe2z4DcdEWa_kYfM6eEbRFxK5oO9j2zmwqSnEr_PGtwWwCifOEUKHL1AxMSLc0u6hqq6S2yjPS9KD_BwS46vgtqmu394eDK961RYedR1560q4PqQsxUIhBZIMEMZ9MEw6R2x2qHZ_yzvzX_B3kUEN-Ubt1i_S1w0rEBCmilWZmnWI2A7x84McSHuh8idysIdhV4t0oFOj_H5MjWGN6l_xLMKzrSijtajFeqrcbpI64my-NxjWQDD5cecJVH4ptmKT4CeP-yeWEyNflMB5gTRhSIPFKfY3g_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژوتا یالا از قبر بیا بیرون پاس بده دیگه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78251" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rysKxa1OjS2WKcsrROaYQX63F4hz9v_aNsuoDJ8kXo0wsu-n2tC_8UtlE3cYZ88WY_O_-C2XgHvKhJl5cyq3N2R3HfFH9BdNKcFB-eBxf3jvwpNOvuav-T34odlqaJ8Vc6fLqkjzDymaBp8U9iC0hLXpMtZyK6VZLRWNDNtZ1APJ52kDglxVJsN4ava_BhHPAo2eK7SddsX3abSEVM7DFVhD4YzndAKAYVSwP020mTkd2YpjcyyfEKnrx1AvlhiFsvtbBxDBMmhrkoEA6cK_Gf4gX_xtFvDa3ZSSFszh-ewzmmowN-OArmJaUiai3h6Vq-TvB75sy6XcMEm_RQPE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78250" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMjr5eLvA8oxXBhgIf8IFJkq84511DFYB3XFZh77bpOAucH_e-D5jnNHBBJtpzWaAgnX92ZeLinFLuSMZTgG_KaBb-piPH21GEJJEtTb72BpVsBXwRoIn7UVKCNN93uxVToc10pwadHwc7hwOP9aOELb2GMHwZeu444wVYQTPRctDBusO8TaAmx_m1ImEVVq56wsmm5ElSzMWpWRfU6dj_069wl6-IVGNQCK3_24LXUGd8M_83cny_RqVm159KWGnYet_z2K3lNFyjniMOVA0fEyB7ie0Nt3dqwAlw5LCtUnb-GiXib-8uCI2LjiSOhJRKyDJwMCgUV4ZftbYoC8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در واکنش به لغو دیدار فردا و کنسل شدن مذاکرات:
«ما از روی استیصال به دنبال دیدار نبودیم؛ این ایران بود که چنین درخواستی داشت. آن‌ها تمام شده‌اند!
ما همان مهلت ۶۰ روزه را تا آخر اجرا می‌کنیم.
هیچ پولی هم دریافت نمی‌کنند؛ حتی یک سنت!»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78248" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOlC-oTTpnvU40L9LET6DaSIq90Ja2tOL1i_SCkP2GtTIAZN0Dj6cTYbJ4zNo6g50t-0pQplhIK2V6jR8p0ND0q5QqAlodeHcybK8CjxpHxpG9BCIsbsGfGdEJIrOvjQdgeAxT7HIN8jvwKXSRdxoHUJ81nKWwAH6dT6PlI-QYn5VMzcIX1OJfzf4kRwb5Eyi38Wd6lN-Edb7ZHnesf6gzE2oJZjCegKNMwk874zmdr9MIrDyVjvDXz4jtda59vHYv9a0HYHWlnx9_KQ0V1nZM_0Q7ESmvkv--7fmIkcYIYz4z5XUg2ncvCdgZQ-k1x6MhGkc6l7wbrzTFNwBnHzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید بهزاد لیتو به نام "Late night drive" منتشر شد
SoundCloud
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78247" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نتانیاهو: دستور داده ام، جنگ در لبنان با تمام قدرت ادامه یابد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78246" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ میاد خایه مالی میکنه و میگه اسرائیل باید حملاتش به لبنان رو متوقف کنه وگرنه باهاشون برخورد میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78245" target="_blank">📅 14:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سپاه باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78244" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78243">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">معاون راهبردی پزشکیان: تجمعات شبانه باید جمع شود. آنها سلامت روانی جامعه را بر هم می‌زنند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78243" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مادر اشکان لئو رو گاییدن الان تو کماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78242" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIeDJxjxRl-0zL1mKp2yInqm_C1AyOZ3smYA00Pk3SVCR4i7tNXugvlYHvUf9gpAj0ZeyI9kAd9v_r5LtUq6v8RhcPIz2AlZENNw9UF8SGl5X-HQ44xKPmronllfLVKMFbplKXT0mgoStb0XSsTyIG0Eb2z1Ss9Pq0QljQ1n8LWXvpiq1DzYIPYxSRFiYtCVQA20SBq6tyRiHUOLhFxtnkGCkhQi3Dj2UN22QXttfp4GsSYmR6uDzxV7uve5sU-7PvCuKL-PDm3TFzFIRO-Q1zeFXom7blaj3Mqbq_lxMdKVNqq6YzBGtVwV_ImJ0c3sRHDegL5-W3TFe_QkTMFCiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم ترین دغدغه این روزام اینه که بدونم این یارو پایین تنه چی میپوشه میاد جلو دوربین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78241" target="_blank">📅 12:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جنوب لبنان چرا منهدم نمیشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78240" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsuXVmgqnFJdLO2739SII0M33eOQQ14Uie6DprcA5FY1JBUODVlu06e2HbEYFbd-dMcaDM7-4-O2F7ZqbjFlqo4BOcwTMHZ7tjT6Q3Z1jTeuJXvyuf5dzTjebK6Vb-bX78smXGUHLdYUbZBHl6Mx9BQIdnPLYtutvGNukkEr5iiaVV6pNlw6BZlsJMFJ0fm4lSbc_FizIk0XjmzuDI_994WdQvJ1QV7TVijZeyPcMPa0sHsixNTJPKgsszNG0xDC3cxDXWENt1JDzCZLwxov7Gw-KnS6glefetLrzujo_1CuBvWqu5fb-HNuq3om3Z4-WTD7RqkjmOB1hbeUjiCJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبلنا که ترک پوریو میذاشتم آرشیو تو کمتر از ۲۴ ساعت بالای ۲۰۰۰ تا فوروارد میشد، امارش تقریبا یک سوم شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78239" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tak2jhXWPCBC0m1GoixXxEJzZrO3KWIpqwOid_CJ63lDNhKVhCnMjMxPE2HL_WFRxq1ehdR-08lIQwhsAxY7wHtngHCFn1OAI5mkJ1xgT0ov7gy24Jg_2NzZQCGChPIEAuAmXJLZ3KzD3z64Hjy9LR_BzGrDhhPPx6AQq_kKmVIx831JcXlNFdYL1dfN4RTeBmgdkwlAKSXoFL7oLwNGwz4R1r2ivZtajWcEEol-L22xauKaFH0bL-S_str9QCoxkjQ5ckTB7FoY0e-AFbfgAy98mOa_dMJbTne9q-pvdgQbC3m6EZqwRFa7e17arBpOpJq8nhxYPxS7aCtlFFjJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای مادرجنده
💔
آقای مادرجنده چقد فید شدی آقای مادرجنده
💔
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78238" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78237" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78237" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NchaK_gcgZFuBaAmdeWtqm8ni0j05pEli6Mp876dXT2J3areQ-r2nAPfCQaqEqqtgQ3JDnMukcX5tFEw3KCkPQESynlqeA2PhVzlLsiUdKloNhHnFjNScZqsWRRlxyVUr4no0WKntDHQdn4ensI7XURhF9NBC4YZpoklg5clfLba5S0XVJ8DYKLbUUNekFzOT_OnarjIE2j-OwFNrJFgCQ5eKYOBCaWBG_EjDmeStO34YmXWmk1Psx2u1huL3N49P6bIV2dl10-zbosGofo4uZrZoQ44K-IYU5BYR6mxOyIiyyrTgwIXhLHeeArt4ldWC2j6AJG4g21neRd_QiKF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r29
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78236" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سوییس کنسل شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78235" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ولی سکانس به درک واصل شدن حرمله >>>>
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78234" target="_blank">📅 02:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دوستان کسی از ساعت دقیق پخش مختارنامه خبر داره؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78233" target="_blank">📅 02:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78230" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اون سازمان دریانوردی که اسمش یادم نیس: تنگه هرمز گشاد شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78229" target="_blank">📅 23:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تروخدا وضعیتو المیادین: هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78228" target="_blank">📅 23:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تروخدا وضعیتو
المیادین:
هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78227" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78226">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شجاع خلیلزاده به عنوان مادرکسه ترین موجود هفته اول جام جهانی انتخاب شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78226" target="_blank">📅 23:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1_WqaarR_qGN7cu_18_CQxuJfhfdO-W3LXofv2A4FSFXDnrZKYQGe7KtTj2nMLHn1NItM3bQE_4ly-GliDVTMsNBmdoOl_qC32GMqynHbKaJyTw44kdcrdLvxTknHH4U7aRltYGq7chzctTz0XOFXcI7tviDjlMJHw1OKIywDNJ-3A-P_dE3lCiZccOADBus-o8vWaBxGepkcE6NbYvTPPQTh36v4LCJ7iHc_giTjqvBQyZG_ijq1FNXm7fmHStqUCdiM5w1A9SBYZpMqhcAhwS5A_RbwAGsG9GmWjRHTczQG_BxVaxCgYx75Jr8dfQWnupf-soOSkLu8QDLMo6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام چه داره پیشرفت میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78225" target="_blank">📅 23:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78224" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78223">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWeera news | ویرا نیوز</strong></div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78223" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swO8gpq3hgLMD3v6k0E1TIYSvzCAwaacW5zsac4TnBYVHaeSzkpXO_UaQqp_KzuhprHECfBci_wzPWOXhWvOuuvHraI2u_tssnLgTdvUPkQb-nyYq_1CYgieuatoNqEjyvh4YvX_jyrPmW3X-8JR4ggfTBCRBSMPqc7gl4o3hbIveh3BETFNovLQtOuha4icGjYdikhaqVAoY5iNFXqAJPOcJ4M-iEJuUDmUngUxkp5uwqYRIAQgwPQKM8q3lQgY5d7lN4ylLe9_CAjXZ5ZLiEELiMhK7CBUJ_WvlL9DmE9NE7xUEWRTle1WI1QnETqZN4-keNwjJb0QoOSkdjvPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون ۱۰ نسل قبل یارو نسل کشی کردن یعنی این دختره خوشگل نیست؟ خار منطق
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78222" target="_blank">📅 22:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78221">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خب حل شد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78221" target="_blank">📅 21:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78220">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شما جنبه افغانستان ندارید، بزار یچی دیگه بزارم</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78220" target="_blank">📅 21:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پوری کیرم دهنت کاش خایمال نبودی</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78219" target="_blank">📅 21:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تنها کسی که میتونه برینه وسط مذاکرات تندرو های داخلی ایرانن، تحلیلای مرادویسی من‌باب نتانیاهو همه کاره اس رو جدی نگیرید، نتانیاهو خیلی وقته قدرتش تو لابی کردن در آمریکا از دست داده و توهم اینکه آمریکا سگِ اسرائیله هم از تفکرات رائفی پور طوره
ونس امشب یه حرف حقی زد، نتانیاهو بدون ترامپ و آمریکا(عملا یعنی بدون جمهوری خواه ها) هیچه.
تا فردا صبحم لبنانو بزنن هیچ آتش بسی نقض نمیشه، ولی تندرو ها تنها کسایی هستن که میتونن کیر کنن تو توافق بین ایران و آمریکا
اینکه مجتبی خامنه ای امشب همه چیو ریخت رو پزشکیان اگه نتونن جو رو کنترل کنن میتونه استارت یه درگیری داخلی بین موافقان و مخالفان مذاکره باشه
تنکس فور یور اتنشن تو دیس متر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78218" target="_blank">📅 21:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78217" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862002bab.mp4?token=nXLu4AtoZDl7DdBvKnS28lr6bFm65jPzVlXt7e5SZPf9KPLAlnInS3fJpKc-tJTTZFztTK64pooLv53126RC7zqZS7V_bo9PcaYGPzSRGSj4LE8_fJLoG2oW1AOWPKs9llesxwrUutm52dRKFu2hDWV9Mj2i1StXSrK5nAofei2BVqzjh9FF-89w5p-IVcUk7J3oW-yMFUbN6N-k7cONbtpnKIKn8oo-NLI8OCGu8rB4CyWfS8wC45uS-Wd0VPnc719ux1deE_xrfpoXT4sZjzffLB2_FtdAU2_XYtAz-cpTUMjaexNUEmHiniUMzgpAwWlKPrgPSBBB7iFbsspdcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862002bab.mp4?token=nXLu4AtoZDl7DdBvKnS28lr6bFm65jPzVlXt7e5SZPf9KPLAlnInS3fJpKc-tJTTZFztTK64pooLv53126RC7zqZS7V_bo9PcaYGPzSRGSj4LE8_fJLoG2oW1AOWPKs9llesxwrUutm52dRKFu2hDWV9Mj2i1StXSrK5nAofei2BVqzjh9FF-89w5p-IVcUk7J3oW-yMFUbN6N-k7cONbtpnKIKn8oo-NLI8OCGu8rB4CyWfS8wC45uS-Wd0VPnc719ux1deE_xrfpoXT4sZjzffLB2_FtdAU2_XYtAz-cpTUMjaexNUEmHiniUMzgpAwWlKPrgPSBBB7iFbsspdcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه داروین درمورد تکامل انسان
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78216" target="_blank">📅 20:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">محاصره دریایی تموم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78215" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78214" target="_blank">📅 20:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78213">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNleRhmcyTCzeIHsD0DdLV97WIeXmuwKLjcZly8ls_i6piV1D7RLkllRnBKlD-S9cOg_l_zsiKmec6x86NlBsRNTGCjNL-rhz2r-NLzgfsNwpUWsZNrXacGfwdyOlZlTFEoxgtTPqqccE30sEPHOlfIA6CUc_XOhrLB-LD9-I3JLbwOC_UL9IUE-FPOPlhQnAojxUOel0exv4g7UdaZxySVga8laAXFRI1AvjyFuzYyWSJpG5J_omcedsEFI7SjMxjztWmy2vnWzPCy6d9-NZh99V0KCU2Jg62gfopF6__Ibt3YktT4uxvRXVOORRdZtf_QxtudLOpJTSmWB023Fdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتو جدید ممد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78213" target="_blank">📅 19:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78212">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3knChbBGr-CiabJ0O3zKRKJ48RBV6lxkYJxKoQCARkXxK_515W39GbXJ68Dnh0Gy840Jn8ekT6yvGAgJoaCtoFLhOXmp0Fj231VRVI3EWUGoraWbuJol1doU3LJRRv9d3_KFMI073NpU10kLMnxegA262GyXXHcBaEmvtZCxBriAm71PvSgtdPNu-C1_maJjyxIn4Xd4mUjbcANWKcbk3IuiQfhDj0c5VVaukB63-fgkKMXI71znzvaEsTxuoLR8q1fxCrNMk665RGd5YJA2IAYdQQEdVvlLPYOwUD5kRq5LnQLhk8al4SaHsUy3uQVINTArkLrxQ_RLMceWQXhvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری عماد قویدل برای پوری
@FunHipHop
| Behi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78212" target="_blank">📅 19:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DB0n3J6l4xD3C8ho_937yWks2Hj_ayqfBv6HTsAYfcByyYsRjXzasd01FeUv5HRgar6y7TuUvcp43UDrSfJnOSl52uRbY-LpwN0IMI_6jV5pxQ493c7C6RVxz5ygpmnSZvxc4cW0NqjXaKcnYVCbC2BD2Dea38NuI4wWsM7VgQPxz6aUSeUK7Ld5ZIq3VWCbBn2p7A3nswIKUkpAjSmJx7HGm7C0JSYl33S4OPHKB9uArnXrUnbq72LYuDTExlXhH_PtK-01f3VNct1jWME23IQTgPKgmjR17tIR7oWug8_2SIpKwxHWL1UvufFkGGJC8e0PLAvApSZ69oXgTEd3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 کامیون ایموجی خنده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78211" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78210" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78209">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAZ9fgPIoakZq0hMIJBzVtysWZkLJjqkhijCSxgJwS6WOOdNa6luIQ9XeOujIQgradaJd1ISBqATWH6PzxuUhn0bcHCTWiyRcIHxE7w_UKl8E03drshRbKCBy-ch0HW6CxCu6MRNi9QD3RZhBR2klKwCkP4Z69oMmVW0QiPyg5excA8qWWjNBQC2OepupZ4PcKoYAf85aunQ1UE_Vv4F-JawO09W_2Yrn_WdUUWNDDIFvXCCIvXsGXBQfuaF9wP2a2xwRDVSI01on0H6tnNr5-jVvTCKXeH8z7DidUobjKJIc66hBVnttexxGWmZ_gadX0KahTREJaORqqo027aShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78209" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEKGDztPLpByX_-8mhCyXL-al8GYhYhOWdKsu5mj01rFiti6bhKRaTAp8KnWk40u_QD-cWcK6ipyxiwABuhKqAaYGLORpNXWABRnsoOSqA3fDvAHIprvH7Jn3UCjwp2x5fEc-ELCn4hBmHcSnZbXgIJzJNGiAEF2KMqo8UnEQnDqwpPbCyO4OLX-PUd2sIaBbXbl8wAJ5w42bsGq3KrNGfhldh6Ze82hoNBIFC8UZuz31wbeaew8fOQZnKtNzjFuNzFAV4a8xysx8nPFwXzvKJ4viOfqHW-XQIffnblPILQOe50PrIfeXbI18Ao9ToZS_ym6eAyYsBW1_pWJYoDuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ساله ترجیح دادم پول سیگار
بشه غذا واسه حیوونای تو خیابون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78208" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78207" target="_blank">📅 18:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFyLsJUaNhlDG0KC_9KTVYYptm4XQydSF9taCKPTu5K5yY1iyZw7VavrTb0K11zdlU_8lO_U3rr7G06o1sKWME0vpXNhCOX-9Mhj0LsAazoiEoKe0nif1SU648shpXZUaPi2LS8r0v0Gr6WS_1sRnOC00RtSjUkT3dR06SJrzJ5bNG3FWPG1B5Mm9GGbxB1Csm9zLjc7FjqTvJLBx4RwsX-Q7r5QZadOAPO6KoAJrXudciZQ3dpD2tRK6GvobbyREESMTofAnNNklfK27Ccnl8RGpxBc8ztF87e5BPz5s9Qtv9GKWWtKRfiinwWwjrFBWfXjWH9nsPZQAuJ_YJvjjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب جام‌جهانی
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78206" target="_blank">📅 18:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78205">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLk</strong></div>
<div class="tg-text">بچه بودم دوست داشتم مثل رونالدو بازی کنم،
الان رونالدو مثل من بازی می‌کنه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78205" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78204">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnafaDqwvsSO0g2C6Xa1LOkYvJ5MVSCpbicFyjjxRWyJEj9m1LYxmrlqlnwWrX_fHmA37KVTdw3FkmIRwSFvQpXop3yPtVT7agylIQDBAhV3OZZa3_ZV4BPIRrxWOoj2K6zQ5u5k1a3SsxQTdnX47nHGamCLrNTnBCDmLT-gcv35sTv0_Q6CpBuad80Z0D7dj35lv2Nv-FsBEWLyXtaa5IbbZfLy7sXhrAgp5M2R_WXV1wyFBu1_WcoB9-i-E8XZFoFWX2lXaAXSrpOJO-YqpeFYAUtjBvECIhJTW1LQATNYjFINg4A8ff8COXyko78u0v7EFIF1GtqWENMSfQljFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای تاپ دنیا توی اولین بازیشون درخشیدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78201" target="_blank">📅 17:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJUoaPuGDwUcc5PMgPpsfWtBUqo-46CUiEqMCWGv9R66wvEIB4ERZX3cTAtbpJnLo5Iw64378ZxlNMqsbFd0Qs6I2nG1HXwnNDhtIX_dPgpt2h-n6USSJklcnt9vBXA7gCYggD_DKgc44pWRmoUSBKurTokohAbguoHYi4P3-rVhW8Ds2kMtZXsZK2hVietlMGK2eTU7waUYR0KzNDXXiPIbYDGDWYVHb4Eb6b1-gJIEpJq03KRHYGirOnQhTij-uhlw60j0KkoZwltQItjPylAEhuwGl1PdRcGxDqz4sc9OVCbwaIEcSXj0uXrOhqdZZGrpExyTkiEEeQOwi7Ybew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم سرپا ریلیز شد   YouTube  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBZh2JbSqwuHN55xkntvkuPd9om9WxCkw7JVKOVekgdBtRD2efxCTvM3GBogC9CCOk57HJ1T-dbnDNOJXVxCABGYzB2HPwGWjGFw_Pv993VR7H1vKYDCrgZMX1sEpH9I2UgUO2nFEQvBP63C-i1ViNS308mOW7taHoegVCcsXr5QDN17vp087VZLfBgU-g_NWt22lr1ASO-wTHuEexyB0gkn2r3RR2eBfngUJh_mrIKouROhNxz-y_pMXjnvW6yTPdA7sfklQ1m7QAwj_HVWZp3Q0Q4azKQebKNlknCe0QZYDohjHclmgmdMGPaJIQzWR_cctNZB2Z6yQ4v0QHbf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم
سرپا
ریلیز شد
YouTube
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78199" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78198">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وقتی مردم ایران صدای بمب‌ها را نمی‌شنوند، ناراحت می‌شوند؛ آن‌ها می‌خواهند همچنان صدای بمب‌ها را بشنوند. چون آن‌ها می‌خواهند آزاد شوند.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78198" target="_blank">📅 17:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ: فقط مردمان دیوانه میگویند کشورم را بمباران کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78197" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bABqz3bJ_4Z7Y-kofnuHyjFxutjmCKU0nX0274aOA8XkbpOxBV96aGNi-MUAO2UtjELs2FhGxzQqntNh8FB7nYEu2aWDEbpvVZshcXrPZFiB6mM7SKjiO6jwCwCpCRjoakLa1lHjvqTfXNqcNBNQpElYajr7YmOT2aFAcmXJ2Bbk3_S2b7m7fJ07XRj50mCgJ8moyQyCRCNZZ0DBD8zw5eVo5XK6Nf3w249g4GY3R5Gmjgjs3uw38LKlY5n2eiqlsPk_viHiUcnLPSMRPRK6Nlp-9cFRA8ZB_6Aee-aX6ZWfYISX9yDf_Z4Y9f2l-HWCuKsCOdIruzivb5cPVcCjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78196" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
