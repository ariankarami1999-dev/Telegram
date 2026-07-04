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
<img src="https://cdn4.telesco.pe/file/JIQpRkqx9NoEyOi5Jl0u1L23smQd2f63yAJjQOI7E2VEAQlxNTBHbyTEAfO1_IqwReJGL1NMDUTkq1tMsllVgxZWCrXLglrNa-4cG9gN3A4H9OnlbGo1pIkcZTYbOMkELZmD_GUW0_yd6Tw2GpTfLJ18TvwOTo3H1J3ROlCEE7jY0CszWmQQHEHUTQcY3qDTNvJqgWPUpk6uqIY-0WtLSbYkpdMg3KQg6V9ACp3UWmS7Nt9RV7MNLHdqsdL1kdXnEeKlkIU2qOWA30MwM_fBlzokPHDaWpPz2inAolF060B_SqzudOn5XJRIxsEH8NNLBzBxmUiKzYtZvyqu_DdNUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 371K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 20:24:41</div>
<hr>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkBPWZnXHgd9-jsilGZNh56uW9gIDXnK0Bf7ZypaqY3mWhKAPyyMupLVaDGCNpGpqUCgN0mj145eLw6tCiIXYq0UPoQGc2AVRKgyy3lPJRDNpK1h6bqmw4XCTd_eD-1NCgSH_Y6D-eF02u1k2PzI67roup_USA6azr36E236QcqvArVbEaIhPuLkct0mRpKFR_XZFK_RHIz-HeUCTf8TkKfRAn0hXm9DbUfjwydYHBAZ8f1O-X5ICCJ_v31GlhhTM2664xnigyZjNYvTjk7pG7vvab-rGfr-75o9m4FV9BCUFeSV-j7F4u7j7cs711KZgnv_L3NhRyUL8trK9nf8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUHDU-qVb8ONRU4KmdpaLKx6G6Bqbl4KYgsq24ScWvjO5ocHBxpNP-VcFFB3OnKk-8SiLGEXFpCTHiIc8IniCg2LVLvLbxw0NDfRnywbrRJy1i1F0fIpvQF6MHFLI8zucHp1Ybjb3aIdfJgvKGITeDOeVOr-7mAaHnZHXUPepnuQ1Ex-rwqd2l9Ln8XJnPnMQD8yM0yx7dKNKnLAZwW36gdJ0TkxyYu8ijycxBjVBNKhsaQxXmvPNbrLeTN4gX3vW9C9UplPTt_EIqTD19axwAZtXtvyRhwXXo4c-u_gRvNNnQy9xf3VEesx6QMTNcl1ikeIgIpYO4B2lWZMsPYNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWMrdfcb4j5sFhsnPHManqwOArAgvtwVsL6-mmgbwx_wpGtBgFp_GvrXNjpZATOatMOb3DNGM5T8lNeoB4UPbwP28IkxQvzAe1HF4i87yJ39CRqZGSb_dRH9WvFx6DesL0cqh_Mwaga-eZQgfvTNfFibI2IFLFUCpgn5LW8CkAo8WYWzm7f55e9_kpWtp2uR11UfaxAV_ak20Z8b50sHPcS3XXwIFNedUTV0lRHZAi6vYLLdxtwuesvFZ3zYOaievtZVQFPI1ulY3frK2Vxgpar5MQpU-wizB1KoyY9TeBkxqSXkfJ7YP2G60NrWUwRbqTQnILK153Cr2lQL6yb9Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN75oZ5T0F-OObSMQgXqGLAWt-3jl1-egTT9c3egm252W8AAmyNXJZB-pXNam750UCfxXrLMuRcU-hZX-9OiWo-3w9DyJTjwrU0n3U_75-f3O2A59ThUIe_TKvLt-cSpMM_7YrZtj6CxXHd1pxCeltqK1hOk5p6oW__uOHFV_hgg3gMjAn8J185c_OqfoBYl7nhuGYYv3WJyP-VYlvU-5V7Tq5uWtERUXvdLOXWnEpKcssdzMSmV1iienWbc7Vpx6nBXAq0S2d_UpjywEMGcOkMbv-3zkxAZcKpWLy7dOjwC-ZzC1IQxfgUXrMBA-QC85DKzehuxEpWX-5-AALwqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-WmUmdg286_cJooLu7PatmI6avX0lonYjxr-_t_35Tn73TXZkuUjAnEMdrSPgIJtSUFI3-J2mC9bMWJu0odXhxqjbA9r8bXOUH-5h16aTggo80FpqzOV0WVALqlI5_H8fWaehGA8ERLLMhn1asit6qlXBb4iN4xFmok_wqfpnYcg2MloEOxpPXsJuhiI7BZguPE4iwZUsy66nWqZhBZJFCpT43GAk9Ik3_69xwx04sxbAjCx1SitM0QW58AdPtL0ini3FdZL23SA23rC-Kan5kROgSMu7khayRr84x2acn8usw0fi6oksEMtaLWsTMboLYoVDu9NdaHvNhPkQcZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSo3WN7yzIfck_C1kuwYcswms7lJre8YEFYlAXloPOBzC5zRG1iWxxGPCCcc9WlRiPFrJNCv9zIG5sLSVUShjPZEnJSEShoea6vtahK6_fRAdxKwTfsIWIhGD4NS4MP5sC1JbxEeKZIdccJ-tRuLF2JfC8P4P6_spc6XOxUJSsR6-Uv-pXuaULyLIdC6Whus7sGvPlNidqZ61809GnqaGCQNN0A7KVIfMbxUv2ctglDtXQia-yG-zr_hkZecfZCtHAyaB5itGos2hUmOVDT-uS2oicD6EfH2Cl9T1SFfoTIM_BOft0owechezM8yUixpapvgFBdYMFarNNq43VxZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPmU4iosfckwTQpg9MkMbA2IleHBvsPcDEs4LBbd-K3wOgq7NrINh6AKmThnW0hCzZdM4O-B6stXs__nx4mhcXRrUx7k3NVoVgBn2YryLrpjtahaEeb8eP1T56PbMN1R9XPeP56vNZ__80nonsZYHRVw5ooGUzK6934aE6bueqWbCPfy9rRTjgOQPv_bpkm_AMmmvt9DoHGqY9enxIW4nfYQ2zhkkD6VGnhQea8b5YThFkrMGFYVKT43jqx16aLtbf4oedDCOEvXv0NbGPH-zvxIDAH7ki5UYmGolj1Y91XBesA5JoqqkV5i2EN5deEAG53xGIOah1AdDDfC3derwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxRy2aWfiosgiC0Ea6pJaUOH1z1vddU0yNvUSPNTeWOh_gdiiYDdljrekMbcwWTYkAJUwwo5If1cDI47g8f5ZrWvuC3AaWfTAEtSsqqXqCMLfSsOA5lf57JRUeZmOhW9CM9Io8ZaETniH996dsGieyFw-AigWSil1bvln5TBgZqQhvKFHcDKwZoWOhbtWF_xwDMZIG0nQF8tbPILIvojJykLKn43kzNUrKgJkK8lok7I-4KxD1NVB5uUk6TQpF7O5oOPNnBTP7hBq7-PG4xPss5yldD5_VIix7Glq2mnYmZXmTmNZTvRcFyszLbs582Y03eayPIxKHc-CXrwu74CXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnS5x17foUZDgsOK8QlKiU0kEwb1zj0RrcOm7DjAqkklPzFoEtezHAf3ZcBzi99BxaR7fqf9lalMAJb_wyn1viCMJEAjCO2Dd8BTmeH6gK-e5NBDz_ajChmyL21rWj3-OECup69EoyTktbst3Yw_8Bsaregdqf6enwoQsjazi1uTNYOYc5rgT1LBIOJKeNp0moduFUTH0WKvfNI3v9CQF7LAdxN-a3h1wSKvMuDC9Rh6zlJvFYxFqXBTk53gpJ8URSDNvNoXC7qt12KYopiVJAKMdFhYCLZj5MFqUb6dbiWjqliX1RexEU6C0jHAtSg72J76i_3EFhIlBj71YiOlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOV1nlr54NAOeiHiaC1rdBwL8vhc8Mlx-ZEckWtqFgtQb9sBR0odf1KiehcaJcTNQol44b8FrutN0C5C3prHhhIU81-xjNf0E8HK0flWZY9r_iMI3zKNF3PbR1JJfz9MQOy13cdNNK-N7lgz6Zknuxj0Chyk5bi-YVxcGvxcopmkmusA30jHY6UZtZWZ3-au3_FAk3xGPwL5-Tkb81KhDxuRBrDnf9Ul3jebAf5Gbx_-6CW8S5NNBZnOuX3JG3GoAaaWHmDmwuVcs09gy1elCNd6q6daTgrf_iy6TiCYbS3ASrXhS86hpg_yBrv7JjBfNZC4-zIIp5UbkT9soDkjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/soDTPVQDBL0YK0UrQGf5wkj9l6xejYmKm4NwWh-r2dcJJwzAFH22u5ZYr8Ep7xjpRP9h9WvhobeMCywVqIaozu_BtHrsZxNkPJrCrW1bLZkLHN4aOWmFhftJLp92ewlu6RWP9i8gwYARTquXhFiChwyHgAl14eO_mv7yY0uyg10N4J1SEWF88to-fj9L36OeacT-XsXt0x3hdtLEbW2RKoAuFm1pWkghBbVGFRLL8-MVJIWlyUJkLSBnajeZKKh9_uNtP5sKqZ-BOgj1XpiRtaQ_IS8m60GaH3tccfFNQxxy5wOrM3hM4tAVI7CehsWEEPncKsxZ0fUNoZW-J29avw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKWbvH-L_IPHXs00HBdaXEc63PGQCd5UsILUmHLVdOQ2ZQO20msSx9LleoWRBLVWccMVKteRIJqpZjdkPCTYeWs_h7T318ZMLpRsIwAo9nJ1rpV1Tq5DD3j0L6IvYBjJBxhUVfCY6O-Ioc_Eda02ztCPlt6ZhgPl1uEX9sn4vU17zazZKyC_Xd5wq5DxAff_OoujgJHZi_O53MOZ24KkGUNratbJa34H-8hzHk9wEoXW-YcO3ovuTYCVhAGL7JFm3CNbrNTCI_HR5feia5i_EsZXKnzfESs6dcm-HUO09jAgX2ncO4TdfRTC66DmYzEgd12r8KtrAutZvWfOX5eXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq4VPisiGs5RR_qWpUj4O_lIEouZjKUGK0-Ax2MhzpIPek5kAE2sw6QhhVy7Hbn4KM-uXXwsWa-6AT9aNkUv9TkjYybp4wHPAisPx-8KQp4t3YbrB5wap9RZI_J7eRECpZlq4iY2PMF9EdjWJ-BYyyPCTuhdRbdmIsBRFHR68l3NBlFeRzBHjWEoTwg-YmLw9DEpsOtRS8Qcm1e4h5fzKVItM3VlBP86WOfpwnfMflfE4Psnvhc61Ez-iX0L1FFoAW8nUtF14tscPoRex34c3aILuDVZ5zni2h1qocTVE3fyCSXQFOkrsyWBI5TkxNKRV_X-qqGFWKQt89moan8VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOEVVMQFkJ3f8uIQddJWrOPR5TrL-vo23Aot9HcgqgJMjEOdlxccHIyfPFXFblvbIcn9APChLdQ4LGNBPgfIYiABgpSJ9F-h25eX27o3QAi83PpeYvZNoi9VPkV4KepK9BqsCVWXHMc8X3m7kaOOb7K-4uiJ_2LRZ4GIZtaJ0ozBv9cGySATi3Q1kUcSkPY2JqNkImMLx4ClH5PR-a8Azc7VQGmis6vDwOCX3u19tOaaF_O4sEKg8dZxd17B1fLknkP4wgPoXbokoK-jCPq013n2u3noMffxeQcO5_TjZPtvKSyDLaPXODNIv37nTTdg-2tGNCop7M00J5wyp2C8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejjR8KmeD9QxSDcg3D32hAmqATswLSytytuWZ02v9cF7EjcqTvYK-llg8ywl3TadooJGAAGi2-H_4dGGpCnIZ0JcfqiOkV9wex6_FBLeyqr2PDgZs-zgZgi2d-f7SF3qyh1Xf_rs-7b-Wy6jcfnVQ9o9eTfjW-MiKI0ivrMzmAe5hSxvQzV4eGLSK9MrcHBDqZ-gpZ07x8iYjplRhag12TBGbBF8hHmybN8hmbSwPXL7VF5AvHSdFG4dxpR96dQKwz5ooS1G9a20rqoaAUkjuGQhudPfmHAzHbl4nah3GCqJ4qyoZ2tt8LSl65GKlRUIwkdRVt69VC4qQWyDsGAMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ2AVPrtOvWGswWDe9bOlhrTywd97EmPNduteCgg7vW0Az7J15MQUq-f6MfyuagpIwgK9QHmnxDz9cJB_DGLwk10kdMp4JO4fWiJmP0q2XU-DmVrf9XIcof0EbXu6XZXC9jt5N9Znj8wug4AOBGVCOPwtBmup3fDZBovcu8xuOPpSplnUqnmyS0ApnAA_UFrEKz8U_rh_2ASpCE8JH_5RhcKMwTkcc0GWiHkbC44HwyB2zj8kN8JxibKHxE2FXj873FIhymxLru8WJvqs71KZg_8QaFOUxpacvUl49oOfxeN8I3GPFqUZzsSVjBcvphTX9eNpJ8rk8W8jP_BqEgk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRZmIF_azQyJHTdKoqBTG-MhOAH2x3Ip7_CiRc6rTmZsZqEXp3X5BufR8oQHlnVb1ObC0Ri2hCUtnicdUlvKONVeKvB2I8P3RphPgJe_DuM-qxpBVktuS6QoBFUCbxOQPaltvR9yOQFzizm4nM7cuDrTCOn3ESC_A_ZRNHIrAUOoFKv7jbAug1Skoghb4ZgrANsIaHgmCB_da7Rd7wZbZBr-v12GZBKVCy3MOvfzTZz76w_V83S7whPmrT3N2VcBvYu1NeE3ZAjOk9U9Mgi31fGcUNk7x3UvNJ610EC9_4Bpc4HevTBwX4qV6mB-8R4LXfGPs6DigV7Exp0G3HY5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BxdFMyNz1CDeKA1BM-MNw3G4vatX5PolSQyDmbLAByHmQXWg-pIgjbwof2571l-b1MDTtM7_6snbz3FOWZtnLy-835eqS69sIx8MLCAt7CISOuKPwy_XGHjQE5uu93R_ypjOg5rqlOeYRtreX0mPZWLSb86RFZkyspVXpCmW05skWdM2npcZhsPRTJriArFjwvbhe29Jsy-3zkIZWMepBcoCosgI_1oUAnhzEe-6Qpta1B9ACXdzGDFnVL-X_uvHZkfpGjD2Hw472aTIXvoHJtzUdoK3iDvTE_85ElJW3B993O3m4UAA_8Fy1Rvhmdbr3SUc_lcudza8c_wxRLUp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KtLBInV4F-JrTNqKc1KODLiOE-Yf6erWUjR-u2Fn_x61TFksSpxujX2r2eY-iQ3BIoCrqw3nJO8W8SCDhL7Uq2kcgJtvAxsw6s6Iff6nkRcCYuxRAMfGemybhNe9FjQaDqYWbbTLYxGgs7wlc5pko9kxAh3askt-3xPSh2zcRpIIG6si6EAwBxGviTmC24St9WRAkfVE7WZ7wR3JMfTNd8otJppPZ3RLx2sWrtFOlzidTxXk93PEHW8mNv-yc0wOZKZ5o4JSujxh8MZEE9viNpnqCbNkz4nL6GNndcLkQ91q4vB-olRkZ9o4jmUrH08uCa11y4OqIgVMJfpt4J7v4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=JaVGH0aw7Nk4jRMoXyGkO0D-pNEhSu3CLbWEh9j3xr4YjE_3nrwTRx4M_qC1BmcQdMo4lwVcUA4P85C8S963sFCaHL-qblolHgpEZpBQ1sU_i1Z6jhvptEtQZbyfweIvQkgpiLwM7NArAyMCfGukASdotLZ4DfIzoVdWzAfwzbWyn_hMHxhGoSGG3dJH-1JgNRBexl-tc3yQqzk3-KgTUCr77DGmR8vda7htCuewMqmfnwOVph33gJlauyHeJF-mPNSsanQaRJzhwuSXuwEclSfQ62oCa_O1BKTDicsNcpXji_K678P8EmDJW-DabKrk1IuEDqU3qfT2GLcsiGbf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=JaVGH0aw7Nk4jRMoXyGkO0D-pNEhSu3CLbWEh9j3xr4YjE_3nrwTRx4M_qC1BmcQdMo4lwVcUA4P85C8S963sFCaHL-qblolHgpEZpBQ1sU_i1Z6jhvptEtQZbyfweIvQkgpiLwM7NArAyMCfGukASdotLZ4DfIzoVdWzAfwzbWyn_hMHxhGoSGG3dJH-1JgNRBexl-tc3yQqzk3-KgTUCr77DGmR8vda7htCuewMqmfnwOVph33gJlauyHeJF-mPNSsanQaRJzhwuSXuwEclSfQ62oCa_O1BKTDicsNcpXji_K678P8EmDJW-DabKrk1IuEDqU3qfT2GLcsiGbf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbkK_1IUJkf1_veiWDw0kO7cfFYJov25sN30tPC79y2Xdot0KEvBnJGq_O4QaTgP1DEUef-Nldo2HqUKh20wbDR9aEcTBVVImknjDSTL82abrRG0mzO2OUAm31CB-lEKspo1pQug4uLrmPF3c-w83cXDtG9lM0Yq4MN1MqyUldd-9X2y7wcHWWoBtO9YiMCIInIF1QbFR5G4bl1qQO1hLTny9sbJy9B9JGi8b-hjKyiiMitoBXIQhJ2KCpq1KoMWyuSdQ-wZlyhI-D8v6hMihELnV09laP8LPZTfvX87f7jKAbyouiUxBsNHbwN38sxLG89fa5cmpiinm_mmR40Ruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcMrsEwVAIcmhPGJCCyUgfItrU8Me4PzuWdKu2aKhN4mjMUK6ojJKi3En9vgDr0pemuU4AoQOOXSg3tQweu2MJzahpXvUh4BjtOmqn5WReMaDNyOaZDaUf8qe7NJcbmsBaK4UQWnQsulyV6PLpgs1bCOUi9_xUsNgeu19InUoj9yIOwQfKx5AFIMYbipvObv4xDLK2ynO1J45QSioiuUeZQ3iTGJVrwD4P1xZEd4eKnEEZOu9-sZ2stffAcEBa4tQlPBlMHISpqM19pOmLx2kyrhp2-8TeuNqcaunduPmJM-aghqq4FadnM-Ja6AVvyh12k8DDxSGT6g9Y6-QBPL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHC5-rsS28BYvXNHyrj5CfgwE1JhGcLUve2zcS5R_i9va8EfquBijFh8gCFL2azAkHSK7s7uVmt4pRtNiExRaQ5ym2cLcVHN6k41cooPqVualk6Jris_eWDBNbaPpAMrI5WFBOiykaSc_qXGHBYRDRwFUF9Pvzr0BvgCeuc6glWy6OWjiX2tTMcMDntL6pDndzgWmRcrp76FWS3O8aJi5pcDOTTVOmZQ5b_MwyXH8mANx7ePs_wK-fCfHdIMcUFW1Q1thKnBDOtad2RwlBCueKyG25-kXQE3EwbdEwMKkecEl9cDqCGuj_hSmmD7RJNcakrpbvDX3ukXImdPqXlr9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9iX4uImYElAtMpBXvWtkQce3Tb5fQ6S97I_7rbmdrUQPzYrzy5MqchlkvtRkHJYPz2cXNh0z2zeNaBond1jnSw4yPFrMJK7u5r8EIuyyYxRq-1-WzVzKxsgxH0xGFRa-9HaPa8rxtSpw4Mm3DdzPl1QjdwLg1zI5PkIoGGp64cFlVSxZLNnbL1VonY4XblHBkOEyNsm7JJoHzKXlI5xN5lDFcpCara_iTupsbx4SXWIDGTohZVGfeY0Z75xxHgvmGsqQmGu68XSafEqv4WBQFBAOJ-YdfKiywtqpcexZLM2Mq-hxmPFwiZzyKJhcE0uYltSDm3rOHRVPa5wD9ZWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnMbWQ5dOheQdK-PMPrFEbY1u8_DVYX2OXA4bKAIcz1BidkvO_5Jwm0MPEqoVgtHj7BYz_OuSskI0v7Uhf6RNJtPsIwsdwZ19XnXlD_WfKFVtI9fhwNSnIBD82pI1YYdAt3yretsUKzp3RE68rJgRR9WyM0KmpLRMTgQwGG1cnyd757iaObY54g7R9fJLByHAyRx7iwEPSIxgc9-30vBLOPEos-3U0uTZq1bqMoH69MvG_8oJdOC5lfhlIBMmlm4gAKKlblJmXhuLTVsKcAuejr0TGrz8vO5MkSDaer63bBswQ8_zomdlMHZEMQqznZ2wP0jYd25-38aJUGVAf1MqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=TBa47sA42usHrf8_6OBGNDZyA9w42aD_WrWvQi9CHdrHjjlY1m971ZMVeqB3u2Yc522PGjK8Rt_Rzp-uZfclLN6OLgFU51m-1VxeXL89Vp_k1MZpWmzC--7yluGapHLpeePckE2tu9jN9qO0y1WyAXOJBk4Clbjn3VZUHa5pjcbey0nfWCTRxfxKa0gEqJerwKc5g5UU8LbXr7FCdRqY9w4YNJv1tU4A45dOXVtZbmYOadWWguGaw5rn3hvgKcZ-LLnHv2nYANsjC3F2Rnadveb7GxFiCNM8CdRqaxJk97pBJeypbFJBuQ-cl9gv7El0BlmpCgjM6a6O_iTu9UazkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=TBa47sA42usHrf8_6OBGNDZyA9w42aD_WrWvQi9CHdrHjjlY1m971ZMVeqB3u2Yc522PGjK8Rt_Rzp-uZfclLN6OLgFU51m-1VxeXL89Vp_k1MZpWmzC--7yluGapHLpeePckE2tu9jN9qO0y1WyAXOJBk4Clbjn3VZUHa5pjcbey0nfWCTRxfxKa0gEqJerwKc5g5UU8LbXr7FCdRqY9w4YNJv1tU4A45dOXVtZbmYOadWWguGaw5rn3hvgKcZ-LLnHv2nYANsjC3F2Rnadveb7GxFiCNM8CdRqaxJk97pBJeypbFJBuQ-cl9gv7El0BlmpCgjM6a6O_iTu9UazkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=nAB045fmFjzlWN8OxrtP1Q4_fEHhwChZ6HaPcAWrbckS-k8QAK6-NGtTHCuFm8GLJbD1R6JMpzwREjnvu3c-WdOHDDUGEkPxkDAvdw4lNzgIbeQv6gudtG1P_ycc7DzrKuYG-J_K8z_ThY1NHzzHUp3kRpFZ9nxNAtpzHEOp3fZ9riuSo2LGzfheDZaHiJTXAIsNAgcEqIPKQ9LoaZqSuEBxx6S6u1l4I9qHrLz6uG3TE1YioA0meYWlMZq_tMKOLEzTQ9oOxYeBvcv8c98gqLL4Sa8K0Gc0TrRRHdpMD3X5jqqYNPUlIgKHaKh3Jnuf0U1Uyyxz9th_KeI5xvklTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=nAB045fmFjzlWN8OxrtP1Q4_fEHhwChZ6HaPcAWrbckS-k8QAK6-NGtTHCuFm8GLJbD1R6JMpzwREjnvu3c-WdOHDDUGEkPxkDAvdw4lNzgIbeQv6gudtG1P_ycc7DzrKuYG-J_K8z_ThY1NHzzHUp3kRpFZ9nxNAtpzHEOp3fZ9riuSo2LGzfheDZaHiJTXAIsNAgcEqIPKQ9LoaZqSuEBxx6S6u1l4I9qHrLz6uG3TE1YioA0meYWlMZq_tMKOLEzTQ9oOxYeBvcv8c98gqLL4Sa8K0Gc0TrRRHdpMD3X5jqqYNPUlIgKHaKh3Jnuf0U1Uyyxz9th_KeI5xvklTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNAtg3kUJRg6Scns30mR-KzdAZuCc_WV7zVziw-Ki97Yb8QwUyv4ksmmiXa2T3wTnVIz7AhdBCIWlbfeIdaBOo9v4sPL7L_4D7_04k7kMqeMtQzy32u9vH-5uNtDmIEB3nlkhUH2mEwrMUGBK9fvD6DEraI86HOJuhowi1-UmvR6J2ladfvx9x-2SjYj0qVKEd4nIbXNSClB24hKKBg2iCG2CZ7domxsEON7tLkX95cTwnuw_YKWOWyKHXaILkvQgRzNG-V7TQq-ph82zdOqPxwi9V8rQRb7RSbq-jcXX45Q6DC4zcB7L94y2oI2skrYqFjhG-o1oPAXEK8HIecnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/but2wGEVpTys3ug7hC90Du-HvBWm3Sg3IllQBRQMq4YGn0TWMIJddoGQl1Dd_jyUUO8XuiAJ54FmIjsu0lEVbAzzO6D9M5cnay0jpEiHQSIYTw2RFVoJ9qeGdqEE7l_E-56KLVh_mIxxRcSpUB3Q8rHlZRJZdjboBEqUmOTv9Q-BSyFOrtuKpVAb-ft8s1PKBiiOvWS5IfQxsXo56E3V32xLwDDIrh9Mo7N8IkZZFAFjNJE6tJgBcNd8i4Zq7pq3AcggJA3fx1F61Xo9oY7Sr5_m4GfRnNf9iM-OfrOOniDl1E3YYZU-DKmNnjJ-5PhKzbukqMMo4BZaR-Xls0IROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZaeFnLyqMB3Eb2M-VlIJ-53PDLAKCGtgHrgooc2n9dEW9Z1HAQkdHUVkNhhclaJlDBJ7kAb2f1zCHp5z2TLVI50TSEFR8ZOQPmJB9bPHcePj9CattOri_o9IcJfoOWVM4g9uWGCMNfKY8gplruvlB7DdgnoIs-f0tZllaqZvqM6DvzlwxqJbsYWp0U9NjiNvAE2Nd6WY0HcQscm26pjmZFYMTxEla37ABsfherhiVqzSrY2k9yktNErNj5qqSuoThxv0KYxH02Ai0T8rWUSHdNA66d660Ftkv_oJ4B0XEnSp7ub6yOqc0lVENI0vdzbUEfBDMaNBeWtKy08rwEELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24924">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/24924" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24924" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24923">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S5_fdzg8sthhi5SHHVEh9unntbU9Gh3l8oey38ziUruWKzM5OXHoowcR_lTyZr711UfYLNvx4cegGPYkcerl9gEaJPNTb8uzdYzNvXPJ39q4pWjc1PKv7Ti8ki1irsm1wWCbfumdhvgj0-2M4js_vKS_P5GBB5g5sjL5bp67G6QrT5XP-x7ZXpeqjCd4gZmDkBkMcpAX5Lea0asJ1w9fIpVNMfen2CS7GGuya0UvWROFFJL6EYNvcc3vbZHf4XNodiSS5E3gJaGBVRzGlQlBXF4_aJfw8i8bVau2XzTLkDgJFMAKjKboBV8IZ6LFclQkEPWKKgqPuwADnb2nwru0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24923" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYYoBwytKJrYxAbDLoPq-7bIl1mXj0bcpIXK7_0g-RJSLb0wPiYGS-b94EDR8PhF7a0I4VtbjvMw3URhJxUbqm-pmMboECa4TPRWbIvcyhZUlaTRi2GR2_eZzMS6kzwS9ivH2l63meDK-1qlF2_A1Ott2itwv9cUm9Gl-XqCrFzV9tssjxvqo_1V1PJEWLSM51Y0tKJ7i7z4pDnroaQT0wpbthtQk3Kn7O928O_706IzrsglGQAM_83wXbKOxm9gOQIUIYfGnpqCVUQhqMXMMKN5M8BKuyvC0qTIvPfehXw4Fg4iMvoqZajDmbFHrlWPL24nQNFknpkrrkgGNEEgxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFyaUQveVZloUrBpZg-Z7w72MdLvYgctZT84J7MKP0jarrZlACsKxxTjMUicIl3a5FkG7bXxc3gA1tsmP9-oUksuyaz2fKWRr9gdQHwcZL9JSSBQgn77zj9pvaymGmR6nF0QmaJkSEE9KuZtMuwV6DV-drLOirmVrgGsc7d2b6Ir-uTGOuCLJfRvY083r01JxlG6XVmAbTf5W2urPbV6d0iKsUKMGVbrxeFsbGEVv2Lp98OeqrPt7lRPe3H1rtEco-yKIe0Hfm1XI3gcCc3zwvR2vnUClWuXkNd4cZIZytAD0OolBV9wOp3F72LvhkOpw9OYg4fMmpASVDV5VUisjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0R7_Ci7imJFvwzZ3A9-bSdr6B63g9p4bStSSkHj3KB4LCTFh_AOMvdtgwwVkkepLc8mUojPKrz1USoMBeHS91GVn6tPxW_yZ4FNdxbEnKNtz6rHoTRaZYHEpPNUbVXKV55xZpDcnONe_fko3JAbQG5FQBqp0IvdGm43Qu0J_yXn3hLHciipBecsB1hauk67bfGa084Evv7k8yaXtTjxQwhsrcrLj63Pz6iyakQgX131IB3muAl36CAJms2AOI9C--Bis7W0HE1io-rhAmd_w1G9sxHnlm2HEQEV47WdfClCMQhZzv_t3gumTqs4IR3HjagP2rHoThTk_1VZesIDOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL1OS7ZTkl-ElRrAdfvbadmVGR0ZNUvYLbuTlmAv2zzXB0YG_KZ6K_siAKn6btsR9UdFEZOE_Ea6t0UpYYm79Sw3bVwdv8cqMd7Wb2blI_CnWvcgXmpBmbzBr_988Jl-69zyASeUfyy6Hu8p4OtUuGk9RPqRlx4wcgBIzOFRFGPswWCRo20KHZuf5z2FGlQRB6vtObvC3h5NzLW6OioHbDW5wfa_1vZvOUVAQnW0TpUfTz-3GTS8ugC19hoND-Z1qvGok_6jLU8vrFRic-s0NP8NfIeQ5xjmKxvvWg-Cm0RRejFqEB6goSbU2oO46dHVw0ufEfcX_UOLfuJtAldeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=I3QNqkzv5e7ZDcQoxUqerYc1XOyz-huXr-r1Py6I2DarKML80hQ5QtU3fyaJndB77KUk97K_sfNOKC-nZlBWqDtjYs8h-bQIki2RXhV9SxEBK38bGt6F-7c927yQfh1ZCwPClx3USUCHGxMdfJ21QNaU5U8xGhf3IR154CVlX-a5o1tq7eKVQ5pAfD_qIvRhgyD8ZGJEwPd1TayUnWxs6_Rt0tNXmR4tPHW-t_uF6wwQt5L7h-1QobKQBFbimcJcKm1ItJVW2sqftETMkwqRWcOn4bwHGNvzQqzhOsE5l4EDLpmExqvtGxY5EFFKXhiHEbXz0FSpefpzSEHM_EwUUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=I3QNqkzv5e7ZDcQoxUqerYc1XOyz-huXr-r1Py6I2DarKML80hQ5QtU3fyaJndB77KUk97K_sfNOKC-nZlBWqDtjYs8h-bQIki2RXhV9SxEBK38bGt6F-7c927yQfh1ZCwPClx3USUCHGxMdfJ21QNaU5U8xGhf3IR154CVlX-a5o1tq7eKVQ5pAfD_qIvRhgyD8ZGJEwPd1TayUnWxs6_Rt0tNXmR4tPHW-t_uF6wwQt5L7h-1QobKQBFbimcJcKm1ItJVW2sqftETMkwqRWcOn4bwHGNvzQqzhOsE5l4EDLpmExqvtGxY5EFFKXhiHEbXz0FSpefpzSEHM_EwUUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3NZRm5eyRslINHkopFek0rx9W8nRLzJN7S79rtiMHOSP_S_UgsmNV73AAqr1rc8_bcCK8FvUPoJhGz5Chp9CqxLS3Cfi31JUMS4MJFwYPl0_38pwbrGoMK4n6eJWOfplx72C7n98E6cPUnbC-_D0PRujDNV9eNv0C8dd2it13Kb8gJJQa9GrXX62X_zkr5wwWf0-BnE5rPk6JSUXI7wSRtqNdYBcViUsxw60ztScLU28zCpIfT_0UQEgXESmx53R5RMj7fd1nzkmkKYVVl79ELdXxYDLjud_DW2pTrH-mOHtCimX0SqQWT_GaNNQ-MAWrKEt4AShLw-bektTIfptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZxzW415wP4AawZ5ardZEXWepVyb4dnfATLy9J8XKHe6Zzl52_AoolR6LbLww46zq563lbDd_1DBgh52hQn3K5EeU1wGnuPqNmW1KelX7LpW99a69Qq3adRmhuQZI6qfPxSPkk5Fez105jIkkPdopcD1mb090QF0em6ZsAdelyw-RUJIHcmWQAvTucf26rdMCvIKOh5QsWrrmJNLFu4fZeOC3wNPL5Mr8IHIY3999ylsmeL6mWddBOMZEYnPVGVU4HEBKluVcfpqwmIhRtxWCSNcepvXngjCTLHgsXI7eQ5wY2Dl419Z84MV1SKkQgGM-u1nt237HUNTJGXfZxIpjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=mT5OA1xbHk48ieDHJ4PGRgNMaIqk3nQsiV4cPytm5EshUdr8cyfMijj04QIwdQMG--3y1ogX_0aGZHqYLis_lWeY2GibP0xkXtciay1zjDpQ9i3OJnKgOlqpZaWeJJapXwnV3pU9_b98n9v0KozgiXyrvNWyV0HhSHeWBJh-ARGb8Lz3vrG80u4s7d6myaMtwOGBkmOQgXkb9DaQe4wqAb6AwmOdTAx_qLA_vVJ0m1Vdyy9N5BuwvC8qjwp82SDkkVm1tVitBT20vDNfof3R0kCpa-eE4ZuyC8NNpvwF65EwpZtM7gUTalELiobdBxBGvk5vIqs8pXVqlTl692kiug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=mT5OA1xbHk48ieDHJ4PGRgNMaIqk3nQsiV4cPytm5EshUdr8cyfMijj04QIwdQMG--3y1ogX_0aGZHqYLis_lWeY2GibP0xkXtciay1zjDpQ9i3OJnKgOlqpZaWeJJapXwnV3pU9_b98n9v0KozgiXyrvNWyV0HhSHeWBJh-ARGb8Lz3vrG80u4s7d6myaMtwOGBkmOQgXkb9DaQe4wqAb6AwmOdTAx_qLA_vVJ0m1Vdyy9N5BuwvC8qjwp82SDkkVm1tVitBT20vDNfof3R0kCpa-eE4ZuyC8NNpvwF65EwpZtM7gUTalELiobdBxBGvk5vIqs8pXVqlTl692kiug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وداغ هادی‌حجازی‌فر سوپر استار سینما و تلویزیون به میثاقی مجری صداوسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=lbmjMeGjPoDSRdgN-mmOGlojID3bACwOn-FE3Cekj76FUhiMK3waVO01afilF7SYK-j0G7iR9-tRw7kobmJBrMFVQJr8zGkar8Ga7k4vT0i053UhalTHSGjpcI6YReiZVbyzj50b2xKBKFpmyfKoe-b0z7_AMt-LcLcsYak0IlrpZn1IzHh9Up9BF_7sLP5V2LU0LI6QQZJClAb3c9WSfd-IUE8XPWA1LutCt3gkgRo32kbZwz1NWN0-2Ga2jTsLLgaEG6c3D8ybdH36Xr9mq88UkHfNVS6zFdMuqqS86A4bzWL6eEWAzgPRQe4Tu1ahKivJI2FG8FtlbjjKw-dhTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=lbmjMeGjPoDSRdgN-mmOGlojID3bACwOn-FE3Cekj76FUhiMK3waVO01afilF7SYK-j0G7iR9-tRw7kobmJBrMFVQJr8zGkar8Ga7k4vT0i053UhalTHSGjpcI6YReiZVbyzj50b2xKBKFpmyfKoe-b0z7_AMt-LcLcsYak0IlrpZn1IzHh9Up9BF_7sLP5V2LU0LI6QQZJClAb3c9WSfd-IUE8XPWA1LutCt3gkgRo32kbZwz1NWN0-2Ga2jTsLLgaEG6c3D8ybdH36Xr9mq88UkHfNVS6zFdMuqqS86A4bzWL6eEWAzgPRQe4Tu1ahKivJI2FG8FtlbjjKw-dhTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLQX1veGt-u2q6kzrvfJlgEPgT29zC8tvH7hqCcj00-T6swX7GIb3IilQzjQHGuMQzxKQpzfhhDbp95kmmMhMGDX9tpMTSzU92BzY0TftfC2ifWuF8DghIfFLyGQWbhFSjaRbyeqfJXqSZ09xb1pEtJ1GqJmq8N-ymdyeo6Ns9kXxoFIf29J81ZAqN2jD3L2mHZjhpLa4IEE2G96gY1zFdWdvCIYzCFVpC4xd0bd1s1so2dS58-F0IKgBz_0GLlTIRsXURKMNzP1SgojzNcZmg9VzWWwR6CQrWWAYSEq_XPup2i5NrXK0Y2mz4RXt5uUU5GzgaBytqRGi-5cW2-Y2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7arZxU0367crw8tpfsjlbju6i9mozeW0zJ0nCVh48El8Sg4MeUIsqvo4hQgwgdOg6DvsaRjedMK5VbC35AD7DZfP51EHVsxkTUzTCfojfv7mjMHuMzY2AS6k4WUoCdI7Pw4IL6szTeXZeIHMEFJiZfF-MsbwZiqgbQDEnnG5CZuGDk712xG1EuCMocsAmu7tmr4iBH4bTi5Y7AnO2i2Hlcu38ox220xkrHIbYDGHac76YfUEe3HsdVb4d4-9ex8NEfhJB1yh8o_Bad_4XhxCx9rIWJg44xmJ_eTjVuVj9_cUksWLzUTyldYbsrSfoqZUd3iA2nBDLyWhVwvjB6-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iml781wG7UsUxiSFzC0fLY5XDvdBpM-2VBJK6b1u67RozUcJlmrOQaMB45w2rUBJIShciHvwpyGR1yu8Pyy5z0YMfC4KIJyRSxXoU7riPk0_EvStf-aU7iiGrDQLGol7U03Dknrn15UYIZGUT1pwTLvwCrFFLddSOBhcRS6NNDO7GPJeFMxm_P1cuKwEM3mrsWEN23KW6yjthExVwCupqPd43luYu-1s_BYlpkIYRplAjvlLoTlLS9j07vd07oQVF8aFpDI0xnWErAIFjVSXiYbtzFDqKCqQSPLYWXGTuY6ujjMqGQxfIKaKNp4MOpfCHCjl9tz5rZRJzwLcKfmcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNNiV0syklUfD3x0sSxqLxg-c1-gA4baB0aCCEtH48I4G8HwSa36rBXvU9aIczcYzgREqvFa1WbvvzM0LNRLxBt0A_Pz8NMYnC8_QU1VHid8aj_-0lR9YVQ2YESsnegblBlnXwcX-0atG9XWloaoi8YZetmbsa1ptJ-qUyFaejdk6nl6qdSwlEFsEl4NbMAbn3EAtvgDfu6LMtFKwEMeVFvd0wTeGD3pulYx8XfwLbbhaCMybBuhvswtxQPyJ6-E6wqDX0LtFpDO8I3Juz2XtvVsdV5L7iBIhQ_qZJQoQ-SRy7NHQoe0eEmoXQhubSfD3GOQTVebqxWEemVgtioUng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVx-xG0bHnz5MbCJhckmmiM5ctdK5y7fuUvtyDNwDaJGwFxfiTv0_MTi4fgr-pDcWdkaZw1HO5kGO0nyt5P2TSTba-M7xhEDXMWbfMr-bFjb4kh_RUJbNEDXrBh0_5UNU4QIoDIahkrSgxBhVAvuiA-fbwMBoASQnPUvYOJ8BBqlx-SrWDbDitaGhh8mwbwogNMLjHMUNkUkWDBojZ6MRxu8UcROPPtrPzeEkUbFeaMh8grk2ns9vOELFhdWEqfpw4fLsaaNoGoOQLYCDQ_hBMc39tEJgdoH2qqe5lLUnsSCGNrGqPuUuIocu_itdLkJlNiyqTtw4RMSZ62wjGWx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=QaWpFb3iyKEgLSn3y0ULIYZNX5TxltETFTTjSw_sZUYIgR4483XlvZF0bQT3bUAYXjLqwJvnkzybAhj46WRyPwU7-_SV1Nqslr4gXA_JRZj_U7jAR5ry_b28tm2RJ_whydIVQLrMI4A9o5NhHs3NKjTYA8rcNvHjBPOT2q_m1iiZ5a8ZASlLlp504xvOJU_8VhgoRz7knENO2zUSDkvSVGRpdYukpuHHoPZP5WBFMhaYTe24451tHBmDxui1ktl6KUvmFIlrApMwCSO4nu_tEkg3CeKxERiDI-OKjGPQ-VLFyLwOBdxwY4kKlcr2yxbDj_9waHO5iWMeb6QIVBlQbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=QaWpFb3iyKEgLSn3y0ULIYZNX5TxltETFTTjSw_sZUYIgR4483XlvZF0bQT3bUAYXjLqwJvnkzybAhj46WRyPwU7-_SV1Nqslr4gXA_JRZj_U7jAR5ry_b28tm2RJ_whydIVQLrMI4A9o5NhHs3NKjTYA8rcNvHjBPOT2q_m1iiZ5a8ZASlLlp504xvOJU_8VhgoRz7knENO2zUSDkvSVGRpdYukpuHHoPZP5WBFMhaYTe24451tHBmDxui1ktl6KUvmFIlrApMwCSO4nu_tEkg3CeKxERiDI-OKjGPQ-VLFyLwOBdxwY4kKlcr2yxbDj_9waHO5iWMeb6QIVBlQbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛ شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUsuDSW9qfwWC7UErwefQo5wq5ibxe3dqE6UtKuggZ34D-tqi7Y95QdhOyoiUPck81k_SA12WhluJQIyN8g0hsdF6hPWfjpsoB5Cwv2m_IyDaPGfaV7YDSy8MqEY9tIeEnXH1dlUu5fbIjnyl6Akp2BKO4tLznIe4ujwURKSXn8zmmdJRAkUeXeSe4R9S5ZfJCgxoXRC0Ccn-UkvBbKBBjQsEhY-sWmvBLVyht7iF7NHMlNYHX8ZN4J66Dp9SLdsxXDIQJgQLCkNml9Noz0wUuNiDF9dQgsrdD7YSdcgLD-kDKp97h0UzqlA89VIhzPJ2S0SdcKw0OE6OKtPaIcLQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWa8SXLdJiYVKJMiJvg88k7UGBCDuDKHBj05rAfeiiSKEo1jI66SMvsxwHmCvwP0dQJHQ5s8pOj9QyWGHR52W28922kvetsRwdpMkTMCzJZNR8R8utRRBT5Nm34DHjO4GTsr-sZMkJmALd9LAaVJJGloXeIazAxu986BP6fEp2_PuSdpBYNOHIXEJvpTHygvx0uDP9AyvAnDZtPwii_Cm6D8EuamnZHyAel8drTbYgwPq93C3YZkUkamR-cOVPygGD_wjmVoaQTHY_HxFJOPM6s7SL_JRoSyr8MdoqDsutFOyCAN4PjEDTjNpEUXcGVnPtNv-foHkAw9m792WcetEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLCye1hv2wilsV2MdCeeznItd5bRlLnYT4r_LpDb5cQQQRTi9PvJDr8izXKrAbdbym8igN9b7NbRn_SQqWzNoit6Ds2H_Rqd7P1TMse2EJxXTs2t3ezEDRejBEztZqHyCljv3D8pQN9eHRxQHZ1iz9Tr8ZwlPtDhgWqBqU2Vrcc89DVfMgANLIP_XtW5baDqg9PYiGrzebCKBBbO5Be7pD5-BFDOEAB7f4Ukf1Vdl_udoM2Iv9fem9J-HGqJqxhKeLWj5_UugS-K9sX0OFSCOmed0lRxj20s6yBMFCMaWQgX7PwBv1gtD8-rsW5EK9A0tCNtLcm0UqrDXrewCandVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xo-RwQntSWMfyZKTTihPx1w1PCgqgcctxz-OO7-x7tyF5wxRC_8eu6ZBlqaCbtj6EB1ZNa6VjGPaGmk71GQmDrFXWsmdRaGCByFwCwy52YStG7oPsKz0mefHCD3vxYva5Kh8yEMD6sf38hQ027-1h1qI3_8OXR1JA61XGf-ZXFzLvAHliqtLRg26w61_EXz4we5J10lfRZJZEQvyGX-W8tOGW00ZwpfFNtCwAubM7A5blAU3NV7-JdBYn_hovbGM7K5ihwdHwWfjISJwZ6cTa6F5O478w9QDK9rPHNfTU7JSV-QcQFTcPqiJCnhdQy6neCwTnERi8iGGyq0HBlW6DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdRiMbYnwfW6nR2KBXrlviTWGsQ0AqX0OgqWTqpFxzlCzHCeRUxRXzTC4N8dAPN19IysNWbdij9hRBaskF-KQhTc8zEshmaWOxXEax8tDJot13mbaAWMgyLCzixOqrEkN8ER2vSiuWjDel9c63ptbqnhsFlysMCSpjIUCkpcbQQA342uiH1bk6qMIPV9i6u0GrRfNJF6i26kW5sK_BliAxjXkIaP0E9mlYWWATz1Z8NKHzBkU0efxw4ZwRM_c4E6EaY75p4hMqYa2KANuHDENY0NTeE9ScFsAhdeAc9B1RxkxQ7UYBqN1PFqvCob99InLrYJ-uAPyiKAHEtWy2t5SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktggsuQgkEiBQ-rJE9fUv5Kw_ZjsmNeujV1cZrRGdIh9_fTDSiBLcfTHD6Z0_WSZJkTBTWK4qqVcDNY2S1Ffh658naHXz8qV5-Vxca2WKGRasrKHwDzbB3WEDPA_skub7kLuD-nPlonCflSSDONa9dOpvgG49jSp22ooDuShE_OQKQ8jWAW46Xp68qaEOqF82pRM5uCC30ApW77lJ5lMCXPWcNULFYMiQIPf2DtuES79eBjaGCQ4iOn2Kz9NSYizNgrYYoyNNg_2Szq1p_DvMCcIHh0eD32j3OSWpdHCC_bIdhVwhNIraU4kaHYEsgzIYFYnZGUn8FyrChSqietp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=vflvJai7kiFTBWJUfAOWydgOgK4p1xJROqiyJSnLyT6nCWCi4PpjFSSF0KRvtdj5HppHJn7QeAfp3UB3cwLNRHu6o8IZ41K4LGMrNYrzmmx1pTtExggfVi73FCdAtbrxP1DGAWSWLOXwIIPKP4zrju3XHMqyH5-BBA2YJjyYXFqpEIcacOjyPO4u70f3t5BZsjzIeg03Y_O1jl2XpqlSsPvQ-F0tlLSP4fgNUuYIC_sPapRP-g0NjZ6SvC0uEmz5mNTuZRkYdUIsWp60XRcCykuYLApSVPiPSo92NZxIaHVsy3PxMrZ1Grwp2eXIStAi9LRQkd-zhkxmxDOlbwsFPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=vflvJai7kiFTBWJUfAOWydgOgK4p1xJROqiyJSnLyT6nCWCi4PpjFSSF0KRvtdj5HppHJn7QeAfp3UB3cwLNRHu6o8IZ41K4LGMrNYrzmmx1pTtExggfVi73FCdAtbrxP1DGAWSWLOXwIIPKP4zrju3XHMqyH5-BBA2YJjyYXFqpEIcacOjyPO4u70f3t5BZsjzIeg03Y_O1jl2XpqlSsPvQ-F0tlLSP4fgNUuYIC_sPapRP-g0NjZ6SvC0uEmz5mNTuZRkYdUIsWp60XRcCykuYLApSVPiPSo92NZxIaHVsy3PxMrZ1Grwp2eXIStAi9LRQkd-zhkxmxDOlbwsFPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛
به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_kuBUa7j-cv70CNaLbYHVs5rEIye1PDSmGwD1YqqYRMnEFTFV5oUpYcUp1eYD8UxPL3scMoDthIWZ_Bon6w_OrAX_hCjy5MS38jOOrQsRrUpDOpPGZmVE2X2o_0v16WD6Pw6Jt5ivpju38o34r8NBQ02oMEkGKxOK2FDL_rugkhhZNgrPRmk1mHdgfR94st1D05Oot02wC-iDT5IM2aZVgdMXTugbK-TXvhfiAjfT500GQ9bOiornML2Pi6kWbve0kcEg9c6SQC2AAa6xYS0gykei5Y9RsRExVxzrBdgY8Q7t5aDDOpwvdl94F6vgKmeYEqX9Eatq3XckrLQ--taQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIxl1cQP_yygWpZoM5XZ-z64Z2dqZKUWzCPD1MVQADkeezR4v_BuDOZ5BoyXy1YrRy4HqqXYqkCV3-MMgUGFspb1sxUabvHhiYfVTBTN58f78gnih406ipPQCCZpkI4wHirefmVqwnMMmGlP8jKa4zAWMMsGnvo_9r29G8rWQlhzWze4q5DCqJFzfkJfPRvBfXZXKLAOV6y5OF3MBj8tnQA2vjK4v4x48NPBiBmUcL-8GmLTN2wRQMp5pzF1fJp7vNbWELOKjFKsdYWHhWzgOj-1Gbocn2uretZVA-DlIhqHZE6ZGhUHMj309Gb-c2h-RagMqFj3cm-aV_8TifxqBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTVSgfGxUAtc2AMurLJOnqvhMNU42TuR9m8VVF-vl5dys7TVOmwN4Y3JjAO5B6-U9FrufyX1A_2xkG1IvmvbCUqQsh4DKjgoYYB8x1H5Jgh48_5P1z1JmXOQBDo4fPkzoYtb2T94uArKCvXjrCwCMtE71YYzvQW9QTxbYYAyGMb2yHPlAjNU2D8PR9-zVam-yfC9o_XjzvM63pSJ2wMhmmlP1CMALaidDRFZfjahw3SSHzlzcUO5GEHVol0HqZYIybsOkLlOzEdYQN5euYeRezvdrFo5t5YORWBFfju5xeHimgeedsLCsPJEqUHasl2USm36m5MKegH2xnJFu7h2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpJoUALafHrvxiUE2AeJrdaIE8vMtAlHY8w3Gi59fW0CwX5KNImCUMNx9ziB3t17v8C4BigfXmJJ5534n7bYk36xx57pN5eHMCjKyItrihL342h23oKrpP5W-RlqPtUaGnJ_qw3_1yR22xFcerQ4gbzHJnohOIDejMxmA4MAjBmGlKSE0r31e3UjDtbS833DDoEv59IGCAJHnyiQfaU00V_CoasqjlSIq8p8-BWPwItliTkCmRs2iGNf_RtXvbdf2CJN2X03HTmX7ddbFkT7bI0NxhkV6J8ngELTE153ixSDstZEWvD_wRLAktRLjTbVaQ2kudHUypGzRo7iWvlA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl27Of7yYircQGZPA4a7CoJZpDMdMNJ22NKDipfLF6dzTDNC5ex3DBjmXLhjxlvKnAikqCJ0PLSY_dLeZXjBGrjIGPnRIcb2U8xU8mco8J0DhRer2VAsB3wjIBixI-JDoLG1R8kd3pEbpGUdvmZGmOmVbnv8Y3zXQP1JcEjo0SHIbNx6fF3XdfMbT-cvbtd9LxfviBM3ITDkrzGMo0k4OMys9gVBgpK0DHApca99jPYF09CMKZW3_0ouFPVT7c1HVRCJzrur3QrgpMFSll-110v_WDuucia3LAiZOKv5muKsBileFDnz8NSDB4qq2khBJnF3sGfxVr0wmGXX44z4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db3tUrWwrzak1OcUhl82hNC81kuEYYQTvUq-jMEeLGIgbePmZziMQQ_rqVuKZmy9QgY9QQZxpptgMj_6qNSv3_EKYFGRgoS3D263ZUPPQsrng8mNYPoOmeo2IoOyaPoB0b2tdxLJBv5-cL7ZVTnn7c0Xw70XI71OZJr9LBHXoQwDedCooxMs5pHupV3bPDbnZoUyQCy8S_bZZ3BvpPzfFbvsoeab1h_pFXW2uP4bb8JBvTpoCZOzgx7KFB5gwKaLUom9-ibNj-I0uHrDE9KtNcrLk8AVwWRwHeHdj8JoGhq5F5Eh7j92Qcri9kOA2NqU0Jke29__IEnEnfJhvjzDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-lqDSMUmErZHESTD9Q5KWkuCWLao_unu02dO8Xfoi5Sso10NJPCcGWt7-dpS1vO54YIIK9jlbjPp0blmgUOR0w79Sd9-SNmFHYf9U9jUu6v9LjMEzNFm47rVLCAFEWUolDCW7gG7ewvcFDE0NDBwY_6BgiTFaEw9fprdfVbdpS3WkBvnHoSJvC3Wbd6-h_KElH5fdMcAPhtxGMZ4cPM75AGrZAzNBRjgdI8e1Q7yY3Ol79oJ5a0TSy1pWG5D6gNqHqAK-7t82lJ90aWFCYYu30Nhwrq3DK-rrQBIEbclwtVjhCxTrAawZdQKEiBR1BjF0k1rSryYw3osdE-KXfLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24886">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRMO-rwLI1k89XCK2NY-ZiVQIJW3zS4orzG5-uTg3IM9tGumzTKk7vbJqGk3Mqbw9kf_tM02cSFO_R-pHQJiXG_uiRqCIVl09pvm8ITq9UK_xg7v1kvGlwvsanBtgRf8_3Cgu8cMh7ru_kvzMMQaB_aLB5PlKzsXkji7hSM4cxOYHz8_0tPFH7kw1Q-_PVwhvDPvRB8r_WUyVfjr2bl7KUzMJ0Nli8XyR6vqmyCp8uzhiT8yt5AsbPc_WKTVsGWHLDJb3fk9gm63ROjjaNivS6wBUiN-Nhu3P2FcVmK47V94vXKlX7SeN6Pm3yll-3ZloXoXMVX6wflhZ-8Bodfd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه لازم نیست بین انتخاب‌های تصادفی یا تحلیل‌های زیاد سردرگم بشی…
🎖️
همه‌چیز برات به‌صورت پکیج‌های آماده با ریسک و سود متفاوت آماده شده.
🔝
فقط
پکیج مخصوص خودت
رو انتخاب کن و وارد همون بخش شو.
🏆
ویژه مسابقات جام جهانی فوتبال ۲۰۲۶ | ۱۲ تیر
⸻
🟢
CORE
📊
انتخاب‌های کم‌ریسک و مطمئن
🔗
ورود به پکیج:
https://betegram.com/share/betslip/ZKTRF62467
⸻
🟡
PRO
📊
پیش‌بینی‌های متعادل با سود بهتر
🔗
ورود به پکیج:
https://betegram.com/share/betslip/VGPXN72923
⸻
🔴
ELITE
📊
پیش‌بینی‌های ویژه با بیشترین پتانسیل سود
🔗
ورود به پکیج:
https://betegram.com/share/betslip/DACCB49184</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24886" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHWqkOVlcDcjMhNOXSwGcSNaxDJU8Olqsg0ZVFdie3XU1IoBDpXdyUww5XOPj4vrlq-7r9vLqWR2ddRvmqr5Niu-XTmFprJmPs9rsEs_XjmnH9ORlIrNwgjSys26kHDwai4z_M5yYBC9dc2WZVvX1zrPAQC05fA6iGyU3aJulGB6Pe2AWcPqaClkOUs9W_Vi6SE3Z5SDCoh2PdjSjKZzOPAsMDUGfbpJrtv7tbdrD3URDi-d0XWmNK3WIHpTkJZ545USNqxBsBA7aZ8PGSc-kYUZSI1s02bVg3_gYKZS5Spe2IUFucW3cuwjQbnYFXIIguKAc3C1IWezwOjiogHTBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBWr_Tiw8MWnk1ZRGpCYIimhAm472eTGswDYhBWyv35b4OWBXCklfaivUvp944RjGcTSPP91hqAH31N4c4G0Z4ytQN2tWeJdkRCiMR5GMTdkMwZ2ytJZMNO6UBJgOkJRsMknS2JFqRflKhYOoNhBaJzH1iQQFmiaM9Lk1E7HGNxoWr2ptd8HgqJof51_50QPpeMmrvZKnCI39Cq8qZG7oieGHtxeBi5edwGE4z0-8z5u4x1hkigZSlPAt7ifWbGt06ulycyAjUBXJ7F-w25w89-2xwrUGweQI2AnleXfEekc4mxsH6iY_wgM_Wkvuq1JB9Pwv42U2u25CkzLwditMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=rhRDjmx-OyA7ycdyiemoHh8_oCxzQIKC-a4pJtbOtcQAqUjJbSa8rF8lGnNESPfPiZ2g4wD1zsP9ILrHDKdp5AnnVLhwRuVRrI3z4_t8blBocg2Wsyc5e6aLxP7FKLXGz-7cdicVKI24reif382ayj9wURNO0aIa2hMdRBv47vYtb-cuWzHJkDq4dVQTu_UAKWoJ_IaUP8oqPsMGxiQW2_FHRzaENVXW6-9vKz_NzTNwGHwPdYJee95ELMsURACYDuokNoYugvA-oB4ogU9lEGzMJWQLZBnsBQnap6bc4Xw_Zk4MiQQnv_6XT-KnneLhfmp6xIOw71dFlkKse3Z8og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=rhRDjmx-OyA7ycdyiemoHh8_oCxzQIKC-a4pJtbOtcQAqUjJbSa8rF8lGnNESPfPiZ2g4wD1zsP9ILrHDKdp5AnnVLhwRuVRrI3z4_t8blBocg2Wsyc5e6aLxP7FKLXGz-7cdicVKI24reif382ayj9wURNO0aIa2hMdRBv47vYtb-cuWzHJkDq4dVQTu_UAKWoJ_IaUP8oqPsMGxiQW2_FHRzaENVXW6-9vKz_NzTNwGHwPdYJee95ELMsURACYDuokNoYugvA-oB4ogU9lEGzMJWQLZBnsBQnap6bc4Xw_Zk4MiQQnv_6XT-KnneLhfmp6xIOw71dFlkKse3Z8og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNzg2600TeRr6TrHBUt9UzQWbJSmtBzIordANi9cszq_xIg86jkUN9kSxaKLxOniVElRr4qxaFhqLs_aiPe2oH9dIsvQzuQ4gsNz-bhJ_5w2jjJF0KzQtUsYLXHxhBbX4VpYDRYgYzndgvS7cbvRCue_UBuIx_OPQEooktK_oFiRAsfvliDjyEG2nTgqqOHreZ44BHjd9aEL-wlVMlFD-Wj711SSkppziY8eo8C5sdVFekZtwVU7oQIBDIHrNOTkvrnMdY9I8RDCHP6sMVMrbZgTiAf29Eqn_EsjQiE7820Un-ghBWBnnYrQRHxAsUAb-5zvmhvCdkMovmI-0UX7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWxcYrIuBuHfrQM3M2O6v9aTZr6ftKrkA6sjIAKYTFNVtf6dGj83-zgellznRpvQVc4NLPZT6Qu4Qi4lToo_i_v7v76YfmAL_33FvbH8geJLNgqqSqgUjXEzxa5ZT89Bu5xdGFyMwSqCYoTjsVfvGTfYISC5nrB01bxGz5svp3uy55x1hB8xqmkUTb1iOgGI2gdGOxFCtjqm3JVQZHydY4OECMFwcIrEsJzvOsOpdNylSDViXpdQgis-i9R1eMqawnRai8ZemAzMyf8SEf4h0y45bocx4dL-SxhpseoWaK8MZi4nz3P0Zrc8iBrZAp_FsvfpcWVCCPzBuJu_4k3ivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ6YdYBIYpU_hbkbwgw33czthiD4kuMugqDunNI6-VYzeCa1gkz2qHceAP-moDDYyhgn0xorCHDWkw9bCYzRoBMaUokIuiH8dLFjhTgDCjsMtrwXK1bmx_BknreMo-fDWZ4pD92v8UTtgkYAtWA4IahtZUZ8qhKQ1pz6q4xIHgslTguzsvX_0oeIyvwanRa14FozLpmYTKlEv0GkbEfPvDFhTliMm9Wbc6Kaecnz9wY3r_0Bnexg6wDpxRLzFeeHCcVgc7h_1t8APKh01zUQfGi-OtXA7z3tVg05xx4hWZIwDvV4aVCoL8n8AsTvQ9pPP-FYflP7JBOk2blnU14O0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=qHvjDCrR7WfClkWgrxQuOZmQPcTqDimd2pYGRk0RbyQYo8mMIbhv0XOEO4TpSwQKGHcMSN_nGMdr3Xa4xVHjFK4-pY4gLwcPSM_6gy8H0yLYkj-Nhu-m3iJXcaUJXtGpAaEqAVJjkYwF9QrBJFAnyyj7zSmCHZAJfXEKazmIP82Y5eNAIqveInirG9T1Os8jQtipG13ZtIl3b2gu42CFQV92GKYZ8Ppw7cBTZ2nmlAN5tu2nVtS63zmu9LLaexwS3Ge2Gy0GoJQUgvKcY6y5ncoBz3P8dc92yzBp4xmrxeLSpnG1BBfZOBhNWVuQBFdcGZoernqCstmUgJ6mWAmiFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=qHvjDCrR7WfClkWgrxQuOZmQPcTqDimd2pYGRk0RbyQYo8mMIbhv0XOEO4TpSwQKGHcMSN_nGMdr3Xa4xVHjFK4-pY4gLwcPSM_6gy8H0yLYkj-Nhu-m3iJXcaUJXtGpAaEqAVJjkYwF9QrBJFAnyyj7zSmCHZAJfXEKazmIP82Y5eNAIqveInirG9T1Os8jQtipG13ZtIl3b2gu42CFQV92GKYZ8Ppw7cBTZ2nmlAN5tu2nVtS63zmu9LLaexwS3Ge2Gy0GoJQUgvKcY6y5ncoBz3P8dc92yzBp4xmrxeLSpnG1BBfZOBhNWVuQBFdcGZoernqCstmUgJ6mWAmiFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqFFKf4EoFoib-x0pbHh8PKbN3qznN80SmHgEFledx3T8uZELhsk2JqWjZv56hX3ZUA__ImN2uIMU5k2Pd0GBIv_PdfAFVcv1KNpVhhyFtUEwpBP3fuK9qkVmNqQ3OUvEEy2XyrXgN69_13Z3qeeAD3JEkTJaAqJOKDPLdLe7FAFgVyKRMeIezFz2NbeqfC2gsV_STstcBZF4VH3PKXfH451zS_w4Z6m2GqXc0Iaiq0l-JrV8cgudaI4yZCkPrW5AA45NmsVtSD1G4PMVPxU7jPPYlm1x4R-ZKp4pG64QepVfsrBT6M-LfMkkxGuLUoaj8ysbcnzErHA27BEygXrjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=GpSy0S67Rj_ehuV8MgbxH0hnAiOA_gv5jrKEdkBJc99YHKuvwiIg_bro32ml9T8TT8V_TWK9YU64PB0cbwW_rU3pMkzCPsfD_wnkpiiObEo8WqvYFyVDUX5UrdRGEdcNOSMu3xTSCJXYVS1MLJAtOoKOq01OQMVlt8Xmi7934genpgaLK5X6zum3Zc3vRlBqOjL1uL3074Xh0Wa1MsB4LCEC8UxFQTcYYgV3v_TV4z2MN82Qg8d0pE5D8NKt62neGsyV9COiqSwrKu1VbgNN5kCA13USmw8PFy_ifYMB8IjmzLbKGcjZkvra2fspUg_bOYffyLC7TO4NDU7pdb2-UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=GpSy0S67Rj_ehuV8MgbxH0hnAiOA_gv5jrKEdkBJc99YHKuvwiIg_bro32ml9T8TT8V_TWK9YU64PB0cbwW_rU3pMkzCPsfD_wnkpiiObEo8WqvYFyVDUX5UrdRGEdcNOSMu3xTSCJXYVS1MLJAtOoKOq01OQMVlt8Xmi7934genpgaLK5X6zum3Zc3vRlBqOjL1uL3074Xh0Wa1MsB4LCEC8UxFQTcYYgV3v_TV4z2MN82Qg8d0pE5D8NKt62neGsyV9COiqSwrKu1VbgNN5kCA13USmw8PFy_ifYMB8IjmzLbKGcjZkvra2fspUg_bOYffyLC7TO4NDU7pdb2-UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGMrDrGK6-TJrLYZK7N3a3AZCp05MFk38AQ74_5GAYjjACz7_zVf3PMiiOhyBsPKhsxbaOohWz1rHKWbPE8Fa0LmmjoODcv9W8Ou_uFs8sFHE-gQroiqktdAh1bqVe5nEH4jP1K4wA1gLI2rpySF0K7uLkbGuJ_JS0juRk62JULbOY87Ec9lUEhdPnLI4FkEMJLVAaPg0097N1fMAP9sBRwZjZnlEOaJkjSJW4kwIhf42IEQY__5fhNUD1_LMhB-wwMSEYujDhzfnp7bBd9_tjRISlwpwmu7uNWWO3SzVdEzbMTKPDLBwgqZRJyWPMsBl_DNcwsB3GYklIkQkpYbhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=o3YWXxcPZvZoLqNhea8tb6btW0Z3pBdjuYQ5RSJavN9JNxI_GPqT3Cz-aJcrmfm3ng5zw-IlE-aWWLHrS-zNsjk84Cm_bxP85u4wfbVU1TilzOB54At_V4UlApUla_QnduelxV05W0IhCgVROkgTDmPl3Iw1lJAOj7V_j_yE1VVLFannPiioK4JSL83FAH1qPpQ2qa3JGR60SZ0GpyPMlJVxTgyVWNpYsImKamV9YQoEY6r2YLoPAjBxI60gxhhLpn7JXzXCOq4WJIzhhTH8aCk_lJRuzFcKzi1uU43IkQmBAg1dWIme5RLclQ_AFvzEQTnSRNv5k2PMdbQ_rKq2bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=o3YWXxcPZvZoLqNhea8tb6btW0Z3pBdjuYQ5RSJavN9JNxI_GPqT3Cz-aJcrmfm3ng5zw-IlE-aWWLHrS-zNsjk84Cm_bxP85u4wfbVU1TilzOB54At_V4UlApUla_QnduelxV05W0IhCgVROkgTDmPl3Iw1lJAOj7V_j_yE1VVLFannPiioK4JSL83FAH1qPpQ2qa3JGR60SZ0GpyPMlJVxTgyVWNpYsImKamV9YQoEY6r2YLoPAjBxI60gxhhLpn7JXzXCOq4WJIzhhTH8aCk_lJRuzFcKzi1uU43IkQmBAg1dWIme5RLclQ_AFvzEQTnSRNv5k2PMdbQ_rKq2bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=QkyYe6VmEOCmQJigXj5hW7wkoOQEsftfpe6YydmZ76wKwGN68FuAjJjRAUBSc_Cs0gqfrYioQ6opgPigMChBrcf0LNOK8MAK-smMDXVvCHXlmVSVGrcSBhOWC6YC7ey1J_za5A77zNuWYUzAt2vR58ke9kYv31vVJnJ4jfEQTiYpuT2fIk43BkZi4pCeyd_qECZrqgxLcHRmu3GBih1qDZf1fdN6vDNjOlXWFche8qT0TR_eKsQ-yYTOg9QcqDVpLcf7HiyjDRQ9Ni1EvRWrQP5HEt0yLWaznCUPmZsEWCNP64idHK6K0hXMsGE8W86l8e77j-MVnfMBg1WT5zR43ALZ72Ez6RxhgDdHtkvpY2FS29GpgXdmqnKQ0xpDNa3kSPLm7RmDbJV4fIwm3eS63mZE4UHYVVBw0KTPA4ylzfRnJsBU0V8iKBF4wOuvizHE2s-MLDpGlU9MoCdswAasILqljkMYD5pKQcc8ppS427sPY5UaqHUtH73yd_MtpM3n9VpdNLTJ1Jiy8M4z_LpQItP4ootLIPcsVdhR9J56xD4g40XyGihhASS5wE5tLGklO8vp5IgDDKzJfulUmmtA5kdFFfkqko4u3aUiO7rEDyxmv994uXquNzd4C0xal3eQZT3Kni5HQW3JiXxzBI9vV7sWEC-Fa2jw2vErAikXK_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=QkyYe6VmEOCmQJigXj5hW7wkoOQEsftfpe6YydmZ76wKwGN68FuAjJjRAUBSc_Cs0gqfrYioQ6opgPigMChBrcf0LNOK8MAK-smMDXVvCHXlmVSVGrcSBhOWC6YC7ey1J_za5A77zNuWYUzAt2vR58ke9kYv31vVJnJ4jfEQTiYpuT2fIk43BkZi4pCeyd_qECZrqgxLcHRmu3GBih1qDZf1fdN6vDNjOlXWFche8qT0TR_eKsQ-yYTOg9QcqDVpLcf7HiyjDRQ9Ni1EvRWrQP5HEt0yLWaznCUPmZsEWCNP64idHK6K0hXMsGE8W86l8e77j-MVnfMBg1WT5zR43ALZ72Ez6RxhgDdHtkvpY2FS29GpgXdmqnKQ0xpDNa3kSPLm7RmDbJV4fIwm3eS63mZE4UHYVVBw0KTPA4ylzfRnJsBU0V8iKBF4wOuvizHE2s-MLDpGlU9MoCdswAasILqljkMYD5pKQcc8ppS427sPY5UaqHUtH73yd_MtpM3n9VpdNLTJ1Jiy8M4z_LpQItP4ootLIPcsVdhR9J56xD4g40XyGihhASS5wE5tLGklO8vp5IgDDKzJfulUmmtA5kdFFfkqko4u3aUiO7rEDyxmv994uXquNzd4C0xal3eQZT3Kni5HQW3JiXxzBI9vV7sWEC-Fa2jw2vErAikXK_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=aX5sjIzMJeFRePL6yXI4ctxjrlGL9yM88Xyi6xak76ErVVP0WncZHvn7zXD11_u8AfAU7nW0lSapA2oVZ1g1iy_EcRpXVZbuRC7xqTOgAEaQ-Coz64rgMDmoQ-zzDhlZ5-p1gCzqwXi7W8sx7ZVT6u835RoJ-T7ytmM2wua2ovnkC64vxZtHkKI56mWiuniBFsoROUkwHDiJROOj5GtdlOFus66EQNDol40Iz_2q9FcDgJhtnKs2fvrFuiUayjABhl_TqtOovzWhDyO8hiv1WSM1iXJvTjxW-hgrd0vSCDAAqzEbbZ0YHEWspC-PZBwV1-T7BDmWdor8SPTDlECoiR_0pqvLd44eKKylpSj9yA0_QuMvXU6vtapnI1iCWZOHVwkNyb4S_Hw5AjHu0fOfXXIjC-iJE38kELLYKu_0gZ-gck9TKXNVEynQDaS1zZmHKy4rtkQSytDZByu2cL7qlKqipLDD4VB9zZ-joMCrYcHlu5k5eIA6Gi7HeC8MXgc7a-KxnKoXktw_Kf_uRfEXKuR6AouM1uPsWnXPS9q7UZwbuvsdN6Xa0nFNEgwudVlPbbMHpNpk0TGzfli2LSzbanvFhGQkffp9O0l_dtZ_N7SHir2oCfzsloa2q70Enox5TM6yi2h1-H0mHWvO9lhb9lt9l99IaUl_xV9mKhWc_O8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=aX5sjIzMJeFRePL6yXI4ctxjrlGL9yM88Xyi6xak76ErVVP0WncZHvn7zXD11_u8AfAU7nW0lSapA2oVZ1g1iy_EcRpXVZbuRC7xqTOgAEaQ-Coz64rgMDmoQ-zzDhlZ5-p1gCzqwXi7W8sx7ZVT6u835RoJ-T7ytmM2wua2ovnkC64vxZtHkKI56mWiuniBFsoROUkwHDiJROOj5GtdlOFus66EQNDol40Iz_2q9FcDgJhtnKs2fvrFuiUayjABhl_TqtOovzWhDyO8hiv1WSM1iXJvTjxW-hgrd0vSCDAAqzEbbZ0YHEWspC-PZBwV1-T7BDmWdor8SPTDlECoiR_0pqvLd44eKKylpSj9yA0_QuMvXU6vtapnI1iCWZOHVwkNyb4S_Hw5AjHu0fOfXXIjC-iJE38kELLYKu_0gZ-gck9TKXNVEynQDaS1zZmHKy4rtkQSytDZByu2cL7qlKqipLDD4VB9zZ-joMCrYcHlu5k5eIA6Gi7HeC8MXgc7a-KxnKoXktw_Kf_uRfEXKuR6AouM1uPsWnXPS9q7UZwbuvsdN6Xa0nFNEgwudVlPbbMHpNpk0TGzfli2LSzbanvFhGQkffp9O0l_dtZ_N7SHir2oCfzsloa2q70Enox5TM6yi2h1-H0mHWvO9lhb9lt9l99IaUl_xV9mKhWc_O8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNLYZdes-DzCz_7ab-lD85hZUUMa8txy9b9sVlRV0jEaMgm4LltH7FoIZOuz9fVh46WkEtZfeXUf1MdEoKi4f3EiMWBfOaIdWqlt3Yt_Qq066C7FaomrizpthH5b25Uz2i3PCv69EKQAzwG4lSDfh8Mev8IYA9rWUPE5sCta81fHVJ-_cJ02ZYiGzO9qyk5x-nylMeWMVABTNMdO_rkBnJFv6WhRDHwhICg731v0wZvK6Z_3G8cHtr5WO_8CAETihXueXLzh_NgddyiaLnfl435IuV2IMJCROAf1UJ9LzIgbyz8gLy6Us5fs8LoDF0dVuWWuNH3GuK-05m-s1EI0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=Swncj6pOshtoBBOkQbffbozoAhZDQoEg-5W80AuA8THKlpkkwq05LVwIi7-46Cxp-r4vsKps9cT5CCRouHjS4ejm6E-r5eGr6LVpL7zLsYY5AIZWpuUcIl8V4beNhYfkAZRRo-vQc6PQ9McAN5J-nNDRBcBwInuo2Rfx3JO7ZMUDp0SFAdioHqlygWGmmnpHo4PUhD88Ym9oGF1Q3JfkAHIUAK2BSAebjmV-k28v0LDZU5L3fA2QKdZRZb8f0Zrwdh_GhAaHE8xKxF9cRNdsyICHsGtBEknxwMZZ1vymE_Cn3kFPZyD9ewNn2jMuyy1Ex8vzLm4NOHPk8LtPOBxqpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=Swncj6pOshtoBBOkQbffbozoAhZDQoEg-5W80AuA8THKlpkkwq05LVwIi7-46Cxp-r4vsKps9cT5CCRouHjS4ejm6E-r5eGr6LVpL7zLsYY5AIZWpuUcIl8V4beNhYfkAZRRo-vQc6PQ9McAN5J-nNDRBcBwInuo2Rfx3JO7ZMUDp0SFAdioHqlygWGmmnpHo4PUhD88Ym9oGF1Q3JfkAHIUAK2BSAebjmV-k28v0LDZU5L3fA2QKdZRZb8f0Zrwdh_GhAaHE8xKxF9cRNdsyICHsGtBEknxwMZZ1vymE_Cn3kFPZyD9ewNn2jMuyy1Ex8vzLm4NOHPk8LtPOBxqpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=mFy_xfHxnlq2TveA1udC3pKtlGIFmQA7nCJpf1cv5NBkUyZvt1lkpQIay93pVsVCh1KyiZ5fdZUUESZfSkWllQ8rg8jC5oq_VjfCe_YdguKC1xHClbdk0QT45rloy_OUtI99O16rsqtYTqLtOaSPkA3Lql2FJPSalvP7lSIDHOOhmPmQsCFQ4bF78-GkEQ32o_LOrznQ7jmBPTcKq5Zhly2Y9Y3UEwgkrOKlPwOAf2Wt2nxx0uQ1BKIl2Gh4rxDXhwEuXBenAjwc5qG8Ulr2fVlcKfynjctlww5w7mq1hRtByQ2FWaIlvVEtzudqxcP924tIMLFUn2vQLIZ6nzTCvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=mFy_xfHxnlq2TveA1udC3pKtlGIFmQA7nCJpf1cv5NBkUyZvt1lkpQIay93pVsVCh1KyiZ5fdZUUESZfSkWllQ8rg8jC5oq_VjfCe_YdguKC1xHClbdk0QT45rloy_OUtI99O16rsqtYTqLtOaSPkA3Lql2FJPSalvP7lSIDHOOhmPmQsCFQ4bF78-GkEQ32o_LOrznQ7jmBPTcKq5Zhly2Y9Y3UEwgkrOKlPwOAf2Wt2nxx0uQ1BKIl2Gh4rxDXhwEuXBenAjwc5qG8Ulr2fVlcKfynjctlww5w7mq1hRtByQ2FWaIlvVEtzudqxcP924tIMLFUn2vQLIZ6nzTCvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=ksbrEeOk2i8bTVTcEavMGZbeFtHg5pcZ4dvOrN5mySLUkJ9bRIMquauRe4aXnMYexaoiaHSaJk-BMoAyrlRY4Gp-RXhQuhOR6fgX9oZlEhKZdKlk9JQfWPwKKtPprpDkX6pmO1cF7cWSkZB6fyfWrdOedxWnjqH5SS1u_QiWgQf156gy_dSUCg61__VGNXfODyNXIYPBOQh0Vb00a_ErdZrtUdgykLxHlosKv1KEKWUqTQ4P4l0RWxLTIcyymsXhxB44bDtFS12olZxVOYWsJLIKZXuFGPGAFU3D0hoxz1ONy9oAZG_55n3chUjNP9R2QyHePQoCn8KOre6VX3RbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=ksbrEeOk2i8bTVTcEavMGZbeFtHg5pcZ4dvOrN5mySLUkJ9bRIMquauRe4aXnMYexaoiaHSaJk-BMoAyrlRY4Gp-RXhQuhOR6fgX9oZlEhKZdKlk9JQfWPwKKtPprpDkX6pmO1cF7cWSkZB6fyfWrdOedxWnjqH5SS1u_QiWgQf156gy_dSUCg61__VGNXfODyNXIYPBOQh0Vb00a_ErdZrtUdgykLxHlosKv1KEKWUqTQ4P4l0RWxLTIcyymsXhxB44bDtFS12olZxVOYWsJLIKZXuFGPGAFU3D0hoxz1ONy9oAZG_55n3chUjNP9R2QyHePQoCn8KOre6VX3RbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_gGxkxn-qyRMrCtzAHLnCDYa_hdc41kTXrCDZ0TH4nCGx0ff3UMzRKR_Dmya9iQscJ2tra8heRBy6n9A2h4n4l3PYCQ9Syz0kkqZYPsHv-MYBeK0_Ga3VhjHizouqISmoJ2G7jUPD7IXfE5Mx2-j4NnLfFMkgc8YCfCqKj4pinDM8wosBACkw8_md4czLq3Qqlr0hg4lHis4f1aKWYD1NOYMVLv3333vxu5YWfCZ6n1gRn2fBabSZrVGnJODl30hlDtbmQwAdyUmVt2fJoKL-lAiyxBLK358uG-0UX1PLG2-KLMSckfq9Rmk3AFS6yX09ZzkuxKoBPmysLGoXFnkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRp15fD_hFeRVy1qwE_n1hMAI43oDq4AjqI3Zljd4-sZ2qxieozVlphxWJ9ytM5aFTVuVy_H4PswsbHwzkgQRPddP7mwLYQ0el8eSUDt4HQ02ip9dQYz2dKUP_2hY-viIP786u0fCm2HrwgK5NwI5zpXwajzflsltXO9s06cD6E1exDtfySB12JvnpXVJ_M616-BVzYfjhBlmVORTYYabAJ6nlMoeZXmCuIbWkM3adObhJUkMrOkE1c9DeP4ZcL1wcjTYXSOsH5cKLYe5QmXwrO_UN7rAkhJS7BrWXIZChr-qEs--SYJCp7wAdNxsynpX5PlbLGLWE8KkWvScCbg-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KI6HfcH1x4brvl2OK5XndhV7XLJ63YIr9GBL89svzYuYrZerqdwWs_i7awNdr-eXXhTo2OnFICOQEwA24ELfIBhEVwXQsGjTTq7L9Sod-J1oZxKhvorYqcivvoIWyC8--MnzcXtEAUlWhTv_7qxXXSoP399cHos0mbEyJAzbpKZ4Fo60bfdGXXdPISP9gptai79fjdASsdSmhLf0jpX6HyvGLz-wgiiqgKqN6T8TSsMKbUNaFDVvpVQHWY_xo6UOvVmw4CEF8JVFRlNksaFts0qhWEOuSPli1MyHFR2qXkIyXZOrafJ4Fi3hPL1mFa82NDV7isN8mI_563f99fXaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUJ1tQMRNMY3VwXo33XIQdp3X6pUCfjPfi8ihnR5j6jmQ8PBGhlf4dVLyrglwZewv7nIrQdcmP3N42d35CNiK9AdxS4luJr0VoSu9eSscnfe9gNF5xI72Rz9opVlJsIOJ7RVTnf-4HRPViCDXX1GPPR3Cy-loZXBN0DyPZfzHUC8n5W84avaBsoZncahjImmpL7oovcIOpVQlJ74c3Jvji0imc1KNFl8aRcUmp0shfkDX7XwfaLOZGFxw0JHogkrfvudhSUI5jGOoo2ndqSW-JKMSEl1Y6lf0dp7vMMf_bbQWPnuY8UkVekfyYAO0Gn5u2KAk_PsDcIshtI_p4z3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8rK7-QWR5tqZSmIYfkJHsDufFmbiqXxXK4_M3uQ1noXXc9Cxq4Yg5tptASH12cicG6fkZsvbYVFDIByzPZGqfGzdOJyfXM8w_KIF4--szYsnK4tlPFwFf4gNrvZv_97Vkk3EvbHsaIOI2K1hnqUxCDoCmQDkvqzjwJIqxR6AYu0AcNT1B3ktt3W6BLGMqa98Y8cBuDED9Knnc6P3JWtBgLJHowonF6_ReKi4jxF4yNrBwpmUUNYQ9Krn4I5L-mUfdG1tAGwUcnwKfEJKu9aSdJjo4i_1x3twFcT9Egiaoq_6o8q48I2P5Yz8vfEYRARbbgzRSpZmekv1-drxLrFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB6Phwk_FI6Bpe81hdYKYDX0WwKXgEXoQS3GxjPxVHmC_rDV88uRo2xHkoEISy2LhfQ-Z7Bl8uUGLApkWVxFUY5Qixch_EK_6chdObXw_Awn9hmt5mrI54MaKahX0c8sgmkTyhysQ_h1sBkvHYN7gS4UDjtI8d9H2E3TzZvbqlb-GVV63wM5iuvC6Dx-71AtrOK7ByC6vrK4w_j3Zsg__w-cLYJ3GJxtZkAIccXHSDsD6JGhZTRNhUsOAijODYVNW8gkKDLFkHWnUU_zjT-mdta1VhXJWZpTG5KG19M9dQdImZYUcju5qqvJ61wwX7v8cvDPLMc6c5g4D26899BXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=ZpK4lkfOoQyU5-2caufum590GUFSQSoPyHZ0xEEKfn4jY6oICac019RPNTz2Gh4jQQFQdmvvImW46QadMvsSiLC3tedsDY1ytGXVZyc8zGQTSEqh97X3sdvkhrCx3s9ahFH6hrHYPjxS9oy8zwXiVcKbUdW13z9zycxx047BS5w8_hJ3JRRguxNhw8xnQQkFy6o5j1cviisnp8AvM1YfHpp2kRUSTID--YJBF5Sb3YC1mv_yvlR0r8fN-gsNCo0azzalN5O3YeW3rd71NjYp8ZuKrxaaY3QFRqoTd25TXCrSLLpduxcUGEWkC5XtonU1Y4tR5OtS7EP_2L4cTHAGcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=ZpK4lkfOoQyU5-2caufum590GUFSQSoPyHZ0xEEKfn4jY6oICac019RPNTz2Gh4jQQFQdmvvImW46QadMvsSiLC3tedsDY1ytGXVZyc8zGQTSEqh97X3sdvkhrCx3s9ahFH6hrHYPjxS9oy8zwXiVcKbUdW13z9zycxx047BS5w8_hJ3JRRguxNhw8xnQQkFy6o5j1cviisnp8AvM1YfHpp2kRUSTID--YJBF5Sb3YC1mv_yvlR0r8fN-gsNCo0azzalN5O3YeW3rd71NjYp8ZuKrxaaY3QFRqoTd25TXCrSLLpduxcUGEWkC5XtonU1Y4tR5OtS7EP_2L4cTHAGcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIOy0F2xLJQ_AlP_mynGBmIvM1a7TqIv_cADJmNzrriZKobBjppCMVKd7h1Z31J65XrvviQEjoIehkO7pgbpRyhcBVgqPmssFBGDDSbKXv9zL_tnS3tH-P8ROOxaOB4eR6GXYtSev3oFWP4R7W170z_wRhiUx471-bv4Sggw427oGwypwVoFjVWEPG5NNKShOdh90pHnssFfE9kyNeCnKb1rdVdue3tEFpG9-xMEZ-LUy-8wjBN7Z-p7y0yPugJxU240NklY3pr_tzs7DZWzByYowFGOW_3jdxoH31SVRIpMjveUSVJdyCAvV0h8_a1aqDjHClUKAEx9J9VU7SetfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIKkvt5R-ofR5uHDLHlm7mezBnY0VQ8DMJs-GaYmOvhzpC8ZemXohcq18kf-dbF94i-gatoKX0sAGOzJpqGYDfscZNQ5g257jtM5Mt_N46ojrfqxHEasgO1_VQfBZPaKTuXjIHhpccyf3BMuvyLfh75lbA-cRTl1RJMRERX8_sFkI_j4QIn0TaO8oi-Y5U2jI2HlzUKbE9jpQxxdcytIr5RzvV5GRq6Mtt24vQXg9bfbSjScUnbUB3M9KQsOlZjpVKsaHlBUYF2dN_KLwBgXdyXoZO4S3WsxPqZz-CozhpTdr0zFeHj3NHLjTvxuBcOgl799FAJaPMYfh4IoaMwqCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYM-Bu8kVtBAv-tyHB3_DGD6HK_NCIXF-cEK2K2pH58SfFUFIj3ci3HvDLYg-gdbaE4IRwJ89dTPcck1MtEADNof8HsdN2o_HpoKs8rNv69oxKEChNUvTxlIlUFFAZXzE7T_WcZyuXd9qRYXInZVTn9T83E8hY_5lrEB3q_LLSaRxq4woz8Kw7a0-O4KXBi9GBR4QftFmhQLqRbyMhrPrDL2WT8mrS8xnHjBH4A_0SKQofeFpU9OXkHKLr8sT8PzgJo3xAuM0-u-sYMRr48lvVMgJvvwyNyK1J-DhhTW6v8FREm9u_lWUI6Yx_-RsW7cDDDaYhwy4bpaeqL9FaggZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eo_1SVQUR2K8-0JhSOAnTRFQOK3M4FDDeaFM1bFGMfK-F8WRpzpRQYbJzRlAoEHvBJPrxBombLXzjGGk99-nS4Exqpbo6N13hBL1qvolTk88c4HZm7lijKNLg0UI3DE9bU0fAgNCp7IbxSYqgncl3eWL-mBmVbKkJQca7KvTS0MvE7ONclZdjaLqK7lKBwNuZTAr6gTCj25mSZzbxI-S8xWiT6SZefJy1k7mswpFkqcnvO8knShFvmroeMttEMi1Qi0afBUrthnSyZeTUXvkAxSONCNa3R8nE2CTfnH4Q3SjstwUBTVTpqtpnfRtsGpA2tjRUrHesO2kZjFSvGyBdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bAo-pdqi_ObRkZSoyk__8NEW7hRt_wb8zSBM9dJtY7IugOtE-0Y9Nx8nJOKVNTJ6A4yekFfZjJ6FLlspFZDaa0WrUNujHSgMiwawDPKYls7xr7HCUIpcJ-iPnU_at4edfd22PJwoTGNo7Nqku9MyXg4XCGIBAiYk76RqLJO3MT4jeJqSkwdetPw8dDLitObyquDYw9RbEGV8gmyUAoqOangu6bpXQOgxW-sX_UIHIU18-YJWARZn7m2MzAXctPz5Vov5HtlPGKvxLI1MQSABGyOuKHYux-JgqYB-n2gUnh2U9elYKPjSonTLLXjtt5TPrnnBOsJP1lHg_gGmnSpxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iD9L7TTRlaYn0Gyv7PR5-nvvGE9ZJldXWwLajwPO6h4MDcab7du3TzWwYdM0Fg6r881hz4lSQqFfiFezjwyAY_8j89L9NxFpBMNst_ZAK1-B9oOtZZHgllgcgqTMw1LL84hNn9hoOfYi_JLUyETUjbrHp4q1oFxQO-vrTaN0wHwr4YVt4ASVxZcQtI_zNsjBokmq80JLflO-BaweK83RQMVVKv7Fi2-MtDewvYl_QC231mISaei3eerDdj6fOXdEStjERTAxuOvsNLwrSjBVM6o0UGecpD7aQT_5UbqSV493jFnwZZpH8aAmBNwaXN_NHk1c19FjMb0U9vEZnCAT1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=e0-oBumHSTms2Z5r3TpQTVcloHrySCJIG4Tl7eOSv2VyumtQqseOUmK6CRDkhXhnTjt2dWSVbxTSKyV2985eJ2aEPnbaI9KJGtJkmOMm6e_FK-2GAGG_r5kkrVfhj627rsr_gzDfHAUrS97k-1rfF3yc2oCotAR6EYWj98THaB7rJVu6zvHUrqy_dUjWMPwaR9UgfF7WR4WQxc5PPk245dFbUbQ5yDo8irQoB2cy4hTLNn_FfbokRQidpWoOCpGCvpLAb2HYmjT1ehfQZMXKleTmKYjk3-jFF4nC4X4iiZcK2ULPnHW338BZnPdpcbGV0bbk4cbf2MNxXQSeIYVHdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=e0-oBumHSTms2Z5r3TpQTVcloHrySCJIG4Tl7eOSv2VyumtQqseOUmK6CRDkhXhnTjt2dWSVbxTSKyV2985eJ2aEPnbaI9KJGtJkmOMm6e_FK-2GAGG_r5kkrVfhj627rsr_gzDfHAUrS97k-1rfF3yc2oCotAR6EYWj98THaB7rJVu6zvHUrqy_dUjWMPwaR9UgfF7WR4WQxc5PPk245dFbUbQ5yDo8irQoB2cy4hTLNn_FfbokRQidpWoOCpGCvpLAb2HYmjT1ehfQZMXKleTmKYjk3-jFF4nC4X4iiZcK2ULPnHW338BZnPdpcbGV0bbk4cbf2MNxXQSeIYVHdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=D5bn3J809RAbYI0dbo8FN28UFVkRXzfYJKrRA9Ly-YV7AGQ1sep549EdXGbMxlEg19SeCAnDHGRIyxAbLYC4ZD7SEPr1__h_TveT912sEWFPh9wn2Pi2fjFFHwLag1Rsrh2eUDm1HOzPAaiF0OF6kbtRohTCjVzgWw_5eO88eW-8_B5ha2OXx5V6i1l6tc7rmiDSrouBHaQ1yZfRiVBYl0vuChGoXln9LugsJl0cda5rQEJfxNU10THg-PhHf9uE4DIC1NAEUWnIPbGhGGHq9ekpfpkvsLhENy5sFlQiO3nwIzEbPhcCTu48cu7ZYaja9quwTCYZ2JlY7d6bz_4eJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=D5bn3J809RAbYI0dbo8FN28UFVkRXzfYJKrRA9Ly-YV7AGQ1sep549EdXGbMxlEg19SeCAnDHGRIyxAbLYC4ZD7SEPr1__h_TveT912sEWFPh9wn2Pi2fjFFHwLag1Rsrh2eUDm1HOzPAaiF0OF6kbtRohTCjVzgWw_5eO88eW-8_B5ha2OXx5V6i1l6tc7rmiDSrouBHaQ1yZfRiVBYl0vuChGoXln9LugsJl0cda5rQEJfxNU10THg-PhHf9uE4DIC1NAEUWnIPbGhGGHq9ekpfpkvsLhENy5sFlQiO3nwIzEbPhcCTu48cu7ZYaja9quwTCYZ2JlY7d6bz_4eJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI3J0uUIOxBHjR4BVkowetZDVfiQAkJJSmpqmc_HEoFPzXU0EAl1iK2CfooJTJhxGq_CvpApnPwOJRH6RtJrXubHRgAV9FV6B5fLHfH2utSIL2bUC8JZJzKZ0LvaTBOwhrdF_w3AYhX-OC6HU3J-u6T0-PUTuSRqKmbLk5rvuCtlgyLoqw59dacBemMWld0bfMudM4R7ytBV8YdgZhPu6SLMoAPnUfhPupEhIaOrRU1FshOslvuxcEHpV3Hj9kUSpatk9s9e2JZlEOJsgTSowenbuvo05W3V9YF8IWaikaPHbyYfsv-iL8Fg6bbyOMjYHAHTWDciZQVDVmlbM3xVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=jDhlb5ZcAufj_yBW5jiLyDlOMJN_6G2LPPcD9zFxxUA-ovSmerL-mKGSWqMh4gEAIBwOcXGq47d8sEiwIWdBa-eqQR2TT26_37ZFEUqVaaFsiWb56rmPga_PKRfqjWHZ8B3KFk7pWfoKpiHAZdsqT7vQUcOzJVqaXQBhtA5JwT4n-IYuF-vgRkdkw6qxDu9eqzYEUCVveTGvnwVc9wYxn3Ra4EMZ1_A5h5Hf695O4cRe1fR_yS0rjX13mDTNDwnarE9XDFZbjVT_QVmkjpWdeNA-qKf_hYcq8JI5cu_fEPxxFEdNnG41MG0XfrGs1WQvLvnqNuxUbE8jXt0rr78-9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=jDhlb5ZcAufj_yBW5jiLyDlOMJN_6G2LPPcD9zFxxUA-ovSmerL-mKGSWqMh4gEAIBwOcXGq47d8sEiwIWdBa-eqQR2TT26_37ZFEUqVaaFsiWb56rmPga_PKRfqjWHZ8B3KFk7pWfoKpiHAZdsqT7vQUcOzJVqaXQBhtA5JwT4n-IYuF-vgRkdkw6qxDu9eqzYEUCVveTGvnwVc9wYxn3Ra4EMZ1_A5h5Hf695O4cRe1fR_yS0rjX13mDTNDwnarE9XDFZbjVT_QVmkjpWdeNA-qKf_hYcq8JI5cu_fEPxxFEdNnG41MG0XfrGs1WQvLvnqNuxUbE8jXt0rr78-9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWsPHpwRxkdBl8pWB78gBfPu4uSI0mOTfKIyJ8dxSm2oEs6WssUvLd8B12xlZCPF_lQwdLSpzO34bOc6q9Qo3LpER2tM025XTQsPmj60qD21f2-aW4rJegzsjT2p0TF_fo5Jl4T2lunQ7MMps3zVi_s33bxJqR4lOLxjGGDl6kVFMp9londBBsS34lDzWLkrgeKMQ3n8krhIl6lMVo_83IOmqaxcvH2P4LEDwPCCOqmnrxA09PNxqjCTCVGrKdV_ftXyLzkiGMGvAQW57FwASgsw3IoaFw44DmfbaOg84ExqMs6zTuP2P9kMC5hc0p2ttE5CPY4I9aQetHot0KSthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liZMEZS4zFQaTjD5TLtmyoGrwZRtGmZED1FWvV6G_h5M8kJjT1WFGcMJnaEm7IDEcfxfzEKS-NjdmWpqPBBdORyO1JvkXMaHJnZulQP9ZHpxoYsaL5Qe6a6ws5FTHefq0Wl-iMVePD2lBxWLCX9Xdjm9tsJ8uqymt7jtyOxfK-TKiEX9RCjKml-o7slulV5R6048emTfY2WUKqberIQC58XRB4-2OizLDxUnbYRDDDM-QmscNAE4hYbEBqmvKEq4AYDDHrE-46rC2ydySmbochdUERmGv-ZBK8y3JeuxBixHrCAox4Oqo4pP_5AIj5wGftysltMunnaI9ip2EZzo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnMXaHpw3gsK79-DsN0_GsNsM2xLZBtEpsEnjor6mScPVZehEh7YRVy2h6-vsBsw06OrIB27CtMazoR6hkfN6mLZXbfF1p_XZ7ys44qbZBotFvAszNxKrxtaCmw2kVkggxXZU8umErg-gXT84Breqiw6OywKXn3GLq_emmwwBot1dd8KuNDuOsQOJFhWUHUaiXdMg_58lvJqVV0Kh7kGWPGvWXNBBoYHv1Z72qIIKkzsvJGDmbvKRWQVO3f4nFUSaDYBadqUnd0PCxAYj4dUh20TdIPhSdtSCjNQTpTLOzW6hKZcnyJlzMi5MuJRigQYSvog_3kh2uYzf4j7FpL-ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlxDEPF_3vTJ-etYGP2AC7JRKvUs8KLIXJYrMsKVH1BUCDzpzUWVer-I9mpYXYc2JYCJDc5ujhuYe2p6VClhVsnE8jul0YH2VTMCWyyYN9m215rsQsUolKQdOk5VFczWJpdVZKcrw6LtjItB-8ExHpzJOd1lWcHP6g90n3zJEMS3Ja01i5BxdqKDjAZT0qMYcmP3QL83mWmygTS0Ab_Gon4CsPjmlShZwiMcXcznF2oX-vv-H8bF8roPIlA0o3P3773sg87uV9OjSncTM7RFXnF3JNxBo-iUN092rm_oViz8AZPlfYEluSX2w4H2o8q3HZKsf2qiVy6AIykvZMVT0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kfo8UTVTy5DnBuplmFCtrKFfsDW9fFztV4YNqmxIspOZvvrAPImQDDfywn4Z9iSCMcZg2hGgT8hp_Z1B7uYNXW6pNgUvL5PTQ0x5TfdzeshOR1bTbHUpaTcKn3QxmhZ4p9K9Te-y34i_n0aaQNhrTw8_i6oDUQKCoXW9cix2AfJ1rq-Jla9Ei5xK68I8fbX6onc7Fu-1lAOZpDJDScjfZn790obYWDzOd1tAPZriE_kTrWVPTKsTHRu5oEs7G0YpnQ2-zD7o5EExpc9dMCzXserGM-ot-_BMSF7yRNBpLH8ZOmVGSzvoOLQkspF_wiEVhuxNhPry5X9ujPOwPttTyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=pkuo6DbFicLiEg1QLnlmRaCZ1gfbv6Dy0wY9Cl35GNDiTZ2ViqbWo2SqHw_LB1Z436zCYdzFKhLDEOjmtvA_h72HCf5OKc0NYuk0UBch7WPVIs7WjKyCM8Iw_nPEbaNeD1Wd-2C7QC9LGXvZTPJS1FxY0JOmGhYPCG7L8v1dN4ViWwe_Wj-vp0ziSuADAbQOn6YU4LI9AHAdLfXkyEZWNkLwwO0X5hnRBHy87yi2CUE5vit_0Zlbs0ovdkHAXYFGxtFUeERkqosIo6WR4uEPvlRvxtPeT2OxNxYUouSxF1weIVkCpRQTLA95BoBXJULRfWJzQPD-NKTXw8DIwYI2Qjjz-KoXWajIeOlrKgLdHaKgB5m8tZAYNk-kS2I-mWQns_8JE7qBv-v6oCwrkF-KjLy8uqdXhVpKI2yJdW6AWBJkOXsJ6Wc0p480ptsTpsE4906HorSyyptccuFvnHLHQGbC2MCpmRNJZ8W4AycQksT0jyaEOcE0wjtdFU-yHkAuFY3x0dCunmezqxhovVW7rU3eGuAdPCpDswEaRAnYsVvmqFPGPzGHt3dSq4ht1PcI7vYYbU_6qs7NxNC8TsI8VuIT3nPS4zlDo_m0RkPCBili-9sXCocQTjsZZYRMInS6wwC2DrydMCJdtVEGJ2ftuYYB6xvGus85jyXX3Bf-l_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=pkuo6DbFicLiEg1QLnlmRaCZ1gfbv6Dy0wY9Cl35GNDiTZ2ViqbWo2SqHw_LB1Z436zCYdzFKhLDEOjmtvA_h72HCf5OKc0NYuk0UBch7WPVIs7WjKyCM8Iw_nPEbaNeD1Wd-2C7QC9LGXvZTPJS1FxY0JOmGhYPCG7L8v1dN4ViWwe_Wj-vp0ziSuADAbQOn6YU4LI9AHAdLfXkyEZWNkLwwO0X5hnRBHy87yi2CUE5vit_0Zlbs0ovdkHAXYFGxtFUeERkqosIo6WR4uEPvlRvxtPeT2OxNxYUouSxF1weIVkCpRQTLA95BoBXJULRfWJzQPD-NKTXw8DIwYI2Qjjz-KoXWajIeOlrKgLdHaKgB5m8tZAYNk-kS2I-mWQns_8JE7qBv-v6oCwrkF-KjLy8uqdXhVpKI2yJdW6AWBJkOXsJ6Wc0p480ptsTpsE4906HorSyyptccuFvnHLHQGbC2MCpmRNJZ8W4AycQksT0jyaEOcE0wjtdFU-yHkAuFY3x0dCunmezqxhovVW7rU3eGuAdPCpDswEaRAnYsVvmqFPGPzGHt3dSq4ht1PcI7vYYbU_6qs7NxNC8TsI8VuIT3nPS4zlDo_m0RkPCBili-9sXCocQTjsZZYRMInS6wwC2DrydMCJdtVEGJ2ftuYYB6xvGus85jyXX3Bf-l_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9Yey6tl680f51h2WW_xkQbDco99I8od5rf-_OZx1UVlnUZd2Z-m_izjUjIQnDTG-zIbY-maguCTHNuOjDLB-fHpi2Um1f9YDTQpkSa7Fi7FUQN9GfbbsE9fOYcGh_ZewCecs7vL909a4zl-XBopDqru6wpTN7L29V1558j0Hkm0nttf0pl4KSRPhHRMo7mNDh-oBRNg8aT2jJbvsVUcgtr6Kq9mzLSIIOkBvNAdU27LC7bRLBs4IEVm0OsfE2liR-pFVLbPBTVwmHE2_j9Xpll13fuqP864UeZVS2Be-9juzsXUlrE3CXXs_nBgLFG56Pp3QMgNfmvTCixAIcBc8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
