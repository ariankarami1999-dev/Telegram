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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 21:22:25</div>
<hr>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گلر هلند عالی بوده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 490 · <a href="https://t.me/funhiphop/78297" target="_blank">📅 21:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78296">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سوئد زد ولی رد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/funhiphop/78296" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسرائیل آتش بس لبنانو که پذیرفت الان شروع کرده غزه رو میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/funhiphop/78295" target="_blank">📅 20:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هلند گل دوم هم میزنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/funhiphop/78294" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هلند گل اول رو زد به سوئد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/funhiphop/78293" target="_blank">📅 20:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGfWcI2yeYLYaHftHZpswNfTgjVDwBz5wEhRtlCqMwkW2HSOIsxcD05qcVWCOngkeY40Qd_Hvy8818UZ3pLPaX2u39x6Ro1oJO2xfEYVYkQCAIev8nOyFAXFtCVro_u4U-lb4--8bUi-j_6TSalJ794W5-v9bgKZdOqQF6FsVR6qB7rcnBdEyTCjqiEAzAfb_t1NZ_SCEmMejs1Av8sP7Ehqc9NKsHyIhyXLOkm2O7pwhkY8lkx3QFd0ouyQh-s05IOvZ_wGdmzO2f0NfTkRtbilSYmCSsdvq81M_Ol0hABjnV6Si5RmFs66TEBkqUf5Op3gN6SVqaKBtn3VjmY70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه هم با باخت امروز صبح از جام جهانی حذف شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/78292" target="_blank">📅 20:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaVbpnZaYNYsLA2xaVnsRO6PNbrs2H0SoD-DJZKtsNnFkc9wILGvbOcWgV4WJgATdRNU7e5_Mp3I-As-ZhxFg7aJV-PG-UfzDojqGSzC2Knwo5F2lYJkC55rSlkY-k0ZYmPMe73JnwxhArplbPfy2WoO_Qh_5cmScb3zt-hYSGhLFiBgIELYXUKFKdYYFh353kVO8igZPeiaQ_bdmCl9XxwRUSBUsCZ22hbb8ROag6LneFdXWHzn5wZXEfzCq0rvozkh6cMqkKLcWI458nd-dZiyBIKxCAqi1EWrmwRNQWeP5nP_U-K8Wa_7tdX07QnuYaDuk6HZSg5CAjEaD6Qg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPKoXYIvgDu9o12hiUUqIRifih2OBVk4xWfBxLlatfNJsvMLXhE2JFAxi8DL34HszcyiokQuj4K6WlWVOkSyhlkH75845SKcslm0AHscXiY-Nk4yI2o1ZNg9yDp-7gVrmPrqGXDwfXr83dvVHsijYPKvNoCC4izCGqWZ03IvlVLZ84qKXqIKvtqyYEnlojO6cOUvqw1QuEzFQW4BNMUtERN-YdFzyQkZt8_FTXTOllwnGh3eCLhZUO7ShqnCbIuGEX75PBCkA3348zznqqTEvIvhMBUPvL1aenAV3lUbNMZwzpkqb-cIs180BzYErXo_2Xzpot1NY0o0SIoZ02FsyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب دو تیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/78290" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-IOZVb7vnE9zYidljHQz7aAaHcmACrTMUESnHYnXvqnZJ65ixxWAYMd6INSUnXaAHs3OvLkjX42976iRcFlX8KMuI4KUXgX_pQQ5PCwwY269os3UPBjaoxgiWs-482E-AVzpkMzCfsxxBW8-tdIYbJIW49e8HJJxB5YmnVqYFyfzZ8Gymq0ZMC1BPKsfF0_u5kwFIqtqL1YMGLc0Gvn4A5fTB6crMmEf6mL9wqFi-uBc3xrpPYrVO7Ry2YQyuLuTYKHBHzCWa3RkN95fgLs88WIh4dWF0zOwsITMP8j_gZzWYc99kZdUiZsFZe1eKwhQlM6dSrWIZai6Wnb-APkDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/funhiphop/78289" target="_blank">📅 18:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcHnPy64UYPiM_rS5gBvMEF2AZfvCsfpjXUyv9cHBx1fn2y6POovFi3t8KWE727VJnNz_TwOQCwHN08V4K12xApHogZh_fQDAYzHU885eqLwi5GlYyPpzI__xkHt_MJN5PxqKQhwxcGVIpeLurkMUGJMFpx9SxPUYz4o2A2UwnVOgGnySn1aC7UX4-AS6JkIALI8tEUZlHaUCTj-PJ9koJbh9yQ0G91yn-3gcAz26VpholBP6T3M7Zrtn3xV5O3VODzGrZQhxLrrYLJw4Mmsm8fukNfBWqKu_p3KN0s68eSYyw0Cmt9Fsfwl4nEXBkQC14ONq4zz-UaCMjCik-L32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداشاهده بمب خنده، فرانکی دیونگ و تیمبر تو تمرینات هلند شاخ به شاخ خوردن بهم و الان تیمبر مشکوک به ضربه مغزیه و دیونگ هم احتمالا بازی بعدی غایب باشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/funhiphop/78288" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/funhiphop/78287" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/funhiphop/78286" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8k3B03QqqFtgIuReTj6heX9bsKzpyWkqjTZLZuJXD-P0lJTti7fzkB0jjwv_27I0q3K5mcu8PeTcK-acs1uAOHbDNA8vgIoZHkK39RGtCbcHftH-sKOaQFJDv6Q7njPXhZojxdQd2K49ncXqsM3xbCywHNtRf0oOW_8JKZSyMHsHVI9gSKRILWbUwns5LmUOBtWbeTn0A2jUZTylJ5X40cW11A4Vjf6HjV7FYwpFTlRGVavcgOCDndgW-NH0GjF_pB2aFIgiDM6BWLjE0fAM1a8kp2KyZwzf1E3Cax1jiQjmVwuQey97Q56ubm5dnR3FDQbYsFeDlWTuHE3aOEIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه نتونن تیم ژنرال رو متوقف کنن حریف احتمالی تو دور بعدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/funhiphop/78285" target="_blank">📅 17:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLKglPph_Frox4bUTgYoK2VPwXwOM_AQ4gVLoQ_pbKqo2HnvacDw_y1TEcNl5qmPO0TcaPc3mZWP28b6BEjJjh2EQ8ytbxR_-56VSk1N1rVLMG3itwmdlsEy3ywATlLnd8fdflYpT3c-aYpEzsY5hdp7XNkTjgZpejmI7pR0Q1G3Pq2UNQ-0fp_FBCEivSiaugNa1xlGMTyMztyyyNiv82Kx9sDLzr84Yj2guz3RfAaSNxVVhm03_CQdYcrQ-QETieFPBTYujjIkRkoMfLvlua84nawC8wqzzruD0abI9Hdv1jUD3CGYcK-MhvrX7b1ZEBmJOEh9ODk9_6PibTzudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فعلی تیم های سوم جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/funhiphop/78284" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/funhiphop/78283" target="_blank">📅 17:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ546SPYDOnPVAcGrMpIvSWB9jVjjFjh_mZ3y8YQMQDJP8xsZ-erETJdoiLRN2oKFmw6XCIIoubWu5_TYYq8Gk3gA_Ki05KlJNgiwj5vsrL6DHOgt4lE1IXtt-1bMOE-MgzpY1d9Pe3-icxjcl7dSY6tN6JFS69WZwgiWE7A0V7ESAcmF3G9uJMX_ISxqjGmoz2jV-YQqdpa9XBxYtdJx37p3C_cRlm7I_TedAMDZ7l_iddj1hAsZpyCDyoATIzT9iPj-BY9PJ2Abm8NOex7kCiPzTlEBBbQ4ninwedZs5vOCMV9MweHUBMaazvglvIiyMU3sYBQnZUBp5chdF48nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم بالاخره افتخار همبازی شدن با بهترین بازیکن تاریخ نصیبش شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/funhiphop/78282" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سخنگوی وزارت کشور: کسایی که به مراسم تشییع پیکر خامنه‌ای بیان، به صورت رایگان تحت پوشش بیمه قرار میگیرن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/funhiphop/78281" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/funhiphop/78280" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/funhiphop/78279" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دولت عراق مجوز استفاده از استارلینک و صادر کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78278" target="_blank">📅 15:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhe04G0qF0TAV3GymFjeMjTkKkSOgTDhY_THmQWPPh-x_DL3KrX5Lyvv5_hTIIJXOV0wikAAcFBF3rLu-IJwiWi_8l2HHCsX3WVgNUNbJYNHejtZHPEcrwU9bxiz4aQgr9CfH-iWK0v62LuEOzMnghxTEnUdVVb2HVJmj7Cf4D6aCczGqVQ7_JPVfgxA-jNzZxRN660YaIadnp2c4E3lEIUTi0rGD0wUREQtGR9QqNTlmfvczpEBsRGg6WLj_GE1j3JkDAJE79BLQXh76yymU_umRuNPRmvSrg9km0lSIVO7Kr1F7KneIE1zVGbEuCWS8_LjuwL5fsT_iVuCwFBFnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدینیو و طرفدار گمنامش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78277" target="_blank">📅 14:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78276">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv9niYtcIAT0CelmNIgBEtmUoVp3zMSGCJfyqa0GITBLe7vxnJw3VUCLKpOnKP4rAMazQptCVrB2NrTniD5hECfZYsNKawPEMeN8AuGOntdy-wK81D5_UqJicOgm87qWtkeDYzrTO235SAfDSN34mze_ehMJwgoymkEr2WoYX-wXRJ2WNzqJZ5WHSukVQc-s7YX5gez0TmHaQOi6nFi-miaBM7nMY3rwWdAUW98yHPwCXynsDMAa-uI37OH8WFBl_BMZiBWxVqgDxO9lb4rzybbxdIIza-eurt1Iy7ytYYuMuHfEmm1Fu-TspEmiDUPfkM4buVSOS2b2pv8k7RZKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باهوشا جواب بدید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78276" target="_blank">📅 14:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تو جنوب لبنان داره نسل کشی و زمین سوخته سازی انجام میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78275" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIVOT-iQ9vo3vqbAO0Gw2DHHnS6FzcmmdbMLJdOtbJrObZHMmTMXxa3SYk7iL3opw3EjUHVf-JhRh7aebY9wz5FbQAOfntGv3zOmalKoJAcl1Y6tlmTizte0KnRx9s-RQN_5ohPC3NyFhj-WOC13yuo6_mSQ4WAW9j3pOis598suLSUktxq_FZBh278H0df6XrsRQ04zoPK8HZ-5bQ8FsAZ2vvPaC9GscUegFFA4QCZmyWsHTYpUen9AE62N7UuwEgzlIBq-4CDaOevaFQrdvNGNj-13BJKYnAy6-2mfsEj2UeV9U71ZBYtLnFJEyg4x9LnZb3JpO_skkvTJ3YuXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخواید اعتراض هم بکنید لااقل یه متنی بنویسید که با عقل جور در بیاد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78274" target="_blank">📅 12:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78273">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4X4rVzSepZ2dBxExb05esSqrKW333rk0dwBMOdQKv5rUw3fR-BgiXQNWxliwiSG_JD67hCZYDxwI7J1Gfj1xnjurT4ZDODs5Td_3iuvawCfGz0WUIrwrBKUnxE_9OHekuMdlZ_CpKyIVIjE2__a3HpbdDTaUN24fO6ZfEsrAM0NHv5Y7n6H0-NGKIR4vDnClr0aBccWqpStaNDFwIRYkD9UpU6p1v92kj4ZmJldPt7Q6qRsf8Z-pE1VUjbuAi8r0pPI93XrNlysiHKTMyH3fVHfoJX9gbMAEdNT-YQjt5uuYZlS8sycGfjQl4RARuhayG39VV7AmTteuGDleuXVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیک‌تاکی ها هم کم کم دارن آدم میشن
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78273" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78272">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78272" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78271">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78271" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78269">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نمیدونم چرا بازیکنا برزیل نزدیک ۳۰ که میشن با هر بدنی تبدیل به شیشه میشن، من دوسال پیش اون بدن رافینیا رو میدیدم میگفتم این اصلا مصدوم نمیشه، حالا ماهی یبار مصدومه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78269" target="_blank">📅 11:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الان وضعیت جوری شده فنای مسی دارن از پرتغال تعریف میکنن فنای رونالدو از آرژانتین
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78268" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78267" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گل دوم برای آمریکا
پوچتینو تیم خوبی ساخته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78266" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ دوباره مصاحبه کسشر کرده که به خاطر اعصاب ممبر های عزیز ترجیح میدم پوشش ندم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78265" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کشور جنایتکار آمریکا گل اول رو زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78264" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بازی استرالیا و رقیبش هم داره شروع میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78263" target="_blank">📅 22:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78262">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcvs5vUGzgvmz7jDKpLJaFsLK60w6d7nEPGH8J_E9V_pb2JQv3tGo4g_rZ8jh63li31-RowDTfe0E9K0epyjNSVrkE5xMYugkbpZhofJ3Y9ENIJG8QdubQysdSv2FoZnT69sDKlrM_5jEzcgWuWrgmovGjSjs82TjIrK6jNRzj-frCvBGYB5afRUZAol4wK0KjBEtXe2h2b_QobVykoN0pkOWvFL7FL6YNmxxERcYergKQc9QWyUKWbWStOE-TlWwizmYB3w4ByU5IFeOwnYmPjRNCIye4ANuiQ9jbA7JreMSNTAf4I386boxsnMmjBUgULJ8JVRbcnH0A6yMeh01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین رونالدوی موجود در جام جهانی 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78262" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifffpWl9jdiw7hJ9GW5ijKPr0NOn4D3bEg1N5x5DPNz6-Kid8UmhdQD7f3jEk9tN8kpm3NltfFEOfer6MKkU5y9gTW_7gex2l7wXzS2ZhUqKxfWi_ETXFCZLvPZtuujiEjNtkzx0JHmbRvmiLtmqy-RpYF8mmucQeI60rO8r-UFD965iVn8AVpP79B0YE1MxOMyJkTqbxolGBqVLWxcplxrHolmV5CjSjY1B9fJkz0qr-WBkrhyqqNJh_emhsRayCUAUc8-UjoAnYEk6-sMm3agy9b1lMP0xlhLlNl4vBLYwuDX-cxldE_dO9I2b-QdRpU1J4N_a-0tYv1pkV8wZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید کون میداد تا بهش 10 بدید؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78261" target="_blank">📅 20:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فنای رونالدو به پیج کل بازیکنا تیم ملی پرتغال حمله کردن دارن فحش میدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78260" target="_blank">📅 20:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kse_yNLF36XzjYJFL_WAHOyTwJ7_XNzq0p4wVpxNWvtWh8uSZRsJrRAteHIeQX8-s043rAFQLPVxJPZ2I9g_SnnipbvS-Dh3VFH9L8AAVL4vGobB5F33fCojHjXEN29LlX2Rt6FTq7_FOT7eIBB3ShAAuv_ZlCz0vfa0pyohqfTbDe0M8iX_4yZvUhM8XCia0VVNsLnSDbsSR_AI6idiObCTMUSxFd0lDTz56O6f9IM2TPgwyHpC_TvzCeS4t8ulkWeVIYgsibzcay6RDSDf8xD8CkZfIEgbiyLQvq3q87Kbn8kVqcMukqY5D84-6-Y4lEObHyUdJ-96wF-Ha0MYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید شایع به نام بلاتکلیفی منتشر شد.
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78259" target="_blank">📅 19:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شایع ترک داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78258" target="_blank">📅 19:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUTfOvnFkTLPywQmGDSUf1pVaM1u3zGQkjuB7PFMMDQAGB9o6VkHwnJ5ujZAWAIAAMvf3-kOfW7UE3nvAIQlCJAdKMw23bE14nfSrGGYXjAL_NSll8012SxYvEA02NwiOQ-JVZCPh_21FgEEFHpr-fkWHrmW4tK9G_ub9JnVllNI3rvuQDgAJ6oBETYa57DSLulxQ1JBrtbM6WPCz9CeXc6li-3uBkixPljNOOJ9MBPOa3gR-cY_CgI6Q8OBSN-2GRWFLprLQyS5xjkW1sdx8hfehwwJUeD1Pm7Sy_nTYRaiuJ0cSC2xD0r3PpTixH9GB7FtWS265BQGNDffe1__cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنیف عمران‌زاده: یه شب تو باغ با برادر خانمم مست کردیم تصمیم گرفتم از فوتبال خداحافظی کنم، به خانومم گفتم یه پیام تو پیجم منتشر کنه که من خداحافظی کردم از فوتبال، فردا صبح بیدار شدم از تصمیمی که گرفتم پشیمون شدم ولی رفتم تو گوشی یهو دیدم همه واسم پیام گذاشتن داداش تو ادامه مسیر زندگیت موفق باشی، منم دیگه مجبور شدم از فوتبال خداحافظی کنم با اینکه دلم نمیخواست این کار رو کنم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78256" target="_blank">📅 18:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7H49ui8FRuVPj-5KWhNrAPHst3D64s1fULPP4PYpFQVF0IUCHTJUor0dUj-ltbjj-nwU6nyv-U_B2StxHJOeNV3UOcIq1f6UXR3ofcflwWrbLQsmxxx2fHa5beAjL4JkSX3BJvFEp6xWgYdoJpbe6GVC1SW43ym-U0yO5atAv0xe7cONHDb1qUvCx6B0tnzA9NG-D_-sMqXqM9r6cUx66MVmeR6gR4lAxTgV3rAVY4bW6A_MuoqHiu-ARlNX6IAckp6lWamc9UKncYXxdv2knFN1LuId5yesAxIfmcpZ1ER-LDR8ozqsCUMsbAjqvtYV7NTq4unC5s1Tb3ZnnAQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78255" target="_blank">📅 17:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78254">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amIsB4EcoH-NBDwnHdPN7h0pDE7fkn2QlY4NfVrrX8KcoE0u9oh4im9CPNDFa3hJnYAOh-Ddwz_Rc7GtymQ60oEaVW-AlY4RMf1OYfm5jecPkbMlUiVjyPJzYWaE1JX9F14yr2cRrtupMRCbkxxcRlkahlKpsfWmKyBgVepMm0qvKgM4O0kdwwxkgk0XPbMdB34sNFmU-IEUsYaFdVi5A1-4TD42s6mfD_H9s6sbwegCX5KalS_h7sL4VaiVIDT23P-pQ6LhWPi4LiWO_KvKs1hmk5jeI1VUmt72O4xDbAA_fRTMh78lslmjiSu5nskA_q9WIlDn-UHuRF0P7Jc5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78254" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78253">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جام جهانی ۲۰۲۶ با بری بت شیرینه
🔥</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78253" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78252">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78252" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78251">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyuFjM6KGVGIfmPoolqhyglS4C1rOyRsRkINyO6ZeJ4SUkQKgNl2RG6D5u6P1pf6i3ny6WzOU5jXwr-bBDTUrwmqnWRNskPjS4Al5CXv19N8ElUGiyvWd9tikleyP59Ismz_uAT7tsiuQsD7vc4VSF-pRxgeQqfuba3QV8dvQ3_1sjBNbIGraql32HqOGqBRcx-6kE0JGW9x-10Dhdxp5eBGOSw-rCxvd1CFO8GET9ZHRDCRj_tptT_9ZwraqSkypGu2t38XNtcIOcVewByO4ZmUKLKWT0XnlKvfVLAgB3M1LpIG5nePxWYe-ylXvF0MArNACNXHL-fUz6MRnsa7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژوتا یالا از قبر بیا بیرون پاس بده دیگه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78251" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rysKxa1OjS2WKcsrROaYQX63F4hz9v_aNsuoDJ8kXo0wsu-n2tC_8UtlE3cYZ88WY_O_-C2XgHvKhJl5cyq3N2R3HfFH9BdNKcFB-eBxf3jvwpNOvuav-T34odlqaJ8Vc6fLqkjzDymaBp8U9iC0hLXpMtZyK6VZLRWNDNtZ1APJ52kDglxVJsN4ava_BhHPAo2eK7SddsX3abSEVM7DFVhD4YzndAKAYVSwP020mTkd2YpjcyyfEKnrx1AvlhiFsvtbBxDBMmhrkoEA6cK_Gf4gX_xtFvDa3ZSSFszh-ewzmmowN-OArmJaUiai3h6Vq-TvB75sy6XcMEm_RQPE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78250" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcE3RDfxUfraTrGJpbYN91c1aXq4WlaQNWDWgN8yTNuJEsu4B5XlsDaAocNERe6VqGpnq-LfB8kekWYzGQXmeVUN7HiAjxexNDsMjnnfBYu5TgVYQWlTqSKbiuhlt5sIqvJLOO745xHgCRS2Dlg8JTbeRGekVIjqtU26en0a21jXYyJWg2nyn72c5NVNZL6-eZjiA5kbi0zqKzVXnTmVdSAVuGDBon-cnI-K5uLqMP3hmCJvdWhCRqBHcA_fHoJINDG9nF3d6o3sJCyiuB5zHDleuXXeL_tQKkaaxEZ2CoJnPAwVAAdYotUyx_Hwnv5B4LiD1G2lfjYQ-mglDY9yGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید بهزاد لیتو به نام "Late night drive" منتشر شد
SoundCloud
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78247" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نتانیاهو: دستور داده ام، جنگ در لبنان با تمام قدرت ادامه یابد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78246" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ میاد خایه مالی میکنه و میگه اسرائیل باید حملاتش به لبنان رو متوقف کنه وگرنه باهاشون برخورد میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78245" target="_blank">📅 14:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سپاه باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78244" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78243">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">معاون راهبردی پزشکیان: تجمعات شبانه باید جمع شود. آنها سلامت روانی جامعه را بر هم می‌زنند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78243" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مادر اشکان لئو رو گاییدن الان تو کماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78242" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8GVhOSdFeK4MDsbxZaPicyEloCHfdTY7gczJTPjeb_bWbcg-NwYaZZDl_gWWU6AxHwFrzi_sZXvSrFxP7ywjGhSu9KTSdUG6pHDJcMN2wtdf5xqKXRTgECHPrD93MisywFuLlcjbmYLIurC6OnHviClM-f2KUKoOTNNegN93dDoIYKTORejRXv7pXSKBEC8Utbs6wjuXo0ITl-BBbcIdbAqstkZX2A8hZSn07L3hIs_mg8-ArTj2Ub6278pXUIj7rUt1dMSahbolMVna-uCvNP-vH13d16zqmEToOoHlO6VFnAJxjLNtAlgwjPcapDYSvXJoT54XIZC4PT6piom5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم ترین دغدغه این روزام اینه که بدونم این یارو پایین تنه چی میپوشه میاد جلو دوربین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78241" target="_blank">📅 12:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جنوب لبنان چرا منهدم نمیشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78240" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvlYqW9_p0TaXmkqDuvY0opG9V1KieWMY6DGvxy3wMeoRLZV6I1klSS2pqxUQQSRnbsgxDggpwC6xqT61xCHQoifPIWxqoAUWBGcEFQzDZ9SYoOZM2oliEgxhZmN-jnFrvfYEb6uPuNfcFfJONSv15OKxeF1LShqBkfiHD8MmkEq3TxNoyw6mVbegfEGTZbpVao7GWu13p_XcLPTBG3vsTgDVPuID7J0yRdITlxLRcAd4t37n5UdDnlXVGbzs0iw8FQ035QJG2Dm085ej-PcwJVq8Aje3n5XJEnPfO5G14rjJ_Y6MWK1AEZKnideOkcnvxtDXOsISWo4YYyIFEVaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبلنا که ترک پوریو میذاشتم آرشیو تو کمتر از ۲۴ ساعت بالای ۲۰۰۰ تا فوروارد میشد، امارش تقریبا یک سوم شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78239" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcEmHpz0tH0w_RIljwOnZsDxe0gOhvgQ3NRSPkBskcfGq4-eYJfKxm2P-56bUgEonx155W4SEY7mBzESypcAtAS4u3WzazULfUQcZuzIjtGuNwTtFiq6frgrjF3pQKCgdOnWX2Yci87ccwjTZ01wOL0yJ0BvuN3LEvFNOyanSfsnkURQPzt1ZBt_Sn6Nuo1WaSKMILb_M_l-JsaeH2wKGNEXvr10nGOZr1Y9hxSEYHo8WT1T3Agx1xXXa41xPb24IoiGib5IBHJkpZ064ykJp_IAfDTWL-1zmc8S-CYgpNoUHoil9JvXlhVUkEcjpJJI8qyITK_Ck58LSLEd1Z8yUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای مادرجنده
💔
آقای مادرجنده چقد فید شدی آقای مادرجنده
💔
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78238" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVeTVbcsA8RDdmj04iytq8X_JgMbzGelXB2t6JE8DSmHpArH7rEFN66cUo_GjYEQLvMPPPKpvpTEvP3-vwgnzjc2XPzYGEaOZbIZ5oA5oRYvTGiT0CrNo97gIvZn-ShZo9h3CkK6pQuxjuOq_cJmFcOiojEabPJMwsXjz_98SAxyxEUXDnYB9W57rWGcmmYRcYUnlAwI4wHDvFC22x1yEpAId3OfXsrnDocnWgyReYsOag48Cfn37ZHL9vWtyoLsSkrs-Q4BAYx_O0tTX94VPoKPNfixhMNUOBDYbSJsDfgmoguwf311qXhc_GLXkZjmw28RL8Fw-toAtbKPneLpgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78236" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سوییس کنسل شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78235" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ولی سکانس به درک واصل شدن حرمله >>>>
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78234" target="_blank">📅 02:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوستان کسی از ساعت دقیق پخش مختارنامه خبر داره؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78233" target="_blank">📅 02:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78230" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اون سازمان دریانوردی که اسمش یادم نیس: تنگه هرمز گشاد شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78229" target="_blank">📅 23:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تروخدا وضعیتو المیادین: هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78228" target="_blank">📅 23:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تروخدا وضعیتو
المیادین:
هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78227" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78226">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شجاع خلیلزاده به عنوان مادرکسه ترین موجود هفته اول جام جهانی انتخاب شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78226" target="_blank">📅 23:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfoPKhkMDaQxlqbNqbjg3NjQEHYSPT4IqGNM5eYX1kpTEEpobOdLG7t6dkl1ciBTxGn6N-5i5c4Ie17VMTDpyrf0d-BmUzgzQqjklBJq1zIYEzkTZ6nz5c5YngAqVfv_jLYt_sMWzNbpA7TUS4aI8FDZY9xhxtO38GWm6_19G_mVQJbVvxWhSfZSAF9Df25DJ7TmD4ZH6EZCZg8Jb25G7bH_kQZPBysZww5wL55kjOzdqn7QZBEJ0FrH5C2Qmj7uVnRuxF7nN3nbwI2Rw0D-YpHbizyQ02LCtSmOkNqnvWpTlIzdqdFEY_X_EIyiuXbi-yGBxIXF9QcWE5tXBd7LVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام چه داره پیشرفت میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78225" target="_blank">📅 23:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78224" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78223">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWeera news | ویرا نیوز</strong></div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78223" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AB_dMk_A7UhZ7ZOL9lEKzGARfpBZdqYKnd3-kFavV2RIQPrjfc8Lh7BWRT0E2uZJGodLbJiUdHNCIwSZaeYGLCvodoeUcSuxhYCr85446F0LECKe6AYZAwVNMrGGChAm-HfXhRz8WRUekHqTl3mHyMlGh-sXZbWgAXrd0q1Tvp_HtzyoeVBvcZf8UPcy9q_gdoUlEDk2VA9j68yAUTSNRWb3E1UArY8X41GzVdOWYY6rYF-9l9DfjXlZacrFoen8Z9PhStWypm1V3b7W6LcmM-p9PgNkYzKggkg6-cxSO886FzWt5zRK7OucLKj4fNko7fsI_OdTGvcWWzXefUCORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون ۱۰ نسل قبل یارو نسل کشی کردن یعنی این دختره خوشگل نیست؟ خار منطق
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78222" target="_blank">📅 22:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78221">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خب حل شد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78221" target="_blank">📅 21:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78220">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شما جنبه افغانستان ندارید، بزار یچی دیگه بزارم</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78220" target="_blank">📅 21:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پوری کیرم دهنت کاش خایمال نبودی</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78219" target="_blank">📅 21:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78217" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862002bab.mp4?token=heZw_91d8MtzIbqhPNijocv-Ghqt74nF37eToX5LHC68ecMHRW9bOR5e_K2O_IrSUZqlqmjf0ibiul1uyv5rMH8g-9RsBFyZf2ri4QeWvy15EynDWDnMk8GgExXWygQuMj8cpBdFDTJRwcaJKV3Z8URN-DzG0WE12KyFIdA7afLxwzeCiuq7SfoJp_XDP53v8f8tmp7oBf3QCKfC6WzXz8l-KG5rG-d3j0t0WH4i0PEP-23T-afvv0uc9wnA45VJlde_QQPpXPPFj90laVdlC8UAJTqn50yXtMxAuus-h9k7DRSP_jT0fGqAtEAlm5eLlxoyqfBFOI7KdWF2bS5vPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862002bab.mp4?token=heZw_91d8MtzIbqhPNijocv-Ghqt74nF37eToX5LHC68ecMHRW9bOR5e_K2O_IrSUZqlqmjf0ibiul1uyv5rMH8g-9RsBFyZf2ri4QeWvy15EynDWDnMk8GgExXWygQuMj8cpBdFDTJRwcaJKV3Z8URN-DzG0WE12KyFIdA7afLxwzeCiuq7SfoJp_XDP53v8f8tmp7oBf3QCKfC6WzXz8l-KG5rG-d3j0t0WH4i0PEP-23T-afvv0uc9wnA45VJlde_QQPpXPPFj90laVdlC8UAJTqn50yXtMxAuus-h9k7DRSP_jT0fGqAtEAlm5eLlxoyqfBFOI7KdWF2bS5vPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه داروین درمورد تکامل انسان
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78216" target="_blank">📅 20:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">محاصره دریایی تموم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78215" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78214" target="_blank">📅 20:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78213">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v22mI94Y2kV-3VCisPSCqq4F2J3UWAKzbtVCcRIpU9L1AltzchJ1Wd5BXqAAyYsuk2ypsc4PqNb7qfYBrNIdJmJxSjTLIxaNP85TIpR8nzzUmtRLiP3cqEYZcl36NvpheFNH_S1eqi3IVtm-H6h-xZp_RKlAd9doYfkqyr8i8yEVeVk4NUTvWiQ6JUk1ol_TLsXoPGl_AUp9CY78RUCRnpjXCKar1Cddi0Mzqyra8Cx99NVhv3ZDm-nkqlBbe6m_ZxSD22U_eDfm5ycjT-ltTuldYhadTlNfse4HRfF6lc0DZ5wxgiZj9Ty9x50hY-ugK8N5L2LbuHE8vcEeEaC7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتو جدید ممد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78213" target="_blank">📅 19:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78212">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk-0fWOBuGnHT9Ees-bFfLWDBHpZrvSPBvS7J-uqDIjFxkrTpr7GwpcFZJ1Cxl-q-ekMHBoYwJ6FkfYZAH1wnu8VyFNDSgUoMxzHAVGi2-pprh7PQpsUj1VATEoaF3H7m-lzQnrMVPo3aRMHXKca7j70FdRlsVQ05U1-Qv-5jrC6ph9v15dJtvehWUiBjoGMYqb84NqIFxIqyefm1h_nzguryGgX2K13cJTSvQysV3gghmYFlsNea8KFYQn6ygheCX38OkRDsqBrOO_zmiBUah5GP534sS6YcnYJFDiVTMCAi3JQU2A159Yx5ARmFp_0WF5A8v2G6Q9eVts2mGWxpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری عماد قویدل برای پوری
@FunHipHop
| Behi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78212" target="_blank">📅 19:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFPjJK2jSFC07na9R6Ni8irxCZg2oyzatipWQUJcOsh1AfJoZ9D6zkHKpt8RaZekN1kJxk0WeMXXF5_pC6zsptoV8-dWBqyt0aqcQH1BCsSTOhY6Qt_HyJAZTlqYQWLIGWUFhOe5e8l0MPngAcVe8-FvBm1KClIZsNgmooEvVGvhM6sADb3Q2UxeubG9anka9b-6NLe19LAAhld3c4tA8INQ75Z1jHJjnB9kzFnxBok2Llgx2wtG8RiJ30KHISH7AolqUkp2LIkbqntSXWxLkzzXHQYYM_8Hx1Y6ZipUSG46cJ7bzXnY_atz7MWve28Md-x1DLp8abW6ixs7LZR3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 کامیون ایموجی خنده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78211" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78210" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78209">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPd-Mth1iiJMOLoDZhM6siqoA1X67a90AiC7oY6YPcMl6jlrRHy6pvMRg7eb6HQfT0x6TEZBv7TUXwbfspZitaXccuVee92RixuEURNgpO7L8pobRIaIkvegY4YrgXMQC_V7p-z39Ce4FBYgqOv2mNY5KSUxmtxkXrsGGo_hGvyyZ4ghC2KkvHsPORkf12RYjQYnJKBJSfqLH527BnolvOle9LjSl__XyZYUOQcPHTnEa4-xsDdafIAZrJ_2AFL04RLLOigtWXfyZMjPL9RguBpuEcm3v2IoWm841fs4DWAqEH8frQ2qB0tMxb_37Y-Hbzja7xxg2etHJ9WP5Ttr-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78209" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNX89-gCs1EwlcSEtKaZI8MYiBmeki3n5d4aBhPUEPvSu2MwelGd8CFt9gHE0rBHHLBKzR6lZUXBqb2AWllQkz6RO05R6kovlz0s47n6X6z9DljwPvrwucpLZAbwW9ngH5I8QY_qUzbSQUPJwgQHiCPeakp5BeAf9CxeXhWsWIJAtcDWsCahTHhjFvtJEJWERSFxfP1mnvXcv_fwpDmCazByGKgnsZTOfJimnhRbZTyxbgHA0I0Wmd0S8BjzgDaqE55eserG6tByTOvfuzyk8BrGMDCeL1UFwYuZbhzQPFzqYDpBopio5ig3T0O7vGwh2_wxp6H9Qb-bxEkKegedXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ساله ترجیح دادم پول سیگار
بشه غذا واسه حیوونای تو خیابون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78208" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78207" target="_blank">📅 18:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaClH-G6or3I4eFsQoXpOIez7zat_fF09GVI2IvsnQu-U9G1JpReqN-kKXRb4nglW4nIiuGRz1PXrwzRC6WjyJJNkK03M_UzRh05I4wCJCN9bh2TMKoSh7A9hStnRXx4rZqLlCMonJywQum56YJBln1T-VyB5CKr0prHv4DLmQUxDScDB_5HHIalKT8btjhtx5Y1V0BgrHXMoXUTGVAl48VdFmfLqMvct9J_oSPSgnGZr2sxU2Ee3X8Z_WBxJBgqEjtEuAa_titFKIYipHiTbbP4dM_FxMLaE9nDgxdBoGnfZ5J0rrgGvp-SFBLx6TtJtx4kT606YVl24saFen6vPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب جام‌جهانی
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78206" target="_blank">📅 18:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78205">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLk</strong></div>
<div class="tg-text">بچه بودم دوست داشتم مثل رونالدو بازی کنم،
الان رونالدو مثل من بازی می‌کنه</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78205" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78204">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBTEb2oFqOuSXHJVJ-UJQdBGXVSLh373Z16UMUcCHFMjDyYvAUTH2SBhoCC13zKeDEwMLE7hoGQ6O3-hnDu_IA7_5f-27BemZrvcN5--3hA2_8i6d9Ymlj2Rh_JbW3fUh525i7mTsa2xm3u16Klx6d8JIftmPQR6mKER7s3WOTXhVXBial4FnEACbU8onrm6Rxcn578kNWTTuHdwo7lsrPoOZs809j21E1v43h9kTDOqYX7ArYrMF7SXh5Sh6sA4YJPMyCN5w3zLYR-AV1E_ht230wSHsQvXJMYD5eaKOcSO6B8La2YKWbcDppbSovZMIDKByIt92Wz1MeP4xDE_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای تاپ دنیا توی اولین بازیشون درخشیدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78201" target="_blank">📅 17:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a981aHzPhmOEPT8iVb5ZphHp7Ve3ElnddBuxcmFlMSL61QYdzqClR_BjRUsKDS38uf9ZDtO2bn3-Q4LynlafEkg1duNpUdp75M55YujrnyVU9T_o4r8HJrh245_5F7orPCz-60BacUnUZ-vW6Mu_e38ccVzQhWULgoaY2AUP-yQIkkORBCAoEm4x59eoLEeeG8yGIIz8zE1TVdiSCoj_TCviyKrB18cFSMIbjy01WhZy91vyzLYIFuELzF-P5fGJiec_X-h8NoM4bEtzBPTUtJOivSRBMNp8wnX8f8TE0jI4jwyQWJlieoRxU-C_x-qi_9I7xJh41DwK0Jo_Lv7L5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم سرپا ریلیز شد   YouTube  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxwfaN3FD976rRuqJ-PTY2BTUNjBlH2OMNaiPttVTuwBclXeMYgxGDXL1Ns1x4s1FAu3Y8OQPJZKWoAD1cR0Y5wE9gmrlKGrS_xHlirqXlRlCW-6KZN26WLGcn32q-Jo7IN5PrV-nZRfgFbxRVDRCkpko5G7zQGE8coL9WvmqMrLxIuQKQKgPdpLJw9qKqHxN_AH8w5HTzbl2sdfWUSvL_21Fhv1CfBO2Jf7LrJFPzFgSwG260CpsFM5OSOmrYmchvOZRhe08x8K-aqCkKeXOzyY1N9WYEUBtUFzRFnP5UHingYHFj_m-pD-2Kdc3PSpPsQEbS_wd-M_FqfsDz1Cnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم
سرپا
ریلیز شد
YouTube
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78199" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78198">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وقتی مردم ایران صدای بمب‌ها را نمی‌شنوند، ناراحت می‌شوند؛ آن‌ها می‌خواهند همچنان صدای بمب‌ها را بشنوند. چون آن‌ها می‌خواهند آزاد شوند.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78198" target="_blank">📅 17:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ: فقط مردمان دیوانه میگویند کشورم را بمباران کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78197" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAj2sLwwG_9tD7HPMgBtYtP7oZcj5j10WYNc1tckKGGrzCrIEr0GvQgjy7uQvghT0pLy5yDvLGMF5yDvB4Ke7rGrBPM0VE59Cr1EVKZvUMbgldsTbOOUcY7prNwaSNGIX2FZ-NkhWoFC9p43268Wv-jx9r0lSwkk2SKKqwkeThDVD4VQT321F3Ojjll0UpTtJ4Ut_r4XA989r8Jayp4CX5YOUQJyoPbwp5lR_PAGVRtDBYccYqlxDTPZzoWjalZJ9bNZUs16EUqf2wN9-1rk_SxyWxQSbdFpSo0mwSjTh2lbL1I1Z0MqoMIfZD8_wkfQdoK8FBKzXeyrjwOvOAbVjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78196" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iF3m-TQKxBOzz66tjgvTQc2EUChDISKfNY8C1EZcZevC9CQbevZq2vWhgmREv8xWpbxyBFDJqR9J17tW8-WAavJxNyeJh1x9-aCHbCUpsuqsMVBB5ts3feLqy8JqADn0Sxy6rhQfzJWyxnge4isy36NzqZxwvzaSXQnLpe2hCieE7nm5ptTU2v8cfMfDAExCSDKEq0jQBWSh2PbSjYnqP2xQGzmG3vPhxeRMGpJBNGBbnUKqhx5W1_zY1EkWX2jIdi5UyNiWiIeORZLraMhBXzBlte5zXcEWxd4cvBounAJioA-ddczSdplPu6r5Altdd-b4vmEu0Gusngqn4IHlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سنت خجالت بکش کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78195" target="_blank">📅 16:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78194">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پوری میخوام برم بیرون، سریع تر ترکو ریلیز کن یکم بخندم برم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78194" target="_blank">📅 15:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromuıǝssoɥ pɐɯɯɐɥoW</strong></div>
<div class="tg-text">مهدی واقعا افغانیه؟ آگه آره که کیرم دهن صاحب کانال که یه سگ افغان و ادمین کرده</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78193" target="_blank">📅 15:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ef661660.mp4?token=cna5J3GCz3cSloilbgKTXuGhN8Ph_2W4ua5IpPD0M3idbOMkfa1dI6sf84NKvHMXYLB2ZmO1Be0R-qBOMMAQEg21lF1-juevM3YbJoKv10uMjSwgC4i4uBlYHQtsfN8n9k1LBiVKXfE-L0lWTH99xP-wDZXeMLxfJXyrrFQ6XPkFctKdbq8Hjz6Z0H21suZfKdB8wBXdt-EH4gz7dKdCe4SyXyiedNUHOXuVD273PdNHhABD31mbLuP__kiOWvT4iHERVickkpeLJXZ6vYxsIlk1aAwqfDe9NF2drNJfDZuSTlm2VkRWAo7z-nRIF9IWS8HW2zB2_E8gETgPOca1HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ef661660.mp4?token=cna5J3GCz3cSloilbgKTXuGhN8Ph_2W4ua5IpPD0M3idbOMkfa1dI6sf84NKvHMXYLB2ZmO1Be0R-qBOMMAQEg21lF1-juevM3YbJoKv10uMjSwgC4i4uBlYHQtsfN8n9k1LBiVKXfE-L0lWTH99xP-wDZXeMLxfJXyrrFQ6XPkFctKdbq8Hjz6Z0H21suZfKdB8wBXdt-EH4gz7dKdCe4SyXyiedNUHOXuVD273PdNHhABD31mbLuP__kiOWvT4iHERVickkpeLJXZ6vYxsIlk1aAwqfDe9NF2drNJfDZuSTlm2VkRWAo7z-nRIF9IWS8HW2zB2_E8gETgPOca1HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچ یک کانادا و حومه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78192" target="_blank">📅 15:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">راستی محرمه، پرچم عوض شد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78191" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انقد همه پرچم گذاشتن جلو اسمشون منم تصمیم گرفتم بزارم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78190" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
