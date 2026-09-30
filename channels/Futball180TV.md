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
<img src="https://cdn5.telesco.pe/file/JkBV9mzjV0n9C3fXO9niaoF-EThvUJAf-izogvPo62qWN5ACUwmvBQruXYpdaXvU2uWGQWjZD9_-l1GqLP6ULrwej-KlEmAC9UPWWtB32t-HhSvrm7klRVE8ZVo3Svi5UFzUxioQqiWcfaP7pVYAiKPYVQJS1NUDzB16TpoW4t-X0yPHSmN0CLfucMUz5SvV6fR0kyA4D9SmOuzuqPLa7I20jmx0XQP4CDpGybqKns4kHDbK_AR2xW0ANSsBGRpBUDXq645M2Setl_KAijGaoErbpHX0LXuD6yUpWdyUGGxptAgW2PCSZ_BPPl_0x_qCkza3qpQlnCFCigQEmgK19Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 395K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 00:24:30</div>
<hr>

<div class="tg-post" id="msg-107571">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db10a352e4.mp4?token=vdnb7zDUOaykO9CNqWHaEBO0182TfhmCZFV9lT9LmvhI3Kt8Wa4XpXEQhR_wOhgD47mIhaopIoCfs2fW8ZNoF95CuCSddpDxxRb8w4m5poiEtuFpQVs17BqFYExxhfgKi0w5-STMXuHt8TwmuoI2BIq5gk4knJquF2i7aSUkjQUcBw6cYOGOzwUblL7gL_zZba5MF7nv6ahFUSAbuDSqz13KqZcYnUw88d7PcNuLerAuwBobU-gDypSqTBsxB15R_ZCG9HVVPpOkl-WjrgUGtoBdSZ8Z4d8LtdkwzwWVANXWiDrpgrguWAFOJmWmBe5tIqBInpx3byPRQT2QNK5zxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db10a352e4.mp4?token=vdnb7zDUOaykO9CNqWHaEBO0182TfhmCZFV9lT9LmvhI3Kt8Wa4XpXEQhR_wOhgD47mIhaopIoCfs2fW8ZNoF95CuCSddpDxxRb8w4m5poiEtuFpQVs17BqFYExxhfgKi0w5-STMXuHt8TwmuoI2BIq5gk4knJquF2i7aSUkjQUcBw6cYOGOzwUblL7gL_zZba5MF7nv6ahFUSAbuDSqz13KqZcYnUw88d7PcNuLerAuwBobU-gDypSqTBsxB15R_ZCG9HVVPpOkl-WjrgUGtoBdSZ8Z4d8LtdkwzwWVANXWiDrpgrguWAFOJmWmBe5tIqBInpx3byPRQT2QNK5zxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
آهنگ جدید محمدرضا گلزار منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/Futball180TV/107571" target="_blank">📅 00:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107570">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8hiCoUOdxAeQ01I40qLHBdvWMAl7-30raDhymzkcOXuDnGC6NMBTnmNbq-dhaORwCDlLK-i5LOUmI4jZnjy8evGTO29CR4Ax5DjxMIHErjYG0Mu9vJZIhSROvyKMcvKoXH44ElBOY7FvxoF0XxPyrMKQRxNuKjCxN3StZfdxo0A6SLBYgldi9ilZ6cHrGqCvOnq2kdLtbfCYx1AGhAoyiZ_b1wzWSbE72whAZEqSy3wUAeketDeHpnZHiO_Vbbqen-cI5bSWl0EYVQqP-y5oNGO0ec1RA5lJ-ukb_vFEv3KGJkCE6P12EEj03nMezlKooBfFF7PbEm-sjxExmj0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
#فوری از آبولا پرتغال: تا زمان حضور ژسوس روی نیمکت، بازگشت رونالدو به تیم‌ملی غیرممکنه و باید بزودی شاهد مراسم خداحافظی برای این اسطوره باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/107570" target="_blank">📅 23:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107569">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba-q87WCTd-lahFPW1xPnlDNqW4IkIwRM-_8XGgZ8_haA_qUl8QwJWUz__YB7_y9MuipjP8LHEydr_KJOGyjR2ZwKKJmo3YkED0bRwir2ONmyt9p7r-5GNKF3jM4MgWhUXzay9e1qK2bgnKzBonpYm-x_epAn--yS3T8jCa3aXmovaPUTZd9FEKRK9hZzxOd_kRdhlk77o7KoU31482HdBpU200vk4Ujd7ifyuucw-6VFEtXEBtFCHCAJLFoUiQdnlTGTQNofeG7RN4VBWTU5TLHvSILrhGVhYXRp3fULDpimxcSSiyyG1c3Xq5OA2aTxYFCfk-f8TFR899_zMdSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
امیر قلعه‌نویی: اشتباهات اخیر خود را میپذیرم اما از مردم میخواهم فرصت بدهند و مطمئن باشید که تیم‌ملی را دوباره پرقدرت خواهم ساخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/107569" target="_blank">📅 23:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107568">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBOQMgSrI1F1XN3CB0imc2ZLju_tt2gJFLvYbXgwkrTnhR7y5H3EDUOOTpYn5GzJm_3dh2JNB4ZlphqIU3VuHr-d0HYfTZOrUsFq6xeZ_v8ac91hPjygDyTkJ-1DMZngSXvjO1dIms2OLsyOn4BcgA8GSBB9-eMcJSv969hFoSzMtyKY-jOKRzbsWtAGfgblu2eUDXKPIPcYa_7SYNAff5H2vZAIta375kMFlqcvsRV1XKOMTvcdCLGO74vKOrgiDxTiByvX634Yi5RQYkht6Uu24cSm72OOOMRnUG1yxhYaIi7FqCBf5WCnFGGveNjOKv98TISECbgYKL8AvA4-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
#فوری از آبولا پرتغال: تا زمان حضور ژسوس روی نیمکت، بازگشت رونالدو به تیم‌ملی غیرممکنه و باید بزودی شاهد مراسم خداحافظی برای این اسطوره باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107568" target="_blank">📅 22:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107567">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O202PReY2bOzW3RQZSpj3xoP8ArCoIZ_qkX_7zWonqLWYPgkmWedwX66bzDCOFk7dXPyoYMvmF3ujdEvwtMpYygEDNssR9afoZu8G1fKDVUOcV6R1r7RdcU3KTsfl_COhlhTwkVO7_8AA6n7l4jnphCxtd5BifCrq_n0KGRyBazOGEpqq-Cz7D7b5xYldPyihvvPyzu-hP0kwaIS_ZMPEyO1bNF1n6nVw1wFrTH3mExZA7HSmBwlSBd1xIG-axkuJ1SjDGa5aGlkOELz1HcjoKJhe1iSXTmVpUtXZ2AB0AYOfR5Dm7bPgzaa31EIJAA2rsmA4WKwxUC-V3LhBv7eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💣
رونالدو اعلام کرد که کمپ تیم ملی پرتغال رو ترک کرده:  بعد از کنفرانس مطبوعاتی سرمربی تیم ملی و متعاقب گفتگو با رئیس فدراسیون فوتبال پرتغال، تصمیم گرفتم کمپ تمرینی تیم ملی رو ترک کنم.  در زمان مقتضی، حقیقت رو درباره دلایلی که منجر به جدایی من از تیم ملی…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107567" target="_blank">📅 22:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107566">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuadZvIyLhanzlTjLsDQITvasQZbpdNHssRyYwzhocXlIveW9qOqajLMRtMK2qzJ2JOn9sWDk_SJBqAnA_iHl9yxDN1N36DJnTHEjFDYfbOhpf4FRU4V3MWX0ZZ5FRNOfcwYhBSWzeXHEQy5IjtFgAST4iJoQUzKP3kFOPuGJLuPxfC47ZoNRUGvZeR7wPNSHvcxiapgzJ4mLVNe9VsPudEj5173_0rwMQ8GCSeEITSRc6iIpw5x91Yzah0T96FHyusxpTqK2udbRqBWx1xahjX0RZpqCQKNJT1lBAhbxU11nAmTCEYFl6AmfIZ1uqy0BzQ5JJnaGdytGnfyWsMPhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💣
رونالدو اعلام کرد که کمپ تیم ملی پرتغال رو ترک کرده:
بعد از کنفرانس مطبوعاتی سرمربی تیم ملی و متعاقب گفتگو با رئیس فدراسیون فوتبال پرتغال، تصمیم گرفتم کمپ تمرینی تیم ملی رو ترک کنم.
در زمان مقتضی، حقیقت رو درباره دلایلی که منجر به جدایی من از تیم ملی شد، تیمی که همیشه خودم رو وقف اون کرده بودم به همه مردم پرتغال خواهم گفت.
اکنون زمان اینه که برای پرتغال و تمام هم‌تیمی‌هام آرزوی موفقیت کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107566" target="_blank">📅 22:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107565">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpu7PZZA-vxxB0Z63gf8AkTtEqtE3BbvlYJltWg0Ei6vWpxnF9M9QISzM5MBt_aV9xh4IcJuNVhTb8AtlndhGrJd7FPcpAExvFdD0mCBcn0mxW3w4shSgGDNUlNOX_rB2t9TQeZ2rdyiX8H_xjeTnNmfB7mef3ueQlzklXdz6T2IM6rQeFQ7Cfom80-uHi9xZ7eOnRH0hZdl1QLRbBOqyDRHFPq166b02-Z2PukJNjDhfJ3gpd0em2kKRiWENzh5W86Q_kIuWaJ6KTfWOUhxcD8wwey4aXE-O2QAUO1ITewPnrUoSUZvBGqgzqHka_Kmbo1ONdLkdpy01i998uP4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
فرانس فوتبال اعلام کرد که عملکرد ابتدای این فصل در ارزیابی توپ طلا  محاسبه نخواهد شد:
🔸
دوره ارزیابی رسمی از 3 آگوست 2025 تا 19 جولای 2026 است.
🔻
هرگونه عملکردی پس از 19 جولای 2026 خارج از دوره رای‌گیری خواهد بود و برای ۲۰۲۷ اثر گذار است
👀
به عبارتی درخشش‌های ابتدای فصل یامال و هری‌کین و ... تاثیری در نتایج امسال نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107565" target="_blank">📅 21:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107564">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcE84GyTGh7bWF_nESBFBbrnnNnCZhwH-I5q_K33ngxkbhZu0lCKSGzkOqZ1AcHYLy-6TNagbSIHDsD3GsW2GWxVa79UITm5z9WWOlp95HTvkoan5xzZ9csn9d4-qERBf61eeX_kk97Bt5jwyErq_uW36z1vtf_T5ZtcdgFWvG--ttR76z4gvaylr3K49uSgLavV6LJq1Dl-THsUMHMnOYM6XIQvzYzqOz2AJt0O5zMbWezN15dgatH0uGBJs6opJuFq7GAyemulaf2X8fsoDy-ws36xQmZaReVsEFT8_ToW4yEW_OegyC4ryFplpr15YA5bp2SlKkvdRPCf3WcQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
ژرژ ژسوس سرمربی پرتغال: رونالدو در بازی فرداشب مقابل دانمارک بازی نخواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107564" target="_blank">📅 21:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107563">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81558f0c75.mp4?token=rA5iwnjo-Uvb1JQA7wC4Z2fvKPldU3RsIRs9_RI63tTcYMCRMgPzRIowhNarq728tJNc2DRd6wcKiCiLGfOPRQIl2-MTsJjPcpwTxL5nywIBuvWQwIiWFKkSWnOUfAVBjuEsfqa-M0ZbQDOuP91usfACQhgIV4fRdnb9FsbYw1C9fS2DSowpf4X52h9UMV9BLrmMTXNTiuFaAkTWLqHr3dglDZvyYg1D0As4A09dvB-03eSemijsPN0iFWW_cq0n5F2Q-wx6sSnwxbzeXCpn4Up8vvenWApXIHbfYSbwLY0wvp5Sk8mTTdL3Nq_RtoVa7aeYkoWWUupOGQPzxGZh0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81558f0c75.mp4?token=rA5iwnjo-Uvb1JQA7wC4Z2fvKPldU3RsIRs9_RI63tTcYMCRMgPzRIowhNarq728tJNc2DRd6wcKiCiLGfOPRQIl2-MTsJjPcpwTxL5nywIBuvWQwIiWFKkSWnOUfAVBjuEsfqa-M0ZbQDOuP91usfACQhgIV4fRdnb9FsbYw1C9fS2DSowpf4X52h9UMV9BLrmMTXNTiuFaAkTWLqHr3dglDZvyYg1D0As4A09dvB-03eSemijsPN0iFWW_cq0n5F2Q-wx6sSnwxbzeXCpn4Up8vvenWApXIHbfYSbwLY0wvp5Sk8mTTdL3Nq_RtoVa7aeYkoWWUupOGQPzxGZh0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رنگ عوض کردن سردار آزمون؛ حین جام‌جهانی خایه‌مالی عادل رو می‌کرد و الان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107563" target="_blank">📅 20:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107562">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a3b8520f3.mp4?token=G27Y32x6QbcvqT-SjyZf86ZBAIi5bKCfUYUly5ghsvX_Tyi4Hu43GC4kECWrc8rEXEvjeyAplQFEA7sK9kwFrloezNvfk1y5-TVZLe7IsY9NBKAj9NQhHNLMUhPJj3um5twFBzm7qrXfa30yXnASRMUaxtWYYDUhD9J6BLG2-vNG04422fjYl81PdpsLoM0aSDSJB0yYd444x1Mtjv_prI0hDi01hyP46gTatQyD7dyeWPKj7b6Nm8D-9ctDMH82SZyHnsWYXLvVSLVdvGECIbBQoW_30cGYm1PqDqhF2MzT2P7P_4uhJ2xLbZVMYVLluCkuY-dtXj4fKJ2MS8ZTPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a3b8520f3.mp4?token=G27Y32x6QbcvqT-SjyZf86ZBAIi5bKCfUYUly5ghsvX_Tyi4Hu43GC4kECWrc8rEXEvjeyAplQFEA7sK9kwFrloezNvfk1y5-TVZLe7IsY9NBKAj9NQhHNLMUhPJj3um5twFBzm7qrXfa30yXnASRMUaxtWYYDUhD9J6BLG2-vNG04422fjYl81PdpsLoM0aSDSJB0yYd444x1Mtjv_prI0hDi01hyP46gTatQyD7dyeWPKj7b6Nm8D-9ctDMH82SZyHnsWYXLvVSLVdvGECIbBQoW_30cGYm1PqDqhF2MzT2P7P_4uhJ2xLbZVMYVLluCkuY-dtXj4fKJ2MS8ZTPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیس ژوله به قائدی و قیاسی؛ ژوله وسط برنامه زنگ زد به قیاسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107562" target="_blank">📅 19:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107561">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvaI2WKINaW2L4un51WnMaBUA_2bn8duQPyWYEy20K6H2Ay_tBDv_ip5YefpJ8Q-zbSDh050-KxvOYHiUneDl8oOVE8ci5hm4gBFBGxj-JZTuGRChE_EYQWf9VQhdEbNO8nMLZ7D5zq-xAIsfE0rZxLwrzNczkzSrNMifiFOwyOF15I-jumNNel8lGw6t0LmYsld2VWQSwgaBXNsJdR2B56upIxjI00FFeorUx_O_SS9TXN_jhhDrgXsma1APBRL7UbiyD0_dmz7fv_A4Yv3lIK8Cz4gLmpc8KBSzUmOpMWhXN440rqaA1uWsWvN9w-zpYvzqijVEs1rOF3REmpKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
ژرژ ژسوس سرمربی پرتغال: رونالدو در بازی فرداشب مقابل دانمارک بازی نخواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107561" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107560">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d3104ad6.mp4?token=urHcw09aZGjwONGeLRcttK-qs3k5qwTWnIAens8qQrTG4vivf9oNbRuh8F_u69U6cav1lV-Nis-TQZZm5rTkGhO2jbPTEPxhBHDKvg-OGVLtSODUqWdA2bQwxBHTSHhJ972QdEMwUIWe4zFmB1cAu7PFO7OD7mpNXGgd3xm-ir1_asPObEtNHFK__E-7eBhEQ_ycPyZRbv6rgn8RliEeucjD4zvLZ_m4_1VFPRxDH-sCmC8JMfecaMOai6RMgmsuZCHvWHEbQiUers66OpSYXUIfWs_Dsy5nHlLTbVWXZz_tdOqluZ2BOPKTdepBKCfc2AmejYAEK7m_IcC1WQgSiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d3104ad6.mp4?token=urHcw09aZGjwONGeLRcttK-qs3k5qwTWnIAens8qQrTG4vivf9oNbRuh8F_u69U6cav1lV-Nis-TQZZm5rTkGhO2jbPTEPxhBHDKvg-OGVLtSODUqWdA2bQwxBHTSHhJ972QdEMwUIWe4zFmB1cAu7PFO7OD7mpNXGgd3xm-ir1_asPObEtNHFK__E-7eBhEQ_ycPyZRbv6rgn8RliEeucjD4zvLZ_m4_1VFPRxDH-sCmC8JMfecaMOai6RMgmsuZCHvWHEbQiUers66OpSYXUIfWs_Dsy5nHlLTbVWXZz_tdOqluZ2BOPKTdepBKCfc2AmejYAEK7m_IcC1WQgSiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های ژوله‌درباره جنجالی هوش‌مصنوعی در ارتباط با سربازی علیرضا بیرانوند
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107560" target="_blank">📅 19:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107559">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e7cfe3bf.mp4?token=J5O2KgHwk_UJdfQB-y3oI0YhV25si0xnMbUt5leguxBd6isZQUlyXdDXRfKhPeQXFHqJJZ-J7o37NoCO0kalPecpIv6SBWqBtkpyn_zJx9Ow2yw32p_-0nrc5sSWUIpdCWMJQjfbxINTmGHtm3VNie0GOyY9DRGwe97ExwTmhDSn2M84u6NFeOh1UAwF254AvXj4g3rSqPYJ5jSOpylh5NM4w9m0SbF9LUT9dMMlztf12gxWWIrnjZVx7wa58iqeZbIlDeCe9mN6FVuXJQXuynIZL05Io1XOu53Z7t8AtCut0FyJrVfoHeDKzHlI5N5Ng1RWyM4kq7ImTpFMAk4qUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e7cfe3bf.mp4?token=J5O2KgHwk_UJdfQB-y3oI0YhV25si0xnMbUt5leguxBd6isZQUlyXdDXRfKhPeQXFHqJJZ-J7o37NoCO0kalPecpIv6SBWqBtkpyn_zJx9Ow2yw32p_-0nrc5sSWUIpdCWMJQjfbxINTmGHtm3VNie0GOyY9DRGwe97ExwTmhDSn2M84u6NFeOh1UAwF254AvXj4g3rSqPYJ5jSOpylh5NM4w9m0SbF9LUT9dMMlztf12gxWWIrnjZVx7wa58iqeZbIlDeCe9mN6FVuXJQXuynIZL05Io1XOu53Z7t8AtCut0FyJrVfoHeDKzHlI5N5Ng1RWyM4kq7ImTpFMAk4qUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
شهریار مغانلو بازیکن تراکتور: زندگی کردن خیلی سخته؛ مردم نمی‌تونن خرید کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107559" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107558">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107558" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107558" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107557">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugEbri3wXs9opFf_32OLeF7cLtciq-7ZBuVFWYYz6tBSWt7lCTq36rJ9wwfa5PXSBmlxt5tKiWIu8wkTQQVb1bbpu75QYBKCn5nByBaosQCswCgW5m1CBhMhI_MsC10J66MVb6RRSYG-A8CgnE9HSFwyxNBGLcpe_bSZlO-ondP6w_Z53TpViSCDKgSOOtFr8_Zlp5aMTdwqz0T2PmRPJoenW9AjsTEoVYhJKAu89iq2cNgUR3lz4uBaeDk2CMzlwSE90CXc90rZsxYf0YUTLLWqZ46ImFdgZonk8sG-WSS8-8fa3oP4qifNGsR4GfAemm1eTDDY-KfKgluiJ9bqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107557" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107556">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
آخرین وضعیت ورزشگاه مخروبه آزادی تهران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107556" target="_blank">📅 17:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107555">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2b8aa84ba.mp4?token=LtmYLoDFXnFfNyN9unfkp4uiG5NzUz2dscn6v1qk-WXIKA7ZFDiqrcHLzEcqqQvYFJUEZ8luENMmWHqRTBF04rQ_be7vYaCtE0ur_Y8Wn3ylHV5vN07BBTdRdWOrTjn_vLBseLLqxNMiKS-f54dL8ndQxdcUdHUGLCvUq7ny1lY1vJ6pB0bBfzGo9Sx3hdkUc6itLGNZgf9g1vRfPwm37JAyQvbFeINmg8ohiBYkjnV0RI-cV3S1l0bVeIA6c6o1yRkGxWFMLLBgZt6Dm1-MSE1tZtsN9mB7oeGJergbJnZD7ZOtChxWpEOp0CctwzH24rfKLVmPH_DoIEWTJ_Kf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2b8aa84ba.mp4?token=LtmYLoDFXnFfNyN9unfkp4uiG5NzUz2dscn6v1qk-WXIKA7ZFDiqrcHLzEcqqQvYFJUEZ8luENMmWHqRTBF04rQ_be7vYaCtE0ur_Y8Wn3ylHV5vN07BBTdRdWOrTjn_vLBseLLqxNMiKS-f54dL8ndQxdcUdHUGLCvUq7ny1lY1vJ6pB0bBfzGo9Sx3hdkUc6itLGNZgf9g1vRfPwm37JAyQvbFeINmg8ohiBYkjnV0RI-cV3S1l0bVeIA6c6o1yRkGxWFMLLBgZt6Dm1-MSE1tZtsN9mB7oeGJergbJnZD7ZOtChxWpEOp0CctwzH24rfKLVmPH_DoIEWTJ_Kf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دیس‌سنگین ژوله به حرکت کنعانی‌زادگان روی گردن عارف‌آقاسی در بازی دربی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107555" target="_blank">📅 17:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107554">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c4e91ce5.mp4?token=Bh9gt6kUfnh-El4rSsB0U_NvvvdpNqjz6uHMpLKXlw9L_HkcEgLJ9uy8WyLjO6It1KaVC4eA0tcPTUl7-uvYvPw_ar7pV_BhPpIYUZdZ0JWts6ElMTo6sGlnqoB2k-6T-DobKlug1qnI570lRdy78hC1UdvmoWXKprzI05e2UF3vIajo88D90TFv6BOqt2-02mYfAmgf5cSDaLZ1png5UZMSJ919Xmn3I7fmReMO64pWeckfdNn0oiUB6IeaPopF1-3vYz2SyG7XE9hry7bwtpg5Fm0U55frdiztCSw085QfDjYiC2rDTdeUXkvbqqhr0H77jckSZepGp-zR-QRlUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c4e91ce5.mp4?token=Bh9gt6kUfnh-El4rSsB0U_NvvvdpNqjz6uHMpLKXlw9L_HkcEgLJ9uy8WyLjO6It1KaVC4eA0tcPTUl7-uvYvPw_ar7pV_BhPpIYUZdZ0JWts6ElMTo6sGlnqoB2k-6T-DobKlug1qnI570lRdy78hC1UdvmoWXKprzI05e2UF3vIajo88D90TFv6BOqt2-02mYfAmgf5cSDaLZ1png5UZMSJ919Xmn3I7fmReMO64pWeckfdNn0oiUB6IeaPopF1-3vYz2SyG7XE9hry7bwtpg5Fm0U55frdiztCSw085QfDjYiC2rDTdeUXkvbqqhr0H77jckSZepGp-zR-QRlUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
واکنش‌ ابوطالب به صحبت‌های مسخره حسین عبدی پس از شکست ایران مقابل کره‌شمالی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107554" target="_blank">📅 16:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107553">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d381cb7a98.mp4?token=Ew5VT77OUNgncY5OHEmTJvK-ykLKRwzsS4IrjLnC0DFoV1vBKqUcvk3TKN3Q_RKE4MdJmXESVo0CJ8COTzbVOSKJ4vbFLssDdVwcmn_WEUgAGmCF3gLQWUNBwkrb35qWUbgHE4UQfNG0ovFtofQYwpv0GZSzEGV5I3MJCJ6ktdboKXIkz0_FHbSI4dnEVpo_DT9y4bPzbLX88f00_WeZpqSAmxia0Q3HOSTkdWPmhOYm54BsdH2mpOIRF7uq0BVxh1D5-lm4ApgtHbK01to587S0dHxqyvqfVxf_cB7P1a-e7b2Twf9FO5PI4WbTjqCXJVjm3WTLPCZYxGVzda8BUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d381cb7a98.mp4?token=Ew5VT77OUNgncY5OHEmTJvK-ykLKRwzsS4IrjLnC0DFoV1vBKqUcvk3TKN3Q_RKE4MdJmXESVo0CJ8COTzbVOSKJ4vbFLssDdVwcmn_WEUgAGmCF3gLQWUNBwkrb35qWUbgHE4UQfNG0ovFtofQYwpv0GZSzEGV5I3MJCJ6ktdboKXIkz0_FHbSI4dnEVpo_DT9y4bPzbLX88f00_WeZpqSAmxia0Q3HOSTkdWPmhOYm54BsdH2mpOIRF7uq0BVxh1D5-lm4ApgtHbK01to587S0dHxqyvqfVxf_cB7P1a-e7b2Twf9FO5PI4WbTjqCXJVjm3WTLPCZYxGVzda8BUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
همسر بیژن مرتضوی خبر از بازگشت این شخص به ایران را دقایقی‌پیش اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107553" target="_blank">📅 16:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107552">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a63edbd38.mp4?token=mp21hRhfOFYgbXEzPOo1lfe9pcRncyMiOD4BoEwnFEOlWdYSapjzhbMzRkrsYlQFv8B54MCtFdgVRAOvvkr567uX_lGxGSN2iYPAx6t_If4y7UloDtIj_2ExOPOltdtKQu71QJSPhMfRImsn34tX_kt0g9PB3XgkE2KWdKO0aYYhXHWDGoHMFFiL7RMfid-grVHpx7ZFNehGBSY6QLP96eMnxvWr8LpPJJNvwVnmaRps8Hcxz_WnaumQjG918nftVJ1Sts7nv4n1yqG7K4R-LcQGDxPXpliQY1emgfMGQ97robykakTJ2fNwBiA0RDptZ5iJiW50qdwc8Coo2GwDhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a63edbd38.mp4?token=mp21hRhfOFYgbXEzPOo1lfe9pcRncyMiOD4BoEwnFEOlWdYSapjzhbMzRkrsYlQFv8B54MCtFdgVRAOvvkr567uX_lGxGSN2iYPAx6t_If4y7UloDtIj_2ExOPOltdtKQu71QJSPhMfRImsn34tX_kt0g9PB3XgkE2KWdKO0aYYhXHWDGoHMFFiL7RMfid-grVHpx7ZFNehGBSY6QLP96eMnxvWr8LpPJJNvwVnmaRps8Hcxz_WnaumQjG918nftVJ1Sts7nv4n1yqG7K4R-LcQGDxPXpliQY1emgfMGQ97robykakTJ2fNwBiA0RDptZ5iJiW50qdwc8Coo2GwDhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
قلعه‌نویی میدونه ترند چیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107552" target="_blank">📅 16:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107551">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlQA2MEE2TuktWdZ-T8fpvI0J_6UxWt4OKSpsDI_qbqY1_mNlvhTlqTuV60X3wxTgnTcGqTbwuPHnSvJULv1CJY5or5IIaeHVDXA7Qg9Z0aaSNCgnMS_Ivs3yrzfPLzlsbWQecOQ6lf1o6kUGLCAxJ9LOxgVVFnpOdyCmXIbGYxL5mbjhRQZZVAtyPNGiVntz1w9OnOaNI9RgskfqzVDtLVTo0QN0_ne3rP6fRIJ7a04QvKsx09-DYhnPvnhEaVSnRXshIpojRjCFAx6cu2WdJc8smIZYwBwtDwUuxenzTwZs16DWDhU0DpUkOZKTTe4z3RxPzf5vS1BAPsl0ot88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
⚽️
برای اولین بار از زمان رقابت‌های یورو 2008، کریستیانو رونالدو در تمام طول یک مسابقه، نیمکت نشین بود و حتی یک دقیقه هم برای پرتغال بازی نکرد.
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107551" target="_blank">📅 15:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107550">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0610e8bf78.mp4?token=W299f2woqk-JuW8xK-IWuez5PbcHpUwTDtFq_x-6sYrxu2603owmZF3nteJgIRK7mbYCwVw5npu8UGIdmAQQpK9XN873eSmlV5U1TGQqP2mkDLciOynWEJueYkwuwi5VOGMKzP0lZXzwd8FUzQqApVHYeU9iP5JDHlhch8wiop3SzM3uIeLyRBCQ6BLCOJUL0ivG_y15Lc5t4qq5BmyVbJhN0tsqv5tMS_2Qj_H5jQT9IlMnNawgSmV8HIFzAcNqEi4fSdBZ3qKD2f6OCOXTqsau2cf3hRtHCe7Yj_5_essrCE7pvPK7WpPF-GOpM0g9-XtqAr3TP4zqdTzonGptzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0610e8bf78.mp4?token=W299f2woqk-JuW8xK-IWuez5PbcHpUwTDtFq_x-6sYrxu2603owmZF3nteJgIRK7mbYCwVw5npu8UGIdmAQQpK9XN873eSmlV5U1TGQqP2mkDLciOynWEJueYkwuwi5VOGMKzP0lZXzwd8FUzQqApVHYeU9iP5JDHlhch8wiop3SzM3uIeLyRBCQ6BLCOJUL0ivG_y15Lc5t4qq5BmyVbJhN0tsqv5tMS_2Qj_H5jQT9IlMnNawgSmV8HIFzAcNqEi4fSdBZ3qKD2f6OCOXTqsau2cf3hRtHCe7Yj_5_essrCE7pvPK7WpPF-GOpM0g9-XtqAr3TP4zqdTzonGptzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
دیس امیرمهدی ژوله به جنجال خداداد عزیزی نسبت به پاهای پرانتزی امید عالیشاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107550" target="_blank">📅 15:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107549">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12598c8c6.mp4?token=o3o3lPKreoRlgn313s1JXWB06w1x9KwJZ6RCVqLrvQQPV0DTq_vMxbsqMnkzwQ-JeNjo_yr4zW3A9bjz6ThS-i4kLPFWTM-6piuEBSLqf5QjZB8hgGvjTaUwi_SL2BIsTMURFtPGE4JqIdBrhOvhYSz2fMJxbCXvKqMYgOqQcFYb6g_sbhvsZwLp_s30aAsufkEo71vCQm_jw-ClzexL3UkI3xtFyThm4QVRxKB6LTdhAkq5EcvhNyaiBJgrXOOnIpFMoHEXfaJuuFaVez-DmFb3wylW9hbZd2QAAV6x-LvSHy4_0gp3CgyM_I8rZ5vofWoR557Rfpz4M1xUyQ9OBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12598c8c6.mp4?token=o3o3lPKreoRlgn313s1JXWB06w1x9KwJZ6RCVqLrvQQPV0DTq_vMxbsqMnkzwQ-JeNjo_yr4zW3A9bjz6ThS-i4kLPFWTM-6piuEBSLqf5QjZB8hgGvjTaUwi_SL2BIsTMURFtPGE4JqIdBrhOvhYSz2fMJxbCXvKqMYgOqQcFYb6g_sbhvsZwLp_s30aAsufkEo71vCQm_jw-ClzexL3UkI3xtFyThm4QVRxKB6LTdhAkq5EcvhNyaiBJgrXOOnIpFMoHEXfaJuuFaVez-DmFb3wylW9hbZd2QAAV6x-LvSHy4_0gp3CgyM_I8rZ5vofWoR557Rfpz4M1xUyQ9OBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
جام جهانیه یا مسابقه‌ی انتخاب کراش جهانی؟ کنایه ابوطالب به لیست نفرات قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107549" target="_blank">📅 14:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107548">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c539f4e6f.mp4?token=FnNPJ0CEb9iIQRAEiC5o7qjUjt7SaBc8yrdN0ywrVB8h7CKFr-rGT6eFMlrwGRFxShzP-WoD5ysIgOCCX6W_iA0sjvi9SNF63sI9ie4ru83wARU0ma069du5nb8RNA10KeWGhGzg6-01wlPw2Uy6lsodwa2EXr9wIPlZIjnNqevIehOCkI4O-gQA8qlUvNVOGAJDyZ8MyKaKUx_yN2X1DVL8afrVBVKPl9O4Mb21DxTojsAps901tyWciJyL8NFtsbA-JUsQf87e5cJ7CtwIfmMV8M8M2oJuy8leWWHO1nr2qNtMB0AiSIpOq1bgepTbT6-WG-2rpRP7sZfcvpWzGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c539f4e6f.mp4?token=FnNPJ0CEb9iIQRAEiC5o7qjUjt7SaBc8yrdN0ywrVB8h7CKFr-rGT6eFMlrwGRFxShzP-WoD5ysIgOCCX6W_iA0sjvi9SNF63sI9ie4ru83wARU0ma069du5nb8RNA10KeWGhGzg6-01wlPw2Uy6lsodwa2EXr9wIPlZIjnNqevIehOCkI4O-gQA8qlUvNVOGAJDyZ8MyKaKUx_yN2X1DVL8afrVBVKPl9O4Mb21DxTojsAps901tyWciJyL8NFtsbA-JUsQf87e5cJ7CtwIfmMV8M8M2oJuy8leWWHO1nr2qNtMB0AiSIpOq1bgepTbT6-WG-2rpRP7sZfcvpWzGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
پاسخ ابوطالب به انتقادها از برنامه‌فان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107548" target="_blank">📅 14:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107547">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc4546c8d.mp4?token=BKMOXOQcmdpBAxN42gsWAUOUySCXbRHZpzxxe08Uo-y94-uXl2DFz0igQ6_UHxsF1PQHnjh7gI0Gnt9C8WlAIc-A5hlejheVCh32tywctQWusxpYQSf9aVFqynz-4RC_frIjQPUosWtGeSH2jaH0GCUf55P-KJWGPgbt_UQGkNxkHd3ysT6DhSdPjvvQlsqU-6jasFWRAeEQGSFWLEpZH1MOdkrOcJBDlIoYfIG3PbQQZWWA44uGhvROotG4R5AqAiMPzN1ru49oEwVOzeAp5yHqMPoO8AEjnauC18svrCzweVYy2vQM-R3Q71MRrjMMw5O2Xiu2hWNssPXr9Inhh038qTZMwf6pR4n8aIjZHOxnxZ1TANXSqZ3nH3UC_SaavDar2Kam9BHmn8PwDI0MnmdGeUDcuggKgye_M56F-2dkQDoERhpL-Kce3gDQG5XMzTKBraQ3o6lAL9mGcYvdDp61P3o92PDGm2FI3eEwbM-b58PtWG11xnfsnC5CP0ApHnUCtCeAz4Yu-1LI9D73_nb1OgPX3mdIW86_OO5A4eWaWhryzuhEozM7qkWAbUeTE6UIX5DgqBTgwfEGYcevi9euWGQEa5FEIlaWxlasafKrdVe5VrCRDbZ6KTg-3qwMvgm_jFqaORsljH6nJ_XDHWF59J2biUt_q2MpCRZPmgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc4546c8d.mp4?token=BKMOXOQcmdpBAxN42gsWAUOUySCXbRHZpzxxe08Uo-y94-uXl2DFz0igQ6_UHxsF1PQHnjh7gI0Gnt9C8WlAIc-A5hlejheVCh32tywctQWusxpYQSf9aVFqynz-4RC_frIjQPUosWtGeSH2jaH0GCUf55P-KJWGPgbt_UQGkNxkHd3ysT6DhSdPjvvQlsqU-6jasFWRAeEQGSFWLEpZH1MOdkrOcJBDlIoYfIG3PbQQZWWA44uGhvROotG4R5AqAiMPzN1ru49oEwVOzeAp5yHqMPoO8AEjnauC18svrCzweVYy2vQM-R3Q71MRrjMMw5O2Xiu2hWNssPXr9Inhh038qTZMwf6pR4n8aIjZHOxnxZ1TANXSqZ3nH3UC_SaavDar2Kam9BHmn8PwDI0MnmdGeUDcuggKgye_M56F-2dkQDoERhpL-Kce3gDQG5XMzTKBraQ3o6lAL9mGcYvdDp61P3o92PDGm2FI3eEwbM-b58PtWG11xnfsnC5CP0ApHnUCtCeAz4Yu-1LI9D73_nb1OgPX3mdIW86_OO5A4eWaWhryzuhEozM7qkWAbUeTE6UIX5DgqBTgwfEGYcevi9euWGQEa5FEIlaWxlasafKrdVe5VrCRDbZ6KTg-3qwMvgm_jFqaORsljH6nJ_XDHWF59J2biUt_q2MpCRZPmgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنالیز بازی انگلیس مقابل اسپانیا که حاوی نکات بسیار دیدنی برای علاقه‌مندان به فوتباله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107547" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107546">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
رونمایی فدراسیون از معیارهای تعیین رده‌بندی و قهرمان در صورت لغو فصل:
🔻
۱-در صورت برگزاری حداقل 75 درصد مسابقات رده بندی بر اساس جدول موجود.
🔻
۲- در صورت برگزاری کمتر از 75 درصد رده بندی بر اساس میانگین امتیاز در هر مسابقه.
🔻
۳- در صورت اختلاف فاحش تعداد بازی‌ها استفاده از میانگین امتیاز به همراه تفاضل گل و نتایج رودررو.
🔹
تبصره: سازمان لیگ می‌تواند با تصویب هیئت رئیسه روش عادلانه‌تری را جایگزین کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107546" target="_blank">📅 13:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107545">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95a2f6b70b.mp4?token=Gl43g-iu7I7EVZbEeewxHfKJ8d_30UYkSxf8Jxz4yfHrAJuz0pConFNEoCAi4pqVRjy_5BRpBZrKvpq4_BFMC5PCLMMR8JYGtNQCwoDBIfvv1MubcyEj2RnAU20BdJ_AsG2E1kt58SbUdJJk5giBt3lCYxhvxsaxmA9BAuDhZQYOhTH694440C75KfWBej5x1ZZC-QgmjGPKC_6BMIUTIPmXtunHeNQybDPYiI18Kz8D0o3q_iCkeLn0ei3ncU_MVMD2Te02IcPq_hcjE97HEH0BAAjVZcEWBAo07eMUt3YWDgMqWnuGSgaylWOmvZZ6FAVwjJl4SDEaKqPkxQ8ZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95a2f6b70b.mp4?token=Gl43g-iu7I7EVZbEeewxHfKJ8d_30UYkSxf8Jxz4yfHrAJuz0pConFNEoCAi4pqVRjy_5BRpBZrKvpq4_BFMC5PCLMMR8JYGtNQCwoDBIfvv1MubcyEj2RnAU20BdJ_AsG2E1kt58SbUdJJk5giBt3lCYxhvxsaxmA9BAuDhZQYOhTH694440C75KfWBej5x1ZZC-QgmjGPKC_6BMIUTIPmXtunHeNQybDPYiI18Kz8D0o3q_iCkeLn0ei3ncU_MVMD2Te02IcPq_hcjE97HEH0BAAjVZcEWBAo07eMUt3YWDgMqWnuGSgaylWOmvZZ6FAVwjJl4SDEaKqPkxQ8ZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تصاویری از علیرضا بیرانوند با لباس سربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107545" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107544">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d3e68068.mp4?token=iGv_pdPokiNJ5cW7r01OHsL1EoahTpozRvyD7uxGDTeCcnHGLZLD7eI0GdTyfMpYuta3hdwB0ou5DVtH8kWJ8tJisCafAOqxnlQG1hGYEL8Z9XdAaRf99SQMqC8ZQGy6jDrVNTW9QqC_t1eopoLNERQQotNd-qvroyTkpAMpoLfdTeiB4RajijIi0rMR1x-kVW-KYTmaD9ayrBTbFp0D-ZqDE309PlSY5ub-e78L8o85Ol2R7MoMBSScoQ4JtWhdxya1uweLpsPbzO4CTvmtbfgE9Cec8b8TOE7c4dq5kBY2p9_UwtqoHOF2_0RptH46hjSXwak_BUEaxqGPiwdM7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d3e68068.mp4?token=iGv_pdPokiNJ5cW7r01OHsL1EoahTpozRvyD7uxGDTeCcnHGLZLD7eI0GdTyfMpYuta3hdwB0ou5DVtH8kWJ8tJisCafAOqxnlQG1hGYEL8Z9XdAaRf99SQMqC8ZQGy6jDrVNTW9QqC_t1eopoLNERQQotNd-qvroyTkpAMpoLfdTeiB4RajijIi0rMR1x-kVW-KYTmaD9ayrBTbFp0D-ZqDE309PlSY5ub-e78L8o85Ol2R7MoMBSScoQ4JtWhdxya1uweLpsPbzO4CTvmtbfgE9Cec8b8TOE7c4dq5kBY2p9_UwtqoHOF2_0RptH46hjSXwak_BUEaxqGPiwdM7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚽️
توصیف امیرحسین قیاسی از امیر قلعه‌نویی: جوان‌گرایی و تاکتیک مناسب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107544" target="_blank">📅 13:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107543">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2b061cd6.mp4?token=blD_D_RqjXBBQozPivZEAPgTkGkCfiaDSfADFegOFQMWYwMuzjLvi3aHsLbn8q0Yq5o0aCArrouzAtt4UvKu-8zdPuUdpPgLyOIYZMF0EZkIEIqiVMvF5XpCWtDIB8C8KoY3otfPgJBdgnCFHNh6k41tdd0b3rec-HeZQC5U5JanldvZCYhC5FD6nMAoociXBi51zkK5LadC-67ymzxsl74DcdQhQsNXfKy5EafMGG-LgpVg0VsMIlts0nhEpzNdztmqf9WX6ZCR0qXqTOWi8bCedl-oaNDfRANKnqgWDpS9vBrTd7GB2vq1k3jQKQJ9thQeula5lCAd6vhbFx0-IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2b061cd6.mp4?token=blD_D_RqjXBBQozPivZEAPgTkGkCfiaDSfADFegOFQMWYwMuzjLvi3aHsLbn8q0Yq5o0aCArrouzAtt4UvKu-8zdPuUdpPgLyOIYZMF0EZkIEIqiVMvF5XpCWtDIB8C8KoY3otfPgJBdgnCFHNh6k41tdd0b3rec-HeZQC5U5JanldvZCYhC5FD6nMAoociXBi51zkK5LadC-67ymzxsl74DcdQhQsNXfKy5EafMGG-LgpVg0VsMIlts0nhEpzNdztmqf9WX6ZCR0qXqTOWi8bCedl-oaNDfRANKnqgWDpS9vBrTd7GB2vq1k3jQKQJ9thQeula5lCAd6vhbFx0-IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های امیرحسین‌قیاسی درباره سفارش غذا ۶۰ میلیون تومانی برای مهران‌مدیری!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107543" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107542">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9a4a5cb83.mp4?token=MKjCUK-Ky7Qsj0P3VZqgnMTs0Vo9727tDGKtwlMHEJnHMhOT8tP_VZpy2P9OHBN3LZAX7Vj-tWnjhdukp7OFe3qLNDCfOGOHSMtyt64yCuJSMY2piiezcIOtI2Z0MoKZMHxze49IpOkcOkeKTD1qkr3ljwU9U69SW8v2tfHus5W-npRBqGlbvSM8xhE6L2BVJFbEII6DH5-8Q0gbLwZ73zakAw5xcYvwHBHthl9nSN7BQ3DW3sDOzAJVHnxffKTquq5n83LkZUjSYwjAnS1uXGn6NfbPa7mvzUJ2LetT4WOKngtSGDd6Y1sLRs0WpLs5JlzmHukNyobdtPrABidmAYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9a4a5cb83.mp4?token=MKjCUK-Ky7Qsj0P3VZqgnMTs0Vo9727tDGKtwlMHEJnHMhOT8tP_VZpy2P9OHBN3LZAX7Vj-tWnjhdukp7OFe3qLNDCfOGOHSMtyt64yCuJSMY2piiezcIOtI2Z0MoKZMHxze49IpOkcOkeKTD1qkr3ljwU9U69SW8v2tfHus5W-npRBqGlbvSM8xhE6L2BVJFbEII6DH5-8Q0gbLwZ73zakAw5xcYvwHBHthl9nSN7BQ3DW3sDOzAJVHnxffKTquq5n83LkZUjSYwjAnS1uXGn6NfbPa7mvzUJ2LetT4WOKngtSGDd6Y1sLRs0WpLs5JlzmHukNyobdtPrABidmAYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
مارادونا: ۴۰ تا بازیکن از تیمای مختلف ایتالیا روی هم،  به اندازه یه توتی نمیشن!⁣
اسطوره رم ۵۰ ساله شد.
🐺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107542" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107541">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4869197932.mp4?token=DE_R-9MPfRD7z8x94Tvo3ExL49nYOeXQSfF6Zl6HvW3wGD-us04OSkX5Ks8_NgTd3Rg7JgZ5A9vR1Qb26pakUEeK_1wa-EZlozothVGusLzNvYPvf2hfhnuFEiC9tkDZIyDlhOjLnqmHN-P8pF3kHfXYH4QefEj0iMDHVso--YE0qRiGVJgNm4etlbjrUm84KHpkaFmc3lWKNFpNIxzMU8W5rTli1XZTHvCNua1GdKEO1_MxwgESDKjG6QKcmLyCkQlu6KB7nM-s4gc2Ze2fMRD8vtP-6PIOtVxRNwxYL7PZvv-NTUAG7DhD3tkRYdkb_r1SHZYsvCk6tz4Yl-yVhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4869197932.mp4?token=DE_R-9MPfRD7z8x94Tvo3ExL49nYOeXQSfF6Zl6HvW3wGD-us04OSkX5Ks8_NgTd3Rg7JgZ5A9vR1Qb26pakUEeK_1wa-EZlozothVGusLzNvYPvf2hfhnuFEiC9tkDZIyDlhOjLnqmHN-P8pF3kHfXYH4QefEj0iMDHVso--YE0qRiGVJgNm4etlbjrUm84KHpkaFmc3lWKNFpNIxzMU8W5rTli1XZTHvCNua1GdKEO1_MxwgESDKjG6QKcmLyCkQlu6KB7nM-s4gc2Ze2fMRD8vtP-6PIOtVxRNwxYL7PZvv-NTUAG7DhD3tkRYdkb_r1SHZYsvCk6tz4Yl-yVhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
🇳🇱
یک‌ماجرای جالب از فوتبال هلندی - بلژیکی!
خانواده آقای فن‌بومل، خودش، پسراش، زنش و البته پدرزنش⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107541" target="_blank">📅 12:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107540">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621d1efcf6.mp4?token=E2Egsu5HmLkAneRcIo_n0pjIkEQ2nj0vnKjksrR2ZK0Ua-UUP0GtkvDw3GwN96CsBGNeE8nmmq-a3aOJdmnARpT_EYlj9gZlyZwx2_Q0sOhkwLKNbGuj5LxV2ZwNJalEDiAecbs3Tc--fxb3mwfZtGTyHMHhLJnOlHe_f78yCmfSYQas1kx6JrU2atVnjzGk_S8YWq6SoZhW8uwscLV02NZdp7-w1PfTGIoJgxXJF_lmJrLpqfFj5Yf2WO8xcm83wOw-S2KKwUpiOL2OL87PDQEDUB0TLkpcUBKJVvgn7cD9qSe1P9Ys31vV2YDdVD39XDtqlRY7wNyqWxK3CRtClleI_9IXgzgiGaCKS7r_ZROCiWI6wPPIuOSZRIkOASiO6ABp6CFau5b8gtUIsm0q8oqML6tLgs4tXp9Di91aSTmXrmQ-l1IcGbQjVFoAeaMNKG_--1iLUfXX5zAbHeeWdBM5RuxpM-zq3q3qkPuV1y-PvxN-aQeMNagGYRInAk-xbDRl4at5N-c2R8JHX-MVQKm6AsdjgcUwABK_CgliefZpoYWGsrBFU5XQZ_ta7jjym2fNVvNVL4twr2w1lvB4QOB-vKq-JFenKmEwioyRUn2_Y2iQCBjpJo5N-Rl657MwsCompFNdIpHxdb8aQy8QvXvLI89PI_VL21xm4uypmnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621d1efcf6.mp4?token=E2Egsu5HmLkAneRcIo_n0pjIkEQ2nj0vnKjksrR2ZK0Ua-UUP0GtkvDw3GwN96CsBGNeE8nmmq-a3aOJdmnARpT_EYlj9gZlyZwx2_Q0sOhkwLKNbGuj5LxV2ZwNJalEDiAecbs3Tc--fxb3mwfZtGTyHMHhLJnOlHe_f78yCmfSYQas1kx6JrU2atVnjzGk_S8YWq6SoZhW8uwscLV02NZdp7-w1PfTGIoJgxXJF_lmJrLpqfFj5Yf2WO8xcm83wOw-S2KKwUpiOL2OL87PDQEDUB0TLkpcUBKJVvgn7cD9qSe1P9Ys31vV2YDdVD39XDtqlRY7wNyqWxK3CRtClleI_9IXgzgiGaCKS7r_ZROCiWI6wPPIuOSZRIkOASiO6ABp6CFau5b8gtUIsm0q8oqML6tLgs4tXp9Di91aSTmXrmQ-l1IcGbQjVFoAeaMNKG_--1iLUfXX5zAbHeeWdBM5RuxpM-zq3q3qkPuV1y-PvxN-aQeMNagGYRInAk-xbDRl4at5N-c2R8JHX-MVQKm6AsdjgcUwABK_CgliefZpoYWGsrBFU5XQZ_ta7jjym2fNVvNVL4twr2w1lvB4QOB-vKq-JFenKmEwioyRUn2_Y2iQCBjpJo5N-Rl657MwsCompFNdIpHxdb8aQy8QvXvLI89PI_VL21xm4uypmnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
روایت عجیب و غریب میثاقی از معافیت پزشکی برخی از فوتبالیست‌های مشهور!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107540" target="_blank">📅 11:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107539">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884ca354f5.mp4?token=Nut6BgwiG4rxH-LDhY_M24AJyNa-wXli1X18czXRVYCTOPuysOls6SyBQj2cWg6kxsxwmZgENB0I8OvlKS1hEueHT193XZauGUONsdRKyfdbeNjBvYiFOkoDT3ootY7ALygKfA6H3OpAFpDzwECVTuelhN_Z2l4nCheiv9PPzvP_Wv6NSeiNBUio2vRDKv1C53wsbwZ13MpS2mLrvN4VsjG6nmPsuHia13P66Iv_-TJrRslA_IidVeaUSzGXTNwgBN2cTaYV_1PBI3oxiOGbrLp5OBM9LjlB_KEToMvmRT3dljRkQSQoj075eSFSt3FY35geYCZY_LDzyQofMMR_vAjsKfOcKex7YjVAnMIPcmel8fibX_9Xi1sr07nDmOE2Mzvfsp9KGBevFh9Gsp_8QVVjY0emhjz1kG8I1EEJEHNznCEbfwnupTViMA9_yat9i3eImkBf-30t3EG_dJdeofpI-IyWc-zKH_2eO3x2ttYMN_K4D7bMSABz6xe312yyvSD5rquSiaIHFj0S4rvqUWdB3gYD3ZvKl07Am4lK9AGRQLir4wJyWTtmbXSGPCNYZLb5jO3uWqYHSxNuCeWbtFweJ8QyP16t_dZ5OIYqTtyG6JeRdJsdvqtFGtRq-yr06RCSP6tvZN7j-aMqOFwzdcC_zwwKSpAhFbOfXdRrEQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884ca354f5.mp4?token=Nut6BgwiG4rxH-LDhY_M24AJyNa-wXli1X18czXRVYCTOPuysOls6SyBQj2cWg6kxsxwmZgENB0I8OvlKS1hEueHT193XZauGUONsdRKyfdbeNjBvYiFOkoDT3ootY7ALygKfA6H3OpAFpDzwECVTuelhN_Z2l4nCheiv9PPzvP_Wv6NSeiNBUio2vRDKv1C53wsbwZ13MpS2mLrvN4VsjG6nmPsuHia13P66Iv_-TJrRslA_IidVeaUSzGXTNwgBN2cTaYV_1PBI3oxiOGbrLp5OBM9LjlB_KEToMvmRT3dljRkQSQoj075eSFSt3FY35geYCZY_LDzyQofMMR_vAjsKfOcKex7YjVAnMIPcmel8fibX_9Xi1sr07nDmOE2Mzvfsp9KGBevFh9Gsp_8QVVjY0emhjz1kG8I1EEJEHNznCEbfwnupTViMA9_yat9i3eImkBf-30t3EG_dJdeofpI-IyWc-zKH_2eO3x2ttYMN_K4D7bMSABz6xe312yyvSD5rquSiaIHFj0S4rvqUWdB3gYD3ZvKl07Am4lK9AGRQLir4wJyWTtmbXSGPCNYZLb5jO3uWqYHSxNuCeWbtFweJ8QyP16t_dZ5OIYqTtyG6JeRdJsdvqtFGtRq-yr06RCSP6tvZN7j-aMqOFwzdcC_zwwKSpAhFbOfXdRrEQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
‼️
سه‌ سال و نیم بدون رشد و تغییر در ترکیب نفرات دعوت شده توسط قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107539" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107538">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4v1flw0HMJuFCj1_xrEiWi2hexRKGGDoPFChYRUCMFA7o6T-IjgCuadSs5f010FEI0OgFVmKcszS0r-ifE2mi5-ZAcqvuqtHqmvcAdTGfiWHi-8ChyPGgWNRRlctxL988jwux5b3dBx0WYRNN5yKsS9bgreS2sMrdYW4v5l7gHo3VqOG9hQzQ-0d1qT1CT7930MAjxuDosLtO1L0yKzuASzkIOTT9FbQfQuVy9HvGmfscXQmMkFxGCkqe9yGKCW8igtxuXcSZS9TCzCwyhsbt28onYaJeT_aRUXMn1ggVE66IYKal6FhTLshjt0pOQMJnWrihuFGJEe0nXrfG95Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
📊
ترکیب منتخب دور‌دوم لیگ‌ملت‌های اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107538" target="_blank">📅 11:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107537">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
🎙
صحبت‌های شنیدنی رسول‌مجیدی درباره کیفیت آکادمی‌های فوتبال اسپانیا که زمینه‌ساز نسل‌سازی‌و قهرمانی در جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107537" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107536">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107536" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107536" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107535">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5Do6VBTnG9AIRhScEbIFGseMq7o5TlrrMIkGtMtzFLqZf6bINd4VSIexjAax1Sm2u_vVQUNydO3XKr7oEp5NERKqbXMDSqVwxHo3D3sBY-VB3KmtHhY91IU5e0326eZCcJqtm6QF-9OACRDhYz5bZT5Ly5hhDHgL9lYQaX3s7oqPsf87LbHgVbdCNb3s6xCl2CzzkQvAvdgs-QBPR9FSL7S8-71LAXFkprktzf7NiVDbJ8dipuy2JiYDvEIu1pRPTEbKrkmLq7maWFjly0LyyJhAKxaZImEg4F0AuvgJkIaBxS044U5pjyWRoL9bNZy_6ZKhmV3O-AezAmGioSSgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط ۴ روز تا انفجار در قفس
🦖
​ناتالیا سیلویا در مقابل وانگ کونگ
جنگ سرعت و تکنیک؛ چه کسی قهرمان جدید
UFC
می‌شود؟
🦖
​شانس‌ات را در
TrexBet
امتحان کن و روی قهرمانت شرط ببند!
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107535" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107534">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4KJMRg4ANxC1T-ELxsle8pBuY2Of6AGnapsfsETItM84wN7PIRvsq7W2Gz7wJItLODK0vrmKTVK4e5x0kz4DKoWwsxnvRcRBdwU-NbAGPSSPUotBpQlPLwRQ6NdL_TLQvpfErPjQIL14Bk0aC5vDkUdrWz09pAgCXFq30GEpRj6zeEnyi7sZsvBRRjDoIm6XnDLB3vAH26U9BamGNivjsKDRh2CprjVZ6umrrSBCP0PqwirgVp92w4IIrM2MlT4lJItgMtnXZoKu6XWQckzjgKu7y0W9cxzeBWsk3_fZIsl6h90tlfKAqHlGuIb0APU_nuFBY3ERqINI5dWHs6Xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
رومانو: رافینیا اردوی برزیل رو ترک میکنه و برای مراقبت بیشتر به بارسلونا برمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107534" target="_blank">📅 10:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107533">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvU7mHQujIP-RAp66NrttRuy4_OfECvkuV4kOIdZEdliM6HQ_j718XyEisdrBSYBiLqne4eUMyan-JpQiUHbf3FRDH3j65EQq55u4bq4bpwKN0HIdYahn0wPgUVn3ryjwia9DPq2Dhoa5hJHiRhy0rtHpVDgs5AJwBL0yXYqQojtfbkWW_nu8iQV_Fb9axiCXWsWeAzZZJ1QvJ7yw0OFVI0A_AL21zKP6CweDILn_xeUdS-57NSuTWBLoIk6zeLxGI1iTnfQEWl7ewNeDjRP_PJUGyJo2bhFL6suCwx9mB5Chzc5ml_WZl2DBHl9nEvcF1PSQSpp1_cseF0HhQ7LQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🇪🇸
اسکاتلند تنها تیمی که توانسته اسپانیا تحت هدایت دلافوئنته را در یک بازی رسمی طول ۹۰ دقیقه شکست دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107533" target="_blank">📅 10:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107532">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78614739b9.mp4?token=M4r_WRthLys_Emyp13BeMqhHIgZ9tWZZqvR7TwTFxESogv9CgWos37PbZjv3RQnc3lHa7uM2vYL91Swx4wM1W4_b9_ij0I6oS5OVRVwvp961ifgj-7pGgSpWoY_IFy_Rm1HJcaOZga26I9noCWjT3T3LJfOVDSuNyYZCXPwobQhxrij0UL2grh985ebYvS-Du2PvmLRT7g6hKM5q5cPTOWOTVzag9FDdArvfTTGYtNvuFYVHctJI-x-TXIal3AX2E1lOclq5pvkHn7aSN3pE2q0fRV9amQkrJv2v651mUFdRiSKdkzH0ehLFmjMCa72jZZzb4y8oynyn2PozwDQuQGE9CC658q4KinvzZYP4xYG2d4DYjJ5vtlhViBedOyIEYgOCxPY5GpKP2TY8Qo5lx4xo4MZ7yZ3qyNcqDR6KpEO01oJGKOGC6TYW9lkwDp_YguiO1pxhWWKZdkMPSf_e4mVG_Jep_XaT1czC2flcgXgBzcFBPw_nGhkbSeIJjV2gjeKmN22cT4y_0v5smSWWTUKeLYYAPKXEGDH-0JGSdw2DiCo4E74nd0P-oAtNuleYE0b_CeAIJL_JpxWi0D4zjWSG1krJNSKqitS6iQoYbWBCJYnno4ePlJZTz3vRPfRbNgJi2O8e46Yrr2v2mbZmpmWFgT-6YcpikpJkSfp4OH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78614739b9.mp4?token=M4r_WRthLys_Emyp13BeMqhHIgZ9tWZZqvR7TwTFxESogv9CgWos37PbZjv3RQnc3lHa7uM2vYL91Swx4wM1W4_b9_ij0I6oS5OVRVwvp961ifgj-7pGgSpWoY_IFy_Rm1HJcaOZga26I9noCWjT3T3LJfOVDSuNyYZCXPwobQhxrij0UL2grh985ebYvS-Du2PvmLRT7g6hKM5q5cPTOWOTVzag9FDdArvfTTGYtNvuFYVHctJI-x-TXIal3AX2E1lOclq5pvkHn7aSN3pE2q0fRV9amQkrJv2v651mUFdRiSKdkzH0ehLFmjMCa72jZZzb4y8oynyn2PozwDQuQGE9CC658q4KinvzZYP4xYG2d4DYjJ5vtlhViBedOyIEYgOCxPY5GpKP2TY8Qo5lx4xo4MZ7yZ3qyNcqDR6KpEO01oJGKOGC6TYW9lkwDp_YguiO1pxhWWKZdkMPSf_e4mVG_Jep_XaT1czC2flcgXgBzcFBPw_nGhkbSeIJjV2gjeKmN22cT4y_0v5smSWWTUKeLYYAPKXEGDH-0JGSdw2DiCo4E74nd0P-oAtNuleYE0b_CeAIJL_JpxWi0D4zjWSG1krJNSKqitS6iQoYbWBCJYnno4ePlJZTz3vRPfRbNgJi2O8e46Yrr2v2mbZmpmWFgT-6YcpikpJkSfp4OH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
واکنش فردوسی‌پور به مصاحبه‌های فرمایشی و سفارشی ملی‌پوشان: سردار آزمون، با سابقه بازی برای مورینیو، وادار به گفتن چه حرف‌هایی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107532" target="_blank">📅 10:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107531">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4481359e02.mp4?token=GKuMIfHfRqodm98K2qq_2d_CiVW0K2IG3_0MKY1tvFaFT4Nfh3Yvr9mdNYhCqV6ctVW3c9ZemTu-MiRhmFI4HAJAaZxBL3u1icG_Aeib8vqd4LEvzRGjCh8Bm6m7HZAE0tDLjTY9xUVeXwnHi4nBtNs7_GBmxSXW5HAqosqReAFxV4uCJYkYYASjISsbMxdLul_Ifi6LEl-XFCK2pV2HqKsjCMMneUsqRXqL1GIQX87_6uK2I4cPA9nDjaEL_rrIEvbrpZVRN87CieADUGgpaUlCYQfxo5jkiM2UBH-duygPa1Zbo2NLEDlCIlCfG71H5qyQSq745F9HvtCoaxHIxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4481359e02.mp4?token=GKuMIfHfRqodm98K2qq_2d_CiVW0K2IG3_0MKY1tvFaFT4Nfh3Yvr9mdNYhCqV6ctVW3c9ZemTu-MiRhmFI4HAJAaZxBL3u1icG_Aeib8vqd4LEvzRGjCh8Bm6m7HZAE0tDLjTY9xUVeXwnHi4nBtNs7_GBmxSXW5HAqosqReAFxV4uCJYkYYASjISsbMxdLul_Ifi6LEl-XFCK2pV2HqKsjCMMneUsqRXqL1GIQX87_6uK2I4cPA9nDjaEL_rrIEvbrpZVRN87CieADUGgpaUlCYQfxo5jkiM2UBH-duygPa1Zbo2NLEDlCIlCfG71H5qyQSq745F9HvtCoaxHIxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
شهریار مغانلو و دانیال‌ اسماعیلی‌فر:
🔹
چند روز پیش بیرون بودیم رفتیم یچیزی بخریم، یه نفر دیگه هم اونجا بود و خواست خرید انجام بده و پولش نرسید و رفت؛ بنده‌خدا اینقدر عزت‌نفس داشت نموند که ما واسش حساب کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107531" target="_blank">📅 09:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5234add2e9.mp4?token=umnyXm3zB7jf26HCpvNbLo9H97l0wpZmhwlE_DbRTEKwU2QSwpOA6QOo5cmLCv5YThlW0U3VQFL4ZEC2TnvUEJSBR-2TWBM_KZ5T_cESauxbjucsQLGSRedc3r4YuCZcsqbfN2pxMQA3VkqarQZEbZ3APR1KnVWtytChYJoiuFEoyALfRHPglnCz__p099mowtz1IB-21mGk0hFb_oeol4vRZ04xzUTRx7fWPTakWV8VKCvjugzVoZMIHVIt3bxO2U2lvRGDwtNF-70MDyzu7Uu2emtPv_urCenPov4ETUzxf-aqWhVL47Be2CV9rhsCiYk6bY1bUpU_UEbCl2QyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5234add2e9.mp4?token=umnyXm3zB7jf26HCpvNbLo9H97l0wpZmhwlE_DbRTEKwU2QSwpOA6QOo5cmLCv5YThlW0U3VQFL4ZEC2TnvUEJSBR-2TWBM_KZ5T_cESauxbjucsQLGSRedc3r4YuCZcsqbfN2pxMQA3VkqarQZEbZ3APR1KnVWtytChYJoiuFEoyALfRHPglnCz__p099mowtz1IB-21mGk0hFb_oeol4vRZ04xzUTRx7fWPTakWV8VKCvjugzVoZMIHVIt3bxO2U2lvRGDwtNF-70MDyzu7Uu2emtPv_urCenPov4ETUzxf-aqWhVL47Be2CV9rhsCiYk6bY1bUpU_UEbCl2QyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
میثاقی: سردار تو وضعیت سربازیت چطوره؟ معافیت تحصیلی داری؟
‼️
سردار آزمون: نمیدونم ولی میدونم دکترای فیزیولوژی ندارم، اصلا چرا باید بتو جواب بدم به نظام وظیفه جواب میدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107530" target="_blank">📅 09:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107529">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02612ddc0.mp4?token=icBzWfywV8vpOXt6cCyeRYRWCYDHOkTBCrqdnb3HNkL0Cp3yQYXERu9gqIvf7WGEmG9qu6B8PhQzJ6FU8TtdlMNlrQNY_N55LlM4QJKqnZefgl5Ic3kBFV760SBg6K95er2nWIQZ9pyR5ufy079-yy5j0AMR4KKUCXzuPNYkSYlO-JVRvxRW9ka_Jw-E9phkbH-yDOTBIxobVOnEecx7fWNSWDR2O3gq5pVQifM2Ak1RoAcM0LXkPwr9MnaO08W8kKH0t2yzfSSLlV1kc6rxMeC0MBYNc4oob5ibCeXiU50oME-L7bGxPizHJOsGlU94O76cD5RLUxd7UHSuVsuNZj34ip96DACarbsE_i9FcCphPzBtArOFu7g1PtOSavI_DHugs8NdneAUAxSEGApKKY3scSG89nph-k4sGf9Q-4Tvj6OH9YE9NdeAFsuCdgm4qn8JnqvGZ2_dsQ70T0M4_c1eVtOtaMj-YnjymW3deWp_AoMqp-yeKe1V-FglqHbXpp3OCb_SCObWkCu4btQ4VCeYbXOCmsXzELXHDlNGmvjD08oEe2f4c_a9pOmW_7rDoXV8yRYo_lqdai7I_5BsqnGS7_i9WeS41DZBPEOQHKnIPptEoShYEKJq14RPFVk4jxq4YPJmyoxZTDdbYxojMpY0hSeUCdZeN5Q8u7PLOTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02612ddc0.mp4?token=icBzWfywV8vpOXt6cCyeRYRWCYDHOkTBCrqdnb3HNkL0Cp3yQYXERu9gqIvf7WGEmG9qu6B8PhQzJ6FU8TtdlMNlrQNY_N55LlM4QJKqnZefgl5Ic3kBFV760SBg6K95er2nWIQZ9pyR5ufy079-yy5j0AMR4KKUCXzuPNYkSYlO-JVRvxRW9ka_Jw-E9phkbH-yDOTBIxobVOnEecx7fWNSWDR2O3gq5pVQifM2Ak1RoAcM0LXkPwr9MnaO08W8kKH0t2yzfSSLlV1kc6rxMeC0MBYNc4oob5ibCeXiU50oME-L7bGxPizHJOsGlU94O76cD5RLUxd7UHSuVsuNZj34ip96DACarbsE_i9FcCphPzBtArOFu7g1PtOSavI_DHugs8NdneAUAxSEGApKKY3scSG89nph-k4sGf9Q-4Tvj6OH9YE9NdeAFsuCdgm4qn8JnqvGZ2_dsQ70T0M4_c1eVtOtaMj-YnjymW3deWp_AoMqp-yeKe1V-FglqHbXpp3OCb_SCObWkCu4btQ4VCeYbXOCmsXzELXHDlNGmvjD08oEe2f4c_a9pOmW_7rDoXV8yRYo_lqdai7I_5BsqnGS7_i9WeS41DZBPEOQHKnIPptEoShYEKJq14RPFVk4jxq4YPJmyoxZTDdbYxojMpY0hSeUCdZeN5Q8u7PLOTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇫🇷
آنالیز تیم‌ملی فرانسه تحت‌هدایت زیدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107529" target="_blank">📅 09:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107528" target="_blank">📅 01:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107527" target="_blank">📅 01:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107526">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b621a66f.mp4?token=rwkTas0rkARARXxGBNRCzyaNglGS5I20v-bTqqs3wmrVWPv71xHEwP87U3I9bXkSL9tj0EkrDETAHnXjx7K056ETTh7olcblRHvvNj_asoyWHYIQoa9sqI4WsLJ7DlaA9oVY30Pm_XhGI_WqpXteRNfLN3d_Tzs9_Eefga-RHXAM_44ug1YgFQCtNd92TEDvoJFPQtgHrQTyIHBUZ-vqhWmj0SuSYEXycaPKnuLRSfJ_HbjgPao0buV3TYzgWH4RKXRCjRQuTL1zuutjZywZzRHVL4lyKZSWkeM-_PIdB3rNRxmkq9KPnxQ1LfQkb5GrOicCZdX_sq4SPR3MuDT4mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b621a66f.mp4?token=rwkTas0rkARARXxGBNRCzyaNglGS5I20v-bTqqs3wmrVWPv71xHEwP87U3I9bXkSL9tj0EkrDETAHnXjx7K056ETTh7olcblRHvvNj_asoyWHYIQoa9sqI4WsLJ7DlaA9oVY30Pm_XhGI_WqpXteRNfLN3d_Tzs9_Eefga-RHXAM_44ug1YgFQCtNd92TEDvoJFPQtgHrQTyIHBUZ-vqhWmj0SuSYEXycaPKnuLRSfJ_HbjgPao0buV3TYzgWH4RKXRCjRQuTL1zuutjZywZzRHVL4lyKZSWkeM-_PIdB3rNRxmkq9KPnxQ1LfQkb5GrOicCZdX_sq4SPR3MuDT4mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
کنایه‌های سنگین ژوله به امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107526" target="_blank">📅 00:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107525">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tI7FLluLQe5fph6TVBcVPx-L83-XDgubd_3ohLGiPHgjuHLwaC7zuU2ZgkWhS6LOUdChv5BaD0KK-sReHJ0-r-SbSinPI6eLtWuh4QzNIbi0nRNgMlf5kCDK5hyBppL8KU6p7HaLGr0Ni3dPkt4p320w8FVJgmlW4yPhtiHMzV8Os-sw0UfsaVqncmd0uMDFzMEJO-Kz_V7ZgpnxG8_QaXKH2eg29VGp6JTdTOq9N7xhovL0x_uSd8sjEbuxmeoRNKA3kywTgGEIKP6gxjztjeH6-QrWdPDdD9DK_JCO8t1E9Xg5r7Jo8bwQorZeD58oSKLio6ycLfama5OHcvoNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعتراض میثاقی به باخت امشب تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107525" target="_blank">📅 00:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107524">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqY40jl9SzNoX9AimQMfl33LvRUc4tJ8quQ54Dn7jqIffjz9xrEcNe_EJA3AmZoPJikqpaGtobRYtvNntrYsMycMgMjzkcrHlgEKekaI4D088cqltqbkraSX2W-URNKRjh3Xtnmh3DrJ37NcZK7lKm0gBBR8onFdV4e_-hjHjSdPpRZ0ewv4FX4rnyJ3qKRErhxPEnXb8a6GsVh7RwFqUsNUSo97QHR_VjYvekRhJG3KCDrRVgzo06yB9j5cgmJbKzzh4mZiXbvgkrkYzXWrc3ANRWtEeCrx1ldLKjGFSxOQyG2BA3DiuFtZk5P1Du3drYfxoEG5CgPB_3THnw63gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
پایان بازی؛
🇪🇸
اسپانیا ۴ - ۱ کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107524" target="_blank">📅 00:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107523">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5febf615d8.mp4?token=iobkedkTuCeg8-uI_2jVT14Lp-a8WNz2xfxawABn8tbwRCSFUKW4AzxPjVqN_ZCkZxX1MfDOSyZ7b8s8iC29ZoqgONdrB9475KzPA4SyEFGDPHvRnx1iz8eLOMq-gLIFGf1ZCnaoeYrnv55wijBxvYE_Ic5nC1xev2Eq_h-8boIdMj9eXz_qquFZ7BcecqkqKwKnGyzRQ4bLTcFTCeOzmEu5XLtTpZxUdGqUKw5NRtkwV7UZGFMm0wgg5Jty4uqUs1HJgv4OqnYY6M_RVs9NoXxuee4D1aSkuxPWEpC627uTOupmGf-VROqUfSX1hLWvbH72SIhw1ExUCqwbbQy1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5febf615d8.mp4?token=iobkedkTuCeg8-uI_2jVT14Lp-a8WNz2xfxawABn8tbwRCSFUKW4AzxPjVqN_ZCkZxX1MfDOSyZ7b8s8iC29ZoqgONdrB9475KzPA4SyEFGDPHvRnx1iz8eLOMq-gLIFGf1ZCnaoeYrnv55wijBxvYE_Ic5nC1xev2Eq_h-8boIdMj9eXz_qquFZ7BcecqkqKwKnGyzRQ4bLTcFTCeOzmEu5XLtTpZxUdGqUKw5NRtkwV7UZGFMm0wgg5Jty4uqUs1HJgv4OqnYY6M_RVs9NoXxuee4D1aSkuxPWEpC627uTOupmGf-VROqUfSX1hLWvbH72SIhw1ExUCqwbbQy1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌سوم اسپانیا به کرواسی توسط لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107523" target="_blank">📅 23:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107522">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گلگلگگل سوم اسپانیا به کرواسی بازم یامال
😐
🔥</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107522" target="_blank">📅 23:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107521">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/713c4da9c1.mp4?token=ZeDi1vLTNaqzb3BOfcmZ_1qI8QjFh14tppdjf2vceBBHykcri_YfSQ4asnsFcYGrWYb_QxBBTqp5uLKFBDfitfGxMzI6Ts9UjXCtwniFxuhyuMckHOrpcEWJN_0aYjmjfURXGS_C6o7ado74knM52HCMTdjS7pZrcG1emLXkfLpzMs8bIcJxZkQO39JHyfvI4Z68SclDX_jOgibBUB37PPJMLhP6BE79gzU4xFW1PAd5BkAdU54yOLahAzS4nZIbabDWKbC5LjnQr54P6Oi0ZMaavGHPNFBytRRySnLBS_M3Ts4CMmP95QQM6EWhFL9w5VmmDhStzOtPZTEf9XEVQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/713c4da9c1.mp4?token=ZeDi1vLTNaqzb3BOfcmZ_1qI8QjFh14tppdjf2vceBBHykcri_YfSQ4asnsFcYGrWYb_QxBBTqp5uLKFBDfitfGxMzI6Ts9UjXCtwniFxuhyuMckHOrpcEWJN_0aYjmjfURXGS_C6o7ado74knM52HCMTdjS7pZrcG1emLXkfLpzMs8bIcJxZkQO39JHyfvI4Z68SclDX_jOgibBUB37PPJMLhP6BE79gzU4xFW1PAd5BkAdU54yOLahAzS4nZIbabDWKbC5LjnQr54P6Oi0ZMaavGHPNFBytRRySnLBS_M3Ts4CMmP95QQM6EWhFL9w5VmmDhStzOtPZTEf9XEVQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
قلعه‌نویی بعد از باخت به روسیه: از برخی بازیکنان در اردوهای بعدی استفاده نمی‌کنیم
ای کاش از خودت هم در اردوهای بعدی استفاده نمی‌شد، آقای قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/107521" target="_blank">📅 23:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107520">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
‼️
⚽️
امیر قلعه‌نویی: دو بازی اخیر ایران بسیار مفید بود و توانستیم پلن‌های تاکتیکی خود را به نحو احسن اجرا کنیم. انشالله در جام ملت‌ها دل مردم عزیز ایران را شاد خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107520" target="_blank">📅 23:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107519">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86c5f06ad.mp4?token=hC8fWeKMOVpAGJKYt5Nd5PqxYMGIZPCa9SDG2ftc3MQTTvGX60UuYimDQy7Qrnqvr0tlaLlB6YSGm8MEBaOgebIA3ktzXGruMBuPb5NLdD4ZXK1vJ3YVLVhPJSiAg1_DM3QWjfZR0Et7HApg4xx69mqvd7Lkn5zlcYcKN0R6eapnYPjB_x-VbK8wQxKNYWIpVQHvHVlZDCbFPqPedtL3psC56ha-9QfND0tsbAYtqRl8rSuJ9h1Thqf6ZbHnazZ3GJM9xIuHgczk2nJuOegH9c1m8iOIxnefcE9-e6yd3lsLzG-eGMDhUmnT2xQicBlGT7lC3E56U2FPiOO2-xqcnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86c5f06ad.mp4?token=hC8fWeKMOVpAGJKYt5Nd5PqxYMGIZPCa9SDG2ftc3MQTTvGX60UuYimDQy7Qrnqvr0tlaLlB6YSGm8MEBaOgebIA3ktzXGruMBuPb5NLdD4ZXK1vJ3YVLVhPJSiAg1_DM3QWjfZR0Et7HApg4xx69mqvd7Lkn5zlcYcKN0R6eapnYPjB_x-VbK8wQxKNYWIpVQHvHVlZDCbFPqPedtL3psC56ha-9QfND0tsbAYtqRl8rSuJ9h1Thqf6ZbHnazZ3GJM9xIuHgczk2nJuOegH9c1m8iOIxnefcE9-e6yd3lsLzG-eGMDhUmnT2xQicBlGT7lC3E56U2FPiOO2-xqcnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
پاس‌گل لامین‌یامال روی گل دوم اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107519" target="_blank">📅 22:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107518">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2651377ca2.mp4?token=a1B29B9nd2ZgxZi5yRZOgAiXoY9nGBLAjKLdaWTp_j6viZr_-QJNFbtwmWY3zwx3Rll7v27Ci54KxscyL9MW9HXZKyHZDHQPMv8zjQgUeeSwKzGyb6vqA5io5s0S62FV8LafPq5ly60x1t-Kd49A4TG5KVwCphj2hhuoZAea_NWXfUKzU0VQhsJCxOpo9hoR_tBIFB3ZQAYkLUsQ-GBZREnIeb71vg943-rgOeIIJDjPn76HSKLZMfhXtJOu7mzOLHv0nTC_4yz_7A-Tmv4IX5bpMpJtq_6msQyRoNOM4QKsrLIyzTUmPWzKbVqn7Le4czVrSacAPxA_10y03oYVUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2651377ca2.mp4?token=a1B29B9nd2ZgxZi5yRZOgAiXoY9nGBLAjKLdaWTp_j6viZr_-QJNFbtwmWY3zwx3Rll7v27Ci54KxscyL9MW9HXZKyHZDHQPMv8zjQgUeeSwKzGyb6vqA5io5s0S62FV8LafPq5ly60x1t-Kd49A4TG5KVwCphj2hhuoZAea_NWXfUKzU0VQhsJCxOpo9hoR_tBIFB3ZQAYkLUsQ-GBZREnIeb71vg943-rgOeIIJDjPn76HSKLZMfhXtJOu7mzOLHv0nTC_4yz_7A-Tmv4IX5bpMpJtq_6msQyRoNOM4QKsrLIyzTUmPWzKbVqn7Le4czVrSacAPxA_10y03oYVUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول اسپانیا به کرواسی توسط لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107518" target="_blank">📅 22:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107517">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگگلگلگلگ یامال بازم گل زد برا اسپانیا</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/107517" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107516">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f859d863.mp4?token=RIbB8Qf_-lDljYWdpSbWIJYxFwSQ3jMhSUc9Xyt2T0Db6c7sSebYvWbuqoXFJBeWyxfZpE69yKiqeoZmBHHXAu83_DqONfoUrgvEmMNpE6i7pAfPx4Nh5Z7srzbi1Aty_x4WN6T1T4k_alRQl-AENIiyl1QnJ9pjqY0MTpjYJVPukA7IttJz6u2KDAI0KLuPM17csEqSCYTZc8kkkhL33_I00RF20HjfHPG5JbOHxkNWhTgokDq4H7RZ97bel3Z5lP131mK82J32HcAFSJtx6XEDeADkLbSN-JwnqDLJ-IXiv81BTuAjkwspj1zBtwpF-kQscpLnBCzcDZkZgZKV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f859d863.mp4?token=RIbB8Qf_-lDljYWdpSbWIJYxFwSQ3jMhSUc9Xyt2T0Db6c7sSebYvWbuqoXFJBeWyxfZpE69yKiqeoZmBHHXAu83_DqONfoUrgvEmMNpE6i7pAfPx4Nh5Z7srzbi1Aty_x4WN6T1T4k_alRQl-AENIiyl1QnJ9pjqY0MTpjYJVPukA7IttJz6u2KDAI0KLuPM17csEqSCYTZc8kkkhL33_I00RF20HjfHPG5JbOHxkNWhTgokDq4H7RZ97bel3Z5lP131mK82J32HcAFSJtx6XEDeADkLbSN-JwnqDLJ-IXiv81BTuAjkwspj1zBtwpF-kQscpLnBCzcDZkZgZKV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دیس ابوطالب به فان 360 فردوسی‌پور: فان واقعی اینجاست و هیچ شعبه‌دیگری نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/107516" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107515">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpBZMnh7dQxptnnOHhwz6u7ig15irjH7qawe50W0eOqVjTId3NH4m5g_9g6fKG96JUWpfRcz8EhHW6EA8Bl4xYkNXpqAoEbw_ZZ6fuLQA2n_i0_LZ0oZmlD8Sr58hFbQMv1reOgC3K3PF2DoqkZjk_xihzMhEjb5fhAKZLmgN6GKzkbJFQiOdSivI_f_k2PAgNI7QKRBLiFoKr6ONLXKOt2qcdud5SmIKNbBHzrHCHc-lOzHmfD9AQ4t6LWGCoXBLcdJL70a6tPXOBfgpaUtM01kzFvE4LgpK6m1ZdsuPZdid6efOb2wZIai0x7a1SO98EuviWdIsmZ1jrGQNbeqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان بازی؛ روسیه 2 - 0 تیم امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107515" target="_blank">📅 21:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107514">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
پنالتی برای روسیه</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/107514" target="_blank">📅 21:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107513">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niCp7m6-GkQbHTAMtBCLYfhalh5pmEkXVFw3GXi8gLvXw4G_l_UKV8ePyxKxGj2Q2ZhxRCdA8AdCVftURmo3w9NUsvaHdw0qQdRN3uQNJ3izc0Ou9b3nCYR3Nn-eI0z1YwO_XGEZWrhveCWuqD4tl_YLjVH6PncVjIOvOAuKmANBIDTK55YBJG7ZTB1CQ2EVUxLeZGkk1OYyVJYsy4lXxxC_iQJGWBhDfvhK4G33YQe4pnJVaiNq6poz7slqxGBAapRVC4Qq6FWwqkre3DQ8dJsnOT-ixYNN_oVDdcFyZ7EMEt0PqcdY7w2ZWp3acDe7idwf-eTlB8wIhsDZYUtQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
وضعیت پات چطوره؟ ران پای راستت خوبه؟ همه‌چیز مرتبه؟
🚨
🚨
رافینیا: «خوبه.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/107513" target="_blank">📅 21:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107512">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c98093c1e.mp4?token=VwK9nHKyLVbe9UsqoireG13TbvanO-PMb7r9JAGS0LNmzD6FoV-8ETTJoyezOlpszxLoRTkw6Twe2KvbHVqQuCEtFO_iR-Y23SN08HzDZOiuUSDWBidcZWYwwpQuKDOJLL3GxQ-TVzD7u7Hcsd8Cpn56qDRFds3ogH22gBjih99vPgpmblZLo85FwUU7hkKTEwXAn7PXt3SuJWkuYs8bjDf-i_FluXYsqPWzWEzZMYzZFs53UWjdiITDIVTnD3IseAcX8ur8yZYkUlZI4J5DO7rqnnsDr_jSXzifUFvMnlvy4L2sXZCs9wxR1e_qUnK4TPJ-IR2f9gekNo6bmedfLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c98093c1e.mp4?token=VwK9nHKyLVbe9UsqoireG13TbvanO-PMb7r9JAGS0LNmzD6FoV-8ETTJoyezOlpszxLoRTkw6Twe2KvbHVqQuCEtFO_iR-Y23SN08HzDZOiuUSDWBidcZWYwwpQuKDOJLL3GxQ-TVzD7u7Hcsd8Cpn56qDRFds3ogH22gBjih99vPgpmblZLo85FwUU7hkKTEwXAn7PXt3SuJWkuYs8bjDf-i_FluXYsqPWzWEzZMYzZFs53UWjdiITDIVTnD3IseAcX8ur8yZYkUlZI4J5DO7rqnnsDr_jSXzifUFvMnlvy4L2sXZCs9wxR1e_qUnK4TPJ-IR2f9gekNo6bmedfLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
‼️
چهره درهم قلعه نویی روی نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107512" target="_blank">📅 20:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107511">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlXliUzZGFbrc3bfOLLWpCJPQdj-LGzSTfebtt1pbMPiwR-0rij6LC83EnEYBcIM0c4FyOV9X9n_rU687SLLjJ37Iedx93PNnfhiBY9Okh9GGn_f5P6ggTBLIGP9foTeghRt7ckL16VjthKlIJekhMf3POfgA93fAliwInr1XBlUI32ZBkuCXxCCPYPENa6cN7Dxq_y2M7Slz2ZeEHbmGO2IxjOEj_JDfpQqj8MNDR3NqZXV34VSJFTTxaLOlZUtsmlgdKcPiv0I1K31wbaktgSQYg8E24BKoxZ3GfzdERJe6sEOXLpQRmKIAfctO2JEId02l8V7y-EKVBjz-CePyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇪🇸
اعلام ترکیب تیم‌ملی اسپانیا مقابل کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107511" target="_blank">📅 20:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107510">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFScL6jO__yvqA-yce9PN8QGw9PbGzJ2tPFvR5ZFtjDvKOvVaowYWFpCP4iAGjHkX4O5NBWNv4x68UvHm7hiTNoQpNhyg8MPXJQU-JU8fXz2ZlqU1ogbEqjLeSQs_ZVejyLuISLHm7qZpMFnqpxbG7SAKp7yUjllpGaPuX236HMeLWebmlDwO-upX3OeJ6mVBAdl0qyuquXceTSpm4BSEQ2-VX1YQ6UHV1bshV3o_b3GC3bFrHkVlVlgwcVsYicqOny3BdvSju0fVHWMUVn2vbFzTVLlMruJ-Ap74gLRlENXjKpV74peYgFqdDWctQKDoK89Bb-9Iw5OGy9h1fQ8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران حالا بهتر درک‌ میکنه که این‌ مرد چه نعمتی برای بازیکنان داخلی و لژیونر بود و فوتبال ایران رو از حالت کیری الان نجات داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107510" target="_blank">📅 20:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107509">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=XnJUnqyYd-Kvkob2JY6RPaPx2tFG28L37rsLN5cVFn7mFeIi_AuV-vTFG_jxfcCC0jgnW3KBNcbDOmc6AmdeMTycEPNqvoOpgf1DB3zSp9TCC_CPvNEaCw1LQeWT2RGggt_idce627QBUsy7W3mQ_xKTY5EiNR-lPhYoNKNStlHW32hbuhPdcsWm7CnGdl0Jt3WA2xaCt3oxF4zqiXBtKfvWwNI7GM-_7xxiH3Z5aZOcIoSJ4HuroC1PfubSsKz9_g5_NijsEW8TXHLa29ugDfSpjt9zD2t9YcrLx2fM1Av6MqGSi0YVZNP8NYAIXgC3--dgan8_48VaAxhdpa5ymQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=XnJUnqyYd-Kvkob2JY6RPaPx2tFG28L37rsLN5cVFn7mFeIi_AuV-vTFG_jxfcCC0jgnW3KBNcbDOmc6AmdeMTycEPNqvoOpgf1DB3zSp9TCC_CPvNEaCw1LQeWT2RGggt_idce627QBUsy7W3mQ_xKTY5EiNR-lPhYoNKNStlHW32hbuhPdcsWm7CnGdl0Jt3WA2xaCt3oxF4zqiXBtKfvWwNI7GM-_7xxiH3Z5aZOcIoSJ4HuroC1PfubSsKz9_g5_NijsEW8TXHLa29ugDfSpjt9zD2t9YcrLx2fM1Av6MqGSi0YVZNP8NYAIXgC3--dgan8_48VaAxhdpa5ymQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل دوم روسیه به ایران توسط گلوین (35)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107509" target="_blank">📅 20:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107508">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
گل‌دوم روسیه روی سوپر کاشته حریف!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107508" target="_blank">📅 20:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107507">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117f9ab643.mp4?token=gEoWtESriUW5fMV8GDRPMV6JFLeIby7z3HiHeGzEXMRmBLQfc4ifJWFeuicdA2PU5rsZKHQXsjFA7FPAmB7ys1Q8uHkxH5GE3MqzIURc42Puaj-2Eq9PXkvDkQW8_qda8Hptyl9EGOBYOfDHOPdJJKhdG6vOrIKMB_0vNgJ8WepiBLVsbr15BUB2EbOiVkxfXh_ONIm_ouyRDgRS0LRtbwjdy0w_BF5UYjAx6ygaDrWb0aAswMDls5yWaxyol0eMRhmbrGHGOJ1e5vcnVxj_qaLmS0mqxsDGGYitdVtalA5zHsvqV_rjYwxwqj9r91O1WRvOp3K_TC5Va9dUeUHYEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117f9ab643.mp4?token=gEoWtESriUW5fMV8GDRPMV6JFLeIby7z3HiHeGzEXMRmBLQfc4ifJWFeuicdA2PU5rsZKHQXsjFA7FPAmB7ys1Q8uHkxH5GE3MqzIURc42Puaj-2Eq9PXkvDkQW8_qda8Hptyl9EGOBYOfDHOPdJJKhdG6vOrIKMB_0vNgJ8WepiBLVsbr15BUB2EbOiVkxfXh_ONIm_ouyRDgRS0LRtbwjdy0w_BF5UYjAx6ygaDrWb0aAswMDls5yWaxyol0eMRhmbrGHGOJ1e5vcnVxj_qaLmS0mqxsDGGYitdVtalA5zHsvqV_rjYwxwqj9r91O1WRvOp3K_TC5Va9dUeUHYEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇷🇺
گل اول روسیه به ایران توسط گلوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107507" target="_blank">📅 20:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107506">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">روسیه یکی به تیم قلعه‌نویی زد</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107506" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107504">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDvJG_nmWloakWzQDbwEOwMYO3q_M0XQkPgTAMi22RMf2X5IcUn2EfmwesBTaCTkUMjtSaU2PSsKUuanojTsLq5dFfkhy-x9qVuyN6vpsAF0_r681XpofsA3FVQMOjJ7VDHvIMFyjfTJWeHR9BTTxmystTKFniHMMQ-cscnJmqvApRjZwzgjl-Ckfdyoj6E0GjLSDvpQ-OrVuNB6-f3lUw_LGj7GfjHOMMKjke6aF81BUid0qsqJ3GiwiNwY-vXhHAUd_Kz_2VsNnjenv1CKIgz9d7Jz4-ddzBPmIcValSdSNY3A0FszwiYYOA8Pt863lf-mji3NTYDllHc--fkq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر تو یه بیانیه جزئیات تخلفات منچسترسیتی تو فاصله فصل‌های ۱۰-۲۰۰۹ تا ۱۸-۲۰۱۷ رو تأیید کرد  این جزئیات تخلفاتیه که تو بیانیه لیگ برتر تأیید شده:  منچسترسیتی با تعدادی از شرکای تجاری خودش قراردادهای جعلی‌ای تنظیم کرده بود که توافق واقعی میان دو…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107504" target="_blank">📅 19:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107503">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJxJ0pTNGgOaANMK-wlv6L0IqnZTiplViIY1F5t2n2bn-5vbVb5lv8RG6-KoUKRx3nWjuxCN1zgjy7OfqaDjIXhAQ9QcDXJgBFraXDZiwjsbasFMPfbwSev3C7TGlNW2Cv2Lr16P8tcK8qMZVsmW5bVZ_-YVG2L0rZnwrWaxnK-3OkBxvbpD1oFm16XlitdDi7Bo7AoUbCvMGoM_gFis-khKLxx9bSOrRyM9XzCIfEAenjyt8Stz2BFu9bBnewOHvRKShL8aRpW7oBHNVsGl4ihZ89K0x2VVirO6kXlcmbTIK6rgJa7d6lyDKCICYvoAcEfzvO4UODS5PHMMTNqw3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر تو یه بیانیه جزئیات تخلفات منچسترسیتی تو فاصله فصل‌های ۱۰-۲۰۰۹ تا ۱۸-۲۰۱۷ رو تأیید کرد
این جزئیات تخلفاتیه که تو بیانیه لیگ برتر تأیید شده:
منچسترسیتی با تعدادی از شرکای تجاری خودش قراردادهای جعلی‌ای تنظیم کرده بود که توافق واقعی میان دو طرف را به‌درستی منعکس نمی‌کردند. این باشگاه همچنین به توافق‌های «صوری» دیگری نیز اتکا کرده بود تا درآمدهای خود را به‌صورت مصنوعی افزایش و هزینه‌هایش را کاهش دهد.
این باشگاه صورت‌های مالی نادرست ارائه کرده و وضعیت واقعی مالی خود را از حسابرسان و نهادهای نظارتی فوتبال پنهان کرده بود.
منچسترسیتی به‌طور قابل‌توجهی محدودیت‌های هزینه‌کرد مالی لیگ برتر و یوفا را نقض کرده بود. در جریان تحقیقات لیگ برتر، منچسترسیتی چندین مورد از وظایف خود در زمینه همکاری با لیگ و رعایت حسن نیت کامل را نقض کرد که از میان چهار مورد ادعاشده، سه مورد تأیید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107503" target="_blank">📅 19:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107502">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a09194b9.mp4?token=f3ovMNxzBZ4glpE0SJgwC-tCosvOLceHQGC0f2V9k1dLpIA6oJ5l_f4uqSQRNrc4xQVq4RvBvuX8S1Ypun-2Y-h2uZ4ejiLdcPyP8DPy9s4jFsmSoMPD6Zd5fm-fbEDjyIlTktLKhBUXSQLh3T7uWfPN3qBszb5uYJ8JwWxLwV3vSX7tQwiPDWmB3IBOZoVXarcTyxEhJCgOMa-Pp7Rcb7naZr51oXkKHynL9nTHBRp4PIVgDxvOEypN40gg-z7Jg1v-Bym0atNzAbH7OffOW-XkMYfU3Q_0ejrxfXzzDlVkUd07JBSmuDJfxA02MQIkh-lAS-Cw02amATXVH992LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a09194b9.mp4?token=f3ovMNxzBZ4glpE0SJgwC-tCosvOLceHQGC0f2V9k1dLpIA6oJ5l_f4uqSQRNrc4xQVq4RvBvuX8S1Ypun-2Y-h2uZ4ejiLdcPyP8DPy9s4jFsmSoMPD6Zd5fm-fbEDjyIlTktLKhBUXSQLh3T7uWfPN3qBszb5uYJ8JwWxLwV3vSX7tQwiPDWmB3IBOZoVXarcTyxEhJCgOMa-Pp7Rcb7naZr51oXkKHynL9nTHBRp4PIVgDxvOEypN40gg-z7Jg1v-Bym0atNzAbH7OffOW-XkMYfU3Q_0ejrxfXzzDlVkUd07JBSmuDJfxA02MQIkh-lAS-Cw02amATXVH992LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باهم ببینیم قطعه ی زیبایی که استاد جواد خیابانی برای گلر تیم ملی، علیرضا بیرانوند تو مترو خوندن
🗿
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107502" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107501">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107501" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107501" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107500">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tu985II7ezgEvEu0KsIsU5n2vubCKd3EMvfhsSADeJcAkondNaZDhnFQqXGkUuMLFFwjoLC6_LNLeRPJPX0zYY_DD97J1UoplZPyTvmQBuHLQMKx28cvg9oL0hfrXh1YCGZJm5jVXzydSZA6NAWVGx07ayB7qLZRZzAk3rdLl2uGZV-kI4nEtuIsE0cB43URQVxAIy8pRl3rVqVaHILmj7YffpbyvWbGSPdsgdz2aBA63hPEGY4om05KGM8I6JHigpinetEFoIoxNVJV507faEbkW6CqfF2hiRkm11dzz8oc5skIVfakIZBTynlXeDWsddogljc-8rDN5dtYY4B_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز کرواسی
🆚
اسپانیا را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
کرواسی: ۳ برد، ۲ شکست و ۸ گل زده
اسپانیا: ۵ برد و ۹ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107500" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107499">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0WxohbESnot85jooeN7aDSCE-8WVQ6Gjpn-M27_UpTsPmXopXW49ezWUvxo_MfB8WwaPKLVZ7MyUxkxs7SBJVelwoo3_sVxMgDaSNU5VZc2JCoYksmOyeTqztcNr7kXE7X5P57miSpWvwrBlNksnVhtiXyOEv_LZ4HjEbwemKxyxEu38rDl6hXLp9YhEm-uBJYhU2El35MxIZR0gBSiFLqzLUQ1-iQeflCnuknNjvBwzFsdijyjWeXyKbdKPnZGEoGO6BIqEsogXcOlnWeNLXeEzpQrivrxpXQlNrkX9UqjXZOqWDg2DIyxVHZk0gI4RfKkxQz7UrLppq5XrGDfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
رونالدو بدلایل نامشخص در تمرین امروز پرتغال حاضر نشده. تیم ژسوس قراره فرداشب با دانمارک بازی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107499" target="_blank">📅 19:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107498">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68583cf71d.mp4?token=ZlXuyMcdpcb2NvOJR_-rU39CQSMGnnr7oMGKPGTrUrgNy_jOBL8nQKILv98MFa81YUpXcn6Rxc5opQOfbacvatk5QQ-HbwXnZZEpcxWAXcQ-GvgVPkaPAinj-gHpzjChvKvKQOWdm2BmuFdnreJTnnmN00KziCPzRJmyObieUOECKxIl3S5eMaQQlHKAGZ8A0HXxaF8UGE0XZFsVT26o4MpVOhdlQDBW0H7Ao0Ds_rEUwrcpMMLRmnXVT6iY9mnqgPmRVH_JsTuYi3qr3xM3hnKYDYsRlTdMN9hC5HBzElBj_ydOGJSPm1SAHz9loFsCAnOK3JhwtDKKpxbqgWyrBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68583cf71d.mp4?token=ZlXuyMcdpcb2NvOJR_-rU39CQSMGnnr7oMGKPGTrUrgNy_jOBL8nQKILv98MFa81YUpXcn6Rxc5opQOfbacvatk5QQ-HbwXnZZEpcxWAXcQ-GvgVPkaPAinj-gHpzjChvKvKQOWdm2BmuFdnreJTnnmN00KziCPzRJmyObieUOECKxIl3S5eMaQQlHKAGZ8A0HXxaF8UGE0XZFsVT26o4MpVOhdlQDBW0H7Ao0Ds_rEUwrcpMMLRmnXVT6iY9mnqgPmRVH_JsTuYi3qr3xM3hnKYDYsRlTdMN9hC5HBzElBj_ydOGJSPm1SAHz9loFsCAnOK3JhwtDKKpxbqgWyrBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
صداوسیما والیبال را هم از روی آپارات پخش کرد/ بودجه ۴۰ همتی برای مخفی‌کردن لوگو!
📺
سازمان صداوسیما که به‌خاطر پخش قسمتی از یک سریال تلویزیونی در کانال آپارات کاربری عادی به نام نفیسه‌جون، از این سایت شکایت کرده و دنبال جریمه ۳٫۵ همتی است، بازهم برای پخش مسابقات ناگویا تصویر زنده آپارات را بدون رعایت حقوق ناشر تحویل مردم داد.
🤯
جالب این‌که همچنان سانسورچی به‌دنبال محو لوگوی آپارات است و مجری تلویزیون قطع پخش را به ارتباط با مرکز(!) مربوط می‌داند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107498" target="_blank">📅 18:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107497">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Urg29ABb63_WcCReRwB8gVfsxtL9oo8y5txa7sXVLmyzKpFHux8OdlfWuiTbihbooYoe0PyGEm6siDeDAM7UrJ6YLMbueben1GQY_nntXtmn5totkKOSg-l0H2s-jvPnyIG-Vu0NPKfWAqmaR3RSyQzg7NhNVCehTxPJjSORRH7LUL5ibocZKlIyI9hLu-znJI7qjDHw99PSqqYJ9y4jGZM0b4NQKCdL-qDmobFV5xq9ptad9LnN-6g82SSMLMfHcLIsXX3McGNsm0QD3mCg0HZPYAF1Vyb6rndYirbmJukPnGJBoAzL1GVQoeQFG_vzvuggtCJvGmASMwCUCmrVFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب تیم ملی ایران مقابل روسیه
سید حسین حسینی، شجاع خلیل‌زاده، علی نعمتی، صالح حردانی، آریا یوسفی، رامین رضاییان، سعید عزت‌اللهی، محمد قربانی، محمد مهدی محبی، سردار آزمون و مهدی طارمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107497" target="_blank">📅 18:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107496">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2P67XVHSAYci0PuLdrOvPTXv74pOJkEi547POsfV74dZVhArvS3iL407Y8yGVjQrvGFt7qZP3vgaJ0qpxv5zmCGDt3wiEKPABgvyVRMb23vc2fjSYYMaLSEdv9H3GxP5cybzwITwicffac9sD7yAbRLrjYxzp7wkI5qJZLjPVq3uSLMJpiqC9vUjZdZRoRrzNDQXN1HfSGrEMxL--pmrHuGXcRBVcOFUQQoiiIj92KiDWyhFLXRT4fdVYHr37hrGjYTn8PncLfvGYrQJrQjBaV0ITwOFMazJrmZTRvpltoAQGQH_wL3zAoDRCPoxtq_haaGiuWFmiW4k5ecEKIhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
مصدومیت های کریر رافینیا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107496" target="_blank">📅 17:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107495">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30660fe341.mp4?token=o5BGEwPocMGJMSYs-4TfU9djvrUE-og8g-w5mOGjT6JgpyHKggv3v0wn19Vuomf5w-JpxeTNLCYyEycUi9Ruw-tZJdh-yirSeQkifx5ZUsEZCD7AEQAqHk3srDLBHOuwr6mJ_vMYjUPjnvLnZJN6F7lVJiXmk-2LnEicy5a761bJi5kVWoSaeOcNeSXyt7wIw8LCRB2N4P3fFP9pV_LoSW09VFKRQNJfYwBHxn-1ABbFhNTBsVXltvqFNzTUGYO-1w25dHN_ofwumKOOhktIKC2DzZR0PdPFft_1PMA0fmh5zaXnX771yUNnXp51o84LzhSvn-C2EvPF7-ZJojdeZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30660fe341.mp4?token=o5BGEwPocMGJMSYs-4TfU9djvrUE-og8g-w5mOGjT6JgpyHKggv3v0wn19Vuomf5w-JpxeTNLCYyEycUi9Ruw-tZJdh-yirSeQkifx5ZUsEZCD7AEQAqHk3srDLBHOuwr6mJ_vMYjUPjnvLnZJN6F7lVJiXmk-2LnEicy5a761bJi5kVWoSaeOcNeSXyt7wIw8LCRB2N4P3fFP9pV_LoSW09VFKRQNJfYwBHxn-1ABbFhNTBsVXltvqFNzTUGYO-1w25dHN_ofwumKOOhktIKC2DzZR0PdPFft_1PMA0fmh5zaXnX771yUNnXp51o84LzhSvn-C2EvPF7-ZJojdeZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
على تاجرنيا: با والتر ماتزاری به دُمش رسیده بودیم اما پیام های داخلی برخی هواداران پرسپولیس باعث شد قراردادمان امضا نشود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107495" target="_blank">📅 16:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107494">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa385d1d9b.mp4?token=V1xfXswgiqp_QfGNBTt3W0eaWToDh9NqW68kQ4fhEhjYbjWOKbHoyeqElfWgAeNLEOyEthS2U3Ac95Fig9H-J_qjTEG6ukJiodEjbegnGbuYXupk5EOpNv3bQmh4aeezpJD6VKzfY8mvyUjvIV4j23uZZYsxlfXHxg69acL7i4mw5Krwd3-JMDiwN2_rH1LqhJ6x-y7_NgJZnC764HVMTS2lGBuzsdN-JowF05RvitESYEcIefZR9xFg_y58hjO7MVUr14d1sSZgZpw7aEzVUBsND1rCq9Ehhm8xkhLyp0GyaUEaFhMUUxzXEnpr8ffHexDs_LBllSJGjGU81Xu74g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa385d1d9b.mp4?token=V1xfXswgiqp_QfGNBTt3W0eaWToDh9NqW68kQ4fhEhjYbjWOKbHoyeqElfWgAeNLEOyEthS2U3Ac95Fig9H-J_qjTEG6ukJiodEjbegnGbuYXupk5EOpNv3bQmh4aeezpJD6VKzfY8mvyUjvIV4j23uZZYsxlfXHxg69acL7i4mw5Krwd3-JMDiwN2_rH1LqhJ6x-y7_NgJZnC764HVMTS2lGBuzsdN-JowF05RvitESYEcIefZR9xFg_y58hjO7MVUr14d1sSZgZpw7aEzVUBsND1rCq9Ehhm8xkhLyp0GyaUEaFhMUUxzXEnpr8ffHexDs_LBllSJGjGU81Xu74g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
وقتی امیرحسین‌قیاسی با چندین یوتیوبر مصاحبه و از درآمد عجیبشون سوال میپرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107494" target="_blank">📅 16:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107493">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b949da6c.mp4?token=pN755rUWM3zr3SlOTmoL5MJ4owzGJoeQWpIBQ6zVuNxbhb-w8lG5aHI25LGKkrgN1R-le2JKpEHJeUPLLOlb3mAG9DdtXVtY54V2IEdfg9jwFnc_W2xYxG0Vl_uzfk8fVmp0KWmSnuyR_LqvqwGR_CHw-zc4yD28H28E0xDRkFiDqTa3Ocm3fVMXoT-_MLm6-W3plP7LaTvb2bJ49-w_3iQLPhogHWMaHY2aGctOdRzf533USekwLVCTVrD_H8v0O0PEmrThPS30L3gcNzBonU5IzXsYWrHkWTVUMKzKE6HDZ-zW3FpAFR5VWpV8X69Vw58fCAKnHk6_UKOuJJLBJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b949da6c.mp4?token=pN755rUWM3zr3SlOTmoL5MJ4owzGJoeQWpIBQ6zVuNxbhb-w8lG5aHI25LGKkrgN1R-le2JKpEHJeUPLLOlb3mAG9DdtXVtY54V2IEdfg9jwFnc_W2xYxG0Vl_uzfk8fVmp0KWmSnuyR_LqvqwGR_CHw-zc4yD28H28E0xDRkFiDqTa3Ocm3fVMXoT-_MLm6-W3plP7LaTvb2bJ49-w_3iQLPhogHWMaHY2aGctOdRzf533USekwLVCTVrD_H8v0O0PEmrThPS30L3gcNzBonU5IzXsYWrHkWTVUMKzKE6HDZ-zW3FpAFR5VWpV8X69Vw58fCAKnHk6_UKOuJJLBJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
#
نوستالژی
؛ درگیری تاریخی علی‌دایی و محمود فکری درباره تیم‌ملی در دهه هشتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107493" target="_blank">📅 16:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107492">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3Mleo4DfDXX89t98F4081NSot_7xbbB0dKA_YINKVgXAcy1DNre09KMLn5VpzoLjcaXi4e-ftL60Gwu1c8Y7bmHCZviju5qiEvO82_4ElESv2ZoqzQ3QzCNNwTAF4FU4AUq7wUOXjBIMHGg-4EuiqHIgMQlgcRz4JVGiN5Twg-IaqxEJPcFKUt-dGbhcuouOAui_s3xNtgkKu9Xu2zyKvfH6KujNWhiDYOWMwH4XyKL94QtilFDnR8BjvIZtx0KTRy2i5DxWCMSwCs9UUJVKLXwYFBe6rwM1zbLTmcsOkO9D5Jp0xjn1-Sk4MKN32DYi6hKq3hQCBwEmM3QV5qM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
میزان دوندگی تیم‌های لالیگایی با رتبه فعلی آنها در جدول مسابقات این‌فصل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107492" target="_blank">📅 15:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107491">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بررسی پرونده فساد مالی منچسترسیتی به روایت دقیق رسول‌مجیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107491" target="_blank">📅 15:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107490">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚑
#فوووووری
؛ رافینیا در بازی امروز برزیل از ناحیه ران دچار مصدومیت شده و از زمین خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107490" target="_blank">📅 15:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107489">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11af8c0994.mp4?token=Saj_zYATdqFQZWmHFxSLWebPBltE0K1OClW69klM71q4VDC_XpdIrWHDt6Hw-0PnHYO1dfS7-lNXlQN5VmuJ9jeGuw7pY6DCsWR3Tjg0XiVOujbY8c2H8TwPz19Ls8Op6pLvJvUGW2m_JNOL3Qmp3PZOvbA-VH0pNkNTf8-t9c_X3IVBJqcsKnP9P8YrIIRJSwxNn1zazfPVN1JYt8AVhKEJAeI6R4OiG6hg2yN-2G0HhivVG1zkoDAOJ5ImvSeXxiPkkBn3HpyF7f8eXKrf-uvI7-JcDQ2uTJr11Bqr0hvpVfZqpNEm-qB4GeS9YOOnr5abYhbGK8OA03CIGskWB672c-t_lqI0kA_6sr_n9U-oTsa7EWmUzCmB5E7DAHfdRvV-zzVgo2rel-fk10z3QrCnZp6belAu06lw1JuPo_vv19l59JZII8DuBtEkxadMnW_Qw_zH1pFbVfOXOAli3d9cxhWdcihJ_6EgA11wEAF_rjXQI9EcBRu_T9ZKZFwFeE7zSX2q33F1_QegdNwW2XxVCJntclMxiQ7APrnGHXSqUpNT5m0CoOUhGf4A5X-hCk7Ye7jV4wEdBxsoj4oCkZcOLvKYp95h4EHPMtbApnGQ2uaHfzT8azCC5WAWpdk_48AiazLXsA7_Rc9YnMYGfz4Y_Hwcn7-R1T1RaiZAsPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11af8c0994.mp4?token=Saj_zYATdqFQZWmHFxSLWebPBltE0K1OClW69klM71q4VDC_XpdIrWHDt6Hw-0PnHYO1dfS7-lNXlQN5VmuJ9jeGuw7pY6DCsWR3Tjg0XiVOujbY8c2H8TwPz19Ls8Op6pLvJvUGW2m_JNOL3Qmp3PZOvbA-VH0pNkNTf8-t9c_X3IVBJqcsKnP9P8YrIIRJSwxNn1zazfPVN1JYt8AVhKEJAeI6R4OiG6hg2yN-2G0HhivVG1zkoDAOJ5ImvSeXxiPkkBn3HpyF7f8eXKrf-uvI7-JcDQ2uTJr11Bqr0hvpVfZqpNEm-qB4GeS9YOOnr5abYhbGK8OA03CIGskWB672c-t_lqI0kA_6sr_n9U-oTsa7EWmUzCmB5E7DAHfdRvV-zzVgo2rel-fk10z3QrCnZp6belAu06lw1JuPo_vv19l59JZII8DuBtEkxadMnW_Qw_zH1pFbVfOXOAli3d9cxhWdcihJ_6EgA11wEAF_rjXQI9EcBRu_T9ZKZFwFeE7zSX2q33F1_QegdNwW2XxVCJntclMxiQ7APrnGHXSqUpNT5m0CoOUhGf4A5X-hCk7Ye7jV4wEdBxsoj4oCkZcOLvKYp95h4EHPMtbApnGQ2uaHfzT8azCC5WAWpdk_48AiazLXsA7_Rc9YnMYGfz4Y_Hwcn7-R1T1RaiZAsPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
اگه‌یه فرد سیگاری هستی حتما این ویدیو رو ببین و برای دوستات بفرست؛ تاثیر مخرب سیگار روی سلامتی از زبان دکتر رهبری...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107489" target="_blank">📅 14:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107488">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd91aee857.mp4?token=NP7VNlhhgotxiiGLHBr3rk_u0PDOHyeT89zRmaWUi4zS5l4gdlaQmYuZnlWJ34yNfxPukR1as1r2mmFGzqc9FzqGAIH7LceQnZZGkHuRce51dL8YjIVxuteKVMQR8sRx8igkBejtDRjlfFJp1e4Xl2uxj3o_PU_DQhoilIQ5MlyAtmShTL3K7V88uVRQQaelZAik6PXVhFcT04kWnO1gGcZtuNox5Ta8T2iDXIqf3Ss6f4vD3o7djGR5OXcfhqZjcIxUWYCmkqNVglg6yfQ-dWKBlB1lrP7DaDnHWVqKXs7cIKCCsKilI8BrTnj9HkPP1SsOwyCtsyDOQEOLfht1hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd91aee857.mp4?token=NP7VNlhhgotxiiGLHBr3rk_u0PDOHyeT89zRmaWUi4zS5l4gdlaQmYuZnlWJ34yNfxPukR1as1r2mmFGzqc9FzqGAIH7LceQnZZGkHuRce51dL8YjIVxuteKVMQR8sRx8igkBejtDRjlfFJp1e4Xl2uxj3o_PU_DQhoilIQ5MlyAtmShTL3K7V88uVRQQaelZAik6PXVhFcT04kWnO1gGcZtuNox5Ta8T2iDXIqf3Ss6f4vD3o7djGR5OXcfhqZjcIxUWYCmkqNVglg6yfQ-dWKBlB1lrP7DaDnHWVqKXs7cIKCCsKilI8BrTnj9HkPP1SsOwyCtsyDOQEOLfht1hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇵🇹
پیام‌واضح ژسوس به رونالدو پس از نیمکت‌ نشینی در آخرین بازی پرتغال مقابل نروژ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107488" target="_blank">📅 14:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107487">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf450995b.mp4?token=X-UVSqQDdyLiBZW0z3j0_6lEYr1acCIC9_Do4nKvSovBrjD02Y90Vk5Xby5s8nct2egj4eeRJoV6SAymc26XF7ShKoT9B534_KCCUaDRuztLUPrbAyZcK0290_qEHA-JOJ0bpKKJRx5YyjvoJSk1q9psDAAoAym26BHuz5zv0CB8AdLaktI43CQAierltPC_rxTMp4_s_gIrvSLEMLg7tWInS7-kuqUyry75CHZhSyBpCdluKwF1BjMeNk9NbzxwwaQLiyEMmILXiuFiMWvsIuf8gIO5v-AKoSErePUa8M4ZonUKOMqwKOlq80kmjvvHfecv9TnvxNHGJVkJEpCPgw4HCZ28e4JYRiBAoxjpTBC3X7Lub58Cjr-skH3GcYYoVqRkuC0PP3p9qU_0edAe44eBVPIoaWvjVNTtqjUQJ8Ufe729yXoZbytSV1Y5I0WQbEmgD1t-4CB4ctzzUiiPOWHj1aZ2jFEDzvbBUEYzISNNGM4iiAHAZ5EDLv8Rb5AZlk0sHUQhdozMXQKKC-it_bfeWxRljfXp8uXeefnoLTCQQMi9TQfv2rHog0AYkpK9GGVhP0XcX_NiVlWv0cdRFPbC6CBlvnEgPYTg1Iq0qQ3R4VpMRHmxdTK2EpjOJ8ISqtzAgyJkfNhHPWYJ7hN_A1CMTxGj0d7LGfVZBmiV6AE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf450995b.mp4?token=X-UVSqQDdyLiBZW0z3j0_6lEYr1acCIC9_Do4nKvSovBrjD02Y90Vk5Xby5s8nct2egj4eeRJoV6SAymc26XF7ShKoT9B534_KCCUaDRuztLUPrbAyZcK0290_qEHA-JOJ0bpKKJRx5YyjvoJSk1q9psDAAoAym26BHuz5zv0CB8AdLaktI43CQAierltPC_rxTMp4_s_gIrvSLEMLg7tWInS7-kuqUyry75CHZhSyBpCdluKwF1BjMeNk9NbzxwwaQLiyEMmILXiuFiMWvsIuf8gIO5v-AKoSErePUa8M4ZonUKOMqwKOlq80kmjvvHfecv9TnvxNHGJVkJEpCPgw4HCZ28e4JYRiBAoxjpTBC3X7Lub58Cjr-skH3GcYYoVqRkuC0PP3p9qU_0edAe44eBVPIoaWvjVNTtqjUQJ8Ufe729yXoZbytSV1Y5I0WQbEmgD1t-4CB4ctzzUiiPOWHj1aZ2jFEDzvbBUEYzISNNGM4iiAHAZ5EDLv8Rb5AZlk0sHUQhdozMXQKKC-it_bfeWxRljfXp8uXeefnoLTCQQMi9TQfv2rHog0AYkpK9GGVhP0XcX_NiVlWv0cdRFPbC6CBlvnEgPYTg1Iq0qQ3R4VpMRHmxdTK2EpjOJ8ISqtzAgyJkfNhHPWYJ7hN_A1CMTxGj0d7LGfVZBmiV6AE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
دیس دکتر ابوطالب‌حسینی به دکتر بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107487" target="_blank">📅 14:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107486">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a02722eb.mp4?token=HLxL79a2foLC3_n0O5dYdCUSobd7MWgR1WEe2IbkPWMNgZgwe8zwCtHBqo25gRwknHppg-D006LXDdxdiG_BsOXcVLXhVYF6MQCdRauZtJcSMZARtv6qDW7wYm9QoZSIJo6XuFzX81tYmzZjRZXh2M5at1xvTqV8hCFIUuyKq7N6XhCfsYXjh94n79LAygNWY-oLmgqvG3AwEJhHkqZ172J44FJzrVluzrYLV_ZjQ7JPTF5IGAsTZG_sxvuHgJR3ig5_wZbvHnjSu3AdqzjWuMlKkAJDxuGeTnGJ7O0RVlNG4DoXwWnvNyxEeweuMpAY_EBshDbx0HPSUefaV0dVEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a02722eb.mp4?token=HLxL79a2foLC3_n0O5dYdCUSobd7MWgR1WEe2IbkPWMNgZgwe8zwCtHBqo25gRwknHppg-D006LXDdxdiG_BsOXcVLXhVYF6MQCdRauZtJcSMZARtv6qDW7wYm9QoZSIJo6XuFzX81tYmzZjRZXh2M5at1xvTqV8hCFIUuyKq7N6XhCfsYXjh94n79LAygNWY-oLmgqvG3AwEJhHkqZ172J44FJzrVluzrYLV_ZjQ7JPTF5IGAsTZG_sxvuHgJR3ig5_wZbvHnjSu3AdqzjWuMlKkAJDxuGeTnGJ7O0RVlNG4DoXwWnvNyxEeweuMpAY_EBshDbx0HPSUefaV0dVEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
عادل: ناکامی تیم ملی مثل داستان تورم شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107486" target="_blank">📅 13:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107485">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ee940a4.mp4?token=I5o963NI0Ua_PSb9ZmAKp3OMHWugTBlwp-tP6slGTOjkzB652_2SrINctLjBS-amT9yIquwFf609uv8yDLJwGXrPMYp0ExMfqH6E_is4wEZE4kewLfiLIwyD0tGE7uEqEiq2tr8Wg_YLQrunrbNCYCmFn7S6p6jMtof27Yr6KFvoyiAJghelsvQO9YY9N4zPGU0Y_xuw_vcOhnTFb6S9GdPSzbNiyrvRoxqHUtQ7RdahH-6YJcYZcu_cfAkdY8wExik-Dq8afw3N6vFRVuNlgzQgET-w45cmoE_oEZNRZn50PhlZGTMZhhT2vfEdK9_6xL4KqAhiwQTsGoxOD_U5fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ee940a4.mp4?token=I5o963NI0Ua_PSb9ZmAKp3OMHWugTBlwp-tP6slGTOjkzB652_2SrINctLjBS-amT9yIquwFf609uv8yDLJwGXrPMYp0ExMfqH6E_is4wEZE4kewLfiLIwyD0tGE7uEqEiq2tr8Wg_YLQrunrbNCYCmFn7S6p6jMtof27Yr6KFvoyiAJghelsvQO9YY9N4zPGU0Y_xuw_vcOhnTFb6S9GdPSzbNiyrvRoxqHUtQ7RdahH-6YJcYZcu_cfAkdY8wExik-Dq8afw3N6vFRVuNlgzQgET-w45cmoE_oEZNRZn50PhlZGTMZhhT2vfEdK9_6xL4KqAhiwQTsGoxOD_U5fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📱
پست‌جدید سعید صادقی بازیکن سابق پرسپولیس که خبر از ازدواج‌خود می‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107485" target="_blank">📅 13:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107484">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
نیکولاس‌سوله مدافع سابق بایرن و دورتمند این روزها مشغول دروازه‌بانی در لیگ‌های پایین آلمانه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107484" target="_blank">📅 13:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107483">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bf7aaba1.mp4?token=c2kZdS4vVqpMAvi50-9MLdluBNn6vvL5xAb4NfIMXseVxSypufTeNZZnx6vkVDiRkQWNRSm0mElaIlpX53YSr_8f_ah7aYuMvNl3RI9nO4t1-HMnc_EC3zZRgaPT3yRfN6HvqXfdYGjJr7FdPZxATxPN_rHQMuIHgyE8VIIpylXN70T8nfOKxDzj9ubR12oVB8bCjVATg4Xg-Lo7iGS1hXHRktrldkP9lmphcEsfY5-aNyMcXSkawK9fkEUwTRGCv-mpyuXl6mEd1OqZ4xke93eVlVM5dcccbRtcwZP4_q6rB277FpqH05EoD9eHBWcCbJSVe-xYO1QPVxjesF5bsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bf7aaba1.mp4?token=c2kZdS4vVqpMAvi50-9MLdluBNn6vvL5xAb4NfIMXseVxSypufTeNZZnx6vkVDiRkQWNRSm0mElaIlpX53YSr_8f_ah7aYuMvNl3RI9nO4t1-HMnc_EC3zZRgaPT3yRfN6HvqXfdYGjJr7FdPZxATxPN_rHQMuIHgyE8VIIpylXN70T8nfOKxDzj9ubR12oVB8bCjVATg4Xg-Lo7iGS1hXHRktrldkP9lmphcEsfY5-aNyMcXSkawK9fkEUwTRGCv-mpyuXl6mEd1OqZ4xke93eVlVM5dcccbRtcwZP4_q6rB277FpqH05EoD9eHBWcCbJSVe-xYO1QPVxjesF5bsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
وضعیت وینیسیوس در بازی با استرالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107483" target="_blank">📅 12:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107482">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgEBZbc0jyriS8H-iZC4QqGIomRFsqWusIQ2_aHWRcF2nMVlGBwa2hdq4A8pm7zlKBDp2s1gW521B0vaWJcyYOazgX1XN_WXr2_8poNYgsSM2AiE4P8h8QQUc0GjEHJp5FRP00Uqr6Y40afgXcLZb1ZOCAp8LWby-PXHQgwXs56BXfqg-gQvZTY4aws8o8SnYNbUi68kQuIvDarFQMgGLZm-Orv70ni5_MMXFvz_3OlASXADWEwQJOQwBC6HzDGTwlLUQjNT5GZ17tRMWD6ZLdpFvowTIKssDRY8pUvXuTQ-HF6krrPKeW_NC4z4WfuQS8vmP2zXs_hCLdILW3vDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
علیرضا بیرانوند به دلیل تاهل، داشتن دو فرزند و شش سال فعالیت مستمر در بسیج، ۱۵ ماه کسر از خدمت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107482" target="_blank">📅 12:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107481">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2592f7770.mp4?token=BFBhdyyrn97eyAHHeszev-uvmTi3qNjPMD3M6K5arFbd0I7rOhp2zF-pdSgr-7-Uk0gT2fjKjwpnbzXFRj-O8afqSHcV4UBsjPVQkKx8ysLFRqCm18h_BiG_e10Rs6I9oxWnfBwIou7Y17FNyQIAV5vNqm6MH5M82UfCXHGnMzCj7RllupG0nxfz5BqfqF2pYEv7R1brV1jlf7JWVYWTd9xUssBvnb3r4unTc1sautfjH-VKbv2x4Akw2tRdOjnMtZJf-XVWYE3LcsKclXX5Dkozn0lm9zsWGz8_FVonCEmiDPhKQ8bmsqYfCroAhoOM--XCr0LMHjkxUlhiqG98ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2592f7770.mp4?token=BFBhdyyrn97eyAHHeszev-uvmTi3qNjPMD3M6K5arFbd0I7rOhp2zF-pdSgr-7-Uk0gT2fjKjwpnbzXFRj-O8afqSHcV4UBsjPVQkKx8ysLFRqCm18h_BiG_e10Rs6I9oxWnfBwIou7Y17FNyQIAV5vNqm6MH5M82UfCXHGnMzCj7RllupG0nxfz5BqfqF2pYEv7R1brV1jlf7JWVYWTd9xUssBvnb3r4unTc1sautfjH-VKbv2x4Akw2tRdOjnMtZJf-XVWYE3LcsKclXX5Dkozn0lm9zsWGz8_FVonCEmiDPhKQ8bmsqYfCroAhoOM--XCr0LMHjkxUlhiqG98ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خاطره خنده‌دار امیرحسین صادقی از سوتی وحشتناک حنیف عمران‌زاده مدافع سابق استقلال وسط مکه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107481" target="_blank">📅 12:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107480">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW6qApJJbAJGkyyNR47qiMIFvHdtfr6e3xF4Hax5stsTTP_kMVRUkXLADcc94s1tXEi7J6WuKhl9YgXqJq5kf5UI16ntzzTdlFZEdjjL6-pTH7hSiKsrTtE7SRjDe91f3fnqJVk0UZ3XfnNzpZ74kCcX3KrEkJ7lrJUqn4xkXOAIYGwKv6NU2huqGYwb4XPob3HaJ96UhlTSuZGLTZCTHFiOeYII1NZ6gNRt-TH6JNevcBAs9grXjVi5qG3FyGmwBLIKa79kbrgn7i15ie3YEn8Ufo-IMN9mdBF7NOUY2_qj1KvzcY4qMBbjmAOgltBRIun8jt4C-Bsets2rOXU4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107480" target="_blank">📅 12:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=Y_QsoZx0vQv2ATbLDPb98BoOZqRJQdmxfNLw1juGc_2o72h6dHpx7DpXe92NGY4n4lrPXgl2uLzGSdJujTJPxBF3Vfsw63pg2PulpvDm9ZcNBBA0NQ_6AymdiVfDBAqcbYU25EhOB1nkoJRvqvupoc6NQ2r_wMu5l7ZsmixVx_QC41VRC5gOAnC3DQdmxp2DxrQADYAOf3_4U10vGllXjPv9aaFVcPlRUeCsxVG5UzVxj2GtE1xVTvtRLxDOaM_6oB0F7UEoVAkvBlsG2B1B7FQnCgHrADRo2aeGjK1hjH2GlV9Mypv5J6gkpjjRGO9qdf8F323PsW8uhYQiFyhtzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=Y_QsoZx0vQv2ATbLDPb98BoOZqRJQdmxfNLw1juGc_2o72h6dHpx7DpXe92NGY4n4lrPXgl2uLzGSdJujTJPxBF3Vfsw63pg2PulpvDm9ZcNBBA0NQ_6AymdiVfDBAqcbYU25EhOB1nkoJRvqvupoc6NQ2r_wMu5l7ZsmixVx_QC41VRC5gOAnC3DQdmxp2DxrQADYAOf3_4U10vGllXjPv9aaFVcPlRUeCsxVG5UzVxj2GtE1xVTvtRLxDOaM_6oB0F7UEoVAkvBlsG2B1B7FQnCgHrADRo2aeGjK1hjH2GlV9Mypv5J6gkpjjRGO9qdf8F323PsW8uhYQiFyhtzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
تشکر عادل فردوسی‌پور از ابوطالب‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107479" target="_blank">📅 11:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107478">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUIqycI0qehdjEGOgYp7ZXLM9g803YXDOEPTQZw35trDTkm3mDF8JufG5D0-vpn9MRWDWj31xI8ROoWyTdWnTuiPONEgoxHRHg8p-ESywKW2LxFXx_8JvzRtTVKx2bTMO47K7BQPSQdLI17xTgr1B95yRrbN_A3VQ-2Y9WTt9lfd96InHVm4ApmBe0LU01ewaCm-ePnkcaffO1tKcEtbaLAozcVEapVOrZQBTM1NX3F1I5e76NMMtOyov0dEVYYKvFexobxuU5ZDQAqzz-aReP_N_QQ_Pe6EVEYSfounMclCKg4FHalVfWDVBOVGMVvCBVZYPWrbH9B2iRo6--Ib9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
وضعیت دلار تا این لحظه: ۲۵۰ هزار تومان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107478" target="_blank">📅 11:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107477">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFQh1miMBdqSUXaWbzBZsfcPDl4UE4N4wdTYiFVWOAhhYoESIVz1EBuwfJKsIdAj8GrCwl1u5_MnxXt-_529SAdzY3T2-OIstP-RxKwOt1UoLVz4gDEzoo89jODnCh_w6RHTxy81KD6D71DAAN5XnK6cXq07-UPiuI-nyxXT4kpENKTs_EWRBLKGwuVTHEqKKAo5846ew_W2Hcl8L3hesL9qhyw_w5qf6C43OBz31yJn8cgRO6kpt879BJzNwHV_y2zQJwUvSDF4-oKxxYQKuaQ7AG_YCmeAzBvEpHUX6L0JAH51abK0GivqV4ASQbpH6jgwinXX13vGvv57jE-LtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
🇪🇸
مقایسه آمار رافینیا زیر نظر فلیک‌و ژاوی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107477" target="_blank">📅 11:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107476">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8Z9oqejTiNtWOEfkvcgeVo5Ws9oC-8n2MP5uxkURnzLL9fv5G8BzrHTj3GeyTZzvLA-_xeEhuH9HI-EUPN2egOwl5xaSQ-dUPMKW1a3WqT95MLREE_R55idtOAw2o98grz8fo5vkVaW-K_y5nkaebnkBzX8SaCAAvJUeh2PGz5k2AKnOs5XPfOuHMopR7Yg0OZEKdzX0LxG5DsqyYW5jfS8-TbOrYz9uC1XKQs8dONAEQIhMA6Bn7hCMAP3BSCvk7nVX-F8J6sHLpp7py8fDpaxjL_G5kaWfsv3ZRzN6VhNp5eGTt36YJz6gzGnIcd6R_-0BvxAet6_FEiP6iJY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
بازیکنانی با بیشترین گل‌زده از روی ضربه آزاد در تاریخ فوتبال؛ لیونل‌مسی تنها دو گل تا تاریخ‌سازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107476" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107475">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107475" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107475" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107474">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hlm81rfMtOGcQHKMPGYGyrks5XblUe8A-oKyLmiW2tGkO5VGiTYuC9aOXTXyMpKUHJDPG4NO5Az46hwB0rTsgrnsjM1DN6zbJHS648m3IuQ_hlP5ht2mquFKm1JXlHY8uggE7lUtO_gr_ojF4cnhAJ7aXF_id5ubQBwYqWr4TgLLtpSDI4f5W_UEs_XWvLJAjoThL_NQMD6kbHMuXRTXHhIc6s2FD4XfTx7qv9DNpVzSzD7hipXqFYxu0Oxk5jcTM6QCjUd_RJ9V2Hs3iUijfS4SnoVW3jLinIFxq3AwREcQ29t2S7yZI_OZAs5387rrye8jmwUJ-taP20GZkR3SIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
چک
کرواسی
🆚
اسپانیا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107474" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107473">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3862876082.mp4?token=dAFTRH3XrMGKWVP45jGLjTsao_Y26dNYMPFke9gRwqWJFVs3_n43CO32rxMQeGV4PdbkAsfOVuyMWbxGX2J8W2_nec9SqBrkaaxxrhoTLbnQ1myGW9cNMLys9ls85nvwO_I-mjMgWmM729s2KUFmA4cJXREi2fTfFEM3UKrgZgoW2-Fcj__Rr1H-T7qCiq70ncXYWqDk_tHXb6O5tGt9A6KOh3J_2AONddzBo3gzaZ-SvBgnD17iQdvPKHwv5wvsVefTB8rLYGtRDHcwLmPC_ZLQitcg2dR-eOiKY-St0u9GO_JLL_UDfPaNZj8mrEZExbtx-a85uBBVEyt8h2bY2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3862876082.mp4?token=dAFTRH3XrMGKWVP45jGLjTsao_Y26dNYMPFke9gRwqWJFVs3_n43CO32rxMQeGV4PdbkAsfOVuyMWbxGX2J8W2_nec9SqBrkaaxxrhoTLbnQ1myGW9cNMLys9ls85nvwO_I-mjMgWmM729s2KUFmA4cJXREi2fTfFEM3UKrgZgoW2-Fcj__Rr1H-T7qCiq70ncXYWqDk_tHXb6O5tGt9A6KOh3J_2AONddzBo3gzaZ-SvBgnD17iQdvPKHwv5wvsVefTB8rLYGtRDHcwLmPC_ZLQitcg2dR-eOiKY-St0u9GO_JLL_UDfPaNZj8mrEZExbtx-a85uBBVEyt8h2bY2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
انجام پدیکور فرشاد احمدزاده بازیکن فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107473" target="_blank">📅 11:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107472">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
‼️
⚠️
ضرب و شتم دو نوجوان سنندجی بدون گواهینامه توسط نیروی انتظامی که‌در فضای مجازی حسابی جنجالی شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107472" target="_blank">📅 10:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107471">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae822cab56.mp4?token=MN4untZZptX8CfUL-jWFdC3HkHdGwGd6jMMbOVYo-IgmbZk_uHSgd0WMkaLfJC8qolcm_h1C8kdIglSLTd7zXGC1jBeUnEtNNDml5CgiVBmtOpZAQpyKv1t_XAp6aSLeQxjR16asYv-gFAR-eHIA1f21m86x9zkLBHahqutqPZOsyUO7M_rOiORekJ30thNrWCI0FuTL0A_swcD0GlNrl6MZFieQknSX6SuNOL1-9ugYzD7iDJFLP4jR54SN2zWASZ-lvybP0kYW8chIp7wvRi_CN8fNQmmawg8VWRysju6QyqJE146sGWXNWyCpPqdjoIpTCH_SOhqdrR14PkHm3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae822cab56.mp4?token=MN4untZZptX8CfUL-jWFdC3HkHdGwGd6jMMbOVYo-IgmbZk_uHSgd0WMkaLfJC8qolcm_h1C8kdIglSLTd7zXGC1jBeUnEtNNDml5CgiVBmtOpZAQpyKv1t_XAp6aSLeQxjR16asYv-gFAR-eHIA1f21m86x9zkLBHahqutqPZOsyUO7M_rOiORekJ30thNrWCI0FuTL0A_swcD0GlNrl6MZFieQknSX6SuNOL1-9ugYzD7iDJFLP4jR54SN2zWASZ-lvybP0kYW8chIp7wvRi_CN8fNQmmawg8VWRysju6QyqJE146sGWXNWyCpPqdjoIpTCH_SOhqdrR14PkHm3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از عجیب‌ترین مصاحبه‌های امیرحسین قیاسی که پس از یکسال مجدد وایرال شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107471" target="_blank">📅 10:15 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
