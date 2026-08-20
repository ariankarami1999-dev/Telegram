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
<img src="https://cdn4.telesco.pe/file/fwAIGGuUyr19DpP8ZxXKagIbAw8cWsl44E5wdiTwfIFoE6r4hXv_9ik1Jq9BOwf91U-rCdLeWxF1je8Wr1UkYJGyYPvm96ffEujg3MJtBzoHofrl6--rOeLYKzv9TWLy5pcUFaJ2h4lWC8hRMeWuZ4FNpcZrWGbwqOenSTOntuggxezyUJtdTHI4FlTiyLRMvqVYXjT9VLnTh8UsVbfvomAC2C_KFsbJT3ySamGa1fTGtSzvihm5fWD5d5n2U1MTfMLxFcfxpYCnqzNfsbQBxIsOWxxyef5XG7WdLy4aSvy5nNnpt6BJ-gyyK4QM0EAOjKNlmuCnrLaIcJRLLEpp9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 622K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 13:56:18</div>
<hr>

<div class="tg-post" id="msg-28118">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbdUOf-nhNaW7NpStb7LbOFyoIa2Iy9MFqfd7ClQ5Jy3GgCmU-L7_tIABvYAwz7kel318FcleiKIBQucjID6aJ-GrjDIJ-qIBdDDfFIHgR4k4V5odDfjqsN1DzDAtAda68vlxA12OZLeov3JhGeaLaBEq_ZFXJOwUbjfEL8lnYzb8FJr4gp1VyCkg2WcIdYB-UJMTfpuqA53nvXKLJRX8XeJQ1DIGdrOWUPa5edr8993dOXGGRtVbP8zZIQaqQz373kYF4qWrsQLGtRWj8fYK8Sa5tHR4u-gS_yWrs5iM54DzXapAqldsUo_BJIAULVDPNqGvji7m3EucE_Km_aGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برای دومین هفته پیاپی؛ محمد حسین صادقی وینگرجوان‌سرخپوشان از لیست این تیم خط خورد. ابرقویی هم دیگر بازیکن خط خورده تیم تارتار بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/28118" target="_blank">📅 13:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28117">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsPRbhgKLs_BwvWPbq8uSiV4I-9YlBbdXW8JlVOzrRZVZyHtlMiiXXQL86PPBTot9eDklv1Ao-cCCn546LaaAn-iFZ8ehm0voRxVyrNXyyspDaRLp5e_y1KXcYDNyVR3n7dR9J8Q7H0nP9VWKtU0ojPGLPy5-57RbEC0GQG6AojI1r9g_i3idq01JVNsSweZlXvM5mOriXJAbOR5O-EyeMpBLuNCNiDtFujeNqhs3Q0GXlt5o_soAmeM3KRk2gejEFEI6lWY6gf2AzDGdDGg-DzXwulogY7ltwRYOApqiqecV4vQQfOkLU5TRhgWNJ0rgZFqYDjoXEJ-Nj358ieZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
یه لیست دیگه از بهترین و خفن ترین نرم افزار های هوش مصنوعی برای‌کارودرامد و تولید محتوا. سعی میکنیم که در کنار اخبار فوتبال چیزهای بدرد بخورم معرفی کنیم‌. با همون گوشی دستتون راحت میشه بهترین درآمد داشت فقط کافیه اراده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/28117" target="_blank">📅 13:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28116">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNoDOz0W6PPMYVAQ8SajoH7YtmXLmExZvNHEvCcjiB-4GqvTw4rMzm7CtMyQN7GuyvJwXyZGjuTus4ksOku9PrzxXkk_jnduHWO29eL8_8pr-wObETyaBTVqrXSRQLFWoPu_kI0ZtsbiAoDd8OrHCRdUhMjeCV4a3kFx2ww53i4GXTW0mG7FvBwpdfNYt_TblqgkTL_U2nQbbyVNcaULwenjs9JA_Ck8EB3X5pqgxwfgFxb3vERoSkSnxpVm6UGpQWj9bnSifsKJ4GvE_Ss22SRFawgYaUYHPKDbjMRvFGvEnyfbhvwzss7ZCFrD4ZjAlO7gsY6KebHr62YC0vwOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جورجینا همسرکریستیانو رونالدو این رو استوری کرده و نوشته تغذیه مورد علاقه‌ من برای صبحونه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/28116" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28115">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g01WZOgJ1rIAwgAlNgkfOGvJxqXgfygZG-_k74IYrhFd8UHiVoAox5QC8ScGU9SxOpDsR10wukpffpsZGKiiaOO_xZ4ayXv072AcQ02r_70SpMTQXac2GzhPvDm7o_brR523K5NHCOi-iTLMBzEUUvu4QTgilglYn-0M5Etyyy6d5E1lN3DoaucvmzeJ7jiE6p-Yb1CpnurnoL4b8VlnvCcNjdg9nzYHvQjnk4Zwccb079FcTkdASD0EJA5ksJcmpq7DXMeb-WtcvRoMsPd1aCGeUyyiJHojtC4drNlFxYarAtv-Syhwg-U2nBN6OAx8brayxib0Xahrl29fc8v0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
رونمایی از کیت سوم خوشکل بایرن مونیخ برای فصل جدید در تمامی رقابت‌های بوندسلیگا و UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/28115" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28114">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiUrdqfPDIe84qsj4U6fj_HK0q0UPqdBVeK9iWu2maBeYdHXeImC3UdT9Uv0GaSOZK9pUztWSx4Ki5h9J0W-aGUwbdHcq8SNB7Rc80DDEMZBZ2vJjZGEXnoGDJirZeFgIYglKFzvk3S_IakTQ-S2CuSp0vBTE7cc4UZgH_oAVXm7Ryd_n-WEsMV8Fl1j6G7Z3OEfImsnqVdnrnPN6AC6p8V5xfP0M6crtNIgkOqNMkNqb7yDN3dmHsFHm11UnoKKEwW2PL3Jmp2UzdnlJfcS9fBAN5q6daqQxInoQWdFzatjvxWB3ZSdj54kHT1kBM95G4FjA5GEocEIULI95Rmf3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به‌دنیای‌پیش‌بینی‌فوتبال و کازینو با LINEBET خوش آمدید
.
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://t.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/28114" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28113">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyBqobLlAlIdWqYbEmDQZVYdw8Mf8as8MJ0sYLGKetfLaUuz-g1MLXjsGPBAF90WtFTb9CEN4J_LP3cvlXk251IuRZWEOMz7bcbSe5igDUExOhEbySL66M7kpXkn5y2Sv5A1d21SkKIqtC_LiZn_6DNy4rq_12BpUtnwdtodQIIha09ul_PP54ToMBIWQZwbCUNC3jJ-6-s1i_-ARxho7rq3Y9W4MVkzEYbzAHwUR7gUkvmC91HPfpl-ffcySLt_NC4GxWuUJOO0FHnfiWE0H57n4SbKEZ7hTiPh7A9Thk2nyy658hgDzIpvOHPY1-sSq-NRVQR5oNNTfbaKOsBuKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی:
پدر رونالدینیو وقتی‌پسرش تازه داشت بزرگ میشد و دوسالش شده بود،تو برزیل با یه باند خلافکاری‌درگیرمیشه اوناهم با یه اتوبوس از روی پدرش رد میشن طوری که جنازش به زمین بچسبه. با تموم این‌مصیبت‌ها رونالدینیو به یکی از بهترین تاریخ فوتبال تبدیل شد و لقب‌شاعرفوتبال‌رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/28113" target="_blank">📅 12:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKrkyr1dFKg70Wgwy3bx28JH0gD2r33CtFi5yKCc_ZmP0_i2arA7WtLNA648xZFidMVTHl_xM0FvDHU5tJgJkvuojuqQzm84vfdlZA0l0L8PxzgmTa_OQBkKOONElFzVzoB358O34pfwzrzNmNq0cVRRlOxxAmEt_08JS7j08rj6_DR0rpBUuGcy1yVUNYWE-Pv-ONKg7j1tHZtZmPMP7EZcR2uGJdsTIc801ou8Vlvhdc9P820Rc6cxo2CmtNm2OZbQVaHLlEpCsWjNeNswsTQhzb-GYaGa_VAb6evFJJnU8-rgvBNmxEKE6QT25iq-WDp2zZBEIxXXkPjkHfmGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیداسماعیلی بازیکن‌فصل‌گذشته فجر سپاسی شیراز باامضای‌قراردادی رسمی به ذوب آهن پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/28112" target="_blank">📅 11:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En-UQpOD9x9od4J7EzkRo-zKp9I_EPl5hWrIuqgeR2wH4C_WlF5E385w8PvP1pRCkvTNCbONStE-vBhdwBV5s-Lf18vK_JjI8TAjb7kFdp-As7j2F5P9w6UyBDdFYN4jL0N2dG5S7N3LrGm2l8nT2uo8DidZaajdmt5rQnHIcs0pEUFvsycKneLr0hOPdUO3ytc2MQrs4u79bGvfci2JcNtzYwp9Q7t7lBHsDIUjrt5kJ3VdIlCyDx38UDJtykRhl3t4LYm_u6PxHQTa3FfBlDVwM2SCIrZoMT_RMSuX1D5G3Ea4fN9GfTw4zpMFyBtftdH1m6LYrgzPb6jOjTeQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
نشریه‌موندو: مونیر الحدادی در آستانه فسخ قرارداد بااستقلال تهران و بازگشت به فوتبال اسپانیا است. مقصد مونیر احتمالا تیم آلباسته خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/28111" target="_blank">📅 11:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNIu-TiHZFPbVymscTAfw39AsAXE3lxXhpA0a_8DHzl7HzFGjRUpJWmr_GCRg8Z0sABpSF_ycWXpXHo-KeNNsSl9QSfE1aT0jcyR8kXA_-PfqAI_y-4k9i224J6G8yP3LSkaScMp0asMIf5oRkLam4sH1JCm6_1wUz0PD8jpZE1V6h3Ito9IJ4qSyfRO3kPZenXYjKDRag77pKu7BQbelHDEpMSvo8o3_TxpjCkoLaIEQJNb1ne_fNb84fXtE_-dls44onGrsP_siMgepSq_OIXvvZCzhf44QSa24u9-K99UzZfxzZM4zr5Cx-7J198tsqUzAwbQd-S4swtPhIzoRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/28110" target="_blank">📅 10:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🥅
کارشناسی‌داوری‌دیداراستقلال - نساجی، سپاهان - تراکتور و دیداردوتیم‌پرسپولیس - استقلال خوزستان توسط مارک کلاتنبرگ داور سابق لیگ جزیزه.
‼️
طبق گفته مارک کلاتنبرگ: گل تیم فوتبال استقلال خوزستان به خاطر اینکه مهاجم در آفساید بود و مانع رسیدن مدافع پرسپولیس به توپ میشه آفسایده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/28109" target="_blank">📅 10:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f4df3199.mp4?token=miJZ4IOzwUXUeXeMnSVRhXWdwkIAs-AA-8Qk03ypcbsm9EPtIJOwQl6CNVoXibe6P_SY_mqHl1dvoggBf9ECT38m0K_RGUt9BLn2k_rLqcCXaeqwLhTnGAKkbUP44ckw_jbOGFGXepXE4ng_fXOOjdKmTc-Wh24ABR4_D_xlZGHKLBtdAW8SQbi-aijjgYtfAbWQoEwi_CgBB0hGFCMkATQRNQJ2L3XdVAEwrtJQakjP59LnukzfVZNjN8nzZUk8PwWcyNaeVqYfpGutlIIYxFgSEpZ5uDBpAdqYk3IyzsBHakhcmwfyOrfsxfAmJBnqbRol3Qfir3YYdUQkuSGemA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f4df3199.mp4?token=miJZ4IOzwUXUeXeMnSVRhXWdwkIAs-AA-8Qk03ypcbsm9EPtIJOwQl6CNVoXibe6P_SY_mqHl1dvoggBf9ECT38m0K_RGUt9BLn2k_rLqcCXaeqwLhTnGAKkbUP44ckw_jbOGFGXepXE4ng_fXOOjdKmTc-Wh24ABR4_D_xlZGHKLBtdAW8SQbi-aijjgYtfAbWQoEwi_CgBB0hGFCMkATQRNQJ2L3XdVAEwrtJQakjP59LnukzfVZNjN8nzZUk8PwWcyNaeVqYfpGutlIIYxFgSEpZ5uDBpAdqYk3IyzsBHakhcmwfyOrfsxfAmJBnqbRol3Qfir3YYdUQkuSGemA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
تاکتیک تارتتا دربازی شب‌گذشته پرسپولیس روی گل‌سوم و چهارم سرخ‌ها به استقلال خوزستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/28108" target="_blank">📅 10:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e9ad128d.mp4?token=EKiXlZY4TS6ROp4YeBxDsxkhOpSFaXLE_cVxml-mm6DP4vS3K452b8WuYRI_0DtZcSBJicxjjULBeQWAxAWA5HhOZhLB-n9Y9HJE7SuOC_Y9ah426nnMEQRCPvHmFto0H0ZteOlOHo3tgfW1yzTkZ7gONoBcmqEGxLU2SRWFwJgOlYLBuA6J7jjHYx5EgwLX2dDqcL4WKbYZAytQ-7KIG6rN7j-K87ewh2soQ59HQ8jkw85XlwTM_rxbujkMxIratsEz9txXYgqxkQnS5f2uZ1s78JeZibf7Hyx-5NsyTmwdULU9dZ5N1TgqJhxU63wtGDiR4yHvjpAQf_0BXBhGxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e9ad128d.mp4?token=EKiXlZY4TS6ROp4YeBxDsxkhOpSFaXLE_cVxml-mm6DP4vS3K452b8WuYRI_0DtZcSBJicxjjULBeQWAxAWA5HhOZhLB-n9Y9HJE7SuOC_Y9ah426nnMEQRCPvHmFto0H0ZteOlOHo3tgfW1yzTkZ7gONoBcmqEGxLU2SRWFwJgOlYLBuA6J7jjHYx5EgwLX2dDqcL4WKbYZAytQ-7KIG6rN7j-K87ewh2soQ59HQ8jkw85XlwTM_rxbujkMxIratsEz9txXYgqxkQnS5f2uZ1s78JeZibf7Hyx-5NsyTmwdULU9dZ5N1TgqJhxU63wtGDiR4yHvjpAQf_0BXBhGxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فینال جام‌ خوان‌ گامپر؛ قهرمانی آبی اناری‌ها مقابل الاهلی مصر بادرخشش‌ستاره‌های تازه وارد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/28107" target="_blank">📅 09:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d55041935.mp4?token=ATtz7O0kKmNRzMQQ9o--2vc9Fas8H8MMc0pBOLIdc2P5DGFnVqsNGq4lJwOdCo1MxrdAiHGPJYCp4AMFEhR-6_VL9G-ShR6OL18fF4WViouCcQLpgXDdQIBjFU_CfAymbLFKYYyjJBrS32S86vXcWwY8NisAvcEdCPSRr5OnnZShDwpiNq30AohLVIjrqx5z0KklN9owMinrA6-fC10FoqD9TBsFWvHAjNSCTmtHcEDinAmRaYkyXbConKLb6yhE4t6QJQcikwj2EehhklzFmh5zcC1M5kiNhsNRVCBZ4pJJilM1fW68LghzvjGsZl52MSOUPJiDE7A46Lbgs4ApMyd_ikLlFruN6U3WIPdZ6ohTewzJb2zR5EL_kq11txBWriJFr98vEJkyOxTWmJFtOjhxrY19xlwMScH0-z6Y0jsgwg2otZZ7kWfKKY6TBdIoXye5PINMEsBLGnVsFiJJcmpr1ufzJTe7LpBFPq9ebFxwpYLt5-mK7oW1nrsGR1fNHgTDzAao2o0S0anExy85gEjNU7no6Wd13eL_tgB_glbmyYigH0qb02szfv-P_-PiK4SDGT3EH_gTdcJl8MzHuNIyzCyyDEzMnea7Obh-ZzNYjTD7ibqtkJro5Zkstec5wYyHW-IzAyMJ7g-bTCTuPhMiZsVLLbi3l2sQr2hpo0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d55041935.mp4?token=ATtz7O0kKmNRzMQQ9o--2vc9Fas8H8MMc0pBOLIdc2P5DGFnVqsNGq4lJwOdCo1MxrdAiHGPJYCp4AMFEhR-6_VL9G-ShR6OL18fF4WViouCcQLpgXDdQIBjFU_CfAymbLFKYYyjJBrS32S86vXcWwY8NisAvcEdCPSRr5OnnZShDwpiNq30AohLVIjrqx5z0KklN9owMinrA6-fC10FoqD9TBsFWvHAjNSCTmtHcEDinAmRaYkyXbConKLb6yhE4t6QJQcikwj2EehhklzFmh5zcC1M5kiNhsNRVCBZ4pJJilM1fW68LghzvjGsZl52MSOUPJiDE7A46Lbgs4ApMyd_ikLlFruN6U3WIPdZ6ohTewzJb2zR5EL_kq11txBWriJFr98vEJkyOxTWmJFtOjhxrY19xlwMScH0-z6Y0jsgwg2otZZ7kWfKKY6TBdIoXye5PINMEsBLGnVsFiJJcmpr1ufzJTe7LpBFPq9ebFxwpYLt5-mK7oW1nrsGR1fNHgTDzAao2o0S0anExy85gEjNU7no6Wd13eL_tgB_glbmyYigH0qb02szfv-P_-PiK4SDGT3EH_gTdcJl8MzHuNIyzCyyDEzMnea7Obh-ZzNYjTD7ibqtkJro5Zkstec5wYyHW-IzAyMJ7g-bTCTuPhMiZsVLLbi3l2sQr2hpo0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
#تکمیلی؛ لیونل مسی در بازی بامداد امروز اینترمیامی برای سومین بار دراین مدت کوتاه پنالتی خراب کرد. سطح‌گلر اینترمیامی روهم ببینید عالیه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/28106" target="_blank">📅 09:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53707ca2c.mp4?token=J7IM-eDHKK2o7i8udp4AFEatuXXFvdiFvjsF4ryYUTtUVSk80jN5UCiyt-vwdeTv4Mvbr_Sm5EPurEUgoxVvMlFSk2OcAUOMxhcILhvv8xmCik1s4jox7RFcVutf2-MvX-uOnDNcGg-pEGosnzgX2HRLDk44GGUPNVPstazMNbOAT3Y-QhH_bQizOjVh0srQgi1Ip8IaLKVMDUg9cWsDt3gE5XvRABb7-8J5qKNdPXrb0hkT8uBzqdhKZdj72DHgueuaDqto3QYhbQkHbqVc3bvLW63rr73Xn9VhoOp8CDySG6kH4e9kO4T8EV_tmHrhonGbyD53EDQFFMz3xB9ZSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53707ca2c.mp4?token=J7IM-eDHKK2o7i8udp4AFEatuXXFvdiFvjsF4ryYUTtUVSk80jN5UCiyt-vwdeTv4Mvbr_Sm5EPurEUgoxVvMlFSk2OcAUOMxhcILhvv8xmCik1s4jox7RFcVutf2-MvX-uOnDNcGg-pEGosnzgX2HRLDk44GGUPNVPstazMNbOAT3Y-QhH_bQizOjVh0srQgi1Ip8IaLKVMDUg9cWsDt3gE5XvRABb7-8J5qKNdPXrb0hkT8uBzqdhKZdj72DHgueuaDqto3QYhbQkHbqVc3bvLW63rr73Xn9VhoOp8CDySG6kH4e9kO4T8EV_tmHrhonGbyD53EDQFFMz3xB9ZSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نون‌بیارکباب‌وسط‌برنامه؛ اونجایی که السا فیروز آذر گفت میای کار داشت به جای باریک میکشید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/28105" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUEIFeareoJMEs38Fq5jR0vE-n4H3iy1zm1vacTAh-JYqMcirZpwhRmmRuXXWrCOR_I8gytDx9C9k6lGl7Mik65hEG5emNG77JzhrOFR80MEAT9F5LEXH3h_ty0RHae1x_lwJ1GoSVE2rAA7MjizUb5D_1ZE8bhBK9xU42zN4I238oNbAV_giAc8KfJYa0C7IwN-jr4FmcjZdbgsD-teq17ll5wpmGbc57_Q2LQrijqlzpmE2Kfix2UzKUdA15dnJLkYgu6m8RMOEEVeR_2NmlnUW-1GBoq_w7wXCb10TqghKHUYaDtPij8RQf5kYA3TAdGkrUvk0RkLWLLZ5zudVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار دیدار پرسپولیس
🆚
اس. خوزستان از نگاه ورزش سه؛ آمار متریکا آخر شب میاد اونم میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/28104" target="_blank">📅 09:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAqMuED6mawyiwjTJNVtAevWj5Snmt8zbSsg0NgzhPc9YLf1pXs8E7QHNChP_mOH99ETv3mbJ0D4_CldmYXu5VgnCcFV5dGrVmU0NiwyqyQ9UhlZi3Mn8YznRJF9-8W3Wq7odndCLvdR7U5APLiaY1lm9d0ULs1a-TLcQbNcnsCvxdqFoP6zKTzt15zQT3TlmnvfcqpIdBLzo25ky3J3gFGCriBvu0jA7m-t6s6lRix7Zr97kizEnHEFLA0bJoQyYpXZVmmUu3C8_oPGO7oqs2fnM67Xqr2-n92obuigzo_DD0xWbdYJ64PbFqmrcNvuIXAwQpIB0Aos5zeuTE7OZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی هاشم نژاد دیگر ستاره پرشورها نیز به دلیل مصدومیت دیدار با سپاهان در هفته دوم و دیدار با پرسپولیس در هفته‌سوم رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28103" target="_blank">📅 01:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca4590fc2.mp4?token=ohuzu_mtsiCTfgrGp0UwIZVJ00S5aHKkUx23q0QGRd51Oh2B1KisrRy21ltucav3gAm0X_U4SHYL8u-hY4-rg6ZS1iE9g9ihcbM70uO6q4OdmdMQHdwRZEW4DkBUBHT4HWl9mj6M-t6ZtyGis__8o6GJU1gmnMs0WVi41ENH7KPdg9GW77O_eWcREeipcuvcrVc5flj48DZrUXfI51Fqa0_UGl9p4Xu8TKdqQEnyQLXesMyCiYrzd5cXEgRx2SokoVE_cmCDCII8hTLbj3y_V3vwJciJSgxeXGL1Mn16gS8Y6IILk__oc_NKoRIlK0Be4nw-EXW9u8T7XM5_TuBeXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca4590fc2.mp4?token=ohuzu_mtsiCTfgrGp0UwIZVJ00S5aHKkUx23q0QGRd51Oh2B1KisrRy21ltucav3gAm0X_U4SHYL8u-hY4-rg6ZS1iE9g9ihcbM70uO6q4OdmdMQHdwRZEW4DkBUBHT4HWl9mj6M-t6ZtyGis__8o6GJU1gmnMs0WVi41ENH7KPdg9GW77O_eWcREeipcuvcrVc5flj48DZrUXfI51Fqa0_UGl9p4Xu8TKdqQEnyQLXesMyCiYrzd5cXEgRx2SokoVE_cmCDCII8hTLbj3y_V3vwJciJSgxeXGL1Mn16gS8Y6IILk__oc_NKoRIlK0Be4nw-EXW9u8T7XM5_TuBeXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری از لحظه به ثمر رسیدن گل تیم استقلال خوزستان که نشون میده توپ کامل از خط دروازه عبور کرده و گل بدرستی به ثمر رسیده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28102" target="_blank">📅 01:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28101">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quM9qGlhsF__RFfoWsUthsc0D6FwmniM6ECJcB5vEwWS-EFaKyT0YU1wqmwiOz8b3QLXZEqI0rw5_d5tVX9B2sYB18prfEHvry2rXSnO6CjhrZTCA8Fmj5DMwnoLnjD1xLjRaZsIxPtIEG8SWyV9cFqKomplob1yf3b7fc0HzrN4j4d1j-UKAXVPZVi2niqfikNJp5BJ9PuxBFQfAkk6HfGLt4-f0P4MKDw92Wa7uE7ansifyuQf_jVnv2RgjqSdk_QxSvGLmj1mO6NoCLMg9EbkeF0dWdx0ErgKTA6YO2DPV1u0LHmqafvmIOGyxfKBFI4hQMYUlcX-L5fYLIdSjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف اینترمیامی با تیم قعرجدولی تا بازی‌ اللهیار در دور نهایی پلی‌اف اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28101" target="_blank">📅 01:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28100">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCFmfP-pKdvXg5FUT8BadqKYfn4rGm1C4KsDLwkVSPg5xwKaU0lgSHPPRWHgwGLLpXflJ34n04OtepcRObEFa9lbFSXDGyOwSLf0nB44NO_zvV6R23FjnArPwF7YwnzVcUrTyDa5Dcj_f9DvV_W_xGlSKiBHlry8eoxo-rbikDSzPZDiK4Dm2NbsIEnNiAw7Zc9a-iFMekdXpdf00sAZQilrZEBaao051I-H_hVUPKa5N8Qf2cRj3Te99HqUq7pJLJWinakjdym5xulh0siuq-IPr1WtxDiubQEJ_QtgnaWfdU9ttX-V4AHBbXeU5x3ZOMnloY4vt3368Ic33RRKIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌ دیروز؛
برتری چهارگله سرخ ها با درخشش علیپور و قهرمانی بارسا درجام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28100" target="_blank">📅 01:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E67hCpL1OYWk7YtaO3BstVMAlBCnSHtE71MFcvV5Cr4B_MQbEeDZYECKWUmVrrTXgmTPFmoI2wAPYYORoOY1Qg5o7PCzxp4IXxbayJfGK0eY2RNcq7zFjTf3PomKlQopY3hJQKAtqqc5_0l1jTFXOcp_8tjiYVqrFxbibWrG0rhMO4DG1yZg4SBwMxntcujbVcAfehcD53MZh2plSEcED9aae5CX6SMePtDjsGoZS3vP2hk4-SXLvIoVrYeeNfWf1OyQzSrmlSbbIYFvkfxqmmj2WGgBkEdeiuHuEp6uwiaF9A_Bux37gqUbIEYaFy-112-wuAIjVLEb8zHeRYnhLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
2.5 میلیون شارژ کن 10 میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای 3  واریز اول در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
درگاه اختصاصی برای کاربران
💰
✅
پخش زنده ی تمام مسابقات
🔊
اپلیکیشن وینرو
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sa28
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28099" target="_blank">📅 01:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28098">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjP0uqHIfvm_k3YZ4jU1QIfxbUWY6Fm8v4NWlNVDKseTAiU99FYqQ7gN-TTcOgfBJTYswBuWAaGMz3yq2XM-03eE_2rZX7rO_2mzAUReUDi_u9JsmKFmyU52CLs69UgyVpjWHJT5tDI3fGpKGGamF0GdbnHoK75liyCMchaDdLz6NX6p5a9oNXTL3dwGnx3akC2SQPAtnG80YivUIOPTwltBg39M_FFum3PfLrDd9UcMcZAp1gqfUGmPyC6BOu8vJepR_PB-hN68uy7H0W_1V-nOM3Ud6k83hk_weEYKX2mdLyRXXF1yWvjl5hfVolUgWgUGeleyI_HnwRIjvOctKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کلین شیت نیازمند در دومین بازی خراب شد! گل اول اس. خوزستان به پرسپولیس در دقیقه 64 بازی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28098" target="_blank">📅 01:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28097">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01c23a6de2.mp4?token=VijI1OLXVNBJEsay7WVVCCwQH-cUBAbvxOCbaIS2OTcUZZM0istQo0Lo59liNNi-MoLNs3bG6mX7f4uK042oenv-XKWS8H9t2FD3Xgl3d-BPMtYa5BRl_TqynMmmaAYMuZuriNx9oon8jbY1kq1X-tnjML7h0K6kmRKblwkOtB2jnqxlQUidWmJDfVPFDqnqjFJY47hVoj87zeDIkRxpm2Y1hvXLG41KIIRriCW-fy6E6abK7V0mQGcnuwbLCt0vYw_XaXSw1drItS2MKqOEciUBlp-vURoH0_9N8e8qSE-l6z7pt2_6Mk4s9PSSSUnYJoc3WwGWUWAqGRfWr_2fFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01c23a6de2.mp4?token=VijI1OLXVNBJEsay7WVVCCwQH-cUBAbvxOCbaIS2OTcUZZM0istQo0Lo59liNNi-MoLNs3bG6mX7f4uK042oenv-XKWS8H9t2FD3Xgl3d-BPMtYa5BRl_TqynMmmaAYMuZuriNx9oon8jbY1kq1X-tnjML7h0K6kmRKblwkOtB2jnqxlQUidWmJDfVPFDqnqjFJY47hVoj87zeDIkRxpm2Y1hvXLG41KIIRriCW-fy6E6abK7V0mQGcnuwbLCt0vYw_XaXSw1drItS2MKqOEciUBlp-vURoH0_9N8e8qSE-l6z7pt2_6Mk4s9PSSSUnYJoc3WwGWUWAqGRfWr_2fFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی همین دو هفته پیش یک میلیون دلار پاداش از فدراسیون گرفته. جدیدا هم رفته یه رستوران که غذاهاش‌روتبلیغ‌کنه‌که یه مبلغ هنگفت هم گرفته. بعدشم میگه‌خدا با من ناسازگاری داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28097" target="_blank">📅 00:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28096">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKSRZXckm-arp6z8pONvhmeCejdOHMAEkVPURBj0hXeGQN7deW0zHpwuIsPlvrJPa_0Y7B5l5T4zo6jPTE0fD2QE6b-qeXQzWmFKInz0iU4kf_mOEpaSXF1u0tVud3I0CEcOiWZ7V5n6VLAvb7idHfyNB8iPNEj5s4i2zwzJkmtS_wS3Fph_5eImPIGrS3mjJEs9jQP6TW__1_i4dZAnjkskJyBSHalJvNOWNdnm3eT0-j0cUzAySEEAqrgpg0G8PBJ7MWayRKlkpMdZCp4scj9kjVBPq_GFXWVrlEZtigxdNUHg0-xm71204CZ7TuTOzMWN2Dup87mDOaUCT_VhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه الوحده بعدازچندروز امروز رسما تخفیفی 200 هزار دلاری به باشگاه‌پرسپولیس‌داده و بمدیربرنامه‌های قربانی اعلام کرده درصورتیکه باشگاه ایرانی یک میلیون دلار به ما پرداخت کنه رضایت نامه قربانی رو صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28096" target="_blank">📅 00:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28095">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggXebtuFP4R7CCYpNyRdTKFVsQrx8G_FasncFwIFkI3JKMlMNWiLa_7qJCt8MYXN6YOEUiDK_2g4A80WPOBnHyXKYshQjonoLuh1LTQN8ba2L0uRxQeKliLKGqp82-dcrFcwWTZITRmeI86EIKZ_NYgmjfMqE_qHaCseU8MJYxu7c4DZq7nhqRxAL-3QOSHKXkhg7Rt_vyKFfpO8yNq88mG4KVpyZkDt7_twRLk1gjKI5lOwoeUTeb2NzBPOkQqE3DstJKRcny56PWg9PQRi3lpGBAZHYAYs1O0u92XkNaZrfP0D7-5_1FHzwZ8hQiJXeM3YypP6-nwtvsKlM3ljRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛به‌احتمال‌فراوانAFC ورزشگاه السد رو میزبان مسابقات آسیایی استقلال انتخاب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28095" target="_blank">📅 23:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28094">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukXEjKXNlz0LGtmgDB8Xhsv2Zr9t49hBonTWM0I5JSOjlG7ngTAoDfu024Y2ww5KcCrTdrzVVoexQWswSw6ReAqsrtmOaE3yaCyjeyd3QRpBHBGPB1IwdXqFdUFyleZ37ro77sddO-Ydh5DotRIY6eu7o-q2P2oa7k4POmV-p_dGmK_o3GPFl5VBIOpnQRJP1z1a-R6cNSMqu15WtruX-cBngQ2rSrGuknxJsTH4WPAmYgB58HmEsIgfxwaOFV_UBal5N1cg5DHJ05z5wOP-p3sb4BZdzwROVRmzUso1G-YmOy4MdDNiwmNQa7m23IqJ4FlaekzXtlN33tiMZf2zYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛جدال‌پرسپولیس با آبی‌های خوزستان و مصاف‌بارسا و الاهلی در جام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28094" target="_blank">📅 23:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28093">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5ACEDrBs9rM_FC7d3LCJRZDAAlQ7Xlvt7XcDibXRzpzzMiMy6781gQgXTf7er_I3Izsx2B2uxjHBPE0tWbktKEIeSG87oNGByQcuy7W3FkWueV45cplII8pCNEgKFs-jdLOZXT4g29o5oBr8KwRaodPfGEcJYIEJtlMonavrv_3goQDaBEWhghzc8LaHkIIN3zm2JKHbcC8FBlMeCr8JB4we16znRyDKNMOg5bmFvJkikrdWS9NqAShtGuoNGvEMrqroE6V_F8IyDbsqxsr7r739EpqRdiI2gXIw8O-YsalVO73BpPenygJqVCYzWc8MYHlwsmaShE-t8E04qQyAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نتایج محرم نوید کیا سرمربی سپاهان مقابل تیم های بررگ فوتبال ایران: 6 مسابقه، 6 شکست تلخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28093" target="_blank">📅 23:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28092">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vs0npl76X5TBBXNNYvc3d-f6LzQS5MAz5H_T1YCI_aYSD6GIAqhCblNrCHY3Vc0Nlu6TBpZdMyG_VQFKFy9fuxxVHuwpAHYMuFz_ylklxEtpZyIavWpGnGG1otip2TJ7g1Hrukjf3sFJe8HUEeJ8jm4-QOFow6-29HdjQhMF3A5Jpgy8tkx8GO3Y6bFkLGazbZGvrCA0MrwmqMr2xUxBQZfMzcN-e4MHWptmD3me6lZhZTX5htB27GSZen87znJX74YOzZSrlsVLzrUHb4IJJ14G4zBXpQcQimH6jfg6CEIaRj3zuP2avG3DXGA5nUPSdaE8cI71WhyEo3MxDVpsLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رسمی؛ دیدار دو تیم استقلال
🆚
پرسپولیس در هفته پنجم لیگ برتر روز چهارشنبه یازدهم شهریور ماه ساعت 19:30 در ورزشگاه نقش‌جهان اصفهان به میزبانی آبی پوشان پایتخت برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28092" target="_blank">📅 23:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28091">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T46CkT_6Herj_UnNcTZ3OWg3R6TLbZodlDOUQvHSCGQZKrV3hc6QaKetZ5auHnh3OH56ryb89EEaENhFznjmqJVOemrfsTMXwt8YpvetDdZdx0qiu4PR4Hxa_5G8mARZJhNGAsWQJwXYi_1T4LUjiY-flNWwW4zgKFfCUcOxaycKzMj0LAD7zyejMXdZxgJ3HeCUlnCVOykZaz96bG2Ry9CZ2cOl6YZvbknrJ8jlqD-7BOQTGnb6ACaAInuwYd2l5stbmflz_jOHFMoyFx0-FcHIma45t_bSk5TKYNOfwbmm4b5itkF7RSYemACeOJz3ElCBbL-fyYoq03Ts9WWKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌وجدول‌رده‌بندی‌ لیگ‌برتر در پایان هفته دوم؛ هفته سوم تیم‌ها محک جدی میخورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28091" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28089">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cru4fUl2renR2HMrbLTKveL-JVaAH6TzO925N1zoSCDhTBp3Ljirj_1SRbF0iT9l9sPNktjCyqmbEnIxPVjeTaqLDyhU__S1FmYZHfOWh4WGa7K3RE5RzCKmu_GG4ggeYLt9JwwyTMTRL7d-nDyu8GUHFl4c10v30jjjqhyBUqsfBF4K-5URGUfNDnF6P_cKbwmYDMeBF6ssfh4kT7E5of-6QApFiFjS11zadvsTx8tzyhErDwbJKvTd_n-P_e4mASXs_ZZlWjmuN0gYCna0-YI98faq0xZjILTMXzt0qc87pkfrqkvkiNSuVEUwIg5KS6E9r_k0fchGhVkgyYcDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZF3a6OyBXxmT7UKkVOG9ZX0wW72rOPmmi-6luYeDVlTUAW11Qr71nRYH0CJrkQztW4OrBbfveFfNQssN1en5xeg2CbjVTLuRTaoNvn_TYULtsG7jChuXDLecm1LA-v54r2cck7FmsQ51QIQJ2WRxoC5darwqQDN-Bm1JSXnv1tIAMKg7jz-CUKN1_O_96TB5CicgWQrQweIOxY2BKRpOMsiiWtbolIYFnpxWZr7VR29pX47NpLezwa84r9NMfMZTodQKxht8UyxA2Diwp1f1_VXMkFCCfgzR7Z2wtwZeKyGo1BtqdSv_WrJx_nuKdlLaFfdYj-XToz4sRvEKR43gkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌برتر؛ دومین پیروزی قاطعانه سرخ پوشان در فصل جدید با درخشش علی علیپور؛ تارتار باپیروزی خانگی به استقبال جواد نکونام رفت.
🔴
پرسپولیس
4️⃣
-
1️⃣
استقلال خوزستان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28089" target="_blank">📅 22:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28088">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3_Rs_zTr03MkvzAKBjur66eJ-HvtfEQlvrMAKrd57JMM7IZ_hLS1KsBp6VaQUkzRnxM6_BjheMdbs1xDrL0sF5PMQwhDPPO7jLPT81g1HvwZ4KcBf6vlaIZ7vEmJVtdyffIUPZ0B4EooMKRzjr5fcyvzRJ4cRH4laeVagDPHRT30MlBN8wO5ot0yxMA8yTBvrUag1pDj-QDDygGmi3TxTSxGcD3tt9Hwk82qC4OmjpUvDZQWHSLURFmCBrrPj9Xs12srPtMesycwQYq2HCNAwXJGumWgobGuUhoWD2V484ieRku8AIpjEpKuP-cAz1ewaeMVtVg1wGRlKEbvOTNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آرسنال با پرداخت 45 میلیون یورو عرزی کونسا مدافع میانی28ساله‌آستون‌ویلا رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28088" target="_blank">📅 22:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28085">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524ee90d80.mp4?token=OE4svvaaeCWDbbvagJgncLQB7bArY9sr4GryDWTXB5ns_QeEb40qp0N_mwWRItvXDS2rP92voLlQsVF-qZTB6MeYt2BBxxXQpIP0MOXsDRr3QzIOrdttllYTQrTx_qAZI_IsMyRN503MxHYAC4zqnWLzxSGyLtUFXlw_EKz-B8RfSnbACQYn0mZe0ChdHw37vYFjUIUiGZQxT_bEKhRISYa9Z5tMrY2r3x-9-jqKSUrjiJWlIFSFwCqU7Subxsws9BCWaKCREYP__mvVh_HxkbjCsSe7ewFxjc9Zzn8ElDNox439boxAirB1DbQpIAcMaWNr2yibbr7-RKB1ex0Fo1OKSEuXm0BWlEV3XlyK43jVjRYo8Zo_gRc5Ij579j1oVQJT7Oa5I67X45Q9ZObhhxRyUc7nahYbROLEaETKwmkoy_GH7sSTu4ptFZzpBeIBhP4KERG3-IQ9ckbV61pNnDeRsQZKidaXYT19iFxSQ_QlajLUsSHdevC_oCYuk-PeC3e_IZklDl-_B9rgITnmex_y3i8YbWr6RkKN8YCc_pconY_OSkZ61nnEeKZE4tWjtb2C4xN_sZGNretJF-GzrJmtQ89QXkcwaVMLz48ZZpjPG-n886dhzXaWnw18I4lvTmibjKWHeTEa4Ws8zgcjH8LdcR_DsU5TkFr-3vxF-Bo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524ee90d80.mp4?token=OE4svvaaeCWDbbvagJgncLQB7bArY9sr4GryDWTXB5ns_QeEb40qp0N_mwWRItvXDS2rP92voLlQsVF-qZTB6MeYt2BBxxXQpIP0MOXsDRr3QzIOrdttllYTQrTx_qAZI_IsMyRN503MxHYAC4zqnWLzxSGyLtUFXlw_EKz-B8RfSnbACQYn0mZe0ChdHw37vYFjUIUiGZQxT_bEKhRISYa9Z5tMrY2r3x-9-jqKSUrjiJWlIFSFwCqU7Subxsws9BCWaKCREYP__mvVh_HxkbjCsSe7ewFxjc9Zzn8ElDNox439boxAirB1DbQpIAcMaWNr2yibbr7-RKB1ex0Fo1OKSEuXm0BWlEV3XlyK43jVjRYo8Zo_gRc5Ij579j1oVQJT7Oa5I67X45Q9ZObhhxRyUc7nahYbROLEaETKwmkoy_GH7sSTu4ptFZzpBeIBhP4KERG3-IQ9ckbV61pNnDeRsQZKidaXYT19iFxSQ_QlajLUsSHdevC_oCYuk-PeC3e_IZklDl-_B9rgITnmex_y3i8YbWr6RkKN8YCc_pconY_OSkZ61nnEeKZE4tWjtb2C4xN_sZGNretJF-GzrJmtQ89QXkcwaVMLz48ZZpjPG-n886dhzXaWnw18I4lvTmibjKWHeTEa4Ws8zgcjH8LdcR_DsU5TkFr-3vxF-Bo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🟢
گل‌ های دیدار دیدنی دیدار ملوان
🆚
ذوب آهن؛ ملوانِ زارع بازی یک‌هیچ‌باخته‌رو دو بر یک برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28085" target="_blank">📅 22:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28084">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZqAYVw1WOYhiFPoT49JGS_fUCIotOl_jcyf0zMiultYQ3kYS6AwBWp-8OfPgMyY0I1EfIyPTPD1mTRfm7gPZiKGwH-kW4mb6uRwwx0FuEUxmdeIg2xNT5kD-sehNEimuWBGUial5FO2E-G3DQjUOY7mIDqw8-FY3h2Fz-2zfCEv-TqgIR_5RNzkPZh9CEhk4wLVeckmnoonMGRcMlhUQnPpv9pdxbgO2cDyC_vBlViVStOq6nKT1dR-Gaqf0Si33epnpDi68rdw_4nhiXWOHRHu8YhacUqTqRhjyIjbkHR-EDn9RftY9rtlbnqdQ2NX45EW7Bc0x-srq_cbu00BIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امید نورافکن ستاره سپاهان بدلیل مصدومیت از ناحیه همسترینگ به احتمال فراوان دیدار هفته سوم مقابل استقلال در تهران رو از دست خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28084" target="_blank">📅 21:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28083">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lC5eskZ-B7bTx9iUbxkUOgkGC5i9pY1HdVyCe5JtWrr52WXrTsMLfZqtpyvSPzY4bCX1oE4UC9IzWQ4Be6VCVOTq41g9lva-2RwRKS8Mj112tkzAxx9i71xTPQE5qa-OEU8VP1kbVbVKGFgk3fOhO6LcKS9pnT2WKRN-ubmVlMyyxKfYeYkNfE2KaJL4eXo_ADEsPXYtxIGQwSXEUfuVxIe5WKSrxVkaqYR_PojzreuTwXHEyZwuEwvMBU_KAtfF81g78Jk-FO77BAuJU7WxNfmHxUuOR9JKFNCfiDOcF3vfB0WGi78bST3crwahoNAXsLn0VOjddOqjPvlT2HoZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
🇮🇷
#تکمیلی؛درخصوص محمد قربانی تا این لحظه باشگاه‌الوحده‌راضی‌نشده رقم رضایت نامه این بازیکن رو از 1.2میلیون‌یورو کمتر کنه و همین باعث شد تا سرخ‌پوشان پیگیر جذب دهقان شوند. اگه طی ساعات آینده اتفاق خاصی رخ بده پوشش میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28083" target="_blank">📅 21:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28082">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6602afdddb.mp4?token=k4TJi4R0WYFkv6fX_v7Hw003xHbcTZl5_y6Zum3P1FAxdUOOHOvN9AiF6ZIqmBzVaSMmNwrerMilewd19tKRzLp8PgA9_sZ55XosrPtlVw6uC99N1rUyBKU2hVi-56JvGNPxfm3oCkWwNho72NJSCgkG_SwZODBw3O0svBrVVf9gsoQdcC6CBj-GjCYZBxUrC9vZFPw6C_Zc_Ed6CbwAbs98D61QHvD8rpdob56TDejXP-vg6ril9oIye6ZQcjP-MseCP6n4QyCRt6-sF4hDZzyhS6y4LsQTEk1Xu5mFyEOEdR_O7rQSwKPWf-RTBq-DCWr33ZlXIPN-Lp282Dya1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6602afdddb.mp4?token=k4TJi4R0WYFkv6fX_v7Hw003xHbcTZl5_y6Zum3P1FAxdUOOHOvN9AiF6ZIqmBzVaSMmNwrerMilewd19tKRzLp8PgA9_sZ55XosrPtlVw6uC99N1rUyBKU2hVi-56JvGNPxfm3oCkWwNho72NJSCgkG_SwZODBw3O0svBrVVf9gsoQdcC6CBj-GjCYZBxUrC9vZFPw6C_Zc_Ed6CbwAbs98D61QHvD8rpdob56TDejXP-vg6ril9oIye6ZQcjP-MseCP6n4QyCRt6-sF4hDZzyhS6y4LsQTEk1Xu5mFyEOEdR_O7rQSwKPWf-RTBq-DCWr33ZlXIPN-Lp282Dya1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛جدال‌پرسپولیس با آبی‌های خوزستان و مصاف‌بارسا و الاهلی در جام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28082" target="_blank">📅 21:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28081">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRYcZc8XFYX5VX50K4988AbyFT9Kfir-_clzBZrvKE7ozi9AO2cuaUOXQHfrNs-m0Wd-rVLwb38xYpWMnIrTtgBMldOTIpwONE4f8MA32HmyrX_O_7Xf5SpAnddLOoZukPPpCd4BkjbIzlD92KjkfvmyxudvEwOPQy3H73tsek0fTBfVYMiwoh9GGwIeLBwThKAMEJr7Z9lnD80ILRfy6f4LHd2BSgKLEZbt25uxKjBZDUKM9cYncTCs1MPGdHwenF-BkdwvKtNsfOylR-5wwNzUIgAgE_ZadcB3_TPgHgooJccAwWBv5n0suU8l0EW5M70Zi4NqsVyELee0CP_3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌برتر؛ دومین پیروزی قاطعانه سرخ پوشان در فصل جدید با درخشش علی علیپور؛ تارتار باپیروزی خانگی به استقبال جواد نکونام رفت.
🔴
پرسپولیس
4️⃣
-
1️⃣
استقلال خوزستان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28081" target="_blank">📅 21:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28080">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfIff1HNdW2EcMMEhN8tj4ZOgyifq_xYI6lENExOomxFvE_oyMfrHjO-sVWMdLcFF8K51adu_Gc7lRHfdJMa5n5AwIINq8oaRyOH5A-_5RHBXRxgoMwT0IACwHKR8prqlSs525M67AH3buhyMQ81WBY3Cdjp5yn3NHX8amx7i_MXZlzDJ52xbC36Dv5rfaFcXff5LaBBQO6A7czhLRxI2tZYl82EA_OeTe58z_DgXTFJ_0BhlF5aYYj8qaAXArrGBuuX39pyQ4RkYioH2lk2Tebv_ppvh2tEAjXYNQJMyBrs4xHrPv1Iz4BH6jf6QUb89-hNYilvGFBf73BFs72uuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌برتر؛ دومین پیروزی قاطعانه سرخ پوشان در فصل جدید با درخشش علی علیپور؛ تارتار باپیروزی خانگی به استقبال جواد نکونام رفت.
🔴
پرسپولیس
4️⃣
-
1️⃣
استقلال خوزستان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28080" target="_blank">📅 21:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28079">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhL6Y9KcnmcTyWe_5ruEIZiuefyyFR_lfcafEavYTJINRjLh4B4Qi8ja1vSU7Yje60o0TzwNsGiyjMvp6_CC8DkJ6U2zLzt4gtAAqV1Ljf6COmCBFl5IwrKICO6oD1fshpZNpJQ5XzUNzicWmmapqlklm3SBSylqQ79wT_qFSS47dK9SgrDdiXZq-gYjYQANVAdCxFlSpVnzWmau_-5OQNLJ8HTg15-0kC-HhBkQHvjbKzmQNqIRIXEVnwphOh0XrjYFS2Z3uJRzapSWduMlOVvI1juNxNeN-c1he-CnNBApK0gl_Nx_CXRRTIGoJwFv80vq_UtPJi9c5jltDaYe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کلین شیت نیازمند در دومین بازی خراب شد! گل اول اس. خوزستان به پرسپولیس در دقیقه 64 بازی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28079" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28078">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f0b34890.mp4?token=V3RCsok-d-PxgKIPpiBC2ixL6PT7fDzNQmX5vpKbBEkf1hIaNX8O5ZaHKJok347wq-Q6ImTuo3as_pARTZjd_2UB_j8K2iVJte70Yp0A_i6TN_CcTE3yOYLgzwNc65DyG-4dXYfemok7Bok0iRb4My4IpGw63k0qttZ3PAcl7t9njUl0XHupQSIyiBAVS1cRij8fYfVQKCg4uTeAQ9TpsfsRk-X5H4KBepuBx1ZQJPikJly2XqUWdXposNaqvOpbSnSRbfIxkMeXX3Gr_9BOmumMwmqKd2WZ5MeasFqKJzu0SG5rmSF9Y9W9DQH7MuPb5ZVCfXFxyHTRzi7PoAhsrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f0b34890.mp4?token=V3RCsok-d-PxgKIPpiBC2ixL6PT7fDzNQmX5vpKbBEkf1hIaNX8O5ZaHKJok347wq-Q6ImTuo3as_pARTZjd_2UB_j8K2iVJte70Yp0A_i6TN_CcTE3yOYLgzwNc65DyG-4dXYfemok7Bok0iRb4My4IpGw63k0qttZ3PAcl7t9njUl0XHupQSIyiBAVS1cRij8fYfVQKCg4uTeAQ9TpsfsRk-X5H4KBepuBx1ZQJPikJly2XqUWdXposNaqvOpbSnSRbfIxkMeXX3Gr_9BOmumMwmqKd2WZ5MeasFqKJzu0SG5rmSF9Y9W9DQH7MuPb5ZVCfXFxyHTRzi7PoAhsrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلین شیت نیازمند در دومین بازی خراب شد! گل اول اس. خوزستان به پرسپولیس در دقیقه 64 بازی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28078" target="_blank">📅 21:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28077">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIuUnosxA8-ZYiRE-b-lADhWQqbT-nDJ2HV-YCCeLrQTm1bQtYRo2DGmm2SNVc0eIuGSniZFTMI6pzYelEJi4gnl4URAL0ZHBSbJ1zAK6Q_0RyDa1g3ZMFLSrb6FzBYqyexT0UfH2ZrRpeQhNcoRFLmLeY_jS12vCr7VUi0h_cgdtX7mO4mbIh_MBeEt902ZVngxeNgIxPI96QodHAtCBMHWIMKmUMVqiarITLe9mFB_H0M8N10fU1cpBNIBOUeqqUasXsYKuDEaCJvUQM3ykT2fYoqPUZtJ5bSlwHFcMUSSx-61oOiMJnl1EGauI9LXqc92pVIe8fBhQe8A_7Wksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌ازگل‌های تماشایی رودری هرناندز ستاره جدید بارسا در دوران حضورش در منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28077" target="_blank">📅 21:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28076">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb9a3fa5f.mp4?token=pRDqsmbZXO5feWw-cdc_5-3HMZc4axeVu7RQ0eQlhULz51KsCgIW76N010i81gio3nySuR_vfRAliYSQz02m6eDZBUuywDOUv2Ndd5lVXwf4fAgCzX7kJRtZ64-mFJxLl4zVIrx1YqxU9I-f6SF9frpMY4MEEMWPdT21dcGLvj6sVgFcgPCHkYbwXctP6prKy2QNV7EpvLtSUoAzbYnDRYL2crH1UAzdrgiPkzmejg8uYrcch7k0KDgSCV3GvJxnD3Bp-A_y7s69xacBm1e_Wf-HUsLbCxqMe_liIvtNm4Yic1BQZ1DHWfirsviFDoqKs5vhNr-3yQnphsAtdNfVwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb9a3fa5f.mp4?token=pRDqsmbZXO5feWw-cdc_5-3HMZc4axeVu7RQ0eQlhULz51KsCgIW76N010i81gio3nySuR_vfRAliYSQz02m6eDZBUuywDOUv2Ndd5lVXwf4fAgCzX7kJRtZ64-mFJxLl4zVIrx1YqxU9I-f6SF9frpMY4MEEMWPdT21dcGLvj6sVgFcgPCHkYbwXctP6prKy2QNV7EpvLtSUoAzbYnDRYL2crH1UAzdrgiPkzmejg8uYrcch7k0KDgSCV3GvJxnD3Bp-A_y7s69xacBm1e_Wf-HUsLbCxqMe_liIvtNm4Yic1BQZ1DHWfirsviFDoqKs5vhNr-3yQnphsAtdNfVwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل سوم پرسپولیس به استقلال خوزستان توسط ایگور سرگیف '48 روی پاس هوشمندانه علی علیپور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28076" target="_blank">📅 21:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28075">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef87ad1f3.mp4?token=t_sSocNT8Fpb3ouPk5XhyvjxmENr2WZ9bKxTCBERHYu1TiSLpDi4bt_eGQNcMuAIgeOA_WbT83uurfR01vnLbvgXvxnrfK562KST0y0VGSzEDmN9spwNUSS30Yc8bj2u1XopOxxbO8Ps6f9_aoguqtgChXuwOrU7h76uIXcLDeVMcLTISuP464deMkwtx15E0trG53DPTqF8MCsaN3IXI2mvpvPvEQM3wugXTdQZ0CgxQeMkdt6XnjS6bNVIZJ6mw7TgGu6bDYHqrXBb3JR7uTKclhYu9ulOfh-UT0EkVF_aesVgwywOjYpBkVMAyUdtvEI_YxWqRP3WFlXLpqOiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef87ad1f3.mp4?token=t_sSocNT8Fpb3ouPk5XhyvjxmENr2WZ9bKxTCBERHYu1TiSLpDi4bt_eGQNcMuAIgeOA_WbT83uurfR01vnLbvgXvxnrfK562KST0y0VGSzEDmN9spwNUSS30Yc8bj2u1XopOxxbO8Ps6f9_aoguqtgChXuwOrU7h76uIXcLDeVMcLTISuP464deMkwtx15E0trG53DPTqF8MCsaN3IXI2mvpvPvEQM3wugXTdQZ0CgxQeMkdt6XnjS6bNVIZJ6mw7TgGu6bDYHqrXBb3JR7uTKclhYu9ulOfh-UT0EkVF_aesVgwywOjYpBkVMAyUdtvEI_YxWqRP3WFlXLpqOiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به اس. خوزستان توسط علی علیپور در دقیقه 20 روی پاس مجید عیدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28075" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f80a1480.mp4?token=Wta-wOvvWRHc7EcV0NqjeXMzhUJ95gCcffVa2FmGmnfWU9I8YuBnCrs9QZvr3cads2PRHVOw1z1QlqkUHpnOhAac1Ao5a7BG-NKaY9r6AakNOodmXhFtyS4RNH-uwPLRSllLFfP7K8mDgRlFRTSW109fyvHvVg75Ah1ltNjz8Esa_z84Xpvv8YRqHbDiDETkq7lmofUOPmrqFoMTwYFC8cQhBUEsrnpwhldEGZ2RXnXyL9YGcNX_IX03QwunhT5u-s779_7lETyBaHitJvozyUGMwqtcWVRnysfggQUp0ZLOTbjXQQFUbA3v_cR4kDLxn4H0EBHQDr7lGaHabzlD1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f80a1480.mp4?token=Wta-wOvvWRHc7EcV0NqjeXMzhUJ95gCcffVa2FmGmnfWU9I8YuBnCrs9QZvr3cads2PRHVOw1z1QlqkUHpnOhAac1Ao5a7BG-NKaY9r6AakNOodmXhFtyS4RNH-uwPLRSllLFfP7K8mDgRlFRTSW109fyvHvVg75Ah1ltNjz8Esa_z84Xpvv8YRqHbDiDETkq7lmofUOPmrqFoMTwYFC8cQhBUEsrnpwhldEGZ2RXnXyL9YGcNX_IX03QwunhT5u-s779_7lETyBaHitJvozyUGMwqtcWVRnysfggQUp0ZLOTbjXQQFUbA3v_cR4kDLxn4H0EBHQDr7lGaHabzlD1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز منتفی‌شدن حضور مرتضی پور علی گنجی در باشگاه الطلبه عراق؛ رسانه‌های عراقی خبر از آغاز مذاکرات این باشگاه با سیاوش یزدانی مدافع میانی سابق استقلال و سپاهان میدهند. یزدانی از طرفی هم‌پیشنهاد تمدید قرارداد از گل‌گهر دریافت کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28074" target="_blank">📅 20:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28073">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxgM-20V_PK1bbl5NftOGXgn58JAyFVmb0DoZU6Tij5uJtp-a62NUuhSxB8AsAnTrqCV45PAmx9G1F2VphD8Dm6nS7i6CQiqWYXX_olI3HiOoidcbNDXWlls4xLl-JOi8WLHZPEiGWmyR1q5hxtdofC1iCYBJkIDGunpzXfcyO0TWzWxhOglvWaWMPXxonbCdPqHdEdOCqj1oTDbnHoTvm3_0_rlHqwRIjtgt01-5E4M4O5J0PSYSA1_A7XN-4lOUdyFmRy931Jomt6Mxydqih_iowXCMUQU1kuBocOkZyimY44CU-lRy9tSPjH4W0hWZmCEC91kvhcLvIBg_4zSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآستانه‌دیدارحساس باتراکتور؛ ابوالفضل جلالی از ناحیه کشاله ران مصدوم شد و فردا بعد از گرفتن MRI میزان مصدومیت او مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28073" target="_blank">📅 20:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28072">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aba5f2ad.mp4?token=T_VytIvIkz57d7TZCDmsNGodXK18pu4dyWzJR-hEskNC-YEZ16iUU_ZQgxqDdGnsye2WoAkYyXxK_ZBiwGjkELToyEyrVdBm1ynI0R8GOayWrlDpPvIG7XTKwLuWPsytK-bvNOJQnzUt4Gxra4vdgPAYCu6aBpK49rVIgBp8Rf6PHM4uaWE7Zot9bhdkgOXc5102AIdIJO_yBxGJ0wo2mn1EOXe1FGFCbM-Gx-C2JiwhThChhGiUX8SRbqYXY9eOoG_OkSWNiLixUZzwCwpM3buHzcDy2sI7G47njF7VJU6p5FWXfg4-to1VnQx9pIZZXSoOEA6XMdIsnTfiDodg_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aba5f2ad.mp4?token=T_VytIvIkz57d7TZCDmsNGodXK18pu4dyWzJR-hEskNC-YEZ16iUU_ZQgxqDdGnsye2WoAkYyXxK_ZBiwGjkELToyEyrVdBm1ynI0R8GOayWrlDpPvIG7XTKwLuWPsytK-bvNOJQnzUt4Gxra4vdgPAYCu6aBpK49rVIgBp8Rf6PHM4uaWE7Zot9bhdkgOXc5102AIdIJO_yBxGJ0wo2mn1EOXe1FGFCbM-Gx-C2JiwhThChhGiUX8SRbqYXY9eOoG_OkSWNiLixUZzwCwpM3buHzcDy2sI7G47njF7VJU6p5FWXfg4-to1VnQx9pIZZXSoOEA6XMdIsnTfiDodg_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
رامین‌رضاییان ستاره‌فولاد بعداز پیوستن به این‌تیم با استایل بالنسیاگا کنار این تیم حاضر شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28072" target="_blank">📅 20:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28071">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJLA51evo3TvCkSx7FoJyMxRTaDNorJNOcRCMKXvS7up4yD7MRr5B3uoZKmtW0yaqvtXXly-wjvmDNqe_6kUx_mswhYvrlXeYXZnKzq2vJIJ_O59qgHNrMSuPsdKVXjeBXec0-2FJTbSg6WICzNDIgXdYdTerAcQfn8GGqycIvwqALPIU5d6BNTMWVq3h0-unNTUiWUn8lqR_rNrSFCGQ0NP09q2k7CGQWi3Wo-oZXIBya969-1ERS0rp-AeJbCeBE12-R9a1FwBIMj_zJU_MwKzqhlZl31i_jUy2SJ6z1pTSWIFDWWi9SFqrdf63WVnK6Zyk33nlDp5bPY3WUdowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به اس. خوزستان توسط علی علیپور در دقیقه 20 روی پاس مجید عیدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28071" target="_blank">📅 20:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28070">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYYWntip02tusMslyT_nD8YEM174wDez4IGhFLCSY9smpQc3WRxxmkNE3Hup8gz3vv7VNFFcg1sxUo-Bb5a6Fehbi2DGtOhDeThHEdMb2Ea3f6WcNTGKCoJl6kLQ4w30QrRi6IQC9dIjldf7aYTh03YkosCQIAObkDJX9Mes8n4Gx3-TvY-eSROUuUHVKn6nTO4JDUUmeYY9GYKCnGVzEqoPLiJZ0Bzby2_XJ8NIDdnZTQh_4cJw3_DyTr3fDBrMMnCdN2g1TLi7bCHiAbKRkmDavOJ3l8KF2MGVOwcYDmB7k8Bn2TetP4A1oGb3JR96K45lHARxAvW3-KjAsdMQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآستانه‌دیدارحساس باتراکتور؛ ابوالفضل جلالی از ناحیه کشاله ران مصدوم شد و فردا بعد از گرفتن MRI میزان مصدومیت او مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28070" target="_blank">📅 20:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28069">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b577f54.mp4?token=A89M2doZnaNjttcaaw8tTx5FYI86ZoQ0SI9jHMEp70yRfrWPExEd6D9Mh28XnjfnAp5kyHkAxq9JCfUq2Zb_h5P9DBbo4KoQUSEJuIc0MO4hjeaYUG--zkvuFeEDC0eRUDI0rV8Lr-PrUM3-yjIPJYEIN9u2hov2IzPfIdeWtKFmnR-w3Kco6VyQOxyDNT45g3MYKpzkP3_Ba08bPsbJeowOCuNZ2ohb2rqDDOx_ktahvC8DFAvlTFYewzNJ-Uk6SwsdajPXnatlia8kUAi0Zlvl8_QJbE0nNldjYJ3Hg3WK_s2yDHerf1fRatRnt2V17POWZQpI2xl7W-6q_JHV_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b577f54.mp4?token=A89M2doZnaNjttcaaw8tTx5FYI86ZoQ0SI9jHMEp70yRfrWPExEd6D9Mh28XnjfnAp5kyHkAxq9JCfUq2Zb_h5P9DBbo4KoQUSEJuIc0MO4hjeaYUG--zkvuFeEDC0eRUDI0rV8Lr-PrUM3-yjIPJYEIN9u2hov2IzPfIdeWtKFmnR-w3Kco6VyQOxyDNT45g3MYKpzkP3_Ba08bPsbJeowOCuNZ2ohb2rqDDOx_ktahvC8DFAvlTFYewzNJ-Uk6SwsdajPXnatlia8kUAi0Zlvl8_QJbE0nNldjYJ3Hg3WK_s2yDHerf1fRatRnt2V17POWZQpI2xl7W-6q_JHV_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول پرسپولیس به اس. خوزستان توسط محمد خدابنده لو در دقیقه 6 روی پاس علی علیپور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28069" target="_blank">📅 19:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28068">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f85915bad.mp4?token=K4JrG9q7_i7XVaIUOcZazONwrKdVctskELxqU4nUycM__hfBjsOuVY-i-8pJ7jbgz_qS0E8xOnE-R1IJZPlkspg_ZBt9v7NHcT1NOxuwQHPvbX7qSz-puc07bzsQWZLp9ba9JF-HI6PgfFIsLL80Rg2W49yqVT0HTLJUfDsGaqPRRmdndYzZ0KGUFySIx-MyX_b_Gs0p3aHPP1Ho4MkeFU1P9O5oE4OjvqjOQ4-TOxScWUnIRzyWp3l25bd-ZTQhdvGrh2mwIb-r_LLNBZNPaLvwdKpaITNd3R6hrGDR2AihLHbL1hbmPjV-h2vVMarDgE4xykzz0o8d0BfigxT8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f85915bad.mp4?token=K4JrG9q7_i7XVaIUOcZazONwrKdVctskELxqU4nUycM__hfBjsOuVY-i-8pJ7jbgz_qS0E8xOnE-R1IJZPlkspg_ZBt9v7NHcT1NOxuwQHPvbX7qSz-puc07bzsQWZLp9ba9JF-HI6PgfFIsLL80Rg2W49yqVT0HTLJUfDsGaqPRRmdndYzZ0KGUFySIx-MyX_b_Gs0p3aHPP1Ho4MkeFU1P9O5oE4OjvqjOQ4-TOxScWUnIRzyWp3l25bd-ZTQhdvGrh2mwIb-r_LLNBZNPaLvwdKpaITNd3R6hrGDR2AihLHbL1hbmPjV-h2vVMarDgE4xykzz0o8d0BfigxT8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شماتیک‌ترکیب‌پرسپولیس‌برای دیدار امشب با استقلال خوزستان در هفته دوم لیگ برتر؛ تارتار کاری کرده که هرترکیبی از شب قبل منتشر میشه اشتباهه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28068" target="_blank">📅 19:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28067">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568f2b5232.mp4?token=H2cXRMS51iY36ekBg8m45XG-4wiHAK7HIi9_8ieUwJZ9l1MY6sjPB7WrIUp292oBRHTmPWoiWeNrklW5zvWByKqmbI6qyNjLFG1vs1vLJgehcYMC46-W-G0ieCtVLy9drE9L4ANJBZc14DGyiGhrbLhGPWN-hr7dT891_-MYgJgrYtYJi-dapnbCjl1Vy_t85eOnoqbgJoUN6gd0cWLoTAWaCElKd14ggiBU8Mk_9lyiT-hRTTIz2-bw63C-fwL4DjGXSd0pHnVBeRO9wAkVtwGRzU2G8KMGYCW0M0d8HYkr7GuFpN3WBFlmgEEf0RQrjsQGrCQ5ckLVpnKJH2hnHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568f2b5232.mp4?token=H2cXRMS51iY36ekBg8m45XG-4wiHAK7HIi9_8ieUwJZ9l1MY6sjPB7WrIUp292oBRHTmPWoiWeNrklW5zvWByKqmbI6qyNjLFG1vs1vLJgehcYMC46-W-G0ieCtVLy9drE9L4ANJBZc14DGyiGhrbLhGPWN-hr7dT891_-MYgJgrYtYJi-dapnbCjl1Vy_t85eOnoqbgJoUN6gd0cWLoTAWaCElKd14ggiBU8Mk_9lyiT-hRTTIz2-bw63C-fwL4DjGXSd0pHnVBeRO9wAkVtwGRzU2G8KMGYCW0M0d8HYkr7GuFpN3WBFlmgEEf0RQrjsQGrCQ5ckLVpnKJH2hnHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو و جورجینا رودریگز در اتاق نشیمن خانه‌شان ازدواج کردند!
🔴
هفته‌ ها بود که اینترنت پر از گمانه‌زنی بود درباره تاریخ، مکان و لیست مهمان‌ها. از جمله مهمانان مشهور شایعه‌شده از فردیناند تا ریحانا بودند. در نهایت، عروسی این زوج در یک تاریخ برگزار…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28067" target="_blank">📅 19:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28066">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AN2soJ5ZAfQvoKZv1omLVbOc7NCUES7Ukvlzkfu_N5_b8eDetMLFb7t5qYwza1boPGEQPIDqadGjaXua_Mmi1tj3HRZ2w8c8guYPaKDXTwcFNOVPvcIQCYcWlY_rQfm-DE29WntEtUR6RDsQ7r4tMumeBfqWWPrB9Vf1JwdQok_C2-yABsA7nQQZBrDlXfppfYW-nwjfVBQtjEc7qLt2x7uDQPbxV6gvHTU8JSDdCDtvBWQxv_zwCCq4L7t4pZpoZEanq2H_N1pkJFhGApb46yFwFYhBokwK6yXEQqqYU10IpFTZLd9R6BMHj2LMZfnO7a025AjJKcgQENLqRgJReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#اختصاصی‌پرشیانا #فوری؛ پاسخ‌ منفی ستاره سابق‌بارسا به‌تراکتور:برگردم اولویتم استقلال‌ست.
‼️
منیر الحدادی شب گذشته از طریق مدیربر نامه‌ های ایرانی خود به باشگاه‌تراکتور اعلام کرده باتوجه به‌شرایط منطقه و مخالفت همسرش فعلا برنامه ای برای بازگشت به ایران ندارد…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28066" target="_blank">📅 19:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28064">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGkBhrD1FIjNDeAdHi96gT08aVc7c7YkKXNNACag6aK5Gm3VkgJyMoQh6zB1C_zc-9xeIAAyBbwND1cE2FnYEDTz7th3RTchz-5TczgJ3WqdwdAps8EIw_dsrAmXB0zHuEZanRCscLTyvAHLBWdQcps3gSH2zq9oSY9Iu7-y4OVNW3nbkBb18kgtqUWd5uMBQKwTaFotu83JanrQIQYumLai_nlvMG2c293eGOAAQiPkA1gWZxYf9L12SHpc7xjprlaz-Iuyu9NxHqAkw9jgQvKM3ZoOtZJq0Gy5MKFtbklSWtBcCIdUIDxrzMLIID_SR3vKzF3Rj3PNfcYAF2hrdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ou1tpZQak8ax2QnnGyoAlkR_D22Bns0B6J42JXGivECKYyKAMFZaBEvsbaZTruvYHnxJFrtET2tR4A576OY0dRbC6MMsSIKCBd3Fj0hN6GvQVJ7tamJQvDczuUeGHJk_2SvBDeTYotS-D7_vhA3bFVYvOjmATbBBCj-YgtMUlENEiWGGu3iIOOE8W4YiUcLnZwuDFah2rY8NoEChhc-w6gJ3-waVYwLHhrPs2siQfIBCXjaU3jk80t4MtllPZOMF0HUXF9-S8TOC-VR1BIEk-KD8UOYNUvIMzezgnsKiAAnvjeXtlrhlPXg4vrFH2jUljAomyy8MLQhMHr4hohLV_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
صحبت‌های جالب پپ گواردیولا در رختکن پس از باخت ۲-۰ به یوونتوس، دو سال پیش:
بچه‌ها، می‌خوام الان یه چیزی اعتراف کنم. من از زیباترین زن این سیاره طلاق گرفتم، همسرم، همسرسابقم! عاشقش‌بودم‌دیوانه‌وار، ولی دیگه شور و شوقمون از بین رفت. عاشقشم؟ قطعا آره. اونم عاشقمه؟ آره، ولی شور و شوقمون تموم شد. فوتبال رو چطور بازی می‌کنین؟ فقط چون بازی می‌کنین، یا یه چیزی از درونتونه؟ تو زندگی‌تون، هر کاری که می‌خواین بکنین، با شور و شوق انجامش بدین. من بازیکن خوب نمی‌خوام، بازیکن با شور و شوق می‌خوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28064" target="_blank">📅 19:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28063">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbUbT_UXPALoGQUxYxMKdjKipRq1yGKoxsCrh-KGyMHcA-X7lLw7_lOCKhtyxl0NXDv9iyAkC4opXoQSOxd2HAC5K2yX4zG5fUWgvDoEWY0PPiXAzEF-STmMEVa38JiUqPEerZyimRL179rgaRVLBbPkHcmCNjYMru5uvTgQS8gs-B_7DC85HAPqQJCAYpC4ZFc7H7coEQK8Ly2Vr3ccQpJ8wB9id6kLOeaUJF4hY5dodgX_3v9kujy3OttsbCyeG1Vbj6ZRmHO8-v6qO-CopouVf7l8BkNG-kzcP17OjnQcMkWxezbLAMU51IA8dHD7Buzf8V45FtWCYZ_GMqdakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰۰‌هزارتومن‌تخفیف‌خرید با اسنپ‌پی در شبکه‌های اجتماعی!
دیگه با اسنپ‌پی میتونی از بیشتر از ۴هزار فروشگاه و برند محبوب‌درشبکه‌های‌اجتماعی مثل اینستاگرام، بله و تلگرام، خرید کنی
و با درگاه پرداخت امن اسنپ‌پی هزینه‌ش رو در
۴قسط، بدون سود و کارمزد
پرداخت کنی.
با وارد کردن این کد تخفیف توی درگاه اسنپ‌پی، خریدت رو نهایی کن:
✨
کد تخفیف:PAY5SCMD
از طریق لینک زیر، لیست برندها رو ببین و با تخفیف و قسطی خرید کن:
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28063" target="_blank">📅 19:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28062">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFvvplXgb2ZrpppnrvNFcJRc1Eo1kcK0KU9jXQryOQ6DEdPRLZ5gTxBT7CMicve1oyHrdd8BdZnPUmK4mnWjeRbFKtK2W1RBWkMi3tDzjhDZcj-TlaYXSNU2Jw7xzXToBwbnGsFXQVIYVaEvL6oBI311TJ8dlUiYKDU4vxgc_6zmroJJb5qkkH-nLyQKMQOd7Epea0SgWnRk8cnaxOSbS8F4i4RExKudhqG5HSJLCTjBxrQRCFUX4AjCoyCRLh1AclgWMCU7tdToQOj0pO7A11fel-IhZDVwZq9tIYVl5B0rlGmLDPSsPkCyfb3q1rJ9-QmqURNG4lAUD5egFdykAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28062" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28061">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCxNmRxHH75XIvm2UqbCNkvmabSblnWyDlqTqVRhX_qIgZeBPCIYAgzrXTuAPXfn4FqaBz8fm_jCTJHuxUUYCrJM5KjaYz9DZkPs2BGaum9rdnyYT2BAOnkksvNSvQWWIF9KPUuqA95CdUYMZ4OhZBkjOly4jpyEZAqc-uh8Hx8RigS6tG-Fw0d2Fq4D-lG5lRn-dJYgJdbMy-Z35gFw36EAwLG8C5qKdZAGjP53N_TyRr5MEbkUz40f719afEImqC4ulTp85gL_YDIz_VOjp1zQ0lh-7-RnOLSOEIWBKEMr_wDdT9aN9VH3VqWTDeMwNJXCX6AgOyMyhf7cA1ZmKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم لیگ برتر؛ ترکیب تیم پرسپولیس برای دیدار امشب مقابل اس. خوزستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28061" target="_blank">📅 18:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28060">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngwdLQmjPOTksIvgsjfnvDVU_szUYSxr64rtAbO_vZsbe0Ybh3bwFPA2oTJ9Y0fT4wcoKOU9Yw4SM1t4gijxMU0GHwZFrXkvxmdPJqIb2xl8Z6wvKbJCPJ5dV9OmaBNJqw1qmGHlO_Z_ACKbUeyeVN5nAimQTjE_939XSUSSZXsJT2gnoLkAA_5cqUuESEoYRBIjqm4yY0EAz6POJJ_wHgVkzzVVoyAuqUNaBozZnPvwHzrhnXTB5vghmCq-hdiP0TE3PqgYAJRf9h_n8uOByc87VTyZsvCMH3jagOVnqqiGaMlg4h93JPVp2OAy9MqpTbE9ZcHXPhAHeCIzD-yimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه گل گهر سیرجان به خواست مهدی رحمتی با ارسال نامه‌ای رسمی به باشگاه پرسپولیس خواستار جذب محمدحسین صادقی وینگر جوان سرخ‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28060" target="_blank">📅 18:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28059">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_cfmdL6kvmWf5B4l0EAFm9lRfVfyGZTwzmu4NVi_otb_SUsateMf4i5Uqg6OrZ2U1bQTbXkQTefKi2lwW2ihwP7szGy5VLjT8lUJxs1dfknACqT-2ujKLqg_9tr9h3qv53piXDUIfcZbGIiib4be71uchuYbIfnHbAv5T0eAX-ReVRB122cfZlxcChhVuU9JY_akXQMdipS2LfuNTW7-0q41Tto2u9H29I7LCEUBryY_yWVPdrJhpZf22paLnMPAoKOCJUsTxu3opV2PQwQJGbAV6RagJ1NkA-qg3bZEePtsUtUHUwNMRD8hNkOUBmInCEUCVecPu7nl2v_vOkAHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج 5 دیداراخیردوتیم پرسپولیس
🆚
استقلال خوزستان به مناسبت بازی حساس امشب دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28059" target="_blank">📅 18:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28058">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41809830d6.mp4?token=Ml6zQwhbf7ynJYIPQnbc83UWPBiCiCC2teD6h54DI_VT_5aYnrWZRDSc9pVm0bgwhNf5W1nKE2gMMrZo02JWVYU_Qq5eHwlt4mpBa2mviMP4OxQaHJYjlNu-fn_e6s1QwEbLZpuhaCYCDjoBdbAQdT6946u5-1wJpeQkIBdqXyvlGQWW29xAeZJq-pRp2PFoZIhFavf9oB8kwnsqprWPMPof_RLzFdaywqxoeSfsj9yYVJOVegh6Ms2vUk6YbbXVbPmresFhB5UP0zz2v5zJkSDYgxx9syfC7GBRGVYKLe-qV0gem-nnyKhdqoC-14t92K0cOQ_6JRnUN68g84-eFQUM30pz3yQp839o5eyM4-xQ-xJyZP9qIgc18-35QReBbknzeVQDAKSUZ-j0Y35vlw2btYXjv0WE62gMfgaD-DU7R0SK6w_ZBdG9Pr0_RCILx4FnL97LhnUV4u_4dhHdJUxSWYJlEPFGwcTy30ZdMlRMAf9zKQB45r0aNjBEGgSdsdhrAvAD0m9ItRWjvZ5SqTIxOliXACtWvo2fKLwY0JLHqMin_kQzVpq23yV20eywyiSyaFQzDPd6dwNEAyj40Rm8FGF_No6MQpOZZscWvb07nqI2JH0rU1t6qH5RClHkLCKHfgzOcw5C662k9XkymPHVrWQDIg7GXxDX2YNa8I8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41809830d6.mp4?token=Ml6zQwhbf7ynJYIPQnbc83UWPBiCiCC2teD6h54DI_VT_5aYnrWZRDSc9pVm0bgwhNf5W1nKE2gMMrZo02JWVYU_Qq5eHwlt4mpBa2mviMP4OxQaHJYjlNu-fn_e6s1QwEbLZpuhaCYCDjoBdbAQdT6946u5-1wJpeQkIBdqXyvlGQWW29xAeZJq-pRp2PFoZIhFavf9oB8kwnsqprWPMPof_RLzFdaywqxoeSfsj9yYVJOVegh6Ms2vUk6YbbXVbPmresFhB5UP0zz2v5zJkSDYgxx9syfC7GBRGVYKLe-qV0gem-nnyKhdqoC-14t92K0cOQ_6JRnUN68g84-eFQUM30pz3yQp839o5eyM4-xQ-xJyZP9qIgc18-35QReBbknzeVQDAKSUZ-j0Y35vlw2btYXjv0WE62gMfgaD-DU7R0SK6w_ZBdG9Pr0_RCILx4FnL97LhnUV4u_4dhHdJUxSWYJlEPFGwcTy30ZdMlRMAf9zKQB45r0aNjBEGgSdsdhrAvAD0m9ItRWjvZ5SqTIxOliXACtWvo2fKLwY0JLHqMin_kQzVpq23yV20eywyiSyaFQzDPd6dwNEAyj40Rm8FGF_No6MQpOZZscWvb07nqI2JH0rU1t6qH5RClHkLCKHfgzOcw5C662k9XkymPHVrWQDIg7GXxDX2YNa8I8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سم‌جدیدی‌که ازطریق هوش‌مصنوعی ساخته‌اند با حضور ارلینگ هالند، کیلیان امباپه، مسی، رونالدو و حضور افتخاری رامین رضاییان ستاره فولاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28058" target="_blank">📅 18:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28057">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWaT2zntnMbf7R1-RWBzLslbaxnfwCFgX4oJctezMYvTyr2oapP6vRgxIHzHg5z44zy3aGDEomnY3EMGiijO-pQQKPt_QTzfBm_Stz39fRl-4YDgd91drrB6DRdj_mhjoYl2FKRCWXz8Rp2FdJHFPg0tvt1cojRR9x2auJX6DTKQDdjjK8KIKXZOWWUMsz86Bp2RtnSqVxVNf7VWFtDCJkSfMF6ZVrJRU47UBY62G9UgOj0i-KroRkNY8NFvAzkWTeAfx2alz2TdRe2mOGCeD_EhGgQs9U4BUBOBeej7el285jNaZ8B7nwEc6_kuOSL4zm7VF6kS1Wb23njMvglDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اُما مودریچ دختر خانوم لوکا مودریچ که ستاره خط میانی تیم‌بانوان آث‌میلان بود با عقد قراردادی بلند مدت به اکادمی بانوان رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28057" target="_blank">📅 17:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keiF2mF1m9xBOQ_V3jBg2bHAegqRMoHayZYdxy7UcNzO_ZXjJUXYr2wNTI1uohXwmZH_tcyFf6VLbysPZs00PTPsmBjyXliuP2aLhYZ7p40lA_BAYGVwpjYmjLXG3D3N_itNAKw0V70EEGQbBxPx1pYjauHf7gWdiwhntBsLcAZx4irZrtVh0dSjfF4k7QXSfOR5AcxtMNWJ165EKRqEr8eRVgBaDVgs_3u1E0h91s29VxpdgbhIgaPn4Le8GheI0M0FwxW2DtkJPleyIwgd411CxC4Vxrv_K5LVVFS3fONXIHRVELMp9krd2XUd3DFIND2ffrXK0ateNPKkbOMT6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امشب مقابل اس.خوزستان در هفته دوم لیگ‌برتر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28056" target="_blank">📅 17:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzMPSjf2kVRnyV07PnfODM-1GwI0ZD4-idq0Ah1sIVO9qyvQPhKFc5jkLKDnFyfHkfUsyl_ZLBJInw61wdT3pIirU1XDmvFxyMR2nMLMn2DtikxP0ezJ4eWUbv8Dvb45hXujIPvj3o9nwniYRf_snjOfTMoTejWQ3Agjvy97UUPljWIbyJWSRBMMtVAG0u3ytJTx8HRGUe9KC1jvr2Qr_cSl2HEBSoP6RIRIC8ds9PXKzci6_UYhY8CysvmPPd43_8uY-c4F62bCA7JCpxXapksGdFjj97jMTvIZXHXfH-dx6B5bRg4C2hvmyphkIEiv4Oum032h2FXQusCicR97AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آرسنال با پرداخت 45 میلیون یورو عرزی کونسا مدافع میانی28ساله‌آستون‌ویلا رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28055" target="_blank">📅 17:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28054">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-egzfWvmlx9KYD5a0MM9q4ENTiMsaqQGAbCQgFc5qfwUMwe0uIq25vZG64L5tgAtfOwtfsUrge8jZ6F9CsEGfXx8UrMxsLR0XMw5MHGMS8Eue1SmF2BXLxcrZPwAfR94Mqfe6uZAwEb_wTcp9-leeHKPZJ82ACgvOcMqUn1yAB65Vd9GnOOY1ggsJjivUOfQErsD5MfaufUMrITSgvzdSEpJ21ok8hXKRyUPqB_0pCm7VoQQ1QRdJ_y9RLak-w42r3QFeTjzQCHhOlaID5oxs0YfuIf4RR4d0NNzK-Z0c-rhjmQZvpa2DMk6Qdw_Fl1-7Nlcuk5QUb4DjYDl7PWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
عمق اسکواد باشگاه بارسلونا در فصل جدید رقابت ها بعد از نهایی شدن ژائو کانسلو و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28054" target="_blank">📅 17:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28053">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdbd62c202.mp4?token=gJP2nJLoi2pW9_PSnDgF8Yeb9xm7RwjM9sn-UwGHMPl9RaKHlRLcuZZK018aS8wqGjBnRqhmkSQjMlwtvFvCdnspNrn0-PI_FvouDXxtJMMZQQ-ppkv4Oj3jI3pqcHPivqQOjqIEXRuD7_0Do4CmdEd_HOlRDdQFa9ctgPXIcpHDKSxB5M9YnIBcRzvZtkWL8mTGR1zi8vA_0uENWwsWoQYpkI-0RKapQOKljVerWvs5e-tX88GW_3G0-NLWaADZ5SfD1AC8102E8xoPhIpezJt-6G97fUVQVxyeFE7JBhXl4IpYNugQo1VKxfdT_ztqaMEDzU80zfupymY7u31YnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdbd62c202.mp4?token=gJP2nJLoi2pW9_PSnDgF8Yeb9xm7RwjM9sn-UwGHMPl9RaKHlRLcuZZK018aS8wqGjBnRqhmkSQjMlwtvFvCdnspNrn0-PI_FvouDXxtJMMZQQ-ppkv4Oj3jI3pqcHPivqQOjqIEXRuD7_0Do4CmdEd_HOlRDdQFa9ctgPXIcpHDKSxB5M9YnIBcRzvZtkWL8mTGR1zi8vA_0uENWwsWoQYpkI-0RKapQOKljVerWvs5e-tX88GW_3G0-NLWaADZ5SfD1AC8102E8xoPhIpezJt-6G97fUVQVxyeFE7JBhXl4IpYNugQo1VKxfdT_ztqaMEDzU80zfupymY7u31YnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ازگل‌های تماشایی رودری هرناندز ستاره جدید بارسا در دوران حضورش در منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28053" target="_blank">📅 17:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28052">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3Ue9eI8CEX9UzoRYC2hyKXy5Cnln107CcliFmNXLa5ou5ZYjbxjqO5U3iyUlokDE_Fe8mvNnOBIQA83VZAtcMzM_dYIaUpyKVHQvIbc-PgDmZVW6VplltbGvEdf4fO1dt1R6N1epFAIwWKCBrOuKdVp9t9T4SjoKgIDOTw8lEYxFRrrdDt_tXmot7R45Upfub7CH_4nKpGIZjkbvHlU15OP9r4YstgefI7UDNStiLEtSSr6R2v_6REEjSXMEtHcWGfIpcLyfY41oDa8GkBeULae5ivanGU5bWnBOoaVwZa8nj-bNgXOe8tIua9UqS54nRKolgK4SHvH9xHfZw0A-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته دوم لیگ برتر ایران
🔴
پرسپولیس
🆚
استقلال خوزستان
🔵
🗓
ساعت ۱۹:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی در سایت بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28052" target="_blank">📅 17:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28051">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBNCBi6rsXkolg4oqMCU6dY_ty30dl5H93TcJFmK25VK95KHHNS5YZloKqJTyNwjr0JhnEP4qwnce0wmaMmjtj4CS20MwQWahu3wAIuY44OSO-JQl5luXBFvscyOVmLTA7D30u_WlAeFSgT-AD_Lj519IPaqZljjeyJudW1_7C13La8kY1c43VTdYY53r3EIxSrkZYldcOq_9KaIiSWsE3WSqDWZMRslcwrQ1_tjfKI6pmdrct6vTid9yAv6SUUUQwBprup7byYQa33tdRBGs3JJn2GDowiazLNzdZa0Yf1B_05erLUobUWaO1wdNjR_eQnx42CYMVtz2Pwg8yrBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28051" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28050">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfxP6sJEgyrzugX7TOxixS1N2P3vmUsISD6P89gkSoJEEcHD-zOM_-iaVVYofAqYiV9pt-4YeZjZ5EP1XNFeZgJDfbxhGwjQ1VXWWXHxtzrzSNyVSq_noUyGxdHObQRhXvN6YA22vZdRZiddzdLiIHTxJG-ZKt4AogqgUeyzhs3zWF7blcZ_FsvHqGqxmx2_Q5oPGJi17f3PbZ3xYOYWPnOBoHVxe8YWtglUnnow5h3XRKLXn09SlusnGISqHX-y2AdMSgjS9TxS7JthaM9akyfUl5_Vf19k1lqYOjaiZFsozGdmtErH-WuPy6PPb1weypqFgxtDb8-rCHl-Oh80Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
مهدی طارمی مهاجم34ساله تیم‌ملی رسما در لیست خروج‌المپیاکوس‌قرارگرفت و ظرف 72 ساعت آینده قراردادش رو با این تیم فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28050" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28049">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsG1HUgHggFkoCFt6qX_0jiS4uRKE4F66p7PvCKtAPxw-pr8f7wWve31SS_lMaKFnrS7KFH9dadqDTtOhWbeK-mAkI1lEoNGUhJsFzvnKnacAKAk_knVFOdB4F-MUDmnSYuzllkFc6rEpjUo0xYMpQag4XHX8vjR8gTIa33EhpBBwYQqNSgLFHe9sbg6k2dFjjFtdBY55wbl7GCoYQ0r_OGPf-7Dx8mLqG8nljCHlE-Mik7s3TP-A24CQcNyimwifbbzByY3I5ZSHbdFTngBqfzuPZwrIswrkd1TRvUEYVa3UlQHPFVRf_zsAxZ4BC-fkfRs32WvcI34SO9W4glE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری‌عادی وحید قلیچ پیشکسوت باشگاه پرسپولیس؛ رئیس فدراسیون روسیه به دنبال قلیچ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28049" target="_blank">📅 15:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28048">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICAPj5lzQCjFfflD0cZQY02yVgKO8LyD08S6-Gaub3KiKR1CZOgQp_i9BdUD7XBrUXYILXfkhL8ACxfbYDUPIPEySDJqG8KsRzya-TC6XsskWKz6_bPdLvOG6q-JGb5WcUVYHixEdwXH_lO6g3w2t8O1Y-4X2gGW30p7Geq7XTOr2gyT-nrxwBm9szgDaakqiaRamEJd07yCV-GKsKxNXjXm_0SKMYni8e_Ksls8AIGPQXn7NlaBwq9b1bbbCt-6nUJQMKJ_7cSrnX-yFYhwuDCMSGPyQSF_9xU6bYGfoBP9wPQKgxRRg2NYAyfGd2tp2QVzrEACBJgbAAZUlyCBJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داروین نونیس مهاجم فصل گذشته تیم الهلال با قراردادی قرضی به الدرعیه عربستان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28048" target="_blank">📅 15:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28047">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrJx_nkqfLomVGTPdrLSkJ_rwmE_d3fx3lMRnMmqvlKtB2IbErtgNBLqIYjdAVNVoXEd0FBLVB8lqALcvaHbcNnVYEcEzzf0fMLhX9bovuceWb6dXLEWtZ2EMo5kyz0fy37ZhaKBKPgybbGmq3iRTIr47wvCgfgU_3mheo1tle0kETqfDOoaHSg640jEMvqGJKewHi1wwg7wjHyTPZs1VdVq5iFnTGYPMq2oNvXZlloQNWtPstFpaAfMMuLPG1QH31e1JyND_RMfCT9QX-3BruaXf0-lfjXKUmLKSh3Nieujs9w8I7CX1IUBBvphO7nxVfB82jZ4Km-1RFEP6aLwPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رسمی؛ دیدار دو تیم استقلال
🆚
پرسپولیس در هفته پنجم لیگ برتر روز چهارشنبه یازدهم شهریور ماه ساعت 19:30 در ورزشگاه نقش‌جهان اصفهان به میزبانی آبی پوشان پایتخت برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28047" target="_blank">📅 15:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28046">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5lVQdVMuPl4X4ssfCAgLPylEglETLJ0LNClY4Se6sfJgg-7nw0DQcq5PQFRC_JKhoTbcxBVl5-fx2_1ZWfFb_GBfv1SL7N-WY0LnmSheSxQ22VeKD6KBbYc7TrlmJkFTPOxptg2-lo3YN9y7aTju-MGwex8ltWhk-HicHg_V7te7sLFt-tG0Sf__C-6kI3hlTC9oE7t-wsgTOXy5FbB-EXlu90SeiVFJi-7q6FZNXIc_0duqVaQIw7iv0-nM6ZkEr0kevdFrBgUeFVyZRGbi4bwz78T8TBHfBjl61ALRfeWMGP8GwgUj1_KOEBblNT60vN-V7Kan-qs-KpBHUvp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
جواهرات جورجینا رودریگز جون توی مراسم عروسیش دوتا تیکه لباس ساده‌ی ساتن پوشیده و جواهراتشم از برند chopard بوده که گردنبندش هم ۷۵ میلیون دلار قیمت داشته و انگشتر پروانه‌ایش ۹.۷ قیراطه. ارزش کل جواهراتش تا ۱۰۰ میلیون دلار میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28046" target="_blank">📅 15:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28045">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuGg_Dpl7XoXt0sFuCLoJ-hYYLSu9RyuAHQxtZpnFCnQ1azp6rgb62uBb5hg9-0P3OQcoMSWQhdmT03D-2e2xpE_P4XVVKDIIR84_G1pj6ckGV9mtaBkFhNNtvQ60qWq0_RbVDHl4zhzGjhxRw_yT3XELSJsUMLVQC0HJv6DjtsSn82EyTHll7Y8mH9WfGirhYt9jHmuFQksXmajyoF_1xZM3O1yM_aVq-DHiW0M1dOg1TVsub43BLxqDSn0OuiLjwiAMYUWf5YI7MSyZr-NQ0M94rPyvZ30fAlUVA0VA3ew90PCMor0KpcZzQg_tmrPT3PRW4_X7lByNaupXCnd6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیو باشگاه بارسلونا از رودری ستاره اسپانیایی جدید آبی‌اناری‌ها؛ قرارداد چهار ساله امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28045" target="_blank">📅 14:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28044">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKbRPfUtqKYhtzLfo-zMW2u330Yv41Jx254sqO4SEd1nrCLOMJ1PBGN9NhlTkxm9MssBwUdBdolS3CPSgiDNDjiSLdqn4p06kF4ZRMglMkA5wMU82OnE1U6e6flsxhZuyy8Fqgibwg29ehbxVaXkW0vYVVJIDrc_A4kjb2AUOYLXJMNGE9yP6KA2PISNq6_GCmCtD9LizLDJo0y37TwbFjX07nGIr0kTAeH903B4vYkgsYpRlr_XLVXX1kBTB4mxsa-NqqprxOeZDNG07-SlQGK6AcRdV_SalkF_ZTC-iFkZAq_21Tn3tDuZYkJp55gTeMtVhdIEURkMh2O4KwSrjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
باشگاه استقلال باارسال نامه‌ای به فدراسیون فوتبال خواسته که بازی رفت شهرآورد که آبی‌پوشان میزبانند درورزشگاه نقش جهان اصفهان برگزار شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28044" target="_blank">📅 13:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28043">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba681cb008.mp4?token=RcMR35XJ96vSFgQ_HZrIXUWz01IGdnB4PFyZqbewUIcWxrTcT61V3x31b97FTqww4C_O9cR2ef80VmmhcvYzO5sfTdLlNceNyhu8J-yHggW73fc3ek8zfX63Xd89WZtNnAOxmjHgBa7r1sD_Em3NEbghdCEJtqMdX0hK9UL6cAi29sperCDZPLFt79JfJ56NibiBcAAdZowc1Vzet3pW-IX9KnAPM4q47vEYvLY591QkSEzHA702j4LiAnlcRvOjZSLzj0tM-WOhLSgzbXk-SIoW90iWdOrhbBnQe6jcDcTIMyMLtX_yB4NDYbxux8W7a5MPWtjq0eshqgg8u0G_uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba681cb008.mp4?token=RcMR35XJ96vSFgQ_HZrIXUWz01IGdnB4PFyZqbewUIcWxrTcT61V3x31b97FTqww4C_O9cR2ef80VmmhcvYzO5sfTdLlNceNyhu8J-yHggW73fc3ek8zfX63Xd89WZtNnAOxmjHgBa7r1sD_Em3NEbghdCEJtqMdX0hK9UL6cAi29sperCDZPLFt79JfJ56NibiBcAAdZowc1Vzet3pW-IX9KnAPM4q47vEYvLY591QkSEzHA702j4LiAnlcRvOjZSLzj0tM-WOhLSgzbXk-SIoW90iWdOrhbBnQe6jcDcTIMyMLtX_yB4NDYbxux8W7a5MPWtjq0eshqgg8u0G_uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28043" target="_blank">📅 13:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28042">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjtRkoYckfgsyuB_0iOn5dDNqrKZl9mMwL3P3D6th-K8711D9IFL3J1Hg3J6UMquSonkpFx0SrtcWmbfM3BiQF-Zz2y9JgxNzl_VzlzBjDE3mRcIpxv0BGjyGqodVec-il4nYBoFBOEEDAFd7XmdpPxvns1jLk5k-0eftXdR0ayLhs8wS4PV8j60JJT1Nh0JSmJapUAuBuUWiviujfSSV9mUove199vd6vxV8TCUGSeOKAQmrdMGmnjUMjnAGeht3AR4m7mODqvY_lV2LNL7oeyD6hQyDZo_z103hOLH_nT33URGic3ioAPPX22mzjdxIgXdpoZAMyqNrO9Zmz6TMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته‌سوم و چهار رقابت‌های لیگ برتر؛ هفته سوم دو بازی فوق العاده حساس داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28042" target="_blank">📅 13:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28041">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXylW44-ut0L3ydw724zrrZ28ZfoqoyGgiTOA2k8rbWwyWvo3yPY9z18ztU-zFLFAwGLPWOAvdDJVmV9rk5i--_stNpoCgUUbAWTf-2W7llIly6kitvVvNPkedpIgU7J-S3JsTX41fmpc2H2lfMBSKJM20YzvWAdT0PN1M1lbAIbIIyDh5y97UF_TBRvZUJO-1Y3WJdIDQYxG2yM7xoUWG4LIJhJRS-Vf7N3BSyJgJhaRGl604ltmnvF29zklGK3E4Iso21Fp745SZqOodGyCtOjkwNMGch0zpVExsuKrqeOZU_nhdd05yI2hsWnWflDHvlQ8GyKEkLXkWspd_ZrpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام‌رومانو
؛کارلوس‌بالپاوینگر22ساله برایتون باعقدقراردادی پنج ساله به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28041" target="_blank">📅 13:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28040">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikTbXQNC-w8zs_OoliytosNq44IziUqGUyOyBDZTdTAc2m4Sx5gGRIKAlSgjiVUrZfh3rA5r2P6VHORKLD1-Evvg99BfcAV-a0XJH0pxoe3Ha3u5vVwT3x8uvXzAFJ7azGH328yoHnEQl7TD-5_3oeTYhtnGbbzb18Eq_skXHUHFxLEgKYtFW_-3lgnlOWWPSIn0lenLBfScs4TjLIN68pD1Ot1-6AOQqVAyaFF3tndOeXz-AnygbwZidoEpzNuXPMz2WBQTHOHQ6Z22brkuz5x3hGDGovYWAqBKcl1Cfv6xvPzyMjcJv3uaTAxeFoQcIciePiZD2QXCtKO7XRX8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
پل پوگبا که پارسال بعداز 26 ماه محرومیت با موناکو به میادین بازگشت امروز تو تمرین این تیم بشدت مصدوم‌شده و رباط داخلی داده و طبق شرط تعیین شده موناکو میتونه قراردادش رو فسخ کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28040" target="_blank">📅 12:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28039">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyDW1U_LADNZW8QkcU3BfCc6fXN2hqrF9TioARuvzCT540PBXwsQ7ry18dn6She8OR-Taphozof5JKWtQ8bAvNdgBVzASBuT4SSvHWYjOgJw-gS1xJ_Hwo38bA1dsSNxzfweCZKMISxKHuLggQj_RgwVB1nCNAvEP-Liv7vsnny3P_Pr0iXjm31Cv0rmZr9QNfa1yXpRzpxVsR22U3Iky6XYKvXnd_3XDDzl_YCefX2rqYSu3WmMNnTO1HDF6LAiKlFQNjiPAAsvbX_U8fPJu3gWImZ9RsIPM7bh0rv2GSZ-VjGru_ZTTCPUh9jnDRzxMGZNtsT-_VM23xZELGnh-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
رضا عنایت‌زاده هافبک‌میانی جوان پرسپولیس با عقد قرار دادی قرضی تا پایان فصل به مس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28039" target="_blank">📅 12:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28038">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXzBNbjw9pL7lFsNl6AyoU7UxWBbRBp8-1rTaVSbMtm9G0L3NPvePNnPnfEk_T2zrNYEJ0F_owfwMDclhfR7hZQZFazubZwGHbdpHoXtHSlGFbGoLux9iD_ylYNP2okbf_QbI7NZjlQPvKTvRyIb4zVFRSD6bV7sE73hE67Er2SVDEhvgC40GIL9IqJrZJ3tounsCccPasJh1w7N5s_LOCjGQv85RDI2tv9wQTQ43TCuRYRtiiYaVvlZO54dqYXJGsKwvnYAcj1hCD2yb37LAP43TVf9wz-sWxf44SC2lJPUQVJVdmLPoOFsmu7yP49RBae0e6BD76itbLPWMY_Iwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
فدریکو پاستورلو مدیربرنامه مهدی طارمی: جدایی‌مهدی‌طارمی‌از باشگاه المپیاکوس قطعی شده. درحال برسی پیشنهادات هستیم و به‌زودی تیم جدید طارمی رو معرفی خواهیم کرد. مهدی یک آفر از لیگ ایران نیز دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28038" target="_blank">📅 12:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28037">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axqBU0tyXrKYSEY3uxeUhHP-4QaEf-gAG96QiQQ2SfXGwceylX2UG_NbE3pgSeIG_XeLOx3SyBJ8wBiCkD_JlZt7xUU9PqvLsdncfS0CPMtzc30fZF6RJMXjBdeLpsSScLn_k6bQ9yaPD_vkDne47O7NqUID4EROfsox95w7JDXVQ7M3R3MqYJgqUuKxtFMGh07PFfMbzAElQX0ZDrao9XT2HYHzxXBxIszRLjbebWgSaHFDlvScq_UHJvR688Fe8JTdexr2RQ2Y4rVcpim_08HecaiC-cLLgbb4lzisRvf3jWGUB2WhRhKPIn3MV1PphZF6yVfbBZJp_rk4esE9hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
یکی‌ازمسئولان سازمان لیگ: روز شنبه هفته آینده درخصوص‌وضعیت کسری‌طاهری و یاسر آسانی جلسه برگزار خواهیم کرد و رای نهایی خود را درباره قرارداد این دو بازیکن رسما اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28037" target="_blank">📅 11:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28036">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAXRFMHCvwygktQtC58haJOk5Q_teYs09THSm2jhhfRCzVzBxnn1JvhI00fo8LMnb6h8BZQFisK3yU69UO2FGHRTZJMxCgcJnnBRozSrHybNgJdikPz2CuOOTfiVzPSzkxWknP9ryKdj-zXiR-jme8o5aoCEWKhF0RIjderR2UGUv0oU_7MYZCke1jDdmi4MVQWupQBA2AsTU-Vc5lw7l7BaB79fqA6E4XcpG5itNbLZvh6_Mrq3GfalVdcHP3Fhy91JtGLxik51SBsgC1Rr-cjs7fyK3JCZzLNq6Ah1WqbI-E2UYVog1sC_tqJAlmY_dY6rddBBzEl8a7Ie6G6n_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
دو باشگاه استقلال و سپاهان امروز تمامی مدارک‌لازم دال برقانونی‌بودن‌قرارداد آسانی و کسری طاهری رو در اختیار فدراسیون فوتبال قرار دادند و بزودی فدراسیون در این باره بیانیه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28036" target="_blank">📅 11:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28035">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4dSaputAjn6VrOLvAeSLK0X7DummY7USQF65wzqMp4AwnTRoUSoSkFR9lbKaiBkc4had31yM5IqVdes8HFJBfl1hSEVNt-_4O8y4y-UhnMMFR-1aZhQ8Bdn7oY6yP1SHs2sw7rW3jQH9J-g9Bj8617WNcgC4cLZxt4QP9HYkdIjOP625iroZ2QpTDNJmHI4Cb6P4xvwdnRnNruxkBrJErr4H2SmfXIt6C2vdEvB2rM28nsd0FQEhtpodu4WIrnOwiKzz6QEl-V70JiVngGFSwuinXcVwq55Hd0cosIZbz8FvL6WhYqLwEAXo9G1QN0TVc57p5JdtWo0bQ3K0PhU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نتایج محرم نوید کیا سرمربی سپاهان مقابل تیم های بررگ فوتبال ایران: 6 مسابقه، 6 شکست تلخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28035" target="_blank">📅 11:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28034">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZy8t1mi3JNKLPnjCmLdSxVEBpnH6E9obRLusWUxZ4JcFqD2omXLesRNClyNENogtAcBA8BsnHf7cqQPEc0eX6eiW0PsMRZS29qx05pLZh7pCYhVYGvYsCa7HMbZ4fOfkCmfeX_7sOPEDNrFsQbUPFCtwOZYIA4owHFXJWaOi2A72HfiHYzUBfLBZJ-oUWNhEX3_gorJg3ppxDrDNDkw9ndZNbuNfxiChW3ItJxGgDV_fjYc4xh6k8-5sKc-3juRCdVa4IaGGJCeM-wROUjcTywrtKSv1RGHxjk_93pDj2bjrJwAf2x7XoAy67h3t0WZZW_sDdRxgKwLfWeBaD5UWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کسری طاهری: از پیوستن به سپاهان بسیار خوشحال هستم؛ باعث‌افتخارمه که کنار بزرگانی هم چون سید حسینی حسین بازی کنم! واکنش حسینی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28034" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28033">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWEgJ3DNmp1UwnUIc-wcJYGv7KUk82JJZPXPl16sBzJ-PT2Yo_jmP-Pe804O2Lr-INy8dVwOC0c7ZbY80NmYRwi0mXnItGDJOtbodox_MGoija-yK5zDsFMbM94jTESdslaSaI8XhhTSKeupOqWhbEOQCte6LXsUEy6Bs4pSUCkN3rO86pj_jXntUu9TUCqJLDcwqc5WTOs9gfwtX87VkepbRTCt6q37sH8Wkdc0sx5eaVS1HXPYWb1nmm535K5wYwOgmPPV_EW8olEPIbyOlBFEznUGqP4WNApgzYHBwdNBNTw9CQNe8HcElezoRCf3jwsguEMlPMRcuX5_x2GP3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار: چی‌شدکه اون گل خوردی!  حسینی: این توپ‌هاجدیده، تاجابیفته که بگیریش یکم زمان میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28033" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28031">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ8-UcZxH5NS8aB24maXiWI0y8g1ff3d3YbIexMjd2X1iKO0x9xJm9LLN2fsgGtYN2oMAiPvc26ArQxhwjHWpAN3jwVSU4yKr9Y3sf5xTKKDD9N20YXdqnniN4Yu9oCbmKZAzOcsHwSlbhnRLK6hi2Shif8f2qJZhV0-dsbPG0WJ0tZWcAZfJz8sFWExR_YKWz0GPh6ign3ipoXRGYFWb8L0LPr7AWakxcR1wMPUzD5JN4ma36VEDLq3mdp0jfTzyxnaFbElsU8-qXElhKeuo6YcASFiYuMXZ5DY-YI5_5ryXAqg33MziJEYlJHAO13zYTkZxiC_p-TOoqorJYQI5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه‌ای که هوادار منچستر متوجه‌شد حالاحالا‌ها قرار نیست موهاشو بزنه و باید همینجوری ادامه بده   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28031" target="_blank">📅 10:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28030">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8ipS2fttz3GNXVUecShooAYOVCelpjH4AoB2QgPInh9au6OvXezWLkzRfgvdlYKL2K5Pe3wfBMWO0GqJrMjPPQLR3et2mL7AXLw-gASfgBykj8tENcyFKbm-_pCPxXUYyNVAo-_Ux3fXkWRoVRWRAP7hxsBbP_9gEoFA33sDLEgalKpHbz533gBrF6GcZFnjYqGA4dJDZCvd2OIt4REWaWxfVn8kC9gZ2UMgPHouj4DXG5XcCCX5QIgpXYy3jKTgnhgrpKBs46HZ1gK8vP5DBxwwr_45ztKZkfLUsUEaC4ZBea97UHSIpU-Ba_DpUZ2UsDBw91UiGWaAELXNxgmuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارکامل‌دیدارشب‌گذشته نساجی
🆚
نساجی از نگاه‌سایت‌معتبر متریکا؛
صالح حردانی مدافع راست آبی پوشان بهترین بازیکن این مسابقه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28030" target="_blank">📅 10:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28029">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936c9a62e9.mp4?token=bvXKlNugIhmBt2aq62mRfeh0le-dE3KvxRy-NfFg_x42z4vvQIBrcP5Gb_PxeoJvBov-8sfy6-G0DnTJg_wBDHuwIzGS9pojbLDkf1GO3ujUuAlyRHLaYVxFC3H6OsRqK6KtJrNkBa9lcaR3gnuXv4bTJWEfKqvatBCnYXHDkUq1nPgJqEv-Hq64MAeP30T26aPIE4aN9FB78BWmLFyLxzp2bc8zjipezC4qNEiiYfznFC0-mm0O2cF6o0hL2xys5qAifrVgTNx23VrBD2-k9FGbiPwaqyX_y46cvlRvhzw_A3xNfhfA_RW5-XMHrvFVq_t6nindskyv3WVz9o_n3lBayNiAVAlvkR78mWsvHJSXB070ijGCIysTyjlsNYc535AZy_GCHHY77ivLH1bp48_XyUu2N1_foUy33Kr8wOhE-lpV2eX3Hegpljz0ttXZVoYE4g0IOMi7B0ePLkxrRJeCzMwLVjfZ0WXIC6DL9Kk9rGkDm8ffGL_UHWuBFUvm8O30lJIXGXts178ViOaN4uB0Bjk3Z0Y82EKDBwVeEikfwH0nGkMPFRS7j1sJydg9qWjXMQKhDsqoZLR9N5x_oJ0tT7or_M3o_VmxS-lN5FWeMinU_smoDzePryxyCJroOK5dit7BFHFi5aJBkPEDT1Nj6lwU3Y8tkiim_pjktNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936c9a62e9.mp4?token=bvXKlNugIhmBt2aq62mRfeh0le-dE3KvxRy-NfFg_x42z4vvQIBrcP5Gb_PxeoJvBov-8sfy6-G0DnTJg_wBDHuwIzGS9pojbLDkf1GO3ujUuAlyRHLaYVxFC3H6OsRqK6KtJrNkBa9lcaR3gnuXv4bTJWEfKqvatBCnYXHDkUq1nPgJqEv-Hq64MAeP30T26aPIE4aN9FB78BWmLFyLxzp2bc8zjipezC4qNEiiYfznFC0-mm0O2cF6o0hL2xys5qAifrVgTNx23VrBD2-k9FGbiPwaqyX_y46cvlRvhzw_A3xNfhfA_RW5-XMHrvFVq_t6nindskyv3WVz9o_n3lBayNiAVAlvkR78mWsvHJSXB070ijGCIysTyjlsNYc535AZy_GCHHY77ivLH1bp48_XyUu2N1_foUy33Kr8wOhE-lpV2eX3Hegpljz0ttXZVoYE4g0IOMi7B0ePLkxrRJeCzMwLVjfZ0WXIC6DL9Kk9rGkDm8ffGL_UHWuBFUvm8O30lJIXGXts178ViOaN4uB0Bjk3Z0Y82EKDBwVeEikfwH0nGkMPFRS7j1sJydg9qWjXMQKhDsqoZLR9N5x_oJ0tT7or_M3o_VmxS-lN5FWeMinU_smoDzePryxyCJroOK5dit7BFHFi5aJBkPEDT1Nj6lwU3Y8tkiim_pjktNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قرارداد رامین‌رضاییان‌بااستقلال برای فصل جدید که زمستون امضا شده‌ بود: 100 میلیارد تومان + 25 میلیارد آپشن که توسط‌بازیکن فسخ شد. قراردادی که هوشنگ سعادتی با فولاد برای رامین توافق کرده 65 میلیارد تومان نقد + 10 میلیارد تومان آپشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/28029" target="_blank">📅 10:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28028">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC5EMr3rR9-0Lv8W90Sfj2oHUmqXB_ZOd1opTYSp51OApQp64Dp4AL88ngx2WD90M3J0oSL2vOniVpGz0_p9O6A_5QoMRuNPCaellDeJuL0JU0RfCtnVT0GKfb9-KT412hudzBRdOW5kSHIR8qgXVN6sXEHhWZ4idMP0zp6r08L2seSO7pn6OHI3Rj3eTJX9YlhvB3hr59nyATclHMOptYbeJd_nvVPjprBCpA5uw0mXGfhKeo12ApcwAYP_0z1YZ-BmLb0YdCm16WgTod2QKXfVBFfih-Vv2OucPcsLF3ZZBsGUud0UfBdbDm-_tvlHF3eBKNJurQ4n0uppnNgm8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امشب مقابل اس.خوزستان در هفته دوم لیگ‌برتر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/28028" target="_blank">📅 08:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28026">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INJzALYS_6AKg2TFjRmt50E21GnA_2wD0txOahLD5Fx-IQivzmAPQQxjmS8M58b2t1CBMlvaUxpe2tfYClNGg3-wBwSIqN8cP3qPA_4p-7wq8L9SqrguoMukUla-Y29GfnL0ZnlckBWLVn6SbXaHOxYqd7Zbg8vTgEPylv8ki3ICMIC6EDzHhacXl9cYU5Xcwqh-NOnwUS3XRm4bMe_8LWk6mAiRgFcyWS5LaopLeXTbvzXvqF7XSIx3pZ9IZJWmEMLByTWm1xIll5WE6fNILR_rbBJMcksyVvIcT2HxOaf7vJWYhZC_o2m9ITEEFo5SkM5w83P1FyRzjzAt6Rj4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
جدال‌پرسپولیس با آبی‌های خوزستان و مصاف‌بارسا و الاهلی در جام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/28026" target="_blank">📅 01:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28025">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7YBUs5ykuIz3A5yRPPzCGVEpCJoOIPKxWMor8klAWjeCJH9VVFpoVCYOzUWtam6irI8xsf4mrfo7ONETju0Sc12UrOn87erSQX2G1Z5zsjMxMEP0BXXQ1g6opbJ_IlcDNtqCA2ldI3jaYRd0k9CZBNmY7sKd0Oi2sh4P_MBXAQ2xDszCGnmcA-JeHdl9oZAgkFeNwxFcZ8THlSdTICBj0vmxa69uG14DHxWzdy2Yq0sI9s5NZPSzE5d7rOVKmA0S8qdkaMJRQmN9Prlhe5n9KEtKsj-pr0SG3fEfap3wjTNMnkgJf0Wefa4fh7kfS0Y8my8r8vuQg3-JMBjKx_X4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
برتری‌استقلال‌برابر نساجی وشکست‌سپاهان‌مقابل‌تراکتور با درخشش حسین‌زاده
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/28025" target="_blank">📅 01:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28024">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkQkka_stqLzhOg_lILiYltij3yi2putiT11PIBXK20U4g3xQtWl8hBi1yRzqP6aYuaZR7HBHsBvMUTiUbjIr2QRM436dPQ_5gnalrrTkc77TD50hBhInRsaYCCNaiWFc3hRm3BloGTZbATpsjni7GxzqhdWBA7Oi_ezSMSqxQd0N8vtToOxZn7jIsiecE-ZYnwvoN7RYy3vlRhrYSPVThGbnw_NgXQ_Y9LHMK_M9beRJwK58l6jzDqZyTMYHFPYcWuIjVNxnuYIVM8H8XjFmwcaCayceXonKi02x1bpJQRCVZkKj6sWdxy1YUNpoLYU9KrAbraDDj4O4He5vF-8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روبرتو کارلوس، اسطوره فوتبال برزیل و تیم رئال مادرید که اخیرا نیز مسلمان شده بود با یه دختر به اسم سهیلا 22 ساله ازدواج کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/28024" target="_blank">📅 01:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28023">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd87aHWEyRSKbAnJL_7oVXBOAqaBLa7tSWc-X5luDYyB9ugj03KhcXCQG1YSKQhCwbLle-8XgNQyJlUx4p5EXamzbUQo8ZbxnVM7pm-JRvwIk6i18Kj9ePxs2lHJ_hJt9r9E_eVQqGVL9YBOUF_B2t4d6RFhIVGFZ8xkWISR5Jc7AALDmgeH79A4OWR7q0wPlVqR0bbRJSMDOaN8BoNcej_Bs9YTX2M1utK7S5TF4qgCODNOYS5u1ddiB_GPMYiyLbksHbWtXSXq9Iq7ZFQtGaAZvTDv3ZPuvw9iauBhjzgX29IlAeGsqyxb39kpCQHPl6wqq9_DC2wAPbKhhvdqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون و آنتونیو آدان دو بازیکن خارجی استقلال تاپایان‌هفته جاری به تهران خواهند آمد و در تمرینات استقلال برای هفته سوم حاضر خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/28023" target="_blank">📅 00:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28022">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMPo1J4hvVwACVjvjqG16SzOBMy_p5gMyqBEdbXe-qeIaYTBEH4tCggMIWRvxcvuo3ieuk8phiDMDiwSXiuQos9qAtEH1R61LPXgech7m1qWYBbCKLaDnxzEv2qawnOeszGsJ0EdnpMx6GI_4ztqOsPPiUDoh5g8N4ddAVtC1vSoVvh8hI5woAtQySPtsroRhEc-mXitoEs-2WxFFg6SYoJKvbtjzVabd8ZcBO7gCYJnSzzeIf81NMKqD0--PJhRqnkPYIGOcqRvOxUzGioVQtO8cSkaLqIZBIeFfnKIXjOtqOw0nkajKDIR7C54Gxwvnu-9jhsVgnVkvFs3pJW3Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛باشگاه‌الهلال بااولی واتکینز ستاره خط حمله تبم آستون ویلا به توافق شخصی رسیده و این بازیکن آمادگی‌خود را برای عقد قراردادی سه ساله با الهلالی‌ها اعلام کرده و  تنهاتوافق‌باآستون‌ویلا مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/28022" target="_blank">📅 00:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28021">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19d89cb00f.mp4?token=hWjfSamz4UK0cHd60HuKF6R6xxbZDdeW-2KCyLWqdZOSic9qXhwa9sdI8YTjSIoHVNDKbA1ROzfj8coAklIUxbG21QRuR_zVekI7JAourtGzWBzUqGcjsiS0J6fmgfHCf1fVZxft6qz0KzUKA6n4J1PwoLdQ3rQ10rELjoHDdzxL9hbgfFZRyAZX4-QnYgO7eQOng7wxFUmmcN_qkPdzffSxtrYdDAL3FwaA_MsLqNXjYeZS63SZeHFiVYc7ZaW1_uxAJYtX2-n2NYME4qoGxAM2Nb8yi0-VJzSHf8qRx8gih8V6Z13DWnKs095_kiMOvJrfF0pYqQrWtx3vdLJLtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19d89cb00f.mp4?token=hWjfSamz4UK0cHd60HuKF6R6xxbZDdeW-2KCyLWqdZOSic9qXhwa9sdI8YTjSIoHVNDKbA1ROzfj8coAklIUxbG21QRuR_zVekI7JAourtGzWBzUqGcjsiS0J6fmgfHCf1fVZxft6qz0KzUKA6n4J1PwoLdQ3rQ10rELjoHDdzxL9hbgfFZRyAZX4-QnYgO7eQOng7wxFUmmcN_qkPdzffSxtrYdDAL3FwaA_MsLqNXjYeZS63SZeHFiVYc7ZaW1_uxAJYtX2-n2NYME4qoGxAM2Nb8yi0-VJzSHf8qRx8gih8V6Z13DWnKs095_kiMOvJrfF0pYqQrWtx3vdLJLtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام‌سازمان‌لیگ؛ دوتیم استقلال و پرسپولیس فصل جدید رو هم در قلعه حسن خان شروع خواهند کرد و فعلا تا هفته ششم هیچ خبری از آزادی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/28021" target="_blank">📅 23:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28019">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9ofUJFtyabsr5g93QEviNqx2KameOoJjO3DG55HbRg41KdXWjWUpTOsM545RNRprHc8dSdXaKzTzImxUINkon_xE5wXFsiTbLpXQ45Vf9xJarC_1MEkwUed9BJaTrDsGeqo5O4NWyB-CURJW-tn-JNCdBiwMRUsFJwk_px-6APGg2iVw0DYJfdffa1cDU6XXyogs3gOj8L5FxuYvwnCPRtPQ_J0iZXrNZaANcjrDGTYq7C3gggpai3jliFvm30Dpm4gbUyYjhtdWZinChggHjbZVLojVCYuyr2dZPHS6KRWK1uUT4xeMXxervA6hPmco2evmRxBW7WC7-gj33tIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJ-sBTTtcqhmKc6nO6Tmh-GyGxfZun2R9GSfjQDQpNcxHCRbCcyiY3If5tebPStQHGDQS7YhIeXiIRY7sBE61ciwfOuRoZFWbgRXzCAYU-DZ_oJ1piKS66Wy50QoWiADneL4BAPK-V6NX0ylyMJDOkgLj7McKuJsE5LJU0HDE-PfmOGa-DlA50JeEbqZo6KJcjmuL-GC54--OytVbpZTkSqdwkKmncmku6iQiadTXh2eql3GflOvH6gdaebvdpgSS454VAYAkKpayJ-ZAAs-1wkEfC3GfeKNy7iPgC-OCQ9IRqxjakG0_9KvkvlSoR-0uMidH3BFrX2lFbn3e9kWcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
روبرتو کارلوس، اسطوره فوتبال برزیل و تیم رئال مادرید که اخیرا نیز مسلمان شده بود با یه دختر به اسم سهیلا 22 ساله ازدواج کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/28019" target="_blank">📅 23:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28018">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89654a5b7e.mp4?token=SKRAHp07NRPdvvIyu0YXftvd7zhQYyYK6rarsdsi0ujoduYV49j5J4oARy3WBgvc9BBKkV31goNL50aGt2Bajwvg1gAq4FqoQCYjlzwwVbXB_4iV7O7xQ9sAamOjBtlKyi05HDwEX4oNOjL4MDS0LvvZkhRQFuAijymq4hip2bAdxe5v8mBugemP_ocrDOlfI3Mf5x6nJoHFdYQ_3P76SOjS1TBKPpVcxGr_Ir-lXpEIeTEWM517wZl90FI2UDkW3SEXRPvVf_aeqa8ufeuMprfpbhCOdq6x8LPkn2OzbUvCw8WeAUbWniaLE6Tst8ssk_ibP2wv_eb3VVydNbga3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89654a5b7e.mp4?token=SKRAHp07NRPdvvIyu0YXftvd7zhQYyYK6rarsdsi0ujoduYV49j5J4oARy3WBgvc9BBKkV31goNL50aGt2Bajwvg1gAq4FqoQCYjlzwwVbXB_4iV7O7xQ9sAamOjBtlKyi05HDwEX4oNOjL4MDS0LvvZkhRQFuAijymq4hip2bAdxe5v8mBugemP_ocrDOlfI3Mf5x6nJoHFdYQ_3P76SOjS1TBKPpVcxGr_Ir-lXpEIeTEWM517wZl90FI2UDkW3SEXRPvVf_aeqa8ufeuMprfpbhCOdq6x8LPkn2OzbUvCw8WeAUbWniaLE6Tst8ssk_ibP2wv_eb3VVydNbga3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جدید شجاع خلیل زاد مدافع تراکتور: فوتبال دعوا نباشد که لذت ندارد باید دعوا کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/28018" target="_blank">📅 23:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28017">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a8d45198.mp4?token=EZeA61rmQ8qRaGRW9Lgm2svVHSQEzGUbzP6qD5EwIlWZ8cn98Dp6PLjCePDnq-m-RqajSaVmfFlHbm7kY7mo0As_i9LRGWwXfudIF0HhOmDxiexcToEFOikRO8-jdmH5lbp6Hb7nBE6FBuG2Gy1SsiQA3vO7gNvXzVtMJjNNA8SX-H-rZZNd0KTG5AjDiyIPfyCcb76mlWB6o_gvc6u2GWiW1MmTD0tId8d2KcouFLq82sXgLHjmpt6xWQorbnl-WdFAy8ZSrgzQH1Wcv67xTtmXPFtu8sVdtxzuYWkxz8l92kTTx0GxdExOGEG8mmNe24SJcVbULS8GLI7yvU6VwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a8d45198.mp4?token=EZeA61rmQ8qRaGRW9Lgm2svVHSQEzGUbzP6qD5EwIlWZ8cn98Dp6PLjCePDnq-m-RqajSaVmfFlHbm7kY7mo0As_i9LRGWwXfudIF0HhOmDxiexcToEFOikRO8-jdmH5lbp6Hb7nBE6FBuG2Gy1SsiQA3vO7gNvXzVtMJjNNA8SX-H-rZZNd0KTG5AjDiyIPfyCcb76mlWB6o_gvc6u2GWiW1MmTD0tId8d2KcouFLq82sXgLHjmpt6xWQorbnl-WdFAy8ZSrgzQH1Wcv67xTtmXPFtu8sVdtxzuYWkxz8l92kTTx0GxdExOGEG8mmNe24SJcVbULS8GLI7yvU6VwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حسین‌زاده‌ستاره‌تراکتوربه‌اینشکل دروازه سپاهان رو باز کرد؛ یک شوت محکم به وسط دروازه زد که با اشتباه سید حسین حسینی توپ وارد دروازه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/28017" target="_blank">📅 23:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28016">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175de0fa0.mp4?token=evNPNQOQQ1MkwX8kV28OKYEg_vTudv-g__VlrGSwQ8n_yiynLkO3AasRVY_Evkc-eb0_nJQ4q4x1DJqKhQXDgw3UGl0EHLhSElgWudXvJ37FA28U-SDg0hDFaYGcs49d5ZOInCC4JNi9kvsvlOTBq5NEq6alN_fWUWoZtCMeP31Y1e61HKnic4ixWhpuRtagA2zu9N8fTYFZXGuatPOye3qQdEXKcr5C7KhCKqX2R_82CTeJeKIQfujVTXfG7Hw_wz9-SOG3gedmVmv6r2HBQIiiti-PM81RF7mkj0WY9peEB589DxmDP_eDnY7zenNqJgp5GPKf7J7uyk7oox_ltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175de0fa0.mp4?token=evNPNQOQQ1MkwX8kV28OKYEg_vTudv-g__VlrGSwQ8n_yiynLkO3AasRVY_Evkc-eb0_nJQ4q4x1DJqKhQXDgw3UGl0EHLhSElgWudXvJ37FA28U-SDg0hDFaYGcs49d5ZOInCC4JNi9kvsvlOTBq5NEq6alN_fWUWoZtCMeP31Y1e61HKnic4ixWhpuRtagA2zu9N8fTYFZXGuatPOye3qQdEXKcr5C7KhCKqX2R_82CTeJeKIQfujVTXfG7Hw_wz9-SOG3gedmVmv6r2HBQIiiti-PM81RF7mkj0WY9peEB589DxmDP_eDnY7zenNqJgp5GPKf7J7uyk7oox_ltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلیل‌زاده:اون‌عینک‌لعنتی‌مال حسین کنعانی بود و دادش به من‌که باعث این ماجراها شد اما من بازم میگم اون گل آفساید نبود؛ ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/28016" target="_blank">📅 23:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28015">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc13a6650.mp4?token=AOP8sfJbiD8uBUDBjPryvgezS-1EFlRqd2vSNsNFdhY5TaCHJgzAqbKJWmO4ddCaa5nX512RygSeWL0sLku7ECQDjPs_is_pUSbSdbAlYgBRMM1LI7sOtKgDwioGZjsNLgC75TtHtIDZHNtgPZndTGcudqLKc02AG-EffSgMLWtx9UanWDOuqxfxsOYYO0mbz-vongYvdkEtpgIHz-p3NT1ykurXvFvr4V5-2NFRzKvdnIJeUQHiMTerutq7s1lQi5QjyPSWcFGFLCJg6vZ3ros1prbCuP1npJP5PHbyczJwNXikhj3UHmMjGaNuxEEAtPODI0Aq5k1vnXy27R8QGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc13a6650.mp4?token=AOP8sfJbiD8uBUDBjPryvgezS-1EFlRqd2vSNsNFdhY5TaCHJgzAqbKJWmO4ddCaa5nX512RygSeWL0sLku7ECQDjPs_is_pUSbSdbAlYgBRMM1LI7sOtKgDwioGZjsNLgC75TtHtIDZHNtgPZndTGcudqLKc02AG-EffSgMLWtx9UanWDOuqxfxsOYYO0mbz-vongYvdkEtpgIHz-p3NT1ykurXvFvr4V5-2NFRzKvdnIJeUQHiMTerutq7s1lQi5QjyPSWcFGFLCJg6vZ3ros1prbCuP1npJP5PHbyczJwNXikhj3UHmMjGaNuxEEAtPODI0Aq5k1vnXy27R8QGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رفتن با یه هوادار نساجی که لباس آبی پوشیده مصاحبه بگیره. هرثانیه‌این‌مصاحبه عجیب‌تر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/28015" target="_blank">📅 23:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28014">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCC1iFKI2FBwJ3w6B9zhB2c5mz1CHNrZj90pdWls4uPv3GQUyIuJ9BViQS10FW0iNcfWA-9e4wHJrcphYtprtivz_TmGg6-nhLbSaWOBHCG11WagQCHCU0x0JnZikl26gcrEfy-ug9C-M6IbI1nLuFAc1T9jzIJo5qJY3_KVdrmRMsmKrT5SwbnUBGrbNfPKlDhT8gWblirxCIzKRxTYcN9Yl6GI1dcXcpIxTKPdQz06hnodyE8NvuifYfjBaVOORpp-f3Ml4Pf3JRAUJckxAXrruD4GeUEz3b5JKSZijgI7cxlGjD2QOGKnLJYzP7SIP_74zNNviIslimQbuGjekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمال موسیالا ستاره جوان بایرن مونیخ تو بازی امروز بایرن‌مونیخ دوباره غش کرد؛ رسانه های المانی میگن موسیالا مشکل‌قلبی‌داره و ممکنه پزشکان او رو مجبور کنن حتی از دنیای فوتبال خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/28014" target="_blank">📅 22:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28013">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO9b-g7r7a_HvjaQDhUCpBZBT4YRcT2R3wHY_kCAXrbJ4Hwbkt2_cQrWfxuAKaRjDslloXCieptVkdZJFFJw1cZx4PpH4dC89aiT1bPVa-dKpkPWn7XYLQQqjRtXa97r8FQOryVUSTwYPsn1h10Cfje9TGjaoWbkWrVKiWraAlJpVSOuItvmhUxtLlXSE6OEm_9m5GxWj10UtbyddM7fmzWNaPzAAN4sBYacPDt-6L4D3glX6lgGWpJB3yXwWHE9JqROPjT0B1UPRfjZ0vM8CnRkPBpOP6i5uJqqQyObZtEOQMxZbYpZrVIukPx3EhIg99EFbNOsSov_wPFkmBFmOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته‌سوم و چهار رقابت‌های لیگ برتر؛ هفته سوم دو بازی فوق العاده حساس داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/28013" target="_blank">📅 22:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28011">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cggMpG5oPElAFht7Bnf7Q2Huefq7LKhNy5kzfGF3qFFqnTFY7krmjEuZET2zDacSB1Ag4EHLq_SRCZ9sx_crspZZkCYt7MYtyqPU_eTc7HTqEVBTfJab8_0HnlQIa6AnoKJU8RfJUQS07Rl44-mV6u9VRKJesd8iWkkUNdgDZp9l74Oew47VeDUCKZGZRUcpoaiB-DVkyS9oFn0USnF1QUToQmEd_6FBdjDoLGGhAp41N_WQ0UDMQK7eoytq0hlw7SMqEeOT418kFvj2ptn2wzCjsm94hg7i0aN6c29jdAPgKbZnJoT8Nvn7YYxawBb_bmi6buH1PUeEPRwjJj5S0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrgxQZ4X4Z5txGTVGiAbbGlgy4xP7u42KZrfwtl0OnyZXNL0IH02nZOfIbC4jG4KrrG-7LBE2KDw8iPaqMKdc3vs6K4RYVaB6_85TfG0-Sdk80JcfDApwx0ulGNN1q0QC0mgX_YX4bUolMpaR9IqN1kMqiswiqiUVyr59iDMC-OE9b5vto308WsUwQ1SzPDuqkJ0JsshmghS-W0rlCkiz1380Z0bhyHqz6dFlxd_zT5GQgLs8dH68Xst27dDRgA7FYw5rJSL1VScNLKmO3dbK9S9h9iG2h1mljaCV5rl-ig7gMluVzoGixqUtLadYesBSTKlZF7sC8SYSxVbm__67A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌ونتایج‌بازی‌های‌امروز هفته دوم؛ ادامه مسابقات حساس این هفته فردا برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/28011" target="_blank">📅 22:06 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
