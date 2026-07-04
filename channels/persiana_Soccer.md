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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 19:08:54</div>
<hr>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN75oZ5T0F-OObSMQgXqGLAWt-3jl1-egTT9c3egm252W8AAmyNXJZB-pXNam750UCfxXrLMuRcU-hZX-9OiWo-3w9DyJTjwrU0n3U_75-f3O2A59ThUIe_TKvLt-cSpMM_7YrZtj6CxXHd1pxCeltqK1hOk5p6oW__uOHFV_hgg3gMjAn8J185c_OqfoBYl7nhuGYYv3WJyP-VYlvU-5V7Tq5uWtERUXvdLOXWnEpKcssdzMSmV1iienWbc7Vpx6nBXAq0S2d_UpjywEMGcOkMbv-3zkxAZcKpWLy7dOjwC-ZzC1IQxfgUXrMBA-QC85DKzehuxEpWX-5-AALwqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-WmUmdg286_cJooLu7PatmI6avX0lonYjxr-_t_35Tn73TXZkuUjAnEMdrSPgIJtSUFI3-J2mC9bMWJu0odXhxqjbA9r8bXOUH-5h16aTggo80FpqzOV0WVALqlI5_H8fWaehGA8ERLLMhn1asit6qlXBb4iN4xFmok_wqfpnYcg2MloEOxpPXsJuhiI7BZguPE4iwZUsy66nWqZhBZJFCpT43GAk9Ik3_69xwx04sxbAjCx1SitM0QW58AdPtL0ini3FdZL23SA23rC-Kan5kROgSMu7khayRr84x2acn8usw0fi6oksEMtaLWsTMboLYoVDu9NdaHvNhPkQcZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSo3WN7yzIfck_C1kuwYcswms7lJre8YEFYlAXloPOBzC5zRG1iWxxGPCCcc9WlRiPFrJNCv9zIG5sLSVUShjPZEnJSEShoea6vtahK6_fRAdxKwTfsIWIhGD4NS4MP5sC1JbxEeKZIdccJ-tRuLF2JfC8P4P6_spc6XOxUJSsR6-Uv-pXuaULyLIdC6Whus7sGvPlNidqZ61809GnqaGCQNN0A7KVIfMbxUv2ctglDtXQia-yG-zr_hkZecfZCtHAyaB5itGos2hUmOVDT-uS2oicD6EfH2Cl9T1SFfoTIM_BOft0owechezM8yUixpapvgFBdYMFarNNq43VxZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPmU4iosfckwTQpg9MkMbA2IleHBvsPcDEs4LBbd-K3wOgq7NrINh6AKmThnW0hCzZdM4O-B6stXs__nx4mhcXRrUx7k3NVoVgBn2YryLrpjtahaEeb8eP1T56PbMN1R9XPeP56vNZ__80nonsZYHRVw5ooGUzK6934aE6bueqWbCPfy9rRTjgOQPv_bpkm_AMmmvt9DoHGqY9enxIW4nfYQ2zhkkD6VGnhQea8b5YThFkrMGFYVKT43jqx16aLtbf4oedDCOEvXv0NbGPH-zvxIDAH7ki5UYmGolj1Y91XBesA5JoqqkV5i2EN5deEAG53xGIOah1AdDDfC3derwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxRy2aWfiosgiC0Ea6pJaUOH1z1vddU0yNvUSPNTeWOh_gdiiYDdljrekMbcwWTYkAJUwwo5If1cDI47g8f5ZrWvuC3AaWfTAEtSsqqXqCMLfSsOA5lf57JRUeZmOhW9CM9Io8ZaETniH996dsGieyFw-AigWSil1bvln5TBgZqQhvKFHcDKwZoWOhbtWF_xwDMZIG0nQF8tbPILIvojJykLKn43kzNUrKgJkK8lok7I-4KxD1NVB5uUk6TQpF7O5oOPNnBTP7hBq7-PG4xPss5yldD5_VIix7Glq2mnYmZXmTmNZTvRcFyszLbs582Y03eayPIxKHc-CXrwu74CXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnS5x17foUZDgsOK8QlKiU0kEwb1zj0RrcOm7DjAqkklPzFoEtezHAf3ZcBzi99BxaR7fqf9lalMAJb_wyn1viCMJEAjCO2Dd8BTmeH6gK-e5NBDz_ajChmyL21rWj3-OECup69EoyTktbst3Yw_8Bsaregdqf6enwoQsjazi1uTNYOYc5rgT1LBIOJKeNp0moduFUTH0WKvfNI3v9CQF7LAdxN-a3h1wSKvMuDC9Rh6zlJvFYxFqXBTk53gpJ8URSDNvNoXC7qt12KYopiVJAKMdFhYCLZj5MFqUb6dbiWjqliX1RexEU6C0jHAtSg72J76i_3EFhIlBj71YiOlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOV1nlr54NAOeiHiaC1rdBwL8vhc8Mlx-ZEckWtqFgtQb9sBR0odf1KiehcaJcTNQol44b8FrutN0C5C3prHhhIU81-xjNf0E8HK0flWZY9r_iMI3zKNF3PbR1JJfz9MQOy13cdNNK-N7lgz6Zknuxj0Chyk5bi-YVxcGvxcopmkmusA30jHY6UZtZWZ3-au3_FAk3xGPwL5-Tkb81KhDxuRBrDnf9Ul3jebAf5Gbx_-6CW8S5NNBZnOuX3JG3GoAaaWHmDmwuVcs09gy1elCNd6q6daTgrf_iy6TiCYbS3ASrXhS86hpg_yBrv7JjBfNZC4-zIIp5UbkT9soDkjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/soDTPVQDBL0YK0UrQGf5wkj9l6xejYmKm4NwWh-r2dcJJwzAFH22u5ZYr8Ep7xjpRP9h9WvhobeMCywVqIaozu_BtHrsZxNkPJrCrW1bLZkLHN4aOWmFhftJLp92ewlu6RWP9i8gwYARTquXhFiChwyHgAl14eO_mv7yY0uyg10N4J1SEWF88to-fj9L36OeacT-XsXt0x3hdtLEbW2RKoAuFm1pWkghBbVGFRLL8-MVJIWlyUJkLSBnajeZKKh9_uNtP5sKqZ-BOgj1XpiRtaQ_IS8m60GaH3tccfFNQxxy5wOrM3hM4tAVI7CehsWEEPncKsxZ0fUNoZW-J29avw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKWbvH-L_IPHXs00HBdaXEc63PGQCd5UsILUmHLVdOQ2ZQO20msSx9LleoWRBLVWccMVKteRIJqpZjdkPCTYeWs_h7T318ZMLpRsIwAo9nJ1rpV1Tq5DD3j0L6IvYBjJBxhUVfCY6O-Ioc_Eda02ztCPlt6ZhgPl1uEX9sn4vU17zazZKyC_Xd5wq5DxAff_OoujgJHZi_O53MOZ24KkGUNratbJa34H-8hzHk9wEoXW-YcO3ovuTYCVhAGL7JFm3CNbrNTCI_HR5feia5i_EsZXKnzfESs6dcm-HUO09jAgX2ncO4TdfRTC66DmYzEgd12r8KtrAutZvWfOX5eXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq4VPisiGs5RR_qWpUj4O_lIEouZjKUGK0-Ax2MhzpIPek5kAE2sw6QhhVy7Hbn4KM-uXXwsWa-6AT9aNkUv9TkjYybp4wHPAisPx-8KQp4t3YbrB5wap9RZI_J7eRECpZlq4iY2PMF9EdjWJ-BYyyPCTuhdRbdmIsBRFHR68l3NBlFeRzBHjWEoTwg-YmLw9DEpsOtRS8Qcm1e4h5fzKVItM3VlBP86WOfpwnfMflfE4Psnvhc61Ez-iX0L1FFoAW8nUtF14tscPoRex34c3aILuDVZ5zni2h1qocTVE3fyCSXQFOkrsyWBI5TkxNKRV_X-qqGFWKQt89moan8VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOEVVMQFkJ3f8uIQddJWrOPR5TrL-vo23Aot9HcgqgJMjEOdlxccHIyfPFXFblvbIcn9APChLdQ4LGNBPgfIYiABgpSJ9F-h25eX27o3QAi83PpeYvZNoi9VPkV4KepK9BqsCVWXHMc8X3m7kaOOb7K-4uiJ_2LRZ4GIZtaJ0ozBv9cGySATi3Q1kUcSkPY2JqNkImMLx4ClH5PR-a8Azc7VQGmis6vDwOCX3u19tOaaF_O4sEKg8dZxd17B1fLknkP4wgPoXbokoK-jCPq013n2u3noMffxeQcO5_TjZPtvKSyDLaPXODNIv37nTTdg-2tGNCop7M00J5wyp2C8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejjR8KmeD9QxSDcg3D32hAmqATswLSytytuWZ02v9cF7EjcqTvYK-llg8ywl3TadooJGAAGi2-H_4dGGpCnIZ0JcfqiOkV9wex6_FBLeyqr2PDgZs-zgZgi2d-f7SF3qyh1Xf_rs-7b-Wy6jcfnVQ9o9eTfjW-MiKI0ivrMzmAe5hSxvQzV4eGLSK9MrcHBDqZ-gpZ07x8iYjplRhag12TBGbBF8hHmybN8hmbSwPXL7VF5AvHSdFG4dxpR96dQKwz5ooS1G9a20rqoaAUkjuGQhudPfmHAzHbl4nah3GCqJ4qyoZ2tt8LSl65GKlRUIwkdRVt69VC4qQWyDsGAMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ2AVPrtOvWGswWDe9bOlhrTywd97EmPNduteCgg7vW0Az7J15MQUq-f6MfyuagpIwgK9QHmnxDz9cJB_DGLwk10kdMp4JO4fWiJmP0q2XU-DmVrf9XIcof0EbXu6XZXC9jt5N9Znj8wug4AOBGVCOPwtBmup3fDZBovcu8xuOPpSplnUqnmyS0ApnAA_UFrEKz8U_rh_2ASpCE8JH_5RhcKMwTkcc0GWiHkbC44HwyB2zj8kN8JxibKHxE2FXj873FIhymxLru8WJvqs71KZg_8QaFOUxpacvUl49oOfxeN8I3GPFqUZzsSVjBcvphTX9eNpJ8rk8W8jP_BqEgk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRZmIF_azQyJHTdKoqBTG-MhOAH2x3Ip7_CiRc6rTmZsZqEXp3X5BufR8oQHlnVb1ObC0Ri2hCUtnicdUlvKONVeKvB2I8P3RphPgJe_DuM-qxpBVktuS6QoBFUCbxOQPaltvR9yOQFzizm4nM7cuDrTCOn3ESC_A_ZRNHIrAUOoFKv7jbAug1Skoghb4ZgrANsIaHgmCB_da7Rd7wZbZBr-v12GZBKVCy3MOvfzTZz76w_V83S7whPmrT3N2VcBvYu1NeE3ZAjOk9U9Mgi31fGcUNk7x3UvNJ610EC9_4Bpc4HevTBwX4qV6mB-8R4LXfGPs6DigV7Exp0G3HY5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BxdFMyNz1CDeKA1BM-MNw3G4vatX5PolSQyDmbLAByHmQXWg-pIgjbwof2571l-b1MDTtM7_6snbz3FOWZtnLy-835eqS69sIx8MLCAt7CISOuKPwy_XGHjQE5uu93R_ypjOg5rqlOeYRtreX0mPZWLSb86RFZkyspVXpCmW05skWdM2npcZhsPRTJriArFjwvbhe29Jsy-3zkIZWMepBcoCosgI_1oUAnhzEe-6Qpta1B9ACXdzGDFnVL-X_uvHZkfpGjD2Hw472aTIXvoHJtzUdoK3iDvTE_85ElJW3B993O3m4UAA_8Fy1Rvhmdbr3SUc_lcudza8c_wxRLUp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KtLBInV4F-JrTNqKc1KODLiOE-Yf6erWUjR-u2Fn_x61TFksSpxujX2r2eY-iQ3BIoCrqw3nJO8W8SCDhL7Uq2kcgJtvAxsw6s6Iff6nkRcCYuxRAMfGemybhNe9FjQaDqYWbbTLYxGgs7wlc5pko9kxAh3askt-3xPSh2zcRpIIG6si6EAwBxGviTmC24St9WRAkfVE7WZ7wR3JMfTNd8otJppPZ3RLx2sWrtFOlzidTxXk93PEHW8mNv-yc0wOZKZ5o4JSujxh8MZEE9viNpnqCbNkz4nL6GNndcLkQ91q4vB-olRkZ9o4jmUrH08uCa11y4OqIgVMJfpt4J7v4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbkK_1IUJkf1_veiWDw0kO7cfFYJov25sN30tPC79y2Xdot0KEvBnJGq_O4QaTgP1DEUef-Nldo2HqUKh20wbDR9aEcTBVVImknjDSTL82abrRG0mzO2OUAm31CB-lEKspo1pQug4uLrmPF3c-w83cXDtG9lM0Yq4MN1MqyUldd-9X2y7wcHWWoBtO9YiMCIInIF1QbFR5G4bl1qQO1hLTny9sbJy9B9JGi8b-hjKyiiMitoBXIQhJ2KCpq1KoMWyuSdQ-wZlyhI-D8v6hMihELnV09laP8LPZTfvX87f7jKAbyouiUxBsNHbwN38sxLG89fa5cmpiinm_mmR40Ruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcMrsEwVAIcmhPGJCCyUgfItrU8Me4PzuWdKu2aKhN4mjMUK6ojJKi3En9vgDr0pemuU4AoQOOXSg3tQweu2MJzahpXvUh4BjtOmqn5WReMaDNyOaZDaUf8qe7NJcbmsBaK4UQWnQsulyV6PLpgs1bCOUi9_xUsNgeu19InUoj9yIOwQfKx5AFIMYbipvObv4xDLK2ynO1J45QSioiuUeZQ3iTGJVrwD4P1xZEd4eKnEEZOu9-sZ2stffAcEBa4tQlPBlMHISpqM19pOmLx2kyrhp2-8TeuNqcaunduPmJM-aghqq4FadnM-Ja6AVvyh12k8DDxSGT6g9Y6-QBPL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHC5-rsS28BYvXNHyrj5CfgwE1JhGcLUve2zcS5R_i9va8EfquBijFh8gCFL2azAkHSK7s7uVmt4pRtNiExRaQ5ym2cLcVHN6k41cooPqVualk6Jris_eWDBNbaPpAMrI5WFBOiykaSc_qXGHBYRDRwFUF9Pvzr0BvgCeuc6glWy6OWjiX2tTMcMDntL6pDndzgWmRcrp76FWS3O8aJi5pcDOTTVOmZQ5b_MwyXH8mANx7ePs_wK-fCfHdIMcUFW1Q1thKnBDOtad2RwlBCueKyG25-kXQE3EwbdEwMKkecEl9cDqCGuj_hSmmD7RJNcakrpbvDX3ukXImdPqXlr9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9iX4uImYElAtMpBXvWtkQce3Tb5fQ6S97I_7rbmdrUQPzYrzy5MqchlkvtRkHJYPz2cXNh0z2zeNaBond1jnSw4yPFrMJK7u5r8EIuyyYxRq-1-WzVzKxsgxH0xGFRa-9HaPa8rxtSpw4Mm3DdzPl1QjdwLg1zI5PkIoGGp64cFlVSxZLNnbL1VonY4XblHBkOEyNsm7JJoHzKXlI5xN5lDFcpCara_iTupsbx4SXWIDGTohZVGfeY0Z75xxHgvmGsqQmGu68XSafEqv4WBQFBAOJ-YdfKiywtqpcexZLM2Mq-hxmPFwiZzyKJhcE0uYltSDm3rOHRVPa5wD9ZWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnMbWQ5dOheQdK-PMPrFEbY1u8_DVYX2OXA4bKAIcz1BidkvO_5Jwm0MPEqoVgtHj7BYz_OuSskI0v7Uhf6RNJtPsIwsdwZ19XnXlD_WfKFVtI9fhwNSnIBD82pI1YYdAt3yretsUKzp3RE68rJgRR9WyM0KmpLRMTgQwGG1cnyd757iaObY54g7R9fJLByHAyRx7iwEPSIxgc9-30vBLOPEos-3U0uTZq1bqMoH69MvG_8oJdOC5lfhlIBMmlm4gAKKlblJmXhuLTVsKcAuejr0TGrz8vO5MkSDaer63bBswQ8_zomdlMHZEMQqznZ2wP0jYd25-38aJUGVAf1MqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNAtg3kUJRg6Scns30mR-KzdAZuCc_WV7zVziw-Ki97Yb8QwUyv4ksmmiXa2T3wTnVIz7AhdBCIWlbfeIdaBOo9v4sPL7L_4D7_04k7kMqeMtQzy32u9vH-5uNtDmIEB3nlkhUH2mEwrMUGBK9fvD6DEraI86HOJuhowi1-UmvR6J2ladfvx9x-2SjYj0qVKEd4nIbXNSClB24hKKBg2iCG2CZ7domxsEON7tLkX95cTwnuw_YKWOWyKHXaILkvQgRzNG-V7TQq-ph82zdOqPxwi9V8rQRb7RSbq-jcXX45Q6DC4zcB7L94y2oI2skrYqFjhG-o1oPAXEK8HIecnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/but2wGEVpTys3ug7hC90Du-HvBWm3Sg3IllQBRQMq4YGn0TWMIJddoGQl1Dd_jyUUO8XuiAJ54FmIjsu0lEVbAzzO6D9M5cnay0jpEiHQSIYTw2RFVoJ9qeGdqEE7l_E-56KLVh_mIxxRcSpUB3Q8rHlZRJZdjboBEqUmOTv9Q-BSyFOrtuKpVAb-ft8s1PKBiiOvWS5IfQxsXo56E3V32xLwDDIrh9Mo7N8IkZZFAFjNJE6tJgBcNd8i4Zq7pq3AcggJA3fx1F61Xo9oY7Sr5_m4GfRnNf9iM-OfrOOniDl1E3YYZU-DKmNnjJ-5PhKzbukqMMo4BZaR-Xls0IROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZaeFnLyqMB3Eb2M-VlIJ-53PDLAKCGtgHrgooc2n9dEW9Z1HAQkdHUVkNhhclaJlDBJ7kAb2f1zCHp5z2TLVI50TSEFR8ZOQPmJB9bPHcePj9CattOri_o9IcJfoOWVM4g9uWGCMNfKY8gplruvlB7DdgnoIs-f0tZllaqZvqM6DvzlwxqJbsYWp0U9NjiNvAE2Nd6WY0HcQscm26pjmZFYMTxEla37ABsfherhiVqzSrY2k9yktNErNj5qqSuoThxv0KYxH02Ai0T8rWUSHdNA66d660Ftkv_oJ4B0XEnSp7ub6yOqc0lVENI0vdzbUEfBDMaNBeWtKy08rwEELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24924">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24924" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24923">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24923" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYYoBwytKJrYxAbDLoPq-7bIl1mXj0bcpIXK7_0g-RJSLb0wPiYGS-b94EDR8PhF7a0I4VtbjvMw3URhJxUbqm-pmMboECa4TPRWbIvcyhZUlaTRi2GR2_eZzMS6kzwS9ivH2l63meDK-1qlF2_A1Ott2itwv9cUm9Gl-XqCrFzV9tssjxvqo_1V1PJEWLSM51Y0tKJ7i7z4pDnroaQT0wpbthtQk3Kn7O928O_706IzrsglGQAM_83wXbKOxm9gOQIUIYfGnpqCVUQhqMXMMKN5M8BKuyvC0qTIvPfehXw4Fg4iMvoqZajDmbFHrlWPL24nQNFknpkrrkgGNEEgxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFyaUQveVZloUrBpZg-Z7w72MdLvYgctZT84J7MKP0jarrZlACsKxxTjMUicIl3a5FkG7bXxc3gA1tsmP9-oUksuyaz2fKWRr9gdQHwcZL9JSSBQgn77zj9pvaymGmR6nF0QmaJkSEE9KuZtMuwV6DV-drLOirmVrgGsc7d2b6Ir-uTGOuCLJfRvY083r01JxlG6XVmAbTf5W2urPbV6d0iKsUKMGVbrxeFsbGEVv2Lp98OeqrPt7lRPe3H1rtEco-yKIe0Hfm1XI3gcCc3zwvR2vnUClWuXkNd4cZIZytAD0OolBV9wOp3F72LvhkOpw9OYg4fMmpASVDV5VUisjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0R7_Ci7imJFvwzZ3A9-bSdr6B63g9p4bStSSkHj3KB4LCTFh_AOMvdtgwwVkkepLc8mUojPKrz1USoMBeHS91GVn6tPxW_yZ4FNdxbEnKNtz6rHoTRaZYHEpPNUbVXKV55xZpDcnONe_fko3JAbQG5FQBqp0IvdGm43Qu0J_yXn3hLHciipBecsB1hauk67bfGa084Evv7k8yaXtTjxQwhsrcrLj63Pz6iyakQgX131IB3muAl36CAJms2AOI9C--Bis7W0HE1io-rhAmd_w1G9sxHnlm2HEQEV47WdfClCMQhZzv_t3gumTqs4IR3HjagP2rHoThTk_1VZesIDOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL1OS7ZTkl-ElRrAdfvbadmVGR0ZNUvYLbuTlmAv2zzXB0YG_KZ6K_siAKn6btsR9UdFEZOE_Ea6t0UpYYm79Sw3bVwdv8cqMd7Wb2blI_CnWvcgXmpBmbzBr_988Jl-69zyASeUfyy6Hu8p4OtUuGk9RPqRlx4wcgBIzOFRFGPswWCRo20KHZuf5z2FGlQRB6vtObvC3h5NzLW6OioHbDW5wfa_1vZvOUVAQnW0TpUfTz-3GTS8ugC19hoND-Z1qvGok_6jLU8vrFRic-s0NP8NfIeQ5xjmKxvvWg-Cm0RRejFqEB6goSbU2oO46dHVw0ufEfcX_UOLfuJtAldeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3NZRm5eyRslINHkopFek0rx9W8nRLzJN7S79rtiMHOSP_S_UgsmNV73AAqr1rc8_bcCK8FvUPoJhGz5Chp9CqxLS3Cfi31JUMS4MJFwYPl0_38pwbrGoMK4n6eJWOfplx72C7n98E6cPUnbC-_D0PRujDNV9eNv0C8dd2it13Kb8gJJQa9GrXX62X_zkr5wwWf0-BnE5rPk6JSUXI7wSRtqNdYBcViUsxw60ztScLU28zCpIfT_0UQEgXESmx53R5RMj7fd1nzkmkKYVVl79ELdXxYDLjud_DW2pTrH-mOHtCimX0SqQWT_GaNNQ-MAWrKEt4AShLw-bektTIfptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZxzW415wP4AawZ5ardZEXWepVyb4dnfATLy9J8XKHe6Zzl52_AoolR6LbLww46zq563lbDd_1DBgh52hQn3K5EeU1wGnuPqNmW1KelX7LpW99a69Qq3adRmhuQZI6qfPxSPkk5Fez105jIkkPdopcD1mb090QF0em6ZsAdelyw-RUJIHcmWQAvTucf26rdMCvIKOh5QsWrrmJNLFu4fZeOC3wNPL5Mr8IHIY3999ylsmeL6mWddBOMZEYnPVGVU4HEBKluVcfpqwmIhRtxWCSNcepvXngjCTLHgsXI7eQ5wY2Dl419Z84MV1SKkQgGM-u1nt237HUNTJGXfZxIpjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLQX1veGt-u2q6kzrvfJlgEPgT29zC8tvH7hqCcj00-T6swX7GIb3IilQzjQHGuMQzxKQpzfhhDbp95kmmMhMGDX9tpMTSzU92BzY0TftfC2ifWuF8DghIfFLyGQWbhFSjaRbyeqfJXqSZ09xb1pEtJ1GqJmq8N-ymdyeo6Ns9kXxoFIf29J81ZAqN2jD3L2mHZjhpLa4IEE2G96gY1zFdWdvCIYzCFVpC4xd0bd1s1so2dS58-F0IKgBz_0GLlTIRsXURKMNzP1SgojzNcZmg9VzWWwR6CQrWWAYSEq_XPup2i5NrXK0Y2mz4RXt5uUU5GzgaBytqRGi-5cW2-Y2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7arZxU0367crw8tpfsjlbju6i9mozeW0zJ0nCVh48El8Sg4MeUIsqvo4hQgwgdOg6DvsaRjedMK5VbC35AD7DZfP51EHVsxkTUzTCfojfv7mjMHuMzY2AS6k4WUoCdI7Pw4IL6szTeXZeIHMEFJiZfF-MsbwZiqgbQDEnnG5CZuGDk712xG1EuCMocsAmu7tmr4iBH4bTi5Y7AnO2i2Hlcu38ox220xkrHIbYDGHac76YfUEe3HsdVb4d4-9ex8NEfhJB1yh8o_Bad_4XhxCx9rIWJg44xmJ_eTjVuVj9_cUksWLzUTyldYbsrSfoqZUd3iA2nBDLyWhVwvjB6-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iml781wG7UsUxiSFzC0fLY5XDvdBpM-2VBJK6b1u67RozUcJlmrOQaMB45w2rUBJIShciHvwpyGR1yu8Pyy5z0YMfC4KIJyRSxXoU7riPk0_EvStf-aU7iiGrDQLGol7U03Dknrn15UYIZGUT1pwTLvwCrFFLddSOBhcRS6NNDO7GPJeFMxm_P1cuKwEM3mrsWEN23KW6yjthExVwCupqPd43luYu-1s_BYlpkIYRplAjvlLoTlLS9j07vd07oQVF8aFpDI0xnWErAIFjVSXiYbtzFDqKCqQSPLYWXGTuY6ujjMqGQxfIKaKNp4MOpfCHCjl9tz5rZRJzwLcKfmcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNNiV0syklUfD3x0sSxqLxg-c1-gA4baB0aCCEtH48I4G8HwSa36rBXvU9aIczcYzgREqvFa1WbvvzM0LNRLxBt0A_Pz8NMYnC8_QU1VHid8aj_-0lR9YVQ2YESsnegblBlnXwcX-0atG9XWloaoi8YZetmbsa1ptJ-qUyFaejdk6nl6qdSwlEFsEl4NbMAbn3EAtvgDfu6LMtFKwEMeVFvd0wTeGD3pulYx8XfwLbbhaCMybBuhvswtxQPyJ6-E6wqDX0LtFpDO8I3Juz2XtvVsdV5L7iBIhQ_qZJQoQ-SRy7NHQoe0eEmoXQhubSfD3GOQTVebqxWEemVgtioUng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVx-xG0bHnz5MbCJhckmmiM5ctdK5y7fuUvtyDNwDaJGwFxfiTv0_MTi4fgr-pDcWdkaZw1HO5kGO0nyt5P2TSTba-M7xhEDXMWbfMr-bFjb4kh_RUJbNEDXrBh0_5UNU4QIoDIahkrSgxBhVAvuiA-fbwMBoASQnPUvYOJ8BBqlx-SrWDbDitaGhh8mwbwogNMLjHMUNkUkWDBojZ6MRxu8UcROPPtrPzeEkUbFeaMh8grk2ns9vOELFhdWEqfpw4fLsaaNoGoOQLYCDQ_hBMc39tEJgdoH2qqe5lLUnsSCGNrGqPuUuIocu_itdLkJlNiyqTtw4RMSZ62wjGWx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUsuDSW9qfwWC7UErwefQo5wq5ibxe3dqE6UtKuggZ34D-tqi7Y95QdhOyoiUPck81k_SA12WhluJQIyN8g0hsdF6hPWfjpsoB5Cwv2m_IyDaPGfaV7YDSy8MqEY9tIeEnXH1dlUu5fbIjnyl6Akp2BKO4tLznIe4ujwURKSXn8zmmdJRAkUeXeSe4R9S5ZfJCgxoXRC0Ccn-UkvBbKBBjQsEhY-sWmvBLVyht7iF7NHMlNYHX8ZN4J66Dp9SLdsxXDIQJgQLCkNml9Noz0wUuNiDF9dQgsrdD7YSdcgLD-kDKp97h0UzqlA89VIhzPJ2S0SdcKw0OE6OKtPaIcLQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWa8SXLdJiYVKJMiJvg88k7UGBCDuDKHBj05rAfeiiSKEo1jI66SMvsxwHmCvwP0dQJHQ5s8pOj9QyWGHR52W28922kvetsRwdpMkTMCzJZNR8R8utRRBT5Nm34DHjO4GTsr-sZMkJmALd9LAaVJJGloXeIazAxu986BP6fEp2_PuSdpBYNOHIXEJvpTHygvx0uDP9AyvAnDZtPwii_Cm6D8EuamnZHyAel8drTbYgwPq93C3YZkUkamR-cOVPygGD_wjmVoaQTHY_HxFJOPM6s7SL_JRoSyr8MdoqDsutFOyCAN4PjEDTjNpEUXcGVnPtNv-foHkAw9m792WcetEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLCye1hv2wilsV2MdCeeznItd5bRlLnYT4r_LpDb5cQQQRTi9PvJDr8izXKrAbdbym8igN9b7NbRn_SQqWzNoit6Ds2H_Rqd7P1TMse2EJxXTs2t3ezEDRejBEztZqHyCljv3D8pQN9eHRxQHZ1iz9Tr8ZwlPtDhgWqBqU2Vrcc89DVfMgANLIP_XtW5baDqg9PYiGrzebCKBBbO5Be7pD5-BFDOEAB7f4Ukf1Vdl_udoM2Iv9fem9J-HGqJqxhKeLWj5_UugS-K9sX0OFSCOmed0lRxj20s6yBMFCMaWQgX7PwBv1gtD8-rsW5EK9A0tCNtLcm0UqrDXrewCandVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xo-RwQntSWMfyZKTTihPx1w1PCgqgcctxz-OO7-x7tyF5wxRC_8eu6ZBlqaCbtj6EB1ZNa6VjGPaGmk71GQmDrFXWsmdRaGCByFwCwy52YStG7oPsKz0mefHCD3vxYva5Kh8yEMD6sf38hQ027-1h1qI3_8OXR1JA61XGf-ZXFzLvAHliqtLRg26w61_EXz4we5J10lfRZJZEQvyGX-W8tOGW00ZwpfFNtCwAubM7A5blAU3NV7-JdBYn_hovbGM7K5ihwdHwWfjISJwZ6cTa6F5O478w9QDK9rPHNfTU7JSV-QcQFTcPqiJCnhdQy6neCwTnERi8iGGyq0HBlW6DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdRiMbYnwfW6nR2KBXrlviTWGsQ0AqX0OgqWTqpFxzlCzHCeRUxRXzTC4N8dAPN19IysNWbdij9hRBaskF-KQhTc8zEshmaWOxXEax8tDJot13mbaAWMgyLCzixOqrEkN8ER2vSiuWjDel9c63ptbqnhsFlysMCSpjIUCkpcbQQA342uiH1bk6qMIPV9i6u0GrRfNJF6i26kW5sK_BliAxjXkIaP0E9mlYWWATz1Z8NKHzBkU0efxw4ZwRM_c4E6EaY75p4hMqYa2KANuHDENY0NTeE9ScFsAhdeAc9B1RxkxQ7UYBqN1PFqvCob99InLrYJ-uAPyiKAHEtWy2t5SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktggsuQgkEiBQ-rJE9fUv5Kw_ZjsmNeujV1cZrRGdIh9_fTDSiBLcfTHD6Z0_WSZJkTBTWK4qqVcDNY2S1Ffh658naHXz8qV5-Vxca2WKGRasrKHwDzbB3WEDPA_skub7kLuD-nPlonCflSSDONa9dOpvgG49jSp22ooDuShE_OQKQ8jWAW46Xp68qaEOqF82pRM5uCC30ApW77lJ5lMCXPWcNULFYMiQIPf2DtuES79eBjaGCQ4iOn2Kz9NSYizNgrYYoyNNg_2Szq1p_DvMCcIHh0eD32j3OSWpdHCC_bIdhVwhNIraU4kaHYEsgzIYFYnZGUn8FyrChSqietp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTVSgfGxUAtc2AMurLJOnqvhMNU42TuR9m8VVF-vl5dys7TVOmwN4Y3JjAO5B6-U9FrufyX1A_2xkG1IvmvbCUqQsh4DKjgoYYB8x1H5Jgh48_5P1z1JmXOQBDo4fPkzoYtb2T94uArKCvXjrCwCMtE71YYzvQW9QTxbYYAyGMb2yHPlAjNU2D8PR9-zVam-yfC9o_XjzvM63pSJ2wMhmmlP1CMALaidDRFZfjahw3SSHzlzcUO5GEHVol0HqZYIybsOkLlOzEdYQN5euYeRezvdrFo5t5YORWBFfju5xeHimgeedsLCsPJEqUHasl2USm36m5MKegH2xnJFu7h2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWVh_5aWrhvEXLWy6ticWsRgD1ZKnSGOpjvjseSigybufkp-k9YZtagl387Xy9FuK4dnrPNFRnNb0rnx1kIKKljZ7f1S8hP-DRwVv9NNNc5tWc2elrprOQbReStwyhCuQLCQzzTcQbY8TvaJDxYzJk3LQ29rdAshWx1sM02nMIK93bjGqShAQxd_VEZHgfsLXt21WRcOm4-VKXQQnkonwJx5-eu-2cXrfXi568bv6fw4Wgvfbic3WC35_WfQSkAUpuPpArcX0-YaczFB-YBjfn-wgB6GTyU5xcE4nj9KGe_QTKyOFuxwWFK_Q15hS567xw_iB9FrU5mSVakYfFkLJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXTtce8WFBisYg4dlQa_5aRYODvWvciYNlscD6tUnAPifU59ErHDZnix3ETB1lXkkKhavgPRDhVJoPtguK8OSylg7xlwNpGUWYBnywGLySTtLicpUv4f0SQMzNaqnj__XAqkqclui3ZKUowhpf1-fVxkL-_vmeTQtDZ3s9Cmxmeie-K5lZoMVC3DjusEeoawXloZaskltQ8Pr9Ql45XqqZxXsLhNilycyYwZdTsyqlEdMQp6KMA7RQM8oVLU6OdxiSH8nVd5-PDAgzZXTXpBu0O4fjZI3L_vwckPbwwT1pWlU0_DmiuodlhHB_dsb9k9adgK3uTyAwyM4_i6AtnEQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-aDXsBaRj3ApfmHehpdbUEK1HAYLVqm-TsnfwfpJkGLBVLwCu_-jRWcxfFfWTRo18hTOfTPdJUSAMea1T-OEPTC9uKH6MJgX8VJ4AtwkGTxV2SqiCnIdzQITVZvFJQpFeGcVG8xM5e1--El_hxYYTlyFxLmG2q3ReCb5aurC-r9Jgoa-zDrNBwTqywkqV0GR5UXAvV_uLWD5CA4CBPZGoqrjZLTBkzalMhS1tAIFky53wdZtxalnTIS8GuOGc9RnAKNwYWGLoOEvDkdWyMoC4fgJ1XSveWU_pAhFI_91nz2rKmOJyd--JYIn__WirpMiF4QB5WHtHZtR8rFUJ_pLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7QCaqei5ZrOycDmw6yFurldX-ueThE-CFveadG-0y0WO4y-0G5K6rG6n3-52gLm69hDG_9zlngLjzkRKOVyZ-aO-a9D4Vxx8tLK6b5cevuSs1pXlncroeLeoTH3vQPhPbtjf1rCpuCAOQcv2pMcmm3FavLhvsUKPID-Raztwr_G9ZXFq8OSwa9Nmn1rcxniWKVWJ0K6Yc1hBIglvNYEwi9w9nR_BRNzA2o98hw8Rl7u6Pd8pXaR96Sk-I4odv-QLcLZqTT_5JKgOLyyERDHktTr1cq5EmjlO-eKvjGpxPXcxLMNSBrkopeHsuTincXWzBrP7OPopKcRaBF3a8XC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24886">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_WUjY2ipFzThUoUf3FW6ULauQVppJuAxKaZhJTqyNRgGkjJr6wnOzuZMTJNouiVjq-vyeYtPpBFmglqwLzIF6I_SFhmg5AIgr4bFnpCNctwLjAkYEDCBB2EzFf9jXlBVXfgD_tyNcxkxeD6SYYy_lNC703Mx0TbaZIIXoFC-ek2Yas3ygW7FukYRjNTVuGDwYR4mZ_YQU6tYhHifADYlZoWbRyxx8vHoTnVYliA8XlOEl8kldatvA0R1C9D4af9ZS6d4hHUMFVnlbhBpwKvnkrex2Bxy3s7hrQ6mgrzd56csn5KkBCxYh6sr8D1PW22ijYKmBDQbGx1ov-KpXRQPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24886" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaS3_NppT12n6OOdMJdqjdeDLxUui-ZYOeOryZ4TPsTnwQCjkI4jl-fc1Dhx18S7Bxsm8oDGyp87dUQeNQ--feLqcsFU6RkRD-MCTUCvIaY8RiBfSV47NUvodQctYghZ3sfjTQVMLVQ6Tc27ptsffqmdTf86i4h8UMB8vHU_jhLsdzublsFepZ49E_A6sMgC_rld3GsHx9EjlHYSuTgXOMmtMIluBJNLNwrB3RuQgE-r8qTT5DviGLIwFrxXFl4PffuyFAg0nHytZIfuuMIZw6aNSE0L2BUOgbOokfX6XPcSp-XNdTDeiiH0TfVCTKIpmuMi5T-xA3sb0HnLksvdOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBWr_Tiw8MWnk1ZRGpCYIimhAm472eTGswDYhBWyv35b4OWBXCklfaivUvp944RjGcTSPP91hqAH31N4c4G0Z4ytQN2tWeJdkRCiMR5GMTdkMwZ2ytJZMNO6UBJgOkJRsMknS2JFqRflKhYOoNhBaJzH1iQQFmiaM9Lk1E7HGNxoWr2ptd8HgqJof51_50QPpeMmrvZKnCI39Cq8qZG7oieGHtxeBi5edwGE4z0-8z5u4x1hkigZSlPAt7ifWbGt06ulycyAjUBXJ7F-w25w89-2xwrUGweQI2AnleXfEekc4mxsH6iY_wgM_Wkvuq1JB9Pwv42U2u25CkzLwditMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=R3pYVJ2SwAdPyEc2P8ldyeJuFSfavFpi1PvwSDEMl39zCVqdUfcM9Dyj4fBpIUCjs7zodmtlMHQp7cofLIArpUpc-tltDtqeJbQzLUUEQtla-gfi-UzhaTymVdo8AjnRECCWcYXi7NL56g8IWKWAv855Yox5Yrz_E0gffAz2POd2wyyWqfH7irDS3oo7VLfyaVal_-hdUtSrK84zHa57wpdlHmQXWody7lqffJBuWqRDAtTmEloIdrDsoyyKj-zBtHvryTDCHZzD9-9i9Tlfq_6wr8IxhgZS6GY2K9t8snX7vjYUPBojKIxKUbk44IuUuI-QmnSN8vXjgBWW-W1f9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=R3pYVJ2SwAdPyEc2P8ldyeJuFSfavFpi1PvwSDEMl39zCVqdUfcM9Dyj4fBpIUCjs7zodmtlMHQp7cofLIArpUpc-tltDtqeJbQzLUUEQtla-gfi-UzhaTymVdo8AjnRECCWcYXi7NL56g8IWKWAv855Yox5Yrz_E0gffAz2POd2wyyWqfH7irDS3oo7VLfyaVal_-hdUtSrK84zHa57wpdlHmQXWody7lqffJBuWqRDAtTmEloIdrDsoyyKj-zBtHvryTDCHZzD9-9i9Tlfq_6wr8IxhgZS6GY2K9t8snX7vjYUPBojKIxKUbk44IuUuI-QmnSN8vXjgBWW-W1f9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LW2PDG7D9VyztTSzfZNtsIjfE5_crxOXkdQdcbZHDoltnsfKdKCp3ISxOvOfTKC9l9UJy28FPmd4LBLkHC_feRfTYoCqT4mCTK-rHMtc1z8NcVs-2aGoxKaU9xMoshDQG3smNOEbE6NYyvgV96CT6BKvR81yM7Fgyd8AJX-567gsLdd6j82IahQv3u2iR0pRwPI6yxyaxZ-zAAWK1y4FFAMuJWlBjPSSaY5GUYEQ-KqbrCkyPFU4ZaoW_qSqTpkjK6YLljAQQc3GJva5Ku9yCYv9QiwDyKIhZVWxQ9uCgnnG40sJ8-Fww7ZMRSauPdtYiMX9YHtIXS3ppPGvsqli1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzJKHfQA_vjKyCIarOj7STLgibCjW2GTjc9xnGPLYd_nQ9VpVg30sl484tiGz3KxXOYcvNZZcjLXZ-DDduZ-eFAdm7nyFvHgWzDOd0o2Qvabg_eQtjiuJt_ujAOhHvtA_DHiq4l3oGavzhoLmFQcFS46_Mn5O0WClEirrWx9Cgg9BgxHlW_tOSxqLeYvYyvJ8PJq_iDykQeZa0SQuZ_o_oeBl9Y3XLlhG48YFFh3AX8jhC_0nA_jSZygjaRcNwUnAzY6OPAQ_pajiKxetflxh3fDLh7cZKMsN-oPTgVJDByHIJuPGRgEy_jxWNz1u7RUugtfRRK9fY-qPfEwZVVyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-2F1RahznHXHdKzqL_QV0oMkbBthNBW0yDvT12N9AU16QktXLJOGKgt8KFjeJlP3YbWfKIS9k3zlyevl2-u_87AQR2ieDSwCovfqzS6dnsTyaDstlIOpWGkK2D83sMcrguTDqvfXFfSe6Cmu4gQNFptVWdU21blltMC18V4hwLwCHIpUaxkAH0CuSjyzsnmHohX4CsIcP35BcgDnYZxO-mrtMVepLy9_8Kj6Scb7DtVj85-CVmhElvG9zCDSsuSNJAEKY_S9YDt2KPz6pmeoOZam4NzvUjqO1wJ8U42G1nVW_D7_4_u-nrRxagAAGBDH6K-cpyPllWevQcWib7tdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=PINbJepIdq2jZTO4Tc2YG7oj5EjQcj-FZNHLrKHNEZsdLmdcLcLfM9rSc306_Co85ZEedPTdpup1yI3CLzuid2BMq3SaAT9FP60uWRIJ2WY1LrxtUlYoQv-zscijGOfftVP6_6muUGjGpoCT3iMnZ8Aqs2M4cdCvtd2WfOPEJ4MGQi4LhpZds2KnkVkqqzJ7Ko513axP6krsrJzZimGwdNuXGPIk9xtzxEV_eKmMzo3VdqGYMEKePSR-LkOJVOlc8vvS-KgEGMejKpVAZyvcNpJqZhmYU2-SvkK8X4t04zGicBFYA8NUO1ayXf0LF86qoXdh9rahc0uS54NnGahiOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=PINbJepIdq2jZTO4Tc2YG7oj5EjQcj-FZNHLrKHNEZsdLmdcLcLfM9rSc306_Co85ZEedPTdpup1yI3CLzuid2BMq3SaAT9FP60uWRIJ2WY1LrxtUlYoQv-zscijGOfftVP6_6muUGjGpoCT3iMnZ8Aqs2M4cdCvtd2WfOPEJ4MGQi4LhpZds2KnkVkqqzJ7Ko513axP6krsrJzZimGwdNuXGPIk9xtzxEV_eKmMzo3VdqGYMEKePSR-LkOJVOlc8vvS-KgEGMejKpVAZyvcNpJqZhmYU2-SvkK8X4t04zGicBFYA8NUO1ayXf0LF86qoXdh9rahc0uS54NnGahiOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1mxXG9t1gQWX-GAXJkkx6D29Cc9iecF6nTRFzw3rqECTxNEfaFQZ8_m_4wC10iwLBVkvhVez-Kdy8NdJod44JH11gHBJbwWwhjjLpLHB27mzMrU3YtaKlYDPtkt2V6sJq3hy3ZB8-UePyeuVGn64qSjWtFeAyVLWqZG1mRCuoxvSIQifzbcV7jnErPVvuLMQFx532CjSaimuul7ydQZ880372PaaXlNmAB7fxjVEDvtPTk2fUBdE5wPLronaqjZgwUCVuUBp6BUAdsxP6C0geg7H1rfdZ25DbhqaxHZTFUuffX5WaOYPosUQk9_MGoQtMS0TKCuxoZknhJoTCKvhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=tAAzU8qgh8YnMUz73C-pS0cW4eK9l1dDyOqJt363UDKWJ2zy-U6-rVoVwoOPnsrDuqmmMv3sGK1U_ec-2Ao3UMP24xo9zZnCPw1a9v0eWy3DSFVXV2gShVHDNO6qQSl0jpzOcqpVaaDCmA2HKsEuPatDauAzYJpkoze5QvTwHUvMAKqKV66ctdKHE5olRf6HAQ7yk-7mMRo_haQnfT0gG4TKuvjauF-flpHEzKYoCZnsmIiti-q4ZbcMA3CvzgzfIppSpU_v74hVo98nxZpP68Apk9GjD7AcMZVxnvfnb6pz7WQXepyDvM3aRQK2xtBgmHQ1sZM_DM4u5t4_Or6TZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=tAAzU8qgh8YnMUz73C-pS0cW4eK9l1dDyOqJt363UDKWJ2zy-U6-rVoVwoOPnsrDuqmmMv3sGK1U_ec-2Ao3UMP24xo9zZnCPw1a9v0eWy3DSFVXV2gShVHDNO6qQSl0jpzOcqpVaaDCmA2HKsEuPatDauAzYJpkoze5QvTwHUvMAKqKV66ctdKHE5olRf6HAQ7yk-7mMRo_haQnfT0gG4TKuvjauF-flpHEzKYoCZnsmIiti-q4ZbcMA3CvzgzfIppSpU_v74hVo98nxZpP68Apk9GjD7AcMZVxnvfnb6pz7WQXepyDvM3aRQK2xtBgmHQ1sZM_DM4u5t4_Or6TZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9crcBGbhp--2q9TpOjwrmMD5AfuoQJ0RhdahC1abSZHMJUj-UsPIWVmiv2QNg5749txm6aaK1sLo2L0d-EVYc02_3G4Vqj8YNGX_ctQV48C3jnxgj1CmcM-P8sNxHf0SwTQ7iONWGklBy7IF5-5mudYHh6fPN0WV7MSbwRJ3aSjqKXXaPdYUEBLCs9EQoUfLFnvtGNgrYgaXyDXdubMSrL5rZQRyqNscyzeCG50zPreBeBhQME75Eu5cVUWDq5eo22vx3eq8g7cQF9eTg7ER7rcE2I2FizWtEo8lvPmjt_C8b6XUvb70Nhkqkz1cZ_1SnGDKCZDCBhMMItB2bvOMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=RJWLkvVBEQM3E78Qu69dFxZvuGWMMZPPNIf9cu7ntrQ0k7y-RJ2_W2m5unQkRRtKuc1H1S9JmaIGt35cFoOfKDT-gF6mjV77swdq5hzPy6VOZTdJbh7AZ3iKIu8PvI8mz5XWY6Fm-mStHWfOjTl9HfxjQo3IXJrqf7IJ7841NNlihzgFuDKMuQbN85kn_7TnuHfWIqHmLMVyaLJlupZgDRsSc1cIxn75iBtiY7DSVermgnMFabQKqVmsl-gQI0Fh5Cihg7j6Ao-HrFgCGWr81naMPdo2x7p30zAvS_LHM9OfSeqGqX_Z6dk9yKvOB7lTGkP90Z2y2m0p5tMznJTA5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=RJWLkvVBEQM3E78Qu69dFxZvuGWMMZPPNIf9cu7ntrQ0k7y-RJ2_W2m5unQkRRtKuc1H1S9JmaIGt35cFoOfKDT-gF6mjV77swdq5hzPy6VOZTdJbh7AZ3iKIu8PvI8mz5XWY6Fm-mStHWfOjTl9HfxjQo3IXJrqf7IJ7841NNlihzgFuDKMuQbN85kn_7TnuHfWIqHmLMVyaLJlupZgDRsSc1cIxn75iBtiY7DSVermgnMFabQKqVmsl-gQI0Fh5Cihg7j6Ao-HrFgCGWr81naMPdo2x7p30zAvS_LHM9OfSeqGqX_Z6dk9yKvOB7lTGkP90Z2y2m0p5tMznJTA5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=auCf_AZQIa4L7mirBQvU5knpXTvwQMIRZZc06EKSzaWuEV5Q-TQEQocgwb5B8om54Q1Gg86Bpz9cJ_7vcV4fU3ZMmoCjkD8SKX1HZWM0QrNIL-S_-YoDbFLCFPs47gXGEM10zEu-FNHEzvGAJ_9Azh1S-p9DR7cxzinC_w0YSNjx5DFedPv-iG8lCb6Ng9mRTxu66etRKoSKYLPBMWndUgbLYhkpftruFaDL7zB35wY0tIGrTdkVRxJKA6BBwvw0a4FdbNijVU8yexRue3R4bqFKhvaSiKAfL8E5M6UhskyssZNPCeNPTGJweaSaecxTtHXNuKuneVC1TBr4VdoQNE0S3CuFTPRE1snioyJeCJB1-bhlzUOokRXBDMPsSVhkE1YfNqX7HSFRkR7UtvEly9Z8c94SAhnaqF7DbVhBD_NCZDkbxbbkJzO-ntiyGMIDlkEtURD2FvhTz1IDZfruw84Bfv1p2Nn0q5Iwc5u26Yx8rLDJc-AvEXFIjCvfkyAfX4LSrrFNjNM7EZobaBWZacgGAI8ee7nVbgYzFW68zJIikPoRy7SfimEzblkM8SGfu9-JAAh5xjovJWPgb1c9-kwFW0DAycYlh_-VZZryTWe9N-rX8yuRhLHV5o9xGN86LU7w721XPSnuA2FNIX56zRnud_H1C7h-E-KJRf1-DD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=auCf_AZQIa4L7mirBQvU5knpXTvwQMIRZZc06EKSzaWuEV5Q-TQEQocgwb5B8om54Q1Gg86Bpz9cJ_7vcV4fU3ZMmoCjkD8SKX1HZWM0QrNIL-S_-YoDbFLCFPs47gXGEM10zEu-FNHEzvGAJ_9Azh1S-p9DR7cxzinC_w0YSNjx5DFedPv-iG8lCb6Ng9mRTxu66etRKoSKYLPBMWndUgbLYhkpftruFaDL7zB35wY0tIGrTdkVRxJKA6BBwvw0a4FdbNijVU8yexRue3R4bqFKhvaSiKAfL8E5M6UhskyssZNPCeNPTGJweaSaecxTtHXNuKuneVC1TBr4VdoQNE0S3CuFTPRE1snioyJeCJB1-bhlzUOokRXBDMPsSVhkE1YfNqX7HSFRkR7UtvEly9Z8c94SAhnaqF7DbVhBD_NCZDkbxbbkJzO-ntiyGMIDlkEtURD2FvhTz1IDZfruw84Bfv1p2Nn0q5Iwc5u26Yx8rLDJc-AvEXFIjCvfkyAfX4LSrrFNjNM7EZobaBWZacgGAI8ee7nVbgYzFW68zJIikPoRy7SfimEzblkM8SGfu9-JAAh5xjovJWPgb1c9-kwFW0DAycYlh_-VZZryTWe9N-rX8yuRhLHV5o9xGN86LU7w721XPSnuA2FNIX56zRnud_H1C7h-E-KJRf1-DD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=aX5sjIzMJeFRePL6yXI4ctxjrlGL9yM88Xyi6xak76ErVVP0WncZHvn7zXD11_u8AfAU7nW0lSapA2oVZ1g1iy_EcRpXVZbuRC7xqTOgAEaQ-Coz64rgMDmoQ-zzDhlZ5-p1gCzqwXi7W8sx7ZVT6u835RoJ-T7ytmM2wua2ovnkC64vxZtHkKI56mWiuniBFsoROUkwHDiJROOj5GtdlOFus66EQNDol40Iz_2q9FcDgJhtnKs2fvrFuiUayjABhl_TqtOovzWhDyO8hiv1WSM1iXJvTjxW-hgrd0vSCDAAqzEbbZ0YHEWspC-PZBwV1-T7BDmWdor8SPTDlECoiVEbG-Qwk63l8x0YW8PPUkP0YKHFUO_o5miFbIMcS8j7DtSSqO539FoeVZZcnHFDzm6EA6eYIq287GNlSl3TnyUReFRpTscCcm2V67eCqJH0kzEauchBrleGC673IbyoBGZbdicBDdh84smil3KK2II-Nc9pI8SlTGzfzLyIsB6_dpwSWI_6jQ4mNkCfOF0XpP2QYk_ZnqUv_DOj9z3xmHBcSZE9xjUfmLo2oJqQ7wDM9v46MQFJcn9MhBLigdnbLpQmdHBJQz_0JzNoSWfDtinIwOnxHiqOy3zsWcLRIWUi4mVj0Wwl_CAU3gNMoWhsq2zhaLyWcvRgGU0VnuLzCAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=aX5sjIzMJeFRePL6yXI4ctxjrlGL9yM88Xyi6xak76ErVVP0WncZHvn7zXD11_u8AfAU7nW0lSapA2oVZ1g1iy_EcRpXVZbuRC7xqTOgAEaQ-Coz64rgMDmoQ-zzDhlZ5-p1gCzqwXi7W8sx7ZVT6u835RoJ-T7ytmM2wua2ovnkC64vxZtHkKI56mWiuniBFsoROUkwHDiJROOj5GtdlOFus66EQNDol40Iz_2q9FcDgJhtnKs2fvrFuiUayjABhl_TqtOovzWhDyO8hiv1WSM1iXJvTjxW-hgrd0vSCDAAqzEbbZ0YHEWspC-PZBwV1-T7BDmWdor8SPTDlECoiVEbG-Qwk63l8x0YW8PPUkP0YKHFUO_o5miFbIMcS8j7DtSSqO539FoeVZZcnHFDzm6EA6eYIq287GNlSl3TnyUReFRpTscCcm2V67eCqJH0kzEauchBrleGC673IbyoBGZbdicBDdh84smil3KK2II-Nc9pI8SlTGzfzLyIsB6_dpwSWI_6jQ4mNkCfOF0XpP2QYk_ZnqUv_DOj9z3xmHBcSZE9xjUfmLo2oJqQ7wDM9v46MQFJcn9MhBLigdnbLpQmdHBJQz_0JzNoSWfDtinIwOnxHiqOy3zsWcLRIWUi4mVj0Wwl_CAU3gNMoWhsq2zhaLyWcvRgGU0VnuLzCAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_eUMChU1oTBP-iDixGZytH0skkpZIFAhTkzUM7D4HB4B8RU-1jGuBHThDoR3NYMJE3fvYWxiTmDdsElwRWohm9r9uECMFEIbmzyYcqi9PPgMhPazHr-KnssRktucZYjrKUCz9Do6gGndEgdidtE8f8zP9jxxwsRQHE3P8jIxKDwSzizeyjwnsK0cWYQtWk7NIUeLixLAlPTpRSJ97oNYT9oubO4wZPHcY8aFnl1tCgX4ePDHVJ16WEF6PRa1z_2r7uOMjKeR-a4KqcWB73G5rp-r215AgYDizWAaHz1rfqjAT8Zp4jD0YEGKtFghfCJozx92BFzGLNpQTrMHaKVZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=IR2svNXfxVWJ4YL5udDrPSJkPSEK2Bd4dhjQ9Gsk3iRCYOvCfznBuT2aDan3akl7yG3v15Vn5Pefvz-6OCAcxNGCSksBVcTHAHUraNDxS0LiOR4P2X1PzQKmi4TbgOcjzumUBEmXPW-xwaXgiipa1n7_zjEOheCIL-Z9k3xC-gbaHMWmED5Z5bEPQ0oqQ_uHIM_KE_pX50IMAkUj-O-7_pnnC6nFLbgXwhruw-UjNCXVlhgGWSWResHpED4MIg-rv7DxRXvAYBNY3QF5sma-c3VK0lnsg25MyA3ND0o9SMvcR9SeE5aJpnaOSkoV64JGerl5q58DlpXyZ113X_hsog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=IR2svNXfxVWJ4YL5udDrPSJkPSEK2Bd4dhjQ9Gsk3iRCYOvCfznBuT2aDan3akl7yG3v15Vn5Pefvz-6OCAcxNGCSksBVcTHAHUraNDxS0LiOR4P2X1PzQKmi4TbgOcjzumUBEmXPW-xwaXgiipa1n7_zjEOheCIL-Z9k3xC-gbaHMWmED5Z5bEPQ0oqQ_uHIM_KE_pX50IMAkUj-O-7_pnnC6nFLbgXwhruw-UjNCXVlhgGWSWResHpED4MIg-rv7DxRXvAYBNY3QF5sma-c3VK0lnsg25MyA3ND0o9SMvcR9SeE5aJpnaOSkoV64JGerl5q58DlpXyZ113X_hsog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=jVHbkfBU2YbqPLhs79CWOk7LLQfBy5SjONlfj_6aufX1x29_uDYQ_1t374CeInQ5CWX9XQCUpWb0_AiLcGpbpAh7F-ESnfVBpcPD6jQxWVqESPO9AupbIZ7vKM9WWB2vWJGspMs8WhN3ccbTF2acOh-U0xyGso2XyfVQNjAYdWv72CpI4RFAbCNuAg1M6DV0i36pDcybeL4VktBMpZ7qbbOlBbO4QSrGitaRFYwcFYMH9g_9woylFvbbGSnoSR3-GyiBdtH7xFL8mg-xZqnH-YfWS2BUVdkprtADCHRkKtv03VexG-OovexBAOfziZoqyvCpg6PpEzst04AhpoVtjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=jVHbkfBU2YbqPLhs79CWOk7LLQfBy5SjONlfj_6aufX1x29_uDYQ_1t374CeInQ5CWX9XQCUpWb0_AiLcGpbpAh7F-ESnfVBpcPD6jQxWVqESPO9AupbIZ7vKM9WWB2vWJGspMs8WhN3ccbTF2acOh-U0xyGso2XyfVQNjAYdWv72CpI4RFAbCNuAg1M6DV0i36pDcybeL4VktBMpZ7qbbOlBbO4QSrGitaRFYwcFYMH9g_9woylFvbbGSnoSR3-GyiBdtH7xFL8mg-xZqnH-YfWS2BUVdkprtADCHRkKtv03VexG-OovexBAOfziZoqyvCpg6PpEzst04AhpoVtjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=Mxthij2A9tiheRpvtP1JIbnxSH3DzdKK7HvYcSIjTTqQKzWL7UantYAoN78aOWQqrEZALfhW1iwb8aaAe-JJ7P1ferCBEsDfFssucfOkEByKoXqN_xR1-zFN0UdCSJ6_5TcHxPPGwf1buSs3jJA8tGmkxtpDtZQ0ayqsG7NJyQ3bzlyYF11arDvXljW_wOFlC-I8L-AZ5vJxplchpW6EENRH9mPgcCgm-zzDq5DyUuEdHTnqbDebfros8BmUfOblWncS9uU7bu97kzGVi2n9CGCyqbsAU7GYLXTloZn52M8Ne97vaJizoyix_cYvW-g0afNGDtlfjzI4PLWq-_xVbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=Mxthij2A9tiheRpvtP1JIbnxSH3DzdKK7HvYcSIjTTqQKzWL7UantYAoN78aOWQqrEZALfhW1iwb8aaAe-JJ7P1ferCBEsDfFssucfOkEByKoXqN_xR1-zFN0UdCSJ6_5TcHxPPGwf1buSs3jJA8tGmkxtpDtZQ0ayqsG7NJyQ3bzlyYF11arDvXljW_wOFlC-I8L-AZ5vJxplchpW6EENRH9mPgcCgm-zzDq5DyUuEdHTnqbDebfros8BmUfOblWncS9uU7bu97kzGVi2n9CGCyqbsAU7GYLXTloZn52M8Ne97vaJizoyix_cYvW-g0afNGDtlfjzI4PLWq-_xVbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy6pXztdZHoULIoHST4IemS5378UnWaZTJNZ3kx5ouCS1dxIcbVXIKlZezAtrv-BwfLR2eRi85s-DHbG82gFaCkis9UAnh0EtLJKqmD6Jnh9ngG15vaIlvXIAP2NZWs6UfcmZsGBPmbyNqel-EZ-ldFL6zzOgq69ZcKt_vdxrnWBcpL1MQuFDeB0SKkISMStowMWljapuskiBICj0IMI1Cc2RL95asbR2NfT3nrPGej0LDn-IMNtk_TyNKeZFoIGucw_dHOHDp-OblqocFho8YN-AuleoToGZCWGH_0gHqZi1hpaKkOcbjXhLrX9E_sNPZV1KnyQdfuNgrY-dDDF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyHKxedyl_ph7llksMddQxhBzgqyawuuFoxXMXq3TkqHzU0o7LJvI15tSL9k6JSIW_Hw6M6ukl_HPAcmuCS0nxl93q07VnEqGyaUSvrbyYFcB-sKBT99dScgdfjYNkKpKslE1HMx80ppksgeVB8gMVNYR0VOqo5DPqB20gwJfr4rDBPRQKBopO84MZCj6vblcg0KGp1DSvyHlOtiBGMdp7tiG8OLfdahpcDUQqhatw0Sba1S8h7XKChQ0icU7f1bFo6Lj789Yk9CVZMVu7i_7n_MxTEtFh1X3GuexJhlmfErjoyRip4LseYak8uIOtWjDEdlX56KaU8_H-AVzwTvXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNfeI4l0Olr1PG--GbjbHXSE6-kLpkImKXmTs-NGDDKykaF_M6CYTf8vpSXr3c3aSCGO-Bh5JEG25KjRbpfaDzZYqWpIjmeziBzHVw5DuOTHGCgLNIAFUAFLD_Cd54UwUryNUf5eRICZ9YoiFspDxiYa6WD66Cix06z0Rf3PAh3dnM1JyELqMIiWn017APL8oMKBLj2qu3NZS0NLflnPctDSQ6dO1NQerJ-5lCz_8qODCmH1euvbxrOep9_M3AUDN6YD-rQA0Yok4dKzaWsrZE7Hhhja3prfK9tqUN4i6xPMvjD4NAnUv0xh2ca7KwnlU2diPJMU9GbHSKwYYun2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2PtG0jdfVB8r_kIcTJdMvUsPK-bIyuwu-k2v9BlACJ1LBdczukmct3_3GXKvu5_gnVzVfX34Ie2nTwtW0xHovTkgqaUT7Dtx7478tgNOwHmhVgn21j8YLMJqTXGjNpJLri6z_beQUnZR1IG6px6RqrsB4wkDutSn90lqEitfwg-uwqgkJEt6bN-73974-UvwYcgb9jhsZzJHxqXqu3pGoER6ikzDH_hVQGQKVYpUg-v8LrMM_WIxGfbt3wD_vdi2OH4-bJ81112UC3Wz8lvhHemIWujmxvD-6HrkBKJBfq-5fxPOrhV2iVkZEqW9atxP9aYxlPfnSz6MelAOlhl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms8pDFttMcb_vJFCqiDxTTsH9BEQW3G6paJgKdakafrzH4z9gOccRYOt2lGf3DbSBYZx2lnXgZkVlfjovqLR54KjqIm8zBwKbwQRFAanRMzFyIqz1G9HOAJjmAIbaY6zNb8AuRRLQknmwG_olLj0z6UYfC6GWqAytxAYE3bbTWU-jHBpqYyIkCkqhAXvp2cZN_eJG1gjRL9sSwiO5k4m8ufEkzsae7Q9F5K83424GxxlFpPByfdGMCasGOzsic1sgVUScXDTXGO0u8h8i_FgvXUQ3BSsh0paiEFeOOM2DqJ3hBYzwju_XgTcLM9a4VA_NgUNw0Aw_sOskEPzoih-JQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWsYFrNvClj95GyV8rYbHQjtjHfS4jC2r_R7StjNKX66h8BTMvjZJOLuWrKsc20HNxX_GftuOhUtCtvBVk6-hctm91NqPy5bEXk-mXbxWfBk-ouXYTWxzPixQLKJgbtpQRW_yNMycQRlGyiwqtm4J0VUxQ2SCS-sYHUGiRAmNowiFFfsGQUNwyR4i5fOHzjet2Tm31S8AB7HKLhK1LydE22K-NS2lx572pLASBsERx03nLfEpsZ_tBYvm64n3A3Vc6vOrhb3oCTxyikOnIU2HiPOX025mSOUTw8WJOfbuXCFFTSCSuI2FgczCc1VgYqpvf0BGrm2w7HVBO5yCHNREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=H9i4tVVlIQzPXQ_outjAguKf-o6NNH4WL6oOjm4QCTtmJLg4XcEm4L5dGg_jDCXJ9m4VdZggjqMnB32tKfQObi-XgYrIzA0a7EayDoHR1cgPb2bxyOuUVTHRx9eYC-z1c5bo2_gpohkQR3gCACRlM2pIlnL-b-5cHjo3rbdNmCztVx-7ZmxFyCIlommRuI9y6ExLD0x7IQBF-GDDpVOz96wAD6q0_OBlY2afSvFImxGvQfN88F9a4UhFnrT-0iQukaNpSXuRfzawA-HKMNPUqnHzDYELLR1VcWC-f8sKUKPADWv27gBRW-G1NkGfpWK3WoqRfuUSlmgV2-LSqjaG1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=H9i4tVVlIQzPXQ_outjAguKf-o6NNH4WL6oOjm4QCTtmJLg4XcEm4L5dGg_jDCXJ9m4VdZggjqMnB32tKfQObi-XgYrIzA0a7EayDoHR1cgPb2bxyOuUVTHRx9eYC-z1c5bo2_gpohkQR3gCACRlM2pIlnL-b-5cHjo3rbdNmCztVx-7ZmxFyCIlommRuI9y6ExLD0x7IQBF-GDDpVOz96wAD6q0_OBlY2afSvFImxGvQfN88F9a4UhFnrT-0iQukaNpSXuRfzawA-HKMNPUqnHzDYELLR1VcWC-f8sKUKPADWv27gBRW-G1NkGfpWK3WoqRfuUSlmgV2-LSqjaG1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBCKFTgu0jFjldt3kN2HRaZordEruRv7u_vVXNPg5RawstIlWuwV5Qf3qgcBkQCQZdF5b0oEns4QO7JMx5x2x_gDy3CJn3cKQWmQPkWN60r9PaIuwPmL9SZ9ibSmF7t3vRckpts6zet3i451gK56qbPkV169-vcjYlU57_hF_RkQFrgTSzFqsfAsdMLMdOxjW8XMM1UG3h3E9BFuecT9CnzaCMIbGx6mQp0c23PspKTkTYqIVJ8iSwU7xLUd-_WQy5Xvbg60HWAuNw2fe3aQqTGN9OoRxAOSYaDc0xx02BgNve8woa3QopZivJVv9kXwI_iZsNlxJ7H8aB4NuDlMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6SDfZuuUAVzF1qmhibxQQA9w6wBCoke5iHSXyKGeGpLsJmLEVGGJJ82lKI_Rfs5jAT4WZH8Jph8U5HiAFC4rdQ9FW9g26EwwUeG5sMSMpOrxR1sXOBKqU4C4D22OyN8oeRQnLsbTMo0G-MkNi4AQMWSatlrNHc73Mokf96rlt0tIcCYfW4BfZcQeW6lcmvvXS3fQcVDZWYSvS5MQSDd_444ONiZIHiF6vi9ny8t9pRQwySw5HabF5-ODkyin_DNkYrfU3gACEZn-USxygK7J9x9IvCtAj7Q6UEKFHB1BvKpoPdH2In7TbRO1-zekGoRUOK0c3jWB1hEjeNeb9_5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4dUCWoIdqDmINS3Ybq0EATayNnUfhzakQM1hCOqbVWi5LCsIDSPXe4Zyn8TQp1c5ZelM4H45-JnIAk7J_FM_bU8JJepx-QW79BLw0-cHm6OtL_WYnI9i_p548iB5oOjZO_QMHsQNUGCkxDYHEPbA_K4cgKI_T1uksC6k5-GMM0CP9LaZRoqMgjxYJ8DDSgf5rsTA9KWhBwUnQSHrayuez8YELEgAspIvEeFl-Qvzj5LPrX3OS-cu3J_RgsT7o04CjRYHbzWVDGCIuPa2AwIUj5N0ia2LO-c8zlzDhVJLgOpGOplRgVrg_ULJqEpE_vcadkcT0mq27iTjRuiurF_yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc1AW9y0Rv619njSMfXzi9mt3mlVVGYer1uExgqWY4LA7ZmSAMOBNBU9tmQpfLx6qKKoofiEXeextPWamGEIgJjIZKu1nK_cqMs5jxa79-qGpulZk31WWs-5bEnmsZOhFg3nubhLfYllS_H3M2FtKIbD-BixzDqDqLGzmwqA-BpqJJoh33Muz5qHE8v_QNvduk8Kx74tpdTnoZDEqJQ5vhs1M1kDE7dNUsKgDpK2LhDwgEdoFwHTRhvrZHQ-cdHAiTmtk6E2TI6a0siq-CCoHDyE5LteXMiSAvoIu6A7UE70Vduy9iRhy_0X7NQX7sYqwwuubV4_QxBrJgYgPk2Llw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vK0FSWv7PsrgahR7ni07NV_MLr3BVkHCUHVWLnwy4HxIiwkTnEqF86eBzQQ-VcgNAdSq16mJAzRHaE6MRW59MYCIC-0wBXTWfYvSB73QPhE0kCk7S2PdUIB3mbmjgMp_xpQ71Il23QV_PBf9-W7-G7zQFKTxQGxkSKqk0Y_ub2r9MNXALYyqiDOwKo5nOe-3XujqtXC6HX-uqOb0oZ6umG2FNknbkl5eAdbbEoyxdOoBV-hN1ksGUYbzAc69obZfKukMjMxQl-eW5S1NZkSAxIFJeL8GPUPBNmlCQwYvzA5O5E3ZmEI8vab78j__CZh7hU9YIQzOW1bMyIACk5zR7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEu3JNW7dk09XctWC0kM-9o6lz-HdqlUQzQV1htWYdBeZXNGowkILVf44rv3_k1oGwK-pxnbJ7XVdrYB1WlVR86ZEAe16vI349ZAt6dcdgxRB_87L1cv3jdvg0A0PAUMl_1FclRBIYYpAmhO1sSJBXxuU70yiIHvVSIeQlFhuhRW4pj1WyfGQ_9-1xaqnHhfiPT0pE3p7ZhntNKaSvLw47cVhnmAVLNizsIAjsPDZHt_jTGVo4d7biZG0g15jX1qGuWH4seA3LGwKeybVzRwKA3AiPsWBMkJCyRy4a4XIsSvrFwnam-o6vZ-EooZTDr9kGHUWx3ZVO1olf-1Kjynzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=aht8-26oVOGGk1_-QXQfexsgzDI9jK08tAPLuEoClGc5u6BeqYDSvCkwicfefL2AP3chtQAxDe3q2Wn4GDSEouaXm7cmFqiRKXtPuMINGQepG8jOWfcKEXpkpNUo2_eaf3tSJU6Let1Qz-n_Xuu6jT_KgenUZuwdoBHcb6w7d7D2kBcTJq0HTIZR6GOX8c_zmLB4ayY3OWg7RscVk0sut-oJPbWvi6-ClkUZYXYdMZv2i-fIsL3k_bctrcKpFVdyh2XEmJd4pcb07HGAXy1ii20bQpEjt98AMDvYiUQg4pttrrfSqBSIZv2tMNYEMHF4VPAsjhyr61xKK0fQyIgcsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=aht8-26oVOGGk1_-QXQfexsgzDI9jK08tAPLuEoClGc5u6BeqYDSvCkwicfefL2AP3chtQAxDe3q2Wn4GDSEouaXm7cmFqiRKXtPuMINGQepG8jOWfcKEXpkpNUo2_eaf3tSJU6Let1Qz-n_Xuu6jT_KgenUZuwdoBHcb6w7d7D2kBcTJq0HTIZR6GOX8c_zmLB4ayY3OWg7RscVk0sut-oJPbWvi6-ClkUZYXYdMZv2i-fIsL3k_bctrcKpFVdyh2XEmJd4pcb07HGAXy1ii20bQpEjt98AMDvYiUQg4pttrrfSqBSIZv2tMNYEMHF4VPAsjhyr61xKK0fQyIgcsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=dant2azbQ7V6oCzDMuJZlEInyKqrwReqn_l0YRL0FJnWryAoXxCEYdzblffGwSw_LWiRtAGgu_cyMMnbrcHfX11okpKtIpd0TUVjSFpKaOEMwTrCs_oMgacousjYikeYpEvx1QkNkxBut6-Jw18zRpnVrLYRRB0xJYAzI-6PNwmHHH5yTGvvRojKb8Gy6twQET3etVKf7xnub7QGJE9ZqVDDr4BeoqeyhWo9HYSkMzL1g96hnCl5Xf4PGgyv3ixlRhm3vvjqXYmENcDp3GDvXItfOGYhlkwyVXQ64wR9z8oq15jehS1DtVSpQETGIsNmWwNqX88rwHCQchLcVlnxDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=dant2azbQ7V6oCzDMuJZlEInyKqrwReqn_l0YRL0FJnWryAoXxCEYdzblffGwSw_LWiRtAGgu_cyMMnbrcHfX11okpKtIpd0TUVjSFpKaOEMwTrCs_oMgacousjYikeYpEvx1QkNkxBut6-Jw18zRpnVrLYRRB0xJYAzI-6PNwmHHH5yTGvvRojKb8Gy6twQET3etVKf7xnub7QGJE9ZqVDDr4BeoqeyhWo9HYSkMzL1g96hnCl5Xf4PGgyv3ixlRhm3vvjqXYmENcDp3GDvXItfOGYhlkwyVXQ64wR9z8oq15jehS1DtVSpQETGIsNmWwNqX88rwHCQchLcVlnxDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzPOsLt2I6u3bTxGI9q2D5qS2C20KCkzLoYu_pPxXh_X3fttcY8dEw6BaeFzXP6FSYvBpC-aVlJzaq9lHGdOfhystELg54MYgEKp9Qa-pO5vY42FPyihh_7nQcjzPUrR-ca7O5kGBcaE4SM1ZaegxCSpp5QTEP-MSQAFBF6yGksubHt4gKUHY4IVpAYTVzeCq7H3MWdBL6ktnNvITvv_zLm2XIEgC-P0VgUoMJPWRvZG6zmMjJoddA2vipb0myu_GWhiDEgEAgpGJrfkSZQiZaxOtXw5liUqhOiw5mLhTqIDzy56YPFsElbDYTauXrmGYmz0ZfNsCbZ6SMpqUtg-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=bygLIhD4zPaKP8ReKlDVvl44qzCPZwO7_FmCQo1WXDziCFI9jxRbLCx_rqEIBAYBFQAeTBXXcHLG0Oauy4QepqQ4kN911ZTqssrANG984uvBoNwrxnc4MX26fubeofwc5pu5bRB4bMhOw6FFjFOGy4CcI6R3yHeJ8cKR-itWetQOCzDJrSlxZ_Ol5osG9l29m1bPUozQY0YEEwMgwksBOSHxEF-qLTD03BuwylOOB2sl_ZzpLUNEZcmxnXrK_tDK6fo77jSQA-df82za4cQiKFC2tMvR0XBHksw8dEFv2ATJ0ZAYcaKuEx7jrgXNq8WnKccUm74S-TQodruvdPKmmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=bygLIhD4zPaKP8ReKlDVvl44qzCPZwO7_FmCQo1WXDziCFI9jxRbLCx_rqEIBAYBFQAeTBXXcHLG0Oauy4QepqQ4kN911ZTqssrANG984uvBoNwrxnc4MX26fubeofwc5pu5bRB4bMhOw6FFjFOGy4CcI6R3yHeJ8cKR-itWetQOCzDJrSlxZ_Ol5osG9l29m1bPUozQY0YEEwMgwksBOSHxEF-qLTD03BuwylOOB2sl_ZzpLUNEZcmxnXrK_tDK6fo77jSQA-df82za4cQiKFC2tMvR0XBHksw8dEFv2ATJ0ZAYcaKuEx7jrgXNq8WnKccUm74S-TQodruvdPKmmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0XYF_R-93yPR3kRzpfOh3wn1o_DemocBlnn1mZBozBfEdqs92JUitO0AnWyMjhIGtqwK7n9ex8rzI62ow4XKh6x-z1LKxo6lVbHdL_MQDPgrOowDSQsuTlJFPppdlKJluzPEMTmrV-67NnwVaRWXQvaSQJ2yIC6RRN7UZD9wmXVqLxP1sLFzJ5cuUWTv4qz6pNGNuLAlscH6FVWgR42KP6acOzMTJVRsOUrA99XQk_SBNm_8SM6PYiOC82DsqKH7uLehaC-RchZHJuNU6T0i44KXkf7rbK2fg85BgB7uJgI19JNmhzCd568sFInjZI-IfYiEPtuBZD4DKTscR_pmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSBGEbfb3uQkL2Yg6NqXLfv0smsvU1dSGWJwfWAZfFE_L42xqd62iZKpUwgAiPjEaklMuQwl20HKz6ifdpb47T-xJfZhbVUmsnpJDye9ezCaaCs5moex_oCDeLyZr9pFlPWmOy9VF4KnoZ_K7fAeRM8R3RHDlD5lljTpunNPvjq1Ca05Aq8AhYqrJYxe2W7gw-FjXxFlRwWyJdLNiFXVJym_bFq4zkCyi0x3uEJ_YZ7nVSERQDbwY6Jq8aJr5_44FIPAlsCosRje5ZOrrL2otPqVOXGW_a4-qwO8VVah3IYqcmRkKLibhz9pkbj01FDSkg4E2mybAS56jrHg-mt2hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rckp0MnH-010Oe9nQTsfkZXrI_ZuurAHdy7xEe24RsAY7W4bBurQnn_46ijiee9-cG8xPIa2GghHtsjCq1zqghP0gyJtHWDoxmntLMUqMoYn-M1cU7lun7U9hBC73A9HUcJRD3Vlth3l0CZ_5QUR3fQUJNbDlpZ7AnapHrWmFstM02XwXKnWB0KWV3tDWoboqjXXV_n4Gx1RJG1TthHB0gkqL3UfI2kK9m9ytd7ljjPim9jucIadq3S6HWlRYvL4zhIjUGvamYc0_dbUWDouDfT_uVnRWX7PofUAQNabzfNEDHm3d9dvl2oWZ9iSvo-0R3w33SEymJ9SmiaD20kwpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAuzm_JBbnX7kPQB97-4ZvsnAXNjOEZpL0zkSm2sYXo0bOhGX9QqaUafrJLqEvLrPhMzEEOmNtQ7yMUozfTYg82RHG94lVe5tZ0wCIdzQEgm2iJC_NA2jjFbsf0yDfKIGXTO0C5FQA9YWxzZoGswXcOzrH35p6zCI2WBp62_F_QNYh8BW9uvmEe5OG0l_RX9-YfPeMnlbuODjFLv-Y27wds7ALVn26H9Gbp0Mg9VTgaj9zKmvzIlBjp_cgfUZJMvkLF4ss158nXwO2mruiui6NH7qwUep2kDRW540zv9zR8VbtZ9pU8qcCvMUadV-DCDX9qJyrXWOJL8X5pFDv_ejw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpgJf32J-gtR2roqv76uIk9uT_HOQOf_PhWt3tn93UIv-Oaccy2TTCVgo_KSCWWPJBUwBXg0TolZPjiUGQYrrINz3VE-ADCxkW-lZQelhp-YA-ribsUfr7bkhDBbdP73fe4emiE11Bkd3bErqhzbXV8MB6D7in-cWWB3j6Ta-aExc9TPgkkk3m4_65LyhAw5mBHCNlQZ6wH77m9XYJmQwfGyuqRkIRq5EJO6MeHy_kBmMKByPpAfXir7DaCT_xxuGOM60T_Q2EUrEOLM2RASc8tnfq5Iep14-6YSRLHrZpHHk3XxCbEI81UK8_X-uNgT0xXPx8tGt9ynlQk0RLsulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSBkLr5nThJIfp3A5WRBO_OqFKLo2-UnbtwfxgLtyv3D1In_jsPO3PvLwx2eTNYTQAZoXTRlfqU540H0cLdbi8KdD6_6pt-PsuYCJJVd_Ec8zCTIenZMrgTmhP5LM_lzZIAzPcWOsPrfT5hz6XkT8m8q4wu283sZQTSG66W6a5jHG2MiRWCX-AyNLVmn_pErMblE_1ElN5tAUI-7b_DiCBxFH4kejZ-t2xSslRMbxNZzlLEZ4dcv-vv8PX1TA1CY-Oew4LGPN7TQ4WwSJukoeie1S9n9VV7uJm5UQrqCBLYcmv7dXyeH8rTY2SKMvhoMVSNIcPvAeVrjB5IshrLkGZ94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSBkLr5nThJIfp3A5WRBO_OqFKLo2-UnbtwfxgLtyv3D1In_jsPO3PvLwx2eTNYTQAZoXTRlfqU540H0cLdbi8KdD6_6pt-PsuYCJJVd_Ec8zCTIenZMrgTmhP5LM_lzZIAzPcWOsPrfT5hz6XkT8m8q4wu283sZQTSG66W6a5jHG2MiRWCX-AyNLVmn_pErMblE_1ElN5tAUI-7b_DiCBxFH4kejZ-t2xSslRMbxNZzlLEZ4dcv-vv8PX1TA1CY-Oew4LGPN7TQ4WwSJukoeie1S9n9VV7uJm5UQrqCBLYcmv7dXyeH8rTY2SKMvhoMVSNIcPvAeVrjB5IshrLkGZ94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUz3g0TwrJmsnTwpQi3SxjgYhb7v-IxtrKjSaDlui75DY8M5VTyYPgAgfpTN1hRnNe9IQ98KsIdSanaJPqZ9sk0oUvHx14TQ3bwbTShVvwDSLDLe88_prIxrJumWH1cBHf_JWXOX_Hjt3psptBf_BmtwUOCKfAX6wLOAggbkWaMxFk3S3WU38xnD-1HwKcFSI8bDGfC4M3nJ_Vrm71zfG1RwfH4vr6WQWOLSy2im1mNdqWVt469GLsBde-SaeDimQvMoI8oGMERdu8WNFEVO6Qsv-xbclRdJ0wCWhfaakVizOCoMK355jFNse1wNC_4OLtnO1MLWcrjAjjNCCUQd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daoB_obfPVPSvYrTKY6WqOk71xDSxoTXHD-XGbwFNe0XhZA5VxhGuGXFweWvPdbBWvY45vG1RKSflvZrTbdjzxspo8goN41_jnsznfKalDLrdHQhlCPQM1NjBkYvRmAffTlo92r22olE-BYrtqbGXiohi4tyo0LIyKsQWzAlrQ7y2Thwfltm0QdtxoBH2VI1PPRKkuuBKqq8PtYJ7Ra5ILRVra8SWucPOFGnPs3r59azadlTU1IU_tTv29ral7AcNSEF-_q54zWs0RESi-Kg-pJn39ARzvPAG-K4UP3BooM2jjN87n0vIaXUUIO955jFo4EkpMz-DFNCEzGFyXnctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUrntzzhgcJ3cpDsRlsOY4qBxBHjCewvwAM_yThMKLot9Bh8RjJstYJBA-8D5zU6O44scaAX70TGWsNQihWEaajJzywB3WeXYtCjn0gd4PhjZMMRSOuo6571puzDhudfNZqp34XjS2GF2cFLKUXk5lr-DvlqDGTA71FYLG61fP5--yvFVfU0oeM4R3X8lJfha4ImG40YQN_rN0zk0wRcuox8QFl7dsLyBb5i1k0FV8qOu14Nd98UzcZrNAeIYm6ut4j04E4bZxHFoS-r3kUscvJsnkYakxrmaF9UZeX9VZ5gMxaiL2dSufZv0mi53GnhxBAoCLq_ixZbOz9K4_2A9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feCUEOzvJpepPC5dJeJl-KLYoM1fHd7j5x2yXktMQ930vaU4zQ9Zd26NCBYvkitUg1WBG2pDjonXmKT5Yk0MFV1p4-RN5ZbSXKKoL_iM8z0m1EZIyvYGPqm44qqBPocS3wI5-QecFoqyshFrK5GEfLHhTKDbgEFB4witWIEIPtGik_EUXqaZq32xhwTQrERnboPMZKrmXAWDudKIa6gE1afV5JBa-NSKXSE60mWfn8XaxHsM4Jo2uyysRRc2t7uDt6athKmI1ilQEzwrE9CxHMShd6pKMYlKrBH_kB5bOclbR0HhKlv-NUz5YTcamlbjv2zhEcensPwR3s-Pgsp2Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام
‌
جهانی
؛شماتیک ترکیب دو تیم ملی پرتغال
🆚
کرواسی؛ ساعت 02:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc6tu0PrbHVAJbA0GeK-JqCd-SuBpGMYals9LTv_5W8H0VmYK0ZA-Cf8vRiuKHdGFERj2k9wCkS6EM1NDW7c3ZtLAUtlQadIku0q70WrSlzZ5NW8srS2tBteArL0Q2UE6MF1OEtj7QaAA7r1wMoVc7RmlxaKyciwmFNRyJ-PQImKCg-bsBrGYcIGipPGKyL4KzVIUGiMLBD3yF7rW3ngnuz5BP-FdxmL8bJ6RZePGJxT06q8J3_zpPdNTaZc_brdArnkXm9Rb1gXQ7HJxcbd58HtOjgkZQdSutAf_C2dWBrnBctY0q6xSw1DKenK5BGpqRALyp2qt1lAhK2_OZLZ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlHua0IUnoEEYb-EimcH4oyfXKVosIPapO_9YY3cP99NCoSe9i32Dy_fnQwguMDtXlFbEztQ_jk3gcTOJO2LqjUqbO-L3bkFLv8nNJVyLA3lmPWdQZfjXJ_iwz3u5-Bd3CYKP4ajKPashnR8pJl4uCACovjGQ-bPAt0q6_65aXTd8MrfcDAIABUakeoG_GlFAPEQVurLq-IcepdhX7kNr-b-ieC0N7ZWedzy-RiO3_PJo3rIJVZ1V0zfxOCmMS-Md-nyId05JBvXNGz_Pit65RYRJcMtmruCYU0TNLLwaaGaLIfeohBam3FV2SYlXNX6LhI0hkzkmsWs9XjIDHYvDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
