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
<img src="https://cdn4.telesco.pe/file/n1pOccFqBAwEGxZOe1vG5LSZqG0ZazPMcnoiVpVD3Hw9rvDfnWeDOd06NgkD56J7bxtL1XDgMPYTX6xtPNH7CfBaGjbP3AHcbwMwdptlA79GIzwWpL5v5s3HT-_0Eo1b-bjy6O7FuwMYrtmxLLmg8pRMGhunVLBqLh160IEnCbwQt06Jw8VAiRI2CXD06w1FK4ry4Sddl7xZJWgldZjlewVZFHD1azdOl05s2Yl3QUedUE4vhnTpIRET7lo-y-qCIKPSazZPSaxdkX_Na2QDeLisPVb7hiAv-TtmgLBpYKIXY66PmcWoVN3AGOUumTDp6l-Yqyfbzk18Ihl3Wgmp1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 312K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 16:38:53</div>
<hr>

<div class="tg-post" id="msg-24060">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCgb-k24sYBmYjXrCPnDnumGTaNbysBQmP-c_bDTEmlooLXbb2TcYZs3zcrARY6nht0Lmd9G7KiTI_9N_dCBScC91UMQyMg41gBQ7syk-KfZs2PZ-4aNYPMuNhQU5lbijtFSgf3SDKtRQmO7m30yncBl_ugpPblkD3SLJDjxyG_fje1baN8CvR79xG0rUw7RWdkPeT5TNrr-0HAPohd_a0Mobm89YhFIijaebVOp6Ag-XNOc84kGsQq_dWc3MQ75OxYY2HLNBhB_SiyEeZBBd8cDR_U4Dqaj-7uDC639CFw5OwI6RZad3qsrQUnZcNroT0oYUAKVWKFtdht0DddIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/persiana_Soccer/24060" target="_blank">📅 16:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24059">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3R0D4P17fMCICnQPCBfhDmQhEidQp_qX02FIsmgIblsahQLxpR6kqCOZiq1fjZA2CHWnpgstn0yJYKsWdfDbSG0EvbUxC6eQTcudgiHCcGcyHonFMKEupJah6EZHVS23B5V3lTyomibvf1E6UEtP_KgQKoVgBH0zHuW1_utSEPftqO5IvKOfKQUi1PyFpXsIocN4wzNHurgIErN4r9HJwO_OStgJHN8jtYakuDrwfbZWuIH1kfI1axRT52RMjxgg87b_pQPegh4fTWnc_XTPzVcMJRfQ62su4LtQN0fZy0f7BAhOEn5RutZPB5eh7DCiMVzaV2_D4Z9EBE3VNA2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/persiana_Soccer/24059" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24058">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiyRE1Z-pljjyVPh6WyFJ64bkfnJWomfFfRdEFA4OGopDOw_HpqsTDrV37_sIxTBlOUDvjtF3IRvKw39wJxV8S9zbs8MqmNTiqTbCFskm4Fqi6vVGkOg3rJEXEV1az-41H_G1x9oiTvk4LB3TjZbPJayuqQ4igfPU6_lcT1gzefhwuDMgCpjulO1SVfgp_yIGpeFzH1s2F6mKW8T2B1z6WCAME-sjY3LEkpo9wVRuQOs_Hy7gQHb94Mg9fBMOnhPJ5dBb_ksohu1GIYjcMZGcW6DxLvvHQo2FYfVV3AJp8y_vHf0DYBrgCNOSkKC4nRsmiyx2lNVxH7D7nV32pDV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمام‌حالات‌ممکن برای صعود تیم ایران به مرحله حذفی جام‌جهانی؛ازتقابل باعربستان تا یاران امباپه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/persiana_Soccer/24058" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24057">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALBkCWwskFeeYUAen-S1-TPLmzg6_aumPtAFocAp90W_yr5UyCtrMYgTf1n-iKDcH5qwCsh0H1tveTvvB3EZsw5bsCmcPZkXnLWsPzY0Kx1CKu8QmD7La_A_Spwui8dJRqYoZNQWRoiLZ3HQ2EDcwGdN7nPtE-RJigxl67xRM4aNRowgaRpWdL9xeyA6LhjyHHfd2ePMznDhqw8upklj9Sn_SP5kIwoX7DIi6_A172dZ3lY9A8ybP06SPqUBcnK2_CY3V8vqkauvwaBO_o4U6EVR68e1iOU0hO6e1wcTWPrlLpyMpY0dFmv-T8CRXq2JiW0f0MeQsduVR5Js5UPT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی درمورد عملکرد علیرضا بیرانوند در مقابل بلژیک: این سری خیلی تنگ بود خدایی
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/24057" target="_blank">📅 15:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24056">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fba3c01e.mp4?token=SObbQ9xxr6jQ0z3QI03OwEElQv7odLnBD1BLemOfTUW5mNB9Mi2R56wh7C9913EuLvQM3wQGuBJFaTGB-3Mu43-hWEjBmqxUMnqNiSZBYebYT9i93NQGd7U8bTfqLtUvVl3tVgvwpr2qd0tUwBu6QXAkjDcwxxPOoqUCta3ss8iQaXiYZRclusgcDLaV9UX65qQUARyhUmCvW7vJAN14SZqWKlkZN9NPnpa1QZ1zRTunkRju2fV-lj-X6-YlIhoE8QwWP4pee1LirEc5bekQu1nIU210obG3BGYKVJuGiaHgD5zbb68zASEgtbWFqWDcmHkZjShzrE3Y5LEE0GRKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fba3c01e.mp4?token=SObbQ9xxr6jQ0z3QI03OwEElQv7odLnBD1BLemOfTUW5mNB9Mi2R56wh7C9913EuLvQM3wQGuBJFaTGB-3Mu43-hWEjBmqxUMnqNiSZBYebYT9i93NQGd7U8bTfqLtUvVl3tVgvwpr2qd0tUwBu6QXAkjDcwxxPOoqUCta3ss8iQaXiYZRclusgcDLaV9UX65qQUARyhUmCvW7vJAN14SZqWKlkZN9NPnpa1QZ1zRTunkRju2fV-lj-X6-YlIhoE8QwWP4pee1LirEc5bekQu1nIU210obG3BGYKVJuGiaHgD5zbb68zASEgtbWFqWDcmHkZjShzrE3Y5LEE0GRKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی چرا اینطوریه؟
واقعا دیگه خیلی عجیب شده، یه‌چیزی میزنه به حضرت عباس؛ لحظه آخر قیافه خداداد عزیزی خیلی خوب میشه
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/24056" target="_blank">📅 15:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24055">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC7ZcRlJaK-PxNIGGFugGqHaxDEEG4mk3PRWAtCI5ms1BZ91Jf5xtOQSBCP2kFpkt9o4N4uPSX9sxzAusfeG-aUWoJJXfy4vIDLijCwzJjKJq7pT0xvW4JMqUoLV_MCzJ-zIlo49n115mR4LbVQl5DdEtm15yKDM3bHIq5PLd4DYuzAEDHJL1OQHfadtxKFO_3RXx3gsBdzaNFBt162RmY2w86RDsBLAtimTxZkBRt0S7wXQxwP5p6nmPbZs1D249O8UhVDDfGsouucKMGcE88DlmwT7dcu-PpR0euyu1qA3SddRQjyXlMzEPQRgwi9fRpCr5hSVUJRbuAdfE3-uuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
#تکمیلی؛ علیرضا بیرانوند با 7 سیو و کسب نمره 9 ازهواسکورد و نمره10 از سوفااسکور بعنوان بهترین بازیکن دیدار بلژیک - ایران انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/24055" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24054">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6565fae72d.mp4?token=T7i37vBdmXjDoc6jVKu9D64MifQLH-jtoFrFYf1HJdKR-gocjgn_Wptg_gTRRJCFE9t2XYHM6hGeUFQ5GaThPMQVAVZ9SokerF-MnGZPhnaU5wIyQ1THiHOqoOUW7exhR6EZDMeLJVR6FQ0J7Ip5Mfxpr9dGl5GiI_gb_DYatNZai4iJoSUMZWsRcamziLRYGRDkdt0C9WMsXGBSyxpJp2tZCO8VyEAj_nlG36PlOOsqwTYdiy0bH49mxUwQIZU1zRGYdnFGBC6gKQZruw3GndEEc6cO0LmzGauCPSqejUkmJvJptQ6xW6xEQ9JtOqG-py1PgKtCLFKQF4KrKiMMPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6565fae72d.mp4?token=T7i37vBdmXjDoc6jVKu9D64MifQLH-jtoFrFYf1HJdKR-gocjgn_Wptg_gTRRJCFE9t2XYHM6hGeUFQ5GaThPMQVAVZ9SokerF-MnGZPhnaU5wIyQ1THiHOqoOUW7exhR6EZDMeLJVR6FQ0J7Ip5Mfxpr9dGl5GiI_gb_DYatNZai4iJoSUMZWsRcamziLRYGRDkdt0C9WMsXGBSyxpJp2tZCO8VyEAj_nlG36PlOOsqwTYdiy0bH49mxUwQIZU1zRGYdnFGBC6gKQZruw3GndEEc6cO0LmzGauCPSqejUkmJvJptQ6xW6xEQ9JtOqG-py1PgKtCLFKQF4KrKiMMPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚪️
نمونه‌ ای از وضعیت متناقض جامعه ایرانی درحاشیه بازی شب گذشته دو تیم ایران
🆚
بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/24054" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24053">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d16aWjPoQRmUWBJLky0pfGNE78av3J8wMk08KJiFSmLrZZ19s5QZZwgi6Dam8HLweH6gkikd45AyZHw17vNK_yvnQWLpUqlqHe628y_HD3NseVwHh9-YJk1WEKAHtHLCrMOtDiIhnhF_pm0QJ6iFHVRH6HWvrvjUMUymmiPQdfrGlXQo6Wc0ANhs3qwvpFyYAWh7OzrPRIZUEd3XURKtm5R6V3u8GPrCvGPDwMaUIuU778pAkOa0LSR3V9ygCbznFSvNHVDFb5YZrRq1sQ6QO13TVlgjvIVvfNM5bxCW0ERY54Cp4UkYzmmvUogJcvn2nMcBrxHJgsxNRa24pJWgnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
استوری معنی‌دار اوسمار ویرا بعد از مذاکره باشگاه پرسپولیس به دراگان اسکوچیچ: خدا همیشه خیلی خوبه... متعهد بودن، حرفه‌ ای بودن، با دیگران مهربان بودن و قابل اعتماد بودن یک انتخاب نیست، اصول شخصیت انسان است. داره به مدیران باشگاه تیکه میندازه میگه وقتی با…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/24053" target="_blank">📅 15:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24052">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaQCaYT22uW6wEiOjehp7nJzsqQZKNkpYHuUnpZ06U0amqRxX-OFCjxBsgCMmNKQPUh48-IvlfSCTp6sUbL1K_MqsQc63QddE0zMTxU-6MNvmx2m69oY1HWMsTuQc4XbjchAEa9dvFV6pW6A-gKOqUSbKPLkTGMICU4QCbzTmlEc0lbPvUUEUKz_FPe_5oW-Xzwu-YwtEBVknyvpQ5f7g6ALNaumDyqffKyicYUhmDeoNXzvQA5Q7KTLrcMxl66eAIVv0-zxUfDVSAUgmxQuCTMFHMYswG37u6R8YAfW06txrr91K8XQvReNY1skoxw3IASsZXvObgHg2SC02bEzDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/24052" target="_blank">📅 14:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24051">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrsK6s5r7fnRajp4p0SLziPUUhddHL3sQqAwYlph9dQixLOeytmik4Sw3w64gnBsmVnNwKPaXTv_f_hlRP3G4Xs_1HuTH36SVbe10gjYWeF1ki0U37pxI8IextknawneFZNz-Rfy5mRtXyN2n2xIWPNPuwj6NI3X82WCTsWEjGPiL1tfOOQT4Q4-bi-LYE200cGUT9kj32v---hMqfp5uaV1PInmKPjS-Fieclr6fp_0a_uZO_26CMxNQTI9-uNkzbGOGKhE9zLhP94k6SkVTs-9UcXK4WEomf7MUTNa-wyRN8WHEi6bepfB7j71wnQkEhvdfYLtOVBywWFoXYMymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
در آرژانتین یک دین جدید به نام مسیسم متولد شده؛ این دین جدید که پس از قهرمانی آرژانتین در جام جهانی ۲۰۲۲ پدید آمده در روستای لا اسکوندیدا درایالت‌چاکو آرژانتین درحال‌گسترشه.درحال حاضر 3900 نفر در این روستا زندگی میکنند که مسی را مقدس می‌دانند و به آیین «مِسیسم» اعتقاد دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24051" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24050">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⚽️
از دخترانی که اطراف ورزشگاه‌ های جام‌ جهانی هستن سوال میکنن که جذابترین فوتبالیست کیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24050" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24049">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM_EjY-ZQLKAGfWayghD7MlvH817yCuz35Yljy0BxJsAFk46Fyyaejuf-s7MWX2qb9VfkszrFrUhUIim1lcIDr-NnBYeU2NhWkd9hTaoGh8nU-MLzM9d2EOQaQd-m5dzbp4bnx9ci-eIWg2imeZHfb8BVMFp6dMwWqYKdjAM7k5r2vP22szg-Y7aAM6OakultQOb3pb8fjNzNmew49jJtngABbx5ovpgUqrM4frhZJHkSj8f_W36QKl7kl2W9AZDBOeWBdgv8zWludgUnn84aiVH2GRL4cV6X5-kZxMBDTDEIh-QnwlBeDXZWghgJJgc23yfPOft9ja5v8ZUDIK3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این‌پاداش‌پول‌نقده‌ولحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
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
کانال اخبار و هدایــا er1
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/24049" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24048">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS4vfviphsew9QRCrE8hndzCpE8QJ0Tve9T43mtxQn8UOFsTlXyjzp6Jtk1v-j1P0Hd95NeX3vgfxTlntWu-MaZdNMA0ztXQqEAshO2Fq4KrOJMu0gZrPdRU5GVyoVSYP-Z8nxA3ZLM2hgNz7Hb6VkcFtH3RH7IGOyssAdNB8_fWWJvPp8iizE-F1m5jpkh9QjX0cuiue5E337Yvkb_hWDrJgBnO6LRkhUGEHxMrwFa3JeExUJ1yl9ZFctYqZvgarMxoBizdLb4WRNFtXUD0XybBwJNDTKa5im7FjzZ20Km0lcJWJDttFzu4PX_5MPc9q4NHDyouSHhB3DKeD-5c4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ علی تاجرنیا رئیس هیات مدیره استقلال ظهرامروز با محمدمحبی و ایجنتش جلسه آنلاین یک ساعته‌‌ای داشته و پیشنهاد مالی بالایی رو برای 3 فصل حضور درباشگاه استقلال به ستاره تیم ملی داده است. محبی ضمن تشکر از پیشنهاد آبی‌ها اعلام کرده اگه با تیم خوبی در…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/24048" target="_blank">📅 13:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24047">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGI_flAFaFTD8iI3FC6ZUimOq4G2Pq5p57W8S0ePb24jSgvaoKmAI6jJqQP-F1cyu96LqbiGytcypdGkWFtlUNqHzgJL_9PrRnQWAMG4PuFCKT_icqcigUpIbsBSiYKAjYi7RzJXe141Y4T37kflxScn71c5dQYw-Z3Xylkd__jPrxF-YopozScGFnltyrWxxckExak4eiHlvlC1Mi5rhGQ_xTdxvgpr8sqWbNhIa8x2D9OFc0ctGFRGaclSSv5fd4KrCJBJwx-6JfHEy5VPJqsKSN2ksGmhnILBXy2MhqSVeTkzHfQoGULFGy4ihuYN5EpefTOQobRZol-6-l6AEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تعریف و تجمید بوفون از علی رضا بیرانوند:
قبل‌از این بازی هیچ‌شناختی ازش ندارم اما عملکرد درخشانش در بازی شب گذشته باعث شد که راجب او تحقیق کنم. انتظارداشتم او دریکی‌از باشگاه های اروپایی بازی میکرد. دیشب فوق العاده کار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/24047" target="_blank">📅 12:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24046">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej7LNxIfKHR-fSNXZXx7icM795bgXxq5h8C9fcz-m76fBTFYqWFKynEeNT1BfOQgO5yBH6m-efIpSbv1mM2iVJnZFQN8ofv4ox8Grl_TypjtH9b3JneFpdCmLy2IoBe9YQymJwRjZD94q_OoNC-XoqTtdy3pOXYeG_wnAgSZj19_XecZIL-uBXv0JLhZNVjvP_FjPtGH5RHJSd-xJZ08uDzu_98nHh7Z20ipp_jgaHKwJGfEJYNocL5SWzHAljT8aN0RLxmiqElz_3bGfzl85N1JfCarI5hFW9EYww_8FSAPu-UaJvIW6143-nbr4eMg1WhPyPLnoDYTRNTJRg6aRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24046" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24045">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV_PM1WZpExdxxHjE-w9SDNklplEudZMsLyYs7ZBzVgWMv3vyJx37JIZAo6REx9kZgLPSLRflpcRSXC0MsgV5UkNVdlo9_Vg6ZPM76vsVqIG-R-FR-pVKgwgKdBBEES_8swATmfc5RvbU1v9H7QU4hDigkAOfZkxsyfEugXjqcZnGMorOqGMoYtX8TDJns7mH6PZ-rpPEarByfTggjq6GLxDOA9BkjwCK0ZMHXfXA0UCOfYqVhlrKscK5q6xkTw-0RuvXZmc48m8826ZTPIfZx_r2s83XjNDzaqf8zhKTHvSTaCBNp1cIxumrSNSLUTxpxY15GpfVxVRba0XoA_E6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه پرسپولیس طی ساعات آینده مبلغ توافق شده رو به حساب‌باشگاه‌روبین‌کازان پرداخت خواهد کرد و سپس پوستر کسری طاهری رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/24045" target="_blank">📅 11:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24044">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGb2liRYMckM8JKVYXW89ksRKPBUILPzcteOpkwelfL1-kFER-rL8KghnP9Wcz8SQ9RXsoYJFntl59W0sr0V6LqjddiQGkRmO-y5MQa0k8ux8FxQecBg1RNfnieeo2wjx6T0a2KVUxEGQmTqu-OV7qj6a6tF1UeXsROcFL4rlKj5ZruKxw4EoBbkuzry-fVOCVJQ8qshYrfxnUe69T_t4fny42JH-zh66DsOHHBDZfEU-VKkVPBQR3nNYEgu8fCfY6KKme-PcTtcP4FhxK5qLvJlXx2kGJA7XOo-tOH7Qz644iQ2CfA4jLdRYJUj5bxEel39BBnGEMYlR9dtGL9QCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشگاه آزادی از هفته چهارم لیگ برتر در فصل جدید دردسترس خواهدبود و استقلال و پرسپولیس بازی‌های خانگی خود را دیگه اونجا برگزار میکنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24044" target="_blank">📅 09:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24043">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAHynf0CQyurmErvkH-XUv_gYXTT1ta0sDzWtI8ewyGNnAW1qPsgdIcBmg93aeZ0Mr_mWZmixDrZ7GFyik0hywG1bpn_ISeP8cVfenVjQWh2s1htN0ZS_DB-SQLrzLhASl8jjK57_JhAeYAAbtlDOxrRSKy5Oqr6vxe6DYtitrrHqPXLRWinNF4-1ocEy0x2YjqK_vj_He99c9ivwO8PTuo-Iz3OfqW_2XLQ5H34JQ1rsEXd28dEQR6nWw935sAq_vujJ4jEh8HqFuva9WLY5FcBHR3xhEuyWJpV1NbtZB-GdkrMBgs-s6-lj-nB9i0FRHksGy7FHIzOTtMHc1ltcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل مرود ایران به بلژیک از نمایی زیبا و متفاوت ببینید؛ جوفوق‌العاده ورزشگاه رو هم مشاهده کنید.
‼️
اگه‌که‌فرم باسن مهدی طارمی دقیقا مثل سهراب سپهری‌میبود احتمال‌اینکه‌شاگردان قلعه‌نویی‌ امشب شگفتی ساز میشدند و بازی رو میبردن زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24043" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24042">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbGEOIKIArKtQuMXyD4WJuLoosSYJtx2Wp1tOAg3ySavNmWu0PXJjOUnw6bdev3KDXQCvAootMHzE0QpHhTa4AwcgOz5pyNbciWSTRqIdITwCi_rUv-aA54ZNqIYOVoDs-whbFuckBlVu_zOVyQN1A2nbfX5xxVb2_oqAlOmBYTjiSCZULDZ_R4ayhIr0ZIxpIRYYcaRDBMcrzucYn3PTI7L_gZwXJu-KtDA2I9yMlwE5IQbhm9MoxPvGm2YAw6hXwQprHrC7QOd2pkOxc3lYNerEhCk1kUEJtiPOs4WUIrjnU2IPcL_SSZLoexuPxOsgK2J47Z-PqxANi3O0NEUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24042" target="_blank">📅 03:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24041">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0ALhM-q4F7VI6tXIHVNXe9EVf1RCLBqjA9Q2I62KiXAzzEFpUk1OF-MOSNOcgkCLRXSEts3K9IwsSxiusCJjgmJMBsPtLkXmwWLxAPq9jjLQR_5MAcssJgnCjd691kW5gWZSdyMtjKUHmdS6e-c3U7ZZXPPOEsG_9A0FCJHm5Q3Sy3BLRYn0VGc5QW5G0vQeeZdNR4peYJ_AVF6ghEJSaBJEDfLtim85s_YMHPSgsCf0c1qxDfXcXOC84HMGKHPfChk8Qkd4vHC_7SReNFJLV4ppG4oZxmLR0PYXdeq5jRLDkLexy62-iKhBSA7haoxrwyx4C8xg7UZihqy_QZgmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24041" target="_blank">📅 03:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24040">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚽️
گل مرود ایران به بلژیک از نمایی زیبا و متفاوت ببینید؛ جوفوق‌العاده ورزشگاه رو هم مشاهده کنید.
‼️
اگه‌که‌فرم باسن مهدی طارمی دقیقا مثل سهراب سپهری‌میبود احتمال‌اینکه‌شاگردان قلعه‌نویی‌ امشب شگفتی ساز میشدند و بازی رو میبردن زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24040" target="_blank">📅 02:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24039">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e90d0111.mp4?token=aeVXUoKVxETEJU0sbQnp6QI9bXqQGru8zcr1MbphMsTfh8aMhoLvbbPOYVW853vWav0fZb6j440CEVMWvrrheTRdj4OYLn9ncuFnfq5IxBNE_7a2_voRDoG8OO9PfkDURRbQOZABWh7QVYeOsnUIwf_jobjEe8HAEggYZhe7YPd8smHGVYE42BRlZEQ2AJKzi9nNpaCX7UK2iHDfugqTeaL5qNl80B4TEq7ezdAv4GQo2B04je_zsYu-gk_dU2NQ6ouo9tDKT2KH2vxcRTZigDRFDfhNW59DlqmCeaK-_9sLfuCjzxzIWVB1byGUSpyDKOPlHocXV4MIYJUb-jVW5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e90d0111.mp4?token=aeVXUoKVxETEJU0sbQnp6QI9bXqQGru8zcr1MbphMsTfh8aMhoLvbbPOYVW853vWav0fZb6j440CEVMWvrrheTRdj4OYLn9ncuFnfq5IxBNE_7a2_voRDoG8OO9PfkDURRbQOZABWh7QVYeOsnUIwf_jobjEe8HAEggYZhe7YPd8smHGVYE42BRlZEQ2AJKzi9nNpaCX7UK2iHDfugqTeaL5qNl80B4TEq7ezdAv4GQo2B04je_zsYu-gk_dU2NQ6ouo9tDKT2KH2vxcRTZigDRFDfhNW59DlqmCeaK-_9sLfuCjzxzIWVB1byGUSpyDKOPlHocXV4MIYJUb-jVW5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24039" target="_blank">📅 02:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24037">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBTM3wwlGhQrtYFriP11Ya-WEgtxmOJ0luJTDG2Hp-rP79eR7JYMUmri9CAhADruqdgFVlLFkSyP45Fs03n9by9MAIILDRBLwNxvZz7efQlkJu6RBqxj3v1mIX_vcn58HY7KiBQy2G_pu9P5wdt61tdRaY2_tQLEbsx6VcF3rihbeUQmqMmzZLeZCeEUV8TSezmzRYBRcUf728Mud_JvtWDx_z_USnQ4yl1FcGE-ut7j6wM1lUw6mC8U5h0FqGCRy1M1jDjT2zqO3niiqnmhU9seLCJ2dJule_3Nlj-Yym-QnfTKEa4SshhsBatEhUeeBnxRxYmwxZa71NmwyQrJsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24037" target="_blank">📅 01:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24036">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfxXeya6rhxBerr4tGY_HwO-4PM0ErOt9fELLzvbo9azRbtWme4jIaar4GOKM_EftDs6zvCUp_y4ZZJ3Xhk7oSO9Vy_2k7kfD18HKH-c8C9tS9qvaWwpaCp1trDMInRrfhKnoGVnLKSmlXLc8vKowooSLNV09EY73OaIBKBk3hcZxo6uY2mBXYxIxnW-fso3zwhchhx4cfy1OPM417pRJMKbkXukIVjq7c70J2M5ZauLJbwtUCyz7Io5c_2YTGtDx-9mZXq5f-7A6JTnJpB_ipR1z2W00Yiv1GCCKujeTnbPbfzJnKzKEBRPLJ3lLboHI8_3zrpGifZlkAULGOsfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
#تکمیلی؛ علیرضا بیرانوند با 7 سیو و کسب نمره 9 ازهواسکورد و نمره10 از سوفااسکور بعنوان بهترین بازیکن دیدار بلژیک - ایران انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24036" target="_blank">📅 01:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24035">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d43c42ae5.mp4?token=he7bLiysfvyrHJqmJvxxOrZz4vPQYurHJikHcT_qXq9eFaFUgcWHcM30AkL_zxEZFWlPXTv4dDtYBksaqk8waR_aIqbaJRivNoCS0F5b6QGSpoGOJcv9CIN0OJcjWJcmBr6ZviYNV8xHAPdyYywD0QttmZEKPmI3bNJmeJhastgFVRuXAG9iYH1mUCQ3I4uWMBzMiWtVzBAY2TF2r4BQoQHXrq7tN3QqPRhRposmpS7-HR7g5DkMii93BHpa3UA77htQR6MaYaHtqtID_0UI0SLq7hpMPBFZuNCcBCQ95d-0NqQsL2uhutLtoM4lYPx5OQ0lGTJkwiKCe8jjxBAQ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d43c42ae5.mp4?token=he7bLiysfvyrHJqmJvxxOrZz4vPQYurHJikHcT_qXq9eFaFUgcWHcM30AkL_zxEZFWlPXTv4dDtYBksaqk8waR_aIqbaJRivNoCS0F5b6QGSpoGOJcv9CIN0OJcjWJcmBr6ZviYNV8xHAPdyYywD0QttmZEKPmI3bNJmeJhastgFVRuXAG9iYH1mUCQ3I4uWMBzMiWtVzBAY2TF2r4BQoQHXrq7tN3QqPRhRposmpS7-HR7g5DkMii93BHpa3UA77htQR6MaYaHtqtID_0UI0SLq7hpMPBFZuNCcBCQ95d-0NqQsL2uhutLtoM4lYPx5OQ0lGTJkwiKCe8jjxBAQ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
گل‌اول‌ایران به بلژیک توسط مهدی طارمی در دقیقه 27 مسابقه که‌افساید مهدی طارمی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24035" target="_blank">📅 01:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24034">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd1eVXM7OF1I72uvVGwM4jHD30w-6VoWCf7eXOstSDJricxTJXE2E5nBbEgi9kM7rqVHVMzUhuSKmnZyJ_8qhqN3vZNRgwi2qdQx4DTfYpQoFVnlhaj-GZoiCAf8fJKRCCfc55RtpA_NIKJS7EcZnSNUNBwfa0GFIVq6UFYKnqTHwzNNIbFrfIcGB065giyAze-1tGh_szfjA31mnbY_GhwYzKxH96-iU0QqinTXYztf59Ukttsm-xmahvtlccfZIsQAF2C8RGRRorPVRDSwVKiYfanLRnkdf6ul8oyXGvOjQHcKP6YzKmIHwJ4XV6ShqLIZSrzdDYwhsyFPD5H_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازنبردتماشایی یاران مسی با شاگردان رانگنیک تا جدال فرانسوی‌ها مقابل عراق
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24034" target="_blank">📅 01:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24033">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xut-WmmB2V42eDa4uRjudubo8QlT7-VoDYud6A9giqrpNvsv2qaTtKJteWyJJNrqATLjwgceHK-qLu1sNKFklcqOwF2ZsecP9SJ2pTRjOzOguqsXuAwM5JVpkLMt8VKdpb77BITSCiiXyy0QtSzkugC-R6Ssg4XIqdJRZIFR9oaEjTjTJxF4m3xQdnn5BlJIPykMT5DO6bUCgSIEAFNtFp8N8GAlj9QLzsVPT1wReIVArL-CDVaI4mCG2GJ3w7alitHvPyCcO_5rv3HE52F1aR5qeq1h_Gzkj5vn65Zz1XSA3rUHbo0WTAdkAoV1UmFVkRIIPko_SFOhhi63FahiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از برتری ژاپن و اسپانیا تا توقف بدون‌گل بلژیکی‌ها در جدال با یاران قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24033" target="_blank">📅 01:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24030">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de046aa0.mp4?token=Ux0iVJ-cGlfIVfnE5zO6HVLr8VxLDUUePhOMzNoVlJuxP1BHiQMmbZfzsau24je7VPNW9agZ8Czd_Idw9G-CV1XjxVv3SRaIx5jjW7KNlN9GIjOnpBAxu3J-2uF1hNxcIfFeExozIf0FGkv_qzlaKcafcpxd5jA6cIJzi7kgE-RarlL82U4XyX2JOSpY45yA8X3QB9gI2hqjuYkJOuLRGg61lbHiKhV3M8oHbmxc9Dmr7QlFl5n9bmizpSDHirfWF2EzZFi_lQWz3I_4eJpAP8L7AZv5Lbhtplg3kyoIjL-cW7znbMddY7fG67MmWHRDifcS8Uug1WJQWA1SAwKWbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de046aa0.mp4?token=Ux0iVJ-cGlfIVfnE5zO6HVLr8VxLDUUePhOMzNoVlJuxP1BHiQMmbZfzsau24je7VPNW9agZ8Czd_Idw9G-CV1XjxVv3SRaIx5jjW7KNlN9GIjOnpBAxu3J-2uF1hNxcIfFeExozIf0FGkv_qzlaKcafcpxd5jA6cIJzi7kgE-RarlL82U4XyX2JOSpY45yA8X3QB9gI2hqjuYkJOuLRGg61lbHiKhV3M8oHbmxc9Dmr7QlFl5n9bmizpSDHirfWF2EzZFi_lQWz3I_4eJpAP8L7AZv5Lbhtplg3kyoIjL-cW7znbMddY7fG67MmWHRDifcS8Uug1WJQWA1SAwKWbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال: بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24030" target="_blank">📅 01:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24029">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQGjXLVMo99Hh9dzqGQc3hYKW1CRQ-oO14AuDnHmZvPdHIEuKOesqqoxssGgGswTX7qg3giCz_vqNdpdzd6fk04XzOcXhWZzXdutEIOTU2GtkP89yRiUbQR-zoQClkYSpuC18GSoNSObyLjNHYqEwULfn7HXPsMWviOB0yw1o5rJQFI2R5E03mXwWgyPJMSGT264P7AnnggUnXLlcEsXhQjEnQkI6nXcf3TiqHRAll9t0BXgfQhCV16fhYNsjvnGrX_AWc3MQCYv_5JUmUvdo8IVoaqp3yPUT3Ray7C4QWzv7oEgQLQIG6MZ2viGWtxHAU9-lUzVUaUCACLLXX01Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام جهانی 2026؛ دشت یک امتیازی شاگردان امیرقلعه‌نویی مقابل ستارگان فوتبال بلژیک درشب درخشش‌علیرضا بیرانوند؛ سوفاسکور بهترین بازیکن زمین رو بیرو معرفی کرد.
🇮🇷
ایران
0️⃣
-
0️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24029" target="_blank">📅 00:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24028">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSthk7jnKtPoNB0hqhDl4eC2tu2v97eQvwdYEJlwU0rDNtQ_trbehlgSz0C7912Chq_X9g8CvpWkNVKeSwOw_KQ3PypVenIO3fwBXjZTaF1_Q_zSa3pSL5tlSo4uUaAtx_jhqp-qXZZ-0HFgTvLCuQSwlLFFaLa20X7IlORhXIta54eC8tE0v0sG8m7LkqlLfAZ_4UZK3Ggu_aH2LccCeFi1JgCFg4-hhfHpTttVyvEq6u6C8SqsuXYoyFctPQHOuE-ZwI8_VVvlqzjAGYf7gZNCkketjG9V8i-jgVXTKsZR1ZHOtw8oWHpOki2JdhkelV9fVl8vN0hLI7plKlc4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام جهانی 2026؛ دشت یک امتیازی شاگردان امیرقلعه‌نویی مقابل ستارگان فوتبال بلژیک درشب درخشش‌علیرضا بیرانوند؛ سوفاسکور بهترین بازیکن زمین رو بیرو معرفی کرد.
🇮🇷
ایران
0️⃣
-
0️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24028" target="_blank">📅 00:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24027">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smRv0klxaCYRKhpkL0OJNru35-HLfWLAcj85MFKUVMXtWJ4E3UIcgLLr-K3ANzJ2uQhGagJFNjWlJbGjwe5S5mD3lctywREiigIpxv35m94xAtEyzX3s24t4qI0QrG74hFl4qYCOuckNcvOVCaJXdewbXvKbBxhHD1UjmQtjP7N6QVsv_MR_anRxHpd43o2GgE239VYAwPN3z4QTITKb_XsXdMO7PksyPApqZ2qPlDGHwBCATeW7hFlJ8HU81EE26P6eMpFKxqbIq7fDB7FqthnQ0EG86M6fgBNfwF0FCKkNoi57WiJNzMubHZtlgwssjDbf5S0S6E-O_9KAU8w47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یک واکنش دیدنی دیگر از بیرانوند که دروازه تیم ایران را از فروپاشی نجات داد؛ تمجید رسانه تاچ‌ لاین انگلیس از دروازه‌بان ایران: علی بیرانوند مقابل بلژیک بهترین بازی‌ دوران حرفه‌ای خود را انجام می‌دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24027" target="_blank">📅 00:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24026">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54539b7e86.mp4?token=Sdy80QrTC0Ez6bJfTKOZkWiGgHTcJzHDAMo3I4-odfiPiAwxxTKJbF5OXKLZjyvOlrNq_VHs7aWrSIWfIC-5Vy6ghB_r-jx3bt79C8zKpOlsf3kKkvl-QjhELmvqCl5EZ0H3nYG2Vz0ZUqecVPM97Hi04DZPT_FstS4vOjo_xoon3yCnTdY8LeO5sofvhdHZlRuR80kskCwwyqwj90u6Sj6U7B2OKc7pfGb1kDTk6BO63hZb0omAeFgJjQzFK0IiIy-sW9DHaLNXGSc4fCIOB2eeAKwVaZrF4LJRZi_6hbN36xnjXYZvqSuRi8BY8yrH_EkFvNuGVuM3c9BwCkTg1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54539b7e86.mp4?token=Sdy80QrTC0Ez6bJfTKOZkWiGgHTcJzHDAMo3I4-odfiPiAwxxTKJbF5OXKLZjyvOlrNq_VHs7aWrSIWfIC-5Vy6ghB_r-jx3bt79C8zKpOlsf3kKkvl-QjhELmvqCl5EZ0H3nYG2Vz0ZUqecVPM97Hi04DZPT_FstS4vOjo_xoon3yCnTdY8LeO5sofvhdHZlRuR80kskCwwyqwj90u6Sj6U7B2OKc7pfGb1kDTk6BO63hZb0omAeFgJjQzFK0IiIy-sW9DHaLNXGSc4fCIOB2eeAKwVaZrF4LJRZi_6hbN36xnjXYZvqSuRi8BY8yrH_EkFvNuGVuM3c9BwCkTg1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سیو عجیب و غریب و استثنایی علیرضا بیرانوند که میتونه کاندید بهترین سیو جام جهانی 2026 بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24026" target="_blank">📅 00:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24025">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94db339245.mp4?token=OOHyRbxENwfl-kkbGhHcR0T8ene4ODN6p0M0nNmY7iuB_YUDy1S4QIGrQYtTtWv9bas7s1dZMtAW34y3NQIozq4DUV9kNotf7nrYd8lq48xR5D5RV_moZBc92cZ6hqJhJaejpTT6uFx0QBt2I8f1v2Z7Egw8H6o0flZt8bbFENWXhb5cpvj8D_2aDJPVcGTW-LLTiPJyrTEdRkSih9nND2eYtjeazf41WZ4zCxq3pJ6dBYckmXPjbnuDHiYfHQ2wMWBIOXr2B1NvLFHB5YL2rzcX5JahGOIpVC0AGfdAEhDTLlNzTLNxu4dZthTQQ0TSKMwxbv9W_40lTcYyETn56w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94db339245.mp4?token=OOHyRbxENwfl-kkbGhHcR0T8ene4ODN6p0M0nNmY7iuB_YUDy1S4QIGrQYtTtWv9bas7s1dZMtAW34y3NQIozq4DUV9kNotf7nrYd8lq48xR5D5RV_moZBc92cZ6hqJhJaejpTT6uFx0QBt2I8f1v2Z7Egw8H6o0flZt8bbFENWXhb5cpvj8D_2aDJPVcGTW-LLTiPJyrTEdRkSih9nND2eYtjeazf41WZ4zCxq3pJ6dBYckmXPjbnuDHiYfHQ2wMWBIOXr2B1NvLFHB5YL2rzcX5JahGOIpVC0AGfdAEhDTLlNzTLNxu4dZthTQQ0TSKMwxbv9W_40lTcYyETn56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نمرات بازیکنان ایران
🆚
بلژیک در پایان نیمه اول بازی؛ علی بیرو دومین بازیکن برتر زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24025" target="_blank">📅 00:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24023">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqQm8kxUITzxLxc0nPw-jm4JdejQpMoEu1nORDg5BpzBJMx-Itvkfl4fFLfcahZidyYiB2_qqYMjV_nCY04rhWE2lktqXPdqr5l_Q-YtFx0u4LLiV_09Dk3hpSuGA8yH0VixTDssQHYt2wHnxC_g_ASjvNRAdioW87heMuSFx9uiM0rkZ-fzjWfzfR9Nt1xd1pq8ruANsVv5aBWsigesxvO5I3esO7L3lDH4sZyoO0p8RyzkPs3P-yKo3D5JSmzBqGT4r8oxEb_WcKvQH_HHCcmHP1s7c8pIJ6vOkX-qTXH1ki_lDTPQP6AO_0sxki8pTzHwObFeODCw0dtW2UwooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6bhAp_T_TwEweUZSlV7VAWOfv6H8BwueXhuFL0csQiWN8C3DMviJHxRTlC4-1aC91T5Reob_Htdbbz19rLUSoENAxQUelTaSBKIoJOtgV1N07J-UAlXd-0y1JebmCKflaKjAylMSKqzxNJC6ANKHQpoSBBeo3yltRBSVJzgQH9thxlUuOyAF7aLOiUOQfsfl9MfO9V0PfOAE01VNogKNY5-0Us74tJlxWs-7zjS_g9ZS5c8ZxofXmLEZMgBRevCt3M-H7CqszbBe-rG9zJA2TrYtCNu78IHdRi9irJZnzN2B2l6gPOSpb4Wurzbo9qalfosHpibENiNS3cOWhiboQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نیمه اول دیدار امشب دوتیم ایران
🆚
بلژیک در هفته دوم رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24023" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24022">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUiWelg0YhRalCbBH4aAy9bEeTKLj6Kef4lxeWS66MNZPYLn0w1-7D4eIw__eG1ijliQ6xbCygRbDaMONGEuZGAx2WghP3ZGLySjQqOxD-u0U96SnZpl-OqNuYPTmd999ANtpCuhuOLUArU5u7402vib3irgzUkWFyQxBPNuDx3YWA06gXuZUCSXcDMz6E043UeutoM_7lQufVf0LTSJzXbQL05dHrVLIzOxdeQgVQyeeRBpRqwPMGSdmpmvjHuvi7D3YE6CmtV8JOtijmjXEbvKf2LQODoaxb3ok0FUUWrzNROJrxhYgO7e2-daxM9WC5gxHdla-7x1JZQBt55DMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
امیرقلعه‌نویی این تاکتیک تیم کومان در جام جهانی 2022 که منجر به گل شد رو برای شاگرداش گذاشته اما غافل‌ازاینکه‌باسن طارمی توافساید بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24022" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24021">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43b24a8b3.mp4?token=ONeJGTOVO_FWe8lqQrC9sFZGVXsBkxM6w51Z39NlqAlLfuIjYU8P6neK7y_vnPDYxT3Gv2ByqWb6ZLZMrL0AzdAORbFJF_SCONETpKX3Uf-lEs9x4loHfM2tExkpkJRWTng5BxkFPw43Ku9jzcy5zkhr1eOujslIAvijqByPIaHahhAps3vFMTtUYcLJf3nvd3H0XC3xww2oq46dBTz-6rNdwgZsNXHeOk9W0RAr_rqkRY3BlbEDgrhouqizUlrG5TH3WT_sgh3qLBZB0fTKlQsxJRDEOE0cHbFdBw9y2pEXqhqY0kRZWaCSk31g7_jYq5bQRJ0mFOi5ohTDWGmXOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43b24a8b3.mp4?token=ONeJGTOVO_FWe8lqQrC9sFZGVXsBkxM6w51Z39NlqAlLfuIjYU8P6neK7y_vnPDYxT3Gv2ByqWb6ZLZMrL0AzdAORbFJF_SCONETpKX3Uf-lEs9x4loHfM2tExkpkJRWTng5BxkFPw43Ku9jzcy5zkhr1eOujslIAvijqByPIaHahhAps3vFMTtUYcLJf3nvd3H0XC3xww2oq46dBTz-6rNdwgZsNXHeOk9W0RAr_rqkRY3BlbEDgrhouqizUlrG5TH3WT_sgh3qLBZB0fTKlQsxJRDEOE0cHbFdBw9y2pEXqhqY0kRZWaCSk31g7_jYq5bQRJ0mFOi5ohTDWGmXOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
گل‌اول‌ایران به بلژیک توسط مهدی طارمی در دقیقه 27 مسابقه که‌افساید مهدی طارمی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24021" target="_blank">📅 23:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24020">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61647a74d.mp4?token=tC5ECG6cqPDfLCWx0dKC7kbD6J6L2jJC9TSVR5jvwD5M76faS58PVNBYFiooXOxLfUjxeRbFuuYwTmCx4mzBYYY4y1NegvyMAQFOYYcNtbBSby-8opP_qhC2tUn9J75jCSIrGB-RLGpFAHCNBI4VhGW7HVHni0Zoyc9kW1xRo7RF_rDHNhHH9PMr14bVEaqVQRDYLLksuBzNMxVLBltB6mARktTmBrL1dMgqsxn_49mpWzl1na4_n1ljlUIrR-FmbyEVUVZpOTGVdre8YaXcTaMNkNEA6xPB-TIgvofKehIRQ9dS9-i5zwaqEtknRlL84bn1dUmJlmwAQDLv0gk64A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61647a74d.mp4?token=tC5ECG6cqPDfLCWx0dKC7kbD6J6L2jJC9TSVR5jvwD5M76faS58PVNBYFiooXOxLfUjxeRbFuuYwTmCx4mzBYYY4y1NegvyMAQFOYYcNtbBSby-8opP_qhC2tUn9J75jCSIrGB-RLGpFAHCNBI4VhGW7HVHni0Zoyc9kW1xRo7RF_rDHNhHH9PMr14bVEaqVQRDYLLksuBzNMxVLBltB6mARktTmBrL1dMgqsxn_49mpWzl1na4_n1ljlUIrR-FmbyEVUVZpOTGVdre8YaXcTaMNkNEA6xPB-TIgvofKehIRQ9dS9-i5zwaqEtknRlL84bn1dUmJlmwAQDLv0gk64A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24020" target="_blank">📅 22:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24019">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIoDMTLFn17s1lXpLZkXCIg6CabZpKanXceU2zpb3lCkOyZPuzy3yDA_yG-1Uf4N80Ax4Seo7bTlLO7YNanozffsIit4ZwTZ1PZbkSaXHZgDNrAzPDb8WT0EoEr6GlaE2TXaLB9Z_nwU12BvX7HekKb-m2_0mYb0J4yUeBXzd1jYzihCv1s3yU743ImP_ap-ge-f0ABL6vitqWeVglyxyPExW9mHVR8lLwR7aBuCh1B3pRWJtVJ3SJevaUcj44jNBQI2Xx8gLllUbjLlJnubTxVBMgcRLMBnOFzDMw00ZBS7DLphN0sfkdzUpIAd2mnYAUO2E-rM-s5YXLeSmug0rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
شماتیک‌ترکیب‌بلژیک‌برای بازی امشب با ایران؛ درحالی روملو لوکاکو و تروسارد به بازی رسیدند که سرمربی بلژیک گفته بود ناراحتی دارند و احتمالا در ترکیب‌ نیستن. احتمالا خواسته به ژنرال رکب بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24019" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24018">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0QlP3oOS0D7oIhzR0keP6ZOMBtqVUWETSWqFPhomV2be5IOOHu5Lwq5NiAqJOenjffC1V0QDsqErOxFOjUThAsNhANVTJwNZzENwwc3JkDRqgGmuwTz4304-dhxhFpXbBeD0S_W_8ZevGeGcimzNwMrhx-fPC00MGeUYIK9o307mIAOYJSHK3fm0wkXkWG4Ah_tLNHV3Tr6sQVmuT2ITejh8oDrBGkK1TtTPH5ZSzRhbxIifL6-459HKItl8hl7g2LBNEjXTgdCu2NtsBTaO0n9dg2d6QIRSkOtZvY-QvFlza4AiQViMlN0E9TniZI90HiA763gvYx4lax5Z6eTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیمان حدادی مدیرعامل تیم پرسپولیس: تا پس‌فردا بین اوسمارویرا و دراگان اسکوچیچ یکی رو بعنوان سرمربی فصل جدید انتخاب خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24018" target="_blank">📅 22:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24017">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI_4XYAsQaAflwS9w5jF750U5Lsrnex-anP61TPy1zjYJSsjiioxDvlyaeDYuoGBF1bQ6CduhF_We4FDxPk6DSG0obWPMgdJAK5C-m37HytvDC88WVbqc3agcqDQ43c1nzSueMp_DpCt1AfPTltN59e27W_PqMLYYeEwR0GdwfvhteQVdI82ePr9j5tDWZt8tEFVl6dUlJ5avWFtrCZ8LEsWwS1RAP5s0nEhsEx8rly3O8pNJWJqqy8_Thnejo6ErKnxQxKrxCSLRPUImsaoh9hBj0Lhx6nnYfv_NNL2wrgBiGnDQgEc06npq095TIXGjhVvP4luMaOgm0gv5QPtIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی؛ پیروزی پرگل و شیرین لاروخا در گام دوم رقابت‌ها مقابل عربستان سعودی.
🇪🇸
اسپانیا
4️⃣
-
0️⃣
عربستان
🇸🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24017" target="_blank">📅 21:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24016">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی؛ پیروزی پرگل و شیرین لاروخا در گام دوم رقابت‌ها مقابل عربستان سعودی.
🇪🇸
اسپانیا
4️⃣
-
0️⃣
عربستان
🇸🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24016" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24015">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvGaIRNH8MMqlgAcHRo9jgsfzp-aSXyvwnH10-UbkDPRnVzB8wKenEcAUwnJGkeSBvdl-UHOzk2tgnXihCyWVkDLZV_WqUB7u77ylwy4jn6ND85Ta7x22codgpVSNkonBvAY4WGMENhkrt1r_6DdfGMKZoM5FbGB3VbY9Qt4MCuDxldPNtYWWEFQDXkLOH7eLIYc09EGVVpfKll_vzn7cNlSR2x2H4z9iIHecwpDoKQlw6A7D98pqstsnmUWHBHLohqI9ffeeiCJJBoedu1ltsQpbUadggx6-6bVWgf1an8bQOwx8RS4eO4VXxq4klILTOX6UVrXFh-3UCAjyBILxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب تیم ملی اسپانیا برای دیدار با عربستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24015" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24014">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Umor9EBgvm9pjfw7FTGz0a36oSnfk8Ne07Sml_q4OJEuDb2fNTLA9-jUSMRnA9NgY0EBrsl6rFhRAtC0cVBrcN4-ctiq6yGz1HnD0pSRTO_nrOvrKeCQxMlJ3LNfN22TUctCAmBL734Y_ehUSPELE-BuQGfdB89IsiufD8JEw9GYOyQUyXmLbTLlktGsmaYrqPLzDqzd5CpACJ31yDuqN9vVgmySIHaJ1D68CXSrK-cYkzHoucuUq_HrGGAr7sotxOyaakZQchG8IjY2E11KfU-9kPJ75h8NHOb84dK1_8SLOUSQ5C07gGlDqJEOu6UGYgkOkD36_EH8jwuLfQkNyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24014" target="_blank">📅 21:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24013">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpLZvnVc4A1CQ9x8Ioxd1PEFF2AoFNxaWcLhYAxvHCqgL5TKynzZc8pdB3CgHx_S-8vXwGGm4YrcV-muFhmmpsU4FJmcci3z4iTzDqAV4fwGYSnqN3p2yvC5WjHxrKg4X4vhPN_H1o71hZbuKMbWfJ9f-BqX7nS710Q6GwhmyHYOheI9-ISwuTlDsP8V8ajSRkKWwwEJZ73sYDrQllI3lnCEfRVXPTZoA4_Opt23dgoqfgwBKTEnmGf8g5IeziOIBdpueDSE4jrzRB6jp9chQd7ayUzaGpMOphSV6z3Wu9Qi2dorMh1b5qfmZNM8LBtXi3DRvvLFbDMszbeUWjhjRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24013" target="_blank">📅 21:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24012">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaAWkDM_m9l1arP2wR1FoMw7TuWyPX_AVgq3BSWfWFJCm39XvslG8_7cYCdzfrkuZnOD75K2Xe5KFmQ6fEmaeuO2DC2dJ5Y85VBsM51GEcPlwCfoNfQZsZ7S0broYeIOA_Cxqy8S8R3NtAfd4q3wAWuXXacCVQH3tAmOHlfvEABsdIIPlXjfyb4OYhIH0JFukc-_RTxAUWqhvDUDKaq4QrH0XWVUjMYXT_-clWvSzrfG0QtI9_7zUUtB3zILY24TjvbjD_v0dcQq4XJ1dD4E7VJyJdaswz5oYphVIQYzl9LO5AGfM3N6thhIS-85EJ9Xpr8RX4fQ3kczeXaLVngjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026
؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24012" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24011">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxxPZzaHIYU4Yp-d-fN6K_3DquGY89GquBF3XHz6DqCzUVn5iRz5p9KVwwsFawvVc485jmQEjwak9MzUXVdgK4BSEWfihzv-YRC4EZsf1JmwVwT7QHRbSQ95fv3AjZwax-UvqZ1Z9K0j8WLjQfIFTU8N6iOYRKb1H8R8TUujJDYJ_ZCRLN5dzpDMaeaifXZ7z37m4anI6cQ1bd4Caw92zbPBfdZ9vu59GMsjE1lmOvlghQSYLKmOVKs_50daEBTt5ne0-n4fsW2xsz5Ix7J3Ad87aqi2GRsKnDOQ38Scr4Ny2LQg09lGkltWXssPHJIJSaeaUY9msPdBbx7WtFMi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/24011" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24009">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adYHvVvkTnLYCivtuQG6ENZYD6W6MPFWd6RfBZyOTkPwh7u9verpARlcpBkOO1daOtDvE3cSobJQEvJeybnn1zDqT98zHbhnsEUmlWNRAZdLkGBEwTP7b-SuYrAfqjzhXlatvy5ql3F95aoVwOj5i9d57wIbXjFV5dJ2H5F0bz6kAM6tV8rf0IgcWQSMQ5bvi9HctfzhTP7yOIkVH_Q9X9LlRfPWQYxjKMSP2blmQDiwR0arYV0zyeg9zMInRP8WEdA1zyh9brZEl6EjOxUFqgf9Aktz1H-GGD1FkaDcuYRVU1hs2Rp1Cx58auR6GGb2mXnc4ADG8w0OS27qesmLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛همانطورکه‌بعنوان اولین رسانه خبر ازمذاکرات محمد دانشگر با باشگاه تراکتور دادیم و صبح نیز درباره پیشنهاد مالی این بازیکن خبر دادیم دقایقی قبل تراکتور موافقت خود را با این آفر اعلام کرد و دانشگر به زودی راهی دفتر محمدرضا زنوزی خواهد شد تا قرارداد دوساله…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24009" target="_blank">📅 20:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24008">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk_lsHos2-C9jIFP5IgAPmcD0Z1wlwGCMZmc1t0-6Cv7xnWYnRh0-PiKTdzVV8K9MpccXzXwDNuOTSfY4GC8mdOsCMXyfsjpE0a0rKPnzrrAgJtm9cd5JM5iTzjmxUJ8O1ovNQgdM9tsJs9_QHAmAmFN9M4s86Mqo47Rgi8v7mMEyRFqtCWM0y2pf1_BuOagJ2vy-J2HseQAHuSyKZiZymIMagN6-pt9Tvisw3i7rUyesATazgm5oFo01elkZftmJwXFmxqhoiatwor4qKfmrW6kPkmJDaJTtbOH7RZ-k6toxqyHdBlm-4USqESD2yos3QjWzR2efogb9GCxu5q8gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24008" target="_blank">📅 20:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24007">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmUtGF7ZOuzXNb_2pm-ndRF3IflA46MPCqzVIlb-HSZg1GXZkw8dgcr6tvsd1u8kB96EFcFeYTvFx8FRlF3AUZ-f7bX5w4JiVo6v7IgRSTcI6V3cykth4unJQtL_i9ddm0IbVGgePWTUogdU3QiQc4BuKhousJ91DRiP9QDpV8I9duzy2PU755TolQujX2Odp8cRporAMvZ8IKbHe74QOGUPlJKhA2df3AZr2dNWGoUsz7BT4OkGOuckJdNlJ8nBS4AAix7Gou0V09dMTBLx60HXp7tPJI4vuNSxwCd1xx8GX5LQjs7O11Zw2j36bvUGl-DlI6DYWLX_X4uUTfWG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24007" target="_blank">📅 20:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24005">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DD323aD1Zjr48QXjUmssWripWeEdWwxwy_uezKB2B24ld-f6C4DM2k-vbdRBzq3TglFgTSHWSLVAgdSKsP-O55Av0ggQi373p5zyy6GKefn99u6SE2K3H0ZBtvbYlFqPN1td9H8uRyEngxrmWUcZbUQHlztyBS1oee1UxBlcLVOEup1YOAOdOy0B8p3lg878x7_ltrIgLwPZQeGrqhMIvltnNEu_BgaJjW8zGoRmQ5kFPnyccfNvm9pka9RM0UNDa5Tf6VpOCnOHFVtT19Q6oXpAdEg2msiykPZF11kAEi3UfxiueM9EUNWAE0MLFLZGYStlpqIZW2Mod7LYWhFtxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ جلسه‌مدیران باشگاه پرسپولیس با اسکوچیچ و نماینده‌اش‌دقایقی قبل‌درترکیه به پایان رسید. پیگیری خواهیم کرد نتیجه جلسه رو تا پایان امشب بعد بازی ایران اطلاع رسانی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24005" target="_blank">📅 19:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24004">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtCObCZJRanOYNMz_lTbUoWB1UfSPkXQ-CtU5XEUSaSDU14ROwEZAEjXL9lgZwghKL35pNPniybpREqpPfsRI5rLZX-eOBZdOpOhd5lAQ396TNCvlp4Lv-Fg3YTAazwdkn9P1yr4YbBONlFqR-Y7bdfRxc23gH6uDiCHhQSjVCk28VKoeXxSSJIpXEO39jkhgOdNhF6vzTKyzpco2E0M9XVP-nBScHYoVj2NFSHaWe-scE4M37bWuw8KoJ2BpnwlFNuKhJvq3lIB1an2NyTcuGjogjBEEb78FJtBPp6Yo_CFsD580eIoElwvq9nrryVTfSsjl06MFvjFn9tX0YL9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد دانشگر در مذاکرات خود را بامدیران‌باشگاه‌تراکتور برای دو فصل حضور در این تیم خواستار 190 میلیارد تومان ناقابل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24004" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24003">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HpXjDVmIm25Emdof89EKqquUf4VSyITFj_uKYMKRxQjWfF_X-y6lDrWvOfMq9hU4ZOSEY4qgf1BuztGXPORUHK6dlktyxV_B02rud_X0BEyOPj35gRUiYrcSzoYyZ4hRgfnzQ5OGBNQ-8oT2oSQ0Nc0qO0haNqSpUPGz5OujKrS2j4uiK-3is7PwpQCYFXJv05DIrdU8b_aiD7cBChwf-GoKA8bTgZBkLRUTDkB5THjIHTx2jaQt6wYHcqA4U78kBytkUp-yTdc4Cuq6BWsFIsCLCrEoxTh1v9uKyh9pTpDEQlMNu0i30iJJpRmKd4U1dpqCpiB7C0A9gCGndpcd8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
کشور نروژ اعلام کرده هر کی تو روز عرضه بازی GTA6، بچه بدنیا بیاره، یه‌نسخه‌رایگان از بازی بهش میدن. وقتی‌نمونده اگه نسخه رایگان میخوای، همین الان پستوبفرست‌براش تاکارای اداری‌شو انجام بدین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24003" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24001">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYa5cv6JCfJMhSms5ili6L1edRFulDlgizR9DrW3bLKhZ-diYhYx6A3d7sTrJbEa3kCLk1tGZOWXnrjnm-3Cm2MY4OF15wOptwoG5VelbRFuulWPP1fyKYHClFguXjqbZNxYIsx7qh_9PBC1ML8GSLk_4Nt5V3dN3s869t5kS7i18-FePUyccu9x8wVWE8PiN0XyrNVJJN0TnsrDygllF4_3D1Xqa_KPUnkD381S1cYsW_C0b9bjJqygzxlwwAnh0JFJZFDmPblKP05SFidBADYdk6k1c6iOm3VC7d0t319q35p_wTeTiCgdPCYaFK0Xaq6QbvDJmM07qz5w2kjfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانی</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24001" target="_blank">📅 18:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24000">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ngh7Nl8UF9tfx4MTSM9y9zLSzLw-eHeVJf0lA8ERGLkMv7HNM2gc4wu2uNx8aS0YCldl11NwthaIogYlx3b8NQrqomVk1BkhnLPZE9UFJrFrqPCnNb0XDXk1jDCxeDvIUXGjf1YZhzlYxkULNlMEelaGbM5FsBJ7xwnA5wnlwDlNKVSEo97-UcoBEY8xXAM_Po-3lx0GXAodqHhMXqVIhnaxDnqL2P0Jm_u2WlxoYU4oxqHuFGcsL8mXnY5Q_DLFHtaqu7-AtkCsnRPbsNDevqz_3rdvigsWwPUkEXpdQ5uqbv51iNy_SuODoKPZvHk37fMwgmElljqdL0-nE9Xo7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رکوردجهان توسط یک مرد اهل جزیره کوچک کم جمعیت‌در دریای‌کارائیب‌شکسته شد؛ الوی روم دروازه بان 37 ساله کوراسائو در بازی دیشب مقابل اکوادور موفق‌به‌ثبت 15 سیو شد و رکورد بیشترین سیو در 90 دقیقه‌یک بازی جام جهانی رو شکست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24000" target="_blank">📅 18:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23999">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe31d4a415.mp4?token=Zsjg879YQlKxO2n-CIPIpPUfHeCN24IYzKMvL-BqrrJwrtE7uD4zUGvO4qbCNeHei5lFgrBLjxwgZXCkoEo98mr2oo2evHaT5TAcGLyiK0ZFmIJhXrjKZt7KdMzY1AuKK0_--Tgr8aqQEKnRa8bXEkdZ7WlFsRNtyQur5B9RCzObDcs0E_yiyq5JEjZrUtg8TUiKqeDah3m2_2xB5mgzotVWKElYmq1eH3Q-hHF2J9F2JN_ANMrRdAm7yvaas8APc5KayQG62HXgi83PxmAIBmUvPnVUpfG4pchx_U-wm-GBfgpZ9W0rqNQEtMQTokRDJFd--NoPk6ul49KX1CFYLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe31d4a415.mp4?token=Zsjg879YQlKxO2n-CIPIpPUfHeCN24IYzKMvL-BqrrJwrtE7uD4zUGvO4qbCNeHei5lFgrBLjxwgZXCkoEo98mr2oo2evHaT5TAcGLyiK0ZFmIJhXrjKZt7KdMzY1AuKK0_--Tgr8aqQEKnRa8bXEkdZ7WlFsRNtyQur5B9RCzObDcs0E_yiyq5JEjZrUtg8TUiKqeDah3m2_2xB5mgzotVWKElYmq1eH3Q-hHF2J9F2JN_ANMrRdAm7yvaas8APc5KayQG62HXgi83PxmAIBmUvPnVUpfG4pchx_U-wm-GBfgpZ9W0rqNQEtMQTokRDJFd--NoPk6ul49KX1CFYLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعدِضربه‌موزی‌شکل؛ و حالا ضربه پنبه‌ای
😕
😂
رونمایی سرهنگ علیفر از دیگر نوع ضربه در فوتبال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23999" target="_blank">📅 18:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23998">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbWoFJ-noQ9pdLhuSCg_x8vQKt0JN5PJtXFpulUF4cU7vPJeH7-JQujUF811w-bj3SiheRR66teWhqe8PI-3qie1YkTV0SGpluScxn3RFxEtZIFHdYgDClwDrwc6XtrTDXR47Pzt00MBLoi5j8ZDTucUcZ4d7T-YFXGwjxWOXd8E3ZLjyPAoT6HtlAVXqs9Zud3IIrMNVqpBaKcEs8N8LVsGmQv4IRh1jr2a4FrdqubjsBflVZ1hpDAWrRBm5wR5QjqXy0gXALfQgn3dSoTMtYjgZ0xftcPUmoh49v5cG7wH56LUNfZsIQbRCBitMWa9xqoA62ngB6jqrnES1WdF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23998" target="_blank">📅 18:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23997">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk10i4Xpn_qF8o2IRa7vvYiYYklkc8Hc4-fuj5VnxLqV96FBAQYbPJHDrugCHyfvSl-YIp9VEWTAkvkFEzS0mI0mBl3Pi9gC9rkAwWV5_yuc83YJKNNqdJMVXi1xXaJ_rhjqKlqBAKNXRaVM6gkE8JPipAO7lLY6LiZQvCLgO-brWFpsc3I8jJRz-WlVkuqdahYoUyS1-RNNV4d84ihqiEdfAZGY334JQicR8WvqBf022gaR5chQJz6recXLe0d3xLk-HHqUpv16fOzFKaljGT9rmNTG8n-WD_F6NyIWASeeZF2aDWJUsdPe9vXhl9WfYuSwB6H9bclk2C79LUs-5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب تیم ملی اسپانیا برای دیدار با عربستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23997" target="_blank">📅 17:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23996">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kS4g3TRd2Jq7KCowXc03M192BnnTsqrUa_d5EtFO6B6vyeGfsjXkyi-Cup2Zwq8YJ2-dmLOSeFfhUJ9DdYJZ7tsiOdRErzyNfPrQPr37Py1T44510-zdDH3pkysdR3UlmYiUztW8YGZdBdhWuBk3Wme6kUuI_GK65yGugW3Wf5GMvKpF4BMyLvgtF3RPb5TSoYAsTQ5ktvOY62uQHrA7-DEdq9vzJ81fwK7S0AfY8rLjD6mINxtg_Slwv0ZLaytiKSBSasvEUZ859eZTa_nY4H7qhfuz-SbHXmA259lQ2viRPUREbrcdAxydlbPm8BmWjyR_hzVDFBq_wk7i5Tl4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛
رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23996" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23995">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM1r3o9-QK4kLLMUcUV51K1X9f46tLeKrt8A6qeKQtcOpC5JE54XCAifcxnPxhO7R0cmfgrjDY_uV74ZJk3JH18Ucpto7u7eZX8DR-WuIPqIjBVQu0P7KTgnj3HLR0pHiA1jtdYZe2U00GPaZzJQWvQyxReOZay34tZS5zSTJdX-x0zJXN8AjVSVoqzzyCb--PxWIEntwoBOpozc4vLwCor0Q8KGv-c61Z2rOcsfdr1K7VTP5dMqFt4lOsF3_7nubg71F8o8AKv7uWlLb4Gh0_BA0JhDJCIq49caCAKiBkmGI4Y839x5fhTYEANxcIDDP4jVwf2VfI7-ibJF1zK0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ تاجرنیا امروز صبح در تماس با سهراب بختیاری زاده سرمربی جدید استقلال گفته درصورت موافقت او سریعا با گابریل پین قرارداد امضا خواهد کرد. بختیاری‌زاده علاقمند به مربیان ترکیه‌ای است و احتمال داره دستیار دومش هم اهل این کشور باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23995" target="_blank">📅 17:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23994">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0r5OXTw970Y9WYEKAFU7Qatx8N9k3RElHix0DsPvSYsf2c1_XzYFZaq64aHFfMv0yALqSMuL2aCxbkfwIsVSFV2iFIUgXz09_fzLynNgM6rvC3nUDJNuD8KQRqE3oTHxyc829vFaCcKCqBgPeAuJg6k-Ob5XLi4XwaHb3Xb2JXFU1o9UNpWHodQDCF_utvLJ0KN911wN_vu-Asp9S9H8AIDHF-zphMeHrOJrhi8rYGOJnDCSulvB9ewRNhxueB0oPSI57-nysEJVu0gahEsgpBVc9O0XRGuhnc178Yc4ApzC3RclCPEjjTBgM6ViUXmiYjDYIuKYip4ERVlbR4ZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
جی دی ونس معاون اول ترامپ: باز شدن تنگه هرمز و پایان دادن به برنامه هسته‌‌ای ایران؛ این کارها قبلا انجام شدند! سوال اینه که ما اکنون چقدر می‌توانیم باهم به‌موفقیت برسیم. آیا میتونیم روابط درخاورمیانه را بطور دائم و همیشگی تغییر دهیم، یا به‌انجام کارها…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23994" target="_blank">📅 17:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23993">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420ab2f182.mp4?token=Zfe_kS4Fo-x7T082xhOtjsYys3ZiRKdDc3Rc7zaqzogSww9v0hhmpuj2dfuQ4GYAwP-8KmeCA0nwzeNzA2j3RkCzxUDIzuKYBmDheA8RpQZ-xxkLtB8NrlCPfqMWv92QgfWx79PjFst5YJI3o6t6eqtLjNzOGzi-kmrmrA_qv0eiet-dZDHHxhde4hRLTf_HE10ilBzjVIWCmCraw3-zpPyrGPTOC6jQLfY14FMRKZ7Pqp4xVsVYFmX3E6z1zyzxHbtOLGBM1-lRhbM3TSdPfP9dEAfP734MjgSvkytmbizInAXUgUG_Oksm4lX6qDmq1ZmO6FHCpPjTT1CbolCypQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420ab2f182.mp4?token=Zfe_kS4Fo-x7T082xhOtjsYys3ZiRKdDc3Rc7zaqzogSww9v0hhmpuj2dfuQ4GYAwP-8KmeCA0nwzeNzA2j3RkCzxUDIzuKYBmDheA8RpQZ-xxkLtB8NrlCPfqMWv92QgfWx79PjFst5YJI3o6t6eqtLjNzOGzi-kmrmrA_qv0eiet-dZDHHxhde4hRLTf_HE10ilBzjVIWCmCraw3-zpPyrGPTOC6jQLfY14FMRKZ7Pqp4xVsVYFmX3E6z1zyzxHbtOLGBM1-lRhbM3TSdPfP9dEAfP734MjgSvkytmbizInAXUgUG_Oksm4lX6qDmq1ZmO6FHCpPjTT1CbolCypQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باز هم ژاپن و باز هم ماجرای عبور کردن یا نکردن تمام توپ از تمام خط؛ توپی که بصورت میلی متری از روی خط دروازه برگشت داده شد یادآور وضعیتیه که این تیم چهار سال قبل مقابل تیم اسپانیا داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23993" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23992">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRhsGIhrV-PYC7ve40WGt1KWj9vWA2lLkWsfeS1bKVNCgmzTVP6GdO_ljgvvNylzi2GyMyb-X2PHdtRTpyBcAmeuUSIicOlEIPXD8uzyKVR2e_Ix9CbrdjGqqgbaDFfsy3BNA8wnZKiMGmqn3KBd5cUFdavOnfzG9rxPj2BrVPm4xNfqaZQJVWfC-M5FAZfznfAn6civT2boO_gA6wPaTMLaPUqGhEUKAzkNqDyya05_KX9l_q6dNPi70Le12RGx_i9Y8z9m6EUWf74c5blDt7CxD8YhYY-lj-BhALkHv8WC4iYjLWOzxJlnkLrfZLN_WAVxnzvLkXW1qQQhztF-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا رئیس هیات‌مدیره آبی‌پوشان اعلام کرده که فعالیت‌نقل‌وانتقالاتی خود را شروع کنند و دغدغه پنجره رونداشته باشند فیفا بزودی‌پنجره روباز میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23992" target="_blank">📅 17:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23991">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b889f1521d.mp4?token=m6cPMVHGx0qIe0yMXbRBVGBGlv__n6hHbh0H8xBc5NF7Jqkl0vXXzisxYunLSxfuWQOJeI4zpmdT1c8U0B4JkRi4R5Wi5OCdc-agf5xo652ycTGX-mhCvLX5jOgxaW16Nh-i-qapiLyvjsPBKgvU4PVod4zK-1lNw7GhKpuzjyKB1xQtrFJBP4LI0Rn7-QZEQ6FZD9GkzfrVbeGymgtZxoSQqSVATX_nw9drCF9rsevj9_zlcEbrJijx_j0EIrPIvuP6L_mxyPZsFDC8IJRSBSfdPX4aSfZqmus1b81xFBjbql6_3YrzIrsC6_xWDDKIS6_g0yduF4QcsnVWNNn12A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b889f1521d.mp4?token=m6cPMVHGx0qIe0yMXbRBVGBGlv__n6hHbh0H8xBc5NF7Jqkl0vXXzisxYunLSxfuWQOJeI4zpmdT1c8U0B4JkRi4R5Wi5OCdc-agf5xo652ycTGX-mhCvLX5jOgxaW16Nh-i-qapiLyvjsPBKgvU4PVod4zK-1lNw7GhKpuzjyKB1xQtrFJBP4LI0Rn7-QZEQ6FZD9GkzfrVbeGymgtZxoSQqSVATX_nw9drCF9rsevj9_zlcEbrJijx_j0EIrPIvuP6L_mxyPZsFDC8IJRSBSfdPX4aSfZqmus1b81xFBjbql6_3YrzIrsC6_xWDDKIS6_g0yduF4QcsnVWNNn12A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دهنت سرویس ابوطالب
؛ فیروز کریمی‌ رو دعوت کرده گذاشته رو دورتند آخرشم خدافظی کرد و تموم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23991" target="_blank">📅 16:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23990">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-TNfm9cZCSd93VkMCSP0b7qX27Co_28dg20fMCBbuy1YAG0BhHDC3ZSWk3Dqr6g3LYe8nwJ3XvIMR5ahfK2e8SGy13plEMtF1K0sv4CRJHz779Gu-iVr84oHvv-I4gdZp7leFg1alJAHnxL9FYBtda0QZkwoUfh2k7WgXkxrSnSUSj15wQzx0QoD6XSHjh06EbP0wyfjDej52Nt7-QPK_9Wx4heyHTH6ZaqBj9K8xA5OvBt7Mq3Oil56JAplHsRpWnFt5dfJ7UDEKv7b8wi56y9Px5uC-DY-egVOb-Ct9TacHqnEMIx2dqg2RvvrxWBBX_ulyP4oVFy7S6N2u9LxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
جی دی ونس معاون اول ترامپ:
باز شدن تنگه هرمز و پایان دادن به برنامه هسته‌‌ای ایران؛ این کارها قبلا انجام شدند! سوال اینه که ما اکنون چقدر می‌توانیم باهم به‌موفقیت برسیم. آیا میتونیم روابط درخاورمیانه را بطور دائم و همیشگی تغییر دهیم، یا به‌انجام کارها به روش‌قدیمی‌ برگردیم که ترجیح ما نیست‌ اما مطمئنا چیزیه که می‌تواند اتفاق بیفتد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23990" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23989">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c577c16fe.mp4?token=egycVwnY5c4PaYO6HbAH2MHY3nqVVcVfLwIVYSmquINAEeTs_BC_QWpXZNz6JpMUQ8WDnlTQUvCz13T_uczvxoQ-AEBQDaky-EL_y_wAwKNr_ASZCONJJVCzEXKOAw0prqQH-xMitr68FwajGVWpX-XbQYYwrzEKMGmYp8ISXVH6kyVYdtsm0Z_56jv4Sog7jWgrUMZ-fV1lXWOZf_UoYCNndtani4f5jCGBvXAItNqhE8j_hrlh0wrq0WA3ptcVkQRg4bWBrHM89k-UIgPgejZcqbXtHS7Te0Imh3IcsbBZkEDCa0i9PJnIfDIGwm0_ar_yhY2SWJPR46vAYoVYZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c577c16fe.mp4?token=egycVwnY5c4PaYO6HbAH2MHY3nqVVcVfLwIVYSmquINAEeTs_BC_QWpXZNz6JpMUQ8WDnlTQUvCz13T_uczvxoQ-AEBQDaky-EL_y_wAwKNr_ASZCONJJVCzEXKOAw0prqQH-xMitr68FwajGVWpX-XbQYYwrzEKMGmYp8ISXVH6kyVYdtsm0Z_56jv4Sog7jWgrUMZ-fV1lXWOZf_UoYCNndtani4f5jCGBvXAItNqhE8j_hrlh0wrq0WA3ptcVkQRg4bWBrHM89k-UIgPgejZcqbXtHS7Te0Imh3IcsbBZkEDCa0i9PJnIfDIGwm0_ar_yhY2SWJPR46vAYoVYZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساعت‌داوربازی پاراگوئه دزدیده شد!
در جریان یک مسابقه‌فوتبال درپاراگوئه یکی از بازیکنان، ساعت هوشمندداور راکه درگیرودار نیمه اول بر زمین افتاده بود، برداشت‌به‌مچ‌خود بست و  در نهایتاز زمین خارج شد.  بااین‌حال در نیمه دوم ساعت دوباره به مچ داور بازگشته بود، اما نحوه پس گرفتن آن مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23989" target="_blank">📅 16:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23988">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBhQOOY-O8vEE7v8UaBxGwd4ah4_m-Oyj_3o_uWplr-MicVgL7PLyl2H3MnDNnePw18PJSmCV6ljTUOERUBFIZsjfq1uGCU5BhExAYaEtc3eKnBXMgd6QvG0wUNTdVc-3IOtdwMCAOUup55wJuc6tTrKivLvUOOuRtBUmMmCIfW7oUhUfqOU6yn9ti-YJO1VD8419PYXQZX33acs4h58HpWPUz0nLf7bR8XkjaEpcgsOMg0jqUbJTB3uLtC_LcGzLI0lj6OrF9ebtfUxaDBVBsE-KlgE8FAFffj7MMi8dYbOVBn8GdlCrO9I43BI1ge7Vr73fdCc972GcQFgZXsZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23988" target="_blank">📅 16:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23987">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlUB8-_eUSUexcXN1MZqcxHBsDAV6XHQNTfHDjUTkUIQvOMMarHp7Ichp-TItAolCm5-2T2O6H3i0vmWtLnOHa4f6_4zFF5G634hNJ9li2j6gawc6Y7RaYqVWGildMQ4b8b6HLpYcawj32sb8OkxREdYvW8x0vLLV9uNk4tkqkAoAG0x_h3l8ur5vNzcCkLFWPnNbRt4SwSvegyVzO2mMaCN-rdqJaU_1fD74gu27qiaMA3FwSoCMhL5wlLit2ntf44xaCGRnc0TN0oJq76Dz99_DrZcmoKPY-wFD9XVINZBRh9pc60zyU7h7F5n-O-kxkpRU53d2h85BFGeMmmkSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌قدیمی کوکوریا در سال 2019: حاضرم موهام رو که علاقه زیادی بهشون دارم از ته بزنم ولی هیچوقت تحت هیچ شرایطی به رئال مادرید نروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23987" target="_blank">📅 15:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23986">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8dba54f8d.mp4?token=cmlcuLC_iHYCqcrdF2xftIEeJVKrJOhbP3QgtDJnCpXAfVntniwudQjFgd2jHFdrwb6FBHw8-6FkV_odrUX1_7IJV2wPbhhnG-FeBw181pOr2SgMV26DBnn5YZSlPRzK987rJXB4ykFtHPW412dOBAqDNgXQTX9Pb_Nshbhx_LLnAs3Rk0Vh7c3RmQQXZfQzF-wkRKPjVGz6UnbYAIgPBn2uJmlvUo1BK5NQIlUbLppdMratOTc-1jMzypN3kvnIR5JiB4hAwTRsF6qhYOFGUSeFzuXybiLDLHrorGA9wUcFNuIxScCw9-EzAiq6mcnI778FlesCLFTdbVAKB2SqfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8dba54f8d.mp4?token=cmlcuLC_iHYCqcrdF2xftIEeJVKrJOhbP3QgtDJnCpXAfVntniwudQjFgd2jHFdrwb6FBHw8-6FkV_odrUX1_7IJV2wPbhhnG-FeBw181pOr2SgMV26DBnn5YZSlPRzK987rJXB4ykFtHPW412dOBAqDNgXQTX9Pb_Nshbhx_LLnAs3Rk0Vh7c3RmQQXZfQzF-wkRKPjVGz6UnbYAIgPBn2uJmlvUo1BK5NQIlUbLppdMratOTc-1jMzypN3kvnIR5JiB4hAwTRsF6qhYOFGUSeFzuXybiLDLHrorGA9wUcFNuIxScCw9-EzAiq6mcnI778FlesCLFTdbVAKB2SqfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر: از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23986" target="_blank">📅 15:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23985">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwXUM3v5UIutk5Qdkhj8pSC03YJ-ORUfzJNxLjbMzLHDY0usFasmP3KKGdzur0_sJ_8XR4dUFEZaUA0qiq1HwSLUpNvQkBe1XjDsjz04Y20XT2YFBGv7_nu3SWyw4NkrZ0ja04yioS-XhOBdKEbI1TTv4Yku5PIyd-PT5OWNCqCx46Ujjf0kQ7ZTVwCNFgopSKqyTjMSM4DGuY8ssg9dMKBV3yGqo18vVl4U-BNeiBdhXEREUu0S2lQyQL7vOpD0EsYeymtsWLzsBpnAragSZe81oMOftzvuIfUdTLezsPdQiFJGT-sKkXpF0c3pJyWgnu-BSV7O8pTIGV_PgTliFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ آتش بازی سامورائی ها مقابل شاگردان هروه رنار + جدول رده بندی گروه F در پایان هفته دوم رقابت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23985" target="_blank">📅 15:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23984">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e6bc8b00.mp4?token=tGxZfZMFA3MBYo2e35YEt826jO82nSYUgKQdlFGkWASJ9FVsMphI5mXZyW02JZZymKXHrRtbN1x67w8fvY0aoh8oqFBhjiDf9gJ87tzdQPrGj5POhVeQ0YSuUE_07oP9S0cH81cqXYEQA5QCOUaSIG2eOb_OkBwMMLKf2-tScYMTeeCr3lvvvLZuv4M6LmipN9KFwH_kBNJ_Sa3z6tZXbwASGpFVrjkzs0vYy28rL8atLfezJSLspQCbNVt94j-2CmIMqWuRwOV9CZHw5KEo3khIfAc1YCJGo6-R3vZV2cU3cjFg6BuoZJ__w35TFbMJ_nQTe_s245puRxcA2mRPAbapX0JFGSEqPUvRLvB6_f0mTdIDZ2w5PB5U2K7w6VCbGUmX5EMAHHuQEz0zpsp5EFMQF0DBEmyPKXaXKUe6Ob6DPlyl1i6ewba_QIN8sFDGJwXaMkGJTUwAt5BjQ0a9JWukXxNvpSQOU2GkyJ9pPOHGDfwSBeqQGSlobkvsEAdhQeMVZh87Z8PAPHM09mK_WfvpNfIyT00y16r19vGlu_iW97zU0SYJXqPlkkShtlhhchqXnfzA-3uSUyjJ-U3VqUFgKi-D2vMnnIk2P82MG723VCbb4Pxnm5_fc0_6ay2TMe21qE8JU4s_KgQG1GNW8f2KN6lz-iGPqBSvElgXluU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e6bc8b00.mp4?token=tGxZfZMFA3MBYo2e35YEt826jO82nSYUgKQdlFGkWASJ9FVsMphI5mXZyW02JZZymKXHrRtbN1x67w8fvY0aoh8oqFBhjiDf9gJ87tzdQPrGj5POhVeQ0YSuUE_07oP9S0cH81cqXYEQA5QCOUaSIG2eOb_OkBwMMLKf2-tScYMTeeCr3lvvvLZuv4M6LmipN9KFwH_kBNJ_Sa3z6tZXbwASGpFVrjkzs0vYy28rL8atLfezJSLspQCbNVt94j-2CmIMqWuRwOV9CZHw5KEo3khIfAc1YCJGo6-R3vZV2cU3cjFg6BuoZJ__w35TFbMJ_nQTe_s245puRxcA2mRPAbapX0JFGSEqPUvRLvB6_f0mTdIDZ2w5PB5U2K7w6VCbGUmX5EMAHHuQEz0zpsp5EFMQF0DBEmyPKXaXKUe6Ob6DPlyl1i6ewba_QIN8sFDGJwXaMkGJTUwAt5BjQ0a9JWukXxNvpSQOU2GkyJ9pPOHGDfwSBeqQGSlobkvsEAdhQeMVZh87Z8PAPHM09mK_WfvpNfIyT00y16r19vGlu_iW97zU0SYJXqPlkkShtlhhchqXnfzA-3uSUyjJ-U3VqUFgKi-D2vMnnIk2P82MG723VCbb4Pxnm5_fc0_6ay2TMe21qE8JU4s_KgQG1GNW8f2KN6lz-iGPqBSvElgXluU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرمصدوم‌شدن‌کورتوا کذب‌محضه‌اسکای اسپورت همچین‌خبری روکارنکرده ولی باتوجه به فعالیت‌های دعانویس ژنرال‌ممکنه‌یک‌ساعت دیگه خبر بیا کورتوا و دیبروینه سر صبحونه کینه های قدیمی رو دوباره کشیدن وسط و سر دختر دعواشون شد و گارسیا به دلیل‌مسائل اخلاقی‌اونارو ازبازی‌کنار گذاشت. ویدیو بازکنید متوجه منظورمون از کینه قدیمی میشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23984" target="_blank">📅 15:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23983">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc33af7706.mp4?token=mz5F6Xjwf7bsltWeB1zbx-XwdisVxbLGayVrpJgpPESIluARmc8gLeCGuQeOFQRr8NFTnZ1TQh9Oqf4mAUpqUr54lCMh3nk-Km6BWN6czLREyiG9owtNlzWoV0_alqNVBfp7H3prxbKnmh_2mEFj1nhY_EvucQohAZLW1RkMYzoaivjZ7oT__fryazWOhUwIVTbF869LbZFuHz-2wOz9NeKccqcLN_IYmhi5cHSGxZRlgTjTiPUDKMIgRzBRv08bYtG2RsdxgFqHfimP5Y-Ygsn8MxiZyOyzLvHydnSeRvCF9np1__uX0Qrz8al5E3JTTiVQeO2Evnirm8obX8xzTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc33af7706.mp4?token=mz5F6Xjwf7bsltWeB1zbx-XwdisVxbLGayVrpJgpPESIluARmc8gLeCGuQeOFQRr8NFTnZ1TQh9Oqf4mAUpqUr54lCMh3nk-Km6BWN6czLREyiG9owtNlzWoV0_alqNVBfp7H3prxbKnmh_2mEFj1nhY_EvucQohAZLW1RkMYzoaivjZ7oT__fryazWOhUwIVTbF869LbZFuHz-2wOz9NeKccqcLN_IYmhi5cHSGxZRlgTjTiPUDKMIgRzBRv08bYtG2RsdxgFqHfimP5Y-Ygsn8MxiZyOyzLvHydnSeRvCF9np1__uX0Qrz8al5E3JTTiVQeO2Evnirm8obX8xzTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
#نقل‌انتقالات|اسماعیل‌ سایبری هافبک تهاجمی جوان مراکش‌باعقدقراردادی 5 ساله به بایرن مونیخ پیوست. هزینه انتقال 55 میلیون یورو اعلام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23983" target="_blank">📅 15:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23982">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eba240be.mp4?token=uHiwawvDJ_EElxig8QcA8hf8R8hW6Sfy2uqstvvegs0b0XS5nXR-aNzc5Sao9xDBao1kEmfiyUgN-zafuWIV54FXkbuBR2QrHtsOxVGX4M35FPTn5QSJ9PcP0QVABcxpzNa6WTC64kdkMRBW0Mpnt3PCfyz6hFNudwAt8Qq-I6nToEAgY2bwfAXHiHKT0Pr5bH4oxE20vCq8E6V_FeJndERGSh1B2rE0QalIwmLyOlqtjquGFfxl9J1Z70ssQV76PmrU0yPPLLbDljOPpqpKhYMS2Q5j8ZWGlCRv4jUxU_GpE-b3AFFStpIxEFy9Jd_4saArjnFhXHAAaGfhqf2LDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eba240be.mp4?token=uHiwawvDJ_EElxig8QcA8hf8R8hW6Sfy2uqstvvegs0b0XS5nXR-aNzc5Sao9xDBao1kEmfiyUgN-zafuWIV54FXkbuBR2QrHtsOxVGX4M35FPTn5QSJ9PcP0QVABcxpzNa6WTC64kdkMRBW0Mpnt3PCfyz6hFNudwAt8Qq-I6nToEAgY2bwfAXHiHKT0Pr5bH4oxE20vCq8E6V_FeJndERGSh1B2rE0QalIwmLyOlqtjquGFfxl9J1Z70ssQV76PmrU0yPPLLbDljOPpqpKhYMS2Q5j8ZWGlCRv4jUxU_GpE-b3AFFStpIxEFy9Jd_4saArjnFhXHAAaGfhqf2LDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
50 ثانیه از دیوانه کردن خداداد عزیزی توسط جواد خیابانی در ویژه‌برنامه‌روزای‌اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23982" target="_blank">📅 14:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23981">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHkMKSUOgbAhcF5BDomPPla0TYZSGJLkZEHRFQv00I5FU7oW7qHtfu7af1C2lgbd7ZYwf9laVOGtJYMimjDKay4hA-cvj5K_v9c_mkeCBwOsMTzlyg6pEr3wMOZoVGUpbO1Lxs4ikDg91XU0Ac-5qc5mI__9fkx8oMSunPL7UU3LeG_A1A9MOxeuxK2gSAgRpLWcfm2OpCkdx0vY5909VJsUOtdCQwdZeOnb9BVwHuE49LwtvwVDfhVI5vBNhf7p2DlEAzYzDlpiFfPUquABL7ACcyN5BzXDhvpurir3X76HBKE1O8BifX08Uxr4j9UbAu9bRzOu8gIhomN4CVy_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌ بختیاری‌زاده سرمربی جدید استقلال امروز صبح باحضور در ساختمان این باشگاه قراردادش رو با آبی پوشان پایتخت به مدت دو فصل امضاکرد. بختیاری‌زاده‌درباره تقویت کادرفنی و جذب بازیکنان مدنظر نیز گفتگویی مفصل با تاجرنیا داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23981" target="_blank">📅 14:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23980">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWOb6UuVuwYWB_yxjwCHtwmNCRzCSBJbxIpcceU_Gurfx_LCq32eu6M3EyQ0_T7YFdokDhIlDo0SW48q84oYR9rE0xggMWgrKh59Yfev67GBe7vB0X4rUlCkmL36WajQipboGLm095TOHE41WXZMa91wf-STagd0tJeFQNfpzkEPuTqcR_jv8g1jG_g-HCmj6_TojroVSxiGbjC1MeCO6R60jLZCG8-_bn5LzZiZFpFNDiDhz5NV5W_6N-p1AS9KH5w9MJ2CMEnvUoLFQ98KGiiwJJd9e8aBKfrryePUhUWaPr8C9seacbWxU0NSagrkIvN99kpkoppakrH1hoKZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ تاجرنیا امروز صبح در تماس با سهراب بختیاری زاده سرمربی جدید استقلال گفته درصورت موافقت او سریعا با گابریل پین قرارداد امضا خواهد کرد. بختیاری‌زاده علاقمند به مربیان ترکیه‌ای است و احتمال داره دستیار دومش هم اهل این کشور باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23980" target="_blank">📅 14:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23979">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqE_IHl7mRaE-VJPFKFy6NnO8Fvdupq97HXFJWTL7iWUzxxTUfpckUwiaafOEQm9Hc2ArpvxhmeCv5JlNWzOyaWL17NUUgbIxQZzdzKd17cURBXftOv65IXLnoxgQC_AvbJ3sGg08Yo0iK3GjPLkf6k0305OffjzIoTUx3c19stJ4Bv53KZ2icPzzAWursZZRb3UPRvsbIBU_jEGtuZ0m74WjED8yrEjJklsZ-aLUVncdKW6QOvVt-D2xaddmcM7F03QLICBAKwqcKwuco6rR_LPeRGxgMH97ApQDYOX4AK2rN084TkHma-W2Pr1lzacJFMzGcl6-qzojurav9mEzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23979" target="_blank">📅 14:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23978">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=JUYwX4fROf47DjDGwNAulB44wqvTHF64eSvwbbMSJrh7sMzUKblgz7SM--20rk8dDidKyxZsm3YARYkk7irOKJfkuMjTwDl7xSNMVd9KnyZrbm32p0gmxeqMKP4q2ovVAR0ukIbSvljzVkLXStP2zf8p4a5NUD1gTsqWDmcO6G4iEiNpnHV4EnSoF1_-qQ6q6WyHJHGWt6Q-bb7uXBNvwrI6bdbT_FrGxvlRjadpDKyQ9Ec_taVQXYHh1Rh5wAroXdUB9f7oVPMvyXyxrRelh5xDXMnhdhEk09byPtRNX6XJd3gBF7oyotnZ4-gk-ZxLFtrQeKN6C-Q1KXmjIO41Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=JUYwX4fROf47DjDGwNAulB44wqvTHF64eSvwbbMSJrh7sMzUKblgz7SM--20rk8dDidKyxZsm3YARYkk7irOKJfkuMjTwDl7xSNMVd9KnyZrbm32p0gmxeqMKP4q2ovVAR0ukIbSvljzVkLXStP2zf8p4a5NUD1gTsqWDmcO6G4iEiNpnHV4EnSoF1_-qQ6q6WyHJHGWt6Q-bb7uXBNvwrI6bdbT_FrGxvlRjadpDKyQ9Ec_taVQXYHh1Rh5wAroXdUB9f7oVPMvyXyxrRelh5xDXMnhdhEk09byPtRNX6XJd3gBF7oyotnZ4-gk-ZxLFtrQeKN6C-Q1KXmjIO41Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
هاجیمه موریاسو سرمربی تیم ملی ژاپن با دیدن هری کین کاپیتان تیم ملی انگلیس فورا تبدیل به یکی از هواداراش میشه و باهاش سلفی میگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23978" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23977">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMMUvWfuK5W1DSKfwlNNUqE3_GhIfCxIqN2eZ5UIJRUPRLxJvqKjFxHwgRcYkYU2CsigpsVcU4K3GXFeIi6UbgAXoJmcH8iEyW3VsIemO-6DbFogshsm4cbCNE-TBaFtNziQJlfb5pf9xZ27rDy3__2hA7mvll3ji16Osu_qtWvJwVEYOwG8U4UZJqdZWyLn9zs07Hrsj2rhCvgyEwnCu6UR6eU-CQxqkENj-uY_B7dZAGRFVUNa9Uqhj-ma_GDsO9WLsRriiBXEdU4iBAfs2AODfhoCDgh3GDETcPFiIMr19hZkpJ3s-my3RHTM8ZQUONbOD7Pp1DD6chjX-S3VlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه‌رسمی‌تیم‌ملی‌بلژیک: آقای قلعه نویی عزیز دعانویست‌رو از تیم بکش‌بیرون‌. ما اصلا با شما بازی نمیکنیم سه امتیاز بازی‌برای‌شما. تک تک بازیکنانمون رو به دلیل مصدومیت داریم از دست میدیم.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23977" target="_blank">📅 13:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23976">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFn1Lj2a6PUjpptVMGLALPWsIrdk1BVGcPEA44qoJg_s0uwdXJkrezqOHpXLO90RhQAs_RaaFydM016_zeSkxClTE5th_vyNL4G8sJtE9lCz6VwqXmuOdOM9CVJy6XDFo1Zz29Qw6zWVGZjxTpUCmlVmltwMwduvge1ElKFdGEwrcq5ohIyGMj9EvGZvcJlvl_ws0b00si-jqK9lz8f2TtsyFfwH7w7nAZOFRgX9FPMbvpzPHqb7y1KvZEIuF3G5Q0Rw51ZV-lyQQY_b2bVe3GE7tOjMZMu2OKMJxEBYUsmGEhRjb9kb-LvLmrNwIP8nlFmfWJn8pN6VSDwPduoczg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ مگه‌میشه؟! رسانه‌معتبر اسپورت بلژیک گفته لئاندرو ترسارد ازناحیه‌کتف‌احساس دردمیکنه و ممکنه دربازی‌امشب‌مقابل ایران فیکس به میدان نره. پزشکان بلژیک در تلاشن او رو به این بازی برسونند. تروسارد جانشین جرمی دوکو مصدوم شده بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23976" target="_blank">📅 13:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23975">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFfXhjpW8UJvnmcndk2SPeHe6n2tj7ptfiTOfo2bpsXKsiWbdHmjmZAWwH8VCtF4Bb0VNOr2vHS3t6lSDVmV-5X2YR6EIxGD_qhvBQBlHSYdM0iab_eTYtWpHqCEk20YVoeVry3WTJM-DtavxpfSAKK3xyKws2uc9nQtAgTybvKKx1ATv5O8n5BE1Uornd6e1x3Vi8q6PMuNk5gBNOajWVoUKPVtKfhW8EicGHlkuD3BpELzWkawpgoHQVl1dyiKNx74GAqDOdO0FjQHm25nPIJvJ59O8lPhwjtzdi_wmFH599E02xl5gg2dD4ITzOIK9O-TTClZg85ALOOwUk87rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌پرشیاناازباشگاه پرسپولیس؛ امروز ساعت 14:00 جلسه نهایی مدیر عامل باشگاه پرسپولیس بادراگان‌اسکوچیچ و نماینده‌اش در ترکیه برگزار خواهد شد. باتوجه به مذاکرات مثبت روزهای اخیر انتظار میرود امروز قرارداد رسمی بین طرفین امضا شود و اسکوچیچ بزودی راهی…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23975" target="_blank">📅 13:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23974">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRlgHU7ljJSKW8dGDInninAvfipYBvnJQ-G0s6V0brYlZTz23VMMQfjpwgBZtqSBHq93ALZizWg4rKsfE_bqu7wtbG_dfJIsbveMBSi_9R50ro_h8dga6YjmTIm02fpYPRtLQc6vToTGt-G_E9w-onoznem6EAY9vhmmZ8_5T3aSupFghfDpQhVc_5by0-MfoOfvW9qgNfb5M0WKT6MZ9UbXm1h1IIq5w76DAARA5vCKTJXRzjOT0yg6XL653G__fTt-asjHkPFmlySCgaROe5DywmWs8lSR_Fqxc3UVolOYvbEeF12vWbgYtKq_R0NCSABdC-LcLAD9l2RpjfRBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانا؛ با اعلام فدراسیون فوتبال رقابت‌های‌فصل‌اینده‌لیگ‌برتر 18 تیمی خواهد بود. هیچ تیمی سقوط نخواهد کرد و دو تیم از لیگ ازادگان نیز به رقابت های لیگ برتر خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23974" target="_blank">📅 13:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23973">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=cGc-_yQKBfoYCEyHWuRtRTN4-eQ3NzA4tsQN5vJH_hSMBDR5jMjUp_8qbHWq197SgD-VCbjLC7PF6rKsAy5S15HYwVRQd1mbA-QLIUVXzHqLNEDHM6X4DcwaziSn8cQFU0cvO8jru-k4TV_3Krlj621O_-yYw3l-pZOJrgGM2eERPnbHedw1ke9ZA3Oz_dM70Vt-aX3NgIeN8hudZESg6vkeTu6AvdEUOntrbIEOAFbg8H-sKX2UZpz_CXmY_0y27WN47naegu_vZl-BBztp17ziRgM2EXEhO_2byLwbG_Se3ziod2tKkHMo2g3wdD_FJm9ioE_eXEB3DQiR27dIOqd6XP45GCoD1jF5fdIq9jRyo60AbFBDU0qVwwOFftpORLA5Gz2aP6vwGLd6CrXNHx1bOcAkZy6anMLbzJYxVQ0ZjtUhlWBsuQmr1ByBgTKC3XKN1PJRiOIzcIOQrdoqJ_I6j2W-G3se-e9cp2dd3V2PELdfn48LP79ihs-dzTOFktIK5r9S0QdhhdF7A6eXvFwBddokbXdl5c4kwVh-IjUy_8xKGDj5eJh80_92xS8d8LMt0HXr44jyeC_360XHugDuoHpfJdG51WWvxp-5XRtA1mCP6z_OFt6cpUOG03TxI2RBvkoeJpaooq95aIp2GD-CWmOOvDYVvawB3excTQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=cGc-_yQKBfoYCEyHWuRtRTN4-eQ3NzA4tsQN5vJH_hSMBDR5jMjUp_8qbHWq197SgD-VCbjLC7PF6rKsAy5S15HYwVRQd1mbA-QLIUVXzHqLNEDHM6X4DcwaziSn8cQFU0cvO8jru-k4TV_3Krlj621O_-yYw3l-pZOJrgGM2eERPnbHedw1ke9ZA3Oz_dM70Vt-aX3NgIeN8hudZESg6vkeTu6AvdEUOntrbIEOAFbg8H-sKX2UZpz_CXmY_0y27WN47naegu_vZl-BBztp17ziRgM2EXEhO_2byLwbG_Se3ziod2tKkHMo2g3wdD_FJm9ioE_eXEB3DQiR27dIOqd6XP45GCoD1jF5fdIq9jRyo60AbFBDU0qVwwOFftpORLA5Gz2aP6vwGLd6CrXNHx1bOcAkZy6anMLbzJYxVQ0ZjtUhlWBsuQmr1ByBgTKC3XKN1PJRiOIzcIOQrdoqJ_I6j2W-G3se-e9cp2dd3V2PELdfn48LP79ihs-dzTOFktIK5r9S0QdhhdF7A6eXvFwBddokbXdl5c4kwVh-IjUy_8xKGDj5eJh80_92xS8d8LMt0HXr44jyeC_360XHugDuoHpfJdG51WWvxp-5XRtA1mCP6z_OFt6cpUOG03TxI2RBvkoeJpaooq95aIp2GD-CWmOOvDYVvawB3excTQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ماجرای جالب آشنا شدن اوسمار ویرا سرمربی فعلی سرخ‌ها باسنگربان برزیل‌ و لیورپول؛
پسربچه هفت‌ساله‌وتپلی‌که حالا یکی از بهترین‌های دنیا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23973" target="_blank">📅 12:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23972">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz8Dvqui0IttVrZDw0wXHvDr56yYMlECUk5tbAIMCVhGmVD6OxjXNXFT8CCv_wPrImAxuRbv8ayrBEyon3Xpf-xXOceyCssXtACmVlnHYrnwcVJALMICdiVbz8uGjuafUUl_UI9NsVzm7cLc4a_l1ZDdd0RbaO3fWJKEN2p8-5YnuL0jbZXcr4vDaaM3NYYQW-0LnQI5JHJMlZbsrP-c3uNV9LtIXf2rQuFAUaqF_EA0apDyDZkJm6zQgkeB-ZEJ8QQODkzWcAs1SgxOTCdknBfyixO_YRCrFiZlB9lOs103ItK0dBr1u1LOZ3ToOhVDMox6Ju1GeYwLFsvszSKdTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکوردداران‌کمترین‌درصد مالکیت توپ در یک بازی جام جهانی؛
پاراگوئه با مالکیت ۲۱ درصدی در بازی با ترکیه، در رده هفتم کمترین میزان مالکیت توپ در یک بازی جام جهانی قرار گرفت.
‼️
ایران با ۳ بازی، تنها تیمیه که بیش از یک بار در جدول کمترین میزان مالکیت توپ قرار گرفته است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23972" target="_blank">📅 12:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23971">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHGCv0BfwOiNL_FYV8isoeH1bczPn51Kx1yxm54Wx0mgyydwCSM8DxEGb0G4yDdbt-KniE16Gr1fH7RzCdRVspqOTs1TdLbkm-cKe1kOqCKQaU39SwscQwDNPrIVJhCZJKbKxm3RGy1_gQdwo_Jcnni25jsSftJkfOlGD9wm2sFllJysQZ3dG6qi-RUQenLR3QELS67A1r4mcA6EB5UWUW6w7Zw3vLe2duiDqPJ0oBN058x5Rh3iTVXfjxZzup4L1jrX7QUA1Ek5tPO0mlW4-dhtdZyBmeSOxcasNbsk5vYNZPzrF54g1Zdg1K736NkcV487thlSqLA28S542CxRdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
فوق‌ستاره‌های‌فوتبال‌جهان بابیشترین تعداد فالور در اینستاگرام؛ کریس رونالدو با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23971" target="_blank">📅 12:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23970">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndzJwHO0IMVIJWk3cJJc9SgpVBRAcaIYS0tNBw83dpQarjKij4POnkylqeIrQnMKZzWxYTiJR92yZB-bFoyX_qmplrh2zNe0cq-l4k-25QxZh7H2vgns0yCnbz4Q5xROPJlMlzJZPpdIjq7_-lIp5erEEw7z6uoVY1zur8bz3lozdmU9EhcCWAyq2aVV1YG5cfEfBAffId4cGAFZK0TxAidu1uylZuqKNRG37DtrXW0J_rYtmiFNdJ0CFtLdxGJrctwQpM5pPPQpstCyv7xAevMOeKFsfSodRDFRtZf0YpwucqnO-SpsCW9bsa2QpAJ2Zk-zg4pD0SzOCbIkQlwwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23970" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23969">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d78439566.mp4?token=kQlzqfWIIS5-2cJU35_Kj-i23jnNPyN1XvFsMXmr0DY0vNJuCdRtHNV30rKmHo43VOEBqb9U-yBNI1VnM0x05E7KS1xyYzFr-2EtvHeWiyrFC988jFlEFTK2TRn8JIbQImmGNVK7m8bF0kny2A2gvBvxvLLDI-Ny5tiGtvd0zpNLHSR5kNxqgdqpwjZ0OcDz_g3JtxIRMh7zyTrolaUF9bDas-5Hf48wt4b4gTm7KOSbZcH4xMqHqudASt9JWQevNwIUwQoc15-1uYlcUD2Orpzx8A8K3mtAQY6GS_UDqcQ3yML66yE6PTE95htEO7HGfaWvAXYGwPUgm93pMPJEEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d78439566.mp4?token=kQlzqfWIIS5-2cJU35_Kj-i23jnNPyN1XvFsMXmr0DY0vNJuCdRtHNV30rKmHo43VOEBqb9U-yBNI1VnM0x05E7KS1xyYzFr-2EtvHeWiyrFC988jFlEFTK2TRn8JIbQImmGNVK7m8bF0kny2A2gvBvxvLLDI-Ny5tiGtvd0zpNLHSR5kNxqgdqpwjZ0OcDz_g3JtxIRMh7zyTrolaUF9bDas-5Hf48wt4b4gTm7KOSbZcH4xMqHqudASt9JWQevNwIUwQoc15-1uYlcUD2Orpzx8A8K3mtAQY6GS_UDqcQ3yML66yE6PTE95htEO7HGfaWvAXYGwPUgm93pMPJEEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇪
بااعلام‌‌رسانه‌های‌بلژیکی‌؛روملو لوکاکو دیگر ستاره خط حمله تیم ملی بلژیک به دلیل مصدومیت جزئی در بازی‌ امشب‌مقابل تیم ایران فیکس نخواهد بود و احتمالا این مسابقه رو از دست خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23969" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23968">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
رکوردجهان توسط یک مرد اهل جزیره کوچک کم جمعیت‌در دریای‌کارائیب‌شکسته شد
؛ الوی روم دروازه بان 37 ساله کوراسائو در بازی دیشب مقابل اکوادور موفق‌به‌ثبت 15 سیو شد و رکورد بیشترین سیو در 90 دقیقه‌یک بازی جام جهانی رو شکست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23968" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23967">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c204841a.mp4?token=vW1jkPYKxXfc-ax2FYo_ig58tPSOXAor8RspbjJhi1g_f0pdvoopZBCdqKlzq_3UPvM_DkV2FX7EAdSi02eTo8Z5ptmqPwVQdNh-3x6rADEgorx0Opv-qBweIfDkL2_n8rUrrsADPp4e5QA6OCXgPV7an0PUVwr_S8qG2NsuUVX-Hd1j7TjLFopk8I_Pv05ccwNFFAwE2yg7252Lzdg9Dfj7-BG7qch_Cl0T3KL7djTuocSYA0UPeuYW0CL8huOgOkeff-TfyPFG5Po8IPOttCsDWHS350T9_Sn-2M17ay-aiMrcRJFQmf9H7LzfrJ0pgLFQlleVOhvZAZ_48MhEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c204841a.mp4?token=vW1jkPYKxXfc-ax2FYo_ig58tPSOXAor8RspbjJhi1g_f0pdvoopZBCdqKlzq_3UPvM_DkV2FX7EAdSi02eTo8Z5ptmqPwVQdNh-3x6rADEgorx0Opv-qBweIfDkL2_n8rUrrsADPp4e5QA6OCXgPV7an0PUVwr_S8qG2NsuUVX-Hd1j7TjLFopk8I_Pv05ccwNFFAwE2yg7252Lzdg9Dfj7-BG7qch_Cl0T3KL7djTuocSYA0UPeuYW0CL8huOgOkeff-TfyPFG5Po8IPOttCsDWHS350T9_Sn-2M17ay-aiMrcRJFQmf9H7LzfrJ0pgLFQlleVOhvZAZ_48MhEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فیروزکریمی‌کارشناس‌ویژه برنامه جام جهانی:
خانم‌های ایرانی می‌توانند داور بشوند. حامی بانوان هستم‌. داوری بانوان از رانندگیشون خیلی بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23967" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23965">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbQ7Y51_Shzln3hh7jHOJIaB9pqZS0qH4GqEB5b9iJo19AgLaUg6l6sAz9OR1RC6wBF6DnJwZvK_87Z34WPIbCpg-A-AL4w3WaxORnOLzTZlUd6Tv0QtSqAEcEp5GwoYEAJ-2BsG6X5QupWPxOfLHWXg0gZcBHB6NXNrTguptEscFNzp2GSMgIVqkOyi1wMzmD33eNRzC9kZ_6UOVsUcgXYbM7FZy1nQZG3C1IVzCptv3flt8vYrjFwnwBlsMRf3YiwVs_040hWWlVKkoEq-dGqvwt3oi0JQPs_Nt-K56YZQmUzY9VxIHF4hnHKGYQ2SeLvoXlPxmhiUgnVxtYzESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
طبق ادعای رسانه‌های بلژیکی؛ گویا روملو لوکاکو ستاره تیم ملی بلژیک نیز دیدار امشب مقابل ایران رو به دلیل مصدومیت جزئی از دست داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23965" target="_blank">📅 11:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23964">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIRTbxp-8A62xBxG5G8jOqsH6wAn3FBzh5ZJWwcw4rnoPueEwlmmKym7mHrcvQ8a2jdBFSRikXWITUtXJ7WrFC95og9dgk8gjEZxWhSZv2BuyIUbyBG-fM9Gm5eWe1ly31XPT7Vxq208gXCfzGlJhNA_9vZzxOnMaTnc1c03XW4_w0i0_2YU1yzlJDNT2v1X1T9zrIjDdoqqNHXBQ_uFecVK07aqTscl23bf80yJIwePC1cLXF9WfB8n9xtL3sfB1zrBkscPwuUXupnJxxcHggIDJhs9kaOQW99ySEpkGsZLfZ7sK42P43XoqYkfwEqcA0TTsG-5kK0BIFGRr-JHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23964" target="_blank">📅 11:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23963">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQfPStAKWjEGuZoqmQvdkpRvpgNBJYKEb_X-mHIPHGZM0vXKDxqYyEmS0stEVZq7dLinIKP6EXLnbwWh2pNgBr5MXoaQO3TiiOYGiAp_FWW8LjOEc--FNtwVpeQvauwAQufREJ4VeWOS89UmGhFov9UqyG7e-7Aem2vfiABjQTec948V3axXYX5v7wcnrvmEQ351u54OcMZMbjIHsfAIkNh5ubqQaihqHjwPGlpDoAcWwaHqnnUGYiPqlrajcGjdPCOz0FUfzvdCJQHwZRiSGW8EmE_GUvvXK0rB9rouEVZgbsN2M5UgVeqvLZMIAOp5JlUC3YfX3czNAsjuFFdtAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛باشگاه استقلال امروز با وکیل‌ایتالیایی‌خود تماس گرفته که این وکیل به باشگاه اعلام‌کرده‌است که نهایتا تا پایان هفته اینده فیفا پنجره نقل و انتقالاتی آبی‌ها رو باز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23963" target="_blank">📅 10:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23962">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BupidrEQzLMtYZiDJyx95FZvyiiH33WYHTXEXEy4oLRT6kTDoIZJP0xEV6kIhKgDXYB73vctWLXUl4dMkAbsxp77htnRILXVlskJ5HvRe8ckpSqUwtCgr4vrSioSm0y4cLGRj_Pm-Q9r2v5d8bOWUmC3hTwECLMqPcxWGmsgZv32y6BVPe_FHLB1fngjmd-LbetYa-uMluN5e7yYZo1_-NybOwAOCtxTRLLnuckn6JmbQONRffHYdD_-1U8eVu1ntI-QmSv-VpPSSn27Oz-pZuLFPcGYMemgAaYjYb6suSTxMaNCyiigWe-r8T_x_3_jq7llzMISRp1VjK4WDAGp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پرچم‌باشگاه استقلال تهران درحاشیه بازی امشب دو تیم آلمان
🆚
ساحل عاج در جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23962" target="_blank">📅 10:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23961">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTETgK6vhzEtTsI1PtaqMUBdUkhyPC6BfuGZ48mh3cU74EesbwsS9BG6L0PQH4eMIKdY85y0LmdbRzYYhwZRf7LMACNbOg30xHZR2svQhDmZ9skg9YPY3nB3iLWtm2mIwIk4MWm-xa3r6fUAOc9rfPNzZfflyvLpyHSlBAN0MtipTCDKpQKEjY_Iy8Gs6fDjE--3Bf15EBnAFDrr4VVrwA4_3Zi3pvq5iHay2hu1X-WvM3kAMWkC1NV6hwPtRz_uuljtYioHDChjrPCOa6uIRWgY50-_tCOepazqr54BG98-PU6eTGfgnW52ua_sr1WgqEe5fMZv-1vjn9_u-7D0WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آمار پیروزی تیم‌های‌ملی‌آسیایی درادوار مختلف رقابت های جام جهانی؛ کره جنوبی فعلا در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23961" target="_blank">📅 10:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23959">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=SH3pKCL8v_TTKAQ1BI4pq29opRAiQj7GZrhgzTNRPwu7IiRGeePzLNJDUd5sYX3maKpNh0DKo9RKFHw_GLIiyxUNmN46r93h56WbJn5vS_HXZgXk3cKE2r9zCBNMjdp0fNXSI5GVABKkMAvRnckx9LdHJ1kcgJHuSyN6jy2vUhqkxN0vkfMlhLqKfHQ7GidpDFKPhqqKBQ7kj9REErGTGHhNjsXw66_1zJMn9kCSl01-wRUsH33gTzJH8gkIR5gzr32rQVoXQZn_tOw8vMVGpGml9AFZRYJY3r4ut0cI1pqdkaOqlE0nh56ALqPeOo6dnnqOM8ggZ6qPkjRjYXSpCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=SH3pKCL8v_TTKAQ1BI4pq29opRAiQj7GZrhgzTNRPwu7IiRGeePzLNJDUd5sYX3maKpNh0DKo9RKFHw_GLIiyxUNmN46r93h56WbJn5vS_HXZgXk3cKE2r9zCBNMjdp0fNXSI5GVABKkMAvRnckx9LdHJ1kcgJHuSyN6jy2vUhqkxN0vkfMlhLqKfHQ7GidpDFKPhqqKBQ7kj9REErGTGHhNjsXw66_1zJMn9kCSl01-wRUsH33gTzJH8gkIR5gzr32rQVoXQZn_tOw8vMVGpGml9AFZRYJY3r4ut0cI1pqdkaOqlE0nh56ALqPeOo6dnnqOM8ggZ6qPkjRjYXSpCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر:
از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23959" target="_blank">📅 10:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23957">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0oyWdsq3EHCRWCGwYIDfe3hhG7EbDH-7sCM0P6lSYw3tBir2OpHIbvyrJfQf2gu3UgTSkuZwrciHymqEUSkKz7dB6cKF09eEHLeaSKOzzugRCNePmn6cQnMfKpAGnVBB8LkK6XFMKlzdM1b87sIZxdpoK9SLjmTdrDjs6P9QPKDxXzNBuP68cy8TnCcboUVqf25-xYpPSzIA5PtGiJQsH5cXHAmAUT0BCBR4PIxtZVf2gi9rugNVX_xBVoBFOKaKzTxN-9iTXFNn6jX7BxLZ7uinwRvpESd6XVmVMRr_r2BHqjxIqqv5lLi1t7V7j__F7yFeM3OJKc1RPX6OB1Bfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/On9vrP7iu0FYTAY5ETWxI0S6lSUVDh-fRFhyMnJw8MP5xgL-aaJs6s6TFMCZE7WCbeYtMk3n1nnq417BKe2JX33UIPxCVuYBX-f-BZcw77U7nVQQlvHcSCwcg-G62PHdjOZczYNrvLuATQre9xVsB2XpyZbAya5BoIfxBPbFEjBFTEIgufSL1YD6KhVgT9PPbPIB-ZDtS1Op67zSy72oI-8glWbObNS-sxiwMvbvzALFy5neVLleeASIG0HU8Wpu0Dgivi9Cm9y0JDFjJ2_xP5Cww-fE6UvmjUCST98PKfRUJy0Ni1yUlkU-5avdg5loQKR8cgrXDJPqKuynKYppJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23957" target="_blank">📅 09:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23956">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMiqDNguJ2hz4DqtmAADXA8ELyvAPPChuJgNYtVzkxgsbUh_cbbnroTunfpAXDfuIgLOGOgLdLt8n_zScRD5lWaWULKbpfeoq4sI0E6IhA_xX3TEJG5qzGXeu8jagSBlAhGMncGFFGM-pYlxOJx2GJEspXfbbAzqhNHSwNuyHAEb7FNQKwliGFJBlmvUCDU71J8rQSbeLI2l2cZLkBkHyiMFZ54vcf4NBII0hEQ2IamRMqkR30k0zcvK6LKM5DKaYbSm3IO9zXLyOZybMJ36_NZqgIUZxq10CJvoTt-yAaPUUVVWpcH6IpswN0jokBDOwB1eEtRlaYlJU6UbZMTclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
رودی گارسیا سرمربی‌تیم‌بلژیک:
مهدی طارمی، سامان قدوس و رامین رضاییان بهترین بازیکنان تیم ایرانند. رضاییان اگه 25 سالش میبود الان در یکی از بهترین‌های تیم‌های اروپایی میتونست بازی کنه‌‌. چند تااز بازی‌های او رو دیدم فوق العاده بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23956" target="_blank">📅 09:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23955">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCQWv10fjw-I8D8bjEpKGDst1HzhWJHDHAQKO9wqm7YMb6u0JhP6QBpK6SqTsiuIVK0HtxH0peyS4xO2c2IvSU8fMQPDSeZqYozDbYqRmsvMxAAyiKpYWz1mB90iHywA9xaYskaHUzjMhYXfTwYn0S_kCl5_lesCA1vO5FkOT-TS6P5WsXoJ-O4EKfTSUpnt3sZwkVkVHY30Iabxn0rfmZ7wtyh1XQY5IpwkCIjR6NYt3M0d6HArZLmpipeBD3guuo5k6579ac1VG1hvktcQlYRNZqOA8US91ZtwSBv2oiem3Vcw6IWcD4EOLwudjaJ7mPKXZBIaEqnf4JCmmkfR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/23955" target="_blank">📅 02:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23954">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxuX9rainaCusrTSdb8dq28yK107h4kVqdhG16P3PYPa8L7D-TTlqO8D9rLM2gynhoDoYwDqU3aIFkYO9YPygWskhYrYv8S_uVAgRiSLy4uCCuqOohuhVISPpk8vGWtVplOLb2pF3j8TvEvszMMTkcxBt2jRAQDFtl9gwnWAoQaFHcKdwsJQmsIB8vtyDmYQj0TKJOwl8tfJMtHZcSs0Xrz79w5sR75Q7F8WQnaNKE97vjQzvT4n-3zztC1hrnvprCyo37UX3ajTGFNCHc8m7BUymcKOPbh6lsCoIyeu7jE78VIYYwjit0b6Qp8bTzbdroH18TYIeZiHSYTYfoxj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23954" target="_blank">📅 02:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23953">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQX82W9KYBKF9swq8zz5gG25onRblRjLWoxD-ebwYVhKRfNcvu9tQwZAXJA-GdZscjJAT-NR3XFx66-g-sKF6z_jztIebcOx9sY7ByQtqcl1997rXGpmk-GGMS1ddG-LdjNwz4HKGNQ3fH7GjlbgudRTiLcjA8UBNazuk6PpEnMe5_KZTOwNQuYtW9_YbaRDiLoeqQNpemi2f8BhUcAkHhw39igH6xmjVuttrdNKefjzuDrW6Kw410qrlibelFLJxi_NqmhokhzJvfKoSWrt9GCWs2NPiUiG3VhK5IwNx4itDVBrF8fbxOxtpS3MnMBV66VHjPMC4V2Gf1xslJhvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23953" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23952">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyLrZ5um8PIgd1S1ZWYzdsCVPVmRJt3drWmmgcYjxkKqdHkJqIcK8aR6YKum8tswZW_7oU_Gt638DsiLOiDnX7oCY6mirPnmhTpajugqRxgHKnb0qS38gv95sl8fw-Peb5sSqerWoKxchJB-4s-umCL_56SAAbcgOJTimNCUIX9qcnEh_rAG7fA4OGZkNqOjCnqh2PVvrD6kIINNHunC3ysXARbSpy1oQLiTSAu61qHNP2LBztZrgpHsnjwEy7nwNHEnK9Un0E6x_KDqtR6e8g8c6zUap5pMtTVVt1AAzdvXBR9TfvQ9x_TUXyHsglLzmvJiG3okprhR1lpcBV8Tcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌برزیل و هلند مقابل رقبا تا راهیابی مانشافت به دور حذفی جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23952" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23951">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=lvDGTsBOLFYWpG5ZaAnc2Doz7QSQCSDR_Z5UGaIEw4IE1sbPvNOKYi04GddvEbtJYQ2JrfZ4N22OgrFkRgXJJvXVu-p1xXd9dzmAGuAQhT0yr7Orez1fAuwSB3NTSxrT8Z-CZBHMgRMgDXm89BtSvt7CXvidjvqNQiHR6WAQBWJBeDJ-s0bgKuxGHqeoJ7iYROw-HAeo1lFdNK412MutgDSBQbwaklk5kbRatzk4MWDyuyOjr2NhTrI7lhEF8TsW7emKFOS_wHkufitTbcBSBe6yqqKyvFrDHeHKFehjsFKYbgWiOwrfl3T1GLsGpAAMCcH1OsHBU8gu7-plbDmP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=lvDGTsBOLFYWpG5ZaAnc2Doz7QSQCSDR_Z5UGaIEw4IE1sbPvNOKYi04GddvEbtJYQ2JrfZ4N22OgrFkRgXJJvXVu-p1xXd9dzmAGuAQhT0yr7Orez1fAuwSB3NTSxrT8Z-CZBHMgRMgDXm89BtSvt7CXvidjvqNQiHR6WAQBWJBeDJ-s0bgKuxGHqeoJ7iYROw-HAeo1lFdNK412MutgDSBQbwaklk5kbRatzk4MWDyuyOjr2NhTrI7lhEF8TsW7emKFOS_wHkufitTbcBSBe6yqqKyvFrDHeHKFehjsFKYbgWiOwrfl3T1GLsGpAAMCcH1OsHBU8gu7-plbDmP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23951" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
