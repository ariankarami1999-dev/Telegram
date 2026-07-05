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
<img src="https://cdn4.telesco.pe/file/WBzt2zUGlmcITvCdpAhzq3bbONodZEvLiZioWT2xcJ_ftTkxDoiMmeSEPr1iLurQyq_kRuoIG37squRxOUfB2BB4zKcVYX5VQWDjO4UixvsN6ZvJAVOia0fDVx6rWCBkifsF3L1kTVKX2GIis7oviniXTDtzy8WolvHF_yyR9m1KENEHmi3EqXyCtDNLnXH-87ZgERrdrdhaVwzYkSQysNYFtF0xDDsedcXh4kYfL-PCMBIZyerMbDcaeprbOpYDVs4X74CGAsDxz3nYQnDHBaxZYo42MJbGZNleXUVhUx8dax7VYNULG22ips6zc7tPVbaCqMjTMafkDZTMfnevyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 385K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 15:39:41</div>
<hr>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUgXgPSSLAdj9Qthp75kLfe406gd8zm8lUD0qFCLDq9NzDbihVbancAqlGceKV1QbjAWCSPLm-pWSCB982AWcj4ZtvJ5fKv2cFbj5JITXQY8hLAJIvT-tCH-sfq_iqYktgUZ_lAWkihGwzGpjwFxCDIxNxVPzpFus089sota3Vn9_tMiLNcEdZ4nMkOcKpHfxMjT9TatH5uIXKS4Sjkr1UasdfSHOAAPnnLlBLl9InmCeyQGEEWDO10K92aky9vn59Se-QsTNqe50BI13BikV1W4rtKCjeatSEnR0a1BlEMvBOvJGvrEb3rnAAS8UIzmb8myT2_R4SFDv52O5vqoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/persiana_Soccer/25001" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfSCZucNivh8XtU3oNP7ZtcgVm4LNBwIzBfgFTSyRIYoiYVoT3orOVTm0YLieSpW7CvcMS2rxEuNszuUFsEXH9B2_s7yoHclhPGtoT9ACLb-2o52qvwmp4oxgRUeH2LlZaVgMquQS-pvDlcjekOwHKnCzGmTHWf3emgONq0wgtBbD1Y8M3FkyeaqNYoZFDKq398ULsPiwUQHpAHX83Iw1PpWcfJp4JBYCiaZ89b1Z_LomInJnJytysvOE9T-wQ5AHFl8IVNBVDxGZhJF9jVgKDac_x1wWBBsbGqOCG-qrPEPgJ2K9Vsah-q4bxNhdGFe0Dt9MLILIYTyEE_ENMzBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/persiana_Soccer/25000" target="_blank">📅 15:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrfBVJFM1OWcumRFVkccCILv3UviL1-KgiXGBzdukLM0uyjkUXiiMk8nf7bwe_vidwCPYku47JqT-OyGkARENbd1lkJvKnduEcTAoLa9aDIUQ4CF_chSCdYkcNxSs4cfy7AfjKgEY971Dgiq7CZ2aae8Y1FalFVjdXBiAzh8zp01GL4BO_tBLiDjPpNT5E7ue1KFhF1NzXaBsgk593UIqe1uAop64yZg_SBuSVKG47FmreampD1VbDlgG995no_n0xuURHMDz7VERKkKuQXCpa2in4A9RMzHlEbKYT1DKbeeggGxLU-X4-gXsIknKLJip-kz5X-j9zGXm7Rmpl_Gfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsssX5qLjuVizx9YsZcjYQEtPMU-axmk7XBofX3ergAeEei0M_Mx2uVPjwUXkyLbevNjq70GyVYqakFsnTFICnvlzDa8GbZVkKMRhf-UPWQeDpQ31ABdE84B61g0swb_5dSQjtsLWx7woYve4xN4kcveNx8a4_F2RsEaVzLShUUhXXP_qso1xOs0tYRsV42aH7u-dbXuKS-imenNtJxTMxd_Nru8XyiqyHYCxUnFeaCQB7xth2ZKcSdv8fE7recNic2NoqEde4OU-gGQboIYeVmyrnuYnVgmV8zQGW2Lqqo0yR7hIy3lSnZm7mOz_EnZcmzs1wENqXFfeyB2tl9TgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم
؛ سال2006 در چنین‌ روزی؛
جواد نکونام پس از جام‌جهانی 2006 به‌تیم اوساسونا پیوست و به نخستین بازیکن ایرانی لالیگا تبدیل شد. او طی هفت فصل حضور درتیم اوساسونا 197 بازی انجام داد و ۳۱ گل هم به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/persiana_Soccer/24998" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkmzarUcy37GRuW-IryboSepL9zD-1MPJHcHl0cP7FYhiRRVey8Y-5VON5_pIZAU3NYETt_2gchJNLT0wpNCvvlG8RvJzFbgohCMaJnLJCEfs8CZTpiZk5Q8lSrH3PftBcZvDWCuALqtY2JacqR3EhpjZrRgOWr5obqNJTssPR2tJUGfHubMU3zKrM_E_IVpyZxbIjJIQNUGR5b4mzouTpbA_YzRFc2usbpKf2mi72rVRcKgUdAIz8fPahgjOQz6lxacRj6mJObrWL_Xifye5a8rkN8KZJPna_UnDjgx8HxEWLZQ_gRuljAoF4bmEYCUIqEbfcl98X52tPLJrkItew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
تایید خبر شب گذشته پرشیانا؛ با اعلام باشگاه‌گلگهر مهدی تارتار از این‌تیم جدا شد و بعنوان سرمربی‌جدید باشگاه پرسپولیس تهران انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/24997" target="_blank">📅 15:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS5k0IlrS_P1Tvrb7a_x8eyoAWKnoMbHBKcnu9CxTUafTOMhhm45LXH_7Fo1AiYE6dtg38lLyVM4M22WGzyc57nVliOQddpEVbqU9jMIv8u-GqL_DOltJFGt8JUMzGWJmXphOsBj1Jn1yioxwgX5kkrOl3Jh9HlGYLV0WkPKzQC4g53i0qCzcf7VRM8WXSBl2qNvMobTCgJAIyIp87LedEd-Hj4V5DsYNN6_loFWIVTkjVabojGk4OoRDLhxNYVb8pJSrOsZ8SVw-tf2LzTZiJyJHYP7lmhU0czwoLGpygIiinMnpkYqXP1QU4PFzGKtcF_gkKs-hliZq-h8OCJyPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/24996" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-ebxrj-W_JazLpoueCxwAony-_RPTIqCCXH2f0kvA2VLMmvK3BNU84ndKJ8XY0RWa36Hozk0jyFXtWNHe8UeJAMo0iyjXL_Ue577Fs61ilHmBlwIHN8xHbt7W-MxfIZrgMYbf47I8v7We_hWVpc5HudI8froNL7gb2c7nZvARdtBFa_Hcc5PwfVeh_FQGWrbkTEyDAkME4-ymANd8Qj9kFiSgiFZ9idIgbhWp_KMJ9l71Vm9zwlFtZbvwOFw1HMdW8BvwX7OeTTiQNYATegIPUhEzAS1IgjI_4WVHfAII9JSh5jJ9FmxYx_RC8Z0lcHR2ophGaaYWefIp1fSE48AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛ از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24995" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzWTa4pK7g26Pk4KEnAX1vv4eb8CtM_MGVOYyf6e5xWc3RRH17Qzxebp1PgV-ZDUDaqAijY5hId4h0nSkYVXh5ygsHOp8BkqmkAiVIYFUe-1GOsJc_sjyC3eAK2c-pUoLvITrkSOM1DKm8B_swWQHi9vn7fXjE1Xin83kWb1IbuTQ2ESuof4ifKgnPDnc4tjhEdKOhhQBfLkbqAH0P1t-5zcP0zNfuXEkQ25973-6uiEYmIkewrXWd4pjn-a02hoXWdvx1pHH4psLKzOmDaM5KKg0JOfUFdWgBJtxarOjCpXauYF72Num9__9enaFQ2eYv1_TBOllVbVgOoTv5PytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/24994" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pboEtNtmdQ4dEgkdkSKREXestPB5RFwpRKgygzfe3v_S_rqVvAv9Ph5CG-rebqqX-hUyFOxihM6A8_qlsNcWwvRYroNpjFhQygxHLiBSi_XKSd-D_H54Ji-x82x1k_ws9gPkMfFZGU7KjslV8TI6Yk4v0ttoicJH4F8UtYfKZhCX9ONd8Co9s9BIBMtw4rmFBTmvoNX8utacstyxIw92cr8hG7Zc2NJ_fbSOGixBQhrgxWelG3vuDdhpOSGL5kbM1TbyfPHXramak0T-6FNRA2ijK53KpMoOrsJ6Je1rYviIZ9shpmuuBkUZAGxkyKUAn5LPhIHoDDwdHxy47vK28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار عصر امروز مبلغ 20 میلیارد تومان به حساب باشگاه گل گهر سیرجان واریز خواهد کرد و با عقدقراردادی1+1 ساله‌راهی پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24993" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxdOSjnZzBuAYWqP5C1ZgidK_xVWwc68wgts-7zBfaUi1QpKWm9qTZ9I1my0lTo2Lvf1MMtKDLfvlaW_mgMCbAGOxPXJ6bGfrxpSRQmnFu4eIBtuk4otCS-Ci9VkUnpYTgnM8PdlAISGk8PGQ6bD7RQpu4xqfztDprrtWn9srk4cmBa7GPSKa8gwK87PCy0yU4nvn3YJA3bFScjiweRDV_xvOAW2w7EesRX49qrMGPFv46gVTYpZK1L0BGYDlc7V8jdGE5F8QmC-43WL_eoEKZWrshwrRuNGyd6OVj6c-akalLOTFds1eKvbsVneYZHaziP17-gfXuG2JdGmX1EVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/24991" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEnTNAzMVpp_7k2aTTcQFk7oeiu1f9ygvctyBUqyJ6PnYIqjH8WSDNpu3QGHOY0Yuvu2E5MS__D7ZmKIzyE0c_mvqAJ9264Xxl_0LAjU-IFOpwLEc_lIOZzLb5ejBzru84OUMCOW9UZmYWDLoCLIleuaWIad7F8YyyT5ipKLllCnjum5TxrNHfCnR3WOsgioQrFbWVzBpGD3xMKAEoXNK7_YNNLVZss_i5UYPELOywmKuAJvWeMiIgMQ1itp9CCxz3il8jRxdWLEVKGSKIH-0929O893X5tFWE9rdILxPV3AiEyihLn_1k6RjlnbMx00Sks5WVkO4Ixof7Znp72LCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24990" target="_blank">📅 13:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVAa5BXRTBYjlsT9RKn43o5zQaZJ4N8Pnk4noVOoLBhUgL_HN7gs8GjSPDG5-uyXyltqb2J2NuWvhdPMRsJFtxEiiFUA7zhZy4aVB7GQKv3-JA6ncigxNW52k0_iSoNyy6V_3Z2f3uItpqvUiiaHatzAVaoaygwAQXO4pXOHE-wwsW3Tt2UQQ6ato-2raxjo1a3FRKvZ61YuTlZdWJVt9KNoid02263mJDSKT8sNAg5kk6ZKTED4uBK_guUIRDo8G_n7KuCF5oJp79WOCV4d52gGlKeCXxbQxm4DFF8fwPVHywpJy5WpcYtPkJYtK65m-ZlgYQTpwwiqsWx25rSQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رومانو؛فدراسیون‌فوتبال‌آلمان با ناگلزمن سرمربی خود قطع همکاری کرد. یورگن کلوپ اصلی ترین گزینه سکان هدایت ژرمن‌ها در یورو بعدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24989" target="_blank">📅 13:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scH8ShAdeCD9RiC5lzvoDSHawCU5g55Swj7lC94vRh-uiiXcLKsom6gztmlRkB0O_0LksrWfu-QnTJnmj6AZht8Q5Ctdfy_tdjKVIIRAf0ob-m2oMh478FEdSVul4RSZ4pzpuN1d7HS1D9FcQxXgF6jXk-ZkbVr4bLOB8furlBNq-77lPQPdiechIcoFlzMQtTKEeZidJTfuWtPqEbNNC6T5N3nhNTvxz8EzJluMpCpyCK-c4aNzu-8HKv06m5jlWHTHjJj8rMvTkxYb5vK5heYICHH_JtD9XJVxrqgx1aopmcfIpIX3H078pQ7_erS2hy8boBZLfeqgo3wQ-dj0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار امروزاگه‌بتونه‌رضایت نامه‌اش رو از گل گهر بگیره سرمربی پرسپولیس میشه. در غیر این صورت مدیریت‌سرخهاسراغ مجبی حسینی میروند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24988" target="_blank">📅 13:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ll9EkuL7IdocoWceTlaodEcn9fK6wHuH88evM051Tiuyj-PzlmEODelRs5ZqG9rQJKT_zqUre9lfWPSjMPJ7Kr2FxTT1jz_q15-zBQS34SroEBXemslozZP6X8kJirpm4tEHKCUBHRRj5RZwIwvb0WfKUgkHfaSe2ALurcp4NKdjSgnZcyJgUr_S--byCZPtfLNzK0gyWPCtchOmQi8EqWX5mjzwyMkrisArzFWNOHneg6dZToCJJQLMoxiFbENCXU7V5QZNzXB9rn4TXXeoD7Elh-SBBoXtUbOdA-heC7MtEhWBP09-k48uHsO_sahm89Ud3l6x2jlFz62VBpOxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24987" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ht2GfrqZfbjU-B4iEVvHxYAw33eG_ORTopl1tZtsrvB2j8VOu8dVEpikkSwLVQbeZ_naa6mii6THZf4FHV__5VA6i2QogjlRZ8GGdXQt5PQaTYAFLCRQ98argqiljskgeZ4sS1IgEw9TDxMVPcn72X2ZWq4zpHvslyZR4BKUD2a88AReaJ9eWR_fRZ0tnyxfRBdb_pMFqFkxCbNNeFjQZFpvaywJB6GN--Qf8ThQvqxQocqJ8POAeBVXV2ZSzMlboU7mG71d8y-rc4Od9vcBne6NVDWBV22N20kQK_dqRVYUz-0BhwEBAlP_x9a9mpDrq656S_wMmvXnzQh2GPZbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24986" target="_blank">📅 12:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUqZzU3F44c63usYF2jUbX3ypKlgnaC_YbksjA002-XxGvFa4Y4lVC0qL_Jln4v-zvExR4Q09aeDMhrSgIBZQMwxnqMeHxUDBVygqsOJDYvzKKcyBbVpD73UQ63eo-CO_Hjwn-ZOAd5qIr-NjOFZ9CdnFe8BaxWWC4Pu1hdFUcgWul1t4mLllgHsfaND6oBOxS58cqJrUcN_X6LWfOxlUJXddOMuHz5x9aw7Q1gDjFuy5KI9IUc7ZxXrsGSRiNXzRf27gE3xurl2bIrNu_VbzF_36cowaiDy_FGoF1_eTSa7BD6RbQz4JNrz3Ql4zsIHeMKWay0f8M8Zd9jbV24NBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ طبق‌آخرین اخبار دریافتی پرشیانا؛ عصر امروز جلسه نهایی بین مهدی تارتار و مدیران‌گلگهربرای‌فسخ قرارداد برگزار میشود. همانطور که شب گذشته نیز خبر داد مهدی تارتار به مدیریت تیم پرسپولیس اعلام کرده خودش رضایت نامه‌اش رو از باشگاه سیرجانی…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24985" target="_blank">📅 12:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU-UpIwdF3zcm4e-0CCkxWLcjW9fzpozzt6nPPytcnnmoOHvHYgo5AlRNT0X1P455qB4F-brlIZQ7zbXD16NcwItV8xHsQhmOa586NafcoQYVVGL6AF01OaF5Kd59fn5oghpdib3aHqBw44VLNLMZMYiEKxGjfB6CeORdnny0oeY0PwAzYNj1FJsRjSIlwj3_nW2WNanfI2WioG404T2LOhDWL8Jn_91i0ZvPNhGlsiwi9kcqbWh0irKWeb8QgxFREs1JbCsOpdBwgFjMLBk_KdmtI8bmMRWRdSiBVbGW5L1F-_L7JcSXkwmMee3Gq66GRx4C3YatffJo_Khelz86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdOyIubnmliPcK43sACt5tuo9kKEIHoV60eYK01dPKFgo7xZGTOJdXDQJf6AinUcDnXRXRsRrtbb8_0WLH9MnX0xEjPYPPXx2j3H42yG57z3igWiWfdBuwI8jmvowRZSmUB9ldu2S0r3Si-_vETBTYZvD595JTo4kqHfXzZmQVKbxnGsrXi2dwjqRzxek9ZA-pH1zP6nwzY8MLGBgJPkWDW775-joiPB9y9fzsqwsyCzQn7kSxyyRl3kKNh5XsXHH_FYZ-kMCw3qtrPz7G0r-HqXXWB63ZGaGra3BReCjt2DugfqjjKX0LNUm9YJSSbYXkGWrgtWoAiAcjV_-gYxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpYQpd4Z_h17HwGgm_vlZA32y2HSG7MaWnpA8sjDvLLR_y7v1aOhiL1lH8iBWF6aZ2b3kb8Wd7QxnUZHAjN3-flgcNLyN8ajH3m6fnCmbHE5IfT8s9kfvlgqazmArEoO1f7R5ZFt9dKOYllxDFTQWa9P6V0_U6LHmgTjw1rYlXq7TrSiO5s5kyilK-7UBZGHSMaXRSmLydmhcl2rK8ffaQEKeHSyC7K2oHlAA3D9KMxDCK8EmHZIczHh2bYYCYLajeE8MwM87oAc5ZQaYttyg7wRp3Mafl_nJQpK8QQIP13o_mPPnwEl5o4WM-EqGSezz7kk_GoAapmh8xINTbtSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRmdm1uPOM5rRHkWowlWNvGnoTD80oIouWTsY-quLyCdpJ4NcA5U6L7asBVftCtnJ3-a5xTJCT4xkXnqv0BysnYiZKy11xguhBBaeiUt26eBcxslaIILx0GgudK1MbIHRuiitw9xOrMuLMMF1BgceAmxS1KAOs29Cz1AABJwTpLJMxty3umVSb0ThUBqFAPRn1KDAmL6EWs69mGTE7Ynu8g81jLI766_fe9wzCd5tWM7skCRL9XcCOhKV8awpeNfICLbdS-B5KdmDmJTp6crWXeMubQopOij0eWihbLW_jdK3niISWgvwn5E6HGlEZSoV4M5E00A8RkXpUNgMCkOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24981" target="_blank">📅 09:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=VsMNtbhzoMTUAFAo6f5xTPHNkan4UNq3ipb54mxidB8wD186GSK_eS-hfHEA53n8jlj13rLNv59lXdeoNjKh88R9jGAkmnsCE6alrWD1J7hpwLIytqRGQbaxa98vEW0Y_gbED0G_egdgT8KXnUWQnai4fnCi5nwdzj1Ysp39mjIJpC2qJz1iSKfjXKcG4IiIkq3dw5Xinr2QDfN9QoUh3ps9u077ABAXCZVrOSOju9RQzDBFUh9DCaOGgPPiLe0gCEpHJZDEE4gSp206GllQ2cCWN1BeDqP4kNXmPHXdUVtRB6AzT9Pnb8HqCwiHplh3jcfPpY1MaGnNoBVJUPf9Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=VsMNtbhzoMTUAFAo6f5xTPHNkan4UNq3ipb54mxidB8wD186GSK_eS-hfHEA53n8jlj13rLNv59lXdeoNjKh88R9jGAkmnsCE6alrWD1J7hpwLIytqRGQbaxa98vEW0Y_gbED0G_egdgT8KXnUWQnai4fnCi5nwdzj1Ysp39mjIJpC2qJz1iSKfjXKcG4IiIkq3dw5Xinr2QDfN9QoUh3ps9u077ABAXCZVrOSOju9RQzDBFUh9DCaOGgPPiLe0gCEpHJZDEE4gSp206GllQ2cCWN1BeDqP4kNXmPHXdUVtRB6AzT9Pnb8HqCwiHplh3jcfPpY1MaGnNoBVJUPf9Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24980" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDRrnCg7pM0S7HmdHX1Ul8Dd4bnCIEOQ8Q8CqGgVwg0-UGbajiqxXeXUnW_PTVo_ii_A96VeI8FBEPkGWgibYL0XruUfrHEWRvaWMwdyQynnbdSbaVxmvoBdCt5-3uS40ZAUd5vDAjEmDEHjPRONYN6BO3ntjQPfWMn-kjm8hnk7gOVSpeLMUXFZXLph-YugBX53zIRDc1O18MoRz_54EBPXau9CWnJ7KIx6_aDUdLIcJPW7zbKbKM_il9lV5SFMFmLJvSKvIIVYLb9RCyZJYWcYSnZaRkfawO3qdiwQKEJljfcsB579rtiW_nnsI6RmSnOAyxQJJfFZvGa-C1oq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=aepufbKeNiKlMYl_yNTp3AZuSzMpUM7UvGutzFDrnEO6oGyuFUitnjWlFUwPidTWz5QpaMboF7yViFEmMpXjww2eKQy2seoZyNRvIvvCIzzIUrhKlLJzUiWENzA6g77Xp066_N16OmmIzOc4N8au2g6q5xUAFinLDU_7h7gS8y9L74nuSX63xkKf5k_IMKfbzjBQKlBu80ybJw7CCrY7vOEV13MEKmdP6Y613d-QUOIDHGscTAuE09G-XvALZL9Oew6oQqcFQtcj4DHGaNlVreFvrKIuyT1eTLNJjQXCX9v42DV1XNMhtcuiiY_OG5FEOLCwcUXoAwGfU78k0mV0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=aepufbKeNiKlMYl_yNTp3AZuSzMpUM7UvGutzFDrnEO6oGyuFUitnjWlFUwPidTWz5QpaMboF7yViFEmMpXjww2eKQy2seoZyNRvIvvCIzzIUrhKlLJzUiWENzA6g77Xp066_N16OmmIzOc4N8au2g6q5xUAFinLDU_7h7gS8y9L74nuSX63xkKf5k_IMKfbzjBQKlBu80ybJw7CCrY7vOEV13MEKmdP6Y613d-QUOIDHGscTAuE09G-XvALZL9Oew6oQqcFQtcj4DHGaNlVreFvrKIuyT1eTLNJjQXCX9v42DV1XNMhtcuiiY_OG5FEOLCwcUXoAwGfU78k0mV0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه خطاب به تیم پاراگوئه:
اگه لازم باشه دستمون روکثیف‌کنیم و وارد جنگ‌های تن‌به‌تن بشیم، این کار رو هم میکنیم، ببخشید که این‌طوری میگم. ما اصلاً مشکلی با این قضیه نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHHxO5KBnvtJSNWhwAC_8Lta3NoUuuqk0ICkK1KTBTcj5Dov5v1WT3Q8Hj5bAEV7fZhGM7GwL8aBCc_T86_t8gF6nwb8yv9KjUxYk_XKQ4K02bee_O7J7yxqfIaKTx-j2bxZePKdBd-TWIaQTJCz3cXcBZVZTsWiln8W4dly9I8i2xgbRv-iJFT1AzM37uqpVhByHXI_ps7RVCOFuArFI7H90IBRHhvramMMUe95m5tAqhaYlrIbx7PSGWcSHkmTnEq_z67mM3tY26r2ii5eBvs4l-a2qN8Bvgj8H2HfOn0QeA-gIfQenkDLGEZAtwUvUBFIHHUmV-P2J29FFv84sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=GezN3ksoTu6rNwnp01shMoZMDusfd0yKil5tND-FbS9cXhnHhLICGAEoPMUwrZFWwcsJStz_MVAaQu3FfQF9oKlu3zCLSZzlA9es029n14NAXBhtMpvMx4rhDRrsTAqnS4bs0QsQ8jdnMquQcDVmbRNWXAwxn8oyxQD1Vmez_n-JkyvL_GHMwPyefwOHvLyO8u9hbHIcHyOkVUBjW-nt2Y6lDjPqDpulqpBJHgCI4WD0mdLBzREuICncjV1SnTFVBr_HPRnLKHGPCZaxj55564rUJk3e9dqhYJOn7ryouRwuaEMHYB0_oag-9NpXXHpySzdzugRhNHkixExm6txj2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=GezN3ksoTu6rNwnp01shMoZMDusfd0yKil5tND-FbS9cXhnHhLICGAEoPMUwrZFWwcsJStz_MVAaQu3FfQF9oKlu3zCLSZzlA9es029n14NAXBhtMpvMx4rhDRrsTAqnS4bs0QsQ8jdnMquQcDVmbRNWXAwxn8oyxQD1Vmez_n-JkyvL_GHMwPyefwOHvLyO8u9hbHIcHyOkVUBjW-nt2Y6lDjPqDpulqpBJHgCI4WD0mdLBzREuICncjV1SnTFVBr_HPRnLKHGPCZaxj55564rUJk3e9dqhYJOn7ryouRwuaEMHYB0_oag-9NpXXHpySzdzugRhNHkixExm6txj2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs0cpzgNs6BwDOPPznL5uOQj2SHuSfFVme6fA5Lc_QmMe3UKV6rtmroMOMKFCDvKS-iwSNa-Z_FR729-IZBBJJIU9146vvlEGes1CMTLaZ0ooJ36kF0MLeBlAJWJ574IMiWozVg1lXbmeGjKR-OumT511hHfE6aR7cL-HwPWxj5jKqTCiDRtMR2_rUSq8AHi79_zyWClBbUXoxUYmdLFEK-B8Or00bFwrDNvzq3ehq-ENWCSa_ojbZEQf7tUtKcfLqwd8J2cKCG1qJVgUWUjVAM2UtyUhznSBTwb0GDR21R77oX0qHk6OAsduzDogEScOTwH3C50-c_zE9pdHfz2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO5yBqTVBE2sm20Gn2dHqnv7TIdzpYHLOYlknWz869D-_CAnyMG2ptkbvEpkZXRBNz8X5WL-aNYPGksOc_ywjvaOhhMcS5YVE_pBSOtcyVEq6pLH5R8ailGmBGSVII0KWQ33i3trdpMC57V811BW1IZQdnbQCjaOq5tD0ex1_nukJHQdLhxnEC6lnVdLK6T9BQbPokCBqjv14-cV7ERuXNN13CTCTBv2uEEahWq4a7RAo4qolZxdf32pqNmIHPjN0VGwf7taeFNXbYpZvBZ146tgNmyLA5xBF4F3aqYIP2eLyBvc2xnUh33z8wneRjrocXTzWVpQ3WUft03E7VbgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdMH_NIDsspAZrlQy8RerpBR-Cl6HqA6-e-Z1IYFMUHKJKfiTZKKvgMJjTAO9Qx4wqEiQlDZeZJEIEBTHz6Z8yChtDF8Jwjx7D2NSyfj73XmPeOSOdhcTPvVq58vB94Ov7cFRJKUlqAgpDbPn0Ld3CLUr4L8uzbb-V6qrRBJwq8NVlqcRQD89W41iKrlV032j9mBn7mLG6Y1Qn0DTWZp9FqFijr_Ac8oiragTeWaEwc7YMTC_rHHgKi2_9zu3KyJHjwZdxZpsTB1ArJuEJFQpXAZRDc_qiEACAwWAdQ-YHA4flmix7uRSl9prLkAdvhrPQFH47WS6f54LDGU7TaaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNqgkvMUhul15PXaRNTNu_AvJPBfuEcXEVMZeAAQH_gie1If4LUdhwH5dB3eZWzsrrDLEwk-kRsggZYaNV_8wJTfj7U1XYTjEgE3SPUOv2M84-CIMYxWDtsjGKps5B5Wlhuzy77nzCkMvoy0kx9d8cy9hP1PHY2ZjxbyfNMSejMlLvVTT2pGonf1LBsjX8_x9QONvPqlA4Wb8SvXfxqw6-6213XEFa5-XfpOqNSxVTsWBHmwBA-fKh_HnF-0pd7gaLWJzsQig3EjTjcNFSefUqMGEmcqVb_9TdoZ_fQe9T2u9jlrQ8-mzgM7Q0CLjnZY8CdPPxsvQ5HGGjN5Y7BaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDL0LB70NJOFzaXs0iIy36eAE8QqsaQSvkL2adBqt24Ei3OF1Sk6bR7ObbDGcteAr8jsfIu6HbcajcopxfsnRXIpZ1y2BZ-ihqAcp55Uu8B8pkXOz6_zwtUvJ5aMg3bzXPbGhdLUFIANLqps4i8af_d52Ru1D79-qPbtyD05tL1eloGFSvGWxGZ3YkMI12kgrUuXp3SghpCSzjGvxySEd7txWF2kFGyY-npVyYGrFe01MjfoZw6HmkzRVHxN-DCD1ABDVbbJzEyLoJEh5y45VSi_Uti6knFEyTTvATkgyMgLwebFXt2OBMt3LZskWFfCbAzr5GZxc-oGl_OWBIh0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQbPyBUYqaCsvFw390eV1aIVkLiSzXVTPtuOAJV4DUtWbzSKKT3kbbJgx0aoTUtLF3_hHWu3J64FgU148YkUAEdWCkvGGKFDysmsyClnjq7BDvTVXr3HvDvOROcRTcZkY7JW9lAOGQ5v_NxuGqIYRy89guX8xgku_D8UvB2nD_Sn8onVdyI2TDU2Yx3pXHWD2oi6RnIsKAneCXs_iJSQ5UY8P5K-J0YlJWoPAjzuvuBYYZtnKpfq3qi8Bn10qFHWqZkJ_kKJpYr1Z7F4QikA21L0ohJDTgbXtaR-0Xn1yZC2mKru9R2EuTIGCqwEhKH-pGgzkAE8H7PmGb7qMKjVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnlm3DCZgq-QU8dSTinAKWwZ3XRK3gKieW7Foau9i2bFK4SkkaLeIjPB8HHfh1tsolHmecAKot7Pwn4k62NozMxdfkZHG4y2YyEocvP2v_zvhvtUAiNhR2pM731rrJRTMrPzBnmueWlf4XkzYmoB9wT_QouFTwDbeoMac0RrE3RoH_-CXMMg589GzeK1HYyf5qj168oUXsOzar2z4AoRFxCSYasRQ-CRfOmetrY3vUOGmq1YCjzLzaHdYMYtO0ecAXAri2ysO2m5r7OmNCSE8GKZanKa42CSQaK6wngWB_f5mQwHfaVlSDGtFU2OysaSVYPgLY0KRxFoPpM-9YysMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCqVlt5rACVvAvD4oozXQyYb0x1SB4r148h2_KQMMPepYe0q8oGeARe11pQE1jAnMEG0rXts2bSEhZJiXS78kCOCw0m1t1ju8A3wPoYvcw9mUvJYlySUdW6zVj0MwfosrtjL89-MbV0NmxGuTHcjnFosjr772bxElo32-yWaF-7cKMiVy7kBW-pfRRzWNmCDaOJrcBUUpXkaD7g7z-StLuDfVMYcAiIJk5ePeXJFJbClzdO4UOBaFMdDsZdoxqwTFSEepWARNnXlPhEGHue_UxKO9hnW4VlX1G18gb1xr_hK-aN3oe4dbAE8obd4l3yUpmi8gG6VzM-wliucFIiC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7KcqKLOMIPTmc1pVN0nqF5N5bu7h2DDsEaZqTA9oU91-rf0VM295kPKmGYlgzUl0vBaK74XpyT4YlSgmtbMzMHNBpa5rcXDMmg4JKYddt7IUbiFj_OGH_o_kp86OojwM7Dxuvr9hoERMHZ1R3ZFxrOflncO3ia_3wC7wwajTBhyNYA_GfTtqpDE55QcBU9sW-gPna2LBBGcmjhL-bQjph1kWvPhv_V9r8_pyYXKgGrlUPKF50PyaIDzcwI84wn_3cFeyyKQoR3AKhOUetE1ee4SEvp-FnGLpnlyZ5BNu-uVVIHpsJPiodz8VVVwRNW0_q3cabWwkU6uYg9BZU2QXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdyVwVCqCppy4ECoxX1N5CtL4icCEXfiTWJ7t6dWZgfYijK1mgmsQx3ivZrmkpZusc5mh8jd92HCeyNoHNoWhVCmi8Mk9Kpd3n--JcRVGbFgXCKo6fAVEDRm_50220D5UUlDa_cFFFMZFfxeoLB2qNtBIOZcRU8x4-bdEuU_6suPnripZEcmeadP4_967xQhk5FErabVWOpn5TXxZcp8nTOysUub4KTb-V9JMcuR9OlWaQyLiuerfsku6xOlbCQ5K8cTw18zzQDw8FRReJU92_ZHhy4mMzN7LSUPVhZ9Jqq7shAFztTawB4NZSE6xdHT-nd-zDViH_thb3tpIKOF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک هشتم نهایی جام‌جهانی؛
پیروزی ارزشمند و شیرین یاران اشرف حکیمی مقابل کانادای میزبان و صعود تاریخی به یک چهارم نهایی رقابت‌ها.
🇲🇦
مراکش
3️⃣
-
0️⃣
کانادا
🇨🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpCV4BTwW6WUGb848v2_gi602iVqAxeHWSyfsMT9evlmFbshD6d4z4fdk97PDYlaVkCd4_sGw_bhygPhVOqBEZrPGfEb0l2F65M20iz0z7h6-PFqcadsZFx3QLoJjBiAifV3hsEtm4btGp73D3_X8zKPym-ITPmSCQrbMvHt-Ll2WSXHLZqeOg1o21unfvmGZqthoV18izzvsnouHdxxOc0aWN8unoysJLfuvsYjXT0QGUizLW93CZ6nCQeSlo7edWPDzkRgkgpq0H1c91KnvLSZWJLAFVdVibjAEw5rxj6MAg9E1RXxCHIhilbUY5HX6pJV_A3597i1SdrgPZkNbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuxasjW53ou1ruU4QIglBeo_10JbC1cwylpdFuLeFLsIs4sZNzkh8xKFY9vmzeYkX1MUWSNQfoXp3xiOAzCMXBk1j0nRwhTt1cBV4tTYRHOSGHqrM9zaLV3kYR3fwQzIKztWlsEwdepw30gJJuDbHXK8YKGc6l1n0d7fvc5pGa9DidHKPRRw10oN-kpr89XKg2EX9EIfrRypVQd9jzI-p6CXpN_c0N1RpbZEfaNQRREuAUHv9kq7zRz7NYouxXmikyIrl0h15ipEb02b52ArXLbug5EedGwfIP3SoCuIIw9YIjRpzPntxfOWdOFgBRRXoqFVs0ATzFv-BaMjguCSvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXrPpvASUSYyDpx3LqvtFpIj32AaaVCcDRiejfI_l5qNnbN4tbMQM_IiD76n_ZIJuAxf0KreZPnS7mzZxCwE6zzPtXmhFwhUWQUFszuz6TtibWqIPvAMhby0kPoZTpUs8OZA-JPq-ILTpdFAHZ2q1r2kSJCf7b0BzugkiyQAnh4CSXLLhkp4sfsE2nw-Fsb7zBlaKquEb6fjrIswIMLVQxr18Z68_DV1yYzmk7swIicMph9EC6VdAWf0Y0sqeQ5NEeqeQkrrau0_jmVtMLP4eN-WezNnWxl-GaeJaRR1MdK8oquIaybF14RUiBC0mOSED-P4CW1pVBetcqTtbHbkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx9NTp-EvM-zzjZhaN3FamwpZ68GhioELq8yXwmeqNJ_uqHRTXU5U9ywWXzZWTQuwIIOpkX_Yi3I4yYu0Nzax44JtC1lDTH8OkOBRg5Ee95HWaJXxRmf79mK3mzImq6l5p3zVD_xlHKZM_HKVfkJx1YMIJsIFCSv8M5Pg0sgWu1IYKgoq82kbtx9HYznYSnxXpimBDtedRzAVLF50aFAMYSox-NXXLMshG5g9EAUEq9N02QF5X7VuNSz5je-B1orA-9_P8yy2yUJgUshP-48QnW7SeCsUp3a1kpsk5iybwSY81HjrGFJHMZusCOTqz2SheVIsMScMJtLrcc3VBCocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mILzayPobTG84Ui0EGYP4g1baVIa70lxmSPfIRYyBduD-5wGrhlpRIZQbA37OhS23p8UHQ3_ito6w89Za83EA4k9qEuPurBfN9gPYhK55t7E1JMjZZF1ACla1G7PI73XUnZtJfjRYdW-2DKKteNVAIhxXPJpSbu9_z0fcONxVwHDW9J3TzVUm23TR3mGHfBcaJR-ewAUl8Kt4mOzqEis_Ts3eKzqEO8QJxOhWNiFDxDfBFMWOjXa8MCt39n-CjxZtmSE-I-TxvZmBUQcfnUK81DCVMpGbPvXTCO4-DrQBAr5aLwQC5hh9kTzS0XUxlhnPFbi0mNcFUY7_J0o3csF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k66H7myEe-65TurEUsEzpIfm9c8aEdFBUUxV6w1ADt1h4rQV6WzDdmC-e-XvRGHupWffd8zPZSAE3OnhF14pOxMny-TffXy6E5uH5FC3omu41OZSUNzUj_Xi_rDP2cx9OxbBCSl2KVx_g-5N3085iGWuHj9Iuo7bDlqK_2BZsaIZjMUN-vHyDMv_A00YIRKJN-rrAy2kNeY4pKOEEh1Pw8ziDpUk48Ev1Q5_JOqYGQ-c-zV6hiBEZJifiasXNLI-F7Z5Vi3B3s-hG6a0KvXvAwChwx4vnilOZzSYfHV2KefNp8mjv8VVfBBXkKgmxnekAJzLaKYa3t6MY8PEv89wfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_mXgC4r7ErgrsNUiK1nT0xxmvi0aHmtiY7qkAX70TavRbO9WLiujI3ClvwSLDlY29Tk1zFIWzO3-LD42RxlwF7sC4bLfltq6yj1SPypNVrzAthITuY0Kzsa3t8BaNTiuVOZtbEPtWRUjaCLQad_PdXXcuUfcEnmAf9m9yT6sGFjcWq4kWOpjyqdRfagCP2V9z9hHY5gL-v_uMMwgLKeh6A2alGwFGbN9UTf2F5snTM5ydQPmdiF-EzwpYftrcDLqCnPBYV-wbcCXQVLWDxNhgS_veUfOwcPNB1Fq8_nrkVmF_P5bdTLFPnlZBl2SERdjavF-OSDoos2UR9_ReDbnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
کانادا
🇨🇦
فکر می‌کنید کدام تیم برنده این دیدار خواهد شد؟ رأی خود را ثبت کنید و اگر پیش‌بینی شما با نتیجه نهایی مسابقه مطابقت داشته باشد، در تقسیم جایزه
۱۰۰۰ دلاری
بین برندگان واجد شرایط شرکت خواهید کرد.
💰
جایزه به صورت مساوی و مطابق قوانین و شرایط سایت، بین تمامی شرکت‌کنندگانی که پیش‌بینی صحیح ثبت کرده باشند، توزیع خواهد شد.
⏰
مهلت ثبت پیش‌بینی: تا قبل از شروع مسابقه
👇
انتخاب شما چیست؟
🇲🇦
مراکش
🇨🇦
کانادا
شركت در قرعه كشي:
Https://t.me/betegramd
📺
پخش زنده بدون سانسور در کانال تلگرام
🚀
برای تماشای مسابقه و ثبت پیش‌بینی، به کانال تلگرام ما بپیوندید
عضويت در كانال
Https://t.me/betegram_official</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsCVy7HkJzSXItO0doahyRo-7JdCITUDU5HlxghxAFBuvS7JKXLEVAMw5Ns-TFTIll5Le_fcT769b-HyEFFz1QmfPdg9ZYhje6sVkTzl2gjd2u3KBIgwQ_S0s3eyD3Yf46iAwvv5VwMu6eXlo0Ic8RulHZq9z69mpN2BqvHu4yZtJ1R3XEKCKBZHCPh6QgFRJ61bLwBr4RIlepwe-T3WCohsfLjXa7phQ1x0qvYsIdkhECGB_vTyptCPsEW_RU0R76FrGEE8bDN5OA47GYEYXR_dLiuY5YCl5YnLZqJnqMFQYBB4-LqaLc7bjjo3wq6wCuyXj9fkWc8JP4LyvYqjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keDUlb8Lt1zXOGNy1XsSLx00LP95OvBb4Mb1nYW_NLHhzc2dZJkU4m_3kFiHk4F8X3PGkgRmc_5Nv8bd9gClp1RG3eemR9dWkxoDFZqZS1ykqyEptww23it4nmSu_OEo1UZ2qEUqod33u95-MlT566B4i5ETV44_2MFBLcg4dUlXCaMGKF-AYGAmatceiGQxruxf1iZ-P6YmfxjLvsnJ9uZtk0M2p18pM4bSS_PUoshkYj_t6ZLZPHnT91gHzm4DpTwzPO4oPts4YKZqhNyNFfhpWHuRqMPnhlTyqRxAp5kF70XTsWvmaZZylDyjvYhiQT7v0-iOHNsJuNnRqRjA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFbMVMOY8Bdi_f3Jgxw7u9peIijKzWbnqsbSxQLINIfBaudXV3lstxAAPQuUQR6xO31_3hh6-sDo_IkbUWSozdkU2tgMVuh1wY2-VZM9Qso6R0iDtIvK2a7KwE1E9KW9cB6WYejyxWHPk3gT7qbrP47Cv2jwz-H2an6ms4m5eTNLKxiNCtdl9ex1aBWUBCBvCZGj1FkiVDqV4ufNcNyc0JU20sqwvcpbvjsnkLY90AZqB0ALSq1epMZnftGJ3Dv-UPIjxgq6shGTvqHc7K3p4D2G0xJTVItBghtTx403bOV-3rxIFYBILP_cMZrAktVl2YyxjYIAIUJ2iU6cLdQ9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiwP1GgLoS4zYgx9Lu32s2IKGBiuba_GamQ3qxrNuzxaHzwRbMBtdSKBMfKSQAmR6EfOwdWvJ2qCJ1Rmi_vhrqQA7l_cmFpmJmxIUFOZCcYJBCKOjKGxeLC8_yaUSAN5f8kffFKH8-Zsv6WGzmx6bAOUYJkZZ3KdUiCeHp5pLUAL5hTpS_MsRw7FZZ3MQGKJkdsFHGE9hIbbuwaTYq6IB4eTXF8By4X-mhgyze-7ncYAebGO-W6hUO2k2swlo6VsQMiuHLlcGj7M2rXpPXxYmXUTBcWLzhncLU1mKR3eLduGhhzGKbhxd-WwQunAo7Z_qB4twL8-Qp5UmbZKJOOktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLf36UGC684DEG5fzwKmpDpqOy5WD0Wn9U3A7NUHp8g_sU3naeZW1FrE6RAqqj8vJ0tJ2RNx5T-LoxUS83I3UwBWaX0-3K_Lgofq20WV4CyI4RVLY9OX40y744eI1wxSvLkPH8cx_qE1UvLu9Qknzxd2oGQtxZ4XJPtGCTQmCi9nRYRMhxAMNhXEHAvCYAk2hxwr6zfxTxUvh7v3fFaS6ge35YT6MQhwe2w7OgIu6QWUe16TDYnsww9TzzWfDQB2OXxxz1KekV9p5NO1tC4zbx4-SYk5Dl-I1i418fcZrUQ23i4sWSceZB43-sQYRQ5dx0DHxTDcyB_jzUvb9iCneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMv3LyU3p-KR6uPnnKpKrxxmYxBgzBMUy2sbgLE1b3ilqmr-GPBpIKCuEiF1gMm79yWUSAkWpJsI1C8hZvuXwmwCtrMcRMhcGHw3v8HeydGN_Z6qgyK3wVObxGVO6EkAlPxKvHqwRgQDWqy9T5aLYiledR0-xZijRDWOxOG9SEyWXbbgeoMUUhlU034XVcuyO13hPm5utCf0SauCHEwyCUFJHkvfbs0nNZ-Z73t0JGcO1pVsfrw6ZN5A-aEm7YXzXBla8pFvv6VQWTYfabFongAi2JSuOEJOy1Ob7R3Yq2QWTuAxMKNeZa8zijCBCDd8EASf7aMxuW9SH7oy3hIjZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPwI3oYuAqnmhfUToWvedRLL2S5J88JbqEM-XD2Waqmgwj1MKWTs1JUGzUq2voBEU6gAp5UUayBnhBsvyNdCu0YDMeKX6wb-NTtdhJZlx3ZJTl6cfMl7x6cZ3bshJ5ZP6RRLvNYRL0XdgXce-ybsY4Ci-ZBfjeEyIU7_DWbMrbiItYD3KJ3HdJVKf5ZRIYyioU42FqYBuVW75_xMW4J91n8_kC1xvmrNuW4LndE0fBhmPH-sR338U6YpIeWi7HR6WYmJSszXrE5cu7hzMT_kRJskAyF1-HvY8tB2Av1btTvNB-j82My73uoIROdWBYfDaf606jVJ4wbEVC6KNmeMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giThAnPNWJivSbfjN0a2bghiY4wkyzHNE0An9h1IGfbN6A5pFbJD8u2Ky27ZIM8SuCVvLaqGVkGlVLMR9qaCRUeqIW8XLRoxk6gejhAlc4CZX_N8n1R1LYC5x-Mm-9-bPtwGlpfrct3yWFJY5Rb90f5NkPirM-Uz_xMfRX09atb7GT8XXm6iK8srTv8Bn-bidcwMPkQJk_5A6j0C3EOypMU4k0ld3X-pKG0QblBl6oLYEEZuf8UBGi7o__272yRi_Jdoeuo2AyERX0mdNBk0Re7OYNqa0u4dXMICaTDccoyXkNgVSkw2CpfRASk6VU-0rir1Pvf4gedbWBiB8UdZ9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDTyANe1GF5CWkP5XajatjzH7Nay7zDZYzOkIU-ADehVn8GwEFMQFty4-Mk6ul8cFp7Ubi6C9rgJUSR_HoK4K1siOic_U_iufa9FlYHSnoTWVYfK5D6l1isDDcS8M8ot1X1DpAgdOE_FBc67QFC5UkPMMZ6acY47GjZPb7BQdnlDixamQdKnBeWuHMbcMygl_GK_NLzZFR2AOE7gCMz9usA_UzvlU2--fM-yU3u7xsjU6BaA587Ccu6g53HvtL_8_urV_hNNvtKTCRGBGs1x-1Ohpixc_3P-eNKQ8vq60d2Ke2gI7qifHscWQuACym0WeYB24Ppf7Otro575Ig0HNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkXkhU-D03AUS3FqAj3ARZzzwtip1o43cXl3-hnY5kvRGUPZlMy6PHOZjMHdocl7zXzF_BL3LOEO8v26hhpWI0seVB2Em7VYJwm_gmBaJAuvZIrq4n8JA2QHHuI_iTekFXamHnmySGpAZu5T1ief8MrIad-oPSki1_9HY-OwdxNMQKxALOB9fxJFip_uWKyywb3BSELz7u57v4StQjsWSODWEZQGKrfOscPLxA64BpS47mXTKL3k2453qERhtWmX3FD5MDcmkwN1z3bM0JATv0c1sjTmy1agwxqdEqTO4BCn0w6sIMm2b7RP8DmYKpUNtEDsoUfRqosB0pcJM6xIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXH8-L6-xZ3Wkd7QGk37svDKXFkKELvbMfkl0WVHKL-cS-Bv9yBLV3q4-fCYfgnkq-q2eqVpiJJs0h2C72DUyGSVsia6zwO-cDkackiat41mbCzlvgDYCDLoLPH_GVZ8nLdqCiZROtn3dc3HmK4QI45zgl_5TN7tSN37SOwv7gdaBkQEbA-4kn-TvBSCbEOuikQrXfGW_zsvthtFIGJxJJ8yH_9YrsELTApk-ODsb2nTHpJLIzZoAHTxL519nAkOU-_67c7O2s4DlZN-CK6jnshtB6cptMTbidOsYJ6ocLKSMDXF54erwGESiM2HITcKG_9y-57c8kVGqqDBTqJJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCcHJuYmEsK2nOP9fv9GBgusLkzTPzi8o4LizrTRJN5_T8OV2mmDsA_8_hjt9ySXfCtVh_iSkSMqcCHsoLZ4krz_QTzf9xdKUFpQObC-isj8ksnCBoyZ6RjZOFlLKZ7qnT6vN_Rn4aLHyV98YHQexgTfig4Z5AwGW1N4rX5D3gl8I_n1zyT3VYsIJDIbtrMQjN82EFPptgAuiuP6nmVJhaC-RbWdAlfRNHsxpK_Qnxpkt3M2ytYfsVpO1h7o92O752ioZ13ZjvWortNciAxKC0axQG_ZLy6C6pGyBmKUm6IqiqHEGUbL0v2Ywp7qoM5fhwCVH77X53pXUaQ_Zf6WgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjsKHD5n80oHUwpN4JGBZHqngk2B6gY02kqMI5IC-X5roOhoOVQoJtAvGU_SbeGxmuWUvR9ER69mzrzFq8JMkzFiDQdkkUwdKEkCgO36AAkPC4JsiHLCW6BsrsUmTMuywasSztl6NrYl1o6s5H5HczwGp3WPYFW3Oow2WXNTEpl7_2g8NaIRuvkWFgTKrAmriBRp8WnKfO8uvxf7RSJpk1SFhA_EgVx90PHySvJyH-Tpm_8vb9PsqRXP-_y-IxHybWO1--g3qhHNEUcUWROUPpKm1_-YdT2CJu9rZNpM50Ekivu8x3eYPCLiALbntCshhVRVTVPv_JJ2165MKOA_4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odNJ7Arznxmqh5md3nrUcGnp0-tKIYQWYzgWnKB7jF8lddWF8Qkp8aL597mv5VAFM7LMwNfQA69BWvvJ2wZK_is0id6lx6-i4ZJTK1aGBKGxVPnVtkPJc02W_I2XlCoX566JJbHfQOn3w0Or4yrwC1BkjKa9CC-CCdaCGh0NIUyyPI5obcHNGstl-liE2RDrxxqkKpU0DP44nhGoWU2aY3HTyjuZavBXtNUUez8zPMtUgrKwfhLHUZXsIkxb9kNqMJcrZs-xRSNCo-T6_H8k7IOhF0JeRRG6rIxYQ3KM32RE4OsdbLVUMiNg_98tMj10yKC5Ux4SkIX5UGw9JDpRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X1ptHhnzF4879Yt8tjzrmfmHDKxLG7ge-TRYCF-14vMtFGaPHvTCK_iBdnhttxa3cOD39D9lSfiK1pvnpPVWe_j7X4KxyNPIRbAlua0Dpl-WHneGIWwSsFLHo7_VbUICra1K7emZ3y0eYFM83JNpjECrf0ZhkcA3JM6-9i9ErAvkh9PCYFinJpue74ZLvZ1Bsgu_yfMxFkrjjZdvzD9Lsc4I4scqH54q-KgE2l3UWcvm_GZP1CNfeBZpsQd79DkyBvugidU-UjfGSAt1Xftw74YQtZT7MUPU8B_oPwO_Wf5d7OdjAgYvCqYnUuwquzPVErLKFKFAha7-uggUtEAMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aytexsODlI5TBHo0KpCkuVPvYcLM5-1wkHLNAfc_h19RMC11LlK0ElzGT4BPnpWRFb5RBUsuuuBJN9lFOMWbNDBXvvRLj_CF_W2vyYkPAsln8HPk1NOah0_nBbJQ4P7PDjWuWPzlGTGojOhHaguB1jumVpZct1rDsFu2PEVkOSpUfTJ6gg4qy2v2YpYn1sPLoAJPzMDxL4vlPla7qtvlQR4Od8w5JL6d46EIHGIUz0sDeuO3bADjbXMoxIHoEPZHGFThE_KpeJsDcVRW6d_KKPw8aKJpNA8rTKr2svUL7dPNCkZrO7J1NngiUzbHoXzBZvISTybuTjxppi2vZlkBvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=L1U-VX0TPt0Grcqq5C2ClnI6UueyH5wDFvcROCDUHxjuQErAEFpj7gZjc_m3YLUik-oqw0--N_-vLGI-wkuI7SyKgJx6Gbq8xmNqEb0HT1TwhGU77-qwpQX6lXK8DaP1nB5j0H0kfCvYVx2Hvbk6eWYJw5yrNatEj3aJXoXf8hM4AKYhdX3xPGNrFlM-xaXOmgxWj1Xg4xO0gPLN2qFmU9qr5yJ4ryhG807KMQmmAnh4GVU8HoA9O2g6IpreKYstvjrygE9E-VGbKZAiIaNi5P3r6EjvIL81b6pB2t4Xzrmu9GO5NEQlqWqb-Gjlc7gRTrvVbVirMMq-NcglftzWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=L1U-VX0TPt0Grcqq5C2ClnI6UueyH5wDFvcROCDUHxjuQErAEFpj7gZjc_m3YLUik-oqw0--N_-vLGI-wkuI7SyKgJx6Gbq8xmNqEb0HT1TwhGU77-qwpQX6lXK8DaP1nB5j0H0kfCvYVx2Hvbk6eWYJw5yrNatEj3aJXoXf8hM4AKYhdX3xPGNrFlM-xaXOmgxWj1Xg4xO0gPLN2qFmU9qr5yJ4ryhG807KMQmmAnh4GVU8HoA9O2g6IpreKYstvjrygE9E-VGbKZAiIaNi5P3r6EjvIL81b6pB2t4Xzrmu9GO5NEQlqWqb-Gjlc7gRTrvVbVirMMq-NcglftzWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jwsg1CafkfneSY2pxORlVeXi2AZQZbN049_RiYtLQgoDnURO4HzHbSGn6o9cSMl2hwogRuormRdNNa2KhzwaW7comyOKSZKXN5GYTH83Lkqf9ixGfWlhPzHQUZAQRbjn3aVWge3am6QJfD2AMYHxlVcyjmMwZ8jWec8ZC2PETEC0eIvC91ZoDDC9ckjaPySGPo5dyNzvkuDbsIZr0oxLH6k0HVeuN755_fUBObWtx1GwdZmkgnxBr23vUlvYKIunkIGrotTtEJVrKIZz4uiXLm2O6iXd7Yl3DUofeV_ke0qF2hWSI7JtlpDC6FxRqJl-oWX60crtcGXhZsmAafiSgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDWQv2Ac1FHTqtL1eEUhJS9g7Y81JcLeCXXD2iuhOpVP_XKtFR-__ITWVv7Qu7ax7t9xMOEoL2burswHRcQWpguBwAenZDIIo6T7-fcsJ5qczUTB-p2u2xR_wqWc1zhl49d_zjX3TYpRc3x8KhwpJ916JRW51hqU0IJy5xwvhqUK9E17sTWnl_mIeg33u_sMD6d6RWah9ckzs_xv5DwiT8VsF62Yg2xoOeDkiHzkoKGRiS1ylE_sudj7_lXqqxdv07cYPfoINrFI5ZFxiBikJ_kTfukohjHOd0dI3y8iWfk_x3v3duJCGxxwqC47YfSbhT-pUFbEkgpGu-3wsIg3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKd_GQjSYh0YDRy4y6P2dZ6kX3kocQTMQYg4sZTIHjBwydDm7EPlRPmnHM2ZG2nFk6rC01ewnT0_9i_AAR2XulC-D2u7dybUCb8mHQUtSTqVtdIUx8t0BVTOT6BZjzxbrixsgBWQfbFOB8M6I19ZsYusCGiglO23TsD9ru78Wq7y-_aU9ebzoafCbI0bercmOMDL9KNgNSnMy3mWA3DF0CMzWcVjPJDJ6M_V0TJekTSxrP-A6496GtTOo9lwVHngzLjCVY56PJyXl2QBIeo97dDT79MV5qvoWPu4UTOpG7PUec1cj00J0VeAuTkEZLSPALbNSh7VyJPSs1zDC8RckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGMykWRnFUcmqUSis-0COXLiD9FPPwwD9D6EUTzS5h5U3jigFoMPCl0DshwNgqI9BYI2zp5G55aKf2ttr_gVAOzfNutiO080JEgj1IUOdIc3Cc-sOA5qyjxfrpa3tukFnUE9RLFPF1urx2SMIe7DCINBDa3xk43SVLZ65V9IDi3aSnzC8EDQf6rC4zVMSOnJWTsDqBGOWc7d_eW7hljRFs5cT5bfGiHACrnr_TopnFrPJ5Pygs7XOo_yzgG556FRucLTucZClY5tBOiU1NmxTh1EL4pHvztjRIrhH-Pc2kl-YDtYSu0g6nj5lP9BgH4CPDWKRX2GM0w298HFXrFWYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZo8SaE5XPC6ov7xcOz1JN7PbHEKiuUonGP9ksYTl8zF1Hr3zmhJ4fCYS8n8Cer8M5eiMYBDo3tV6xgN5olMSAAZ6MT0gNvg7YYCjhCZbd6B8rtytyXvLS1HJnhjho--acwHO_FJvKMcKX9Bo0Zf_89Kj-0dSTWIMtAyo8mU3y1oJCq4oM3E84liVrq2DHESka3YD7i5BS791F0K_wTCua8FYEk8_WUjwNfOymX-aWjkmlQdNOoN63byKq6wHfDpx_KmQw93AaOeiVgLsdoReI8Crr2KYQ5SRTdXqmfwUtokkBljjkkXaeYQvioXLHHO8Vs897ZXAN_pHmlF61Jt1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=pATj3zf-SfkcI-Jd6HBp2ds6JI-LnDNLSuvEmJdKkqxRInr2KESIrHlRR3mWOXf2o7CIwBCzLJ5jMoQYUTLoBvRviuP3u6i95E1SWQ3-TPtZpxXi64lMikFAyD1tLRKOJS_h7JELnLlNdT2bIelKVFABmQG22kUfDQYosh8ngLml6HF7ayXcfU6Xw1pypHom5bt-YD2iVm90IKuPyYId6KLybI8nldaQop0vpA6cdd6WlhzOvX1huxPMgwermtiFat4Ig3ar9XUf1AFHfDrIejmUSX2cRuHzCxT6wmt42YLU0TF2u6OqGVuHROPdNpudnBz54yLAJoz6qkbMSGh_fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=pATj3zf-SfkcI-Jd6HBp2ds6JI-LnDNLSuvEmJdKkqxRInr2KESIrHlRR3mWOXf2o7CIwBCzLJ5jMoQYUTLoBvRviuP3u6i95E1SWQ3-TPtZpxXi64lMikFAyD1tLRKOJS_h7JELnLlNdT2bIelKVFABmQG22kUfDQYosh8ngLml6HF7ayXcfU6Xw1pypHom5bt-YD2iVm90IKuPyYId6KLybI8nldaQop0vpA6cdd6WlhzOvX1huxPMgwermtiFat4Ig3ar9XUf1AFHfDrIejmUSX2cRuHzCxT6wmt42YLU0TF2u6OqGVuHROPdNpudnBz54yLAJoz6qkbMSGh_fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=ZAoLIUAlHaoEEKdmfCVtmzg3BOgigW-7p-0i4P6pT7kjelfi8OLHWNPS2Ag7vrNExhZXxekhhFlBATaRqsk3_IT7c8cWPVVRlhXUos6wWdeRDI-Dsf_r-_ls-jJJXXqyn12Gr5OS-3rmcRV1HZT-_miyp2XSdr-GPMKSLzIbJPkUNocLUmKA5b13KKl0Hm44x-kRaDjYYecHFLzVB7bhCHcfLz-JrGZ8d5GWJUoLi00uqsrTjaO2JT23kuT4ThxeFPf7ffwDzrDtEAE5HlGkXX1rnEu9IRLVB47yUhYJ2LhRVxWgBmoGLgckMaN3dzovnqEQfQ4A0x_SYLW2WQr_4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=ZAoLIUAlHaoEEKdmfCVtmzg3BOgigW-7p-0i4P6pT7kjelfi8OLHWNPS2Ag7vrNExhZXxekhhFlBATaRqsk3_IT7c8cWPVVRlhXUos6wWdeRDI-Dsf_r-_ls-jJJXXqyn12Gr5OS-3rmcRV1HZT-_miyp2XSdr-GPMKSLzIbJPkUNocLUmKA5b13KKl0Hm44x-kRaDjYYecHFLzVB7bhCHcfLz-JrGZ8d5GWJUoLi00uqsrTjaO2JT23kuT4ThxeFPf7ffwDzrDtEAE5HlGkXX1rnEu9IRLVB47yUhYJ2LhRVxWgBmoGLgckMaN3dzovnqEQfQ4A0x_SYLW2WQr_4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHVlZpgU3M_5676Ui2nzNSJnbLML3CWBlVcYUsdLvpYmuW8e2Ql23_QhwphZeq17SSXpwEpMkxRXfcHQb6m_LsWKKeFU9X9tlEwggPxMC61MKdVLIIO5mgk4i2TuxmxOZyXUsQTrw6liW-9I_7pa8NEVkv0HphxvVDlvGVhL6UxXxz9sNUK3N2NqXBLXgfavexPbNVdqZcTKfFjzwmfwNuM4OTxX8VjXHQ0z16PP8MzZxLQLrhLdhK8vqNSgnBS2y6GKYTMJbcCdD5GM5xXZhrv_KQyAcCG_KFUdN5bkYpWe7MDSUC8iy8FTKXl_iR8a1lNCf2x9lDfe7rpySZSSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5iFowHoXyVC-D1ZNBqfERDz3iMxVKgT45JdHoSWZOFT82ejogFn6pQK_G8qCFOfCp6iVcAfKpe2xIsJ3KRiUP0n4-OrABpJ6LssfZOIghI3djWc3j41jzDd6re8pIx3JJ6uzExxdVo3GfuhsYOKDKxtPhBXP620zg2HnKOz7iIdI7Hl85EeJN6_JDkwzazZxhtJtWWaViRpwUZbc9vjEoQVD0cp-moHD-aFhDmAa89tYgnVWoy6Gdb-kMNRMWaqU9OhuL33nmhE9WcsjENLSE402yZzA1rE77Ybgk-rkGV4uxC2-T_4WM1OEoKOBvpIlhKTa7WfKkB7vQ3FVf5x1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDSLus2xp-U3-ICmXomVyUdXqwg7HIh3EJ1jyQ-be3-GantCjMGjIVBKt_lin1rB4GYHrQFJ1FcWbiRu-9KiOnWw03LhDk8yU7AFIdBEVVq3sp1tPGZWCwZZ1KOHoJNSpuCiasil-sN-biOq0cAv3uMy0oPcODLslbbNrupz6GEGRGPPPFU0NPM4l-yOdJ5qJ-7AjzrAA0sqMncoIXtB3jpyL4kT-YiTJMkhtaeriY7WEsfrUinpJXqVyZhDhuwVwh10fMnXMMdUu0rZv9bIqUUw8ei-mJa63AItzPy1On9uTVTrIfOb9DvtwvsKZnrYF_5TACrqmnByTCnOQm1-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmgjdv8rtkyMVlFWALQD2lXXWMG71SGovsaIyEttd6wju0HewWnvRIrrZXkjZg6lJ8aIZhj7ym_cEH-hlTUO-Fp5aiKWP-9GeTCSwjzA191LJa4WFRx7jFX8mwOXzmam_ga9nPb3ChEPIO7hWD2V5apPvme9t_QHguhSb0wIjJsx1xFY3s-qQqoRsPeTXC8JuZS-6A2pToPRlpkEWd28tkuEFD2zNVWsQ_XKMPxNYkEPyQbovsfvwrRMhnshZZSfv9hzp9NUProM-ruPh_q-0Cqo_acUB_0HGjUlJurVp1jRWix_cW47mHOpRSdW9qtT4NvqVRkaoaLbuu4QoqO4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLgPvvup_0aZPOw6NLmJ_hJPfV652am4gj2K8MT_-NKos2HzX_-bOctQNgvKKFul1xOktPKra7crAIbF6Z1Bp1Z7vB-pssUbplEN8u3RS-0OGY1irZesbUmU_AZu5MIkxKldyaeAbk7TW4agToLEUqJz864zpHWzfpwuuWl5oro6LPcy_QrZFjZgt9O9SdEzbQ75_BQfSRIMFhO_Ol27tAihGXGtKK8u-OY00T0H4Jq4r9HWxBq9Wl7XFCGlMV2dwnFTIdFys6OLhASdueTTOVdsndxn-1DJxSrkXgpIqB7Nx243x8tpV1aiCrxeAl4LZBgpG652u3J4flJD7eXR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfncE0Q51QIo0B7fsgKyRjQThMBI5jiGwMmNVbZW_0wP0G5Mxi5B60JAOlNQYDX8RxJIESkEUxfV_ObEx4J394Gb6FAStLP7nG0lRV_LDb2wQJgjJA1XA2xbLQ1i5IzjWxhkD1LcrM3EsjVv5EteDF8yjeo7tE-Qt4CSlS5GAUt-vpJuo9pGD6o_IzxqldGrkIx5bDF3-oP2affpEcPfuQO69CHu1WPydrvCEWl8vNSJv1OEB0aCOMyq8CPMzLvaqojYHlecQEePWyp1sUwlxJIFmhwwtOk2a4k74-Y2fczrB36lEqxy4orqS5pKWjBRyPqCilnQudUpvfZ1rjhjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9_BbMCS71ordgb641CA8-p1NNAZoUNd8q3aHBEBlLaYqhPUGN4xgQEAsssmzG71_XG6oxXyNF4mOBy5v5-fnGKyDLdM2bssrwXIJDzR6Yc_XVPqcg4l0rWbv37JAoaT7OV0D7xWowb2yxAwmpfZIlaIWb8KxlG9fHz-bccFqmAnZO2LnJq-sQxx7ICrkAUB5wa1qwN9Qr2EOBtiRNzSviD9WA78rsxlOo_21dsE1pK9NHU0caB36scSjktNErs-5n5FzuylXO6Pl31LI_PxjOlUseKmrA2WI5i9H-jUE9iPdjEQtsSc2hG62b9S4ZlxqS6UIYHOMZ30G9xSgBENNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=lyKDo4XiwWGLEb3onvSRdcEn3LbdMFkFvuaXbv5IK8O7cxm6Pmw5Afeqs6yyFsNwzwLuxaRAvMPa3qv8nwxsPF5SjGAf07arhNI8Fboc9oICwMGtZu7FALwV5SPJGQ5VbXOytuW0qd60oViOFb7d84vqhodVhGEMrxNSTP_sldIWAbK7KSCGN9HPoahlDvTnRGPdk0RDkR-lldDdwziG-WgqvV45b5U0M8iweJVPkSnUW8tbaQDrr21bqTECIo6o0x2A7ejSHwy3W1PHtqD79NBmH_ErAJBnn_sIcA25qYh5hSy1n_A3i_TqKUiotnoTjjXk2PYUVHFNrVFaafYNXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=lyKDo4XiwWGLEb3onvSRdcEn3LbdMFkFvuaXbv5IK8O7cxm6Pmw5Afeqs6yyFsNwzwLuxaRAvMPa3qv8nwxsPF5SjGAf07arhNI8Fboc9oICwMGtZu7FALwV5SPJGQ5VbXOytuW0qd60oViOFb7d84vqhodVhGEMrxNSTP_sldIWAbK7KSCGN9HPoahlDvTnRGPdk0RDkR-lldDdwziG-WgqvV45b5U0M8iweJVPkSnUW8tbaQDrr21bqTECIo6o0x2A7ejSHwy3W1PHtqD79NBmH_ErAJBnn_sIcA25qYh5hSy1n_A3i_TqKUiotnoTjjXk2PYUVHFNrVFaafYNXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twDruN2oqpP_WYbsl80RVO38bHGqnrQMBnNuhkLrLVMOk2FCaoBE6_Q4869JJPA_y84kiN_MHf8sk3c5UC8172c1GD4Gw54-Q_mT6gpqIcitBbUypA_WRvVf_UjhHBJCxM4kr7RKqUp0XuPYedqZoZ5YJIREMhWt27lG3_2pvCeWY2oJGKuLDqjGlswXuF23vKjFR8CXuc9iOkNZw2VGuNwJYA6V-WRUS0LtM5UgDCGaOlDgtXbubH84s2kKGhtsrcCH7PC4MeYDAKgf2-Bz7cnMqLi54uEaQsMpk7e69z5eqCgAzgXOiZQ_zLeHOue6_hUNhM6gEixrLDW6swCVzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhHFPu3t39dTSo3iHYDO0Og5JTICp3ZY6f8rZEgmX9sgeeNZv_tNgyzPlUhDsuFD-FVZpBK8f3mJYuuDX218P3Jp3IEDCjmFEMEC28IBgDyO12zhYCRukpWONWd9caA-c2P4Vd2c4MOFOlYlMau10QQAzM8WcNi9ejJPw2Tlr3Qn0ITSIp_HjDO2teyEMj-R10xTsB9jLBtuwuJgmSpGJ99hd1G7BMrJYr2RL7JstCSohXhbCT01Qs8sgScrMTP9BUDnhX_eVUs_sEDrkEsOvFyJQpy15K5scAbgwkCPYdzluOkm1kfscYcPmg9tvxcqn6uE1x47z_Q_vIf88xl7rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=XYM1oIprVo9---3Ib7Dk1WxQJlZ6wZgK5LYuvIlZ9JGoW3a1mnXlcDP7yW1rJDl1cSFHhuLnLxWGi1FWZls6FBpo7eMZAcKhBJWUR5Gzv6hu793BzEtrg6RTird4WkQYggJ7zXCqNeo2843yb6G-pKqbW5xTyc8VRz5qBsM7F6olz9bpxJBcymhd0Fqgi_L2_EWGQsi0kR-GKd61Q1T1Bfii-gi-Iya2A6PxAqf95rH0xsuYAeGPASMO6Y4y-cLsQSbIWblmaSA3T8Uu_CfLYPFy37aTggkqBUeLhncG2wPoEAhlGu0k8Nz2VERvVU5EI1hNQBsEZ_B7MUvCzeZoPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=XYM1oIprVo9---3Ib7Dk1WxQJlZ6wZgK5LYuvIlZ9JGoW3a1mnXlcDP7yW1rJDl1cSFHhuLnLxWGi1FWZls6FBpo7eMZAcKhBJWUR5Gzv6hu793BzEtrg6RTird4WkQYggJ7zXCqNeo2843yb6G-pKqbW5xTyc8VRz5qBsM7F6olz9bpxJBcymhd0Fqgi_L2_EWGQsi0kR-GKd61Q1T1Bfii-gi-Iya2A6PxAqf95rH0xsuYAeGPASMO6Y4y-cLsQSbIWblmaSA3T8Uu_CfLYPFy37aTggkqBUeLhncG2wPoEAhlGu0k8Nz2VERvVU5EI1hNQBsEZ_B7MUvCzeZoPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وداغ هادی‌حجازی‌فر سوپر استار سینما و تلویزیون به میثاقی مجری صداوسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=PTbEqf9DhMZFZE98GTUhCize9r7jmUeslOg1WGxzhl875VKf1CP03Hyb845_Dt153KaE0nUetDBIRUhOxz6y3YSrFjz8CEDvPiyMRbpC0KpeFRIOoqRfhVnOoerFrBCzQC1hWnASqedxU8x69rR0qJHbAxEuuG8iWKXhKUUo_9WhAt0JjE4dTHKsTX8yQFNHigpFEKishnCsKDKxHjZ6ZPIQmPXdWHmyxGyvvNg4a4K-TGNLu-m2WZLiUtvMGXq-Shbdf_rQhM5fXIehHfm_TxyL00URww_xyoB-sqAO-6LuX1rmXmvMZ4r6CsMkzX_7JWXiSUTmcjSI9Aikofnf2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=PTbEqf9DhMZFZE98GTUhCize9r7jmUeslOg1WGxzhl875VKf1CP03Hyb845_Dt153KaE0nUetDBIRUhOxz6y3YSrFjz8CEDvPiyMRbpC0KpeFRIOoqRfhVnOoerFrBCzQC1hWnASqedxU8x69rR0qJHbAxEuuG8iWKXhKUUo_9WhAt0JjE4dTHKsTX8yQFNHigpFEKishnCsKDKxHjZ6ZPIQmPXdWHmyxGyvvNg4a4K-TGNLu-m2WZLiUtvMGXq-Shbdf_rQhM5fXIehHfm_TxyL00URww_xyoB-sqAO-6LuX1rmXmvMZ4r6CsMkzX_7JWXiSUTmcjSI9Aikofnf2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqp0VAUYuEpYv7AuMoOw-s-y7uSVGMmI445Ib_9J4KXQHrjHRp1YN6E5XC0kFN7buiEBpywmz7cO6MdzuX7nxwgtSQxilVI9wGiLKJgFcOVhOhWlWEsgAUp-9E67EVanJDdd7na1R_HMxtzP0F85H8jshqJwZK5s4-gUwaFZfls3vZOSZPeBu8amcs6_nQ_1ksXMg0SH7-QUCfNuwxBi45agTdq2oErcZaPQZhSLlyxczVV77fNyOjf0msvisWQVjMWtdzQMv_zYsHfjzhF82TRPm9pIoPXb1XpZHE_tMq3lNaH-xLrZ-DmG_MBAyrWzPs9eN9JWbxlG7t7QiFCX0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSrUAIPbSucfRF3CBBQfiJA_HUQURHLtFnjSTwokvEIfJ2ZkWBjvrYXDXEJdGKEut6EtkfLtqlm1a8zrqbYYQnNCzLiE4TPLkLmB9P9d3ueq78wJXfp0taQ7izpH_2kSOoLmuSsVN2ZIiyuqCYfizT4b6ErWecJAWK_NGzJuNdf2n0sQKek8hDvoua3I8X0V6SlLLbBIToeNMW0f7vgHyCUmTpjnc-lqecQKlfRtHuLyoYa9MdzdT0PmLA_kONoF8e-EdHRp-I3QDdh6i7KnhQNIjzARDG0-MJeKfG6J_UW8BU87z7fr3dlPtPe94VD5I0MtAcY95wvVsnHNzQp72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFoiq1ZSY8yJvp2VmmhLmo91BKeQ8H9pKz0uJJZ9S3M9HiILmo13rB9WvuJTF7RiPQa3triGd3t3IJ1JXqL3poUgE7e62orVMbUikIm9m5CrfWfrIT9u3iZRb6fojnlDduri3hfENpjt3OOhwZWCgYK1X64EFGK9WyKqAiPqcEO1P0F2sfek-pbkltKILoSO3uoGJf22pZ_FqXgCgMNL1bSh8cy9Urad2yCDrouG45ggNFn0zALiLNmXDva6xpFt4sO1JO5F65UGY18L01k7ST6LG_vit_X13BiVYqjK6kfH5w9VVpHJM7up6Bjg00yln7-H6cQDstlU-0wG11girQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk5_JoIQ3Rn8NcJ7U9j34aIOAnUQvSWBrkdrQu76uI8aYmUvu0AZ1AHj73ia6tY3ePhpxZiaKcBoYE4HYly8CtR_834GC9bUZJA2_CFwldqNCgRGAOfCgxa6D7UanQA1KZ18Bra9ckpxpBHSm6hhFxyBwh0OxiOSw2oXtymagKkwppqMxVmx-kuAmAQV--RVx1w-Dbm1_EClg7E6_oVSGQO8TyH9-lcgAO5nvBj8NDrbuYsxcECxBZSiDoh7sjTJ0JpCZg9gxx-YclH4Dvc8pvxKNwROXMbxYIx5yX6GRyKhR7LvBDS-yU2lIKjwgSJQKIx6iXCJtPNrKS7E8uggLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW7Zw4nf_h9925bVZ5Ug25kPruoYLNt_7XaEC5HdSVGlxQK494FUhCGRzQqxGIAfu6jZo2ZR0pYpXy54v28_JdBEPIS_f2c6ESiGFVg1F2coUuPQJJw1U-Keq3W2Ika6iNjS5XtHK_6OgOLo42WE4ejA4Zt44tDTAAJ9ty4nwJ3oi4FXc_XYinPRzpPfqh7amafcErBT1F951Xef32g25YpcvMWqXu9d_bdQhlKzL-b9cwjiAyCgtpxYA0WItT2vF9XtO6okajg4o2iplUh8qwGDRHX2fCV_ZgxLEwlK8wl_ZwXyfzA0PanPisrWyeIiluDMz-cWKyuwAx7HV35Vhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=kjvQ6b1ss22SpTOjbPL1sG9_xJkK5XQ7BBEoaprnMGXEIR6AuDCsDWMBM4OGGdHn_PoYASHxow-ZVKE3vqoKD_nnVpArZJTGNBT8FPVhzdMr1B95UmIHSHHTPJt38dZHbJ7LQh52a5f9dbm5F2ADc_EP-I_LNW2jsKJj0E_aCKMfGj9q_TGy9A0VtKy94EkzC-5XVgMA5L-8DI0jTrcCI63NV4JisGuFyAzM8MJs5QtpSx7FIj6TwKw_arWSEsFBN_EqwTHd7BU15JAfS7Qci7ncXxhmeiix4CHPa9GJO9riDHWhv0u1mpP7tGVi-W7EP5hgj7m-vuEsuGl-Fnoc7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=kjvQ6b1ss22SpTOjbPL1sG9_xJkK5XQ7BBEoaprnMGXEIR6AuDCsDWMBM4OGGdHn_PoYASHxow-ZVKE3vqoKD_nnVpArZJTGNBT8FPVhzdMr1B95UmIHSHHTPJt38dZHbJ7LQh52a5f9dbm5F2ADc_EP-I_LNW2jsKJj0E_aCKMfGj9q_TGy9A0VtKy94EkzC-5XVgMA5L-8DI0jTrcCI63NV4JisGuFyAzM8MJs5QtpSx7FIj6TwKw_arWSEsFBN_EqwTHd7BU15JAfS7Qci7ncXxhmeiix4CHPa9GJO9riDHWhv0u1mpP7tGVi-W7EP5hgj7m-vuEsuGl-Fnoc7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛ شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8UQ4Ch0jpjh8klcFuBDNrRZa6CcH47CK0PRR2ULeGOwpEsP5wd2yd_HwUiL64dAPchf-VVrSoQ1gc0SHR8u_3BnGPs_CmDGb1tAKDbpa6KAUGM9IeXIHL6aGPXpIPLohX6RDbs_fdd0HzVq8nRxI3awkhScYBZtpQrc2R-n1sL831j7ciyZXgWSWaLU7XWibIxrLesWjmPSeY0SCA3zl-Qm2kAxFj8cfJDjyssoZC92Q_TY8RjDqhCh7dl53l_YRe7nCU0ONXHWzWLET7Gzzu3sVKU5qVqR-Ku7Obdt7oYXUm0Lk-vbk0KQY9m4NjszZDgoc3XW7_ioqnOu4lOdrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQpECb6zmjPNPN462iU0TaaiQuWjS69iU6S4Yf2Fy7skWxkv5gwGTZ_vQWqPtLvOeAjkgpX_1yXtmsH-r5qWzcEMGdJqoXKqlYnMu0MJTYUu7VXrDAp5aZsr8QFsEO995QdpIlAW01ryrIuJ1ze4fIyCmOgnkatve8qenLAcI6cqVEkS2T05Sg6qQMSzd2hJxkV8Z-cb08QLEgwT0nRn67uZ-9PdQbEPyJ1LlzKO7E7pUcpVurv69_pWOEs97LPAb681ghU0RVw4iiAuEgBnqgMcSs8TXJCBdFKLJp_sBRaqKuZOa6ZUJdn_GiY5nq2hf49Q-w7jazWin9mP79bwUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZpNE9BU3wOeJCt8bEC_psDMza6Lu9XFz3oFCZA4PnlauJDlkryr26nZ1eOmeUE7GWh0xByt-2Ha189_SH-9UFG2YFXpc9SUBPVWMrP8vSJLf92eoE30r_QBagbOqJ0XEgYEexJRcE0R50sWNfMRqPgG_uNbjws42XLmZujWnw_9U3w4HUPng8gONcVaBp6vw5R37MHb2d-wSFQSnnI594pbcqCZKdOE-8IcB7R5NFOSxg52vPPTPcAJn_sV8ve0xWlcYRroN11AGBg17QME3dhfGfa5s1JTwmmTPi-sJJUXqWaun4MlGyo4_gS4d9DcOddvQ_mZpUMIcEVT6Kh4Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knGp2Ms8SMnvHvYqG_VT_CTVcxC01EugFAzZbkPMf0fArMdtA9bo-uTLKlUBbNUTT5Pn3CVuWWvQr7b5ocZp4aLcHFO8xnTQstxWaUYOfeHREWlmjLED03L9Tqh6NLhcpXCQtg5wuF1hBEibmjmVl4pjSH8mE9HFP_WIz5OPfNRdju5aIu3W7hDtjJ3KPC1-2D15V-9ONH81WmJogySy6xUqmUJLZpYQdFj95wJWfYmdLrocESAJtE-CGWryh9m3D50c-2X9N6NM43ic45IoX7xbmAU9_xPW4SWrc0sJfyvyLbL2EZTypMmjYK0V25QT0gfyrHqwyC7kW7zwHPm6eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U87-Wl-Dog7-xPN65WjkAZsaRr5kB1LJ3aaNxFYdlU6zR_UreVH9luE8to9gBvupg0mXnMp9_hOJwjruOu567h5Gf9FNKK2fvnUaBtvUb1wPKweT1U1EuzFClOb52U9UKw5spK4Ood8TouANBU47R93BILXHGuX6iTIMI7kxlP5zjs_3J0u0msFxJAswCkuKpt4ZXwXrbUU8mJuO_C-LrJ2192_mq3XwciGbaw7F57GaLC4lPRqUkfLD-NMaLaXLspE4U8NdM562tPqPMsol1OmJgJIqbHhXzgCiS1ZXVVoHLZxZeQsFy4P93dr0ELiOT14DsW7RrDyn3ri0GaaL6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6HaXruze_q8tLIZn_I9-Q9Fghg3fJ73sRSHg8h7S3H9COgmhuMe7jot-e3Ul2q_CVMbRGOTKFR3aCjaTRIJrW_mxXloqAMLgjZuAXeKi_7BSFy53ZlIzw10MATdEe3pQ3ZpFHEe4xH709tmzoXzglL-OUplOZ1TCWLkhASmDxCkwaBygkroyQOvpHYXlxtrP6pEqy5zO5uH5bZ0WXo3k9QLfIbI7bvAI0LKs1YA9E74S6Nshh4Wxr1CPVkMTc5FXpkjJWi3e6fsb8QBnU35pZbzbzXPpKBdO62sDwC9oLWcCmnJSw20FM6yc99XfbhgyCEIm3paFXyLJeNG22Zxfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=lCPhd1PGkHx-rAP1Coh8oDJC3N2a5FLszOcsG9zzuhrR9Pj1ixtHCd1HqUNSXX9AbFYOfs3VSKQehJCOw-xeftjVB6GhCbGdDdSC2HdsMRcLvNzbBATFs9mwm_Xnw-dqKlWgP2yYB5WfDJTekEQCbOlhILVxm-3bD1_VtJR0ZC3CG_0vdffcT8t2cgltWD3B96tuSjHVJN1kuwVw6Ie0-U8l7XML52tI5Myrevb17rpRHR8pSrNmILV-1des8uJgTEhRx991cuENFZIA64ZCBpjibOUo3hYkhBq1ICV3e8RPzweYcYzPyhDD0_ZoVDGboFV-oJoQtHHrGbjjoLHZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=lCPhd1PGkHx-rAP1Coh8oDJC3N2a5FLszOcsG9zzuhrR9Pj1ixtHCd1HqUNSXX9AbFYOfs3VSKQehJCOw-xeftjVB6GhCbGdDdSC2HdsMRcLvNzbBATFs9mwm_Xnw-dqKlWgP2yYB5WfDJTekEQCbOlhILVxm-3bD1_VtJR0ZC3CG_0vdffcT8t2cgltWD3B96tuSjHVJN1kuwVw6Ie0-U8l7XML52tI5Myrevb17rpRHR8pSrNmILV-1des8uJgTEhRx991cuENFZIA64ZCBpjibOUo3hYkhBq1ICV3e8RPzweYcYzPyhDD0_ZoVDGboFV-oJoQtHHrGbjjoLHZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛
به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ni4MRoxW54syTYOkTh0BFclQIw4BFb67PK5Ur2tQn-sR9t2pQPKDF8NvSiyCR1ZocUXVkWfTEz4kuwR4A0Ph1Goa9LE75uMAGwaP-maASD4B1Vw1mq3wrNCvlWJwbz1017ljC_9NWJrW4e9n1RJBczX1NhWfLXFR8H4uwBtrubmwG7G-hb7CFx7LIopxKBxoydm-kkhcrWsehZMz15G2aWAjp7K7LHUGtnn95l52tqberGZiFuuanTD3CxsE5j4iL5p4VYMiFvmuexuoyf2J1Z5_OpGniWxju0P302eSsACOi1zbNRoC-9youm8O-Gb0YjVyn2lJxTE_FYWU0woVAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVtqcKmXXNNflLpj_Lw93WLs5rIHggqsNUdE-yLn65v01zeaV4rWEs4BTjlrGFLTwaAs3bSPc57HZct6IomCuZS_BOCT0kuf07NktG4gGn74H_dolyRvWVZMBzHNHAWm-EQw_4yquca8xidDA_jjSHB2h4Y1PycLXq-L0bophsaiokOXKZ3yZhaqs3yYBkSyJA6e2j8DHZzwvYmscxZVzqXY22oAbummcT1SGfVBRlF_-IyvZ_uVmbnAmnumHHSdMCgir9W_arIIn3t7qcDZFCWJQ-rAmFYYGCVuhFc4-7FNvtwYNVDypsdiqhmWoHUXO2_fpAPx-n-sbB5iEAJKxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzFUfsSGijV0WZxytBPY8QQuN5Cfpyia9S9z8N6OydsDdbVM_uwdvS0-kJr4umjXKouAnN8VyZmb57t63U26Sxc4EMSlV-whbaT6akWsSxRBdtYlUu0nZAPwR1b0QioMdbvTtjmkcTRom5U4SVYsORBRtdwSDbKq3mUNHK4o-JUda0bEvAZYObmUNLKg9rqKIRoyDWkZabtjos__MTgfJDb-3qSDz1LfobicyQgA498XGobwK2cAjG715eLzbUWfjRO-ec8qUkr1NjVx4fGTNv0qeEEi5OkoeYZvEy9p3qGbOE97mR72uk3o_qE4yAr2Tu_q6zs6W9D62dpKR62rxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm5jk57hpWx_Iphrdsl4nEqNs8J-vW7xbGK80u0cUzoKWp9QjHBDyaWyVh1VYTaLoaqhvOQ40_tlrFDbtle4Yz3wkZhBIprErnPCmGmjz4ZgKlnd9iYpDOMrLXXH-LEQOxkCCPZlwaDZLRHjNjuQiewA4JWkC9GqE9TLLZc6cDdZjT_Es6YE2yCOLO4dcKfm9JX3LkwJAM_52L8wF8_z5knJDAgPkx4csGWvov9mMwk2zsckx8ZuPkLXbgP7KGVSRYHX5ClHitthKdlkRbnvEgXBYHoTjXzS4-lWC8HWYwd7jR3aSHnnjcxXo_a3UCsWhtLrvdyGhtnHKWfeboN-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0dt6NC-xNtH_wNVDk4F4Eww8hPXqEi0UZM7cnTPfyjgmnE7i_lNov7ymGmv6HQNpqTWSE19OXXHympekXNoDcN_fxHyaGUSiQPgdXeJxQo3yOADTblWeFs_Bb1nziyqi4obnz3XjXLVn9bjoxK2VjCwAMEjGa5tu1P-JE0Rj_BVM2-eFQm7j5jkJMTqqGU6VNmOlw69AjR-Y92x-QorQivGvM2le7cv8CZL9WdpQrBJVOZkDesgy_sYgAqoD6E8rj3eoAQUeIk5ar44k3-LT8W2jSBwQJI0E7AvKcrYhoZr7iiP2IbPBBNdG7-xbkJsZm5IeV-YbDZ3kXWJIdkyXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJOQjx4ByxJsq8dTMMtPHZ8m0dUHSY1ZnEpEdI5gjjKgaf6gSTml1iQnEwpXQMVzPiB50VhM3sbGtW4rZYja5LytbbJOZcpCYljwhEnFEb60tumog0fOqJ0TBD85kpYYFlMCnGvriYv2GlRbucsFhPYnY5kdJqrdwjvZQGvuhbZXp3zd8xB4p4wuF8GE3Epr_DdgYWJ5Hz9YkIxzB-lAGIa_iknd8_53V1PNbhNIh7fpWtV7dYpsMiHAwzSWgCuE0Hp2KQVcYljlLhXqI39qQPNEf83TbQuwKx422EBj8Q0hP2lxg6j_CR0sEW2DecScHbJLDqPDhYPII2dpAixctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPEW4ewIO5rpW_WT4cZFvBFrrH-mIcYfSCnwWwEsCri1q12Blma-aycQCx3lTf6S7f3FB2P35vAI8tb2Go0o5z-dbIzwtcSO9YeEKoFWRqDxTBXsOnB855kVZB8NaxkAhSRClMm-i8y3uW31VD9akqy7bpwBH8ei96uqdwJU9l8Pwco9iIRMzSW7Kpx8iacg8htbtnsfyWGxGXlib0GLaO2Ln0gu-hwVeac9aF30cgGOyXWoeax-RQQ_wA-Qo8OoL1MMBtulGKxK8pAVqm4J-ptrwkIArG2D3_0oeM5bA9tpE0XafZw7JmPF1wx1mP-qf6j2VIoNbY51fwlWoVymDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FciE2kq4vvPGtcC-BhAxMf-Bb0e85B6CNAEFEmonXJ2fOaX84UeFfGRHyBpxsNQ_ULaAtfH-wrgPncbT8t9AbBYZy2FNX7hpV-YKTqKLjZ5LmmXQp-hYPAw-1uuFKyknDMpzbiAJc2v3B-uNLQZyq2R4H3rOZQeakLpP-fpMnMK8zgONjEiLmpd3N1sc-SuntAWMy81zL_SxSV2aNTfn0_AEB6kyWFKvrFMIw3wgg2tYlBDhOuR-4J_9m5qWHypCFWXWni_hGGYhP-qmJQqq51udkFrQ4vS5ggssO_OATC1prqA6215pKQBKNhXgTtfZdFMcC5Ga9LCiHvAzqnifJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEZYQX-RoQF4JckxE_cwLTe7STj6VMiK1ld5vBpjERaDGiNd_8wmoyUqUw5S4qsId7Cdl45M5FTrwxHyJ0u3hPbObISwB4xBkCE6vuh9tJUczkNlcKvbkfoZ3vqxHyu9CqycVBDlQLc3iC2R0WbsA6UY_5y93SVr2-KhzBqH51H9QEutW-rIihHd3CIABQTKY-h_an_GUfvyafj1oJ9yMS91jTASLqHRyXRuunWsh9RvT9r2lSmPt17PCXsYClbYjyZ5iDxvMQkN1u9IvnN9Rifv-xOJpqO1FUp6JlaCTvSjkMlXa98JgJnYfZfuLNrvg5I6E7gD76NjHZ4FexV0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=HBUL_dYsPwS_XLpmfTjK4cZv63gz1A5g4chEVLoQ4HtTlQ3MudvqUxBATy2LH3-DJPYXntt_xaggTWF-J3L1Zza-ZZMoPPJAQfMD_X24QvEK3Z0MYxqSY6T0MmGkm4GSPxY90wyAlhkYQosL1_9wnd7SfPYvzbmq_YL9qkTUYY2mkyAUHc5H0gxbn9bjGBlbWzwxFM3hJ9fslX6Hz_rrAIoQoGQO_aUgf1V5QkyTz5wwC035BkMOCV4hl6fq4LCMbnlKhiXhB2d02KGzNFbjnbYA5iR8S1JwNtqQTQDEI9-Wo4vPjVF3trKaHKGuwmIHiRGGWEY5PYtOCgbkXkQohw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=HBUL_dYsPwS_XLpmfTjK4cZv63gz1A5g4chEVLoQ4HtTlQ3MudvqUxBATy2LH3-DJPYXntt_xaggTWF-J3L1Zza-ZZMoPPJAQfMD_X24QvEK3Z0MYxqSY6T0MmGkm4GSPxY90wyAlhkYQosL1_9wnd7SfPYvzbmq_YL9qkTUYY2mkyAUHc5H0gxbn9bjGBlbWzwxFM3hJ9fslX6Hz_rrAIoQoGQO_aUgf1V5QkyTz5wwC035BkMOCV4hl6fq4LCMbnlKhiXhB2d02KGzNFbjnbYA5iR8S1JwNtqQTQDEI9-Wo4vPjVF3trKaHKGuwmIHiRGGWEY5PYtOCgbkXkQohw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
