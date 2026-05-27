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
<img src="https://cdn4.telesco.pe/file/jgbFB-Eiw6AhjbiKjitEwtcqtuInrvqg76cb5mGF7hxvuKYkXhcEkMplmptFXPCmkw63_I_DPxu6fLdrX8w3iIx63J9mrxTBu-ZS5TkzGeZqr1gDyEHNUMiBBAceV_9ITI5KZh_TfGV-jJQDkbazdm1MljtdykuzqzFNqpeWtTIzGuQni5GpVm7viA-XMboTMbqz_wNXTKwP1kyphCyV6cxzvq1u0zySVeImvi5eJSl-TKJNaRVIH62oWMJMoqsxvTZAMcFrIWjmXY90-tIvB9KigdXZF-QogN5s-WzFbHw623-EfNt-FU40x4mwAJSQCDNfOmfscyOXASRN1JVkrg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 926K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 23:32:33</div>
<hr>

<div class="tg-post" id="msg-123175">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
گویا گوگل پلی تو اکثر مناطق وصل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/123175" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123174">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrp6A4vnVlAdbjc1sGIbEg4XJCxIWNoyHRwTFrACreR0fis3LO04cdxrI2j71FkC_guRSNboiLOvx9Ympd2oNRcm77GolCPUGigrUPr0MTmBV759GmcdDYZon_D2hkLK6x8exLAYtPCTvj_yoOIDA2XMZ-IeerQE-M3GfslBR9EUYC3XJ-cFwO-aHDaVYykmB1_Q3-0f_AYZ52zDldrd4xYfwBN8J5kYUrU1YZifdZO2hwJ4F6_z8z0fq2BqN5W1djjUeb1aQm7ZapVnOSpiVEXETdSUwG1sX8NGhvnbmQGMAtAMw2ZIhqTT4XQrsSj5qda4mWZomFfxhQbSsM8cvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جایگزینی تسلیحات راهبردی مصرف شده در جنگ با ایران برای آمریکا، ۳ تا ۵ سال زمان می‌خواهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/123174" target="_blank">📅 23:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123173">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
حمله امشب اسرائیل به غزه
🔴
احتمالا ترور
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123173" target="_blank">📅 23:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123172">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: اصلا چرا باید به آمریکا تعهد عدم ساخت سلاح هسته‌ای بدهیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123172" target="_blank">📅 23:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123171">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuYQFrLab-lr0s96qVEwSWm5rdmdeFf0teDoa__IG9NO_fv5UEt4OHPcowHbj6nXp27ZDjojQerOcEe4JDdpSyTHzqqCHm0TkDd61Jy5juqFtsBnCE86KyaT3rWPu0fDsRWjzD2k9zYZ2HTpadLUQNJFsIkXed0qmYQRlnm6ccBEJw_i7Gyou09EsQ8mR3K7cuKlpgs2WLOLNBHvERZygLEtftPJ-hNcX7n-220gVNKn5S-IOGsTcvxDvUCATYBPVvz8-d3ZBa7IBK77Z0Qhuz9aLIzF3uUDcMZlPAHA1xxJPte_KS2MnOhS7NDwvBbI2YmiflmFeGo3bFLq8pUd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله امشب اسرائیل به غزه
🔴
احتمالا ترور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/123171" target="_blank">📅 23:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123170">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی  همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN  @NetAazaadVPN</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123170" target="_blank">📅 23:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123169">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iDR9EkrUKKnrKSf_Z-q7PebyREsciJuPlp3xjMDesGeUEZYuvonMBfjZQWkMPhSfmVBgwY-Uw_REc_-pZzPs7YgH3aceiP_cctNmk3twyJkQ-ahbkqyH1VLoR1TAHKhTfC9-MOGUVLqgOK9STPu6trxNSgkyZgfQidkKklBPUZGcis9hYB6nWz_KMWlpTv6zlaf0yJwyc2EqfBBkw33NGzfSZn6t0qu2Pc4VyVGKanw3ImViNFR_tNkZQOflI6q1VlDJkkYgm_pGf9uMFX-n0A1TCZHK4Bpuu_9AfsKheOl2XD9MfhlkCxp6H_aeN29kNbm7Ip-zDqwzNNiT3OzEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی
همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN
@NetAazaadVPN</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123169" target="_blank">📅 23:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123168">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmAy379_kxZJo_pUnF0nTSGDz-nzu2_H95SePD03a6NmUleEBhCbpzbpGdbM_oIOhRFZezCNukIQVpUtXOdpCJPwfx--nokjh1atLg1n6Xf23sfGs0_SzlzO80MugBIA0F44eyjrV_LaZMy7vj0GqklRza3jLkv7hnEZ_79DFcOGgHEEHCiiKZ2VDLE86iPkw9q2_YbOIWk55Xk8y9PiG6D4hb1r7vKWcQCpkgO_aqA0ZdadNIKi7C-FbseyEgqZToEHTjqExXbKh8CDD0uptJQJKUFZZOHDMYb5nDMxiyQeMilXi_hSiT2A0WVHD6eUMluJx_Jelo0f05_ntTXd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
کشوری فرد، دبیر سازمان لیگ: پرسپولیس به چی اعتراض داره؟ اونا حتی تو جام حذفی هم نیستن. 22 بازی نتیجه نگرفتن، بعد می‌خوان تو 8 بازی همه تیم‌ها رو ببرن؟ چطور وقتی خودشون میرفتن آسیا، مشکلی نبود؟
@AloSport</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/123168" target="_blank">📅 23:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123167">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بقایی: موضع ایران در رابطه با قفقاز جنوبی هیچ تغییری نکرده است
🔴
سخنگوی وزارت خارجه: جمهوری اسلامی ایران نسبت به نیات بدخواهانه امریکا که سابقه شرارت و تجاوزگری در مناطق مختلف دنیا دارد، سوء ظن شدید دارد و مخالفت خود را با حضور ناامن‌ساز آن در قفقاز جنوبی صراحتا اعلام کرده‌ است.
🔴
موضع جمهوری اسلامی ایران درباره امنیت در قفقاز جنوبی روشن است و هیچ شبهه‌ای در این خصوص وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/123167" target="_blank">📅 23:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123166">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
امانی، سفیر پیشین ایران در لبنان: حزب‌الله برای حمله به اسرائیل در ایام جنگ ایران فرصت را مناسب دید، قضیه راهبردی است و اینطور نیست که حزب‌الله بخواهد در این جنگ طرف ایران را بگیرد و موضوع تبدیل به موضوع کلانی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/123166" target="_blank">📅 23:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123165">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd6cb21c5.mp4?token=Lw2_iM77oGDJZgleuskJvaqtzv74uNgV3aWJEmBrTnVBvnOVd7P9EuzzXhTkW5dV6CtdZIZmFWHStmDqHUzYYF_r8KJhDMa2_aYFIjjAsNg87-TQ4hBW6ArJ3R_reNwRYADbYmqIsJsH8Uu5NZcNx5LMb6OqHl49bj2eAoKSeqQ3sAzaE68NQQfm7Rc97jByb_R1eygqk6Txay1BTQPxGKHjXI3380WYs1D0uYkvBpTjkSu3R1CIKV-3XjDErrHQeKOwQxJYKnoSDjMp8X4DeCd1-OKqred2aw5XJgUPLOwKYXbe8_XB_GIrcDJ8kwbdi7IfHl6a5-7sZT44SNXfug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd6cb21c5.mp4?token=Lw2_iM77oGDJZgleuskJvaqtzv74uNgV3aWJEmBrTnVBvnOVd7P9EuzzXhTkW5dV6CtdZIZmFWHStmDqHUzYYF_r8KJhDMa2_aYFIjjAsNg87-TQ4hBW6ArJ3R_reNwRYADbYmqIsJsH8Uu5NZcNx5LMb6OqHl49bj2eAoKSeqQ3sAzaE68NQQfm7Rc97jByb_R1eygqk6Txay1BTQPxGKHjXI3380WYs1D0uYkvBpTjkSu3R1CIKV-3XjDErrHQeKOwQxJYKnoSDjMp8X4DeCd1-OKqred2aw5XJgUPLOwKYXbe8_XB_GIrcDJ8kwbdi7IfHl6a5-7sZT44SNXfug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
من خود به چشم خویشتن دیدم، که جانم میرود…
💔
جاویدنام محسن جبارزاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123165" target="_blank">📅 22:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123164">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
بر اساس گزارش «گلدمن ساکس»، تقویت ارزش دلار در نخستین ماه از درگیری میان آمریکا و ایران، موجب شد تا نهادهای رسمی خارجی اقدام به فروش اوراق قرضه خزانه‌داری [آمریکا] کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123164" target="_blank">📅 22:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123163">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: طی روزهای آتی میزان پیشرفت در گفت‌وگوها با ایران را ارزیابی می‌کنیم؛ توافقی وجود دارد که می‌توان به آن دست یافت و مقداری پیشرفت و تمایل مشاهده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123163" target="_blank">📅 22:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123162">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBqhJjK2WnZTBT6oTmgSA7Q-8O21EgDkG8-pPZs4h2K3QFJbnDmM8p1vb96QFjdqatM1RdrWrZUVr2uLtcgHnd30_FGCFdse-neMfsfYjcDrJwK5MKSm_2DDNhZes8lY3IOAH4eNF1MNl-RaI2MbE21IE1gBovfW2JEyTb3EUqtUW39aHFMYwisOOfYst6a4XlnUPKR3yWB3s5xvOiF-i2yVVIZx8aHbDV67wB0E1FA44ki3KlU2wFNquzbzWqvkvQ3ADpMc7inBAXVZ9BKAe75t61spEucOuBdbfsi9kx7wg9_dHj7r3aBkS4u3uMjj84IFzY4kvz6gJyWYmIDuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز: نزدیک به ۶۰ میلیون بشکه نفت خام ایران در نتیجه محاصره دریایی نیروی دریایی آمریکا متوقف و گرفتار شده است. این میزان تقریباً ۶ میلیارد دلار درآمد نفتی است که در حال حاضر به تهران نمی‌رسد.
🔴
با وجود این‌که هنوز نفتکش‌های خالی زیادی برای بارگیری نفت در دسترس هستند، اما به دلیل کاهش تولید نفت، میزان بارگیری نفتکش‌ها نیز کاهش یافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/123162" target="_blank">📅 22:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123161">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
الجزیره: پهپادهای تهاجمی حزب‌الله یک سرباز اسرائیلی را کشته و دو نفر دیگر را زخمی کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/123161" target="_blank">📅 22:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123160">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgV2G-sCZtKzS32qtW_0Cy-mIfVIEHJOCZ50arPvaLfgBTxagxT1GwqrtVfnR5paaP785nbdkdHhrIFeut9Jt7SP-MQ9rc5MFYjhZK1x6tZsGP08z0InyLQLUBdgm9kSL9G48eHU0JxTubyKewHEIoLuVrbzyGuMN3wQgn2YnaOWxA6YH0UL0atxsUaz_AT_F1q7m2LZWE8ZM5vbXFMP89c-XrKqbzx7go7C1TXY49AYJOHsym65ZtHwoIz_FbqTnRNDeA39U_iKqRnNStvt51WA_1dUBH62JzfkZIToQ7MNNO1lLb0wY4CAhTPuOu_RVFc6xcQJeXZRPFbmmxooPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینم از وضعیت اینترنت وصل شده
پر از اختلال...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123160" target="_blank">📅 22:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123159">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
هلند مدعی ارسال مین‌روب به تنگه هرمز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/123159" target="_blank">📅 22:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123158">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
روزنامه‌نگار چینی: آمریکا و ایران به پیش‌نویس توافق دست یافته‌اند، اما واشنگتن نمی‌تواند تصویر «پیروزی ایران» بپذیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/123158" target="_blank">📅 22:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123157">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نرخ ثبت ازدواج در دفاتر اسناد رسمی با ۴۵ درصد افزایش به ۲ میلیون و ۹۰۰ هزار تومان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/123157" target="_blank">📅 22:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123156">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGRd7Rv2pbNQ_2KzW6LHTihFbITzR1mCZDwYIaxX9_RhHjX6h6Srhn1XkPRd6Bvbd7n7rLUWZtW6vfQRl7sEoJfmPHaV8extciDHsLHL4Jzj4cQOEi7gYPZ-5rXxDFfWAilD0oxTXXNbp5N_36ki3itwx-l0ZXxy2WAnm7qY5QvulNnU3TmqtOlTd4Z3JNvTfvMtSjOBo56a2nzKCY2gxefjDaJSX78huVciFTLzl8OWX_DP_yoJ7kyFiPlD4UwYimIVvcoldawKSoJEILWcKsLLtT6Klt6SHS1GquLa8g8KNjBBDm8OGCgkTmLAgNS5Hyzxf-d_VfTC3HAXhV32Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسوشیتدپرس
: تحلیل جدیدی می‌گوید ایالات متحده ممکن است به ۳ تا ۵ سال زمان نیاز داشته باشد تا انبارهای مهمات موشکی کلیدی که به شدت در جنگ با ایران مصرف شده‌اند را بازسازی کند و این موضوع نگرانی‌هایی را درباره آمادگی برای یک درگیری احتمالی با چین برانگیخته است.
گزارش می‌گوید تأمین موشک‌های کروز تامهاوک، موشک‌های رهگیر پاتریوت و سیستم‌های ثاد به شدت کاهش یافته است. حتی با افزایش هزینه‌های دفاعی تحت ریاست جمهوری ترامپ، بازسازی موجودی‌ها سال‌ها طول خواهد کشید زیرا ظرفیت تولید محدود است.
تخمین‌های زمان بازسازی:
موشک‌های تامهاوک: تا سال ۲۰۳۰
موشک‌های رهگیر ثاد: تا اواخر سال ۲۰۲۹
موشک‌های پاتریوت: تا اواسط سال ۲۰۲۹
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123156" target="_blank">📅 22:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123155">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه مشت جاکش هم نشستن اونور دنیا چپ و راست میگن مردم قیام کنید حتی اگه شهید بشید! خب جاکش تو خودت میموندی همینجا قیام‌ میکردی نه اینکه گوز گوز کنی  [@AloTweet]</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/123155" target="_blank">📅 22:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123154">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
فرار گوسفند قربانی روی پشت‌بام ساختمان در الجزایر!
🔴
در شب عید قربان، یک گوسفند قربانی در الجزایر از دست صاحبش فرار کرد و روی سقف یک ساختمان دیده شد؛ صحنه‌ای عجیب که ویدئوی آن در فضای مجازی پربازدید شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123154" target="_blank">📅 22:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123153">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGva6NzZz5Vu3qZbor-dgILuGV25ji3Ls89FMrVpTFy5gFqfBKFujN-EKkYxVio2HiD020yYvLwHsSBVJyErzMqp45ks38304obW13YbcJuoH82UQKBvnvp3Tz4P8-ngVf4w1Q_MYhbX_2M7ChEyudJIO_0v0bWqr8cPAO9eguuR5732p85PvDiRwNpsoCHiEx8sUg5woPkOEntog_qoTE5bqX534lX5cJyhK2s6FZ8wym6jAlHdDOiqnNUrChqnX9BgyMeaiPscFfUcJZVacnGqiZUOujha3i9FgkNPA5I8DBdgn1EyU7bl8zXVSuNFo-uIVnI-Wa4MBOie1mBF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123153" target="_blank">📅 22:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123152">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
اسرائیل هیوم: ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/123152" target="_blank">📅 22:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123151">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJkmYH7PxbqNPQ8WafnWh0jL1cPhgvbXO7lPwGlPOy209tfcUTUYysARaJPostjukQPxqbhgEXp97dyCsZo9I1V7XEr9AmS2fU4Gl2ItEMxJdhtRiXG11Hqi6NJ8228VGxgP_qmNnhigYVnVYVb8QuVplfDgnevY7_WIsr0tZyuL6E_-eBXAlbH3tnHybJZmr352yTyYJdsbvl6efOnCJt5TDY-UEaxrrAHrERIjwYe_pNtgRgI-ApNDXIqrxsRt4iEa6-ALXG0ro6ALqG3l__1jYX9mza4JbcQl6KvtI3zv-z1iU2dsz8_E2tQnFP9qEoTFov4JLHI73mvAuUPRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ملت کارزار رفع ممنوعیت کشت خشخاش رو راه انداختن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123151" target="_blank">📅 21:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123148">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78b1410fd.mp4?token=aGY3wsaul5vTT336uH0FzzFNPXz2qDzwdA84QOWe1_KYoyGNPwj2kFiuG5-g4he0m3KpPaCoAjS_rIQ_hp8PXKS8cCJqis-GYpTrxAr_8j0NiD4JoSBjYtPNbO3uDzddryJNAO6kJXxjy4DbAteJUd8ElKd-ZDlOSVgVDfNVOwDUAz3yIs9kjfitKR3dnvh51TQ3KmcfVL3yrFz1jgMGy9ZXjcjQQP6EzHpGV_DzBbRW-V46-8iLOus8jgzATIQT-QJXnpQTsk1nP61LiC-gWSF-pSy1mpBOIOKrOVwGoaehRp7lDlUhtZKhT82lamlgDtzP6sXTXrHUPZ8qlQKNfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78b1410fd.mp4?token=aGY3wsaul5vTT336uH0FzzFNPXz2qDzwdA84QOWe1_KYoyGNPwj2kFiuG5-g4he0m3KpPaCoAjS_rIQ_hp8PXKS8cCJqis-GYpTrxAr_8j0NiD4JoSBjYtPNbO3uDzddryJNAO6kJXxjy4DbAteJUd8ElKd-ZDlOSVgVDfNVOwDUAz3yIs9kjfitKR3dnvh51TQ3KmcfVL3yrFz1jgMGy9ZXjcjQQP6EzHpGV_DzBbRW-V46-8iLOus8jgzATIQT-QJXnpQTsk1nP61LiC-gWSF-pSy1mpBOIOKrOVwGoaehRp7lDlUhtZKhT82lamlgDtzP6sXTXrHUPZ8qlQKNfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های سنگین ارتش اسرائیل به صور جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/123148" target="_blank">📅 21:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123147">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AszSncYCA3E1SstWkg4lFZh4r8JHcfXyFmyV198CLEeJEvyTrqHOfzmbnuSiC-5oTXASZpWhQ2yJ0oE9qYsrg3V2FAoPQNBNUZxsEXju9mcu6DLkcA7pvfoDYEteP5v844D48fQwhkaCmg4o0XXfOFvj5RJE-JFTSD1RuZMk-EEQR5RKHjfGrAerLfNRxpbYT3iro_WjWjLBbfvvM1JAIWKVHs6ko0Xxqa9eq5_zNUwpbVSl2ZRdCbtjJg0eGUllfW0ulsCNhNcEdB94FLznIZPDDyRjnqFDIX3e3lbTrXqfLMSEllco9MzY2jNVp_7MQ1GmbgNdzemzgOTyq21KfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک گاومیش بنگلادشی که به خاطر دسته موی بلوندش، «دونالد ترامپ» لقب گرفته بود، پس از آنکه ویدئویش در فضای مجازی منتشر شد و مشهور گردید، از قربانی شدن در عید قربان نجات یافت.
🔴
وزن این گاومیش ۷۰۰ کیلوگرم بود و قبلاً فروخته شده بود، اما دولت به دلیل نگرانیهای امنیتی و ازدحام جمعیت برای دیدن آن، وارد عمل شد.
🔴
مقامات پول خریدار را پس دادند و حیوان را به باغ‌ وحش داکا منتقل کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/123147" target="_blank">📅 21:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123142">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AeW9BOHopE6BDD5ihths90YZqRoumcMjOSkyjYP9EjUKAlEMKrtVqe4E7CDdUq4buj_NY1BRojwBrBCnZSVl7p2EUE2yvBkQIZ_cuwlFk3LEoZjEX-Ysb4H15KKamTePwfZ6d2pMsEX1FigL0ohR76yWvu6Q5bzi9IQBg9VgDxl4Bimcq_z3JRM4KmwHtWjMs3TR2Kyz0yGA_oCQ4Lelq8E7F9YFkVdtzB56itwRmxQZpPD8tAE3RisA8vmkIa2UWx7y83Jxu-xrIIuqObxFSNTuPjeJNA35EUVB7VQWmqAap5m-is-tsTM2WqGl0j2hCe1aXX5edfdkkpaM-RFv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWgXxi107mdY-P_XNqOvahBaAgjmQyfufSuvVkCNmN3BgD9AteQdYAedNGuKDVneUx4PYwJROVvDAfTxKjdAjnRGrBrvr-fkDjBjKUE7VLLht7HntJYOIgdV_16ypMBr5IxMO4KGQZ-koA-Ag5by5SoyXgf65J6sSsbQWBBof9LyI9BM2ld9D7Je7yQutqw0W75391n0pWdIk3np0q2nPfWaSXsed78mlROO1r_Bvz_c7xJKJTEB9wLuI4_Xxx_MljDttrxLS4LAANPVApCzx27Iv3TUnzLDPHiOXvrFXaLyOwAUHW5CKT7fybLmbpTUoC5L61zK5Tj9lIzYSNX1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbcyVcEMXlUo1lX85UadzEw6x9QN85jXwshu8STj2hGnFEhxuLIIzePq-7yEnc08_o_bmpS4a4-zr7jkWa6ZUn3BxxiJ6B5kPlKAM1Ab8berk0VDkAEtZcUlDNK-fx--IOt1QlOHeuygi89dEWSP1yl9GQ7A40QTTKpWctDL8T6ANHg9taQvtmaWvAKM3q9UE2zKUMPtbEuEI2eVG1Fl4Mvwm-XTa2HwZka2Xx2hNZ_TVfbeNIHGbs981jkSLk_328wO7m1TnTeUdQp5KEDQqOh4aUsifaqpSjvgAKB_25CZ4SDNYCB8rkK2EBaUn-dY1S9XNMTRSyxA3dwFSLiShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzLArf0v0ey6w0Hikja1Uk42eHCkrohG5vpOfME2VTz5s1p-aV4ulL7-W4X5H6LqG4smRPssIrXfp52kzjihaIEOb_Begj7QwbIk0EXLqcaqZOHCyZy1hWP_GccjzZzoFj_IJmaxSsd0Z9971OFERYxTSj8C1d1gqgOnQvfF8HagCFNO6h-dyveBUIRwpKPKDWG5qX3BO0O-7GVADiStwxq-ChGYiEpFGsG_5rS4YKb18D9V_RyH440ZeMJtfDKUv6mQHSGyowr4H6Cm2p33tD8BF_DX1kbfwJYA7p7HKSTECvVvnerVuwke7Y3IECgbZ2-ckDUBst7xvz_7ixqdtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e5e9e4dc3.mp4?token=PtNmyNAOo7lY3eEfvkzo-uwvdKMv8AjxUWrTc8c7VpZDaykqga0kY7aH3_URyrBXXn7YlAmo8zENFE95oa0uN_BWq1-DPptFJ43v983-uS5mFWHMc0Mo_a8AINVtDj0pUyGCLMqnmdfrKOXvdszrGShEcOnqy7VGAK5ikfSb1hlj4oTiGJsZHAivL1psvWVEimGBvIbLyYSQKSnjFHHv2ajBnu-GTAZotkcqyXyYaBa6yeIY6BshrI8gCKt_0_7YJyUMorUZflRAPII1-nJWhFKnf1WAkO4naZnA5JEIb_2Dsr0IY6Iow0IKOvctVkcl6aHeYSfMdnCzunt79zxn2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e5e9e4dc3.mp4?token=PtNmyNAOo7lY3eEfvkzo-uwvdKMv8AjxUWrTc8c7VpZDaykqga0kY7aH3_URyrBXXn7YlAmo8zENFE95oa0uN_BWq1-DPptFJ43v983-uS5mFWHMc0Mo_a8AINVtDj0pUyGCLMqnmdfrKOXvdszrGShEcOnqy7VGAK5ikfSb1hlj4oTiGJsZHAivL1psvWVEimGBvIbLyYSQKSnjFHHv2ajBnu-GTAZotkcqyXyYaBa6yeIY6BshrI8gCKt_0_7YJyUMorUZflRAPII1-nJWhFKnf1WAkO4naZnA5JEIb_2Dsr0IY6Iow0IKOvctVkcl6aHeYSfMdnCzunt79zxn2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات امروز به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/123142" target="_blank">📅 21:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123141">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
تعداد تلفات لبنان از زمان شروع جنگ آمریکا و اسرائیل با اسران به ۳۵۰۰ نفر رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/123141" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123140">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a49d8fc6a.mp4?token=iqVuxvKvfhAg76AzpsDeoefYLYOCKgBZDjN7DQ04rxMiTJ3tEwSSXuJVkQsSf4m4h3Td43M1UDcsUP1hedWGNTHxShT0uK9KaUFuXt-t8nJwSoJDMFCfIoMArpFRtuLYoiq8N7PORvasq9Zsy5IkuNQLpVwJCU5o03CUEaBgoow_HSRYrK8mN50gByQTwODbd5hmHmEXqu1uBt8_sxu6IbCzCz_23-Og-U5ZJl3XfiU2rrPZcpmvYI-hNDcK24cwc5deC1jGeEF36FGA11iTc6_4lRGw-Tus4blBl2DdNx3IaJt2vrY-m083tFcajKYTAqwZoGiFAhBuvNk4dV0JjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a49d8fc6a.mp4?token=iqVuxvKvfhAg76AzpsDeoefYLYOCKgBZDjN7DQ04rxMiTJ3tEwSSXuJVkQsSf4m4h3Td43M1UDcsUP1hedWGNTHxShT0uK9KaUFuXt-t8nJwSoJDMFCfIoMArpFRtuLYoiq8N7PORvasq9Zsy5IkuNQLpVwJCU5o03CUEaBgoow_HSRYrK8mN50gByQTwODbd5hmHmEXqu1uBt8_sxu6IbCzCz_23-Og-U5ZJl3XfiU2rrPZcpmvYI-hNDcK24cwc5deC1jGeEF36FGA11iTc6_4lRGw-Tus4blBl2DdNx3IaJt2vrY-m083tFcajKYTAqwZoGiFAhBuvNk4dV0JjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمهوری اسلامی در 18 و 19 دی مردم رو به گلوله بست و مدعی بود که این جمعیت معترض تروریست هستن.
🤔
دروغ از پایه های قانون اساسی این حکومته
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123140" target="_blank">📅 21:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123137">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78b1410fd.mp4?token=QQj7LjFk9aZm6uxxllhjWGhyVFgyFl6M5ZWQpcmUcPtKy-XwDnwEjbwFF87lTlTpKFYMqcoPqN5sSkrgZXQcbwaQXx66ZR39dZ6jeywEGzOwxrlv03w2QxMNWZC75pGdljrS7HfpXqwRlMOZF7Uq1g3an5AB4-RFZdhpEqc592i26IFLTwKn1oHPNGpvEidjOVy6DpHzh37IC3D2AdoDW252KoahMYZjPVRODQrVE-Z1Bt6GOLRPLeookXDIJTG8jBkp8p1pIvxMUOFqEA_b3BvVlb6nUMd7vjHDuc74B9wqUjXZv9GUBcfB48iQDXyuvN2hJ27QK_BSeWBVKyW0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78b1410fd.mp4?token=QQj7LjFk9aZm6uxxllhjWGhyVFgyFl6M5ZWQpcmUcPtKy-XwDnwEjbwFF87lTlTpKFYMqcoPqN5sSkrgZXQcbwaQXx66ZR39dZ6jeywEGzOwxrlv03w2QxMNWZC75pGdljrS7HfpXqwRlMOZF7Uq1g3an5AB4-RFZdhpEqc592i26IFLTwKn1oHPNGpvEidjOVy6DpHzh37IC3D2AdoDW252KoahMYZjPVRODQrVE-Z1Bt6GOLRPLeookXDIJTG8jBkp8p1pIvxMUOFqEA_b3BvVlb6nUMd7vjHDuc74B9wqUjXZv9GUBcfB48iQDXyuvN2hJ27QK_BSeWBVKyW0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های سنگین ارتش اسرائیل به صور جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123137" target="_blank">📅 21:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123136">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibkGd6Xtqx5VbbWKal_mJInoqfyBGRp-v77T0i30EyE0-OhTVEFs1zO87widCqy51pJCt9bgTeHgGzDq0Wm5o-ejlK2NBXC5wIYBy-nujB_CHrLhStW2vgrNp_jUGkMuf__w1pKX1So01zydh5syiw042TXBpV-AA_zb4K57CpmGuqZyiy9GvrNbA9C3SuyN25jbBwW61UvQNbGP0uP5tKqegKysjFTYW-PpLQJZ7dsmuGmKabzg4ep0KX9mqqs1pymWe8OnoclKEatT6CWRfnSoHbTNVtmp89Lg431VuPmK6fOSljCeuZNMkXeRisHPQkEwR_YTGfPacyA2cIYXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله به پزشکیان در تجمع خیابونی‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123136" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123135">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سفیر ایران در کره جنوبی: ما به هیچ وجه به یک کشتی کره‌ای در تنگه هرمز حمله نکرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/123135" target="_blank">📅 21:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123134">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
نروژ تحت توافق امنیتی جدیدی که در پاریس توسط نخست‌وزیر یوناس گار استوره و رئیس‌جمهور امانوئل ماکرون امضا شد، به چتر هسته‌ای فرانسه خواهد پیوست.
🔴
استوره گفت این اقدام در پاسخ به وخامت وضعیت امنیتی در اروپا، از جمله تجمع نظامی روسیه، بازتجهیز هسته‌ای و جنگ جاری در اوکراین انجام می‌شود.
🔴
نروژ تأکید کرد که در زمان صلح هیچ سلاح هسته‌ای در قلمرو نروژ مستقر نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123134" target="_blank">📅 21:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123133">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDOoEcWEjTZVWYkzt8VfL0-sl3rIA-xbOrMUDnnJxTOgb1yJ9W-Zr3_kAMwoN1Z1ps_1cf_KesA9L4Ycn3xG0CLsDYfTX8mp8-iJVonL5yGM3Eo-QamBb0DQZ6Ipaf2P7Mtxj65nHjDOIClI5owX5PLFzs1v109f7ipAETU9R8pVv_2vvze40WvMzyZ9BV7bCmSmwanesoz1ValX1tcVDbBDsb05EoEXyCMJk9QYmJoion1pU9Cgs8hbmaJVXWUsNaCBwr1oYhqx6U4kexJ-tac1WIxaKlnWSJqWBhSQEGmdX13TCcJ4fcAE5hoUcaMU0Yu36hQVYn2Wdho0JCq-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر امروز ماهواره کوپرنیک از وضعیت دریاچه ارومیه و مقایسه با زمان مشابه سال قبل که نشون میده به نسبت پارسال وضع دریاچه خیلی بهتر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123133" target="_blank">📅 21:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123132">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG4GMriDK-z18wjKtVzaQLEdpC64DXIJ95BEFqSKZRRUPCviScAMuMH-Inkm19sf30vJGw0txIzYjDDaj9SMWdlW_yfQb4PWzTpoo4P_Py42ZL0vckQ4Y3eA7_VBDTyMO2eoEC1tqVC3i_EKDagIO9liFkFFN1YdKqVK3qQ8MvG2laYnEsRBZHQY3wZC7f5a_loI8tZjd6oLs3nkMqHP9Wp6CpdUC9umJxESHD_mY2cO6Q3uoYhWe-jSOQhhVkY1PIIpBJrUfIFfCKAi8EbYy7pa0PzyvRTMpVPkdpzzVa7Hy52DSKnuLVTiyHnBDX-_uUz1E852TY4IxLkVQNhBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سال ۱۹۳۶ که درهای دانشگاه تهران به روی دختران باز شد، رضا شاه قدمی برداشت که حتی از مدعیان غربی هم جلوتر بود!
🔴
جالبه بدونید اون زمان، دانشگاه کمبریج هنوز به زن‌ها مدرک رسمی نمی‌داد (تا ۱۹۴۸) و هاروارد هم سال‌ها بعد (۱۹۷۷) پذیرش کامل زنان رو قبول کرد.
🤴
رضا شاه روحت شاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123132" target="_blank">📅 21:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123131">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
بلومبرگ: رئیس‌جمهور ترکیه، رجب طیب اردوغان، در حال تلاش است تا هم‌زمان با برگزاری مسابقه فوتبال جام جهانی میان تیم‌های ترکیه و آمریکا در لس‌آنجلس ماه آینده، دیداری با دونالد ترامپ ترتیب دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123131" target="_blank">📅 21:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123130">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
صدا و سیما شرط جدید ایران برای توافق با آمریکا را اعلام کرد: پرداخت غرامت ۳۰۰ میلیارد دلاری از آمریکا به ایران!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123130" target="_blank">📅 21:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123129">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ecae41bf8.mp4?token=jNVu2fEGYkrcORGbZHe1pawUjAe68XCvWUc8mmSoxyxbg94f8l1VfWAe1ovUy8ZsomrFaw9oyj9WZObIHKN-KT7DUc1AudviBc2-26iP-2iX9QjjL5QI69vVHPZx99t1lZjcx15JkfzQs9uyAeVCPvhMerXf2R9KodWZddQz8oUKKyrTbhoZYrXiEg4NbEmGM51l6dvWuvR76tiYMUtzXjer_P2sNg4y9Ys3z0PjfzT0YhxP4QshXc5n87gDcbzfPGqoyFLWIJD4sfbr6bZZaUca3IxpyrivuJTMkJeKybZowZUBHV5fAvtqpegy2CgxCjrJ45dpUfd4xBEIWvbTQYnn21aP3dToujaVlU5RATiSPT4WO-rheLrtBwzuHuc49yXbBeBFUbz8uOWtD5lTiL7tsvSqx7EROyu9qJA0VZMJBmtt71DHccttqlnx8SBnk3ypKQ6LE0uX9yT43z5nKsa8uUBTHZ5j6Cuf1odzjMaB69ne8XnUmcUXXFLZvkHirYyLNuWqqIAoZVygA0VSq9o_bKVDes-SeGV82dBY_Ihiz0anyP4y5GxLWv-oefiCBq1kWiusjDAvVohpiyo8htbDCPqJTB1aoOR_j-XpmUDoXvV6CUOfgI57OqP5P0KWRn8CL0jLbbSC90eG36H7uhh_w3BboNs6SI6HcsnlcKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ecae41bf8.mp4?token=jNVu2fEGYkrcORGbZHe1pawUjAe68XCvWUc8mmSoxyxbg94f8l1VfWAe1ovUy8ZsomrFaw9oyj9WZObIHKN-KT7DUc1AudviBc2-26iP-2iX9QjjL5QI69vVHPZx99t1lZjcx15JkfzQs9uyAeVCPvhMerXf2R9KodWZddQz8oUKKyrTbhoZYrXiEg4NbEmGM51l6dvWuvR76tiYMUtzXjer_P2sNg4y9Ys3z0PjfzT0YhxP4QshXc5n87gDcbzfPGqoyFLWIJD4sfbr6bZZaUca3IxpyrivuJTMkJeKybZowZUBHV5fAvtqpegy2CgxCjrJ45dpUfd4xBEIWvbTQYnn21aP3dToujaVlU5RATiSPT4WO-rheLrtBwzuHuc49yXbBeBFUbz8uOWtD5lTiL7tsvSqx7EROyu9qJA0VZMJBmtt71DHccttqlnx8SBnk3ypKQ6LE0uX9yT43z5nKsa8uUBTHZ5j6Cuf1odzjMaB69ne8XnUmcUXXFLZvkHirYyLNuWqqIAoZVygA0VSq9o_bKVDes-SeGV82dBY_Ihiz0anyP4y5GxLWv-oefiCBq1kWiusjDAvVohpiyo8htbDCPqJTB1aoOR_j-XpmUDoXvV6CUOfgI57OqP5P0KWRn8CL0jLbbSC90eG36H7uhh_w3BboNs6SI6HcsnlcKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره فوتبال: من آن را ساکر می‌نامم.
🔴
می‌دانید، انجامش ساده‌تر است، چون ما فوتبال داریم و آنها دو فوتبال دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/123129" target="_blank">📅 21:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ: ما میتوانیم همین الان یک توافق خوب داشته باشیم، اما شاید نه یک توافق عالی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/123128" target="_blank">📅 21:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JuYvdSCCle2e6-oTaN3yrvMCk5q-Ot8FMi91iMyv7qAGfdBN-Bpm4idhkP1rwC3tSxfDzer5ctgB1X7P0riIZab5l1txhFQoclHwZ1PTaNgTZXAC8khmzx7iuW1S0yzVJou9tHpQOfwZxAbmJK7eYjU-VqaqwKvec6bYJbambUrT3FljC5Smxq6TvETX-35LLDV84VxlhSPp3Rjb3DnquSbRd0SLRRtHQQLYEkRsTz9ogfqJ_wOI59hUuJRZmBeu8k_VpcHrs6KRUVIOf311yfIIJLQSU2j0BA8YwGX5L_FiJH-Pi6X7SEzQab3-aZsUKdJqcDUeaU8IV6RIZmq-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کانفیگ فروشا بعد از وصل شدن اینترنت سکته کرد و مُرد!!!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123127" target="_blank">📅 21:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3f045f53.mp4?token=IccAodZuOZWV75vnVpxrUUU4GgAIHcMDpOciI8ZYA7i6hVXAQ111vpA0p4E6PbdnkvsfCi0G4rrUINHU-Ih43Bi09gYjf3Rxfu_KqhsCKE3_TFzvxjO-U0O9xHDyxcz6jgYW9ebWUkTq2-xggBaTp2MfBvbc3J-CfUpApiHGImqi7nccPtMtEHQbV6_4iArhHj-Vn_7Fdz42fGxW3w_3n8g4HzlY25r-A1Qosi4igmQcJukUlnRGzJd0R02kGEB_s7U3Ucv5l2QHpwqKCUiCyGRM8fpvKc-OGqnsoqBWUOVEzp1IcDFpv4Fvp4fxtTQjl-QqiSwxgcq0uCqNrQHunA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3f045f53.mp4?token=IccAodZuOZWV75vnVpxrUUU4GgAIHcMDpOciI8ZYA7i6hVXAQ111vpA0p4E6PbdnkvsfCi0G4rrUINHU-Ih43Bi09gYjf3Rxfu_KqhsCKE3_TFzvxjO-U0O9xHDyxcz6jgYW9ebWUkTq2-xggBaTp2MfBvbc3J-CfUpApiHGImqi7nccPtMtEHQbV6_4iArhHj-Vn_7Fdz42fGxW3w_3n8g4HzlY25r-A1Qosi4igmQcJukUlnRGzJd0R02kGEB_s7U3Ucv5l2QHpwqKCUiCyGRM8fpvKc-OGqnsoqBWUOVEzp1IcDFpv4Fvp4fxtTQjl-QqiSwxgcq0uCqNrQHunA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فلکه گاز شهر رشت، 18 دی ماه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/123126" target="_blank">📅 21:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyJBzQtKo1URd1FKFA73owxXXMG4-grPzw5_D0PxpAdhkktwWA-zund_oeWc6dFOE3Pwa7in6fAY-o4bu4tBPMW_hpfp6IJWoveP1ZcJU31LHX_pSYe7u9SSzhBXoRGZ2O-VVTdcWkNQlZM6Fh7cDqcUKNZRAknktS6pM5pjtazi0pLNJ93wlPq4UJYDTElyiyPbtID-q6HfxMoth-SbgrXQ56FlCKcWmu2xbAmRgNpEEDbXL8SteYzemBcrhnlJ_hOAZNIprxEalbW9hZTHgXGl_1y3PWbLlMecjTIvibJ8RbjDO2zxU0tK9q1N6r1-0NpiEj3b_u6zX5vtoiBJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش سنگین بازار سهام آمریکا بعد از اظهارات ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/123125" target="_blank">📅 21:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
یسرائیل هیوم: ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123124" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ: اوباما کشور اشتباهی را انتخاب کرد. او باید کشور دیگری را انتخاب می‌کرد. به شما نمی‌گویم که آن چه بود. او وقتی ایران را انتخاب کرد، کشور اشتباهی را انتخاب کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123123" target="_blank">📅 20:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها شروع به دادن چیزهایی می کنند که باید به ما بدهند. اگر این کار را انجام دهند، عالی است.
🔴
اگر این کار را نکنند، هگست آنها را تمام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123122" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a286aadd.mp4?token=VM7Dz_sVauEbsZGFe16RsT9rxoNczNvkJI_HSSxHv41xnUhBS852NpOUzdu37s2FhFI3sG702U_U2CjmYtG51xBiRELjX_tx9xnKjgYU2aog1-10XE6qHR0z9jkE4kkJ_p5FExxvqJ_uR35SFiRtHGM1ASan2i7tOHhGH1X-HVHswZcnxlyKXdCsTLTSFS9qz67NrVsZKC72F72eVAdDCCwU8TJMMXZPCS6VgPL21Sprp8FcniqbF3YsYE633WmLbY5d9XOIc7zZ39tonyUdCT_gnDh4D3kK8UCnC_q36PQ2gHQ5HnSDM3Dnlwfnv7erEcZmGiBRTiCw2zHbCvPVDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a286aadd.mp4?token=VM7Dz_sVauEbsZGFe16RsT9rxoNczNvkJI_HSSxHv41xnUhBS852NpOUzdu37s2FhFI3sG702U_U2CjmYtG51xBiRELjX_tx9xnKjgYU2aog1-10XE6qHR0z9jkE4kkJ_p5FExxvqJ_uR35SFiRtHGM1ASan2i7tOHhGH1X-HVHswZcnxlyKXdCsTLTSFS9qz67NrVsZKC72F72eVAdDCCwU8TJMMXZPCS6VgPL21Sprp8FcniqbF3YsYE633WmLbY5d9XOIc7zZ39tonyUdCT_gnDh4D3kK8UCnC_q36PQ2gHQ5HnSDM3Dnlwfnv7erEcZmGiBRTiCw2zHbCvPVDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: این تغییر رژیم است. یک رژیم از بین رفته، رژیم دیگری از بین رفته، و ما با بخش‌هایی از رژیم سوم سروکار داریم.
🔴
پ.ن : تنها چیزی که تغییر کرد مارک سیگار من بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123121" target="_blank">📅 20:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری / ترامپ: می‌خواهم عربستان سعودی، امارات، قطر و دیگران به توافقنامه‌های ابراهیم بپیوندند
🔴
آنها «به ما بدهکارند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123120" target="_blank">📅 20:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: آنها ممکن است موشک داشته باشند، اما در حال حاضر نمی‌توانند موشک‌های بیشتری بسازند. نمی‌توانند پهپادهای بیشتری بسازند. نمی‌توانند کشتی‌های بیشتری بسازند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123119" target="_blank">📅 20:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: به درخواست نخست وزیر و فرمانده ارتش پاکستان، به ایران فرصت کوتاهی خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123118" target="_blank">📅 20:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a107aa436.mp4?token=WKPk5QqfZFxMcY7onc6ktq1ObLH5A7XGQn8aYd8hyiMx8Z2uXnWWexgvnavhdSfR2HfzHkDRfZGsxPUP-kexZzBlKD-PP4DEMXZzgJPxw3KFz94GRuoqNQ3oJAPdc-yW6nvRm6tTiVXS48mLLjf1UFM54y5C86tPm9gTEf_nDOe59cm1K3pVIlrAgjy1o656-z8Z9tfMgFAjvRVxVmPCjGM3itczuv9ceQtt416ZPTLkwssy771GOY8jLQDpyz8UETjSGOb6Ykvn4jVvBpMjL6b3yIaQy5wPJi52nVaKRFH97EZkXA9Nm9xqC2PAdau2RzkanX4-ge6NM_Hx4i24KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a107aa436.mp4?token=WKPk5QqfZFxMcY7onc6ktq1ObLH5A7XGQn8aYd8hyiMx8Z2uXnWWexgvnavhdSfR2HfzHkDRfZGsxPUP-kexZzBlKD-PP4DEMXZzgJPxw3KFz94GRuoqNQ3oJAPdc-yW6nvRm6tTiVXS48mLLjf1UFM54y5C86tPm9gTEf_nDOe59cm1K3pVIlrAgjy1o656-z8Z9tfMgFAjvRVxVmPCjGM3itczuv9ceQtt416ZPTLkwssy771GOY8jLQDpyz8UETjSGOb6Ykvn4jVvBpMjL6b3yIaQy5wPJi52nVaKRFH97EZkXA9Nm9xqC2PAdau2RzkanX4-ge6NM_Hx4i24KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما چند ماهه داریم این کار رو انجام می‌دیم
🔴
جنگ ویتنام ۱۹ سال طول کشید،بین دو جنگ، ما ۱۳ نفر رو از دست دادیم
🔴
این خیلی چیز وحشتناکیه، ولی اگر به تلفات جنگ ویتنام و جنگ‌های دیگه نگاه کنید، اون‌ها صدها هزار نفر از دست دادن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123117" target="_blank">📅 20:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری / ترامپ: ما در مورد کاهش تحریم‌ها علیه ایران صحبت نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123116" target="_blank">📅 20:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: اگر ایران آنچه را که می‌خواهیم به ما ندهد، وزیر دفاع کار را تمام خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123115" target="_blank">📅 20:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123114">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ: با این‌که روسیه یا چین اورانیوم ایرانی را بگیرند راحت نخواهم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123114" target="_blank">📅 20:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123113">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: تا زمانی که ایرانی‌ها رفتارشان را اصلاح نکنند، هیچ پولی را به آنها برنمی‌گردانیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123113" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123112">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ درباره منفجر کردن عمان صحبت می‌کند : تنگه‌ها برای همه باز خواهند بود و تحت کنترل هیچ‌کس نخواهند بود. ما مراقب آن‌ها خواهیم بود.
🔴
عمان مثل همه رفتار خواهد کرد، وگرنه مجبوریم آن‌ها را منفجر کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123112" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123111">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3da0b6f4.mp4?token=LU7l5LW1-yVXsoElmOe8lEpnWjtPCoTP3dYdf63_1AK1iK9kFB6jp_wxWmyAbqv2qnjUEc7D5cMpOaqb6dAFt3HhC3dHMu0VB28L-IVbPIGix_iNx0SbLyXHB2zq2SSk_ntADpJfP8zFULtFYftQ2fej8MyNxqf8ELFTgv7W8yaAof0bOo5xSjCMbVB7sx8ezBXaWks85QYrSPA4wGxRuXi5XKGZfE-svT5Ijhoy37LFszh_BbrcghjoC0m-V5WViTi6FhTN0WTOK9gbWL_JzKa3hnLd4n0DJJBM3pC7QqNNALblBQ2_ye03eUgTSLglci8h7HT6BTJWMtYM8VCB4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3da0b6f4.mp4?token=LU7l5LW1-yVXsoElmOe8lEpnWjtPCoTP3dYdf63_1AK1iK9kFB6jp_wxWmyAbqv2qnjUEc7D5cMpOaqb6dAFt3HhC3dHMu0VB28L-IVbPIGix_iNx0SbLyXHB2zq2SSk_ntADpJfP8zFULtFYftQ2fej8MyNxqf8ELFTgv7W8yaAof0bOo5xSjCMbVB7sx8ezBXaWks85QYrSPA4wGxRuXi5XKGZfE-svT5Ijhoy37LFszh_BbrcghjoC0m-V5WViTi6FhTN0WTOK9gbWL_JzKa3hnLd4n0DJJBM3pC7QqNNALblBQ2_ye03eUgTSLglci8h7HT6BTJWMtYM8VCB4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : تنگه هرمز برای همه باز خواهد بود. این آبراه بین‌المللیه و هیچ‌کس نباید کنترلش کنه
🔴
ما نظارت می‌کنیم، اما هیچ کشوری حق کنترل کاملش رو نداره، این هم بخشی از مذاکرات ماست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123111" target="_blank">📅 20:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123110">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا:
ما توانایی موشکی، دریایی و نظامی ایران را نابود کردیم.
🔴
ایران ۴۷ سال علیه ما جنگ به راه انداخت.
🔴
یکی از افتخارات ترامپ ترور قاسم سلیمانی است.
🔴
اگر در میز مذاکره به نتیجه نرسیم بر می‌گردیم و کار را تمام خواهیم کرد.
هم اکنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123110" target="_blank">📅 20:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123109">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی  همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN  @NetAazaadVPN</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/alonews/123109" target="_blank">📅 20:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123108">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P-kRq6_zMxNqExmNvKVoMERtQWFmwIHzu3QPLsB4Mmsunt5euVqhxbfifi1jfDkzqJtoJlcFmNOGOTjqyxq_6tFPEZXB9FlvQr3rTN8ris2h5PXcfEMNwyArO16HwpzlJq_5fyed3UDHYhKok_QWi3YEzTMfsdbIFA3vroYyssfCV65V94hpR-F2Rcu4_8esg4mBE3Xm_bNC8t8E5eVrz096CFunrKlXoSKY-tNS_E4j963P4BgrV1DzjfJ4jJlyMaPQA8emG9-fGFZXrUh_vUNJyOlUuTTw97w7qVUpUlS61QX9hGegfQgYfmDCQMFQ7MucXMPiOjz5sDy8AnMCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی
همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN
@NetAazaadVPN</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/alonews/123108" target="_blank">📅 20:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123107">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) کل منطقه جنوب رودخانه زهرانی در لبنان را به عنوان «منطقه جنگی» اعلام کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/123107" target="_blank">📅 20:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123106">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وزیر جنگ ایالات متحده: ترامپ شرایطی را ایجاد کرد که مردم آمریکا و جهان را از تهدید دستیابی ایران به سلاح هسته‌ای محافظت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123106" target="_blank">📅 20:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123105">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b162738c9.mp4?token=CFdn25VsASM2vDjprLMeYjzDI3rwKhdB_cy2v7JqbJOZNr6C5EBnQGaxhIuAtcyzQvTxhYS0Lir5eTijGq7RRewkfkWbGVsy-tijGTXPJIYyO6NHneFj_JyimxbtxVeSIY1IdN5JVswBYpV2wmIkDe-W7UazlDoo9sjJVjfBaw5ziZ3Rpsi5zTlRHAlmF8drNzee7_zjiiLw3RVfHt1fatAHiOLkAFCXp2MpupymeH7EDxsXZzV03W7OYmHiSsc8RAqOjcC6k1AYgBS0mZq6qDNKJ3xOhGZhiy-6wcML89TWTq7b5rR1CCU6B6ZDYNhgwgTCjLYX1gCJOpi9sh5TEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b162738c9.mp4?token=CFdn25VsASM2vDjprLMeYjzDI3rwKhdB_cy2v7JqbJOZNr6C5EBnQGaxhIuAtcyzQvTxhYS0Lir5eTijGq7RRewkfkWbGVsy-tijGTXPJIYyO6NHneFj_JyimxbtxVeSIY1IdN5JVswBYpV2wmIkDe-W7UazlDoo9sjJVjfBaw5ziZ3Rpsi5zTlRHAlmF8drNzee7_zjiiLw3RVfHt1fatAHiOLkAFCXp2MpupymeH7EDxsXZzV03W7OYmHiSsc8RAqOjcC6k1AYgBS0mZq6qDNKJ3xOhGZhiy-6wcML89TWTq7b5rR1CCU6B6ZDYNhgwgTCjLYX1gCJOpi9sh5TEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : الان داریم به فواره مربوط به جنگ جهانی دوم نگاه می‌کنیم، چون اون هم واقعاً تو وضعیت خوبی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123105" target="_blank">📅 20:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123104">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سی‌ان‌ان ایالات متحده و ایران در حال نزدیک شدن به یک توافق آتش‌بس هستند.
🔴
هر دو طرف در حال کار بر روی یک «حفظه تفاهم» هستند که نقشه راهی برای حل تمام مسائل باقی‌مانده تعیین می‌کند — روبیو آن را یک «کار در حال پیشرفت» نامید.
🔴
نقاط کلیدی اختلاف: بازگشایی تنگه هرمز، برنامه هسته‌ای ایران و ۲۴ میلیارد دلار دارایی‌های منجمد شده ایران — با اختلافات عمده بر سر زمان‌بندی تسکین تحریم‌ها.
🔴
ایالات متحده یک توقف ۲۰ ساله هسته‌ای را پیشنهاد داد؛ ایران با ۵ سال پاسخ داد — که واشنگتن آن را رد کرد. ایران همچنین در برابر درخواست‌های ایالات متحده برای ارسال اورانیوم غنی‌سازی شده خود به خارج مقاومت می‌کند.
🔴
پاکستان و قطر به عنوان میانجی‌گران کلیدی ظاهر شده‌اند و پیشنهادات و پیشنهادات متقابل را بین دو طرف منتقل می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123104" target="_blank">📅 20:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123103">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
دولت پاکستان: شهباز شریف در گفتگو با پزشکیان تأکید کرد که امیدوار است به‌زودی به یک توافق صلح دست یابد.
🔴
شهباز شریف به پزشکیان تأکید کرد که عاصم منیر تلاش‌های جدی و مستمری برای برقراری صلح انجام می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123103" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123102">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31be1e9e76.mp4?token=lMjOyTcf9fwDhF50ntIQBrjhx8WKPT_E9S_Vv7_5aR_WQWRh-jV4_cqWvqQLiH03cuTXh1pJk0JGGbFlID0Mc3ENxfg5LveadRaWv8trBdlECvz5jgGfjF88jg_vwD5WJK8gUsjxHbse2aVPJ_ApGPe281ci-eMIQBLneVoMOVt4cOmQVDEiHnp-mESLSaChSqhDj9YxyIT910Hg5tLuPRKYJw8emTQw1yfaJKaAol4_Gi451LcCjprUsPhUUN1S8vJ4O2s9SRmk2-Ccn4-7xv-RWdEJYqRtr0DDfz4uQxmCJ96VCkkoc7DiAassXnYHY_gMY-m0ms5UWZ2eYwEBRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31be1e9e76.mp4?token=lMjOyTcf9fwDhF50ntIQBrjhx8WKPT_E9S_Vv7_5aR_WQWRh-jV4_cqWvqQLiH03cuTXh1pJk0JGGbFlID0Mc3ENxfg5LveadRaWv8trBdlECvz5jgGfjF88jg_vwD5WJK8gUsjxHbse2aVPJ_ApGPe281ci-eMIQBLneVoMOVt4cOmQVDEiHnp-mESLSaChSqhDj9YxyIT910Hg5tLuPRKYJw8emTQw1yfaJKaAol4_Gi451LcCjprUsPhUUN1S8vJ4O2s9SRmk2-Ccn4-7xv-RWdEJYqRtr0DDfz4uQxmCJ96VCkkoc7DiAassXnYHY_gMY-m0ms5UWZ2eYwEBRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو : کوبا وضعیت خیلی بدی داره چون توسط یه عده کمونیست ناتوان اداره می‌شه،
🔴
و کمونیسم کلاً بده، کمونیسم ناتوان دیگه بدترین حالتشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123102" target="_blank">📅 20:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123101">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/086c5a05eb.mp4?token=L9JUW9Sa1CqwhAUnhSzRXlDUd89b14TDppd10dweTnxtisAKhb8EmQ74V7Ge7X4LFCOmYIcn6Cp_JAveJSFq8bARYub0LDIDsMNenFTDdytTe_O4ruZcCoJb3cQnEti_lEiOjuWDvoyp3iw8HRgXW_sZHK5W2VJpdRJJlrD11L5-lGM9zzm-n8mZVgCV810evisEZ4M6ru7KzUzMsCnhZYdxVfK2GpQq1liPplIrmZlIS-SwHKXpWG9NPNx7ySxt_HkKQV-arpTvib6B6ne3guNr6FEs0kCOxkiu1sxwdymGDd_TWkMcxzQFDkEdmF6LYFMETPq1mY2Qq6oVgorG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/086c5a05eb.mp4?token=L9JUW9Sa1CqwhAUnhSzRXlDUd89b14TDppd10dweTnxtisAKhb8EmQ74V7Ge7X4LFCOmYIcn6Cp_JAveJSFq8bARYub0LDIDsMNenFTDdytTe_O4ruZcCoJb3cQnEti_lEiOjuWDvoyp3iw8HRgXW_sZHK5W2VJpdRJJlrD11L5-lGM9zzm-n8mZVgCV810evisEZ4M6ru7KzUzMsCnhZYdxVfK2GpQq1liPplIrmZlIS-SwHKXpWG9NPNx7ySxt_HkKQV-arpTvib6B6ne3guNr6FEs0kCOxkiu1sxwdymGDd_TWkMcxzQFDkEdmF6LYFMETPq1mY2Qq6oVgorG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :  ما به نفت احتیاج نداریم، به تنگه هم احتیاجی نداریم، به هیچ‌چیزشون احتیاج نداریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123101" target="_blank">📅 20:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123100">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
روبیو: دیپلماسی اولین گزینه ماست، اما گزینه‌های دیگری هم در مورد ایران وجود دارد
🔴
من معتقدم پیشرفت‌هایی در جهت دستیابی به توافق با ایران حاصل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123100" target="_blank">📅 19:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123099">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و من به خاطر جهان جلوی آن را می‌گیرم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/123099" target="_blank">📅 19:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123098">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/082192b8a1.mp4?token=q3Bz0glEb6g3dLlSheZbPvScz4AjXqm2JOHeBrggadsBxRtavTX_r6T45nYG6Twyl9207L1fAjvMpM_QDA66ajZMQvTiKFY-jTR5d8neQJXYOwLU8wJoU-d0DLhNnCs2pLfKQj1QdQ_4tbMJVYizgI7qzfTqm6p-gzqKZsEhB7Cs98e1uPqDz25rps1dcGUFd9fdP4yFsrHEY9xn3BCr-bQSw-w2SudH7lLr5QNycnw6Hb1jR1-b0RvcPa909EEMUvwED2saFUfxcbSfb_DFJRq7Ymsg0QtOmRLm1w38SA7rVRw5H9QBNPuwjCrvbxSoq8RaNgah4HZrgI_YxiAQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/082192b8a1.mp4?token=q3Bz0glEb6g3dLlSheZbPvScz4AjXqm2JOHeBrggadsBxRtavTX_r6T45nYG6Twyl9207L1fAjvMpM_QDA66ajZMQvTiKFY-jTR5d8neQJXYOwLU8wJoU-d0DLhNnCs2pLfKQj1QdQ_4tbMJVYizgI7qzfTqm6p-gzqKZsEhB7Cs98e1uPqDz25rps1dcGUFd9fdP4yFsrHEY9xn3BCr-bQSw-w2SudH7lLr5QNycnw6Hb1jR1-b0RvcPa909EEMUvwED2saFUfxcbSfb_DFJRq7Ymsg0QtOmRLm1w38SA7rVRw5H9QBNPuwjCrvbxSoq8RaNgah4HZrgI_YxiAQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : وزیر جنگ، پیت هگست، انگار از دل فیلم‌ها دراومده! عاشق
جنگه
! ولی آدم خوبیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123098" target="_blank">📅 19:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123097">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ : با وجود درگیری با ونزوئلا، کشوری که دیگه نیروی دریایی نداره
🔴
نیروی هوایی نداره، و خیلی از آدم‌هایی که کشور رو به جاهای بد کشونده بودن کنار رفتن و دیگه خبری از رهبری قبلی نیست...
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123097" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123096">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45c44fd22f.mp4?token=qH6PfRu9SLi0UduGn0ZaJu-KI9kKADKtgVigZ0T7fqKOel9JCx9QYPGdwrCqBW78PODoJY7PJ7N1Tnq1k4gn8SZ9u8oLN91YxZVCt1oR_M3iRZQR2ZWoiyHOefZpE3lDfvH2T0hSYllgiCQ7IL6LqpgRfSOq3As9ZgcN0fa2F0s6JEUzFbxGrXwSJuq5iolwv6kRvF-A8yIFY-6cJ86E4lLonWtaWa4eV60zDqa4p6ZRmvJnOC_QNVsDc3eJV2lI6ayrAJmmU4tciRX4vxvpxYxnh9Jq7yOMswP_aiBXFzIFSz_imp7B8D34ULFEMlo7BghhctmDk2UG0oQ54mdBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45c44fd22f.mp4?token=qH6PfRu9SLi0UduGn0ZaJu-KI9kKADKtgVigZ0T7fqKOel9JCx9QYPGdwrCqBW78PODoJY7PJ7N1Tnq1k4gn8SZ9u8oLN91YxZVCt1oR_M3iRZQR2ZWoiyHOefZpE3lDfvH2T0hSYllgiCQ7IL6LqpgRfSOq3As9ZgcN0fa2F0s6JEUzFbxGrXwSJuq5iolwv6kRvF-A8yIFY-6cJ86E4lLonWtaWa4eV60zDqa4p6ZRmvJnOC_QNVsDc3eJV2lI6ayrAJmmU4tciRX4vxvpxYxnh9Jq7yOMswP_aiBXFzIFSz_imp7B8D34ULFEMlo7BghhctmDk2UG0oQ54mdBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : سومالیایی‌ها، همه‌شون کلاهبردارن، خیلی هم خرابن، ماگرفتیمشون و داریم روشون فشار می‌ذاریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123096" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123095">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: ما هنوز در مورد ایران به توافق نرسیده‌ایم و از این موضوع راضی نیستیم.
🔴
ایران فکر می‌کرد می‌تواند صبر کند تا من را خسته کند
🔴
به انتخابات میان دوره اهمیتی نمیدهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123095" target="_blank">📅 19:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123094">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dbdd434b1.mp4?token=c1_MhzABZadDXpp8wq4UoL_MGJFqXUFf2qYsyrjf1yMa8IvBuye-XlbGNF3mxlCAOiY05uBPiWRoh5WtCd9dK394d8V6frBrxOyGaKeaPZOHovI4RAvCUHY2HLoVGxWQavoqfy_dA0b2x0sSPki_vTI_shT50GdDiPfBKCgTvcHmniCZrZjTWEdNX8Yq0a-LfnNkju6e8q94c3qoLCYwMZut5CBQhT9oTaUMTaUxsepXR56--tCWZvb0cvK-YdDJyEGKVNULyev6qnipfTEVbxpmKimL8xihqnZfPHCbJNinCInJDGNvrkExC6svEljykF_MIJei7xK2iQsdCh7pDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dbdd434b1.mp4?token=c1_MhzABZadDXpp8wq4UoL_MGJFqXUFf2qYsyrjf1yMa8IvBuye-XlbGNF3mxlCAOiY05uBPiWRoh5WtCd9dK394d8V6frBrxOyGaKeaPZOHovI4RAvCUHY2HLoVGxWQavoqfy_dA0b2x0sSPki_vTI_shT50GdDiPfBKCgTvcHmniCZrZjTWEdNX8Yq0a-LfnNkju6e8q94c3qoLCYwMZut5CBQhT9oTaUMTaUxsepXR56--tCWZvb0cvK-YdDJyEGKVNULyev6qnipfTEVbxpmKimL8xihqnZfPHCbJNinCInJDGNvrkExC6svEljykF_MIJei7xK2iQsdCh7pDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : الان داریم با رویکرد «اول آمریکا» جلو می‌ریم درباره ایران. یا باید با شرایط من کنار بیان، یا کار رو تموم می‌کنیم.
🔴
می‌گن «صبر می‌کنیم تا انتخابات میان‌دوره‌ای». دیشب دیدید چی شد؟ اون فقط شروع ماجرا بود برای انتخابات!
🔴
هر کسی گفته من دارم کوتاه میام، اشتباه کرده
🔴
الان به نظر میاد خودشون دنبال توافقن. فکر نمی‌کنم حق انتخاب زیادی داشته باشن
🔴
اینترنتشون تازه دوباره وصل شده، اقتصادشون هم داغونه، تورم هم خیلی بالاست!
🔴
شاید مجبور بشیم برگردیم و کار رو یک‌سره کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/123094" target="_blank">📅 19:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123093">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: ایران می‌خواهد توافقی منعقد کند و ما با آن توافق می‌کنیم یا به ماموریت پایان می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/123093" target="_blank">📅 19:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123092">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc219101d.mp4?token=l2igRpb7eGUDbdGXzI99Cq_m3Ioxfg29dfutczQQeq7S4NmhMzFTfrgpeKdZ7lSqDIahddPRnzd5CCU38kD8JRO02NIa_oVbqYSdwRV3jqCXLCv_u16qJwh5SsILGYZ919xFe1Nh-XlZdaKjrrEylAgZPSxTjU7EGU2c-KFd5JgpWEuNNOwXjMz432ttNpdbLB-FZoIa27WOh_zAQhuEVX_8ZqWREM5gyz3TQsx9oZOWH1m1335c1gbtDX0pD82TQYhlVvSoyVIl4hJqHFq3ykACIJyvE2DJK-TtR5kXt45TRWJ4O7LGgnvg83wTIaNjPW39S-yUuQYZREqNQWa9QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc219101d.mp4?token=l2igRpb7eGUDbdGXzI99Cq_m3Ioxfg29dfutczQQeq7S4NmhMzFTfrgpeKdZ7lSqDIahddPRnzd5CCU38kD8JRO02NIa_oVbqYSdwRV3jqCXLCv_u16qJwh5SsILGYZ919xFe1Nh-XlZdaKjrrEylAgZPSxTjU7EGU2c-KFd5JgpWEuNNOwXjMz432ttNpdbLB-FZoIa27WOh_zAQhuEVX_8ZqWREM5gyz3TQsx9oZOWH1m1335c1gbtDX0pD82TQYhlVvSoyVIl4hJqHFq3ykACIJyvE2DJK-TtR5kXt45TRWJ4O7LGgnvg83wTIaNjPW39S-yUuQYZREqNQWa9QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : با وجود درگیری با ونزوئلا، کشوری که دیگه نیروی دریایی نداره
🔴
نیروی هوایی نداره، و خیلی از آدم‌هایی که کشور رو به جاهای بد کشونده بودن کنار رفتن و دیگه خبری از رهبری قبلی نیست...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123092" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123091">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
تلگراف: ایران فقط در صورت آزادسازی ۲۴ میلیارد دلار از دارایی‌های مسدودشده‌اش، توافق با آمریکا را امضا می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123091" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123090">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ به PBS : اگه ایران اورانیوم خیلی غنی‌شده رو تحویل بده، در مقابلش هیچ تخفیف یا کاهش تحریم‌ها بهش داده نمی‌شه
🔴
عربستان سعودی باید به توافق‌های ابراهیم بپیونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123090" target="_blank">📅 19:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123089">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNILe_dwGEKzuTdUX_v7X07Es_EdTW_vDh8ZUBCvWFQPmR935w28LvEXUpTxMAnsbtAPeNe5S3XYaiubbK_TcufJpbLZyBbAKdzt1jthwc_zqFNwKSpzkdYMLDe34NgPMHVGy0Fs7wxq-ISaiBSf80tlak6G5F2BIaI5V_7LaIskmoTxx8NR47ZVEMxzUBdN2elcAWYw0cHPV1OXNRprb1NZiPzH4y_QJf5PpHmf8Uu-Pc8vqPSGwKjqc8T1SQF7ycgH4OmpTm_TLlqCErbXZTzvVw7JsdEepnDwxgO5Urdse6tw0YTDfCbVsXp_cImy9EgsH0sR8RLPDbf_jb7pHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در ایتا و روبیکا چه میگذرد؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/123089" target="_blank">📅 19:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123088">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فارس: منابع آگاه می‌گویند احتمال دارد ترامپ طی ساعات آینده به صورت یک‌طرفه اعلام کند توافق ایران و آمریکا نهایی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/123088" target="_blank">📅 19:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123087">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
جلسه کابینه ترامپ قرار بود ۴۰ دقیقه پیش شروع شه، ولی شروع نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/123087" target="_blank">📅 19:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123086">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17eead82df.mp4?token=a9kOM9eL2gRSVdTSpJSd3DZAkPm30pIgsUcPvsRkXumvijR4N-6X_EEWCIDaM2De55HAGV3rzRweQMfhfMP_gG2PLxE380A25WPHlmYNP69-HlR4D6e2EWXzj_9MGfmwsxcts9rban9kC92dJbkgdbT-TU8OwcpsEHaI6dc_tuCZm8Xp046O3itKHqKn8PlYdokDUsrzccO-gPL41LBjMKZ3SPDpxkkgS4g-GkdhVfiXvZ_hih4jT1pPMp47t-mNDcMsLVf27_s4sOxfQz4yQo487cL0X_67TyLXnKg4mF2uwitiDCwkCUlY1M52Tcu3FAW9DE9MsZsm0vgjtygFPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17eead82df.mp4?token=a9kOM9eL2gRSVdTSpJSd3DZAkPm30pIgsUcPvsRkXumvijR4N-6X_EEWCIDaM2De55HAGV3rzRweQMfhfMP_gG2PLxE380A25WPHlmYNP69-HlR4D6e2EWXzj_9MGfmwsxcts9rban9kC92dJbkgdbT-TU8OwcpsEHaI6dc_tuCZm8Xp046O3itKHqKn8PlYdokDUsrzccO-gPL41LBjMKZ3SPDpxkkgS4g-GkdhVfiXvZ_hih4jT1pPMp47t-mNDcMsLVf27_s4sOxfQz4yQo487cL0X_67TyLXnKg4mF2uwitiDCwkCUlY1M52Tcu3FAW9DE9MsZsm0vgjtygFPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به ساکنان‌های صور تو لبنان زنگ میزنن و میگن اونجارو تخلیه کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/123086" target="_blank">📅 19:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123085">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7909417a98.mp4?token=hzJ6Xuh9v-N-qb6CMEU9yfZl5iVlkH_dps86QWZaA09lb6uXnJNwyW9Hjc1kZyddfwdpAeUSOdTPLouUoI53DUU4hu80-EhZoLhcFlY-6F0kKK5eF1GAQ-dxJ4gIVcmExOcWL-NLo_QOl-CjuITkiaVJyICy4dTlrpi_uQWJYLtY-pd9w6Kg9gvEBaBJTzWlERDpWTNEX4KPjC3eRrWN5UQ2MJcpPm4y16d7hYygoknb_XZdQz_D4ubIJlc0uA1q8gTVNYWJrVvTDTkOsBSSw7sJW7SnALgMfeXsS4R1LKUUKUdNmDcKE7wC988Tv1f5iSrHOY_8Ad_hEqO8J_6Jjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7909417a98.mp4?token=hzJ6Xuh9v-N-qb6CMEU9yfZl5iVlkH_dps86QWZaA09lb6uXnJNwyW9Hjc1kZyddfwdpAeUSOdTPLouUoI53DUU4hu80-EhZoLhcFlY-6F0kKK5eF1GAQ-dxJ4gIVcmExOcWL-NLo_QOl-CjuITkiaVJyICy4dTlrpi_uQWJYLtY-pd9w6Kg9gvEBaBJTzWlERDpWTNEX4KPjC3eRrWN5UQ2MJcpPm4y16d7hYygoknb_XZdQz_D4ubIJlc0uA1q8gTVNYWJrVvTDTkOsBSSw7sJW7SnALgMfeXsS4R1LKUUKUdNmDcKE7wC988Tv1f5iSrHOY_8Ad_hEqO8J_6Jjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش زدن ماکت جواد ظریف در میدان اتحاد گرگان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/123085" target="_blank">📅 19:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123084">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyZaIbY2IgPpfDtHLFKOZOLAEhDgRJQMsHrsGM-4NrRVYm8Osj22jwsJwAVOCT0EGHwqjGiqQhcEf-SPRLSwLWDmzITK7RzNOWA2ZJvrzwBttYlW4j1L_Xg67dqIw926s1VYYCxdosE8uzxEUBvV6UiwsfVrNR-7FKku9mNZN76BruIS6Yn8bzLgevu9Z_kzAzmyhpPNz-JmIkRT-c9U5HUTi0KxJlUpjrQ1XaQ9FyA5AaL6U6CxtY8AMtpjcIO-g2DBV-_oHtMNFGSgbM0yBe5Ne_ZRYuhgFAX4B0m_FQvyuuGqibckGKDQZrjbW-zgOykduHkr2I1IBK8mk8AVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابوالفضل ابوترابی، نماینده مجلس: مردم عزیز(اون ۴درصد) اخباری که در خصوص مذاکرات به گوش ما می‌رسد، خسرانی است که از برجام هم بدتر است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/123084" target="_blank">📅 19:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123083">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/78f3edcfce.mp4?token=GKSbnAsl6l0sKdDOk0FmzHci3pl0L8ah8TLQOU4NW0jc6zx9h6Ir3f7gdyixPaEQY4OMncsZmUBkitqjfINpKPZgXXrOnIp6efnDTUZDInHT0xT0L0ij-fR00bwSGzB57zcl6pHEDw30RlmvMTr5to0Y9AYFBdgkiZQbQyzGolqUpCvkUbOai8oPjVIZiHYheVaTv65dF4mPy_T-Fb-8x8jQaUpECglc31sXYPgzGuKfPSG4RhJ7V5yz9_vJcp6jzhK9JG3lCLYPIsFYCp5fCgyQsT1sGnnO6vlL_VTpXsX2n1EOsjTjCkv2DyDx-Y5qFt7LJCprNhPxyI6YNYqFq5HJBxkP1X7Cxs02T7Obkby1K8AwdxduI5fuh41ajSDQwYDUwf7GnS-rRggWvWNpTW1Ed1IGU0iy_9sfro-187ETIdAZuERjA5Fbs6wgsMH3l3Re-mucOn-WgLSlokyjBs8i3SXtAAhGptJZrp4bpsBlF0EEm8spgkyy3c8nZhJUetRXs4Kak1263lXzpqO-bY8rTENyyQM8qHfjlmGnmio11sVxUnjmFJ1cmVNcwp7WxvahUHoaTRdT9LHhi4lsNUEikHln7dpZg1rAlao6lEdisRnCO61RuVSgR41JI8TxC_PJ-7wggIyVpgjASt4m51HiKN6wQvci1R6PGAUJ3hA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/78f3edcfce.mp4?token=GKSbnAsl6l0sKdDOk0FmzHci3pl0L8ah8TLQOU4NW0jc6zx9h6Ir3f7gdyixPaEQY4OMncsZmUBkitqjfINpKPZgXXrOnIp6efnDTUZDInHT0xT0L0ij-fR00bwSGzB57zcl6pHEDw30RlmvMTr5to0Y9AYFBdgkiZQbQyzGolqUpCvkUbOai8oPjVIZiHYheVaTv65dF4mPy_T-Fb-8x8jQaUpECglc31sXYPgzGuKfPSG4RhJ7V5yz9_vJcp6jzhK9JG3lCLYPIsFYCp5fCgyQsT1sGnnO6vlL_VTpXsX2n1EOsjTjCkv2DyDx-Y5qFt7LJCprNhPxyI6YNYqFq5HJBxkP1X7Cxs02T7Obkby1K8AwdxduI5fuh41ajSDQwYDUwf7GnS-rRggWvWNpTW1Ed1IGU0iy_9sfro-187ETIdAZuERjA5Fbs6wgsMH3l3Re-mucOn-WgLSlokyjBs8i3SXtAAhGptJZrp4bpsBlF0EEm8spgkyy3c8nZhJUetRXs4Kak1263lXzpqO-bY8rTENyyQM8qHfjlmGnmio11sVxUnjmFJ1cmVNcwp7WxvahUHoaTRdT9LHhi4lsNUEikHln7dpZg1rAlao6lEdisRnCO61RuVSgR41JI8TxC_PJ-7wggIyVpgjASt4m51HiKN6wQvci1R6PGAUJ3hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تعجب یک گردشگر خارجی از تعداد پولی که در ازای دو دلار بهش دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/123083" target="_blank">📅 19:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123082">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28ebfd303.mp4?token=sCf4GpThEwI1MQiVMX0sZPKbWb2AQHd9qX9cqHCf2MbUd10-jm4cdIh__Z45PksZW8dTXLEwaZFlMiiMXa_dC8JHPgrBt9oXtkQrPXXgh4EzB9ePhYyI88p_ZPxax33fiStoFaY7caX0bFp2Y9ttVLWWDzdD0McFIs_QGU-BnN5D3dM7Zx10dyyriJwYlTdatL_5phHwtB31hb1fe20yrKk4quevZJDKOhFQVhCtZXss1YfWl_FCb57rL76bai3ptwCt-9uS8JIecpaM_0Qj4vGSe2lUH5iTqcSx8JCwVb13ShjNZ6xJQuzXWhzeTNsLN2iEYbWiz3wztF-HRFEBCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28ebfd303.mp4?token=sCf4GpThEwI1MQiVMX0sZPKbWb2AQHd9qX9cqHCf2MbUd10-jm4cdIh__Z45PksZW8dTXLEwaZFlMiiMXa_dC8JHPgrBt9oXtkQrPXXgh4EzB9ePhYyI88p_ZPxax33fiStoFaY7caX0bFp2Y9ttVLWWDzdD0McFIs_QGU-BnN5D3dM7Zx10dyyriJwYlTdatL_5phHwtB31hb1fe20yrKk4quevZJDKOhFQVhCtZXss1YfWl_FCb57rL76bai3ptwCt-9uS8JIecpaM_0Qj4vGSe2lUH5iTqcSx8JCwVb13ShjNZ6xJQuzXWhzeTNsLN2iEYbWiz3wztF-HRFEBCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل اولین هواپیمای سوخت‌رسان هوایی بوئینگ KC-46 پگاسوس «جیدئون» را از ایالات متحده دریافت کرده است.
این هواپیما امروز زودتر در پایگاه هوایی نوواتیم، یکی از بزرگ‌ترین پایگاه‌های اسرائیل، به زمین نشست و رئیس ستاد کل ارتش اسرائیل، ایال زامیر، نیز حضور داشت.
KC-46 می‌تواند سوخت بیشتری حمل کند و تعداد بیشتری از هواپیماها را نسبت به ناوگان سوخت‌رسان قدیمی‌تر اسرائیل سوخت‌رسانی کند.
قرار است اسرائیل حداقل شش فروند هواپیمای KC-46 دریافت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/123082" target="_blank">📅 18:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123081">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رسایی،از رهبران بولشویک‌ها: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/123081" target="_blank">📅 18:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123080">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuEsdl6c-lHwY3-zlKSgLisQiQyGJC9FT6erHx9UHR41-6NAQAfyVpJLUM69oGHn2hHDixhuCDGV_icSFRdLMAfykr0FuzJqO91xHxwD2FRVArCMU5B5W-pR4O1t-KgnlBNmqPFsurkExejXs832y0yi6pdn-RFU0GF5h3wIgLGaZaxAx6bq7brM7LzbKO7RN5agcXZB9A-kGuoRnRgTP_mYmEKxBbei5jNQjGojZUnfGEVQEPOnQMEJ49CK_kMqVo3A8UOk_fXBPQNiXSK81x-ODnVeFQTWI2aovgq29neFHGNlOLBEhzWL54eYWYUfdxBvDaV-iQzLY4BEBCm0iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی،از رهبران بولشویک‌ها: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/123080" target="_blank">📅 18:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123079">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHsOZc9UKawuD-6yAhSSo8mXSOwTQtdYh4BOuyaViCmJoW6gOm22x3ST062fGmfoZbRLAZNM-_w27YZS6PyrjsXRn0oN2_MXC9h28clhzS8vwkTuVVNCH6VHEnXmMWhLJWAGgwKMP_HCEQMOUuRs3eNbzW6O1CG9xHBmU-C9ynndAlzujFmf8su23L88ekSAahzcmkSW42MjKXJWpem7YYao2TFU6LBMp6myJlplzJInCC3DtPcQjGKPrW0WLc1-qQMsdYCM8F0TD6tnF1LBFcUl1vKx8x8IcbvwqS4SHYlwHv-1ManAouefAYLglBlMCls3GSs0qjleBjVJXRyUhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل :
ترامپ اجازه حمله به بیروت رو داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/123079" target="_blank">📅 18:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123077">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5l7c74Qwx4MJ7bvugOMVkVRYyzCkHUByd-CF5KyUOoSchEO4VdjeKziKZF4TLst5XV1QteeniMlwmuQBVDniprJJJJKgPW99sgGH47rcJ02aWgb2quLzsrEta6S84NsdsjrteWURe8dBi9IkNGxvV9wVmZrC0MtntxQWVk-dlRnN2KJMRYChZVYC_iB9SSxmUaU-7s6FkiiXnSfJ14Z6ZKmMqBCfdStHXEtgwQgLA4_-RsfHqMoN1S9cPOvb5cIvMkArodDXKfofkHGDrjpV9NeEhARL3_bbNL0H82sz5EeOFY9PgV6owg8EWSF0XfXWWDZFxtZvS6Tc0kRCrRYHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGmTaV112uO5Yw7NPscF-40zLjd-zmy54r_RAwkc1vtDbBhyO0TSjfEJviJLAu9Q1CwFhfZaysaRgmfVdkohZ3gxSom7wmIMnIWD7KTOvC2PsBBgcZOWBaIeM4HFkq6V7_nJ2OzdrVMl_a4Xj5Vou1bOfGNe0YpfxahwIDcJl1G4ZSUOHPLJ14NhMZWv5e8396mM4ea4m2qxabEkCmdoAkuwmT08Ga0qyHyvvf99qzZVbFQZDMuo8GCsNRd1-Y92nAjLjBKq9uKecRV6Yh3SrsWjwDjIOCY7z-MjQu7x_6pgbkpDbKJxkPTUC65cCZaNj65bYadgrVEZztQZhHJkNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات اسرائیل به حزب الله ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/123077" target="_blank">📅 18:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123076">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
صداوسیما: سند غیر رسمی اولیه از چارچوب‌بندی یادداشت تفاهم ایران و آمریکا منتشر شد
🔴
آمریکا متعهد به رفع محاصره دریایی ایران شده است.
🔴
در مقابل، ایران متعهد شده است تعداد کشتی‌های عبوری تجاری را طی یک ماه به سطح پیش از تنش‌ها بازگرداند که شناورهای نظامی مشمول…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123076" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123075">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
کاخ سفید: ترامپ گفته است «
مذاکرات به خوبی پیش می‌رود
» و خطوط قرمز خود را به وضوح مشخص کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/123075" target="_blank">📅 18:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123074">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbKRgFQ94ZN0mVKqLax4L0gx_EFo5FzEIcQnxBZXVNafl9Iz4UDvbW_m_k6RfIGjX9jVdWV-MQ8FkLkJHtOZeSwPMxct-miukzSKGvaHb58MP4UAC21speEKHxrKFh5a9QsBkRkiOy8lOOcF21pdHJw-KlF-vDrD7y3hEXAQF9zj3YLw-FXj4-nsHCUPWlIy8Kdwss1i2xPCAPpXkMUVw5y1b7nGgRf_JOK6R9DeiKzYs6p7bW_-i5i3SenCz-YYhDTef2Bhp4P_sg3ADjbYqI4Vo3nEdcIPVYtlelzHGZFbajMh6Ni-ZAizYqe4Z6mVWJF8F-_rL9g-bvwwO8eGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ برای بار هزارم این عکس رو توئیت کرد و نوشت نیروی دریایی ایران‌نابود شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123074" target="_blank">📅 17:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123073">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
صداوسیما:
سند غیر رسمی اولیه از چارچوب‌بندی یادداشت تفاهم ایران و آمریکا منتشر شد
🔴
آمریکا متعهد به رفع محاصره دریایی ایران شده است.
🔴
در مقابل،
ایران متعهد شده است تعداد کشتی‌های عبوری تجاری را طی یک ماه به سطح پیش از تنش‌ها بازگرداند
که شناورهای نظامی مشمول این توافق نیستند.
🔴
مدیریت و مسیر عبور و مرور کشتی‌ها با ایران و همکاری عمان انجام خواهد شد.
🔴
آمریکا تعهد داده نیروهای نظامی این کشور از محیط پیرامونی ایران خارج شوند؛
این‌که نیروهای اعزامی به منطقه را شامل می شود یا نیروهای مقیم در پایگاه‌ها نیاز به مذاکره دارد.
🔴
در صورت دستیابی به توافق نهایی در بازه زمانی ۶۰ روزه، این توافق در قالب یک قطعنامه الزام‌آور شورای امنیت سازمان ملل تایید خواهد شد.
🔴
چارچوب تفاهم اسلام آباد هنوز نهایی نیست؛ هیچ قدمی از سوی ایران بدون  «راستی‌آزمایی ملموس» برداشته نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123073" target="_blank">📅 17:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123072">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کاخ سفید به الجزیره گفت: رئیس جمهور ترامپ تنها توافقی را امضا خواهد کرد که به طور قطعی تضمین کند ایران هیچ سلاح هسته‌ای نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/123072" target="_blank">📅 17:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123071">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
فارس: آواربرداری، تعمیر و ساخت بخش‌های آسیب‌دیده واحدهای پتروشیمی به پایان رسیده و اکنون تمامی پتروشیمی‌ها می‌توانند با ظرفیت قبل از جنگ تولید داشته باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123071" target="_blank">📅 17:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123070">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f80cb944.mp4?token=v15d-QLDy_wIgkZSCJfPG6YJFnwTlkJXD1LjgaGfOiFiwliaUOjDv0aATowYIdZnbuXNl_y9gYk_ciXo2B-yMv4LcugdPh-AM3TGigoO5XfCSf9aYxr9yOZiTCZjEL7bmuCjc4dxlj03jNBa-xu7lZwP7pnPfMMNpko75S6ucjBms5kLA08fMaT-LpQWVU62luR28B02HDb14foFRtwx_zbusYmifWKRN6LO6flKmeiGDrQ3i4n4v9q1aUoDZWMiAbJPOxS8NiQ-EqphkVGeyOhKl0qUwD0bldSaJVW4ZoBVvtcGvsDrtIeABsLAPcc8yv569VpOHXuHGEQXx1GY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f80cb944.mp4?token=v15d-QLDy_wIgkZSCJfPG6YJFnwTlkJXD1LjgaGfOiFiwliaUOjDv0aATowYIdZnbuXNl_y9gYk_ciXo2B-yMv4LcugdPh-AM3TGigoO5XfCSf9aYxr9yOZiTCZjEL7bmuCjc4dxlj03jNBa-xu7lZwP7pnPfMMNpko75S6ucjBms5kLA08fMaT-LpQWVU62luR28B02HDb14foFRtwx_zbusYmifWKRN6LO6flKmeiGDrQ3i4n4v9q1aUoDZWMiAbJPOxS8NiQ-EqphkVGeyOhKl0qUwD0bldSaJVW4ZoBVvtcGvsDrtIeABsLAPcc8yv569VpOHXuHGEQXx1GY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ثبت لحظه‌ی حمله به لانچرهای موشکی (یا پدافندی) هوافضا در اتوبان بستان‌آباد-تبریز توسط یک راننده‌ی تریلی ترکیه‌ای
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/123070" target="_blank">📅 17:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123069">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff9d4354c.mp4?token=khfiiGaf_qUngX19Nh7WzsH2-rI3WPBkD66rHvpZgHsMUTGmy7lq0lugvPqbzq9EnV-4WPgILWXVNtfeROHFaL0a-B1-c4MmShcDyUza8l69QU8u5_x4vq39Pw2CqnxI-A4sgLJjPpB2cdg2jLOlotxwB6b6PdvrXzFguN0WS8N9hu6PxGiDiMrV0ckWov2rDcLfuVHkSJEUiTNI-JtxcRWpm191sutgIIxI6E1ItyI4eAiC4npeVY95wAc9vby-9Pr738wUd_Mi1ZzNIGUIuIzps_BxKxElW6_H51KZmeYARxcEz-Z6vTGWfySH892YIhdfRjpl7g88QZxak64I8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff9d4354c.mp4?token=khfiiGaf_qUngX19Nh7WzsH2-rI3WPBkD66rHvpZgHsMUTGmy7lq0lugvPqbzq9EnV-4WPgILWXVNtfeROHFaL0a-B1-c4MmShcDyUza8l69QU8u5_x4vq39Pw2CqnxI-A4sgLJjPpB2cdg2jLOlotxwB6b6PdvrXzFguN0WS8N9hu6PxGiDiMrV0ckWov2rDcLfuVHkSJEUiTNI-JtxcRWpm191sutgIIxI6E1ItyI4eAiC4npeVY95wAc9vby-9Pr738wUd_Mi1ZzNIGUIuIzps_BxKxElW6_H51KZmeYARxcEz-Z6vTGWfySH892YIhdfRjpl7g88QZxak64I8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آغاز تخلیه شهر صور پس از هشدار ارتش اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123069" target="_blank">📅 17:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123068">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fQDvIrfX_CVrXXrBcCp9QE7Ka0tCcdf-PjNNYvz8vQqqbEs01BF2s3aGED3j90h3N9onj731bEInl_g2l69ve1q3-Oc_OgjojO5zbQ0ZTStIuj5-lftTVpkfGlzAnk2xpGbwnq33bvRytqMAT4dbrGeqSTmG6ku3GI6tjmHgl49uqihqOWTIe2miIEXYLLiMer_QQwPdrJCVcRS_DZUrEQjF8Jzl9XJb8eJ2bxWh1rUmGaWsOm76rO2JZzLbjwH2mvBcBa9nd3LSDQODedHpZjdo4wQbJFKGVPSHowWUe2-P5RyMveuRUSWr9evgdiOxtPz06fEQTSRvEGvIwMe41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک ایرانی رفته جلوی کلیسای پروتستان که اصلا پاپ کاتولیک رو قبول ندارند که به اون ها بگه پاپ طرف جمهوری اسلامی رو گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123068" target="_blank">📅 17:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123067">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ امروز ساعت ۱۱ به وقت محلی (حوالی ساعت ۱۹ به وقت تهران) برای بررسی مذاکرات با ایران، جلسه‌ای با اعضای کابینه و دستیاران ارشد خود خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123067" target="_blank">📅 17:08 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
