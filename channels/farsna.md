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
<img src="https://cdn4.telesco.pe/file/YkBAmxpM1qMvavHojMnzuxqEjN_7pE690vnV_H_QW8qGWMps_-_QYuTsV-6d8QVbOAkJMAE6ce5mKVlaxaEyokhSNiiD4kJ9-_COQVmWISry7w0CB1ElwxQvUWtFWN9N_n5nyXx6svPTL8p-dxCnmveoRea48AdOaaHn5u9EhU-e7MMEOt2CoA7DnavPLPoKy7-2fU9EOKRD0TA4zofJ1YB5ChTJnT72jzWEzrByXPTHzPMVxW7aq9RD0fdhneJNo5hiiuwtsh_WN_LUzazI69lSKDef2dQBru2safT95mwX93cMaWsWyz-NBuMi0ybTDIdBSYaaHQgMoJ0hU9kckg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-461251">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0Dxwc3rhxfXp4IXHTWeXFHxH_YcdT-eJ4NvmbNr4WkSn7EEl9GxL8FWCAWkRxHhA618hiHxENKn_d79lCOinuX8krgNff0D8kD2UIsP1EtejCi0aMTJJgTq3A9hrUPcsWhKo9xFS2bNUb_3045U_ah8EDPqMLPfJljon3vePh26NmXUZlHQBRYpfzH7W2QKf7DltjGKc5UqBcQorP5Du5xK0hqhA9tEwirNO1FkM1FuADkPP0dxyGZF6FCWRz-cTmnwuLEZ-IgfVr1eYSm9ca8r0BMv-R1-vp8Z_nV54deYOHYrJplgvoSEBlc4uL4OqeVCjECB9OKBCmmosna2qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعرفۀ مکالمه تلفن ثابت به همراه ۴۵ درصد افزایش یافت
🔹
طبق شرکت مخابرات از ۲۰ شهریور، سقف تعرفۀ مکالمه تلفن ثابت به همراه از ۶۲۵ به ۹۰۶ ریال افزایش می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/461251" target="_blank">📅 15:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461250">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e0c46974.mp4?token=YdS3Aq6mtBtdEe26jIcKxSJHB46f8fd8pduwB8EIl0DDEEypYTlOHjWkapDpSGbUMzWDnjjVy-Di_5XZhdwLYFAc-N62xNfS0TOSAstU6WIb1iC8GVd_9fPO_r9JW0cUrI5WSksNNBomt69Bvg9zYTmvfnZVQ2E5IoA8Y-yKjpjln_dpsZ-46eddyMmESRS28sN5JFuYKSmH5nSZYivCgoUbLWu973zy2yQZ5VRLvIwP-oZR35_wv0Dfbn4AnZHdR019LNB3U4wk18XZLNEo_Xlon9v9-cmFAvASwsNSmikVVUUPaoG6306L3mjnDGLUr9pcFwNXLY54NbfNAU_MBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e0c46974.mp4?token=YdS3Aq6mtBtdEe26jIcKxSJHB46f8fd8pduwB8EIl0DDEEypYTlOHjWkapDpSGbUMzWDnjjVy-Di_5XZhdwLYFAc-N62xNfS0TOSAstU6WIb1iC8GVd_9fPO_r9JW0cUrI5WSksNNBomt69Bvg9zYTmvfnZVQ2E5IoA8Y-yKjpjln_dpsZ-46eddyMmESRS28sN5JFuYKSmH5nSZYivCgoUbLWu973zy2yQZ5VRLvIwP-oZR35_wv0Dfbn4AnZHdR019LNB3U4wk18XZLNEo_Xlon9v9-cmFAvASwsNSmikVVUUPaoG6306L3mjnDGLUr9pcFwNXLY54NbfNAU_MBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ضربۀ‌ کاری انصارالله؛ جزیرۀ زقر هم آزاد شد
🔹
خبرگزاری فرانسه گزارش داد نیروهای مسلح یمن امروز، پس از تسلط بر شهر راهبردی  المخا، جزیره زُقر در جنوب دریای سرخ را نیز آزاد کردند.
🔹
این خبرگزاری امروز به نقل از ۳ منبع در دولت مستعفی یمن وابسته به عربستان افزود…</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/farsna/461250" target="_blank">📅 15:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461249">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0392dada5.mp4?token=HKFT9tcp954EBvQamlw52R9zi8wfOCMo6-5txv5J8Uj0Kpo6mA2NQ--zqawQtJ8vBU3sJk3fTcPu6JdGEOrJeUtKJTRMS4wIXvLDZXz5GmIjfiHADFfVOH345RAqNnRgeXaDtXC_EzC_rCPwJQL2EvrY0PHDTxuG6d0tfYHKJQU5uAvEd9XMr6Ay4BpoREOShdBK1ompnVxCLgGifm3E73IEnfSXWBGhsPhkHXgFf5SvsbQn519B2umwTU8b5AHGg2WyZ8XHePpTwNXbvai1UIAOR3muagyr-u36ojJWlAgumnXFq-hDDIXiTRLMrHIW1Szbqp4hfKX_nDDmgWf5iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0392dada5.mp4?token=HKFT9tcp954EBvQamlw52R9zi8wfOCMo6-5txv5J8Uj0Kpo6mA2NQ--zqawQtJ8vBU3sJk3fTcPu6JdGEOrJeUtKJTRMS4wIXvLDZXz5GmIjfiHADFfVOH345RAqNnRgeXaDtXC_EzC_rCPwJQL2EvrY0PHDTxuG6d0tfYHKJQU5uAvEd9XMr6Ay4BpoREOShdBK1ompnVxCLgGifm3E73IEnfSXWBGhsPhkHXgFf5SvsbQn519B2umwTU8b5AHGg2WyZ8XHePpTwNXbvai1UIAOR3muagyr-u36ojJWlAgumnXFq-hDDIXiTRLMrHIW1Szbqp4hfKX_nDDmgWf5iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محل مصرف مالیات‌تان را خودتان مشخص کنید!
@Farsna</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/farsna/461249" target="_blank">📅 14:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461248">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8a25e666.mp4?token=md3o69ba0TXxWnUHkiCHwrOFDmkkFQXiMSCfRlNLA38fa61oVcvPpQoddFKm0CavN-AYiyqu6OAGnahsfFruN9jb4pND4AeisCtMlkM-1Sy-rqX1i3vNgtnOitoiAVPTso8CGKRRE8qCUQaaYSYkLV_nE_pUIEhsalmM4aX2cZwbL1p7bS2YtxKp_70Nb7DLJNS8QF3lg1pW0FGC81gYyq7evD49Gb1tvtNTZSUKWjEaGIqJwVJjdKvK4c0-UGb6fcA0kbctcGogjhRrsOpOmMK3XWq4GNQA0kxuKp5VPra68C4b9TvS3ZrKk2duanQJAMzSxW9JfhFulf0sjtqaSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8a25e666.mp4?token=md3o69ba0TXxWnUHkiCHwrOFDmkkFQXiMSCfRlNLA38fa61oVcvPpQoddFKm0CavN-AYiyqu6OAGnahsfFruN9jb4pND4AeisCtMlkM-1Sy-rqX1i3vNgtnOitoiAVPTso8CGKRRE8qCUQaaYSYkLV_nE_pUIEhsalmM4aX2cZwbL1p7bS2YtxKp_70Nb7DLJNS8QF3lg1pW0FGC81gYyq7evD49Gb1tvtNTZSUKWjEaGIqJwVJjdKvK4c0-UGb6fcA0kbctcGogjhRrsOpOmMK3XWq4GNQA0kxuKp5VPra68C4b9TvS3ZrKk2duanQJAMzSxW9JfhFulf0sjtqaSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حادثۀ مرگبار برای کشتی خارجی در چین
🔹
خبرگزاری «شینهوا» خبر داد که یک کشتی باری خارجی در حین تعمیر و نگهداری در کارخانه کشتی‌سازی در شهر چینگدائو آتش گرفت.
🔹
به گفته مقامات چین، در نتیجه آتش گرفتن این کشتی در چینگدائو استان شاندونگ در شرق این کشور، ۲۰ نفر جان خود را از دست دادند و ۵ تن دیگر مفقود شدند.
@Farsna</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/461248" target="_blank">📅 14:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461247">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg1SwQPJCQvO0UHBWiuFXD84z5rl55itr1JcTDzY9eIKO9moOBmqhHqLOa5SZL6ZOSk1hjTWPNq5CHSyrtM60DOe8DhO8iw0IpihRg_NXxIL9I7_2ZftqEOYNXOG_0RUHeGZemTIVQN4uuowz-_AUlHlfMn5uqNZGq0sZzW6goytb-gA52gPcTmzV1gapT51V82mCixAPHMYLr9tvDVZKKEfnfyu1UOoBbSjnqVpWsnKhhk7Exvp2a_8Z_XRyLlva3QkuPYfIoamZb4tYM7nVTyTk0lD86z_m_YB4ybumPEsvovswEyFuTA2_JhJvhdHR3v_CFX-VKErEFw8dxsDFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیبر - پرسپولیس</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/461247" target="_blank">📅 14:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461246">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcjUjjuc1Cp4aeLcXxdwzZVeWtVcXghCqgJ7Jvw2O_bmCwF3K0zEGicPSg_vw9AWB78UUVzBZHgXwZN80K7c-fAHzeok6ny6mJmkkitu6htAQCdYH-KqsbeQeA0nZEaoQlqXZE6PSlDvHxZ4kYN8hFn4ADp9rTD_6kHbkDvzklrme5nMrLgpR9cxoANtPL4Xy_EkEsOEcgcQiX0dihCnSGddb79lkznBpCFmjqMmYimCAWJ27x7aDeQkKHNBuuP7ZNcQeJaK4k9cEEbBXDN5QcuTiOqQ19QrN76i4dczfRvyEeDiDeTR15EuZEpSnyB1gkcnU8_MdUbIqLN-CEzZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثۀ دریایی در سواحل یمن
🔹
سازمان تجارت دریایی بریتانیا با انتشار یک هشدار دریایی اعلام کرد که گزارشی درباره یک حادثه مشکوک در ۹۸ مایل دریایی جنوب غربی شهر «المکلا»  در یمن دریافت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/farsna/461246" target="_blank">📅 14:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461245">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6lOGzJiGlQDlsEIVA193mJBqSl90U1cEqeaHGAWrsbxZCRtiF-dTSCnuHZ1nafCeUDlANCxIrsmG4qiHxFLFNjg-wXtAJhDSaN8zpCNv0XKAke-eW-F1HTYCIfHWQKXXQGU-oRysDbVGmefeXqe5DuzVSxJhkVlrkrPYwlBvs80DjxpZEqxZUCkBQG569Oj2Bf5cmMkSnnGDyGMRNSwL7KSa2QLl6TYTwKEenlUbNUqdXezuZH9oVCwFcxx7WsFiN12z1c7CEIjC6VwLoWjZebUI_6MbNG4POH7SBPV8mEBTeJmFqWkfAn-YXg3mpyPcTPYVtXAKls6oAhyAgTiOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پیشروی برق‌آسا در المخا؛ انصارالله به دروازه باب‌المندب رسید
🔹
منابع رسانه‌ای از پیشروی برق‌آسای نیروهای یمنی در المخا خبر دادند. پیشروی‌ای که از شمال به ساحل و از شرق تا فرودگاه این بندر استراتژیک رسیده است. تصاویر منتشرشده، فرار و فروپاشی شبه‌نظامیان سعودی…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/461245" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461244">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef49ccbd09.mp4?token=OaryaMAw82iqHUjKk3EspVQwfqBdwoWzDQ9-fW_VL4SL4oAs71dLUvPXyMy27OK9311IjHBoJ4Rql5lWNtqJiGxIE0Ejnv6N7AFbdSexc_qhMdUknETniBAZ4PZ7XudFMv1a4V2BzcdWY1n7HIdSu0tOk_-W1OTA7WAqlTOIHJutRxlLnElzxxwtEuee93ICAJZ7x9WnzhkOJubCZlvOBlBXh1tgaPBlXR8Q6qNHoRAYDZzScrxKJTHcAJR7h-fWRvUXxUOp2j04cPbVOGVD1hDtRYkdoHjpKDaiVJd6omq8LEzx7VOSTt_XN8KmFhv_E4xINWXdK5EBOW-daHp4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef49ccbd09.mp4?token=OaryaMAw82iqHUjKk3EspVQwfqBdwoWzDQ9-fW_VL4SL4oAs71dLUvPXyMy27OK9311IjHBoJ4Rql5lWNtqJiGxIE0Ejnv6N7AFbdSexc_qhMdUknETniBAZ4PZ7XudFMv1a4V2BzcdWY1n7HIdSu0tOk_-W1OTA7WAqlTOIHJutRxlLnElzxxwtEuee93ICAJZ7x9WnzhkOJubCZlvOBlBXh1tgaPBlXR8Q6qNHoRAYDZzScrxKJTHcAJR7h-fWRvUXxUOp2j04cPbVOGVD1hDtRYkdoHjpKDaiVJd6omq8LEzx7VOSTt_XN8KmFhv_E4xINWXdK5EBOW-daHp4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اعتراف رسانۀ آمریکایی به ضربۀ موشکی ایران به جنگنده‌های آمریکا در اردن
🔹
سی‌بی‌اس نیوز: در پی حملۀ موشکی ایران به پایگاه هوایی «موفق‌السلطی» در اردن، چند فروند هواپیمای نظامی آمریکا آسیب دیدند که یک فروند A-10 یک بال خود را از دست داد و حدود ۸ فروند جنگندۀ…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/461244" target="_blank">📅 14:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461243">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hohe5tKQrLfXQVB1v4bm9kH84bNWuAqbazsNtw2R5EV5ueLVPLbO9oO9oCm80wYGObP0O2ICA6SNKAQuXcW8GbPS7sa5Xu83wDbfUAp4emH3yqingMCG0bLhL88AoIbIcCcScVjzpNz-aufRMRykMiPNi-riKIsz09yYuxUQKFJYj7CQXt63UsOoIg0YbUBn0_5c8Q4mQvfed_Zqi1tc-sDeMQw-36KlwdJgQXiE0g6UKYQWzyLUojinGi1zcOlaSpLutze-bhI6dUbUo7XdGLvz3CqmLdcydrQ-0Lb2VXMfmHbqOPPWdBzPeXq33ffc2ShmSiTGYQfv1_-3DDpd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تماس‌ تلفنی
پزشکیان با استانداران استان‌های درگیر سیلاب و آب‌گرفتگی
🔹
رئیس‌جمهور: رفع مشکلات و تأمین نیازهای ضروری مردم باید در کوتاه‌ترین زمان ممکن در دستور کار قرار گیرد.
🔹
همۀ ظرفیت‌های ملی و استانی باید برای کاهش آثار ناشی از سیلاب، صیانت از جان و مال مردم و بازگرداندن شرایط به وضعیت عادی به‌کار گرفته شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/461243" target="_blank">📅 14:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461242">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1O1NOB2S9ZD8wg1dhhdMiS0KamZ89CKd58aUDcq_E9ABwkp9khLXYuEVO0lpUWcPGlmr3fQqU6aq-VJ8zfQVDVZnjzfVf4MUc2uFMRIsjU_5ESQAy7debc-JDyWbk_MnP7T95ICTTzJ3Mll6gMD2jsmbwXkP0rp05kGda-Pi-Nhjc-EbJKfP-V-2LqzzAVNs3AVi1d5ehDyvuEappnePcjmfl1BTBV-1DUZiQkJXNxitUCTdrRJP5edqrwUaMLKTeU3kIq_TRrLbT2fhtZirBkshZ0Zg6JmM_ML4MDvOpNBoepNvX0OkYTVypVjg6_nUsac73eoxCTDZ2WALl1vNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«برق من» وزیر نیرو را گرفت!
🔹
تنها یک روز پس از وعدهٔ وزیر نیرو مبنی‌بر پایان خاموشی برنامه‌ریزی‌شده، توانیر مجددا برنامه خاموشی اعلام کرد.
🔹
مشهدی، معاون وزیر نیرو امروز اعلام کرد تاریخی برای پایان خاموشی‌ها اعلام نمی‌کنیم و شاید زمستان هم برق برود. @Farsna…</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/461242" target="_blank">📅 13:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461241">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfVEJTIzcnvI_jKi8Lv5bGt5HSALPkLl7w29GP8eZ-4WDvRSBvvBHmqzAkhQVlwT1vcIuH8n-1lwhFy2vOt5vT6UqBsWE7DuSRM3JGfhCgHWijJvzH2A9NrSvY1iI_Hj_bGSXwJ-C1NT_ZSpn-QCAEIUPjnY4WQ-1zSNvgNM3CEC2YsAgRPk56jLSxTiSlXxiZ_d-I3GoB6PQWpvhoI3LWCK_82xjxK6C86x20z7r2ttQFbIlOzNyUxXAGgXmwDIECPtOyQ1yqfnUnjorOXYzU4vDm7STZwMpulXwJ5K8j0ICrk1L98wceGZuCdr62xQGyOBlDzBwdF_xlo8lh8rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر از بیخ گوش زلنسکی گذشت
🔹
نخست‌وزیر نروژ اعلام کرده هواپیمای زلنسکی هنگام برخاستن از مولداوی به مقصد نروژ «نزدیک بود با یک پهپاد برخورد کند».
🔹
پلیس مولداوی مدعی شده این پهپاد روسی بوده و پس از سقوط در یک مزرعه آفتابگردان در ۱۶۰ کیلومتری فرودگاه، ۴ آتش‌سوزی ایجاد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/461241" target="_blank">📅 13:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461240">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">احتمال لغو چند دیدار از هفتۀ هفتم لیگ برتر
🔹
برخی باشگاه‌ها از جمله پرسپولیس و سپاهان سه بازیکن در اختیار تیم ملی امید قرار داده‌اند.
🔸
از این‌رو، ممکن است دیدارهای باشگاه‌هایی که درخواست تعویق بازی‌هایشان به‌دلیل حضور ملی‌پوشان زیاد در تیم امید را داشته باشند،…</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/461240" target="_blank">📅 13:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461239">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgmJt-Ayd3EW4n7V41U7bVMABRKP5_PrOohaWSqX9K3wg8IJ7KmT4iuH96AAwJWi17Y1r9A5ozwyr2nJbWH3Yc4yK1sSquieudWkH0WKPICg3crDqLOzAhQbMXjBMoOhcmalJFH7RVov5WXouDkx2vPdwN0HWFaq3t6UCCte_81_xMYW9-bAkakxly33lbLDMwK4DikUYgBDxc0kHH3XWPYkFj2MdUtl1Vpmu27RspREOPaZhOP8Yl-b-jP8FJOFgESM_EgXQj6Tcr-KFB_aKBKprJqDx8VCo3O8Cpu04UFke86YWh9aWE_86Ds9MK2Cp9yhlb0xX3XxEypGhGbXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکوت آدم‌کش تک‌پا شکست
🔹
سرباز سابق ارتش رژیم صهیونیستی بعد از اخراج از فیلم تبلیغاتی آدیداس بالاخره سکوتش را شکست و با وقاحت تمام گفت: «من هدف یک موج عظیم نفرت و حمله قرار گرفته‌ام و عقب‌نشینی نمی‌کنم.»
🔹
این مظلوم‌نمایی شلو بیتون که یک پایش در جنگ علیه مردم غزه قطع شده درحالی است که ارتش اسرائیل بیش از ۵۰۰۰ نفر را از کودکان و جوانان فلسطینی را قطع عضو کرده است.
🔸
شرکت آدیداس هفتۀ گذشته با انتشار ویدیویی تبلیغاتی با حضور این سرباز صهیونیست تک‌پا به‌دنبال تبلیغ «کفش تک‌پا» خود برای افراد معلول بود.
🔹
این فیلم واکنش مردم جهان را به‌همراه داشت و آدیداس را متهم به پوشاندن جنایت سربازان اسرائیلی در غزه کرد، در نهایت مجبور به عذرخواهی و حذف این فیلم شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/461239" target="_blank">📅 13:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461238">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de0bc5dcf.mp4?token=LndcrV_iowEJlRKuCc68aWFawDLhpOgEH74SVQyBwTXKXC9Nm8M7M8n78vrO3LQ7_FobMQUGhfTy59_CmA_a_Stzpr83W3DhHZ2RzXb07E8XG6iNHfD6hJvfOdL7QnYJUAJsBaP7BxxrO0NI3jZhbM1OKLqPFnp69JwYZs9LTjYfMZ096KAvReWOito98rAe8Y2TzuIjr6x8o9T8jq5bpJ3nDg31a7jd_FnyP4hsoD8alqQCLYwNk6eUv_5WR-LQ8K6P0FhGjopHdZnpCH9QEafOjCcGQnWBPCDyujQ2BKcGBUMCNmdfPBq9WO_ln4gmzNsJ8HdBKx1Q2z8NQu1REoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de0bc5dcf.mp4?token=LndcrV_iowEJlRKuCc68aWFawDLhpOgEH74SVQyBwTXKXC9Nm8M7M8n78vrO3LQ7_FobMQUGhfTy59_CmA_a_Stzpr83W3DhHZ2RzXb07E8XG6iNHfD6hJvfOdL7QnYJUAJsBaP7BxxrO0NI3jZhbM1OKLqPFnp69JwYZs9LTjYfMZ096KAvReWOito98rAe8Y2TzuIjr6x8o9T8jq5bpJ3nDg31a7jd_FnyP4hsoD8alqQCLYwNk6eUv_5WR-LQ8K6P0FhGjopHdZnpCH9QEafOjCcGQnWBPCDyujQ2BKcGBUMCNmdfPBq9WO_ln4gmzNsJ8HdBKx1Q2z8NQu1REoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیشروی برق‌آسا در المخا؛ انصارالله به دروازه باب‌المندب رسید
🔹
منابع رسانه‌ای از پیشروی برق‌آسای نیروهای یمنی در المخا خبر دادند. پیشروی‌ای که از شمال به ساحل و از شرق تا فرودگاه این بندر استراتژیک رسیده است. تصاویر منتشرشده، فرار و فروپاشی شبه‌نظامیان سعودی را در چندین محور جبهه‌ها نشان می‌دهد.
🔹
برخی منابع رسانه‌ای نزدیک به عربستان نیز گزارش دادند که نیروهای مسلح یمن بر بندر استراتژیک المخا در دریای سرخ مسلط شده‌اند. هرچند که دشمن سعودی طی ساعات گذشته حدود ۴۰ حمله هوایی به استان‌های تعز، الحدیده، الجوف و مأرب انجام داد تا شرایط را برای پیشروی نیروهای صنعاء دشوار کند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/461238" target="_blank">📅 13:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461237">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPsGpHE-Hq4l0wJySE3s0in31E2ftg1ET1PCAU9sSV0TtaYMHVmKNylhDRbvr-KCEdI55nWJ6jBiS2StXXto-GUgEURCn2qPsR3gHfO7AK0Ld5OOaBv8bOAuQZ8rXfImKWaiNSgNFTEikINyH30XvBzwmBQk63jjo3agXnLG0sqksCXeROksYVwhlvj6UmfUGbUaW1-meODk_oMrDyzsu9OMr9DKgu-DZDJPP4uWed-hLlaRcUjRM9vB-MzPN3WkyPbyMNxmkFU_P-HXgwWlmJ0bFZFCWDO0-fww9UKoquwo7GJu7uuNGmRgTJQbmpM4Rs9dQeyX1p-HP2SxgmRINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت کرایۀ حمل مایعات نفتی را کاهش داد
🔹
معاون حقوقی رئیس‌جمهور در نامه‌ای به معاون وزیر نفت، دستور توقف دریافت ۱۰ درصد از کرایۀ حمل مایعات نفتی و گازی وارداتی و صادراتی توسط ناوگان دریایی غیرایرانی را ابلاغ کرد.
🔸
پیش از این، دریافت این هزینه از کرایه حمل کشتی‌های خارجی، هزینه جابه‌جایی نفت، گاز و فرآورده‌های مایع را افزایش داده و تجارت این محصولات را برای فعالان حمل‌ونقل پرهزینه‌تر می‌کرد.
🔹
توقف موقت این دریافت، با کاهش هزینه‌های حمل، می‌تواند انگیزه و تمایل ناوگان دریایی خارجی برای حمل‌ونقل کالا به مقصد ایران یا از مبدا ایران را افزایش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/461237" target="_blank">📅 13:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461236">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شکار پهپاد مسلح سعودی در آسمان یمن
🔹
سخنگوی نیروهای مسلح یمن: یک فروند پهپاد جاسوسی مسلح دشمن سعودی از نوع «کاریال» هنگام انجام عملیات خصمانه در حریم هوایی استان حجه با سلاح مناسب سرنگون شد.
🔹
استان حجه در شمال غرب یمن، دارای خط ساحلی و مرز مشترک با عربستان است.
🔸
کارایل پهپاد تاکتیکی ساخت ترکیه است که در اصل برای شناسایی، مراقبت و نظارت طراحی شده بود، اما نسخه‌های بعدی آن به قابلیت رزمی و حمل سلاح نیز مجهز شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/461236" target="_blank">📅 13:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461234">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f7f705f73.mp4?token=UX7D_hSXvDABAYe_TRTSpkhZ5Pg7_xxiwkjXsz5vCWInp7o3CVOTs4LgVXeFjB8qq5BMz5urjQcowqK92kRdfrtJvLfJ031bvlpJJvEn5exbVxZbOT_QMQmFPpHNgM6hc7LRJrgR_6HdQDluur6GMXAohddVhPcaX1Bc0uhbeVoA1y-0RQrwTWX_M2cBZx2dhuGUywnsSdqy3L__fPmLfD2sjPprDbDCMm08C5aBR-9l8StDfrTSvxO6og0sCdB6xGGG92TmPVGu47KLfZPNFXQhR5drE0eGfmTQJ_hVGhsIIS9Rmog3qgWIvVz8e2C22sWCDK5XmmyyWUGJslr-3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f7f705f73.mp4?token=UX7D_hSXvDABAYe_TRTSpkhZ5Pg7_xxiwkjXsz5vCWInp7o3CVOTs4LgVXeFjB8qq5BMz5urjQcowqK92kRdfrtJvLfJ031bvlpJJvEn5exbVxZbOT_QMQmFPpHNgM6hc7LRJrgR_6HdQDluur6GMXAohddVhPcaX1Bc0uhbeVoA1y-0RQrwTWX_M2cBZx2dhuGUywnsSdqy3L__fPmLfD2sjPprDbDCMm08C5aBR-9l8StDfrTSvxO6og0sCdB6xGGG92TmPVGu47KLfZPNFXQhR5drE0eGfmTQJ_hVGhsIIS9Rmog3qgWIvVz8e2C22sWCDK5XmmyyWUGJslr-3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ شهپادی اوکراین به «سوچی» روسیه
🔹
درحالی که هشدارها دربارۀ احتمال قطع دسترسی اوکراین به دریای سیاه در نتیجۀ جنگ ادامه دارد، بندر سوچی روسیه هدف حمله قرار گرفت.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/461234" target="_blank">📅 12:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461233">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281b0f925e.mp4?token=dv9mtOqTrARAA2U4_T4Kj4z0yyY6ha-DvJJ76ahc2TC4D-EVc-bIri0XKEJnGZy2BguTzY1kX8sLtoBofp14yL7B3z8Cws05jheFK92sq2OCJkqBt4JiH9ewZz-mETeh-IBnPhRCbVV2b8P9l-1LRqVi2ngYYuyUQy2rbrOc3EH0ISwsfgOs_Ut_fHNClECQ2modnDBk3zrwIdgDBCVIqsGuQHAeZ8DKgJHUrlY-SifPiNQRUIiW2pLMGJBbUN9DDWFokbO0rk5MAnKv5VTphq5xUDYGpU-h8emd901LUr1AOH_hEaMu5nT98c0c4ZJcoK-68Ui0WOHSsDwtisOT5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281b0f925e.mp4?token=dv9mtOqTrARAA2U4_T4Kj4z0yyY6ha-DvJJ76ahc2TC4D-EVc-bIri0XKEJnGZy2BguTzY1kX8sLtoBofp14yL7B3z8Cws05jheFK92sq2OCJkqBt4JiH9ewZz-mETeh-IBnPhRCbVV2b8P9l-1LRqVi2ngYYuyUQy2rbrOc3EH0ISwsfgOs_Ut_fHNClECQ2modnDBk3zrwIdgDBCVIqsGuQHAeZ8DKgJHUrlY-SifPiNQRUIiW2pLMGJBbUN9DDWFokbO0rk5MAnKv5VTphq5xUDYGpU-h8emd901LUr1AOH_hEaMu5nT98c0c4ZJcoK-68Ui0WOHSsDwtisOT5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اگر ایرانی‌ها سلاح هسته‌ای داشتند، من به رهبر ایران زنگ می‌زدم و می‌گفتم: «آقای رهبر عالی، حالتان چطور است؟ کاری هست که بتوانیم برای شما انجام بدهیم؟»
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/461233" target="_blank">📅 12:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461232">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpZ1nZ82lGIYotoi6jmkQhVdMvMGI2rs6RxrHMtv6QVUOmTsH3wRmEomlx0WMymuvjdom8S51MMo-YP-IShitWuK_ahbeaUa3oHiRNVp38wYjCLu_epovH0qZ3vaLEpO1QUiEO0IwOHfPTJFhPYcPlQ5Dz_N8yxsYOhbcEsly5C9T0cGwTT1N0bCDttOerN-i2Xoxveq55WJDGlsSVVv3KJZu6pFSKcJdUEIICq8iQZQODzFU_9QFRBwD6LkfZTfh9qQIf9STBXvZZI96vhdevmGLvk8YcBEgU8uLpIfHkFcuHjS_9OILpRwmjgUjpG2R8pAs8VungjrLzOMCaPdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: سالن‌های همایش و استخرهای متعلق به دولت ادغام می‌شوند
🔹
در مدیریت فرایند اصلاح الگوی مصرف، دولت پیشگام است و شخصاً بر جزئیات این روند در مجموعه‌ای که مستقر هستیم، نظارت دارم.
🔹
به‌منظور افزایش بهره‌وری و صرفه‌جویی در مصرف سوخت، بیشتر سالن‌های همایش، استخرها و ساختمان‌های متعلق به دولت برای عبور از بحران تعطیل یا ادغام خواهند شد.
🔹
همچنین توسعه و تسریع در نصب پنل‌های خورشیدی سقفی در واحدهای دولتی همچون استانداری‌ها در دستور کار قرار گرفته است.
🔹
از سوی دیگر سیستم روشنایی و گرمایشی هر نهاد دولتی در فصل سرما با الگوی کاهشی کنترل خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/461232" target="_blank">📅 12:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461231">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmlNnzQPc9j8G0XMXaiIYxkoOY6XK4o-TgfxRVpj-I8M6B28F2-_2eA21KFXGvS4OpbwH4IPpHJu-aM_iEWvUAJBWGlgkyWp1yl7R7UEe2bYkDv4dz6QOFBDYdqISeROqhwcN-4_AQozQHUzg92IUhRtUd_LMO8GStBuSHQlGW62RabmWmzI0q42XnlHAQ2ueDmK8faX3kqVH40jhmBwp7I8b3JmS0q2aIvfqHfEsP90SrTNR9JVcEbkxMMrMslednSymFSdIfxDbUNk_YVpXn-LsOta88P_Budda9kMbs15Cr9UdvCHsTXzZ30Qm4q1oKYzwpMHj_8CNTi1FJRS9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزییاتی از بازگشت پرقدرت مبین برای تامین نیازهای یوتیلیتی پتروشیمی‌های عسلویه بعد از حمله دشمن
🔹
شرکت مبین انرژی خلیج‌فارس با انتشار اطلاعیه‌ای در کدال آخرین وضعیت خود پس از حمله دشمن آمریکایی - صهیونی به این مجتمع را اعلام کرد و خبر داد که ظرفیت عملیاتی این شرکت به ۶۰ درصد در مردادماه ارتقا یافته است.
🔹
در این افشای اطلاعات بااهمیت الف آمده است: از تاریخ ۹ اردیبهشت‌ماه با در مدار قرارگرفتن فاز یک شرکت پتروشیمی پردیس و بعضی از شرکت‌ها تا پایان اردیبهشت‌ماه، با ظرفیتی حدود ۱۶ درصد، خردادماه با ظرفیتی حدود ۵۰ درصد، تیر و مردادماه با ظرفیتی حدود ۶۰ درصد، عملیاتی شده است.</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/461231" target="_blank">📅 12:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461230">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg0bkKCxULP2Nu2nrkLcanjr26G7vfbEY3z-MdI-IyamMWSJQ1hIkPIB6h-Wd6PU42iu3o0ATZhGiT-VknQnkFUNUwc2XrgxdFYFEJv7Yoq3415gg9k0KeEOPlVrUAyVrGWrC8weByh-45C6P0T03MbKtHV6b2NGLOy3yGrlt5C7wCLkoeKX60oMauNcmDjZtfsBekj0_k4sHDvFXjb5u3KJzHVtnS8J0AQP56xkPXngHI9hkIHWghamOOZPye_xvZwyxG_fT1xz1lzs4hBJOi3WyqtKmYDW2HSpheHdFZfBcyj3Eday0HbujFV4PfdHjuOcEiPxkSj-9PvBLiaEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
یکشنبه‌ها در پارک آبی اُپارک، بازی‌های گروهی منتظر شماست!
در سانس بانوان، در کنار آب‌بازی و تفریحات اُپارک، در بازی‌های گروهی شرکت کنید، با دوستانتان رقابت کنید و شانس برنده شدن هدیه‌های ویژه را داشته باشید.
🎁
🏆
🎟
برای خرید بلیت به سایت اُپارک مراجعه کنید</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/461230" target="_blank">📅 12:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461229">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/461229" target="_blank">📅 12:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461228">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">اعلام آمادگی رئیس‌جمهور برای واگذاری استقلال به بخش خصوصی
🙍‍♂️
سرپرست مدیرعاملی استقلال: اگر به دولت می‌خواستم بروم، جایگاهم کمتر از معاون رئیس‌جمهور و وزیر نبود اما محدودیت رئیس‌جمهور را درک کردم. او خبر نداشت به استقلال می‌روم. در دولت جلسه‌ای بود که چرا مجموعه‌های دولتی تیمداری می‌کنند. من یکبار وقت گرفتم و برای ایشان توضیح دادم.
🎙
رئیس‌جمهور گفت آمادگی دارم که اگر سرمایه‌گذاری در بخش خصوصی باشد بتوانیم استقلال را واگذار کنم.
@Sportfars</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/461228" target="_blank">📅 12:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461227">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptD-eD_3YhBmWv6gPxVTp4vJE-tMEQNgCPatgjAPzkDmgOyf2UzHwTnNzKmenbLXsyBQptK_SAysMaMgCnI30zO7DQ7HsZsZkAGmcXyVWhGHbWbLkHX_7Ia-cL6GlyYJWwCa7YxadSs6_cIEVIevnblbC5vJectSFMf34WW8a3fdDkRUlimIZFuApa1nBaXn5idsihTNIhWzkG5pyIVj0sHQXHP9wxASWKFc3mc4KQmQuxvkMXEyYPOcE3QcTJcCLB9HvokALQio3w-q98IrGt4mep8Ash7C3eTcVHtpyK40QunaBINSk-j-pdXH04xldVA6JDs-gsnh6oDTtRyp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خسارت سیل به ۷۷۲ واحد مسکونی در مازندران
🔹
مدیریت بحران مازندران: در برخی نقاط مازندران بیش‌از ۲۲۰ میلی‌متر بارندگی ثبت شده است.
🔹
تاکنون ۷۷۲ واحد مسکونی درپی بارش‌های سیل‌آسا خسارت دیده‌اند که بیشترین آسیب در ساری گزارش شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/461227" target="_blank">📅 11:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461226">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXsP5BY2glNC5hldibPLO8r3b_IHbTY4ZnYCX2Ebx7DkMH8IomtXRh0A5egeQf8bvUzGPtkECEvEOwnIcCe2yvEustZ-zylfnsWAuJZJJu_7-O5a7XvogePAKl4UchI8pOIO2YZPKqyBxzVpHXOpaa2QNL1EiWXKg3OPtFJnU1d0H4c-Ydtloe96qeysylRxmUt3zrpAvlamFPOZANUkhyCbSBk-2oJBK01H8i2tiX6purY5z3hhqmk-mxhrCEq2IbPgX5poe21lDJwwV40pRpcZgUAQetncprxYhiNpW-gEL8iwNAZ3FCkKK40n36Fw0fs07p7fti68yf2rVEcL_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح ۹ کیلومتر از آزادراه حرم تا حرم
🔹
۹ کیلومتر دیگر از محور آزادراه حرم تا حرم در محدوده گرمسار-سمنان به بهره‌برداری رسید و عملیات اجرایی پروژه محور سمنان-فیروزکوه نیز آغاز شد.
🔹
مدیرعامل شرکت ساخت و توسعۀ زیربناهای حمل‌ونقل: ۱۵ روز پیش عملیات اجرایی قطعۀ نیشابور تا مشهد نیز آغاز شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/461226" target="_blank">📅 11:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461225">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeXTvMG1ps7RO0pt7M9Xytu-f63ZBUmcdB3kIqzywLGKa7eH9zULxYgrLKzjwjVbCgKSuWTwkT9-NzT3EwfeY0Poovg9e2mSO9Lqn_LYZSKCC4u3yQ0zQx2MAALhhtKwJmX4DdJU2K93csl9HFG2thlub2Z5ZJeBkmYMNk4GfQHvzf0KGbHmsCgIp4wg1K2oJnGikHDgVjNKixSaQsBgDwVqhHOmaPI8njWp59Ho7zgawNSFHivSJxT7TEUQ-rJpX3thsJ1rAsnlDaqMU9Kua9E4btbOin-ljRTMubThjbRPfPlKqYmlNrP_WEi8N564ImN1NMby4xWow5WT-1Tlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ سخنگوی قوه‌قضائیه: فاطمی‌امین و ساداتی‌نژاد به‌دلیل بررسی درخواست اعمال مادهٔ ۴۷۷ به زندان معرفی نشده‌اند
🔹
در خصوص پرونده‌ٔ چای دبش ۹ نفر به زندان معرفی شدند که در حبس هستند.
🔹
محکومانی هم که در حبس نبودند برای آنها ابلاغیه صادر شده و چون حاضر نشدند، حکم…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461225" target="_blank">📅 11:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461224">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a83d26ff4c.mp4?token=W1GRVJa7J225JpOSwhokpmvb7BTiExpKju4Ot_LES95-GRYtOQeqjZO48bwSD2JsL7tCZWxgmlam1c6C8MT5W3KFZ2dCP3uBhPZztnWImI_RoYX3mHG_oHZzYAXWfRMkKBp4AH765mH92r3V0yrpseZhij-HIsEOVZ8ou1JXk1-laOuuO55wMsZRDBUUXnookCbzTpFF8FHZXtBD0YsOTKqt7uhcrhKBj0zGoyCHbv8L26RHGp_GuezOj_ie27MjZLuGd6v6U6d_aIHOjbBTKe6UECLWlBFnsYInAuhaLOkLyTs_Rf6VLu0i5fggB0gDumUN3wNzY0BwGsfacuXX2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a83d26ff4c.mp4?token=W1GRVJa7J225JpOSwhokpmvb7BTiExpKju4Ot_LES95-GRYtOQeqjZO48bwSD2JsL7tCZWxgmlam1c6C8MT5W3KFZ2dCP3uBhPZztnWImI_RoYX3mHG_oHZzYAXWfRMkKBp4AH765mH92r3V0yrpseZhij-HIsEOVZ8ou1JXk1-laOuuO55wMsZRDBUUXnookCbzTpFF8FHZXtBD0YsOTKqt7uhcrhKBj0zGoyCHbv8L26RHGp_GuezOj_ie27MjZLuGd6v6U6d_aIHOjbBTKe6UECLWlBFnsYInAuhaLOkLyTs_Rf6VLu0i5fggB0gDumUN3wNzY0BwGsfacuXX2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: طرفدار پروپاقرص برگزاری دادگاه‌های علنی هستم
🔹
برگزاری دادگاه‌های علنی هم به نفع خودِ قضات است و هم به سودِ مردم است چرا که دانش و آگاهی حقوقی و قضایی آنها را بیشتر می‌کند و از این طریق از وقوع بسیاری از مفاسد و کلاهبرداری‌ها پیشگیری می‌شود.
🔹
بازدارندگی دادگاه علنی از حکم‌ نهایی می‌تواند بیشتر باشد؛ دادگاه باید علنی باشد و برای مردم پخش شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/461224" target="_blank">📅 11:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461222">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcMoqJqpp6OOfliPWeUTTe2W8Uzr8pD7HduCxCYz3Pk6sh5DXiNfsTYUsc8nkvfp7za0T7Wb5VJrzk2_5KqqzkgfrQK7lLTazzswTzv8Ylg1iGNAB3YhRMpTlCHojtBcD5KSXUMfNlnw7KY7nWM-yO3Dwdnvn086gfKgfUE_Rr65a-fk9J1BhUwtYlP6H_6o9b9WGpyvttfmHPSE5NopbYwzBGmPviO8dpJzrBjXz4WTjJFqhA3l0dJ8uwxlrAkAONIzGbICAWH07d6uiglYc6naHIHzXhqukyBtB1XlzReQRuddQ7kiAVE2vYxMy6txoTYOygAN2EsYd6o2tl6oPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IenqW8Mfh8d23pZa-x2Vzb_OhpRrylfDTLyVt0I9UJOKfn2UgMWTLffiKJyAXWR8jsy2F5HjffnTmitKm-OVoxEAlO87Z0w-uQD3SPvmlfU-bG-CuE2W5tazCF6pDGKCMt6PnoF5T_0Khh1_SBmwcErAzJaFRU6k6l-J92upyz8Q-_PVZbLjefw4x52pvvfpxBkMm8GD-QX8_Dla9XEig0Xaz6uvub8GZmi9I00XgRspiAKXiBwd7xUH6582yO5QzWExdUH1SJ3NI_x9ImgiEjiMxVvHAflRmHOfceAz1-XQR2ZpYV5K6AoqIlJFDBWQkwkndy2V_MgaISzuN3h7_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: شرکت نفتی آرامکو و پایگاه هوایی خمیس‌مشیط را هدف حملات متعدد قرار دادیم
🔹
یحیی سریع: دشمن سعودی جنایتکار حملات ظالمانه‌ای را علیه مردم ما انجام داد. ما در پاسخ به آن، عملیات نظامی مهم و گسترده‌ای را انجام دادیم که در آن شرکت‌های…</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/461222" target="_blank">📅 11:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461221">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8605b20068.mp4?token=D_fQiX9V1zOyLyzN5RxUsCBY7akt--_EuMzGvScyk0hVYNzBIAi-Ri-jXAt3QbfsyraLYWhlrUg-GhUj_AFvzIsyCzUdP75f79tv0CtV1DhosNGrTxxRQ5VpCFCustpYrQlBTyyU2xgy0s5K8z_vsKV_l0Mmw_tAQTga8j4rWwZnSy-eIn8PHwq4YmtMx1dWsz87TI6HnHQsWA_8kUbcUNzdeONm0FzfUXCCbvry6yXo_vPWSgKf4mUXGxye-vVrixpCyzBMUnbeEwCBNgoe0nGDrLWNxK7C7M546tfMW6k27osHFvgQRUHgmbomzQHXbw3C7lNwm2xU3ENQYP5lyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8605b20068.mp4?token=D_fQiX9V1zOyLyzN5RxUsCBY7akt--_EuMzGvScyk0hVYNzBIAi-Ri-jXAt3QbfsyraLYWhlrUg-GhUj_AFvzIsyCzUdP75f79tv0CtV1DhosNGrTxxRQ5VpCFCustpYrQlBTyyU2xgy0s5K8z_vsKV_l0Mmw_tAQTga8j4rWwZnSy-eIn8PHwq4YmtMx1dWsz87TI6HnHQsWA_8kUbcUNzdeONm0FzfUXCCbvry6yXo_vPWSgKf4mUXGxye-vVrixpCyzBMUnbeEwCBNgoe0nGDrLWNxK7C7M546tfMW6k27osHFvgQRUHgmbomzQHXbw3C7lNwm2xU3ENQYP5lyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تخریب عجیب یک کاروان‌سرای تاریخی در سبزوار
🔹
رئیس میراث فرهنگی سبزوار: کاروان‌سرای روس‌ها یک ژاندارمری و بنای تاریخی در کنار کمربندی شمالی سبزوار در دوران پهلوی بوده که در زمان اشغال اتحاد جماهیر شوروی، نیروهای نظامی در این ژاندارمری خارج از شهر مستقر می‌شدند.
🔹
این بنا سردر باشکوهی داشت که برای ثبت در فهرست آثار ملی اقدام شده بود. طی این مدت هم منطقه‌ای تاریخی شناخته می‌شد و در نقشه‌های ابلاغی به‌عنوان بنایی ارزشمند معرفی شده است.
🔹
تصاویر منتشرشده در فضای مجازی دربارۀ تخریب این اثر تاریخی توسط شهرداری مورد تایید است. مجوز تخریب احتمالا با جمع‌آوری استشهاد محلی صادر شده.
🔹
با توجه به نقشه‌های ابلاغی این تخلف محرز است و آن را پیگیری قضایی خواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/461221" target="_blank">📅 11:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461220">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31609f5c7e.mp4?token=sdDhpp-2rJcAavxoN6OH0GiHSXo0KGnrl3D51WzqynomxeB8c-fMLV7tczoS348aD3VHlhgbw7M7r7hEH4OYe-pDBCumQiZ8QgURWRk6ZSJHssmVr-QUeJVCBrbXPwDka_zt--NvK-4o5XRbaypogp870_BcpGEkTMA2NSz4BB3om8RHM8chy7XYC9z6o7IuC68gO3P_lVuPF0OBfloUMQogl0cqDkj0bdyuzvYTu5r5Z9pkMNRM9aJlhgYuckygPaFlOowk7HcO_8bt4iTUvk6TjGzOjenVhx7Wsc_yevZ6QuawLHn6L3peRxqdkRA-tksz_teSAKfh_m4q9I6kFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31609f5c7e.mp4?token=sdDhpp-2rJcAavxoN6OH0GiHSXo0KGnrl3D51WzqynomxeB8c-fMLV7tczoS348aD3VHlhgbw7M7r7hEH4OYe-pDBCumQiZ8QgURWRk6ZSJHssmVr-QUeJVCBrbXPwDka_zt--NvK-4o5XRbaypogp870_BcpGEkTMA2NSz4BB3om8RHM8chy7XYC9z6o7IuC68gO3P_lVuPF0OBfloUMQogl0cqDkj0bdyuzvYTu5r5Z9pkMNRM9aJlhgYuckygPaFlOowk7HcO_8bt4iTUvk6TjGzOjenVhx7Wsc_yevZ6QuawLHn6L3peRxqdkRA-tksz_teSAKfh_m4q9I6kFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امضای پدر رهبر شهید پای میراث سردار سلیمانی
🔹
نسخه‌ای خطی و نفیس از میراث خانوادگی سردار شهید غلامرضا سلیمانی، پس از بیش از یک قرن، پرده از بخشی کمترشناخته‌شده از پیشینۀ فرهنگی و دینی این خاندان برمی‌دارد.
🔹
کتابی در حوزۀ اخلاق و احکام که در صفحات نخست آن، نام و امضای چند عالم برجسته از جمله آیت‌الله سید جواد خامنه‌ای، پدر رهبر شهید به‌چشم می‌خورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/461220" target="_blank">📅 10:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461219">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj4sFBNqCMjTvlXswLqxRtb4PZdlCeVKTRqikntgPlxfXWZVi0Rjxh_g5VJIIPt3mCEZoGwRMvwCeDpah7JDMJ7Wy-jNElM0fC8czpL_JX63A0bi1MANY9WVdu_EnzE-DRFtCaOr6mEoGGTbxOp9zsS9fyiIHSpRTl2X4oaIiIwfG11E2x1uTAss9VVrTdjg4ohxu-PLnj8OFj5h5t_zd0VnREPoo4BPzvMwysjC1kv2o6Gnps--ipnveX5JrMIWVngBbjXtI47GDeqNODnAvmNRINKS2bWFh8vyGUfzpH3C6v8rQ8WVn0waCipd9n59KqBX5bpg77HUMw8XIHSV7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر صفوی: جنگ‌طلبی آمریکا، شتاب‌دهنده برای انتقال وزنهٔ قدرت به شرق بود
🔹
مشاور عالی فرمانده معظم کل قوا: جنگ‌طلبی آمریکا، بهترین شتاب‌دهنده برای انتقال وزنهٔ قدرت و جغرافیای اقتصادی به شرق بود.
🔹
تظاهر به فتح نشان شکست و قبول چندقطبی شدن قدرت و امنیت بین‌الملل است.
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/461219" target="_blank">📅 10:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461218">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بازداشت گردانندگان کافه ازمیر بروجن
🔹
روابط‌عمومی دادسرای شهرستان بروجن در چهارمحال‌وبختیاری: گردانندگان کافه ازمیر به‌دلیل ساخت و انتشار یک کلیپ مبتذل تبلیغاتی در فضای مجازی، با دستور قضایی بازداشت و روانۀ بازداشتگاه شدند.
🔹
این کافه نیز به‌عنوان محل ارتکاب جرم پلمب شده. امسال تاکنون ۲۰ فعال فضای مجازی متخلف تحت تعقیب قضایی قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/461218" target="_blank">📅 10:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461217">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWC_rOnvok1n38iC8t0pu5QLku13sphSxdS4aoojXcx74HgxV25qGb0EHLANE-tLi9g1qxrtVAHkoG5sElCGVtQ72C4mKyKemNmiH8D27yEkywmT-MgEsesOkyWPs9st5BwbvfrgfY_LzX1pSfXTM2FgvXn_6KMMlBsLHb9nDB2T1QYxEaetbOMTUsx1u70wEhwYEHw1oPSWC316APSGKZVRy9zdq6qnLHYuAgnvUziLMGyrf4QM1c88AEmYmhUXBAp9wQmhkS0eLvKND7cFCpZ6TpNNsHya74vO1SpEy7_JDHjiJamE9iM_TgTmPcPsLVbdd-Vt4GJF3xt62eetVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسری بودجۀ آمریکا در ۱۱ ماه به ۲ تریلیون دلار رسید
🔹
دفتر بودجۀ کنگرۀ آمریکا اعلام کرد کسری بودجۀ دولت این کشور در ۱۱ ماه نخست سال مالی ۲۰۲۶ به حدود ۲ تریلیون دلار رسیده؛ رقمی که در صورت ادامه، تا پایان سال مالی افزایش خواهد یافت.
🔹
براساس این گزارش، بدهی ناخالص ملی آمریکا به‌تازگی از مرز نگران‌کنندۀ ۴۰ تریلیون دلار عبور کرده و اکنون هزینۀ سالانۀ بهره بدهی بیشتر از هزینه‌های دفاع ملی این کشور شده است.
🔹
«مایا مک‌گینس»، رئیس کمیتۀ بودجه فدرال مسئولانه گفت: «بدهی دولت آمریکا به طلبکاران خارج از دولت از اندازه کل اقتصاد کشور فراتر رفته و صندوق‌های امانی برنامه‌هایی که دهها میلیون آمریکایی به آنها وابسته‌اند در کمتر از یک دهه با خطر ورشکستگی مواجه خواهند شد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461217" target="_blank">📅 10:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461216">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsCoCtyPRbFx3jpJ5yc_VsYDP1jsroWhjkGAhd__szbsuEpdKU7RWUDskSUyhciLciQy1-QvBV7T4CKIKqYgiGkvn_yd4Oq84YMqlz5y5gZtg4tqXQbWAGKO5_8GkUZr7jdHPw8ii4F2m4H9QOMNPbEFBpo1VrLUr4R6g9vtnD5AtINeVulSIlcXXDsP8u0LJlP5ft_Qp35Jkum1cRkX7HK5aIVQjqZM0lUJhissUHQVTHvL18sybGPm8T6RDMTAwE4tUs4g5j6IcY3zxw04qVJOkFua5zO5dPPxL5zz2x1qokbAqZwWNpmcP-7nCGnj6t8FZKNjVU_c32viA6vR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461216" target="_blank">📅 09:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461214">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b5538027d.mp4?token=v7IqmQ4-TTel2YkbjoZ36V-RTchaPpIQpVevbCKF8KsXkZzLe1dYDNg4OYulHIn_IYmsEMV8N8LKk4ybHarAPgm8v5_B86zvLftYdQnh8V7U4N538fbIi3Ymp_p0HVvABaDEhDh8GjnloNQR7_DZHDpkekGZUO3WmKGEP_90Wv1XC4rAe4AjOvfdDMxMwunI2M5U2gPrKtkJ7VPqjYIrG8KOXOJJNbvVwDS9V4Ybr2w3qRvZKPUNTY6ezQKiaIB35zXU-Adg3pbrkxe6ZqVnZSs2nkEGIOlYf0HM7v1vO827vXaiqDicGoTouz6P8gVSWA1b7x8aILa9w44neBwbRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b5538027d.mp4?token=v7IqmQ4-TTel2YkbjoZ36V-RTchaPpIQpVevbCKF8KsXkZzLe1dYDNg4OYulHIn_IYmsEMV8N8LKk4ybHarAPgm8v5_B86zvLftYdQnh8V7U4N538fbIi3Ymp_p0HVvABaDEhDh8GjnloNQR7_DZHDpkekGZUO3WmKGEP_90Wv1XC4rAe4AjOvfdDMxMwunI2M5U2gPrKtkJ7VPqjYIrG8KOXOJJNbvVwDS9V4Ybr2w3qRvZKPUNTY6ezQKiaIB35zXU-Adg3pbrkxe6ZqVnZSs2nkEGIOlYf0HM7v1vO827vXaiqDicGoTouz6P8gVSWA1b7x8aILa9w44neBwbRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش به جان کشتی فیلیپینی افتاد
🔹
آتش‌سوزی در یک کشتی مسافربری در سواحل غربی فیلیپین، ده‌ها مفقود بر جای گذاشته و جان دست‌کم پنج نفر را گرفت.
🔹
سخنگوی گارد ساحلی فیلیپین نوئمی کایابیاب، خبر داد که تاکنون ۴۳ نفر نجات یافته‌اند. او گفت: «ما به عملیات جستجو و نجات ادامه می‌دهیم.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/461214" target="_blank">📅 09:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461213">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjzfOkHKf6vUSIznqShazbq4W93loJYmWI1K1DLchsHWYChqPAKNGhFtWZOUkZP2bbq23xDK4pz8FpTr_XqwF7VoIRIjLi584rmJMKMzMV7qXlX89rN7L-7Q13vPclJA58gFoNCV7-xmjt_fHFsFGMkpgnAbl0E2by7k2w-TAIEkPmoPg_v7oF7VD88wIhivAO3bHgpbcIAb90f2HBgLsNRTYagksdJzOYAk41epe8I2pGrnnKttTHNc9fXuJKRHztCW0VW6GaKHQCNrL5M_sBMz1tSxxU6d6eNCFmQa64lMDiWwq6iBjuK4ykrZMUCegyz3sKF1HLrMcesxAzOAMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار حسن‌زاده: آمادۀ عملیات‌های تهاجمی برق‌آسا هستیم
🔹
فرمانده سپاه تهران: امروز آمادگی داریم در هر نقطه از کشور، با سرعتی بالا حضور یافته و دشمن را در هر وضعیتی که باشد، نابود کنیم.
🔹
زیرا ظرفیت ترابری سریع و عملیات‌های خاص و ویژه در سال‌های اخیر طی تمرینات مکرر حاصل شده و این رویکرد تهاجمی، پیام روشنی برای دشمنان دارد.
🔹
ترامپ جنایتکار و نتانیاهوی ملعون امروز پاسخ‌گوی افکار عمومی و نخبگان خود نیستند. آنها مدعی نابودی نیروهای مسلح ما بودند، اما امروز نیروهای مسلح مقتدرتر از همیشه در مقابلشان ایستاده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/461213" target="_blank">📅 09:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461212">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f53df36bf5.mp4?token=RHnHD_81VdXt9sP1OuTimq280zrKy4-EeJewvkPxa45XpemmI30Y5-I5GbW5SifRZgspoPXkul-JySSM7gW8T_gSnHqRzP0leSdnxE1z2vXDUJri3BTOm5Jb1BmIg70klTn8JRbBVGTaoI71FjJFZzTeYrm4JJv6kBVQmlbn_hJOPeuiblRyo9QPt237G4NbAfwGxky6DqSniBw3hw8gRlMWnRLQIoD2X6AtnJmBstB6n9BTcRC8J_87dd2ZA4G8JXS5AxaW06RZuqkS_KZgoIef7P9fEW9uU-O8yUi23cxw8X8DWwI6mpvaumD-bY9o-C66Bs7DmCAKYy7VZObkqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f53df36bf5.mp4?token=RHnHD_81VdXt9sP1OuTimq280zrKy4-EeJewvkPxa45XpemmI30Y5-I5GbW5SifRZgspoPXkul-JySSM7gW8T_gSnHqRzP0leSdnxE1z2vXDUJri3BTOm5Jb1BmIg70klTn8JRbBVGTaoI71FjJFZzTeYrm4JJv6kBVQmlbn_hJOPeuiblRyo9QPt237G4NbAfwGxky6DqSniBw3hw8gRlMWnRLQIoD2X6AtnJmBstB6n9BTcRC8J_87dd2ZA4G8JXS5AxaW06RZuqkS_KZgoIef7P9fEW9uU-O8yUi23cxw8X8DWwI6mpvaumD-bY9o-C66Bs7DmCAKYy7VZObkqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: امروز و فردا در استان‌های شمالی بارش‌ها ادامه دارد
.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/461212" target="_blank">📅 08:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461210">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">منابع عربی از وقوع چندین انفجار شدید در عربستان سعودی خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/461210" target="_blank">📅 07:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461209">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsM6jfy1rNSumucZ0GeAT3pj7Anu_Zrn2OcMQGKKyg1ijoFjZiao_5zzNPf9XVZXrFABYE0r1A3VcZNVhxPDaea7nBcRsFOtocBdViISyezpLp8M9T0UsjwK6foTOvGQjlUKo91VdFDbQO9ob9zthxU-gtMBxriVcgU6TbV9zshvszj5wNbEDFeNGGor3irFj8mxHGyUUa931rmAdISttBhziXIt7tl8Sc740HCpjq4ENdjhzInlS2D3vkRdHBrq3inf0SrK2daXIspqOKUkG9KpT-mUtPFFl_-xUDwcxXiHy5zM3m4JTUzz1dTWr61S3JSdtPFvWZU4hHZlx1AFjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپلمات روس: آژانس اتمی باید به ایران تضمین بدهد
🔹
میخائیل اولیانوف، نمایندۀ روسیه در سازمان‌های بین‌المللی مستقر در وین، طی سخنرانی در جلسۀ شورای حکام آژانس اتمی گفت که اگر این سازمان می‌خواهد بازرسی‌ها در ایران از سر گرفته بشود، باید تضمین‌های واقعی به تهران بدهد.
🔹
او ادامه داد روسیه اصرار دارد که برای از سرگیری فعالیت‌های راستی‌آزمایی کامل در ایران، به تضمین‌های واقعاً قابل اعتمادی از سوی آمریکا و اسرائیل نیاز است که آنها استفاده از نیروی نظامی یا تهدید به آن را از سر نگیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/461209" target="_blank">📅 07:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461208">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">منابع عربی از وقوع چندین انفجار شدید در عربستان سعودی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/461208" target="_blank">📅 07:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461207">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99dc1cae7d.mp4?token=bXRdQD8iW0IK4BbfQ7W5kqB-B-0dbpWFWp4n1DsUBNhoFOZ_YhnOAcbqCQzhouz2c4iqwNLdTdFIcdANqCQwR_eP7t8YpVWILX--F4pDOoO6rQOjCh10MJ-V0uvMLBSC1SwP5hasgbDUi8Y4g2je5wQBpM9Un-t07o2UB5NW-SBrc3657B1xIkp7kT9vdh0Hne2_Lu_iepAUDrIHbHZ-jsIGstIKcb16zXZQr7pmiXrPLpCwbQU-ntPQ1rdnHRjcfXKrPGpfAQQ2W_ssPGK0tdtry_bC7ZE6bLurBsZuOVPIIrJt-I_d3EckkPNK8iJmHxPI587Y8M7yqi-LJEbV3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99dc1cae7d.mp4?token=bXRdQD8iW0IK4BbfQ7W5kqB-B-0dbpWFWp4n1DsUBNhoFOZ_YhnOAcbqCQzhouz2c4iqwNLdTdFIcdANqCQwR_eP7t8YpVWILX--F4pDOoO6rQOjCh10MJ-V0uvMLBSC1SwP5hasgbDUi8Y4g2je5wQBpM9Un-t07o2UB5NW-SBrc3657B1xIkp7kT9vdh0Hne2_Lu_iepAUDrIHbHZ-jsIGstIKcb16zXZQr7pmiXrPLpCwbQU-ntPQ1rdnHRjcfXKrPGpfAQQ2W_ssPGK0tdtry_bC7ZE6bLurBsZuOVPIIrJt-I_d3EckkPNK8iJmHxPI587Y8M7yqi-LJEbV3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع عربی گزارش دادند همزمان با فرار گسترده و تسلیم مزدوران سعودی از شهر الیختل، نیروهای مقاومت یمن وارد این منطقه شده و در فاصله ۱۵ کیلومتری بندر «المخاء» قرار گرفتند.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/461207" target="_blank">📅 07:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461206">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
سپاه: آشیانۀ تعمیر و نگهداری، آماده‌سازی و محل استقرار جنگنده‌های F-35 ،F-16 ،F-15 و شلتر جنگنده‌ها مورد هدف قرارگرفت
🔹
روابط‌عمومی سپاه: ارتش تروریستی و متجاوز  شکست خوردۀ آمریکا از روی استیصال چند کشتی تجاری-نفتی ایران اسلامی را مورد حمله قرار داد.
🔹
به…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/461206" target="_blank">📅 07:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461204">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipnaR18EzhiyLdJpsRdWxgG74qQKhK_HvP5bWYfkRG5a_dhOdEPggVnTifheUgMUSqcWSx4iVr85Mi_a_ayC8WHkQlqlGhG7FEynUi6IeEDxvMj_vyf8gHmegthLsI-Dd-qJ1lJGYtrVclL_FLYN8ouEY4iW7vxLnS4RbqRqFC2fwPjD1vX2EETcl-hrfjmsrnLn6NeSpG4BX_2BnqRQOcq3JKa4gvk06OXaBs1zhcTPQxnoIYTrYG858_G8pEgLoruJ18z_sYNMz1YNM2_sJEaakT_pUL_qqfieVAQvlkvqjdFwjb3ar5D7hyAMe5JiFPP3JHSGjMv3KyENWJWJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار یک زیرسطحی هوشمند آمریکایی در تنگۀ هرمز
🔹
نیروی دریایی سپاه : یکی از مدرن ترین زیردریایی‌های هوشمند و بدون سرنشین ارتش تروریست آمریکا را در ورودی تنگه هرمز به دام انداختیم.
🔸
این زیر سطحی هوشمند از جدیدترین تکنولوژی‌ها در حوزۀ زیرسطحی در دنیا برخوردار…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/461204" target="_blank">📅 06:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461203">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a665296d9.mp4?token=jJJyyq3p9n6vW32U5hrfCHnlzG90zP7gcjXv3OplIBZZI1EOl0ccp4wtCNrj7IQQYifPsdvAE33mw7sChKS3ustVgjI3lUtJmom5PPhCMscj92koJxdCCdWpnNLJKRyiBktFbkCJBnLvNcBc23c_InCSsDRJr3szOCZzLgoKRHnTjAvt30T4m7NuKmYt87ZE-FP5pJaqheyD473sN7VEQh8CbRQcJZ-yZT7HlTjo7RsKgXDpzU4HyXwJWlS4bDWs_BITgPJ176WZNnNDx4KxvHhyxBJwSr0M9rbD3EtSjdEdhO0fUs4fQyNzAaqIaUMvF9qJjrIueLcOBB5bET_n5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a665296d9.mp4?token=jJJyyq3p9n6vW32U5hrfCHnlzG90zP7gcjXv3OplIBZZI1EOl0ccp4wtCNrj7IQQYifPsdvAE33mw7sChKS3ustVgjI3lUtJmom5PPhCMscj92koJxdCCdWpnNLJKRyiBktFbkCJBnLvNcBc23c_InCSsDRJr3szOCZzLgoKRHnTjAvt30T4m7NuKmYt87ZE-FP5pJaqheyD473sN7VEQh8CbRQcJZ-yZT7HlTjo7RsKgXDpzU4HyXwJWlS4bDWs_BITgPJ176WZNnNDx4KxvHhyxBJwSr0M9rbD3EtSjdEdhO0fUs4fQyNzAaqIaUMvF9qJjrIueLcOBB5bET_n5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاوه‌گویی دوبارۀ ترامپ درباره تنگۀ هرمز
🔹
رئیس‌جمهور تروریست و متوهم آمریکا با تکرار ادعای پیروزی در جنگ با ایران، مدعی شد که باید نام خودش را روی تنگۀ هرمز بگذارند!
🔹
او گفت به‌نظر من باید آن را تنگۀ ترامپ بنامیم. ایران در حال فروپاشی است. @Farsna - Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/461203" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461202">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN-rjpuFlfYOrcCAAgsZxsMirsIuii0H2eBc6venI5Bh663hJ3qysI7Iv1949hxz1MLxzccXgdTW6zPYVgdAXhSjB4FxiQgqBw48CsrGWi263MBpL23vGjDXX-RGKL6j_LMLKNeTiH1JCh83TgU6_DpEPO-nJ24-daRCzj5Vc8W-JAPUwkoNP1BI4LPl69zSW0htsQoojOtrqFX3jEUcoQTzuMFCnRGh9t-XSvf4DCosVVdyaUH99G17XG7y_33pxKQHXEBUNCVolLLqiMw37DpuVJGy-Zk4VuZcN3QfakYybMwhAi4xPIylFog5qx3Cc3q1YN8g4AeVJJNz2WvvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه تهدید به استفاده از سلاح اتمی کرد
🔹
نایب‌رئیس شورای امنیت ملی روسیه گفت ممکن است سلاح‌های هسته‌ای در شرایط خاص، یعنی تهدید جدی علیه امنیت ملی روسیه، مورد استفاده قرار گیرند.
🔹
او گفت مسکو می‌خواهد جنگ اوکراین هر چه سریع‌تر پایان یابد، اما فقط طبق شرایط خودش.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/461202" target="_blank">📅 06:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461201">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDebxjjbgZKpTNRPU6RpBRJruALcPURZM62UWJ0HolXnNDnGXDdVwPw-LxDkvtYi4BQD73x-BAa1xMGH1b2SdcYW3cfndqxbwJpF7_9TGCplgLC5tQnMjvTj7BoWRhVJ04GYD1ve_Y_mQc8NMP1DNqqB7Ycq7uu1rK8sOAlz8Axbc2Y4DNBVIuwRY2zKX-F5Xef6bFynzY23_b4LnFdRjbBdDaSBDnRzw-qkr2Dewgyc75k93zKqcMicVHbFZUsPnaO-g1Gq6DYtkE2CIp_RJCUX50ZaWOk0_PPYR5UzkNcr76C-1JFStcJ7Q8KLt8SHzUqOqma14lPBK_WfA0LJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه‌گویی دوبارۀ ترامپ درباره تنگۀ هرمز
🔹
رئیس‌جمهور تروریست و متوهم آمریکا با تکرار ادعای پیروزی در جنگ با ایران، مدعی شد که باید نام خودش را روی تنگۀ هرمز بگذارند!
🔹
او گفت به‌نظر من باید آن را تنگۀ ترامپ بنامیم. ایران در حال فروپاشی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/461201" target="_blank">📅 05:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461199">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شنیده‌شدن انفجارهای مهیب در جنوب عربستان سعودی
🔹
همزمان با فعال‌شدن آژیرهای هشدار حمله هوایی در شهرهای «خمیس مشیط» و «أبها»، صدای انفجارهای متعددی نیز در این مناطق به گوش رسید
🔸
ارتش و نیروهای مسلح یمن پایگاه‌های هوایی در «خمیس مشیط» و «أبها» را که جنگنده‌های سعودی از آنها به خاک این کشور حمله کردند، هدف حملات موشکی و پهپادی قرار دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/461199" target="_blank">📅 04:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461198">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ded3bb5c.mp4?token=Bt-shynPI9H2cB4xY1v2qX5LC_Lvnugd4K6o6L7JpYEA6Er83CaT-Uu0NU0oQMx2zBiTYEQlyIMXVcEeFQ7dkG7zGeExCrx_RAds0ddyjQeHYr8BsFGGFwCbvsVzZDeOv2s33zxGeEacdk64hqknYgce1ckfsw3wZJZ3CPfRMsdsxCCK00LQ0jeYhC_t2O-SX-1K-eU5VcLrKSsbJJG8XdYVio5lmlUVTKi3rKOwyI9a3PgRXEaKbjQdlWtLysIWlmVEXdxxulugNM8bASMo1_M-3NbZcQjh9XOtwy41mrzRAfxr3dQSz9ztJIbfQ6QdNcDqjLg0f_kdPV1GKVYd9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ded3bb5c.mp4?token=Bt-shynPI9H2cB4xY1v2qX5LC_Lvnugd4K6o6L7JpYEA6Er83CaT-Uu0NU0oQMx2zBiTYEQlyIMXVcEeFQ7dkG7zGeExCrx_RAds0ddyjQeHYr8BsFGGFwCbvsVzZDeOv2s33zxGeEacdk64hqknYgce1ckfsw3wZJZ3CPfRMsdsxCCK00LQ0jeYhC_t2O-SX-1K-eU5VcLrKSsbJJG8XdYVio5lmlUVTKi3rKOwyI9a3PgRXEaKbjQdlWtLysIWlmVEXdxxulugNM8bASMo1_M-3NbZcQjh9XOtwy41mrzRAfxr3dQSz9ztJIbfQ6QdNcDqjLg0f_kdPV1GKVYd9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش‌ها از تسلط نیروهای یمنی بر شهر «الخوخه»
🔹
گزارش‌های اولیه حاکی از ورود نیروهای مقاومت یمن به شهر ساحلی «الخوخه» در استان «الحدیده» است.
🔹
از سوی دیگر خبر می‌رسد که نیروهای یمنی بعد از به دست گرفتن کنترل پایگاه «خالد»، به کوهستان «النار» رسیده و با مزدوران…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/461198" target="_blank">📅 03:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461197">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش‌ها از تسلط نیروهای یمنی بر شهر «الخوخه»
🔹
گزارش‌های اولیه حاکی از ورود نیروهای مقاومت یمن به شهر ساحلی «الخوخه» در استان «الحدیده» است.
🔹
از سوی دیگر خبر می‌رسد که نیروهای یمنی بعد از به دست گرفتن کنترل پایگاه «خالد»، به کوهستان «النار» رسیده و با مزدوران سعودی درگیر شده‌اند.
🔹
همچنین منابع عربی گزارش دادند همزمان با فرار گسترده و تسلیم مزدوران سعودی از شهر الیختل، نیروهای مقاومت یمن وارد این منطقه شده و در فاصله ۱۵ کیلومتری بندر «المخاء» قرار گرفتند.
🔹
همزمان ارتش یمن نیز مواضع مزدوران سعودی در المخاء را با حملات موشکی و پهپادی هدف قرار می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/461197" target="_blank">📅 03:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461196">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎥
خسارت سیل به ۷۷۲ واحد مسکونی در مازندران
🔹
مدیریت بحران مازندران: در برخی نقاط مازندران بیش‌از ۲۲۰ میلی‌متر بارندگی ثبت شده است.
🔹
تاکنون ۷۷۲ واحد مسکونی درپی بارش‌های سیل‌آسا خسارت دیده‌اند که بیشترین آسیب در ساری گزارش شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/461196" target="_blank">📅 01:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461195">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">برخی منابع عربی مدعی شدند،
چندین انفجار پایگاه هوایی ملک‌فهد در عربستان سعودی را لرزاند
.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/461195" target="_blank">📅 01:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461191">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJhjvaX2Ijd2wf6BxvM90v3jhqVhjBG8gt4YGwRDdXFDG_8qnw5BrckocxzXzhVNuupnNtO0Z2U7z7uzgtWJ7Iz3bqBafnCqcQgbOQEgvoih0_8CG557rlZFtTBchq2-pRXS_mvPY_dQKt4h0NgK-WSFs_KA-JZXH9YmyzfYwSuI-c0YZyF4cmqMkiH20woO9wa0SweC7OIPkXPyUEh9TrEj7xTLeWFeViSj_fIZLky3ip-iVRkVghoDK5Xu45epJSUEa4Nxc4-JKLXxYpiWXKx46KEUNRL1CGHkChywBBZ22oHHJ_8bUJRnP8d8IwSmKBoOpm-mDobSouRuDqJVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1P9Kg_GMhvkMrqyyW1wALR6WLnmL8sCFz23gSp0kR2UBVoI93y7IIC25LwiFqmUNexCcgHFnaslVsbfowaYJcO5DIoZGRb_EAe8AZ3jKFBe7JicD9yAiHectaj83evyErJejq0w7-GuFU-O_UQ__7a-baZCH5qvr6EqcxSxzBHuPUpxg1g8Xmpj5rG5JTqjfUscvh-l-4htbUxdr3jk2wa5-dQ1pHXxjFJ_WCNrcg11tsZLzseVcLCYeuQ2gwss8tQUH-3AYT8HD3Lc7tvzF2P3C331YNHgGmCsiRFAGwt9OBnIcTBBI6K0kB9tEtabRsH0eaf-uFS5XSK0rnjCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIwqMKqbaUJ5M0kyvibNvsIzVA7tjNfBz124tMG0Xs8sOUATHcEDdaBB72sK1k0W7UUNjkYaUeZh-DEXiygEd8Y6Dt3cZXQBDH46J-uhDaUYc_SWZ2vvg9PqrnviVFhb7dMUiQ4tiCOqp8O3hkSuUMLyjUFU_dum86q4b_ZjrXtVtB83xWWNcAEYf0b_PpqNIyxl97v2gY1_CEK0x4wftoE8TM1pzQhtnUHzkCbOj-mXQGnLP8jokZgMueIErNsxul1QShl_Pw2Rt_vcd6T3rBe4Muvs5jxgkh85ZbK3K3CY6odzmsqz_MgmICelY2mf_cUlPMp_A2N13CANRC0ZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q847adB6iJOMgI6ncSFH01qf9DYsSjgGLQXdklXm4uTDeI4B65nFbXUq4Jvy5ReJCOs3t2vKTFNHyuUbId29u2IQwbkvb8VMf58AWZ_rpoQ_jPgtwdnifM7VB_myHobiV4-0rLs6PFGZ4EkpUkieTQXiWHwIG167OVnKkJV2QaP3yug3S49UdSyTcne2nAFoqYV3dr-xYhhea5qH00-N_YQTuWJHXOzq77PuTBfxHFV8OVpWzCRqX0ACVNBmCk6x0WqGX5b1CVXhuscTckAtRVkkVk76zCIaH-JeCkJtAimB3ZFQb2ljayICPppWpC4lwkRMGtlZIist-A0Gx0BMWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۱۹ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/461191" target="_blank">📅 01:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461181">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mNtayaibfOfwLqxwyLPF1mD7nozHF3nyGsY_D6wS_p5PgBx-qedIx6AWEcGTQGZEoDYvnrFHZ9DuNTB4Ca48NnAy9UHOXKsBcm34zAvDOm5JiMY6r6kqe57EpS4DCAViIACJkM8wMD2Erjf9E5DEeWf0kGQVZXE-lXox4uAK8Mhfz0zPu5wZ9uFOfnYx0gTqwDHWp28GeVuTlh8R_i5Fd53whg8Dm-3tHFKVa2hto9xy8iqEiSooIxibYI3YWjF8n8JrZfkvUnSaGIEZS-df9sV_DUJEpwD0p5tfZ6FYKmvsoFvat7q14NqwscRwg7ro5_RfRVePkiRhfiWBB6zQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pd_-sH3Q3RYavOOueMpZlc6WU4cYkV6A9yFCiVDQX05neOb9I45I5TCN3QXuyHEq22Qw3x4sNZR-U-qIpw2SAxpm0viIFAdfDGfb7-pbdPH1aaHY5PHS3vapqAioVtBrG9nX7giA9sxFlBtEWBzWXbi5PACynebHzB_JEelVz6YAfuBfG_3zgGOkvG6qV4NrczggnInx2xUHJkYAPOOG-K0ZWePbEP-3FdhtYegamr8A3tpu_8AA5Npzc5jLPSWmiNr-MklcgjxlW_kYSDtNglCDlSAVkWWAh8A_qP7hTO2huVOoAf9oG9SIooSyW5JcSbP0k_pXEp9cGluIxJZKFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnBvdMs0rgjZuaMA10FBlhiXS0WG8TZIvfZ3TsYE4t_oSwnciibBcPLi4il5vySPqueigCDJ10KCIzSejYKicNUsr392tVazuLrOdlhus15ybJq_fLk3PmBM4saShUyMR1sGVSfweTwfckAg02fox8LxuDvYyiO3CnsU5_px71u6ACCMLwiP5-9AkPg95X1YPkEMS3MQq-5QeBRLGIG3NY7B0fiHeOalhq5hwla8i7aGeiZIDVCtSY7KbrxrL9j6lIrtpnn6-g9YGnb0os-A9C4GZqRJrNaXGCtE6GvKQnNm6SAJkqRaKRYyNKBTL42IzXPfasiIHQVW9K8iTK_VjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkQrZPGNYFAaiv225HUPhSYc2Sck73Z243PCNpSuEbi2EOFwEeDYFDRGOQ6xEusmErkLc6-2alAlAqaZuS1J2f_VgpRf0LMRg0_0ZpjmVDbmj9m7yNQ6GLVPfVHwjLF6ZIOh_jkeYTZ69JnzVypwkxi-yJivbCye7TGxx0YM9o3QXgPbWRA5ob8z8ROqm6p2exZLyqPAQdD1sJ3JMjW_FnDnBpc8pUC5K58wO2fhlhArV3f4t-w73cpugk-R-0Zp9i7KPAF7tH9s6_si0AIfmemq0IhARACP7VozlwsNuvNldoBqGEQJQN9WWrFjeDr3_kgcsvw2YAjwK9EA5WTgzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3wzzZ0YGLCEDf-stuohJJn_2vtL-yH4TOC0XTKy32-NeqJmm8JLm3cwlpGeb9fQyyUTmKt73RYes2JTw7X-YhfFkwogr5q3VzijOvLGOK_6WDilbNyu8-B0bd4VXR79I1pPIy29lFxZqVMjq1HDmYje2cDYJFNLWJbltxs2a-i8UXIQAVhdAPHzFSo7sQgq1Bdb-8X4Fr23beL0ht-mZjnzyVMtO-9vSpE6YGQqgMeUS3j5IPSnujNRF98mPA1OlwtRul4HBDdmr398AwEahljNauuGSHpDd95BpXGLkh7PaJ8XG6IkOamceY6FYekl47hKJJgWCr9KEZEH0xFBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jD7bC69SYaSKTPJ39PYqj38NEnTOQqWTttbX1adfi76iqxwDMrJHZj1qk9fLbcS5f1dM6t-vBpKww18Q9rHS94LP0z49b6kG2ac5BYH97as6sNuoMQPyrWHyrX7Qcvqn7gJwLASEo_saTFFwFO6LYbLf9hGcV-jESUe1KGxep4zm1mG3wQu9rASymeAQyXd_IAcHSZD5PAzzVe2KJFtjV6h32jihL41jJimYehr1uYmLACnQVOiJi6fatUXWJog9xGutsnqKY7VEHuZK_aRn_BnRI9hqYb-_q-oWppmiFHw8w5qZy5cvxnSEh2cbL_jA8UIDX4f5WT_QZA52KPh6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SF0UYIpozHL6jTgh21TuLFy1-luR5WJLynYTRkcGZZoWAdrxhSudaUifxFSDwkZuHfgWoIz1Un6CmVQCE9inEPAfvFJObJagS1qpmre_KDusq8VUwQJrFH8oxl3hG90BJFnSYKGx5MHctdM60ZlgSVdvGQzYGtg1tCspkxv9sYenaMDUfOQaoT0ZA74bKj0A0hYDq7pNFBhwcJFwRoKPUAWyIgOORYuWElt9yobBU8qYxNyRRKTQwIY5NpFyCMq8SZGeN57eTmCPAIyh4ZPGRUtgCtZcWCkBrZuW-nZQN__mHv_FIMgw9-lPMGgouXnnFZYrJ7nVTKSb-Z3BPSoOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pB2lJdHSiU6k6nrzhfTHnu_2_MHbQjXTW4FMORdt__TYdONINkfmnPXEeXYc9SIZDSTX58zYNJoYIzwJNtTa02gtuNWttHFS6BQ-PniDjgP4akaGMagTPyBaV0ByofektVFRPN-JDxS8Rl3NwKwgVcQDD4dVaMvnyF6CiuZYrPMsM7EDT7dp12RrFu4Mtpsmf_3F0iVya6XODmoVh5x7nz1PIgnO4jJtnymovsSGzNOrRv0ApBWloEjDYmberQk4QBQyIVmczjHnAqOnWs0aL-5BMrKlMN4p7EIe5dc6ZEkzunz3xsWwnBjIL8CBBjId_ZS5aJpP2s0wAMfERuk2xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-MouBFJuedEaDBagE0taiwq6RBDCCPiqFpsw9F4_xQQOp_b8F-SOmLdQPgtsxRhnIKh-N_xKj-B2PpKAKTZJImb8KBIPY3HcLaAkDL0aE77GpAjc9oLTwixzvQvrtXPHq4IMDniSBIWxG_WbQN5dMXI2NIE7qlT6rxRE22pG3LKmC3doGgieTrvLa5XEoI9fkzxXLKMMb5mB76KgiaV4eMgk3xnP3syIiDC2MRLeaMCSXo_E3LHn5yd1pWb8G5RpOeUFKDIDfZZmz_El06Os4vhTrJ7BRq8kKPaE8OkB_OORMCwL88km0t3nqo-UJJiTXmH4iRRHvfS86vgMJg0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4kjrhx2DnQYZ_7ETQdSiRrhxidAbo2WbjlewyDlKbUjPuHSEh4_-ZzSGDmUk91Fuli7NhKltW2BiEkqIa8ERzHUxkNRLXFf2mBzAGLzPgMERQr5ABsjrxG0U_QqcXbDCpEwJaNxzm5cUMUY2Dqs6YwrJ5jINZJmVDLobC4bmi0DVWFSpB47BODo7-wP1olNP87tzHMpJjrahROqhfdTgKIXbknpqydZhDlUUSmxiXHRMOWMUPuDTMiGmWOVrNTDp5HhRr83BMV3p4e2xdkwsSEpFO4ajN4mqPvnLjreLMOGHBHKsXNcK7bTwitbOYEhiqEKAssvjRk-RXs5VhJ1VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/461181" target="_blank">📅 01:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461180">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLBlHK6nd2G5U7uLUZcOLe1EWKjSH4bhWDmn9-I5LrjcTip6PtoFic6oW_24ogF4GJzcXqZXtghlJB1SZL2EaIR2mppQ8yX1xEdaERvbMYhzdQaD0QCuIzQycP_dNonomnQGKbngFxCkk_Cjn-l2Km6LX_hTx62qAGJALFr-z97Ro5_o9Lu8nhdWo4vAzcMfhosVQmDmRgHzRXtM2zl46pofjH9CpWX9LE5BvBMYJ22aisCuNjkE22SYM5NvOkJcrVqrkNlXx0NLKnAFLtHLV19Lz9M-ryiosmkD1MMqWxkN-MI7fLbwRPsW54n5HKaY5zqzT2M6eRoScK1BkHMAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: دروغ‌های وزیر خارجۀ آمریکا در رابطه با مداخلۀ ایران در موضوع یمن-عربستان، نمی‌تواند جای واقعیت‌ها را بگیرد
🔹
سخنگوی وزارت خارجه در واکنش به ادعای بی‌اساس وزیر خارجۀ آمریکا مبنی‌بر مداخلۀ ایران در موضوع یمن، نوشت: دروغ‌های مارکو روبیو نمی‌تواند جایگزین واقعیت شود. انصارالله بازیگری مستقل است که خود تصمیم می‌گیرد؛ نه از کسی دستور می‌پذیرد و نه نیابتی دیگران است.
🔹
ریشۀ بی‌ثباتی در منطقه را باید در مداخلات نظامی آمریکا و سیاست‌های سیطره‌طلبانۀ آن جست. اگر واشنگتن واقعاً خواهان صلح بود، تنها یک گام ساده برمی‌داشت: به بدسگالی‌ها و مداخلات بی‌ثبات‌کننده خود در منطقه ما پایان می‌داد.
🔹
صلح در یمن با بمب و فشار خارجی حاصل نمی‌شود. صلح با مذاکرات صادقانه بر اساس نقشه راه مورد توافق طرفین آغاز می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/461180" target="_blank">📅 01:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461179">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">زلزلۀ ۴.۲ ریشتری ششتمد خراسان رضوی را لرزاند
🔸
ساعت ۲۳:۴۷ دقیقۀ چهارشنبه، زلزله‌ای به بزرگی ۴.۲ ریشتر ششتمد در حوالی سبزوار را لرزاند.
🔹
قبل از این هم زلزله‌ای به بزرگی ۳ ریشتر، این نقطه را لرزانده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/461179" target="_blank">📅 01:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461178">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzq6pT-_3Fc4HNlKOs7SercoCKV4_zDPkdLmLfIT3Qo5tknTI4Qqu5tpp18ODcMGMQBFxcDUX0vv-4BHDjgA-3Xep44szSn1Ch-CvcCNBiQGO7prbN_Z6RlW0dRM-koWupQkdahsYPHTIepVVbEkxRguoTngFKe_XxW5BaVvehHpN6Bn4Ktn_rzEPBkHPINUHta4BqlHhZpLz53juP9M-8NkEi8GsQYYv6kP5VpSfkFkPMN57FHs-SD6_Jl1Q53jkpif6LUqSQzo6Bt3fxXLzTcuah1Zehz7YKOfx1bRNYhuUK9i4TuFlJEx14eWd6WVbNLB_N9_3TL6vhaZHTVAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژیر هشدار در شمال فلسطین اشغالی
🔹
رسانه‌های صهیونیستی از فعال‌شدن آژیرهای خطر در پی حملۀ پهپادی به شهرک‌های شمال فلسطین اشغالی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/461178" target="_blank">📅 01:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461177">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">احتمال لغو چند دیدار از هفتۀ هفتم لیگ برتر
🔹
برخی باشگاه‌ها از جمله پرسپولیس و سپاهان سه بازیکن در اختیار تیم ملی امید قرار داده‌اند.
🔸
از این‌رو، ممکن است دیدارهای باشگاه‌هایی که درخواست تعویق بازی‌هایشان به‌دلیل حضور ملی‌پوشان زیاد در تیم امید را داشته باشند، لغو شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461177" target="_blank">📅 00:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461176">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چندین انفجار در قشم و سیریک
🔹
دقایقی پیش صدای چند انفجار در مناطق ساحلی سیریک و قشم و مناطق ساحلی شهرستان میناب گزارش شده است.
🔹
استانداری هرمزگان اعلام کرد طبق گزارش‌ها، صداهای شنیده شده در میناب، سیریک و قشم از سمت دریا بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/461176" target="_blank">📅 00:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461175">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opv6gcEKS17aN-vnTwmWGs_YcHMyWbQxI7KlabTFW8BGU1q4iox3Il7FH0eG0k_5IVVY2p8eYau4UR2Yd0fTVySpuPZ1l9DIMNr9ZiQpn8xU53gTKoRPcCJmcP1_VxfgWhb8EyppRQTxI4pusXocTlZ6jPEO52zbej8dkVUpsErYyPvNSh91ojT78r5fdCfKNbkV-xp22BCUyeVWhhOdD76_LO2PpTlH8X8ORnb17-d9tbdZi8nmVI-aGHjnb36w764hqSlzbPgCwPjKymgo1fF4dYz-AEhvPKLNb0nJ5L--sb9jKYXWdYKSW-GWRPueYqKlbcXV58eGPo5LrlmbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پناهیان: فقط یک نفر در دنیا گفته جنگ ۲۰ سال طول می‌کشد
🔹
حجت‌الاسلام پناهیان: اغلب کارشناسان دنیا می‌گویند جنگ آمریکا با ایران طولانی نخواهد شد، اما تنها یک آدم در دنیا گفته که جنگ ۲۰ سال طول می‌کشد.
🔹
این حرف که می‌گوید از مردم بپرسید راضی هستند جنگ ۲۰…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/461175" target="_blank">📅 00:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461174">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQGxCYJT5lWatvvjsDmOmKMe4C_E2HDrIDCWHDy-MoObUXRsVZ4kJ24c6bUQemRoIy2MuaE56CIHZ3vDDQ5i4Ugq5edp2b3g2qpDqLGa1JnWClU3O0d3YCoeD71XtBpt6NMNcl-W3HHtOYMz1Pga6dOoUQznRTpcCrHXXZ7WQs_rW2x4GDE3R36OvIrC7cKUUFKwwWs7gBI9KrAiox5TXMEr2Xo8LEykpH9k4usG_D3qsj8-Dfi-EM4tehwTnIu-EVTAynHu5_siGPh8bjPlUAb-WBA3k1WSM2ebLU5oxFqmR_rca5k-VbuhLbUqHmLJUTFvDeeyMJi42la3fZsfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی تغییر را می‌شود در عددها دید
🔹
بعضی خبرها قرار نیست فقط یک اتفاق را روایت کنند؛ پشت هر عدد، تغییری در زندگی مردم جریان دارد. از کوتاه‌شدن زمان توقف کامیون‌ها در مرز و تقویت شبکه برق گرفته تا ساخت مسکن، ایجاد شغل، گسترش خدمات درمانی و حمایت از تحصیل دانش‌آموزان. در کنار اینها، پیشرفت در سلول‌درمانی و بازگشت یک بازار صادراتی هم نشان می‌دهد مسیر توسعه فقط از یک حوزه عبور نمی‌کند.
🔹
در این «بسته خبری امید امروز»، سراغ خبرهایی رفته‌ایم که نتیجه آنها را می‌توان در زیرساخت، اقتصاد، علم، فرهنگ و زندگی روزمره مردم دید؛ اتفاق‌هایی که شاید هرکدام یک خبر باشند، اما کنار هم تصویری از حرکت در بخش‌های مختلف کشور می‌سازند.
کشف و انهدام شبکه فساد ۷۰ میلیارد تومانی در خرید گندم
🔸
با رصد و اقدامات اطلاعاتی پاسداران گمنام امام زمان(عج)، یک شبکه فساد ۷۰ میلیارد تومانی در فرآیند خرید گندم شناسایی و منهدم شد.
تقویت شبکه برق سلماس با ۲۲۲ کیلومتر شبکه جدید
🔸
تاب‌آوری شبکه برق سلماس با توسعه ۲۲۲ کیلومتر شبکه و احداث ۶ پست جدید افزایش یافت؛ اقدامی برای تقویت پایداری برق و پاسخ‌گویی بهتر به نیاز منطقه.
۲۲۳۳ واحد مسکن روستایی در گیلان به بهره‌برداری رسید
🔸
بنیاد مسکن گیلان ۲۲۳۳ واحد مسکن روستایی را به بهره‌برداری رساند؛ طرحی که به بهبود کیفیت سکونت و توسعه زیرساخت مسکن در روستاهای استان کمک می‌کند.
ظرفیت درمان قلب در خوزستان افزایش یافت
🔸
با افتتاح بخش ۱۶ تخت‌خوابی CCU و نوسازی تجهیزات بیمارستان سینای کارون، ظرفیت ارائه خدمات تخصصی قلب در خوزستان افزایش پیدا کرد.
صدور آنی کارت سوخت در ۲۴۰ مرکز تا پایان شهریور
🔸
برای کاهش زمان انتظار شهروندان، ۲۴۰ مرکز تا پایان شهریور به سامانه صدور آنی کارت سوخت مجهز می‌شوند.
۸ روز از زمان توقف کامیون‌ها در مرز بازرگان کم شد
🔸
زمان ایستایی کامیون‌ها در مرز بازرگان ۸ روز کاهش یافته است؛ اتفاقی که می‌تواند روند جابه‌جایی کالا و تجارت مرزی را روان‌تر کند.
ایجاد بیش از ۶ هزار شغل در شهرکرد
🔸
طی دولت چهاردهم، بیش از ۶ هزار فرصت شغلی در شهرکرد ایجاد شده است؛ ظرفیتی که به رونق تولید و تقویت فعالیت اقتصادی در شهرستان کمک می‌کند.
۱.۵ همت اعتبار برای تسهیلات اشتغال جوانان
🔸
سامانه تسهیلات اشتغال‌زایی جوانان با تخصیص ۱.۵ همت اعتبار از سوی وزارت ورزش و جوانان رونمایی شد؛ اقدامی برای تسهیل دسترسی جوانان به حمایت‌های اشتغال‌زایی.
حمایت از ۳۳۴ هزار نوزاد با «کارت امید مادران»
🔸
بیش از ۳۳۴ هزار نوزاد متولد سال ۱۴۰۵ با شارژ و فعال‌سازی «کارت امید مادران» مشمول حمایت‌های این طرح شدند.
ایران در جمع پنج کشور برتر تنظیم‌گری سلول‌درمانی قرار گرفت
🔸
ایران به جمع پنج کشور برتر جهان در حوزه تنظیم‌گری سلول‌درمانی رسید. همچنین با تولید داخلی، هزینه درمان‌های مبتنی بر سلول‌های بنیادی تا ۹۰ درصد کاهش یافته است؛ دستاوردی که می‌تواند دسترسی به این درمان‌های پیشرفته را افزایش دهد.
۵۰ هزار بسته آموزشی برای دانش‌آموزان کم‌برخوردار اصفهان
🔸
کمیته امداد استان اصفهان با توزیع ۵۰ هزار بسته آموزشی، حمایت از تحصیل دانش‌آموزان کم‌برخوردار را گسترش داد.
۱۶۰۰ نفر از خانواده‌های ایتام خراسان رضوی راهی عتبات می‌شوند
🔸
با مشارکت خیران و مراکز نیکوکاری، اعزام ۱۶۰۰ نفر از خانواده‌های ایتام خراسان رضوی به عتبات آغاز شد.
ظرفیت میزبانی زائران حرم حضرت معصومه(س) افزایش یافت
🔸
شبستان ۸ هزار مترمربعی حضرت زینب(س) در حرم حضرت معصومه(س) افتتاح شد تا ظرفیت میزبانی از زائران افزایش پیدا کند.
سهمیه عمره دانشجویی به ۱۰ هزار نفر رسید
🔸
در گام تازه نهاد نمایندگی مقام معظم رهبری برای تسهیل عمره دانشجویی، سهمیه این سفر به ۱۰ هزار نفر افزایش یافت و وام سفر نیز در مسیر دوبرابرشدن قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/461174" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461173">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89df592991.mp4?token=ReQCryMM8z8XH6d74-Bv9cBTS5e9G2uI-wK-1z8KOrCM8cXwPzkNpKAp5aRJJf6yT8cq_7Mvbn7zuNYx7n6VMu-BMxCFWONdMhWbais1eIPlPI9NgwU32hE153zIQaSmRvtL1LcSUl89VCqbrNO-WjQdVsYTztafoysW9fmXrlAA-IN51bFWKC09GnQS8xhEgF8e3dJ6mC33nLdHiU47-ElVW--Z2NdulRxp_BtEYEmaGXJpuOXBvvgf_mDSIjsWspa04xSQoLA5Hx1P4VpQ7Xus5Hfzvtg-cH5LsivvZxAue7p9HSZvysKxIacyVqdaLpuKJsPe2KeD_2mF4R5jnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89df592991.mp4?token=ReQCryMM8z8XH6d74-Bv9cBTS5e9G2uI-wK-1z8KOrCM8cXwPzkNpKAp5aRJJf6yT8cq_7Mvbn7zuNYx7n6VMu-BMxCFWONdMhWbais1eIPlPI9NgwU32hE153zIQaSmRvtL1LcSUl89VCqbrNO-WjQdVsYTztafoysW9fmXrlAA-IN51bFWKC09GnQS8xhEgF8e3dJ6mC33nLdHiU47-ElVW--Z2NdulRxp_BtEYEmaGXJpuOXBvvgf_mDSIjsWspa04xSQoLA5Hx1P4VpQ7Xus5Hfzvtg-cH5LsivvZxAue7p9HSZvysKxIacyVqdaLpuKJsPe2KeD_2mF4R5jnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۹۳ میدان‌داری مردم فلکه صادقیه تهران
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/461173" target="_blank">📅 23:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461172">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qs_FE2xrFhmgegUvXTincHjWr2F54HoCaXqOPiJhal9Au5Te2gpgaCno3tjgnur5tflFEeMA0uzI5S3vZtrTBF07BJYtGlSmaHguOwVka3q5vnzM4BeGCiyQkMv42-bsIcwOjYvZ1IFSiYxtolf-k6BJ24_6nEpigPZVQ1NZF93V3YgAhz_MQpIBIRfMeuhlUCgCx4wb4gGslpulRr-qlyDDkDVI4rnaamc0kduFy56rtTWuzSztSfewh6Jab5ceTaF3OxBFHhzkkbBD2gsXFRwuWIjTKURDJlFXJCtBcBSGCxivGwNpZZJew5_ZPyo3skMe6dI24sE87dEDEF10-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
وزارت خارجه: ادعاهای اتحادیۀ عرب علیه ایران مردود است
🔹
جزایر سه‌گانه بخش جدایی‌ناپذیر قلمروی ایران است و تکرار ادعاهای بی‌اساس تغییری در واقعیت ایجاد نخواهد کرد.
🔹
ادعاها دربارۀ مداخلۀ ایران در یمن هم مردود است؛ ایران همواره بر ضرورت حفظ وحدت و تمامیت سرزمینی یمن تاکید کرده.
🔹
امنیت خلیج‌فارس و تنگۀ هرمز باید بدون مداخلۀ قدرت‌های خارجی  انجام شود و ایران دراین‌باره تدابیر دفاعی را برای صیانت از منافع خود اتخاذ کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/461172" target="_blank">📅 23:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461170">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac07f4e91.mp4?token=ucpozVOv-_S7iXqyOpaQ8AZXOp4v7i6DOLopqY_fzT5lvPxMBXRqN4F44cKg0ewl9yfOtHf1Z9Mq0f9rb8Y-Sy6u1rBcCaYtWvnPoQmM5X0BBZSEsH-mIMkbAKEd00tREX24zCUsHzngmDKthNzjn29Jy2LSjW2vWKDt_iDDxHplLraORvsf2WcC0npVUVSVTt4jpJqQEc5mqydI-a6lxg6jzv0c17wrBzKrz9Ngp96wPNnnjljlXep3xabZCc37M34bd5yq4J8nZcb7txSVSeBDdqPON2GJYA07zeSHr5poFY3lIirAZ7QR7zhg-hD5ljBuDZSLE7cTx9hMJWLwlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac07f4e91.mp4?token=ucpozVOv-_S7iXqyOpaQ8AZXOp4v7i6DOLopqY_fzT5lvPxMBXRqN4F44cKg0ewl9yfOtHf1Z9Mq0f9rb8Y-Sy6u1rBcCaYtWvnPoQmM5X0BBZSEsH-mIMkbAKEd00tREX24zCUsHzngmDKthNzjn29Jy2LSjW2vWKDt_iDDxHplLraORvsf2WcC0npVUVSVTt4jpJqQEc5mqydI-a6lxg6jzv0c17wrBzKrz9Ngp96wPNnnjljlXep3xabZCc37M34bd5yq4J8nZcb7txSVSeBDdqPON2GJYA07zeSHr5poFY3lIirAZ7QR7zhg-hD5ljBuDZSLE7cTx9hMJWLwlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرار مزدوران سعودی از دو جبهه حیس و الخوخه در نزدیکی باب المندب پس از پیشروی‌های انصارالله
🔹
بر اساس گزارش‌ها، نیروهای انصارالله تنها حدود ۳۰ کیلومتر با بندر المخا فاصله دارند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461170" target="_blank">📅 23:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461169">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNcRijN17fR7ZkNpqJw0HNjUJq143ohGWgVYoFPrqBKVnGjzchq6ZMagUqerptk8vq2_pchZ3aIIlt_v_XnwESz74W6ikB5JKqIgLR3erCWJ88nSS9NRM8K0Ia43nqglKqtWv9KWej_JEj6or8J-zTx5vN_ch2BSiiphMWHwaZ8B1SGITeSmSjN-XbuhYByd3L02brw2zX87ZX0QyxThqzl-8eF9xQpLcfePQAkbVnu8rJY1tqt0c_e8lkksL4IXIhDTn2o9i5fJUcv9kjK5wu9ciEX96VXE-lKaVub4BYZkQR8V2mf3m_XdEjdg5VTLx7Xjsj_8t98mPgIKm56hcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر نروژ: به هواپیمای زلنسکی حملۀ پهپادی شد
🔹
هواپیمای زلنسکی هنگام برخاستن از مولداوی به ‌سمت نروژ، هدف حملۀ پهپادی قرار گرفت و تا آستانۀ برخورد با یک پهپاد پیش رفت.
🔹
مقامات اوکراینی هنوز دراین‌باره اظهارنظر نکرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/461169" target="_blank">📅 23:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461168">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGC8BC1Hvb1pQft6GQ_8dJAlnAMmYbeZCQaqEZQNv4wfI5gOm3bQd3f7Ze33Thtmi4zkNg6oSbk6MzJtzQkf2idvDIpd1E2vNfZa7hYXgLYXmf2YtgodMecx05UvXwFYRvL6tOvIoI5pMDdb2vjAmMxCnZSOCrbPXjZdzGp4W0tSk6fijTcwiHGyD5S8xF04QoX4w7VIRGmfAPD91-DUI6l15Xel_sNCJZWltkuyqlSUuI0QEDMEMbBYcjvihMjQnIYQAojkCi2kSjNFelqnUZUT4SW9gd4B79FvyzKgnlwivepmSUgqoiLMJubU2UfBJSqDOeaNMIrX4BV0ABzw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت «ساواکی دوست‌داشتنی» و «آمریکای قهرمان» چگونه ساخته شد؟
🔹
یک آتش‌نشان زیر بمباران آمریکا در جنگ رمضان، برای دختر ۱۲ ساله‌اش فیلمی وصیت‌گونه می‌گیرد تا چیزی را به او ثابت کند که پیش‌تر نتوانسته بود؛ چهره واقعی آمریکا که دخترش تصویری فانتزی از آن در ذهن داشت.
🔹
او بعدها در مصاحبه‌ای توضیح می‌دهد که دخترش حرف‌های او درباره شرارت آمریکا را باور نمی‌کرد؛ چون رسانه‌ها تصویر دیگری از آمریکا به او داده بودند.
🔹
این یعنی بخشی از جنگ امروز، در ذهن نسلی اتفاق می‌افتد که هر روز با انبوهی از روایت‌های رسانه‌ای روبه‌روست و حالا نبرد اصلی بر سر ذهن نسل آینده است.
🔗
ابزار رسانه‌ها و راه مقابلۀ ما در این جنگ شناختی چیست؟
اینجا
بخوانید.
@farsnart</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461168" target="_blank">📅 23:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461167">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGwNqnj44R0NVQSs2EJIgcltRGXqJyf_ga0shpqT7MDgL7k8kAtS_6EQ5OR-BDGWOYKd9M082TMHwbkHwZhCK2LeUWN8ndDW3XGQcyxF0CLEzBo30yFIwxMgiiOhpMzTet1DyVqcEbH3h7DFPvdZH7wi7XJAQt3l6yOgrN0YLyoMWn3NgjAWrPr7uC5eEgPeujxv8Cxcdb6ZOeGqexyxycVNx25IszY1s2Au9XcavdNyE8ymY83M5L27bPscYU9qXfomdCyjwhS5MQI3htE3LU5HEyFLB08B9OuGQXfsRGr6WzSdBBFRBfWGghrxmT1VxUQs6fjlk1IKNEBiiUv-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رهبر شهید انقلاب: بهترین سال‌های جوانیم با محبت و ارادت به جلال آل قلم گذشته است
🔹
جریان روشنفکری ایران که حدوداً صد سال عمر دارد با برخورداری از فضل آل‌احمد توانست خود را از خطای کج‌فهمی، عصیان، جلافت و کوته‌بینی برهاند و توبه کند: هم از بدفهمی‌ها و تشخیص‌های غلطش و هم از بددلی‌ها و بدرفتاری‌هایش.
🔹
یک نهضت انقلابی از «فهمیدن» و «شناختن» شروع می‌شود. روشنفکر درست آن کسی است که در جامعه‌ی جاهلی، آگاهی‌های لازم را به مردم می‌دهد و آنان را به راهی‌نو می‌کشاند. و اگر حرکتی در جامعه آغاز شده است؛ با طرح آن آگاهی‌ها، بدان عمق می‌بخشد.
🔹
در روزگاری که من او را شناختم به هیچ‌وجه ضد مذهب نبود، بماند که گرایش هم به مذهب داشت. بلکه از اسلام و بعضی از نمودارهای برجسته‌ی آن به‌عنوان سنت‌های عمیق و اصیل جامعه‌اش، دفاع هم می‌کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461167" target="_blank">📅 23:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461166">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5emOncCSrPocWClLDyWA66SvhY_seO3NL9ceIkeKhkFg6JKbZ4N_-4qD0d7L6EzeEm800IiM2dwwfOglo_pmPQtZaFqU_tet1FzXE1AxIFlFacuZDaJA9oIgr5DzPMyMGIvLclKClRlMUahw2neXTQ5yza73WEVMc_RfVYe1-GvOBzxRnJR08MkXveyEGOUUNgvvN1f2WnpMcu6kkA7lmh4l1wzEEeumtUUgSuQI6CaEZuwUhoCBNvcbdhV4UxCIm8MmmeIQu43DPuVsptSwEyzuhXEVn0evzhP03SRukyeuR9Z3w_1QenMStatF7qE2dymY4MxOOliCbRpuYlo-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: تهدیدکنندگان زیرساخت و تمدن ما صلاحیت داوری ندارند
🔹
تصویب قطعنامه شورای حکام علیه برنامه صلح‌آمیز هسته‌ای ایران به پیشنهاد صاحبان بمب اتم، عاملان هیروشیما و ناقضان برجام، نماد استانداردهای دوگانه جهان امروزاست.
🔹
تهدیدکنندگان زیرساخت و تمدن ما صلاحیت داوری ندارند. ملت ایران بر حقوق قانونی و راهبرد انرژی صلح‌آمیز هسته‌ای ایستاده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461166" target="_blank">📅 23:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461159">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJt3ZGW7AUhXB6esC6K4lLfSM4cviPUdTyVYePoY14-7x69yqgP0Wft22DEXuXJM8YHrJU8a4fwTTYGCTIxGUmvUpalXMV1zmu1lWjQmE7kRyw2QlXXYey8TaCzp-Ufe6LDk2d2x8SiAHywjw5VXk9PvWnsO-zCajbcer1cNP0U2rblt-DUH3_coMz87KrysJ6DAmk9ZNmPeP00SBbdgs3P5Y1eGp4qRbd-1uNxrMid4pmUO1CIN4F7SFYP1_VHPuxB0hMBlZa-LIEWBtA32nIkPIMe75ZgOpVpSMch2emdmyGezTzdPvKu9uval88SLXeCYTNtsMsnqU0P_vg-K8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq9n3LzvYwMzhj1iLdqw-Ti9BfuKMCY_TCUjkQb5m4qfJcRMaVIXMTbVgXv5lFQgQ4H2ABvcSYdmrxiZ1Uz0HqjEB5X6x-O08NuxlXne_d6QJiDHleBniklC56kpp8hVYAmOUHlbGQov7Cii7XIcT88A_5zOYaIItl5mmtGIWcba66Jurb91tRqUZ8Fnr5YlWUMuvzdqe7lX3yA8C7Rl_56LeW-whS-hQKjvTdaizyf1QAYUin2pjbWsHP6suWsJi-nxVaVB4NS_Lrlu1djiRqNteyzi_qFj6xsAY4lhnyW7eOSJjPNtod-CB8-IrRQwsvnbqrn0ex0wIeH-hvchqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2JzCQKKG01vLEJftHERta6znSWNZI_5fVjttRFBEXW552d8IzT4vFaYoYUDs-LUgIYbjwht3xkUBco0XOiNtRBnSONLUn47lMWi6P8P9EZ87T2nZp48BJOhbBFDlA3DksFenztoe71ErGS95zvFNt8IYLvopby0uYaQC1_oyBv0Y5LRL2eYAuMCb3UEh6WiBXi6Mlona2efBLs4nZWCFkl-ffw0MH1reTR0QMkZ5gMGhOHFFs0tR3Ay7o9xHJA3Fxu2aLFE3TRGYwLiev8ffEOSMe_KZMoTawIRh4-M6E0kgQSLoF2RyAvgT_9vIGdp-bjtiZ_UPxGqA5x93lwmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oF9YC6IqgEBSZhAURJSKJ6hZotLg8ydW3VC7AT1BvAISGfPk6YBOO90HpN6-Dh46A2_n_I9mNQbuWR82osHJoS3eMdhLfTglTgPHliFAOy2nrhJlbhgWgcbuXgiWxt_eLoxDQmH4q_SyKvf9j5M_ByChLNc7d9JM31mteMTKPji4l7xCW5Fo2yIHi2C3cNRApGuzkmrlILP35dSr9JL4gJJDBY4Rx3MEwRGWvckAJPfqzIaE8IeyTH0Ch6yVH8qHVkxwMwkpfwJJYEWYYj-Kq_AITcDZRnSTj1bk0fj5haV_7ZMcBFsSv2_qPpndw8Nm57GP97axY5av5lgBpn1ucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOk0Thj1Rl1CS0n6WYQOWv09qIOlSWCTI8SMwhe43ZF8-HOksxD0ywqyJESD5cpSpSj_UupQG7G9MbyhErNishTXIu7bkva7qZd_sGv6d8_D0CvcYt88m1K8PfzPoWuvvVsLug02_LmPN0Svk6C2lQpO6tdXttV7C_RwL2lbA8P4MQxi1Lg8NbJU8_Y0zbI_2XWTBhs2-O1e0hQMrblTJv3jShcNsGBMDKU8FcsRg0dteRFs2ZDxrPaZKSsr2UxCapDX9VFeemWYcA-LQEVJqogO1bmDlyhYBRoNE4Vksvhnfl_7fUW8LWec6CO8exSq-RRk33dRxwkaJv87M3bi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9hdgMRtu82YxZah19fBhLq_Gx_36I6jrG-nlawMfGkxiY4QvOmcnQuDE-UjEPquLgmyOFJ6GTWJRLhaChtWunqymSDgsR6QbGakINFHGFN6tmUtOGKhZo4Q8G5Sv-zw5c0Hx7wzF-twNgwpYuGnvYVAxBmqik3mU-EFqFyw01xgx7u1f2JWkYXzO6GJ9C7fmIbybC1im2lwKpyphayqxWCEx1EgF6I-us5ZwUKJ5p1h07Ag71HUR1ygv8UVH7unYtR5gYtB6CBxoRxbbkvG_I1Awxl_7TLUImysJILE8o2DIDQXGTqnMrv9Jb9e3WgRZSHD0W_rMs8-spoArUkmcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7TRG8BOJIpbsioDdSWlDKqSfssQYbdou0izTd0USKIRt_nP1Q1Y_fxhERQ3t27njDuFr0IfApsE3dXCnyviXKieMrOY7N47WPKtQjTFymEucClsue82bIeROGUF53cSj9On1KsNCZOOqNQ4QOCNdqUk1eZnJwDQbAKAPIaBXxJlpXTF1qSCd6dxLkBsBeN968KF4eSdt6QEZxmMNDOlv5vLWc1pYoce_zm89dbkEl5d5A69OLgy0EG-Kr-AYdFaVWlU1DeJFbeD-hA2HK8vBDdxg8eHz4ejP5h41Iet79zT4NJkaO0l5Ad7HlGEVTeW00Ua1HQ2hjhUitt-zY4vgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازگشت شکارچیان آسمان به تالاب
🔹
۱۳ پرندۀ شکاری شامل ۲ عقاب، یک سارگپه و ۱۰ دلیجه پس از درمان توسط کارشناسان محیط‌زیست، در محدودۀ تالاب بهشت معصومه قم در دامان طبیعت رهاسازی شدند.
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461159" target="_blank">📅 22:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461158">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4ad2398b8.mp4?token=b_URKZJVLRmOyHoJ9HzYdk-i_DQQo76t7n3ONIozjg_DZg3eaCOTtf4UdqUO4wu7ad1QmbgdtP2TGQ55SmBBB3Q_PfiNhaI99wDt4Usz16O-IjubXmQfYwH7QJpdziPA_npBqViwLWAph06UDeKK2R0xZ09heSDTWjgI_YCviPcVxOLRD4VowGhuf7J3hX82QJMdvYBIN9sXRb4XyW-mvAIHR4JvqttMXljCMKTn3m2_6rI32x8ufgD5ulTcczEK16mdLfgMqOiSohovyQ2VQNHmmobd5Dpsam4qwhSvqbWHsdtZL311vl8ADOBf9NSw1aLFUrJ0cytZtUR6tocfhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4ad2398b8.mp4?token=b_URKZJVLRmOyHoJ9HzYdk-i_DQQo76t7n3ONIozjg_DZg3eaCOTtf4UdqUO4wu7ad1QmbgdtP2TGQ55SmBBB3Q_PfiNhaI99wDt4Usz16O-IjubXmQfYwH7QJpdziPA_npBqViwLWAph06UDeKK2R0xZ09heSDTWjgI_YCviPcVxOLRD4VowGhuf7J3hX82QJMdvYBIN9sXRb4XyW-mvAIHR4JvqttMXljCMKTn3m2_6rI32x8ufgD5ulTcczEK16mdLfgMqOiSohovyQ2VQNHmmobd5Dpsam4qwhSvqbWHsdtZL311vl8ADOBf9NSw1aLFUrJ0cytZtUR6tocfhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز پژوهش‌ها: طبق نظرسنجی‌ها حداکثر قیمتی که مردم برای بنزین با آن موافق بودند ۱۰ هزار و ۱۰۰ تومان بود
🔹
۷۰ درصد مردم با نرخ سوم ۸۷ هزار تومانی برای بنزین در کرمان مخالف بودند. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461158" target="_blank">📅 22:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461157">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ed4989b4.mp4?token=kqhHpCxr-SYwsbhSH3Iy2dVdn50m9BUqOI6C9dnJVn2tkwj5z01wWM3dbnxmObG6JLKrgls_doxyjbtI9_R3w_HOKBDTZBe00umL9uTsWQRwGcya3U8dPpewdzv6GvWXHZCaALwtrV88bMKx2SDpHRikBkG09gqItPOjwHRnb4GAKsfgX3pCt6FQ6CjG5oo-euiEUHEmfhCf4htk0zHqsxZ1QFAbg1841E1GxiLRmN1vcVdii-Uyp3mD67I0P3veAmIBpRZxDCSpN1l7X2ODrwiABXVDuCK3QwZ447asW1fU-CSn_GlIe4j2qarawjj_G3OYLjKfAbeqBIckZsxJAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ed4989b4.mp4?token=kqhHpCxr-SYwsbhSH3Iy2dVdn50m9BUqOI6C9dnJVn2tkwj5z01wWM3dbnxmObG6JLKrgls_doxyjbtI9_R3w_HOKBDTZBe00umL9uTsWQRwGcya3U8dPpewdzv6GvWXHZCaALwtrV88bMKx2SDpHRikBkG09gqItPOjwHRnb4GAKsfgX3pCt6FQ6CjG5oo-euiEUHEmfhCf4htk0zHqsxZ1QFAbg1841E1GxiLRmN1vcVdii-Uyp3mD67I0P3veAmIBpRZxDCSpN1l7X2ODrwiABXVDuCK3QwZ447asW1fU-CSn_GlIe4j2qarawjj_G3OYLjKfAbeqBIckZsxJAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: قیمت‌ بالای بنزین در آمریکا، هزینه‌ای است که برای جلوگیری از دستیابی ایران به سلاح هسته‌ای پرداخته می‌شود
🔹
قیمت بنزین پس از انتخابات میان‌دوره‌ای به زیر ۲ دلار برای هر گالن خواهد رسید. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461157" target="_blank">📅 22:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461156">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad6b1db62.mp4?token=gRdvdwAJCCgj5_zDq8-lr5Mt0fDkpQBZp3Xj4tSPDLCj5gtYwWZHqiuNUgSNzo64pHScEM0trAgT4NRN0B-fNo8hCJAznLZSD_hfhXHzIaoqtS9lXJPFe2PX9FMEPV7o4Wob3P4daKIqYnRINB4vo6c5RfXqo34TyjZ-KJ_mSiGu2MTOmYW3ZVRT_qatZf8V5zKR-e8T-T0c3NlGOucTEkuueTJbWargBNIfwZxoOQ3-AJFCazC0udK403Joc3pkTEBz-Cn6xWd0CbtbBpnB7-z2aCl3dhbr2sxBK6beiCMEZFemjK1vYANKtNtmFMKHMWxw7fdCdi4s-QJX8yxfXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad6b1db62.mp4?token=gRdvdwAJCCgj5_zDq8-lr5Mt0fDkpQBZp3Xj4tSPDLCj5gtYwWZHqiuNUgSNzo64pHScEM0trAgT4NRN0B-fNo8hCJAznLZSD_hfhXHzIaoqtS9lXJPFe2PX9FMEPV7o4Wob3P4daKIqYnRINB4vo6c5RfXqo34TyjZ-KJ_mSiGu2MTOmYW3ZVRT_qatZf8V5zKR-e8T-T0c3NlGOucTEkuueTJbWargBNIfwZxoOQ3-AJFCazC0udK403Joc3pkTEBz-Cn6xWd0CbtbBpnB7-z2aCl3dhbr2sxBK6beiCMEZFemjK1vYANKtNtmFMKHMWxw7fdCdi4s-QJX8yxfXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: [ایرانی‌ها] تمام تلاششان را می‌کنند تا روی نتیجه انتخابات ما اثر بگذارند، به این امید که یک گروه ضعیف روی کار بیاید تا کاری به کار آن‌ها نداشته باشد و بگذارد به سلاح هسته‌ای برسند.  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461156" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461155">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cd5330b8.mp4?token=jBrIYrSFxtXTuEGUwUU0xY_Q418jJcF1PVALpTjTjPJsuo0l_YHJ5I-tm-dIJBPYZlCR4Vlt8Y5Pp-GlPto0N4vufGmJA0dgKEUnsswXKyifUMuwIClQA6KFa2u7CDSM1f6CFwqN7lV-7BdN-CGwEJMWjRhcrw2dTSabQZMRdDSnL1dYuRCyOgAozvmgeZYIfNKXOcgFLhoL7XMZa4Lcf9ULzcJk-ntnAa2ifB2LyCnwQHJRW55zo8afRq5k2sHhXskukhJq0I-X-FoZqWXouteGmmcN5L0MVlf2VLd5RvFGh__qyuTKvFvlgwQIpa_suqGyDObTnBxiRqnY_ata5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cd5330b8.mp4?token=jBrIYrSFxtXTuEGUwUU0xY_Q418jJcF1PVALpTjTjPJsuo0l_YHJ5I-tm-dIJBPYZlCR4Vlt8Y5Pp-GlPto0N4vufGmJA0dgKEUnsswXKyifUMuwIClQA6KFa2u7CDSM1f6CFwqN7lV-7BdN-CGwEJMWjRhcrw2dTSabQZMRdDSnL1dYuRCyOgAozvmgeZYIfNKXOcgFLhoL7XMZa4Lcf9ULzcJk-ntnAa2ifB2LyCnwQHJRW55zo8afRq5k2sHhXskukhJq0I-X-FoZqWXouteGmmcN5L0MVlf2VLd5RvFGh__qyuTKvFvlgwQIpa_suqGyDObTnBxiRqnY_ata5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز پژوهش‌ها: باید کشورهای منطقه را به‌گونه‌ای به خود وابسته کنیم که فاصله‌گرفتن از ایران هزینه داشته باشد
🔹
دستگاه دیپلماسی باید بیشتر از مذاکره با آمریکا، بر مذاکره با کشورهای منطقه دربارۀ نظم نوین منطقه تمرکز کند. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461155" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461154">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257aa999a8.mp4?token=ELBTAB0iyi_YjkPsJioI1Wp2E5USFvGZ_HuWZwra8tsMlWxKp91umIAh29RIV1s8P6y_Z2K3_GlgDX3utFPXSXPIcWXLkDSXeUwv1B89y_4pSu9YFA8JZNs2GeZXUw-e1G1zLxkT7-xw0CvxyA_Yv4MuDSHIg1bU_famDGXKJn6M6m2HK8wvDiPRz8KPQ9oy_IcL1YK0WdBWzT55krrqde4L0G3IS4WeYMNNu09R1X_j4rkykRJpQQvHdjp5BtkX06nqsAj38VZ60yEJwvmwkvfQ4Zu_c0Z9kezvOlrRacFHAqx1yMRnQuPeAkLSPud8pGnbWwDfPcXjD2K6n7DkTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257aa999a8.mp4?token=ELBTAB0iyi_YjkPsJioI1Wp2E5USFvGZ_HuWZwra8tsMlWxKp91umIAh29RIV1s8P6y_Z2K3_GlgDX3utFPXSXPIcWXLkDSXeUwv1B89y_4pSu9YFA8JZNs2GeZXUw-e1G1zLxkT7-xw0CvxyA_Yv4MuDSHIg1bU_famDGXKJn6M6m2HK8wvDiPRz8KPQ9oy_IcL1YK0WdBWzT55krrqde4L0G3IS4WeYMNNu09R1X_j4rkykRJpQQvHdjp5BtkX06nqsAj38VZ60yEJwvmwkvfQ4Zu_c0Z9kezvOlrRacFHAqx1yMRnQuPeAkLSPud8pGnbWwDfPcXjD2K6n7DkTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم گناباد برای وطن خستگی نمی شناسند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461154" target="_blank">📅 22:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461153">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd079a17d.mp4?token=YxOOK18blfygvORSO97wFF3PthyGjrlYFqHP_QJ21uz52IYNoJxMO2rjAKZ9Afng2noMPdOCTdEx9mrTbegITYGX_oRGhO0_P3LvmcPK5YiSBqKh7fBRQz76eq75jnt4aDmF-oplikGvTKQTnkyweydYx8itMxJ4IrZ45w5Vf_7JI5zn3-QFfgYgm9eMq8WOVhiZGBYz9hRVIVMeUJVfhJWuK3TrHLYsqD3gBbqyWO0qdTjIO_wynpAWsUtAHCK5N1WuTq-xXw81jbfsxuRAOrdALDzWPYP-ocVlsyEbjM51qo7HcAF1mxAGoDyBcKKQmrW1OdFGSxL5lGrvb1s0S1ByLOKgLY14K6GbBRbPDsyKoAaCZAFGYFLbpnJPVDjXgovUSCu0sOyp8-AGyuv4BGXcB3V0BRC7-Pp6mSvyxnuJ5Trt9FwQmaJ7ZekBj2F-E2JcSYvj7rFm-3z9Ds0NZrwVxwRFS4QZo_s2WlLNTWETJdeWav39Vf0mE2cTDBbFwAdo84kqSAdX97jTOK2Vpl_ictz2ypD056m7tK68PYKfPGT87ARuZv3tnPb4pXkoq-b6hMUsX6Rnjnm7xj2dexNKbtazSYMfBVL8kTLdkrp1k0lhguNSithYOp3f6Pds7I1WdEVpAy65mXRXgzjV57M-uxV8ag0S4pYyL9-HSSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd079a17d.mp4?token=YxOOK18blfygvORSO97wFF3PthyGjrlYFqHP_QJ21uz52IYNoJxMO2rjAKZ9Afng2noMPdOCTdEx9mrTbegITYGX_oRGhO0_P3LvmcPK5YiSBqKh7fBRQz76eq75jnt4aDmF-oplikGvTKQTnkyweydYx8itMxJ4IrZ45w5Vf_7JI5zn3-QFfgYgm9eMq8WOVhiZGBYz9hRVIVMeUJVfhJWuK3TrHLYsqD3gBbqyWO0qdTjIO_wynpAWsUtAHCK5N1WuTq-xXw81jbfsxuRAOrdALDzWPYP-ocVlsyEbjM51qo7HcAF1mxAGoDyBcKKQmrW1OdFGSxL5lGrvb1s0S1ByLOKgLY14K6GbBRbPDsyKoAaCZAFGYFLbpnJPVDjXgovUSCu0sOyp8-AGyuv4BGXcB3V0BRC7-Pp6mSvyxnuJ5Trt9FwQmaJ7ZekBj2F-E2JcSYvj7rFm-3z9Ds0NZrwVxwRFS4QZo_s2WlLNTWETJdeWav39Vf0mE2cTDBbFwAdo84kqSAdX97jTOK2Vpl_ictz2ypD056m7tK68PYKfPGT87ARuZv3tnPb4pXkoq-b6hMUsX6Rnjnm7xj2dexNKbtazSYMfBVL8kTLdkrp1k0lhguNSithYOp3f6Pds7I1WdEVpAy65mXRXgzjV57M-uxV8ag0S4pYyL9-HSSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار امشب مردم پیشوا: فریاد ملت حسین چنین است، سازش با آمریکا ضد دین است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461153" target="_blank">📅 22:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461152">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96074dc5fb.mp4?token=e8iZ0zlDzYadvgohsBpAAR-2XnPdv9CmZmQTotrHweg9A1wKAh5nEVOvxMoflFztSAin1CI1k3P95NbtXa0IwhoUQT-fGa_0wtmmVwCI42y40GB3cotM5jyo00Xs8jTn6TmRx0Aki7wLW6CvcaVmN4mSQi0j7GdFP1B0I6AoOuPacNiZnKrMlLAya8TIHl6TgFxgggbswWTww55bBiufx7zqtMgzS4avKlwwZlBwIXQGOz1O328ad18oWYUV0KyMeN4Tk7bKuCuOKe2kcQ1_GBbyV-XfTq4kQa_nAYCAxc2NTLYwXa4aTh-YkilaxQDgVyZxvSzmqy6gOHIRt9YSkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96074dc5fb.mp4?token=e8iZ0zlDzYadvgohsBpAAR-2XnPdv9CmZmQTotrHweg9A1wKAh5nEVOvxMoflFztSAin1CI1k3P95NbtXa0IwhoUQT-fGa_0wtmmVwCI42y40GB3cotM5jyo00Xs8jTn6TmRx0Aki7wLW6CvcaVmN4mSQi0j7GdFP1B0I6AoOuPacNiZnKrMlLAya8TIHl6TgFxgggbswWTww55bBiufx7zqtMgzS4avKlwwZlBwIXQGOz1O328ad18oWYUV0KyMeN4Tk7bKuCuOKe2kcQ1_GBbyV-XfTq4kQa_nAYCAxc2NTLYwXa4aTh-YkilaxQDgVyZxvSzmqy6gOHIRt9YSkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما به کشتی‌های ایران حمله کردیم و حملاتمان بیشتر هم خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461152" target="_blank">📅 22:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461151">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbjct_v9hIGn0_uhGAfmyWfokGo-o11uhhzMnIr-3dY9sFW-Y_gFCvruaRPw_PWj-k8b7czk5nH94XNCOrOlQcRc9i_UR-xAz56CcOW5JHAK_sM2cT8yx_D8pQn_SX-hKqwwrMFoRINVubLfaPjHPhhicpXC9iCj81W0rWta_uLUZEb5KaI3LMhJO4eiAoHX9Ju_9DdElO6tY3WKCr19yNkrhMHFCF9IxPZ5meikEHzie2-GW70-vuGh33YG46Vg_kYo7bwv6e_jelBkYDfjVL1kA5_DXRoAtb7ND8cdz91Aowbw2KIzYdQorugBwjBzfj2o_TfTgXOsLUez_HsTSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمسیون امنیت ملی خطاب به آمریکایی‌ها: تا دیر نشده به کشور خود برگردید تا بلکه بتوانید حداقل از مرز های خودتان دفاع کنید.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461151" target="_blank">📅 22:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461150">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/905e322c38.mp4?token=fHCX1_OGXkt1a3uQzb3CRz61DI9hae9w3mXQedBsfSWPV_IDLS9kD-fAvCaj-N0vRU6WZh3-U-ZcQfEx1Gfh2mvfZo6787tErv2keEx1gG1ZqvurFOtUYyZYpeMG-UvsmXNJ4dSM__JuhB842b3l9k6V7S7912Ic0MxBM8wDSnDcdOzS2c7puGctgGsI7a__zQM1Byy6dHtdyrqINB5O8Xz4AZe3HcZLi9DpPQUVc1e47bUytZlUdGedvtrBuw4OzgtNQ5FLt-AmmFLouLLxOJeDLCV8OxI6dfVzWtjUuTVgmLj7er3BpcfStXP72SJ0702laSAG_mWn4xcNQfZ-mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/905e322c38.mp4?token=fHCX1_OGXkt1a3uQzb3CRz61DI9hae9w3mXQedBsfSWPV_IDLS9kD-fAvCaj-N0vRU6WZh3-U-ZcQfEx1Gfh2mvfZo6787tErv2keEx1gG1ZqvurFOtUYyZYpeMG-UvsmXNJ4dSM__JuhB842b3l9k6V7S7912Ic0MxBM8wDSnDcdOzS2c7puGctgGsI7a__zQM1Byy6dHtdyrqINB5O8Xz4AZe3HcZLi9DpPQUVc1e47bUytZlUdGedvtrBuw4OzgtNQ5FLt-AmmFLouLLxOJeDLCV8OxI6dfVzWtjUuTVgmLj7er3BpcfStXP72SJ0702laSAG_mWn4xcNQfZ-mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز پژوهش‌های مجلس: نبرد هرمز تعیین می‌کند که نظم ایرانی حاکم همیشگی منطقه شود یا نظم آمریکایی
🔹
غرب آسیا آن‌قدر ظرفیت ندارد که بتواند ۲ نظم را تحمل کند و در نهایت یکی باقی می‌ماند.
🔹
با ایستادگی ملت ایران نشانه‌های پیروزی نظم ایرانی به مرور دارد نمایان…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461150" target="_blank">📅 22:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461149">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
من از اهالی روستای پشگ، بخش چاه‌دادخدا، شهرستان قلعه‌گنج هستم. ما از نبود آب آشامیدنی، جاده مناسب، خدمات بهداشتی و درمانی، دوری از مراکز درمانی و نبود فرصت شغلی رنج می‌بریم. لطفاً مسئولان برای جابه‌جایی روستا و نزدیکی به جاده و مراکز درمانی و همچنین واگذاری زمین مسکونی به اهالی اقدام کنند.
🔹
خرمای سال گذشته ما به‌دلیل شرایط جنگی فروش نرفت و
خرمای امسال
هم دوباره به‌دلیل همین شرایط،
توسط واسطه‌ها با قیمت پایین خریداری می‌شود
. واسطه‌ها می‌گویند راه صادرات بسته است.
🔹
لطفاً صدای چایکاران باشید. از خردادماه چای سبز تحویل داده‌ایم اما دولت هنوز
مطالبات چایکاران
را پرداخت نکرده است. اگر از کشاورزان حمایت نمی‌کنید حداقل پول دسترنج و محصولشان را به‌موقع پرداخت کنید.
🔹
با نزدیک شدن به آغاز سال تحصیلی جدید در مورد تعیین تکلیف
استخدامی نیروهای شرکتی نهضت سوادآموزی
و جبران کمبود معلمان مقاطع تحصیلی از میان این همکاران پیگیری فرمایید.
🔹
لطفاً وضعیت
تحویل خودروهای برقی توسط پرشیا خودرو
را پیگیری کنید. با وجود گذشت یک سال و نیم هنوز خودروها تحویل داده نشده‌اند و کسی پاسخ‌گو نیست.
🔹
لطفا دربارۀ پایین بودن حقوق و مزایای استادان حق‌التدریس دانشگاه‌ها هم پیگیری لازم و اطلاع‌رسانی انجام شود. استادهای حق‌التدریس نه بیمۀ مناسبی دارند و نه حقوق کافی دریافت می‌کنند.
🔹
تو رو خدا صدای ما را به گوش مسئولان مرتبط با شرکت
سایپا
برسانید. این شرکت
به وعده‌های خود عمل نمی‌کند
و خودروهای ما را با وجود گذشت یک سال هنوز تحویل نداده است. هنگام تماس هم پاسخ درست و مناسبی دریافت نمی‌کنیم. الان ۹ ماه از موعد تحویل وانت پراید ما گذشته و با اینکه ۳ ماه است فاکتور شده، هر بار پیگیری می‌کنیم فقط وعده‌های جدید می‌دهند.
🔹
من از حاجی‌آباد
زرین‌دشت فارس
پیام می‌دهم. خواهشمندم پیگیری کنید چرا
زمین‌های طرح جوانی جمعیت
به متقاضیان تحویل داده نمی‌شود. نزدیک به ۵ سال است که ثبت‌نام کرده‌ایم اما هنوز زمین‌ها را تحویل نداده‌اند.
🔹
لطفاً خبری از آموزش‌وپرورش درباره
شهریۀ مدارس دولتی و هیئت‌امنایی
بگیرید. از یک طرف اعلام می‌شود دریافت شهریه در مدارس دولتی و هیئت‌امنایی ممنوع است اما از طرف دیگر برخی مدارس از والدین درخواست شهریه می‌کنند. لطفاً پیگیری کنید که دریافت چه مبالغی قانونی است و مدارس بر چه اساسی شهریه دریافت می‌کنند.
🔹
مسئولین به
معضلات اجتماعی و فرهنگی
علی‌الخصوص بی‌حجابی و بی‌حیایی در شهرها و برنامه‌ها بپردازند. جامعه اسلامی آندلس با گسترش  بی‌بندوباری از بین رفت.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461149" target="_blank">📅 22:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461148">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db4f0dd22.mp4?token=aEW4dWb0mgwDDHMYfFiMoD8aYrk7tOS3SbBBZEKfLs8zoT7qqYLunQZx7rs9VxVTz9dU2S4No2yXVKWk_72GMAhMY_rGWVI8EsBZetLU8ucmkGi9wdm1Okkwnm5bNRt3TcCOEU6RCVsNhNFEbuVtDPCsFWFw0EpTdHrHnHPXDSskWqr_eJ5Q2tF-hmNGMp797cw3E3yy2lkCkvaQmLgQ-nayBvPlGyaI0t8F_7dtJonvSfpDbhgxrkyOY1k1azOs5cxCLZUgeokcWYYDf-lmlyGJf9_2mr28PMW7zSygwW_i0X8tTCGClbvF1koDm6VW1Cid8e_Sgv3hwuLyM5VDwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db4f0dd22.mp4?token=aEW4dWb0mgwDDHMYfFiMoD8aYrk7tOS3SbBBZEKfLs8zoT7qqYLunQZx7rs9VxVTz9dU2S4No2yXVKWk_72GMAhMY_rGWVI8EsBZetLU8ucmkGi9wdm1Okkwnm5bNRt3TcCOEU6RCVsNhNFEbuVtDPCsFWFw0EpTdHrHnHPXDSskWqr_eJ5Q2tF-hmNGMp797cw3E3yy2lkCkvaQmLgQ-nayBvPlGyaI0t8F_7dtJonvSfpDbhgxrkyOY1k1azOs5cxCLZUgeokcWYYDf-lmlyGJf9_2mr28PMW7zSygwW_i0X8tTCGClbvF1koDm6VW1Cid8e_Sgv3hwuLyM5VDwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما به کشتی‌های ایران حمله کردیم و حملاتمان بیشتر هم خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461148" target="_blank">📅 22:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461147">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/954e22293b.mp4?token=MOiLFrtTmFOJtNGSsiAm_ddeYiYdLF6kCDR2Mhy7rDvcN_yHEInI0xnCUj-1lYnZDgVXp_SFA561jEpcuRVG8XP--5387-Ztlzak2ESnJM3ecvqa4HuiKXDzhJFE9Ri5lT9hnVcQ-CibvoNzB-YvUJhvBrlF59rjla3MrdYdOWqBVuAERNv0Ge3vJSdbAy99iGgzAN8aAHbBeM7CXSY5tx_KDhXKx0wY9bkCo5_Uq93CGNyDsMnAfbnXPO8ZPEjFsUDDFF-64zOo6LTH2lrbR1hijGiuXjIYVLF06b_0SWLLil9XeBzCqDSNFA7YtoR0jxjUUyLNEIVFUsRJpPVc1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/954e22293b.mp4?token=MOiLFrtTmFOJtNGSsiAm_ddeYiYdLF6kCDR2Mhy7rDvcN_yHEInI0xnCUj-1lYnZDgVXp_SFA561jEpcuRVG8XP--5387-Ztlzak2ESnJM3ecvqa4HuiKXDzhJFE9Ri5lT9hnVcQ-CibvoNzB-YvUJhvBrlF59rjla3MrdYdOWqBVuAERNv0Ge3vJSdbAy99iGgzAN8aAHbBeM7CXSY5tx_KDhXKx0wY9bkCo5_Uq93CGNyDsMnAfbnXPO8ZPEjFsUDDFF-64zOo6LTH2lrbR1hijGiuXjIYVLF06b_0SWLLil9XeBzCqDSNFA7YtoR0jxjUUyLNEIVFUsRJpPVc1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس مرکز پژوهش‌های مجلس: نبرد هرمز تعیین می‌کند که نظم ایرانی حاکم همیشگی منطقه شود یا نظم آمریکایی
🔹
غرب آسیا آن‌قدر ظرفیت ندارد که بتواند ۲ نظم را تحمل کند و در نهایت یکی باقی می‌ماند.
🔹
با ایستادگی ملت ایران نشانه‌های پیروزی نظم ایرانی به مرور دارد نمایان می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/461147" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461146">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزیر آموزش‌وپرورش: مدارس دولتی حق دریافت پول از مردم را ندارند
🔹
هیچ مدرسۀ دولتی حق ندارد از مردم پول دریافت کند و برای ساماندهی این موضوع، اساسنامۀ جدیدی برای ادارۀ مدارس تدوین و در شورای‌عالی آموزش‌وپرورش تصویب شده است. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/461146" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461145">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3jp6SQA4LlCUcfki70TE-qlV-fViMljdjfTfNj6BeK4HqYAuYUL-zhyOa4VvpRZAs7_duy4YlVl8C3Rx4GqycaLPnKOnk_w1EdlsenDrSvO0yATkfb5h2EPe-6dL9o-pcpSrBjEHqE9hI2okdvfEApHZZ4u0u_m7XhRtgzrKcO-CVQyNJEbIaj2g9uC1A-3jxbfbyK4SmTPSUCj1VNtTb_FqJOXnFovK7peBw99P3Ln8V2sMt7Ijz2hjKkWMiKjAAoJTHN7ImOpxE0rBZYobsKtscT_Z1cIWeLPY1eLmUs221hhFln_ltKiH0ZHYeXV2uqt1_B9m5dqbm93VvR4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: مدارس دولتی حق دریافت پول از مردم را ندارند
🔹
هیچ مدرسۀ دولتی حق ندارد از مردم پول دریافت کند و برای ساماندهی این موضوع، اساسنامۀ جدیدی برای ادارۀ مدارس تدوین و در شورای‌عالی آموزش‌وپرورش تصویب شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461145" target="_blank">📅 22:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461144">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38fef9656c.mp4?token=WgKoxARVBWMvyZM4h-9NZyhfmdoj899MwyShQBDRIMPqA6NgmhGPtCZ1wkFucgkW1jyFbc5zD_-BhMkUx15auorQflq8PR-nw1XanPmYPCacwxYP669vYaJ4Vg5RcbIc1Y-OOpo8ExOA2Mm3TnUoqfokca0gqbMbYBYpfTOmq1wdcdD_1AsuQ5tLq_V6y9gW4Ym9_iGz45Px67zfBBlLIgE5SewQYWsZSv4Po3A04SZs12fUYurVrbIODrDDYusSD4MS_DQADG-G11SjuhRB0cWBMhhfjaJJn1ButVIb05xQRaxFjBTzdPfiydu9R_QlZPz7wt3zXCsHzeUCT3vjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38fef9656c.mp4?token=WgKoxARVBWMvyZM4h-9NZyhfmdoj899MwyShQBDRIMPqA6NgmhGPtCZ1wkFucgkW1jyFbc5zD_-BhMkUx15auorQflq8PR-nw1XanPmYPCacwxYP669vYaJ4Vg5RcbIc1Y-OOpo8ExOA2Mm3TnUoqfokca0gqbMbYBYpfTOmq1wdcdD_1AsuQ5tLq_V6y9gW4Ym9_iGz45Px67zfBBlLIgE5SewQYWsZSv4Po3A04SZs12fUYurVrbIODrDDYusSD4MS_DQADG-G11SjuhRB0cWBMhhfjaJJn1ButVIb05xQRaxFjBTzdPfiydu9R_QlZPz7wt3zXCsHzeUCT3vjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جهرم در شب ۱۹۳ همچنان پای کار مقاومت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461144" target="_blank">📅 22:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461143">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رئیس دانشگاه سمنان: شایعۀ تعرض دانشجویان عراقی، دروغ بزرگ است
🔹
رئیس دانشگاه سمنان: بامداد دوشنبه میان چند دانشجوی عراقی و ۳ رهگذر، شامل یک زن و دو مرد درگیری رخ داده و به زد و خورد منجر شده است.
🔹
براساس گزارشاتی که در اختیار پلیس است، آن ۳ نفر حالت عادی…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/461143" target="_blank">📅 21:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461141">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce568ac68b.mp4?token=ohUu9Ri0G8G9_gb6EL0w6HvYBCJz6BTBdxz-XGc3GylD_Hk2eSKy-QXEHmmvns007NMByosbCYU9a3YZajHGcDWs-MDxIWUmR3b34Oe2-L0dvA7x2N-FTAg0ZKFgYbFEjZhDT5gFHjR-qWw7Q1cQWX6Y4puLKE3sjiDvZfaQcJKr6WZSLloXD57syCkZ5ewyF7xDyUbaizX7atwwumwkXbWkCOLu_zjgmK6P6__PruW3lKMJJasAKHhsFHwuWgG74xkBbxlX7aNMVM-rMWbTcbKQz9fHkCcmF2LRdoRGpk_-cwYploT4I7dnQFGgpdd8LpQYsUCaMRqu71X_NSk44Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce568ac68b.mp4?token=ohUu9Ri0G8G9_gb6EL0w6HvYBCJz6BTBdxz-XGc3GylD_Hk2eSKy-QXEHmmvns007NMByosbCYU9a3YZajHGcDWs-MDxIWUmR3b34Oe2-L0dvA7x2N-FTAg0ZKFgYbFEjZhDT5gFHjR-qWw7Q1cQWX6Y4puLKE3sjiDvZfaQcJKr6WZSLloXD57syCkZ5ewyF7xDyUbaizX7atwwumwkXbWkCOLu_zjgmK6P6__PruW3lKMJJasAKHhsFHwuWgG74xkBbxlX7aNMVM-rMWbTcbKQz9fHkCcmF2LRdoRGpk_-cwYploT4I7dnQFGgpdd8LpQYsUCaMRqu71X_NSk44Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل‌به‌خودی جدید ترامپ در تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461141" target="_blank">📅 21:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461140">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌ سخنگوی وزارت خارجه: کشورهای متخاصم با الگوی رای گله‌ای علیه ایران رای دادند
🔹
تاسف‌بار است که کشوری مثل ژاپن که قربانی سلاح هسته‌ای بوده به قطعنامه علیه ایران رای مثبت داده. @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461140" target="_blank">📅 21:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461139">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌سخنگوی وزارت خارجه: اقدام شورای حکام علیه ایران یک تناقض آشکار است
🔹
عدم دسترسی آژانس به تاسیسات هسته‌ای ایران ناشی از حملات آمریکا و اسرائیل بوده و ایران مرتکب عدم پایبندی نشده. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461139" target="_blank">📅 21:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461138">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Illxirs7dONBcCvyMXW-G19L4Om43dh983qkMRYe9A_FviE1kGkty_Iyd6z0I4_2rpXdg85KFPfgLTPwnNsbxSJYImTjC2-VaRU18iajsfTy6wpsC2kZ4uagLy4ivbC0KuWoyzS9QS8SSO-DU4LSGMIm5IGTvpp1z5lcEIZrQpPJWNGpTxyRLcmol9M7L2P7TXn7_89xVg7Qm7YqTA57JEA2cJvHlnVzjxOd9LpF06t97Mbu4btlpCHLDCsSoXb-jinHNzMffTvC7MDVcs3lz2qQOs3TaKc-V9JGZnHwQc-vWA1qCJRNSN8sz-sqorrTkRnfwLAgsNb7iN6N4Wbc5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نمایندۀ ایران در آژانس: این قطعنامه مبنای قانونی ندارد و نتیجه‌ای درپی نخواهد داشت  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/461138" target="_blank">📅 21:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461137">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceeb4b5605.mp4?token=FYOISLkwfuzvPd7OH6cLIvdy3E7go6ECol0I35CONBHxAwlVHMCse-iRSR_eGsEkVd5_kVbBCqL1pkRMREOp_lT0UH0jApn6WADAJsKU-LrXqIAMEQDFtVcTYR9m3Ocvx9sLil2a8Z-UC57GGJ5CyD1cTi3vCi9Dw-HZ4fpzu3ZunMTBEvU7rNAPca-5_pP8rU9LoPJcetKjyvWHRRxxObMjCcRgEK4Ky-fM6vuJAGbwQ2mt6UlplazGlzjbMma7T8jPBpAI1NSRwox_2zYITGVLRqJMI21b_eRzEb9qoivXziLIBozFeZrzqS4yIZu05c6wz7UXPJnBG2hXx-4l_08a2DYCIai_vpfODkx0daOtbTGOZ7c30ewHUa8DWupJoZggIyTXaVL-ZT1-3JbfcNFOGWOEPXlHQAtllE8bbcmnf-G7OC9rxGbFAc3HPJwhS6MHMvgBuFBxjIVtze0WX4TVbMmiVKkiWvYXoFvjUffM7kXZ3D5MqmxBnxGa-BY7TIZDY859VrCaFIr4V0O3W_CCK-4lAwwXpzNqmRVqot0pLrA0Hq_Et6agCnCR8BH2D0YtppDLHVf1jXYSzcYX4aXXaW7RCrzvEvql7_UCQp0Vxgl3XT42UFgXEdng8hK2NjuOi2CkgkL-otojfOtkU712VoHZ3lYpyYjgVUResIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceeb4b5605.mp4?token=FYOISLkwfuzvPd7OH6cLIvdy3E7go6ECol0I35CONBHxAwlVHMCse-iRSR_eGsEkVd5_kVbBCqL1pkRMREOp_lT0UH0jApn6WADAJsKU-LrXqIAMEQDFtVcTYR9m3Ocvx9sLil2a8Z-UC57GGJ5CyD1cTi3vCi9Dw-HZ4fpzu3ZunMTBEvU7rNAPca-5_pP8rU9LoPJcetKjyvWHRRxxObMjCcRgEK4Ky-fM6vuJAGbwQ2mt6UlplazGlzjbMma7T8jPBpAI1NSRwox_2zYITGVLRqJMI21b_eRzEb9qoivXziLIBozFeZrzqS4yIZu05c6wz7UXPJnBG2hXx-4l_08a2DYCIai_vpfODkx0daOtbTGOZ7c30ewHUa8DWupJoZggIyTXaVL-ZT1-3JbfcNFOGWOEPXlHQAtllE8bbcmnf-G7OC9rxGbFAc3HPJwhS6MHMvgBuFBxjIVtze0WX4TVbMmiVKkiWvYXoFvjUffM7kXZ3D5MqmxBnxGa-BY7TIZDY859VrCaFIr4V0O3W_CCK-4lAwwXpzNqmRVqot0pLrA0Hq_Et6agCnCR8BH2D0YtppDLHVf1jXYSzcYX4aXXaW7RCrzvEvql7_UCQp0Vxgl3XT42UFgXEdng8hK2NjuOi2CkgkL-otojfOtkU712VoHZ3lYpyYjgVUResIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرسایشی‌شدن جنگ به نفع ایران است یا آمریکا؟
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461137" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461135">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حملات هوایی صهیونیست‌ها به چندین شهرک در جنوب لبنان
🔹
رسانه‌های لبنانی از حملات جنگنده‌های رژیم صهیونیستی به شهرک‌های صربین، حداثا، حاریص، النبطیه الفوقا‌ و الخیام خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/461135" target="_blank">📅 20:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461134">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec7416fcb.mp4?token=NSSy_csfL62TgqBtTpzhFEqTm3EoFVXHvxe4nkj-G8oXts0Obtu3yzF5aMO17sGb4-NP1QkY_o9izj8e8TlQuWfu_XtAdw1TRp76GMaVa5M_eDA_Qpp0FdXB4oo18Wtv2AYrfRIAbZjpw9WCdKifuRA1ls3BEiNHJHSnmhw52iGDx5XhY2MiMXkKBVKp-J23TSdp12pvFDNyveL7Va58rreqo0GcWgdVLNkoB9lpRrpLtp3He-enmqTMURAb1N0fQ3_BoRmEzgH9WjsDV1OXJPFOQTk96kyj8j_7gLHomhKqz3dn5MQUp5hnxfc0i77rt7Pk6unw4HURc4d7zFr7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec7416fcb.mp4?token=NSSy_csfL62TgqBtTpzhFEqTm3EoFVXHvxe4nkj-G8oXts0Obtu3yzF5aMO17sGb4-NP1QkY_o9izj8e8TlQuWfu_XtAdw1TRp76GMaVa5M_eDA_Qpp0FdXB4oo18Wtv2AYrfRIAbZjpw9WCdKifuRA1ls3BEiNHJHSnmhw52iGDx5XhY2MiMXkKBVKp-J23TSdp12pvFDNyveL7Va58rreqo0GcWgdVLNkoB9lpRrpLtp3He-enmqTMURAb1N0fQ3_BoRmEzgH9WjsDV1OXJPFOQTk96kyj8j_7gLHomhKqz3dn5MQUp5hnxfc0i77rt7Pk6unw4HURc4d7zFr7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
واکنش معاون وزیر خارجه به تصویب قطعنامۀ ضدایرانی: در شورای امنیت هم نمی‌توانید کاری از پیش ببرید
🔹
غریب‌آبادی: به تأسیسات هسته‌ای تحت پادمان ایران حمله می‌کنند، روند عادی راستی‌آزمایی را مختل می‌کنند و بعد همان اختلال را دستاویز صدور قطعنامه در شورای حکام…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/461134" target="_blank">📅 20:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461132">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnOO4FSgbZrCFPS7hwA1RHRoiA8lSU2IK2fdyYk60kUL-nehyLHR4QjUEVEQ7ghngsCbdTmtkzPoBgnjOO1v7a7v7o_o0f8sVpLexQde9JFib_A0Fy9Oiz_7-r4la1qoimgFcnzapjbsAgqaiJb2JnNJKYny3QT3VF0NZectWUWoOR84aP9z1xqKdbTMN7_KuftMSkfhmEOSQxpvB5hU8J0Upb7r05SWjraAMdb4tdD7_x9RdiUmT1HJuYMGLZ_kMjfaFJKQ0yzy-CmpPNckZM5RALWWJvsjppQAwk_Y9sw5t6krOY-9XF3udIQebAJwSaQ_U52Tjt6ub9LQ8RXT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: به گسترۀ ایران، از اعماق زمین تا اوج آسمان، به زودی خواهید دید
...
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/461132" target="_blank">📅 20:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461131">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d96386b7e8.mp4?token=omX-6IWb8CNaI6nFDm3dSKygMLDtwSJKPQw1z0g7Eu5zo3GPmoqxvciTo6XiNeAmRfXeEWHjw5jglgbmIiylP9dopj71sBNLMydPteqyoOlSWOjnfCPQoI344xtpEAIpJniLKIiYcUyaK7ifB8a4rh_SW_PVf6fG9586W0d9YcHAbfuk9kOaa3pri9shA5Z-G5n2kjrkHl9Cm4fvsSxyR3JmG4cid2iFnLy8tPT6-oAk_d0GdPXD5NeCNkm9V1-WegDdw6CdIusvnWX2GIrdsP7cnzcI1-9LCDaPVkA0GyEVGu1TUq3T4uGkx03-mMd23yMCyODDqEdJVTq0ggV0sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d96386b7e8.mp4?token=omX-6IWb8CNaI6nFDm3dSKygMLDtwSJKPQw1z0g7Eu5zo3GPmoqxvciTo6XiNeAmRfXeEWHjw5jglgbmIiylP9dopj71sBNLMydPteqyoOlSWOjnfCPQoI344xtpEAIpJniLKIiYcUyaK7ifB8a4rh_SW_PVf6fG9586W0d9YcHAbfuk9kOaa3pri9shA5Z-G5n2kjrkHl9Cm4fvsSxyR3JmG4cid2iFnLy8tPT6-oAk_d0GdPXD5NeCNkm9V1-WegDdw6CdIusvnWX2GIrdsP7cnzcI1-9LCDaPVkA0GyEVGu1TUq3T4uGkx03-mMd23yMCyODDqEdJVTq0ggV0sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی روحانی بر «تسلیم» لباس رونق می‌پوشاند
🔹
حسن روحانی، رئیس‌جمهور سابق، به‌تازگی در اظهاراتی گفته: تنگه هرمز نباید تنگه جنگ باشد؛ ما که نمی‌خواهیم همه‌اش بجنگیم؛ تنگه هرمز باید تنگه پررونق باشد؛ اگر رونق نداشته باشد آن را می‌خواهیم چه کنیم؟
🔹
این اظهارات…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/461131" target="_blank">📅 20:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461130">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW-VWbRUXUbn244fpCQnSsgYKA4KUFlPKn_ISQeXAURxGUNKv80xG-BDCM5-xrgEHxhFylq4uLmlYHET3GCpFAkXzGdOgaU8l6xLl1p0JfipJqvBci8g0kIV0SV0_Y6kcgzJEe_cEUjzW6MY8JmKC1Eo9oPutNi62JvGDBEs06kN4rqvYBhqgGfoS_Pn7ZRwod0gfXQIdEd4dp37gof3hWwPxKpeEhdZvNmGgJmZxY21MDXWFZKsRe5rhiS-maNy9suRY88Uh3RILQD2AtmoXQl8PeUXanoBZPTEf5LsVNPHyPnKOjmaOql2M8PYpbCiIeHg5OLV5PSwDGvNw8FTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آژانس پروندۀ هسته‌ای ایران را به شورای امنیت ارجاع داد
🔹
رویترز به‌نقل از دیپلمات‌ها خبر داد که شورای حکام آژانس بین‌المللی انرژی اتمی پرونده هسته‌ای ایران را به بهانه آن چیزی که نقض تعهدات توصیف کرده، به شورای امنیت سازمان ملل ارجاع داده است.
🔹
این قطعنامه…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461130" target="_blank">📅 20:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461129">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guQ-9BlOmah84VwwcToRVAhz-BcC8r7fKV5VEeiYl4nJznY5ILC0tcFjxJ52EjBakwxEnZvHH-xuqWkahNXNAgsR5duXmmi5EyS5t0uy9_fWgVmm4415XqkzOzsufGbba84vwqAcQnLLo-vpDya_cYuRnSPBFeLSfIPEd_V_qZuRPeP2I8-yWz8om-rX5kK8sptFJreoOEYlV_c7mNta0p9nhwp7etTno3ffhSQQZe9QCaVyUaAxdn6aPMQ5cZmAF_IuE1spFxeuJqcrIxepH3PXnUJUOJVAbGPACd6yFhKi2iEaPLh5IjV8gM8KgSbz5CvGi4Lg8qVZQ-evlki83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون پس از ۲۰۰ روز یاد شهید مدرسه میناب افتاد
🔹
«ماکان جان تو باید امروز پشت نیمکت مدرسه‌ات می‌نشستی، مشق می‌نوشتی، بازی می‌کردی، می‌خندیدی و برای فردایت رؤیا می‌ساختی». سردار آزمون، مهاجم شباب الاهلی امارات، چهارشنبه عصر، ۱۹۴ روز پس از ۹ اسفند و آغاز جنگ، در استوری اینستاگرامی از ماکان نصیری، دانش‌آموز شهید مدرسه میناب نوشت.
🔹
آزمون در بحبوحه جنگ آمریکا و اسرائیل علیه ایران در استوری‌های اینستاگرامی از شیوخ دبی تمجید کرد. امارات در این جنگ ضد منافع ایران عملیاتی انجام داد و از مقرهای اصلی اطلاعاتی اسرائیل بود.
🔹
معاون رئیس‌جمهور در امور توسعه روستایی و مناطق محروم دوشنبه درباره بازگشت آزمون به تیم ملی گفته بود: «آقای پزشکیان خودش شخصاً موضوع را پیگیری کرده و می‌توانم بگویم که ۹۰ درصد مسائل او حل شده.»
🔹
حالا آزمون در استوری‌اش با بیش از ۶ ماه تأخیر بدون اشاره به عاملین این حمله نوشته: «کاش هیچ کودکی در هیچ جای دنیا، معنای جنگ را با جانش یاد نگیرد».
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461129" target="_blank">📅 20:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461128">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf0NOzJrU5NasH3FgHtx_lPpXgL_r0Vartx2NKZ6qrUqycGvPZrO4ldzPfDMIbAuGCTVtHbH9aGdTrhSOtrQ2We8OvFBJWamJDfYLA1MrudsATDbzj1OI5pMS0QB6WuHCnd-vHhdZzWKRWqpsNaOVxbTS_hZEEFKAt9aoABOT8hLGsoIfF2Tmt6zgaFiHUmmeCzJKxi0zblkMuZFmdGFdKw8DVi2vm2steqpmvjiHtNmnDzkuMVJSVPeMllZP3O9q5S6cyymdFjBP-BFNXUw_M-FOKJUSZorhii88bLPr2jDktveCvF3kz1PHcLAgFdQutF8naDSBg91LJQtws8GuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله جنتی: هر تجاوزی با پاسخ محکم‌تر روبه‌رو می‌شود
🔹
اقدام سپاه در به غنیمت‌ گرفتن یک زیردریایی پیشرفتۀ آمریکایی جلوۀ دیگری از قدرت ایران است؛ ایران قرار نیست در برابر زورگویی و تهدید سر خم کند.
🔹
همان روحیه جهاد، تحرک، سرعت‌عمل و فرماندهی که در میدان نظامی وجود دارد، باید در عرصۀ نبرد اقتصادی نیز دیده شود.
🔹
دشمن اگر نتواند ملت ایران را با جنگ شکست دهد، ممکن است از راه فشار اقتصادی و سخت‌کردن زندگی مردم وارد شود؛ بنابراین مقابله با این جنگ فقط با سخنرانی و توصیه نیست.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461128" target="_blank">📅 20:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461127">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌ ایران، روسیه و چین: ارجاع پروندۀ هسته‌ای ایران به شورای امنیت مبنای حقوقی ندارد
🔹
ایران، روسیه و چین در بیانیه‌ای مشترک در نشست شورای حکام آژانس، پیش‌نویس قطعنامه آمریکا، انگلیس، فرانسه و آلمان برای ارجاع موضوع هسته‌ای ایران به شورای امنیت را فاقد مبنای…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461127" target="_blank">📅 20:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461126">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6djHlbeMY9JF05L1VkMrWh6iylKaUdCU0BJdPHmnKRYGpvbBjv5qK-QQxE08a3kmSiA0bkDO_P_9iRMDA1XZ5T4qEyLX6KJ80tSoJ-sKykQZ9Q_vn3Q8Q72QE3yBd4cOZn-288GwQTsLWNBqyN75i82_AcWvR8TXRdytnDzjwEg0SLkrpf8XV36Rw0fSyzhoFlnPiCVInJmQBJ2Bhcxnmyl3zAT8LMbNCT0saxgP42PSj_fWSGZzSsRl8g3ZEJ0uMg_U-4y-10hqyPhglyuN_S8N8ZO9PBTHX_V_R_Pz3CDOz-wRMd5_L3DSOL9EtWfiASHX2iGNW4D0Gf09GFi-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۹ هزار نفر از بانک مرکزی اوراق سکه خریدند
🔹
در نخستین عرضه «اوراق سلف سکه» توسط بانک مرکزی، ۴۱ میلیون و ۴۰۰ هزار ورقه در بورس فروخته شد.
🔹
هر ۱۰۰۰ ورقه معادل یک قطعه سکه است؛ یعنی مجموعا معادل ۴۱ هزار و ۴۰۰ قطعه سکه از کل ۱۰۰ هزار سکه‌ای که بانک مرکزی در این طرح قرار داده بود پیش‌فروش شده است.
🔹
سررسید این اوراق ۳‌ماهه است و پس‌از آن دارندگان امکان دریافت سکه فیزیکی یا فروش با بازدۀ تعیین‌شده را دارند.
🔹
قیمت هر قطعه سکه در این طرح حدودا ۲۳۵ میلیون و ۷۰۰ هزار تومان است و ۷ درصد سود هم برای خریداران تضمین شده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/461126" target="_blank">📅 20:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461125">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شنیده‌شدن صدای انفجار از سمت دریا در جنوب جاسک
🔹
حوالی ساعت ۱۹:۲۰ امشب صدای انفجاری از سمت دریا در مناطق جنوبی شهرستان جاسک شنیده شد.
🔹
براساس گزارش‌های محلی، شماری از مردم ساکن در مناطق ساحلی جاسک این صدا را شنیده‌اند.
🔹
تاکنون جزئیاتی درباره منشأ، محل دقیق و علت این انفجار در دست نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/461125" target="_blank">📅 19:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461124">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnYm8B2-PxhWB0-jjDPugoggznu98sKfpr0UX_jVE9rdL3_wvCHlsDTFE4oUjPBRmDVnwSp1dYBoKDrOwBv-ywv4-fhgjAka13zkhEe6s99f3i09kb2avRH8-Dg9pOgluwRI9rLngOeBysXJLACWyJNYAqq6qCpXxOgB3rfrvObrRxsZEBAdl2RDdQGIjFHdCQTWucN6PWBjd61zHGt__-T017J7UKW6HS-27b_NdqUf6EqYJHifO4N8xi8Mt3Bt5OLrxZkAtojfHdi0fAHl8SUKDK7WrJi5bR4mNfLwXopwOwN5czIwsRuukj3l_2OWv8sppTjnRJnbSt7CxhE4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل ۷۷۰۰ بار توافق با دولت لبنان را نقض کرده است
🔹
ارتش لبنان: نظامیان صهیونیست از زمان امضای توافق آتش‌بس با دولت لبنان حدودا ۷۷۰۰ بار آن را نقض کرده‌اند.
🔹
هدف نهایی اسرائیل، ضربه زدن به اعتبار ارتش در داخل لبنان و در برابر جامعۀ بین‌المللی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461124" target="_blank">📅 19:54 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
