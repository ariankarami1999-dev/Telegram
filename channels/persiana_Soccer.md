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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 17:36:18</div>
<hr>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPmU4iosfckwTQpg9MkMbA2IleHBvsPcDEs4LBbd-K3wOgq7NrINh6AKmThnW0hCzZdM4O-B6stXs__nx4mhcXRrUx7k3NVoVgBn2YryLrpjtahaEeb8eP1T56PbMN1R9XPeP56vNZ__80nonsZYHRVw5ooGUzK6934aE6bueqWbCPfy9rRTjgOQPv_bpkm_AMmmvt9DoHGqY9enxIW4nfYQ2zhkkD6VGnhQea8b5YThFkrMGFYVKT43jqx16aLtbf4oedDCOEvXv0NbGPH-zvxIDAH7ki5UYmGolj1Y91XBesA5JoqqkV5i2EN5deEAG53xGIOah1AdDDfC3derwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxRy2aWfiosgiC0Ea6pJaUOH1z1vddU0yNvUSPNTeWOh_gdiiYDdljrekMbcwWTYkAJUwwo5If1cDI47g8f5ZrWvuC3AaWfTAEtSsqqXqCMLfSsOA5lf57JRUeZmOhW9CM9Io8ZaETniH996dsGieyFw-AigWSil1bvln5TBgZqQhvKFHcDKwZoWOhbtWF_xwDMZIG0nQF8tbPILIvojJykLKn43kzNUrKgJkK8lok7I-4KxD1NVB5uUk6TQpF7O5oOPNnBTP7hBq7-PG4xPss5yldD5_VIix7Glq2mnYmZXmTmNZTvRcFyszLbs582Y03eayPIxKHc-CXrwu74CXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnS5x17foUZDgsOK8QlKiU0kEwb1zj0RrcOm7DjAqkklPzFoEtezHAf3ZcBzi99BxaR7fqf9lalMAJb_wyn1viCMJEAjCO2Dd8BTmeH6gK-e5NBDz_ajChmyL21rWj3-OECup69EoyTktbst3Yw_8Bsaregdqf6enwoQsjazi1uTNYOYc5rgT1LBIOJKeNp0moduFUTH0WKvfNI3v9CQF7LAdxN-a3h1wSKvMuDC9Rh6zlJvFYxFqXBTk53gpJ8URSDNvNoXC7qt12KYopiVJAKMdFhYCLZj5MFqUb6dbiWjqliX1RexEU6C0jHAtSg72J76i_3EFhIlBj71YiOlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOV1nlr54NAOeiHiaC1rdBwL8vhc8Mlx-ZEckWtqFgtQb9sBR0odf1KiehcaJcTNQol44b8FrutN0C5C3prHhhIU81-xjNf0E8HK0flWZY9r_iMI3zKNF3PbR1JJfz9MQOy13cdNNK-N7lgz6Zknuxj0Chyk5bi-YVxcGvxcopmkmusA30jHY6UZtZWZ3-au3_FAk3xGPwL5-Tkb81KhDxuRBrDnf9Ul3jebAf5Gbx_-6CW8S5NNBZnOuX3JG3GoAaaWHmDmwuVcs09gy1elCNd6q6daTgrf_iy6TiCYbS3ASrXhS86hpg_yBrv7JjBfNZC4-zIIp5UbkT9soDkjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/soDTPVQDBL0YK0UrQGf5wkj9l6xejYmKm4NwWh-r2dcJJwzAFH22u5ZYr8Ep7xjpRP9h9WvhobeMCywVqIaozu_BtHrsZxNkPJrCrW1bLZkLHN4aOWmFhftJLp92ewlu6RWP9i8gwYARTquXhFiChwyHgAl14eO_mv7yY0uyg10N4J1SEWF88to-fj9L36OeacT-XsXt0x3hdtLEbW2RKoAuFm1pWkghBbVGFRLL8-MVJIWlyUJkLSBnajeZKKh9_uNtP5sKqZ-BOgj1XpiRtaQ_IS8m60GaH3tccfFNQxxy5wOrM3hM4tAVI7CehsWEEPncKsxZ0fUNoZW-J29avw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKWbvH-L_IPHXs00HBdaXEc63PGQCd5UsILUmHLVdOQ2ZQO20msSx9LleoWRBLVWccMVKteRIJqpZjdkPCTYeWs_h7T318ZMLpRsIwAo9nJ1rpV1Tq5DD3j0L6IvYBjJBxhUVfCY6O-Ioc_Eda02ztCPlt6ZhgPl1uEX9sn4vU17zazZKyC_Xd5wq5DxAff_OoujgJHZi_O53MOZ24KkGUNratbJa34H-8hzHk9wEoXW-YcO3ovuTYCVhAGL7JFm3CNbrNTCI_HR5feia5i_EsZXKnzfESs6dcm-HUO09jAgX2ncO4TdfRTC66DmYzEgd12r8KtrAutZvWfOX5eXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq4VPisiGs5RR_qWpUj4O_lIEouZjKUGK0-Ax2MhzpIPek5kAE2sw6QhhVy7Hbn4KM-uXXwsWa-6AT9aNkUv9TkjYybp4wHPAisPx-8KQp4t3YbrB5wap9RZI_J7eRECpZlq4iY2PMF9EdjWJ-BYyyPCTuhdRbdmIsBRFHR68l3NBlFeRzBHjWEoTwg-YmLw9DEpsOtRS8Qcm1e4h5fzKVItM3VlBP86WOfpwnfMflfE4Psnvhc61Ez-iX0L1FFoAW8nUtF14tscPoRex34c3aILuDVZ5zni2h1qocTVE3fyCSXQFOkrsyWBI5TkxNKRV_X-qqGFWKQt89moan8VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOEVVMQFkJ3f8uIQddJWrOPR5TrL-vo23Aot9HcgqgJMjEOdlxccHIyfPFXFblvbIcn9APChLdQ4LGNBPgfIYiABgpSJ9F-h25eX27o3QAi83PpeYvZNoi9VPkV4KepK9BqsCVWXHMc8X3m7kaOOb7K-4uiJ_2LRZ4GIZtaJ0ozBv9cGySATi3Q1kUcSkPY2JqNkImMLx4ClH5PR-a8Azc7VQGmis6vDwOCX3u19tOaaF_O4sEKg8dZxd17B1fLknkP4wgPoXbokoK-jCPq013n2u3noMffxeQcO5_TjZPtvKSyDLaPXODNIv37nTTdg-2tGNCop7M00J5wyp2C8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejjR8KmeD9QxSDcg3D32hAmqATswLSytytuWZ02v9cF7EjcqTvYK-llg8ywl3TadooJGAAGi2-H_4dGGpCnIZ0JcfqiOkV9wex6_FBLeyqr2PDgZs-zgZgi2d-f7SF3qyh1Xf_rs-7b-Wy6jcfnVQ9o9eTfjW-MiKI0ivrMzmAe5hSxvQzV4eGLSK9MrcHBDqZ-gpZ07x8iYjplRhag12TBGbBF8hHmybN8hmbSwPXL7VF5AvHSdFG4dxpR96dQKwz5ooS1G9a20rqoaAUkjuGQhudPfmHAzHbl4nah3GCqJ4qyoZ2tt8LSl65GKlRUIwkdRVt69VC4qQWyDsGAMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ2AVPrtOvWGswWDe9bOlhrTywd97EmPNduteCgg7vW0Az7J15MQUq-f6MfyuagpIwgK9QHmnxDz9cJB_DGLwk10kdMp4JO4fWiJmP0q2XU-DmVrf9XIcof0EbXu6XZXC9jt5N9Znj8wug4AOBGVCOPwtBmup3fDZBovcu8xuOPpSplnUqnmyS0ApnAA_UFrEKz8U_rh_2ASpCE8JH_5RhcKMwTkcc0GWiHkbC44HwyB2zj8kN8JxibKHxE2FXj873FIhymxLru8WJvqs71KZg_8QaFOUxpacvUl49oOfxeN8I3GPFqUZzsSVjBcvphTX9eNpJ8rk8W8jP_BqEgk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRZmIF_azQyJHTdKoqBTG-MhOAH2x3Ip7_CiRc6rTmZsZqEXp3X5BufR8oQHlnVb1ObC0Ri2hCUtnicdUlvKONVeKvB2I8P3RphPgJe_DuM-qxpBVktuS6QoBFUCbxOQPaltvR9yOQFzizm4nM7cuDrTCOn3ESC_A_ZRNHIrAUOoFKv7jbAug1Skoghb4ZgrANsIaHgmCB_da7Rd7wZbZBr-v12GZBKVCy3MOvfzTZz76w_V83S7whPmrT3N2VcBvYu1NeE3ZAjOk9U9Mgi31fGcUNk7x3UvNJ610EC9_4Bpc4HevTBwX4qV6mB-8R4LXfGPs6DigV7Exp0G3HY5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BxdFMyNz1CDeKA1BM-MNw3G4vatX5PolSQyDmbLAByHmQXWg-pIgjbwof2571l-b1MDTtM7_6snbz3FOWZtnLy-835eqS69sIx8MLCAt7CISOuKPwy_XGHjQE5uu93R_ypjOg5rqlOeYRtreX0mPZWLSb86RFZkyspVXpCmW05skWdM2npcZhsPRTJriArFjwvbhe29Jsy-3zkIZWMepBcoCosgI_1oUAnhzEe-6Qpta1B9ACXdzGDFnVL-X_uvHZkfpGjD2Hw472aTIXvoHJtzUdoK3iDvTE_85ElJW3B993O3m4UAA_8Fy1Rvhmdbr3SUc_lcudza8c_wxRLUp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KtLBInV4F-JrTNqKc1KODLiOE-Yf6erWUjR-u2Fn_x61TFksSpxujX2r2eY-iQ3BIoCrqw3nJO8W8SCDhL7Uq2kcgJtvAxsw6s6Iff6nkRcCYuxRAMfGemybhNe9FjQaDqYWbbTLYxGgs7wlc5pko9kxAh3askt-3xPSh2zcRpIIG6si6EAwBxGviTmC24St9WRAkfVE7WZ7wR3JMfTNd8otJppPZ3RLx2sWrtFOlzidTxXk93PEHW8mNv-yc0wOZKZ5o4JSujxh8MZEE9viNpnqCbNkz4nL6GNndcLkQ91q4vB-olRkZ9o4jmUrH08uCa11y4OqIgVMJfpt4J7v4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbkK_1IUJkf1_veiWDw0kO7cfFYJov25sN30tPC79y2Xdot0KEvBnJGq_O4QaTgP1DEUef-Nldo2HqUKh20wbDR9aEcTBVVImknjDSTL82abrRG0mzO2OUAm31CB-lEKspo1pQug4uLrmPF3c-w83cXDtG9lM0Yq4MN1MqyUldd-9X2y7wcHWWoBtO9YiMCIInIF1QbFR5G4bl1qQO1hLTny9sbJy9B9JGi8b-hjKyiiMitoBXIQhJ2KCpq1KoMWyuSdQ-wZlyhI-D8v6hMihELnV09laP8LPZTfvX87f7jKAbyouiUxBsNHbwN38sxLG89fa5cmpiinm_mmR40Ruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcMrsEwVAIcmhPGJCCyUgfItrU8Me4PzuWdKu2aKhN4mjMUK6ojJKi3En9vgDr0pemuU4AoQOOXSg3tQweu2MJzahpXvUh4BjtOmqn5WReMaDNyOaZDaUf8qe7NJcbmsBaK4UQWnQsulyV6PLpgs1bCOUi9_xUsNgeu19InUoj9yIOwQfKx5AFIMYbipvObv4xDLK2ynO1J45QSioiuUeZQ3iTGJVrwD4P1xZEd4eKnEEZOu9-sZ2stffAcEBa4tQlPBlMHISpqM19pOmLx2kyrhp2-8TeuNqcaunduPmJM-aghqq4FadnM-Ja6AVvyh12k8DDxSGT6g9Y6-QBPL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHC5-rsS28BYvXNHyrj5CfgwE1JhGcLUve2zcS5R_i9va8EfquBijFh8gCFL2azAkHSK7s7uVmt4pRtNiExRaQ5ym2cLcVHN6k41cooPqVualk6Jris_eWDBNbaPpAMrI5WFBOiykaSc_qXGHBYRDRwFUF9Pvzr0BvgCeuc6glWy6OWjiX2tTMcMDntL6pDndzgWmRcrp76FWS3O8aJi5pcDOTTVOmZQ5b_MwyXH8mANx7ePs_wK-fCfHdIMcUFW1Q1thKnBDOtad2RwlBCueKyG25-kXQE3EwbdEwMKkecEl9cDqCGuj_hSmmD7RJNcakrpbvDX3ukXImdPqXlr9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9iX4uImYElAtMpBXvWtkQce3Tb5fQ6S97I_7rbmdrUQPzYrzy5MqchlkvtRkHJYPz2cXNh0z2zeNaBond1jnSw4yPFrMJK7u5r8EIuyyYxRq-1-WzVzKxsgxH0xGFRa-9HaPa8rxtSpw4Mm3DdzPl1QjdwLg1zI5PkIoGGp64cFlVSxZLNnbL1VonY4XblHBkOEyNsm7JJoHzKXlI5xN5lDFcpCara_iTupsbx4SXWIDGTohZVGfeY0Z75xxHgvmGsqQmGu68XSafEqv4WBQFBAOJ-YdfKiywtqpcexZLM2Mq-hxmPFwiZzyKJhcE0uYltSDm3rOHRVPa5wD9ZWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnMbWQ5dOheQdK-PMPrFEbY1u8_DVYX2OXA4bKAIcz1BidkvO_5Jwm0MPEqoVgtHj7BYz_OuSskI0v7Uhf6RNJtPsIwsdwZ19XnXlD_WfKFVtI9fhwNSnIBD82pI1YYdAt3yretsUKzp3RE68rJgRR9WyM0KmpLRMTgQwGG1cnyd757iaObY54g7R9fJLByHAyRx7iwEPSIxgc9-30vBLOPEos-3U0uTZq1bqMoH69MvG_8oJdOC5lfhlIBMmlm4gAKKlblJmXhuLTVsKcAuejr0TGrz8vO5MkSDaer63bBswQ8_zomdlMHZEMQqznZ2wP0jYd25-38aJUGVAf1MqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=SS5HJ8XA6F8fM_YJCcMXnOqcJobprPaYuk4sPzW9GS3HHrfJuk3xbD09nSH2qEF4aYAKMk1EuhGPKjiZYMG2eHfi9E13OFyXd8SIQXD7DX2jX2ljIYRq4TsheD2ET5vyKGhkNjovKUFMCJv3vUDsQnrSa-nD6YFFgOyqCgCmQWHGbvW9J9zYNs-cLgRmE243tvrpJX0apH6ehvdDz76uTfD9kFe22fuyCMuh90UxPfYce_FEidJmlxbblDtDtoYhEYJGGZuSikCP_MVyyzyDe_GrabmPE3KJsr8BKu8LniO3Nbd2TH9ukLT9F6jhN6gHKP4K6lO5x7yLlg_RZ4iPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=SS5HJ8XA6F8fM_YJCcMXnOqcJobprPaYuk4sPzW9GS3HHrfJuk3xbD09nSH2qEF4aYAKMk1EuhGPKjiZYMG2eHfi9E13OFyXd8SIQXD7DX2jX2ljIYRq4TsheD2ET5vyKGhkNjovKUFMCJv3vUDsQnrSa-nD6YFFgOyqCgCmQWHGbvW9J9zYNs-cLgRmE243tvrpJX0apH6ehvdDz76uTfD9kFe22fuyCMuh90UxPfYce_FEidJmlxbblDtDtoYhEYJGGZuSikCP_MVyyzyDe_GrabmPE3KJsr8BKu8LniO3Nbd2TH9ukLT9F6jhN6gHKP4K6lO5x7yLlg_RZ4iPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSsPJA93VrcaG4xa4mmE3IeOtlvUiT6ZVWVlq1p2iikERG-ZsGe4qebdZb2P5FKHgyCF6Uxgi5IF14M9-_tmjzzGkre47hzaZuWtN7DG8gzA3e7h5o7Kv29f-jPj_gT9SLqslqPasZrnPRmk99qX8BaSbSVzirA5NdxRsvIaDQXva83-1OY9e6Mlf6NBhCDMe8P4QIodA4R5r9F2k3KCo_rL8hOXQYhggaVYW9ZyWe3aoO6UEbVwmwfpOylM7K3rI3cpn5Z1UEcQjxE1wJ6yvIhtLVJ_JQkgiJj5qTRTi-b00x7Zzsgzg0MWOB2wAtjpU0WWw33WFBE5OcbwRdfljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/but2wGEVpTys3ug7hC90Du-HvBWm3Sg3IllQBRQMq4YGn0TWMIJddoGQl1Dd_jyUUO8XuiAJ54FmIjsu0lEVbAzzO6D9M5cnay0jpEiHQSIYTw2RFVoJ9qeGdqEE7l_E-56KLVh_mIxxRcSpUB3Q8rHlZRJZdjboBEqUmOTv9Q-BSyFOrtuKpVAb-ft8s1PKBiiOvWS5IfQxsXo56E3V32xLwDDIrh9Mo7N8IkZZFAFjNJE6tJgBcNd8i4Zq7pq3AcggJA3fx1F61Xo9oY7Sr5_m4GfRnNf9iM-OfrOOniDl1E3YYZU-DKmNnjJ-5PhKzbukqMMo4BZaR-Xls0IROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZaeFnLyqMB3Eb2M-VlIJ-53PDLAKCGtgHrgooc2n9dEW9Z1HAQkdHUVkNhhclaJlDBJ7kAb2f1zCHp5z2TLVI50TSEFR8ZOQPmJB9bPHcePj9CattOri_o9IcJfoOWVM4g9uWGCMNfKY8gplruvlB7DdgnoIs-f0tZllaqZvqM6DvzlwxqJbsYWp0U9NjiNvAE2Nd6WY0HcQscm26pjmZFYMTxEla37ABsfherhiVqzSrY2k9yktNErNj5qqSuoThxv0KYxH02Ai0T8rWUSHdNA66d660Ftkv_oJ4B0XEnSp7ub6yOqc0lVENI0vdzbUEfBDMaNBeWtKy08rwEELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24924">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/24924" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24923">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24923" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY7jStS811UePNX9kGPjZaRAmG_EwZaBJFcueyZmjueV0CIZdwhX85hEGhPCQaIP72zc52-nJ0TfRFeGtvr_JJSATXJJ8nDS7vKeguSbzezmrh31x1krJ3EGQhauym-C3R31ujBFNXpC1kbyb4ClxY8qFEBPa3uP4S_5lpRXMAW9vkFlJuxA5d9CbTkCsd36ZksbEYSuLbOHV4Jx9SMryfbh-PqYOeZG4Faq82mR0tgvrG94Vof3PEsYWQNaMUbMW9eiiASwPO1nHFj79024PCeiDVOnXlStl1FLY5Re00xkeyCajtOTsJ_5ZlMMb9ICdsRlUXWtpElPmXwfsOJORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-FxCzmgAsZNEY_hwUGy40XduDGmJ0OdljIWI2kJcjf0DQJTu40Ez4Nnp40N1C-6BYFeVKFtgh6Bg8RUYMCYUm6vbq7KFmShetqP2zHqKJinT2nednlydCWdbWCrV6ypNvF4CkQiH8nF2BUDxo67WGPQJlsRDwDNgY-4VtIpLmtvW1i-Bin_y4i1DdRY3GDghjJO2PrUhSo3vKJB_xSFYKDCbnevsd23-Q88Eqae94GWGaPFBks_QR_b6u7QZr3wxt1rWd-Hd26atgMNiWoAe8KHXMgOQyzelKnoBk-Vp1jf4Ev0iPlRLh7Mv73dvYxBfAfBdyBRW46V3f1C6Iiebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmGiU-mq2UzP-osNMuf5aiN_3mVlzEAxVWnh8v859jpoI715C1NsVeVBnBks6FRUjpF4KDTDy5Ao8ziYP27rUfc031N497-z5wz2lf0iLg4Q-blhbc-yXZBCHdf5lzw-Ex5gQ_xs9zShl3DEw2NglnOPsbm2Y7khd5ZbdNIeE6odSiuInkq7_4SspMzcEMxoQ9M_xAKfs6CKiCDoxqLNmMekuphkuArNZYzhH8avZ0o8ph8bqMzjBhTLjSpXSQGB6QtqmaOXJ4B0icieWcoPFUxkGp6hLFF6wXbwj3VAxZh5V7v-kzKaUK-v-gsh22vBUd7H7b6ui8CX4DYK-nnCAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL1OS7ZTkl-ElRrAdfvbadmVGR0ZNUvYLbuTlmAv2zzXB0YG_KZ6K_siAKn6btsR9UdFEZOE_Ea6t0UpYYm79Sw3bVwdv8cqMd7Wb2blI_CnWvcgXmpBmbzBr_988Jl-69zyASeUfyy6Hu8p4OtUuGk9RPqRlx4wcgBIzOFRFGPswWCRo20KHZuf5z2FGlQRB6vtObvC3h5NzLW6OioHbDW5wfa_1vZvOUVAQnW0TpUfTz-3GTS8ugC19hoND-Z1qvGok_6jLU8vrFRic-s0NP8NfIeQ5xjmKxvvWg-Cm0RRejFqEB6goSbU2oO46dHVw0ufEfcX_UOLfuJtAldeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=fGkHTQP2-YowVbVlRvrJzUm-XmTHnMscoIcLyisI6aETqp9b3nd5x7hqzwQgmc07lw55EQQndugGx-w4d5-cIiby9WDJVEOvNNsKpQE98KjYmXYycUPgYjx64Q62jp9kqQJq79uQLXIAcC_yLKK80Q8twqT5lCGkYVBqroKz2um5ZjrmcpygWf5Htf0-dVKmVGcHXl64zkl_AvDvPjX__cV84kyQfpyW3pegTyFD6bAtidp19uNJiPaRKFCAJG-HzbKyd2a8MV5Y5xJfj0C_hRniKNy0nP4qAHY0E9GiliOFe8rSVu1OmO8PXZoqC_uGDnMTE1bvn_ruF8_fLmOhwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=fGkHTQP2-YowVbVlRvrJzUm-XmTHnMscoIcLyisI6aETqp9b3nd5x7hqzwQgmc07lw55EQQndugGx-w4d5-cIiby9WDJVEOvNNsKpQE98KjYmXYycUPgYjx64Q62jp9kqQJq79uQLXIAcC_yLKK80Q8twqT5lCGkYVBqroKz2um5ZjrmcpygWf5Htf0-dVKmVGcHXl64zkl_AvDvPjX__cV84kyQfpyW3pegTyFD6bAtidp19uNJiPaRKFCAJG-HzbKyd2a8MV5Y5xJfj0C_hRniKNy0nP4qAHY0E9GiliOFe8rSVu1OmO8PXZoqC_uGDnMTE1bvn_ruF8_fLmOhwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3NZRm5eyRslINHkopFek0rx9W8nRLzJN7S79rtiMHOSP_S_UgsmNV73AAqr1rc8_bcCK8FvUPoJhGz5Chp9CqxLS3Cfi31JUMS4MJFwYPl0_38pwbrGoMK4n6eJWOfplx72C7n98E6cPUnbC-_D0PRujDNV9eNv0C8dd2it13Kb8gJJQa9GrXX62X_zkr5wwWf0-BnE5rPk6JSUXI7wSRtqNdYBcViUsxw60ztScLU28zCpIfT_0UQEgXESmx53R5RMj7fd1nzkmkKYVVl79ELdXxYDLjud_DW2pTrH-mOHtCimX0SqQWT_GaNNQ-MAWrKEt4AShLw-bektTIfptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRMne6CFkwR8XF5BkSQIWd6nx2iNA7GtOtOhHYhxDGbUzwZCQ_4MGZu-punyxEfVkIdgC58gVRlg6nrGdqXYvM8wjFzZc2px8z0tZf1w29IGCQrw_-fGGxWM5m3kZVQLSSseqhB3By51I0h4lDu-fHyaqETLvhKrCLQM5G1GFs_4-KquDnrE9jeZ2lh6egIX1XZCO7W5mojYIglrq5P45H4J2tnYF8sXVPcxzK7skTmQBIbsqgH7gMxU2DhH_voPNGwm-NI-BD51Xlax_dbTF6xxwzULVW5ktThYWpAe7ZJziU49PoQOiDUylUttIpn4-MTgY6i2nxT_cXxdfWF-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=FTZXB6DUX9OeHjjI2h4fS-QIoZ35q-eZihj5NlsyxSNoLOctICmPr8uWzefmDLTOZL1JlUR0b7R4C2pm0ef6CRLxHq51GswpSvPEOaO5O6Ago712c50r3fCCzcoasKpzFj2wzeXfAMSaJ335JdgpOnJc7fTKK32jy252wUsVpl1wIlHHMTOCWyWuHK7z2jvLSML7mc_T-FwvM306oqqeU8c4Xla8D-H_4wHWToVYfc0gmvV67hn_mm_t81VdyShCNM1mchnRNdiJ8cT1yKm7uAIEq4mI_Zr_MbWQQ0LEzDmc6yfd6olSEKbDJhhOBKC2ExUMCZy-8hmBuxYS_qKXEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=FTZXB6DUX9OeHjjI2h4fS-QIoZ35q-eZihj5NlsyxSNoLOctICmPr8uWzefmDLTOZL1JlUR0b7R4C2pm0ef6CRLxHq51GswpSvPEOaO5O6Ago712c50r3fCCzcoasKpzFj2wzeXfAMSaJ335JdgpOnJc7fTKK32jy252wUsVpl1wIlHHMTOCWyWuHK7z2jvLSML7mc_T-FwvM306oqqeU8c4Xla8D-H_4wHWToVYfc0gmvV67hn_mm_t81VdyShCNM1mchnRNdiJ8cT1yKm7uAIEq4mI_Zr_MbWQQ0LEzDmc6yfd6olSEKbDJhhOBKC2ExUMCZy-8hmBuxYS_qKXEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWGSY1L1qN5nVd_jJK5iSZCLHIVm9QbT9wUUqmhNFTMpaneASR7U223ccZf1Xc8GfhzIm2kB2MqzazKkElHxwhGrc8vZbWJOlrpCNLG0BtBufxnY-msDpgt-Ai9TW2HOJOAZp21vX-8D7pgd0CfvwSr0hwm2Wt6AEcQAbrQ7OzZEEl4UF67fJba2s8Pg5GuSN1CgwAiucvSb5XsbsviiYDjHPHi0b4vDjSJQ3jriDlKDwzXIT-zOX4Hygxou_s8qIeBK5AKHg40VOnOWFc89FQPZy0xGCwtxLz5mkAYEqcYSUxhfD6Tk3PlpsihQM404IAkF59j1IJnLz37YZtwwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7arZxU0367crw8tpfsjlbju6i9mozeW0zJ0nCVh48El8Sg4MeUIsqvo4hQgwgdOg6DvsaRjedMK5VbC35AD7DZfP51EHVsxkTUzTCfojfv7mjMHuMzY2AS6k4WUoCdI7Pw4IL6szTeXZeIHMEFJiZfF-MsbwZiqgbQDEnnG5CZuGDk712xG1EuCMocsAmu7tmr4iBH4bTi5Y7AnO2i2Hlcu38ox220xkrHIbYDGHac76YfUEe3HsdVb4d4-9ex8NEfhJB1yh8o_Bad_4XhxCx9rIWJg44xmJ_eTjVuVj9_cUksWLzUTyldYbsrSfoqZUd3iA2nBDLyWhVwvjB6-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sszkn4FWOT2-dR8abWhPnj5-UK_m5T4gLRF_niTlnHJX8ZYPZ5omHMeyBEBcNk625gAuVm-XG2-PZQEVH9oW7ZbRbvxDLBaD_fCGKGd-7wAKkHNKG3GpSriKJNCRDl1D8slsT_fkNp-ZXoHRMve_s-xy18Yxxx7ATlixDi-JIIHdHqMMqF7i5IJyOyzig_4zJap-rIJETBMqzfEODir9i_VZ_RiDOmwUkp5DTKuO9e5ZuoujHLff4DXPKRFCYbFKafJecVZrB4gyyv5eGFeJt_QwOqtLOojO9aT0YpPDXOQwEmJLQ1wx55r6YtgwFifhlArnNYL7Lxmxy071A563UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGQheozO7lGtEy57BrT0OQmJH9SIvf6h3Ri_Wb9fWPLJrWmiO9YkPoIq1-sf8el5mYLcvb-EIppdxkDjDukSO4qwW3m_quwOb6fQXNryYCQrlSIjJwPyS97IY1bwY0E6VlbxyufG2Pd5zqGNU2naPx3ysaq3g6T5aumTLO62y-FUOlf-UEtrYcjp1MkEmjhO9HV14mAuvcEwr-5iuFoTsUgY3i8VWn7Hnl5RS5q6_psXAX0lPpiCk1exDodd-dGAuDqA-P0hEvHBPB95HGIwu3WelMgJNrA0JflhtoXOVT1XMmAkFOzBdXyMZVVCPQADTgaikU1su8U9VZcap3w2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVx-xG0bHnz5MbCJhckmmiM5ctdK5y7fuUvtyDNwDaJGwFxfiTv0_MTi4fgr-pDcWdkaZw1HO5kGO0nyt5P2TSTba-M7xhEDXMWbfMr-bFjb4kh_RUJbNEDXrBh0_5UNU4QIoDIahkrSgxBhVAvuiA-fbwMBoASQnPUvYOJ8BBqlx-SrWDbDitaGhh8mwbwogNMLjHMUNkUkWDBojZ6MRxu8UcROPPtrPzeEkUbFeaMh8grk2ns9vOELFhdWEqfpw4fLsaaNoGoOQLYCDQ_hBMc39tEJgdoH2qqe5lLUnsSCGNrGqPuUuIocu_itdLkJlNiyqTtw4RMSZ62wjGWx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4PuYMwzRmlY0q3ejcmzwYeR_HYr6JdKk6aAHBXs_eXTmV0XfkO7ZU-kruY7JJhRkSNb_8C2wFa0_jYjqNa3IP3VQNpMnKSt2QcRHXh54gOMHlPfVEcaREeW6jJ7To_NueeSuyZHZK00If_gsn18QLvriZc3SBO28TEigZTPuhRMJXr3v_Jg3ycGlUk8BpKyzx4VEpUY7skfdVuHjLEPahNR1iQo4aKr2yZ-DkPa-YL6nnqNtlurHawSZjKwvCi8RRCH2S-dyaGu8a2Yp0F2oYls8DXVpSP47bvjj7nkO3GQraVrfjgX1wPx4rlL4dhLltY1__zg_klS_BsQgFzHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWa8SXLdJiYVKJMiJvg88k7UGBCDuDKHBj05rAfeiiSKEo1jI66SMvsxwHmCvwP0dQJHQ5s8pOj9QyWGHR52W28922kvetsRwdpMkTMCzJZNR8R8utRRBT5Nm34DHjO4GTsr-sZMkJmALd9LAaVJJGloXeIazAxu986BP6fEp2_PuSdpBYNOHIXEJvpTHygvx0uDP9AyvAnDZtPwii_Cm6D8EuamnZHyAel8drTbYgwPq93C3YZkUkamR-cOVPygGD_wjmVoaQTHY_HxFJOPM6s7SL_JRoSyr8MdoqDsutFOyCAN4PjEDTjNpEUXcGVnPtNv-foHkAw9m792WcetEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWDWU6QmrnZUqdvbLHOubeVcKiXWMIcSOPlqctr7cA6nfaxWLFYNqBpQ_-GmNCmIv1Iytx0-F5qP6Y604wX0zkUI_Ylme58HzX2ZL-O6AG-JDQ4NCAxWIhAxG_DIHriEi9bKw474PCZKj0LfprkXslzXdfRcESoIhiWD1DES-ETeqidyJur398GV-hbD-ksiUYyclymIIazyBhtQLvwESRdc1iucGJ8jM7Ro0b7lTj0sJlnpYfY54yqqj7vTMbFloBAHl0W9Ulokgum98OD1359ssi9rjRlJ41se7OWsKX9Z5QqUEbGhTWtv8yehyTPpT3j55T55wocHOV5p7MBNFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-bdnndQE5DkQ_K9OcB7CNugqRznpe8WnhGn1lmxLx0yJ5-mJ25PE_AwNDMPFj0LXpa0rJpz3B7wzkmtjzJpjppiY6Ahee_045wo1ifpYLXk0A3LRACxhUXNjev529q17eXCmLR5OuCq2JXxLI9dbZ5fkF82_Vf6Q3J05dG-wp7kweJmyw9BTkuwoTmsUIjm9DE4acwP2x1CrbFCMfZ62CMCe75EVJIHeo0bOKogVGAD1QXOAgReRlTSi6jz_u0WQhJmQNZ0Vo8zl6Fp68iC1dy6rUntOP-O51c_isZmg6y_5-reFyLQm366Nhy8D6rmKBxuvKE1ABUfmSvHvNiREw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1bFroOkWQj1w54R2lhJ6LnSmwx39_4WsUjONHlmaeaNJ4lXqzmDjKtCprLB7DS6cFdNCWQ6mHll6ZtcVYtuPsIx3H6OItkkt47Iv-8Vp1WRkQFDTw2T71OBXO83OA7N85QojV-6sT526USnmD8Rg2KF6hpn8IuvBl336MUQKcDcWUVoNNUCl8vXiUOd8vlFi7kwpz2VULVVKxNTQym7ThszMDq7zj9eddXt5EvtavKf15cWkKXARhFgn-Uga1mi2wdsgXSLGzmEO5TielJgPj78y7IPJ4B2-7CW4-7j-WImz2z08lMT3o-fADi4gPcUbHHFkBBqHKLiyBcKEqiRBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktggsuQgkEiBQ-rJE9fUv5Kw_ZjsmNeujV1cZrRGdIh9_fTDSiBLcfTHD6Z0_WSZJkTBTWK4qqVcDNY2S1Ffh658naHXz8qV5-Vxca2WKGRasrKHwDzbB3WEDPA_skub7kLuD-nPlonCflSSDONa9dOpvgG49jSp22ooDuShE_OQKQ8jWAW46Xp68qaEOqF82pRM5uCC30ApW77lJ5lMCXPWcNULFYMiQIPf2DtuES79eBjaGCQ4iOn2Kz9NSYizNgrYYoyNNg_2Szq1p_DvMCcIHh0eD32j3OSWpdHCC_bIdhVwhNIraU4kaHYEsgzIYFYnZGUn8FyrChSqietp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azU3QnI3SHYyCFLPapiZf-bEt5f2w7QRM6ZPU60754D6hyI3bJCwlwcHULd7aZY36coX-y_qdAuoKh6kO7ID88Tfs4Nw5VyVxelVZRtXHV3UQHxsvsyQizPY6Vqo4s_Iu6qBpBBitk1NbN0g8NrE1xNfSLihnHZI-fugOZrVxVXGQA4OE0A8lUmBXZV3_QxvD38kpKZrimMyAwJAp_RY2D2LHBvIGj0Ij5Shf1slQERGIW5BZzGvROaIOFp2_Mry8kATaooL0VfMyUHZe4KGbv8aBEElxqy3tO8vYZyJgCZfBrPjjd-vgqVuJ0nnUAEnoKTJEWaSkA8_i5aobowIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIxl1cQP_yygWpZoM5XZ-z64Z2dqZKUWzCPD1MVQADkeezR4v_BuDOZ5BoyXy1YrRy4HqqXYqkCV3-MMgUGFspb1sxUabvHhiYfVTBTN58f78gnih406ipPQCCZpkI4wHirefmVqwnMMmGlP8jKa4zAWMMsGnvo_9r29G8rWQlhzWze4q5DCqJFzfkJfPRvBfXZXKLAOV6y5OF3MBj8tnQA2vjK4v4x48NPBiBmUcL-8GmLTN2wRQMp5pzF1fJp7vNbWELOKjFKsdYWHhWzgOj-1Gbocn2uretZVA-DlIhqHZE6ZGhUHMj309Gb-c2h-RagMqFj3cm-aV_8TifxqBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrkGjpo3aeyaBq5XL04oVPYdEh0kcdt3J-yD-MCTWNlvthgsQAp6Qg_Iv6kDljnOxcAEo4rJI9mGFo-akT7i6JWXe6dTwX892NnoVPg2uRPdf-Boa-Au21LVwTqkLAi25x2m5C1crSUnBdkwBNjggDc44BycTZY4AcTrWy4OndgNpqRrAv_tCjPQNEkiJdNcCXbfUyHn8C8odqqPw4BK_41J6JhiIFmF_gjbpZE-pXHBvPrtek-6j0Jxbig3DNugczuIbVOyA_jFafUrtkNMDk8sOYSacOf5ULofAtu2We_mZwOfFBazFS09pAcLReCw3urgTB5vlzkea9w_f_nTdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/valiVugJ6ofqNYsTa5g55Q3wo3QRhURrHORinP8248-yGlWRggDvt6yDI38FwDCiOudoORS6OfoTu9tt-YaEir1WaEj0RRWg8eOAT0IxPwzYai-xnikX8g8eCdMkA3hETlGl8qFyaFvJX0oKOtvMwcHmyCZdsPacmWIRde5UeDV4GTLzkeaWG7pne9IJvlFVFt0d1I664tk4Df68awXXYGi5l8dDJEqJGxBCYWpjAx-WryfIglpPqZB6z_PxooWZdbAE2huftV-2i5CzVPJZWp4_lMKmOhdNHCJbFRJ1Ti5rL_uDnUVdhNmElHx_YPlgENUYhnK87--xO-DTuh2zVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-Hhk9pxI799qexHR2ghm4LUE0_Gjg0TA1JxO8Ljl1ZReSU_SI9U52m6SlDvfCFFxzCvhStdFHY_G4pn4ylLRITCsV3-mvH_kidWPmoDGNkXQ9LW0nWPoPehAjHSnjn0mxpTZikJcTbarT2kWTQ_MKTKMCiPNF6NyLXTQGfelV3sAff4GJsVQcCY3G-OBkMbvUT2OD1cYk0DgVC4NIPrw3vi1pJNkD7XFedd3O9kdhIrfBD4-6RfIjK4DMh6d3l6oeHgMuCVZouaRSQ7AYkkkZ3SIabusxuNge9DAdJhYnn4Ty3GGjljlIkFjgLWL2jfjRX5T2A5COqiQRt9Pg6NdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONng__H8ByKkCb-oM2VaDxlaqA5DwBQAUWzKYl4KrWhl1QVXd6lTpMx7WycWNhaCpj6S6XmfWCcpXxap90yMbHS7o6zekIi_bzic4PS6CIqFYu-md24VnSd6_xsJriQEBqKM5TwVkejntqKW8CvivRqOkbEvyhOmrd4x35iqoMuIa7sASVb41L3uQET6b-uyAHDnYEw0C9V-iRrpDFSJDu_imJ0WESw6E_MmGaUtXXdH9J6zSLRkaCz496L89v81xDVKo2bdmATDLlwG09gkyLC_PFjv0CW_hqQ8Mkh01A_VR-UvuGxbBYzsFus1tvfgFWrBxeiKr1Mya0jANdwSpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GE0tKeL0V0_aRg3omJ75gTKZU3FdwjBkljdI-9pErjNipNQ6_gL0cnkfR9Mr75NWffVUGUGYFarwgI90FQuoe_tDlOmhHcwnZEP_Lw3M-xqFtAV1CdsNylhBepo7f1asfWYyM4qO11kWumyZWoHSpgPcF_vlIsOxr8GKfCJV-Rry6H9iQLsXnnlU-YZBoVytXWBro8AofCRNs0Bdbr-fwxKS6HG321H2VoYcvZjCskM-c0C7A6R8PUronNPRGlbu3QD02kwzfT6tLUMxZoCvwjoXU9goK5HIksoXxxy1SLquysoQ4IvdY-KIkCWYTi1F3LoyEFJFTN0Uliwu1-tNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24886">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snv6X4YNnH4izG7m3ZeCpHhAZFLhf41qDwoa-c_hUZl4EU3fdlb7xZiPd2qwJ6kRrF0g4wNNaJ7CyBtyC4d0miXXOCzWlh-GT4sZTCr67QWEypQgM1_h6iKjcYg-nNKDPXAGkMEzDElbDgZ471c4GGLsbrRS7ShzCdOFwpQkhTjoHCG3ENWP0FpHUuY20Mt6SJ8zEwqEO1zdM9zricTsRqozlJ3ZB7TyDr06-mTKDZAk-TBju-L6zUtD05DCLpSfJ5wKsf5cA-162gyRgdXxg2Wk2bN47b-Dbcw_XI8zcxxoJ4m0ZRDVQoMgkrDccuiI-zNX1yulQ93-pHFXYMKHkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24886" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaS3_NppT12n6OOdMJdqjdeDLxUui-ZYOeOryZ4TPsTnwQCjkI4jl-fc1Dhx18S7Bxsm8oDGyp87dUQeNQ--feLqcsFU6RkRD-MCTUCvIaY8RiBfSV47NUvodQctYghZ3sfjTQVMLVQ6Tc27ptsffqmdTf86i4h8UMB8vHU_jhLsdzublsFepZ49E_A6sMgC_rld3GsHx9EjlHYSuTgXOMmtMIluBJNLNwrB3RuQgE-r8qTT5DviGLIwFrxXFl4PffuyFAg0nHytZIfuuMIZw6aNSE0L2BUOgbOokfX6XPcSp-XNdTDeiiH0TfVCTKIpmuMi5T-xA3sb0HnLksvdOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBWr_Tiw8MWnk1ZRGpCYIimhAm472eTGswDYhBWyv35b4OWBXCklfaivUvp944RjGcTSPP91hqAH31N4c4G0Z4ytQN2tWeJdkRCiMR5GMTdkMwZ2ytJZMNO6UBJgOkJRsMknS2JFqRflKhYOoNhBaJzH1iQQFmiaM9Lk1E7HGNxoWr2ptd8HgqJof51_50QPpeMmrvZKnCI39Cq8qZG7oieGHtxeBi5edwGE4z0-8z5u4x1hkigZSlPAt7ifWbGt06ulycyAjUBXJ7F-w25w89-2xwrUGweQI2AnleXfEekc4mxsH6iY_wgM_Wkvuq1JB9Pwv42U2u25CkzLwditMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=i_h4UISlvpwmhEHCdtVWg0-ip_ODALnZj3vhClF-pB-GdMak8u7ZJAvTGqmtm9XE3qBrnN4Yjz1ir4nYtGY6NVoGwd1INOkn-2af6-ah6uneplXLk-qMN_y09mQAq0Zm-4BeS5sUnSryg8SdWDuSF8VCFb_1RoYJv6wZfw6OZL3WU-CBdvHxMBR8QqpZjOUQ313pg_lS1B8nPIkobDpDViWWa8FlJJej90Cuh9V9j2TXsSq-GTAHw2c28J4lzD74qab5aS0dweBumNEjrqai0ErCOvB6cJ_uNgLdutdQMwMzGB808TpDNAOvyK5zD80nTYb1R0m9_H7KFm45I0jEwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=i_h4UISlvpwmhEHCdtVWg0-ip_ODALnZj3vhClF-pB-GdMak8u7ZJAvTGqmtm9XE3qBrnN4Yjz1ir4nYtGY6NVoGwd1INOkn-2af6-ah6uneplXLk-qMN_y09mQAq0Zm-4BeS5sUnSryg8SdWDuSF8VCFb_1RoYJv6wZfw6OZL3WU-CBdvHxMBR8QqpZjOUQ313pg_lS1B8nPIkobDpDViWWa8FlJJej90Cuh9V9j2TXsSq-GTAHw2c28J4lzD74qab5aS0dweBumNEjrqai0ErCOvB6cJ_uNgLdutdQMwMzGB808TpDNAOvyK5zD80nTYb1R0m9_H7KFm45I0jEwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldLDTsScbHZ_Ha87nCP3R_8li3HPIaUmvLRqeNl6kuNUQPzk6Cl7mr7pCrVOA1M5DGg6mqdTygCepRUzasXSaVo9VxOGEmmQRxVxIkeuL3JIndV8syT8QbNyv65p5Nmql1xelKKH7Tm2_lLZdPo03ofPk8ezAMw92Go3zTgTn4f3lRpilbXjLZr7w9EYopV6mE0_vDFlekXuzMKENzVQswWx1nmm7P0ZXmHnrxn5aFN74322QwQFdUt3mgxBSLgp72hBirDwFv8-xm52vf7ZLv46_kYisJ1z4NaX25fcb3uv6Bl5hjsdsJkinPeVi_KL-EyiGWUlbRpeA6UV17M7lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzJKHfQA_vjKyCIarOj7STLgibCjW2GTjc9xnGPLYd_nQ9VpVg30sl484tiGz3KxXOYcvNZZcjLXZ-DDduZ-eFAdm7nyFvHgWzDOd0o2Qvabg_eQtjiuJt_ujAOhHvtA_DHiq4l3oGavzhoLmFQcFS46_Mn5O0WClEirrWx9Cgg9BgxHlW_tOSxqLeYvYyvJ8PJq_iDykQeZa0SQuZ_o_oeBl9Y3XLlhG48YFFh3AX8jhC_0nA_jSZygjaRcNwUnAzY6OPAQ_pajiKxetflxh3fDLh7cZKMsN-oPTgVJDByHIJuPGRgEy_jxWNz1u7RUugtfRRK9fY-qPfEwZVVyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-2F1RahznHXHdKzqL_QV0oMkbBthNBW0yDvT12N9AU16QktXLJOGKgt8KFjeJlP3YbWfKIS9k3zlyevl2-u_87AQR2ieDSwCovfqzS6dnsTyaDstlIOpWGkK2D83sMcrguTDqvfXFfSe6Cmu4gQNFptVWdU21blltMC18V4hwLwCHIpUaxkAH0CuSjyzsnmHohX4CsIcP35BcgDnYZxO-mrtMVepLy9_8Kj6Scb7DtVj85-CVmhElvG9zCDSsuSNJAEKY_S9YDt2KPz6pmeoOZam4NzvUjqO1wJ8U42G1nVW_D7_4_u-nrRxagAAGBDH6K-cpyPllWevQcWib7tdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=X9MDgTYvNZT_S8UB8cUkAgswdL3z5EogXo1x89i3RSp0mG6jWIcsYpl_5Uu_BYUDM7OYp2twP73R1Uba83H-OVlcUbG1QwI7L8NqCOpvS9cqiPv4lJz5bpjXpmpVu8o8HndgLhrIoVUGhq4Ha0fqnz-Ee5cmye6I0wT2gMM1gqmu-ZC8WOl8dnRAJFm6fRz8dXp-Shx8JEX5ESImBkXFJx_YbldZjKRhPzTOHFbdVVDwQdDNOmglhdEfVmQyoDqh8gESVjq43bipY-NXdG7S4ln8PquLgqoacVKAjusYZvhaxw5w_sTXU_pnpYicinZ_v4nU-wTMwD6REId7MbkX9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=X9MDgTYvNZT_S8UB8cUkAgswdL3z5EogXo1x89i3RSp0mG6jWIcsYpl_5Uu_BYUDM7OYp2twP73R1Uba83H-OVlcUbG1QwI7L8NqCOpvS9cqiPv4lJz5bpjXpmpVu8o8HndgLhrIoVUGhq4Ha0fqnz-Ee5cmye6I0wT2gMM1gqmu-ZC8WOl8dnRAJFm6fRz8dXp-Shx8JEX5ESImBkXFJx_YbldZjKRhPzTOHFbdVVDwQdDNOmglhdEfVmQyoDqh8gESVjq43bipY-NXdG7S4ln8PquLgqoacVKAjusYZvhaxw5w_sTXU_pnpYicinZ_v4nU-wTMwD6REId7MbkX9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X57WBSa1zb2V3-bkC9yHDxqMYq1s8QU7nFz0z_8CYq_8M6HoRlAqolqNOPm2cmmprrG7bKZBH1Eq8D_-oDU7VVWKx8D9dF7D99Hnop7Mir_BUA0n1m49J7U2wghjAIfLk5D1ovqgONtrpMclqaHaNKzrCy2WtsM1opEgNrVutpZJDbxAKNR2iPDm77Y9A8gYkzfvifLrPh0p1y3NOS5MH-YVXSokkPxvscL4qggqllvWAr6XBcA60ZKofL4nGdnzSAv0ZYX_RWYGImWNKoS9B18E-1HZfQpwIEJh-x5H6qZah7F-0mgqZpvrvYQIQeMpNPgCeRrqBoXoIj2WsxVt7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=r0nJrqZTgXRoUI5k6FjBOI347_lArLmA8SdoZqLumzAmpVJad9sI7CyhkAvv7ExICIq-d2ywRayAjoz2EPNP2xULXJnpZFYXSrTU3dPl4PuJC4mJvw7YUmGzUzFsRm_OQekgbBwInfFEd8uJ9mDwhTqJp0w-E4tJQfu9XlsW6jEP2nMQHUBKg4cLxOXcwaiktHj2PA3Mh74blr40rcOU663BMWqj1K6ySdSVMfxcs1vF_bwoUcJX0fy4jmLPPTWCrOsRymUoSMynBIUzaGKltHR5eRg2uUJygavD5EhOqdfqgO7n0MBVvFMX21hXySx56prDnPsETUekyDp9kQHAKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=r0nJrqZTgXRoUI5k6FjBOI347_lArLmA8SdoZqLumzAmpVJad9sI7CyhkAvv7ExICIq-d2ywRayAjoz2EPNP2xULXJnpZFYXSrTU3dPl4PuJC4mJvw7YUmGzUzFsRm_OQekgbBwInfFEd8uJ9mDwhTqJp0w-E4tJQfu9XlsW6jEP2nMQHUBKg4cLxOXcwaiktHj2PA3Mh74blr40rcOU663BMWqj1K6ySdSVMfxcs1vF_bwoUcJX0fy4jmLPPTWCrOsRymUoSMynBIUzaGKltHR5eRg2uUJygavD5EhOqdfqgO7n0MBVvFMX21hXySx56prDnPsETUekyDp9kQHAKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEwYPFwWeC4lA7hF-c1yleFvpxpldo515r6ptb-evw2AjUnNIQ0IIQJVCr5yVBs7i4voSHTvgv9f3rENNseF7U94xRMj-ApiKTRzN3VU7P65QnPJDbt2s0aogH8C1r12iFGDF1WppfKO7D_XBtmGG9Z7asVjJ31PcRgLxMu_zsmPYK4jI2QIMsmhvFmtUtw5WAB7jXBFPzxzQiXUeq82ZN77PPrVjVRs2m14B15GDH2-VsUvi0vjzeCoOowtkB-41N3b0k4dQrCE-h-QBGWLoCbFtJ7BPceLBvjCdvKyQUrUSidxsLZn9csI2Qrf0uQTqHaI2OCqnAuUnN_lQ6nH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=phI_9SHrMyoE4NYYyrEvWttbs_xcI5j0a6MTpPk58hxUqXNUV7Ex8PmdlYkuTLGncKLzzCZW0jBuU7MukpGplui8l68geI3mLPT9S4A78uiIs7ffWYoT6L7JzaKvXkX0nZ9UMZ6DozJdW-96VMt6-kLFCWPoL1vvnzFXgyDUfAiqySUkCl3FgGMGQhgxHjaHoCxdar1Qkn_iw-q1jU5570uq1Q8mXSi2td9Bouz37mTI4aU2FSnZozvebfOmvJu4leBqdvP0h_6rOS_QpoEeNQ7dN1nvRm4gM79HPUFM5zNMfFKSsXa89KeoOjEspbxkLLq7Xub6LTX4fjEa_wMFeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=phI_9SHrMyoE4NYYyrEvWttbs_xcI5j0a6MTpPk58hxUqXNUV7Ex8PmdlYkuTLGncKLzzCZW0jBuU7MukpGplui8l68geI3mLPT9S4A78uiIs7ffWYoT6L7JzaKvXkX0nZ9UMZ6DozJdW-96VMt6-kLFCWPoL1vvnzFXgyDUfAiqySUkCl3FgGMGQhgxHjaHoCxdar1Qkn_iw-q1jU5570uq1Q8mXSi2td9Bouz37mTI4aU2FSnZozvebfOmvJu4leBqdvP0h_6rOS_QpoEeNQ7dN1nvRm4gM79HPUFM5zNMfFKSsXa89KeoOjEspbxkLLq7Xub6LTX4fjEa_wMFeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=q9aWaGhHyTfjaizw15GqlZqD_3D7xyeDh3K26dvMaNnAVZomim2XQxACrnFL7jQ9NqnE7pyNro0h4O3g0BxlUfjibW4C50XDcIH67urmnDvCXL6gfMnFIAcv-ndKepyGu9KhC0FCrJWioX5DAFPTHcalKXXwsU4liTOeYX8ide1-_H48L2SvXQBdrazgUhYV4hT94eg5z695jDE_-ZVtlNztxsQFLNeLKVmZBiCo72dcJbFTryH_mnb_z9Ftq4gAqVhAGCe253c4xJVz0kK_wpnFsF-ciZJVQ2WmhBswCTmEZl8gdM0NfxEe9PWO1fJPrxruJiE3i3LfTUofipvqgYpG4KPWLNBKj29fUPhOrZXUqqvUc8mvmZdBO6ExdZtmgnyJp1sJoqAS1QboAczU9WmEYz7dP5y2Yk3DrY34i-a-YaqL31Op2UMG8BvLzCU7yokAvJ0vnB_e61tSCo7z2Fi9G7crLNF6Ae1vLp4nfO1xrc1jYP0IXeSTq8ekyAnCj4fjgXIJH0a_dkQAM4aqnEt-PyxkTPhVaVnd5St52550Cu0MJQfJcP-PeUtT7sIOoXJgDmdNwwGAwsO50UO7D4cyd7xC48hBycrbkig6utM_SD7cX-lw5_lSm6BHxU1wfP7tv99UxyxMxvyIzw-i2GlCxvaLCbZXPTg_NS4cNQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=q9aWaGhHyTfjaizw15GqlZqD_3D7xyeDh3K26dvMaNnAVZomim2XQxACrnFL7jQ9NqnE7pyNro0h4O3g0BxlUfjibW4C50XDcIH67urmnDvCXL6gfMnFIAcv-ndKepyGu9KhC0FCrJWioX5DAFPTHcalKXXwsU4liTOeYX8ide1-_H48L2SvXQBdrazgUhYV4hT94eg5z695jDE_-ZVtlNztxsQFLNeLKVmZBiCo72dcJbFTryH_mnb_z9Ftq4gAqVhAGCe253c4xJVz0kK_wpnFsF-ciZJVQ2WmhBswCTmEZl8gdM0NfxEe9PWO1fJPrxruJiE3i3LfTUofipvqgYpG4KPWLNBKj29fUPhOrZXUqqvUc8mvmZdBO6ExdZtmgnyJp1sJoqAS1QboAczU9WmEYz7dP5y2Yk3DrY34i-a-YaqL31Op2UMG8BvLzCU7yokAvJ0vnB_e61tSCo7z2Fi9G7crLNF6Ae1vLp4nfO1xrc1jYP0IXeSTq8ekyAnCj4fjgXIJH0a_dkQAM4aqnEt-PyxkTPhVaVnd5St52550Cu0MJQfJcP-PeUtT7sIOoXJgDmdNwwGAwsO50UO7D4cyd7xC48hBycrbkig6utM_SD7cX-lw5_lSm6BHxU1wfP7tv99UxyxMxvyIzw-i2GlCxvaLCbZXPTg_NS4cNQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRUmHx-ZSTffOohM6LXT0cuKDRoziNlFT8Zih7b5gN4OGr_vvQ66FbtdkHfCPExt2uxOu-R_0ODW2UWTg8gKPn1WMW8LL6zdMmGtdRNuQsQjBxUtvksepHJbjP41h8_YM_HQa9hpHLqUYhnKZffy7TstvkTrGrOoyptO9fqyOfAWPuOkW1Y-MavnX0dku7OBr8L6zVdrD-a3J0T8mAx63ZpjSI5-yykqjHrKFgp_kt04x0ivSPnU0723_qClezGuIAJ7wLPv5opYwTAGc2GQ2XSbw-hoMk4Y7KwaspvH6I_2KpbkA-AQgeRmtnewSsqC65AV3ltx0T-4FH5OcsxGCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=OkGyl0mCD-33Iej97S1Y7tsnIH7UCRlSovnJpTVaY9EavE1OlhXvx3_8iaLbD-4vs_4h5FsR4R5Anlm39uEczoKNH4iWD_X8o6pfrk6TvbFi7DJpQwRJcQ55CVtY87ruxTRY4OIByNL4WFnuF9X5NceJ_2Tgo-DKstFnc-bNB1JeOq47dV1a1APn4abpksX6P-KMZGMjZOjmFtPzDpCfu_sPwDYwSQPdiLCaCzJTpvcxwC_zu50psuQvMKADpID4n1BaYFoq82y89tngIh3nvZZLviueKIIpXo-PVM5H9HnbGwu4dAXILQnJH_d-u6LZzZaahFKzIjSSxc212vtJYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=OkGyl0mCD-33Iej97S1Y7tsnIH7UCRlSovnJpTVaY9EavE1OlhXvx3_8iaLbD-4vs_4h5FsR4R5Anlm39uEczoKNH4iWD_X8o6pfrk6TvbFi7DJpQwRJcQ55CVtY87ruxTRY4OIByNL4WFnuF9X5NceJ_2Tgo-DKstFnc-bNB1JeOq47dV1a1APn4abpksX6P-KMZGMjZOjmFtPzDpCfu_sPwDYwSQPdiLCaCzJTpvcxwC_zu50psuQvMKADpID4n1BaYFoq82y89tngIh3nvZZLviueKIIpXo-PVM5H9HnbGwu4dAXILQnJH_d-u6LZzZaahFKzIjSSxc212vtJYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=cq9JGsYZc0KXutF4uB88GxKyLWijawdrUDt2rtuJluz6MaJ6-b50Nbe1rvWC2hl01NtZoOLMMN54p1yFt5n877JUqzHzUiBY06I2K-bmMI-ddy-T-2R6GUZbYDS1FKE-yk4gHJ1DKbNWPUIfWRgcoisvGmPVupnpnzUcpigIV27orIIaVv4bPPU2Y-y0iKZe1lPukd5wWDAM8Oub7nZ-jxWqag7kRfGK-P-Ey-3TJMVHb-w-WkjqlTfYBbHnWdqznM9xfc8NJVKGfqvNsoAG1asF8qnuWtWO4z8gby_vAP502ZFVYft1fU8g-xcIjebhyao3XO4GVJTBuuyJaQcb4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=cq9JGsYZc0KXutF4uB88GxKyLWijawdrUDt2rtuJluz6MaJ6-b50Nbe1rvWC2hl01NtZoOLMMN54p1yFt5n877JUqzHzUiBY06I2K-bmMI-ddy-T-2R6GUZbYDS1FKE-yk4gHJ1DKbNWPUIfWRgcoisvGmPVupnpnzUcpigIV27orIIaVv4bPPU2Y-y0iKZe1lPukd5wWDAM8Oub7nZ-jxWqag7kRfGK-P-Ey-3TJMVHb-w-WkjqlTfYBbHnWdqznM9xfc8NJVKGfqvNsoAG1asF8qnuWtWO4z8gby_vAP502ZFVYft1fU8g-xcIjebhyao3XO4GVJTBuuyJaQcb4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=dISO2BrsQxJJs_sf1aC70ChpFKl8bCMbDrXrHdLVsu9bmcclK-RyAD1335P7zsAy6AL2qEk8dphVg6uj42jVW8Lh9Q3QgqyiPhTWTRAMZoHgGyl6NBgVBPGFY8XHlXmDV-6VmM8VYghWJzTFYSJDa7GcI8EttFKAMUqiHHq0Y3-0fksFQeQ70TuAnbQ4BgkcKu4tGih9y-uZpnKmEuqUgpZ7Z_1HDSIC3fD8uWxcqdjJukJ9bKwreQ7J7LnnfvOPEi-958lEDnKD0eNb3WPLCX1bI9CO6O27Ty7y8TVMXmwl99XRKpPiNGbmmlw-ETdIDPG31QzbjLlUrQsSzbTHlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=dISO2BrsQxJJs_sf1aC70ChpFKl8bCMbDrXrHdLVsu9bmcclK-RyAD1335P7zsAy6AL2qEk8dphVg6uj42jVW8Lh9Q3QgqyiPhTWTRAMZoHgGyl6NBgVBPGFY8XHlXmDV-6VmM8VYghWJzTFYSJDa7GcI8EttFKAMUqiHHq0Y3-0fksFQeQ70TuAnbQ4BgkcKu4tGih9y-uZpnKmEuqUgpZ7Z_1HDSIC3fD8uWxcqdjJukJ9bKwreQ7J7LnnfvOPEi-958lEDnKD0eNb3WPLCX1bI9CO6O27Ty7y8TVMXmwl99XRKpPiNGbmmlw-ETdIDPG31QzbjLlUrQsSzbTHlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd7qeZuM0sTr-JQKKZWFUKyNPiCCEdRNW5LqLxvucp0CCoor1hc-yeCWmr2t-TmH5KNAXI3e_y3_hZyg4Qy1i4-mHrD1hCag4UubkRj-WAejKgcpcQaXDUjNjevWswNrKw5VSI-iXh6EzA7XKmkW2RTMyXik9fn6P04-2EEGKA57-usoiUYF2ZSphnlb_9m_PKm6jFxB4OJqJnOX9y1wRa0jPKdIMAWag-gIez-Jc1JFKVnCMdn7_h2gyMreGkc1kmV6u3mq00xfz6JXt3BSy1It7blRzk4x3vpoO6wPTqYONILCAnh0TsZw3XQrh49H_oWfS-Y-2T-sAZoADIBbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyHKxedyl_ph7llksMddQxhBzgqyawuuFoxXMXq3TkqHzU0o7LJvI15tSL9k6JSIW_Hw6M6ukl_HPAcmuCS0nxl93q07VnEqGyaUSvrbyYFcB-sKBT99dScgdfjYNkKpKslE1HMx80ppksgeVB8gMVNYR0VOqo5DPqB20gwJfr4rDBPRQKBopO84MZCj6vblcg0KGp1DSvyHlOtiBGMdp7tiG8OLfdahpcDUQqhatw0Sba1S8h7XKChQ0icU7f1bFo6Lj789Yk9CVZMVu7i_7n_MxTEtFh1X3GuexJhlmfErjoyRip4LseYak8uIOtWjDEdlX56KaU8_H-AVzwTvXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEgpyehw0WJSav46xebBwfUyG7Tin6Er64VqDhtUpjnaQ3ylA4gFO6r-wroeU9QedJT7Lftka4SlEJgRaJDqLouANw0_9-PaaIVaN6C01onBsfI8siJaQzUV9HhVz4dzHKFic0TbnsuKBpxuW4-iZBxoFe52w8XtPORXLRGaEig6y_WtMAT0lajt0Llp9bHj2Ar-ODro4-FWkkH7qu6HbUtHxFjt5sK61mCmH3X4Uj7teYmOS5cktDM5Rc0RYUgJhcpCul5pYCG2IQOq82_YxHOEEHRSYWmd2SiX2tPUZ96SHoOyAievvqRwyOaBFWmgt-8j4CMudElQH0IciknYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2PtG0jdfVB8r_kIcTJdMvUsPK-bIyuwu-k2v9BlACJ1LBdczukmct3_3GXKvu5_gnVzVfX34Ie2nTwtW0xHovTkgqaUT7Dtx7478tgNOwHmhVgn21j8YLMJqTXGjNpJLri6z_beQUnZR1IG6px6RqrsB4wkDutSn90lqEitfwg-uwqgkJEt6bN-73974-UvwYcgb9jhsZzJHxqXqu3pGoER6ikzDH_hVQGQKVYpUg-v8LrMM_WIxGfbt3wD_vdi2OH4-bJ81112UC3Wz8lvhHemIWujmxvD-6HrkBKJBfq-5fxPOrhV2iVkZEqW9atxP9aYxlPfnSz6MelAOlhl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT3Le7gKgXaBEoRrtjJDWNlEc6D5ZNnFRUikGWqWnyxfJ6x14FT7j2XbQKVhvE4kyYpU6a4vAAyc0zKcP2EbbsCnNSL9ylQZT9SwuOVVCNmyJhQwX09siJ3Ztuqldysp5R__6mDNb9_cfhCYnj6682HwYilttPiSWtrwSES4sxOgZ6sll1k8tvrnUJmj8mR5qyQYRxUHBjCh4Js-UG1cgWznCHiVBHoMaFYEwGwf8_ck4GV8hvihk9wyYvB0EEzNM8GJ0nav9oc7G-yFf-8qfqpOR69goZmJWytXA-GmM_VJij6NV1_67_iBjoYdnflA1MVRop8ZizIGCo4nGyL5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=tEwczcnlq7xkrDpLX1aH3wPQkRIlZlRt7XpwSiVNxagNC1MNhc-RSp_nj4HnF15TuMClm9GZV14KuE4dPScHLRDwrkz5WRLQbznvko8QWFuhR0iRLxizt0DwK7c-d7iE0jljbz-_EdTllXK_vY3Q2TXYhBxTSw8ZaGkxT8QAGR9AaoBPsBi6PVS3KQH2Q_q7OMzp8Cf1hV-oyhnWEFhT5GnN7VBmInWYPQDkSctZR4UAb5CTfpepZt0lwX062XD4dCno9Y-TOdFurErK47zLCPL3hB6j425rJ3nPMXLlABMdKSuo9SfBXHSeFqWTLwZ9_P17AZm0EFCqGcnTWeBYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=tEwczcnlq7xkrDpLX1aH3wPQkRIlZlRt7XpwSiVNxagNC1MNhc-RSp_nj4HnF15TuMClm9GZV14KuE4dPScHLRDwrkz5WRLQbznvko8QWFuhR0iRLxizt0DwK7c-d7iE0jljbz-_EdTllXK_vY3Q2TXYhBxTSw8ZaGkxT8QAGR9AaoBPsBi6PVS3KQH2Q_q7OMzp8Cf1hV-oyhnWEFhT5GnN7VBmInWYPQDkSctZR4UAb5CTfpepZt0lwX062XD4dCno9Y-TOdFurErK47zLCPL3hB6j425rJ3nPMXLlABMdKSuo9SfBXHSeFqWTLwZ9_P17AZm0EFCqGcnTWeBYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBCKFTgu0jFjldt3kN2HRaZordEruRv7u_vVXNPg5RawstIlWuwV5Qf3qgcBkQCQZdF5b0oEns4QO7JMx5x2x_gDy3CJn3cKQWmQPkWN60r9PaIuwPmL9SZ9ibSmF7t3vRckpts6zet3i451gK56qbPkV169-vcjYlU57_hF_RkQFrgTSzFqsfAsdMLMdOxjW8XMM1UG3h3E9BFuecT9CnzaCMIbGx6mQp0c23PspKTkTYqIVJ8iSwU7xLUd-_WQy5Xvbg60HWAuNw2fe3aQqTGN9OoRxAOSYaDc0xx02BgNve8woa3QopZivJVv9kXwI_iZsNlxJ7H8aB4NuDlMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPVf3Q8U3K1yJHdW9UHCcNaDB43HT-LjC6xChf1Tz363hRfe9ucE8L_f-I3LaoiW9yni2zdmm_SiHxjqgsYJaEtvYSiRjsCfWIs_38Ox1BqVG5bPjUdldH8AFBzbvMa_ujKoNooxuVSdL_3h9QVzgLSKklREIWriWxDJKfElEtGZD7UNwCxC1bOH3LkTdmXUun1lHr8I5JoZhUgtVOPiGWkU-c-IemaihSoBUuPSqWxMGHM5dmcU2lU-lZO7ioeuCsOtPxaMB1QQMWrt8QctiqTQpyFHpKRfyoVlUDDd70dUknSqEt0HwhBxa6xiW1kX61iQdqgBZvx0l0mpne_riA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOW-OO0TYEb9xTAemYg678VwNThJRY0U8cVlf-YYP_6ttCLSOdn2-4Ixh08A-s7Lkec3evuDqxkme7FEZ7F-d5fy7ME5Uo5jKXISfZLYs0POxXqema4m7vZ36QgeMQxZE43lJbH5R95o-7yLkkIWFI5iCagcewPbdXOF1E75iKNOkHJXFkGC1PG3Vn8AloWhNOa_xnc5MBwe-mxawcOLZbUJ2o9cCLZEsfZ1L1R3K0TbP1PfpnP6vnXwDZTrmm-wBo6MeaboPTuPlPwZkAiOZqQzX4Vz8H4sLHxvAak1Mf6b3_Dbw0NeK7GZeReL6jp-n0HjDrlJJxlmVkmVB9hfBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-S4IeNZjdmdS9cn5fflG9rI_2-wXvXAApZaOkC7x2-BTVZ8zGkSY6nCJixf_oPW5t3vWwhG-rSddXt-kmqZsSitULximvJyBkyADtCmo91yRkIX8VGzaSQcF0io7WfUsjluHJ2Cnk-00GDxU_92CmIi37ry21y4U2If1nS5M5GXYFVmI1BQWQGWJdsUxXlOCNmFePaSwBnlQ_oFGM3D01K9b7dq4Jo-Y6VtE9Wy-8aAcQiQLmdv2Kvt6YnAR00UCHew6xGM0Ttue7gMqkH7XkzYBqdlSaMV-3hR8FqoCUQAWYqB9CZeQlBm8AZhbyCw0wgTPXnb5_2rlBbeep9ouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7p5490KxJ54cPvFsCEYXYQFDR_962jkG-fdnSlnyM0h68zvJrDz58iQPkYS-eG9ij-lCd2o-DdQabO6jVgDtOZrSTDM2zVZr6hesL5drJ0eSUoebgbWcL0BCzwo1_UHF7qyqB1YAUp7IdiXICfNlq6vt6LevcOeSSfF6pnz1Gpxu0KYHTyFYF848G6vI_iqq-OMDOMI-DjD8fCYeAiEMCuR0o_UzGRdqXb8Yx3OQYxqjI2kp_6eWGeGMvrJSMfMk8URD4tjdTMaH-AN-GpWrIWUVMUUkzTIVd5-FtyCH4chCM1LbCH9Ayw3DcJLNGlHZBBuFclOO67EBfOeoGF_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JYwlZ5tVFkQtaAFvI-wePPVkIVUktYxcJYOj-yqhS7WZwv70LkxF6ilHMR6tD0v9xC0Kj_W1j_pAsFK34rm2OPhtpgX9Icb1F5qjKDbckkFHHRA4pEZJevu8XmgzfDQT1vGdZzqBt5Fz9Td7XlSUFQc1DOUg1acjd_plfrDzn5munm8o4sDrpr9BLo8pbYDDkW6iv9E0YWFy17EFQZss6_v1Wy3lnN52IS5A5CRQ8peVwPYzwh7i8BsUMIH6j9PGfn2hdpJZxEiWCMGnimrab12WFc5I-rSa2opIWN1UJes_XlIQ3xy9D7p8wZnzfNAzDFUP18MW2sZZihLxo6c4EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=TgV-57PL2GfQZGNd8hjlbonvCRmtL2TTDnXcVWo11Z6LQvbfGzCCzstJA-cJCEa9CViorSE1EDUbB5AlsZjYw3G2nQwlRDEUWsQ_sTfA-FSgKjBGT1qO1eYZ_Md6Hy9Lpm9ULD3NHS3F46GnzONfdOKKi7YZQaQRWMr2urvl_997hpPSgu5KLT7Vun_fez3vim1j0vrBBGBGcJkOb85UagWdRsfpwFxYggFjeACjUElHZ_nkwT2-7UZk3wxnmgdGgjW_-kAnmjPfdemylCq7NFcecRWgGLPLN5wOZ3lpArdLWTnhq-GJgKl9OoL213snKb5GUwYyIHE1-b4I2jzPEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=TgV-57PL2GfQZGNd8hjlbonvCRmtL2TTDnXcVWo11Z6LQvbfGzCCzstJA-cJCEa9CViorSE1EDUbB5AlsZjYw3G2nQwlRDEUWsQ_sTfA-FSgKjBGT1qO1eYZ_Md6Hy9Lpm9ULD3NHS3F46GnzONfdOKKi7YZQaQRWMr2urvl_997hpPSgu5KLT7Vun_fez3vim1j0vrBBGBGcJkOb85UagWdRsfpwFxYggFjeACjUElHZ_nkwT2-7UZk3wxnmgdGgjW_-kAnmjPfdemylCq7NFcecRWgGLPLN5wOZ3lpArdLWTnhq-GJgKl9OoL213snKb5GUwYyIHE1-b4I2jzPEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=vNmDXmH16IcggEuNgd9KM89lpVZkYosislyCmFuyJjrJQEUgwnn1qAgXF3Zq2kSFY-dNW-eDszd3WJ_VTOHYQs2wowdyJzXYr4RIJ6mzxIcLPNzpEfZk4UYSk63qImMw3xI90XGwWMJLyZPss6_NI2JZ8srkN3BbrDMzj3kNil-lcIAt8Va0Pudk1oHIdZitDAs-ZD5MV_85_SQ91KobXinfAc6UVK8kpyyoGUkXjiOmBJyR44psNnLq8c4YVOgvDTwn0urFQPgoo9l562ZsyuLPvqdBVw3u-Jwz021NPMgmPEeQ7KWNB7xnQFdnSQZKoV4tq_WpMBrt0q6cMRs3mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=vNmDXmH16IcggEuNgd9KM89lpVZkYosislyCmFuyJjrJQEUgwnn1qAgXF3Zq2kSFY-dNW-eDszd3WJ_VTOHYQs2wowdyJzXYr4RIJ6mzxIcLPNzpEfZk4UYSk63qImMw3xI90XGwWMJLyZPss6_NI2JZ8srkN3BbrDMzj3kNil-lcIAt8Va0Pudk1oHIdZitDAs-ZD5MV_85_SQ91KobXinfAc6UVK8kpyyoGUkXjiOmBJyR44psNnLq8c4YVOgvDTwn0urFQPgoo9l562ZsyuLPvqdBVw3u-Jwz021NPMgmPEeQ7KWNB7xnQFdnSQZKoV4tq_WpMBrt0q6cMRs3mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4wPKLoFwzYPBJFETLdQE3_isLVpBfwylJvVKs5F5X4z4bTYyeJkpDHx9QIQCUE7diHpLALSWo4WaNd8hKWyKr3WnyF1dtmNrDHJ75O88fcgonU8FjBpY2jgMIWN74BsUAi3Uws7_8xzwgshTEG_GYP1EpKngrICf6Y0c1prp_YjS1ViI1SoI4LqxJd31EIpICAYngTENL9-PmGyW7a70zP0ej-Trwyh0_5fRi0r7xT-Me6QM3M4ZUu0PNPVl6VoYzsm1bXQzU-iEbY4ImpFKM5eR03c-YoN7VRya5YgjXPzfdAbCr_QGllJhi_zTdDTaqt9IER1D6Z3PntGyNB1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=he6xG38JJzyAqSHYAHg9jMi4lM-1YzHSUK2etGIrQcc0qu7xtQ1Tr2-wTxCxLMAFO7sqwIIeeyvwI5NdbtjB0sauhbuuPmffOe8xFX5svc2nTtI8lISq3GJG-GI3A3V5hFU0rmlZ-v-1KJimrdn9ElLZjb1_oJ5w9gMgXWgxy0zaeARWYKTiGYh2lRXlGrTMzuWsonIgSQNu8xPzKuhBt-ivVhsADncaB_rgarERkcmsokMRoy39BKiDBcPdn6QszauwLY0NhzwGEBbHCjWmjrSuFJxi1Lyc71Ne02THHBQUypP6z_LGfJoRRDoAFWYs0o90vcXqbvxYnBVU4vVFbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=he6xG38JJzyAqSHYAHg9jMi4lM-1YzHSUK2etGIrQcc0qu7xtQ1Tr2-wTxCxLMAFO7sqwIIeeyvwI5NdbtjB0sauhbuuPmffOe8xFX5svc2nTtI8lISq3GJG-GI3A3V5hFU0rmlZ-v-1KJimrdn9ElLZjb1_oJ5w9gMgXWgxy0zaeARWYKTiGYh2lRXlGrTMzuWsonIgSQNu8xPzKuhBt-ivVhsADncaB_rgarERkcmsokMRoy39BKiDBcPdn6QszauwLY0NhzwGEBbHCjWmjrSuFJxi1Lyc71Ne02THHBQUypP6z_LGfJoRRDoAFWYs0o90vcXqbvxYnBVU4vVFbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMGvD79b1Ac75e75BA5nnb-yLpyScewpmsT1dmHhln-Bt_LCYXoh05AhySitm8qehG-f0n2mtBNz93Gpv2-r1NMaQ3j2UOExMBBieSaj1XoPnAe4FdHqyoiAxCVBl18wxdOo9hMX4zwvpLd6TTLsoCrxs-xPSYoAWsoiFXpWk2i4BfHuhEifCPfre-Ah30SiFZ5zTNQPpUlvi4EReWiTmTSlB4r1KjhDy-szz7afBtLPhOTGHI5emzBeC-CZvHLOHD2OAybUejnqer9PTr_a5WPMiVojVoiead0kP77IGFh8sJPW3mhMoELYdtmGeDMFGDdsGB17Wp6rkbelFGB2nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSBGEbfb3uQkL2Yg6NqXLfv0smsvU1dSGWJwfWAZfFE_L42xqd62iZKpUwgAiPjEaklMuQwl20HKz6ifdpb47T-xJfZhbVUmsnpJDye9ezCaaCs5moex_oCDeLyZr9pFlPWmOy9VF4KnoZ_K7fAeRM8R3RHDlD5lljTpunNPvjq1Ca05Aq8AhYqrJYxe2W7gw-FjXxFlRwWyJdLNiFXVJym_bFq4zkCyi0x3uEJ_YZ7nVSERQDbwY6Jq8aJr5_44FIPAlsCosRje5ZOrrL2otPqVOXGW_a4-qwO8VVah3IYqcmRkKLibhz9pkbj01FDSkg4E2mybAS56jrHg-mt2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtiDaxWJrI-uIE6fTpWGO5shBPZCbf9u-zgt1ELg2Qyemjadx3kct5IFob6Qq02OOSk0yLMj1WIDVkoxRxG0_dREzsUnihnTeFVXdVfpuIQ1JLPmdqUxqFpphIXlrg1cWgdIWOWolI6IVjxJc15byWaeZHn-kl_moeXKdlD6e-VHH67ChChXgt-OH28gouu1bBK6ybfGFJUGEinDPxQgVtz9T_222x8w7YWenzCFB_jFi-8vHjBNbt-XbntAJX52GYH3dM1GOOlfu8SurJfnG4Ds4qeNlnXr_skTr4NzFD7T8eP5bmM0YjueIZk6hKYMnOm59ROLE9pO0WjMXeo4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsBp-fQxRzfVXV7J37EDiYJOGKY7f0XNv8b-ZR1k9ErkwoCpMkVDFiUvTheDq1Dgcb2shzWLtsJ1DPVrxCGKMga9Iw34qoxjwXMyePGDoiWtubfjlPbKVv_aXFbf3MrS9in2h11PnHqFU4ESYVcKxiH9L3wK2KZhCcfgR7eqpq4SR7AS7rv-aETpXApWKkP5ubQPtxmCXqoiR8tSah1EnLZyO9UuJYdcmFpIepqOlegUBN7HSVazCXRCch7BpW1ZLVmoI83PdfTSNnrJG-aQyBMUemLnRMniZUEsM6vvPX1p9lTnmsu4OYXg5Qz7PnsVHGILt_RMC1E3JY3KH8mxmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhQL1Swd4nRxrANUo8zh7lmUiJQHfAPNf2I4uwE5pY_SvVaNXXDhJzNbLjYlyImtUHzWJ1HCHkOccs313KLPteJDG5AtZc2SK_h3zLUa7HUSVvQF87kW4oGmkBIsyLG8Lh5-mIXLKDlItLqgt6zFmdtvhEzx9B_ySUDYdACninuL3sC9iH1cjRY0Ws7Y7iHJmdHPcslgu1edDXMt_GcU4OG8jKraTzMvV0865_GsFrTye1YevL9Uv1PypzjOCf1e7jB0Y13JmYS9rjoePjKqZMJuoi7X11gnUrrQ0bky2p8yelG_x89xKvU4v579qtAXGfYB5AG1fe7qhaGpp7iHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEBIYxI_Ai929zay8RdMjSI5sahyhpapy-7EEBiV7KziFk3dF1zmBCIpXccGZN3ZeFiDSSTR459vGEJOAFW-9X_2s6XZIHPSuyHg34UHe0coRop-GDeCx3Iix7I7d0bxl3E3K7RtHka-Amzo2-PgVHfNdpnD9NST7FyQlvRItpeQiYDL_YqssJ7xxTQaqoTmD5H3WMu-mJQK7Fi-aU-ricOw22dmztOXmnGEuOiLbJMAPsG7tt9LPgdfHJQjiIGFHGokBLl1PfVZ951G6n4y_rw7f1_BR4U8usySyPBdEXRyRmmx8iz7GK5zD5LZ9UJCYJrNhHM1GJ9X7BC5cJV5BFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEBIYxI_Ai929zay8RdMjSI5sahyhpapy-7EEBiV7KziFk3dF1zmBCIpXccGZN3ZeFiDSSTR459vGEJOAFW-9X_2s6XZIHPSuyHg34UHe0coRop-GDeCx3Iix7I7d0bxl3E3K7RtHka-Amzo2-PgVHfNdpnD9NST7FyQlvRItpeQiYDL_YqssJ7xxTQaqoTmD5H3WMu-mJQK7Fi-aU-ricOw22dmztOXmnGEuOiLbJMAPsG7tt9LPgdfHJQjiIGFHGokBLl1PfVZ951G6n4y_rw7f1_BR4U8usySyPBdEXRyRmmx8iz7GK5zD5LZ9UJCYJrNhHM1GJ9X7BC5cJV5BFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiEDUJ4QKrUpHIK29fvmcYBID1u2lU_qrW-UYzzS-ZH2KsDzRf_E7DUnXYoVpN8ptSR84fEiGQFdMyMZdpzlwozM8NkFdlU46Rs8teQFO0JpupGLJqmBaMhFKDbXqXzfwsOT-IxZqmS1keNOPAy0FDw334AYHegHhU2V6GmHHX1FsXqg1U6QiVT6CRhCkU1_2FmzsEL3vJxRA3F84EvJp6Sr4fxHuo5UH33_1UZ2c94qT0RpIG5Nva-mQG3N3cGO99pPvOhUGMgk30UGaAKXPAmmuUOpE2d-jY8YceaDitsISaM6I1n-eDIYTYVVOO836HsDjAbpn9AF7fhbnH5P2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZjQIwkKJepvSZjZXU2u2sJ1dwmvaCh80rOuzFnDXwS4Ihu3nZ7G9Lbz2WKbREOY_qgL3Mu3ce_3sj_YIN0S2XyNJVe-mpoAgsUB5vzS4wj4Y4OVzKjNz8C4Ph6AVFmxUrqvEpdH6ljrWqSReuApRYBkrt_pQ55WW3qrv2dwJZcc9axuFkGIMSqUp5XQhJxdVDDCWCJFoTIJk1ys-c00Fu-bNYDSgbD07nlq10pMSlpvSHuF_KTB06ip4qlS-pITFbgk9KWVdOQoRA3Ud5VDT6HrWoFB5YDslYkbETz_zakOgm-OiuVZgG1km7_LtnzOeHx2fVe5EoZNNl-gWAk3qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoHA6qPVgAjPr7DoYMpfpH1iln7OlK3zBtXHuZ_vjEH1Z8KuzR8vn3rey0my3cPGylDLRSJU03zA13MR1Ikx172LO-NxV8cJ8QMqJ1nP5OZPlZa6JXX0UX4uw5oOYPSLIbZMdY7j3M_0mdssxySCL-yHDEK1t8EOZ9ja7p42kEeLCC4bXdABxNVxLCZv_vOl4uzj3wCDMR1AbmIiehvBH2mRTCqjqjXKmtjUVu_aJnOFOy2N5gB__Z93xHZ-C74IOvA-fVzC5uiZmC7e1-6QEwvMaiwDhQZSMQOBCRQpJq0fmrDmgQEmIs_FJdkTNfQ0v8cKoSz2wc5rylofpaiGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBMrisHZ5yKLLxQiiYf-RlGcj8Nc0raw5ebo-KmrpBZDW8GD2TKPcSGhIKQNBANupuYx284c6pabkaq5Kaj7qkNjIgIo-JwHgx7VdhmP7GRb5QOZyC-SoCNs7nSTK8UUGBmo8KcigVQ3f6yxwwX3NpVfIDj7DfqXhen7dijhJNajAN2CtdktOFDANPLKDtElZZIo4fr5NalSuNYxGjrewBp7yZodqYBKFOriFmNok8bLA3iIV5QUwXIA-tdTxtaT0X8torHCSyLIxORko879gtc1RCCHz7NjTiuPIcVpNXLdUSFErIJEIdHIJV1uLcrFBLZn3D02JmXrVg_MSEDJOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOb7oEIqpz46KfYXUXG0WUiOtZf2j4rUaBquMfhvyd--E9_WoWbwM8FxTSNl7pZBMiX5HMzmDRTLS2O5vkYFnR2Kf1riyM6vBtSWnPF7vtebjWVG00plAFkQlyolBmDssXm63gZmIrH45FoT_B_bUyMLzwYTLxhB9QSibf67DFacEAQuk3Jj2CGO1BH_EzPxExBdMv3FPehCm3er4-Np3sdFZrC5Kxq2EBHZmUS03iL4zzUqzPG5vP2PzGyOxgmmRDMNi8sANN9NFn50T1bkLoYoTWy7KxmfoMtzjMvTtLbN20gsWAX3v8wK_lqCCjVP1br3S0IV9rwt_XTLjGjySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh2sNrmhDQlxnNBTp0Twiz-d93tmk5fQX7NIQgq3V0PkosU-PAfC87JYvV1059c59_7EyIHwZdJKwTAcU_8iYRuxEiNV5OUmjIVDU02eYIBu1o-CAw-LT0r-uwXn3o5ZeIG8fdr00dpIOEbHs670UqJovw8IKZH44_t3XFhsKVtoDwda8RqNqXwkU9woFHI0b3Um1aH4MRbA_OS6gltlZ2z3oG6XTAG7wG1ucHDcoJIRwl65Bw3THfpM_aFK3__LS90KYEDeVVNF4ey-VWBgbgrcMKNJdL1z0LRpdNXmQi24kozPk36v9SZIKiFoI5AkhtNx5EobnGrSc1fo3xtjCg.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwxSruRP2p0PX-uLeigR5JYh4ZzwRF-kZXlsQDnKuv35ijH2CyY_xo1ng3NEWBkc1Dl3Cr09MdRHnwYrunq8jAnpo5_6MBfhMvaMRrR0UbSJJ1tWnS2uPpq2ApX7-kw1zKzvvsBWbMkGvdpk16vd4vVjBsU0Rc1RK-ThMOkjQMsjPx0fUEbZo9NKOBX-Y_2Z8mGs1_H0JJx4FHQ5QJOIZUeFvTiPQi365hJyle7KHqaeKMGRvTcUAUmhYQa-T2JYWk_b_5_Y350MJcp2hUtPVSq9zgAZxj1cel8ynHgFNTVrp0fIT6o32UAVMfc4JCOzGV-8kVdaYszkGmSFAwKO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=uvtjw08Go-qjswEpM88fMZAPh9_MP-Oyhls89nUiurRAAJ8tEW5dJDavtmhFw3Hc_09Wv0El57qA8WWj1rgqrAIUaXuYkU11tjUlMpze4aTOu44cWVvPXUPM_SnmnOdbX5foIHXSHTc8sfWakPzyr_X0pr7LAH0reT_anvCT9Tab7OHgUa48DlDhr39_Lm86J91sKTyi3DvadxraeyED_orJ13sMzlw4HX9LlVUta9LeXjqDI6mW6k5n_F14i-SPP66nCMuP7qM7VZieh1askjT7j2_WcTlHAfQb0mO08I6EGqArOOuMj8diCUFsvzjNunhxNnZyqQUa91p17Gg5_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=uvtjw08Go-qjswEpM88fMZAPh9_MP-Oyhls89nUiurRAAJ8tEW5dJDavtmhFw3Hc_09Wv0El57qA8WWj1rgqrAIUaXuYkU11tjUlMpze4aTOu44cWVvPXUPM_SnmnOdbX5foIHXSHTc8sfWakPzyr_X0pr7LAH0reT_anvCT9Tab7OHgUa48DlDhr39_Lm86J91sKTyi3DvadxraeyED_orJ13sMzlw4HX9LlVUta9LeXjqDI6mW6k5n_F14i-SPP66nCMuP7qM7VZieh1askjT7j2_WcTlHAfQb0mO08I6EGqArOOuMj8diCUFsvzjNunhxNnZyqQUa91p17Gg5_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvL9bFnA6F5Li5YFgXec8kNHaXMMrzAhhOvPb-HPVW5KhH9gM2Y7OvCsKWW-2kZAgeN4qPLngtxs_I-XqU7vClxSsA9UZsGbSHzyGnPDxTr2QCHAOEpBSe8VF9CYUfluPyXMOD7a7BIrR3aPh2PEtvRrl491_IPGvEq1rpXmuGIuwGcuE_KH3YkMlkVEG0O5YugsNckI2VO2gf4AFWh4RquMP5xdGF_hHIk078CUA7nWC6TY0mum9QLI2y6PBTfXG_E1zKYuS83yNVddfmapMPNuNgKh-uq6a4Zk_lzfNawklLeb6U5xYEm_TTMVMeoIGmgGSUwJUsXzpwD2fYrOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
