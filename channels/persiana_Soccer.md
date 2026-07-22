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
<img src="https://cdn4.telesco.pe/file/t9QXv6BYYmt70VnVtIEQ32Bnz_lxVUiQmJZfUjEj26KTCNhCiJ-6UTUS3r7FLrS8C5blGXkETOPgBlc3GavOQaBwC2hsVbOPjQqyxEjRXPVET1P5PX5zRkb6BsVhrq91DMH05zDQQSZ9at4ffa6NhW36ZgZnLqwFVRWc4tsPE_i-DV8OSQ4yW-0rUdVkhYfBluo-OpTXX2AbfOnSZh7Kf6pkaE8eB9tTXFXlshoUfbbibGK4GisGAgT1tjXQ5c8Mo3G86WkbR3e6E_iftWO9SQsy6X-GRBTCJzA1dhhAlTZy4RHdlsHH_Qz9ZyExbWapaE8iJOkAA3rzCPxAhELNXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 545K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 15:40:06</div>
<hr>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwvOzMokkoLYNAotFP2S7_AZBkYVoZs1bDiDefzSnC9FwEiEt71aCSvEbrt0fmYM9RY8veF5kbm3NJkj8CqDKOYVPlHteuoDhrMzi2VVNWYIo92QLQ71dRd_7nQBoAyrZMIwg_RfIVB5pvmcyJTMhb5zN7shGS1XUR-cdf18pRABzmrc2RJd2AHdD2ynDwSqcghpsxvSlPHc810-hwm8IaqrIZN4ML8kubFtX3UqaseiIgkGlObpR0agkOUcgwSnnUgtW6VbrV-NH9du5twx53PqLkY481C0cjG1FU3lgLlhOEW-D0FJaFjxWMI5aU6pZVo60TL0jrmlvB_mlY1MIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvEr5QPWrew8lrEJpc95xgK-9DryBZmMVF0EIXwETBLudX5Oeztl3qTZlZcdl8jqYNQe2RVAsyVzS6DGPXQ5qD3jJF4OKaJDrKevZqlTDQyfSCeHD4eaMON_e-jsxq_wXvpPQe3TolTXp6u1LVrvvnGTAfa34bP13CsMo_4hReALLALTvfDm9Dl36AKtF5PlA-C5h52XBXnWM_4YoQhIm-r6x2x5f6LJAjl5AjrTzK4i86cykM9tW5fLByY4xMYQKPLI2nt3FaJuvbA6wBzWpyBaTtcoyaUX9auvrUjAxCj4n-v1Tbm-NUJBuY8jA0SKxZdkST-SB45IPzweVdk7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olteHfHhY6FAGPyNwYPVpjyNozzi1-b3pQhxs0CNhfKf95ngvEx7XDfWulWNJz9GPEYUDRZN9ogw-xZkhNCXIYVWOY2ckts0SlonmYlBoKa85ajFlEgbrspQ4bI6MYPpdLXxqTA2aSFnNoAjTRFhXaF1tAmOkdKyWesraXweIV5dhEDE-HwKgaROIDUYHtL2mCpmrlvzz2ehGJta0PVpuzePRfxBOe37fV_PZl1yVwYRM48NwuMlt75eBl1EqX6RQ8pcMj-QZrIADsPvWpL1k8If4tzRV5-atp_Ap-1Y73_Ie5h25ygNiGnXsUPOTplelVnJou-Sdz7afHBrr7nLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0F2hCZWzazsyCu-F5KGXkjlmCkR6NOvd9fO8f-rQqTBLWqjYBnroHbqDbteYu0b_2gtmu7UIXHzW502-UBj9PhDehMa542M8rbaZNLbMa4_HLtZPheOCe6FWkeyYV6WdBY4CX71KRATXkths2jXAIMnMo_zj2FdToctS3FGQWaChQwBU_tuTKDysjcPsw-1WEbzwayt3xycCZG0_YWto0NQ_FVFw_vwg-1kEqvapi9KfDVb37lnqVDxOO5zPABggnZACAyq8Jhh7iBvCSZroWWGBBxJ6z5W7cgGo9DgqOVYx5k4lJbD7KgN6GIJQs8GZ7dUPH36eaBw-TnsZPHXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4PgX-FlcV-_-wihCwlTbrQ5IrHNrA6VsDg8HNH123FdXmhrffNXINdXKzwYEob-oBdk7w34p5xPySSfQzYirOjVMEoqJl-QXF7I2Zxam69wkX0kbmj984FlnMcSz2UJIaAUi3B9xIk1yij7JrmUunE95H1bcX5hwR5aI1xtFZ9tDB2f9A1sMeQh9QyfnDqGBMpjqJS3xPFVzTTxX7zrzEUQrJeVxEXWp_bJQhONbVaIBTlnaWz7EfeU5LaI5-K0_Bok8CZ8bnWwATtJ-Sxva8ecbfG-ps4hucPZk-zSG5oINd4m8H0Sg5nS5jM12lUyBnwo7zXX4v3SN0x6uN7nBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYIED3fY3wavwMaHP3UZLkjHBpfCaaDRswfwff2c4Yd0r-xbbxJZAOJ-LffKrSn7W0CQ8m21hWIo0JjSsW-bXKLhzaiwPz4wwCCO4FMOeyzxqZBdueWcq8EtClaRmZ2Iis9wVMFIrPHRpor-u6s8HGxwnHfkq24VCf-Uz5hhPt8FFl2UwFOZC2TsHmLJwG7134JIRfvcIK9S1ZQ0D-W0aKxSW1J2cjWXLCrJxUs8-_bg6Jy32R54cXSuVbgaPhK6e7IYZhT5hP9n_nwex_4tOQ6ISL-dPM4LEbnjH25d1iYAGRZgEflPi3vINDerBuEHVRaDgtR4JFzhMXkLpGrfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqFDAKniYAtGC5HhYFlo8SqWZFsdT8PvEpjD2w9sEf82o0hcc9zGXtFuZIASHO-69PRyvISzz9iyfwpkKqPboKkfTnADCZq-pTCzzW8oXZgQq69I5k1Gy2mZZX_c7781u0vlSXLzU5EzxWT79XEnd7CNxtfIXd2trElQXCB49TGphWw3eDFyh-uSLdC8MvHvRdAGOh17Kl0THrQ-veIwEqFE6aeNMaRJ5lZRIL3qfmFJ7wzDZ3yhdyS1S_TCl8eRevoUfTiAVEfolNW1FLljPyXQdBw2Ogy-WExtUmivEcleWDtTIiqJMDyfTMflU5_iNoPyxhbvyNFAbGtmSHItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmFyLCClfnA97WjL4SxLwCGT5BUfKUGYrV25O1L9gJQuQOxleuLbGUTX_Bil83lQa2BXPhxyfgrS93bogN2ZKiqSsds59-J4f0fysbS0RmRBusHa27og1P-_JsfKLXo7gAfXAty30AJFYs9-8L8IQaEO4-33kp7DWZhgbZsHUT6PWWt2ID2PWweEKPo55AIwDh5c1ussKgZ03grf20KnmVNd4hPFJVRgTGPDn--a8Th3IGUkVXgtPUpgUu8YUnwUgPgXAchdIGc6uid_iZsJFbkNkpQ6vReBWpsy2_1PwAC3s7Q1Sj0DRdFs3s-b7x1eHyKq7nfX17ytUdkFmoXI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT77gQuzeTLN56X5pdBpJw10ZzRu4kKByKWBiojAbBdIFLiOJMCSGeYki18JCAWreFgEMOhSavXNcEV9AvFuUgs7Ws1CUkLN2ufUBwmLs0wEoJKvdb6-C5gLUHAeWCc26zE5rA98aCxrGlOFf3Evs5G6LdP5nyt_6IFWHTX7gnrDe8X5mJZs-zRobzbPGPFGiCMKoFgyzwU72Am_S4V610AfeJaycvUPAsemL_QJF9LHv4FfeezVDk1bLydtPPp_c26wk8WUYYJ0p7BA3eLFJxFgl_Qtbj8a7KVQyT4_emDj2rJ31aaKAS4tUv1zuyV2_qIYviDxV-VDGtwWWVQuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h41pbYvhb9e0DKRwl4nmkMylfjR-L_tw-Q_u1kgjrIAa-zqEKnIpLdrsXeEsv4NaKUUyLpzbZUnogyAG8nrPyUxHWEjTejJBgChTLoF26tDq62oMlN9rggeq-HnNLHq1xbsdgLGAQd1Uz23i0J0pCAAL_U8wmX0_ARuoNMvHyQv-DDyU8JrYXMyfBPprca8m0c1Jv8g3xWdzEWntvrDOMsWvDi4IA1_VnsilREud0LNmu96zrOoNtpPS4rzBz9zjVlBqEuVwK5VVzueshEg-U4zst7Zrdb99BALFund44B6QeO6SNd-fvUSw0ZCegQaC_xZxyRK5UiCPR07rRHVDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHSV551QYiaa7lNxeZyZHdoqMT5rVTZ2Mp_QqLo7WTBaFO3W3E1VFTfTT3j0P53qHoyERa1sirBfEfeYaYiB15LtHussL6SMdUEloOrh0KhkK8Thn14Bw-eGzIjDW1WbWK0BPNtSHB4eGsCjKSB0XyF-35NKkFlQy2X_ixysDWAN1KVjjWjRiLztEmR-2v5pJL4g-mnNWeUg6Dyrabb6dwT3qInXbxspQmbmhdYiTnFWj71lwwgRwRbHTru1IO3i_exbTlJBLDKBk47k8niROmoK0mvgDwG3brHc8CUnDotlSe0y86SCFbjuYT41KlrMKjmac5UjCvjabQJgq3tWHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jwia238aa4jtjgpwphxxdxOofx8yCqM494SeCF9gezarIaXY24YO-Z_gvdeT8j_P8nWI95Hty8ZESwACWdIGx-_hbvFMG-R-FfVMWpGHujFpjNTikQIDhjq_fJmIsMqnj-SSyDNSMIEtoySBtyLDMv2hY1zS58MVf_GylbWWNSf2erursHIpUxI8BIYQjLeIZoJG8lnTKgqdHA3BRCJBu68HhysftgiUhMCid-6sGsuqxNaJDujOnSq05tQJIq0pahUccHgdkCXl6Sea736ZlMBcqykxjjJ3AGDWlnaw1NGPz85rX4uSPuwjVivPFVvC2OrPr0HF3vMbf0j_2PdLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfbTxnVOObZtKHadnNtxCtZtdBr67DUZynwZBbegv863QHo7DJRrN4GT1-KpPcUqcbcuP9iAFKUW5HdocjXct_GJouLM6IE11LJnpaqE1LCiCiubLYpF_z8KSWaJwr28LZxjsJyQAnnV3IThy2ELUUCroidbFVji9lFQUrTJmP5W72mnuVGxdtupRThGoZSSNkL7gmI1mlgGRH59_ZOxE1KtcWsXHmVvRzCAlDQIuCV4kGoVvA1NqdASSzwaUOszNx02vbsm4Z9Mgp-iWXAgKGEfiRVVF46hxfVMKkKb8eme1Khveo7yB6yYYw_so6mx7C5yhtDUrThh3OUWIO9LIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grPzqcVyce5MbcL6MKBQ736WntDNNSBCCHlGV4yXv-f6hY9aL9KUptZhGMzt8G1Pfc1clCX_i-89Hsc7T6fyZsvF1hINQT9AH_W0MOE4VI9vlSqndsQCAH0uN1eouRxmaGc5vHleMy7eNpSwdJh5AClTqbRTGEai1NgKnIGzaf3bJDS5V-zwaxbYwJzVVTs-wXq6ks3kXsstP23-W-vDJJdMXGXViybJWMkOT6dkhCWRTBgjCfOn6Fvcf-yRl2ApkEOZNMJL4ohDWF02auUlvzvFKKsD8MC9qU0XATooNq4ikSY7rY3U-fy7FDUWXeglXY-YhDVgkvAeQabvm2E2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FueuJqDAvtTTLVmIuUP2sqMzu9BsTxqfH9b3vV0p2UFwih48yP6fdly-jBfFDRE5zUpO8BcBm5m7A_XtAfbXJPe2D2I9bAaAn7kF3BETpxqxBKxmKmr3lfgTeBtGQk01qEW6pCttXT9q1tDJZOOmb4S0gUEfM1KFFhuomVTax5JlgkPDOPSY2N3UdbS5SHrdL0_YIqArda-7nOE6VPMb-oeLXvn3MupFX8XwdFhCjFAk98AL00gQCl-EVq0XPzmYaHlViHaFkpgrk3-AaKYIBPIE-Za0GfNMN4QDyP2WO20IfOKlKuANLFI8SGKTzT5zQc0ZwRk_fSOr-vAAT1p9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26280">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxAjgqSl2SB1YeWhbuLTig2G-bw7zrV_xlUArawlnZ6fRv0SdEEHxp0A9z9q28hck0olb0ty8F4SyEHlh2t30blDhCu9uIZHWbC2qWugYc1zpuMlDLMKwVZZrs4ZwHuxrExRmYMhQ68PV-S164IVg-HrQyYxxUSP5IHVKA0BpI0nKdpMuIQfsHg4sTk6hp4xtkxJjH2lOm_RlTyMhITMXWrMfNeMya9nNToe04o1rnvOdSq81fF7EsZoevY920xS1RyS4Scuk5MT2D_RduxWbpPZ4V2cgh4ibuylMgES-D6N3a6ug1zAHR86NO-vNoPVf2dzjpg6nWtxhq7kjRIuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
🎲
سوپر بونوس
🤩
🤩
🤩
درصدی وینرو
🎲
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
r31
📩
@winro_io</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/26280" target="_blank">📅 11:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct_sCUJoYKCSkrv7FheNNZqS-RNvF_O_ORHUpCZ9J1TkFd9KMbFXRsSJVfplWs6IIi0Qpl6ARsCITny2-CfJYSQdWYszNX5XdAFkfpE96sy81oyaKX4rxXexB5wuWYPeWnfV7F8rE3L_zuSW6gQZjBFUqWOt5uE785dHXlnWJoAB7uip1Hm0qNChrPM-RSvsm1-FShQNw3syvvpQeT7zTODI3GBY2XI9YaT5gMKGmToLejEz2yI6ogvzPItpupOHtZ77yi-I5UjWnOSTMN1pFOVvs_OWeBbvdtL378j8cr1DBNpkZiGgMdRwM8KDBGrdphF9RsOwHZOEHDVOrvC8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-96ktIoxM9JGuoKECL_hoGqK_q95f3DJgVzGu0fwZnRzImfyu7IAYLYTW7atqFdtz3orRoCa3Nr3aSZrgjM9JU_ElVqRxAMhrwqnOuo-aSBYK2BngShbtpmH9QtiW2HxzT8Jw3oWFjrkka_f-vC5TCmKJh39Nc5Vy6Dr5uAh6Z_qEQFLlvCVwS9mW1pzG8H_bePJKrK6IarMIo4yUgkjvbS2k7DKo3K5Ud0jRyFmCW3kQ7x269FcMqePqbS61VHWMWzsGJm1EcRXFcJGJhuNc_zZ_-tentXYTRrxzWm2ZufrmUmjPZ_JInZ0sig-QBX5p5aNi1322s3iu09zN9ghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2fwQEkDyLVzJCxMXqJVrgoXOr1JZN8wdH5eoVbmVExLp4vUnPZMUhjyFbPKDUp4aTqa9YJT7Mxwir8EzfuKU3R99VghS6DlkYsZcU5fwooaJB8E6o8G-aTGXUm4wyq_ICUTn2xDa1daRLFnJT9Ml6Aqm-69mfJC6QHjz6BufnqePkRLKhkUxrJ7FWtZ4A7ZDajKg9CuSRewC0m3CefYR2BAQhIcuv7mbmfgwd58BBuKbabkWXwTXIr7zW9uUlQ-NexarlQvsq6_GjfOwqA-7b4aBVTijjfMo-9idfdzl7JGxTIH-5n3Ko3PxAMet2EjTS7c1vMpPgfzE0y9OUAwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGgMpjT1WlmePFKXhHUWCNDabILWNpPYo9W9uXRzLdkc9qZt3LuQNHfiJt1mH_txhUg7m78K5sGEUupg8XVS1ZPJlzJTVsx61cxh1-EWQwgGUsDt_q6hy22UF7URl-t6whxcotGFATEae0ejteVgnegn7o2Hvem5Oy4fkJvzctPWUVwCsMfnU8XujpkSvZtScC-8NW_FBAk1CLLLeHnhD576hYTQCCyM2gk7cY_0hJXIItv1Ki_w2NYNceJutoSJZZI0FbMpoUPg-Qi_sndf2ogvKLg4-C5On0dHk4YZSTNMlYDp9XlsH0JpJh7vIuRrSaOd7fIbtFNMYVxmiX_GfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpKImnDXEbYxcK8fR4QFYhY3M1XScePpCNmwZ6cdHbGhC1MPgDPjQ_s0udGbeTncuHl85hmRGwtaVg5Vzw1Oefpze2N4cdOQE9djkkm74bh82dOgmOZaTsLPLosf02TI-kbT9Y0q6zwk3WbOnoBTBTe4cY9oSFFWOZQHN5ZHToxgUqgEboTadi-03-zzdELDr_v0yOPGKym5EySGrup7Y_jrSUlPYmvlujqRkfsuQvzbm9PUtIEBN1rXXkH60AA5ZN04tHBgU5_NctAQhOpR_7Z37CNqMlTxWIGrc_wtDvnWxA_SHp9XTL5c7i1AcFLiPEQNJ3tYuO_b0aVTVYhMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQCmA1ZIljxhPY9k_dJojGRjQw4EH3csPf4WD5PbiEdeEnpveCRbIU58TsYqAjDjTUSCFZwjAoFLTj2aDIX61GL6_IL-MQixoj4ZDA4qKSLAK5090kVT9KKdUfbLoBAfnCsF9D8xZKb8kZ-sBgAx_uam_Q7kO2sMeYQPWtIlBOOpMEeNV2uGh3SmPt7mNZLFHuQn4TJSBfhh9PnwGQojz6qHJPZH0N_fOAVWY8oAutJl17x6OLumj3sNalvQ8M1ejsdT6AHQUmP0eApyrrZNLnfAvJSuKV0KlGUjjK6eJMU5UZgAY-TNXuSsv-5wrzE5nEb7ayoNeQexcOKg7Cn7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=MyxbedJN33ADN--xr88G4aE-npGXv-iNE5upGTEy29Qfgsr1bmOE7S7E9rDouDj24HOQ8-BLZwuZR9I15pNsQ6Y5Xzqw2XyNewR9AtlNwsTfNqLE4zeN-Vxm6H9-3BDfaIszGeE-EzYchY7tFbJRwj2v_ewMCcFc-0tX8sK-BI3TIasYY8V4mo9BZV4PRY6TBAOvJq0DNfMD9bCObvKkPWsDh5_WD9llJoca1SKB3GecCrrCzMaCefGm4W-Esv4v64aDqYsur_MIT444-X1izVDJ5OM891MwcU4QajucL_AeHziSuAgoQ29z0PwAjaAq7Oef56Ry8BceOkjf-b1LUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=MyxbedJN33ADN--xr88G4aE-npGXv-iNE5upGTEy29Qfgsr1bmOE7S7E9rDouDj24HOQ8-BLZwuZR9I15pNsQ6Y5Xzqw2XyNewR9AtlNwsTfNqLE4zeN-Vxm6H9-3BDfaIszGeE-EzYchY7tFbJRwj2v_ewMCcFc-0tX8sK-BI3TIasYY8V4mo9BZV4PRY6TBAOvJq0DNfMD9bCObvKkPWsDh5_WD9llJoca1SKB3GecCrrCzMaCefGm4W-Esv4v64aDqYsur_MIT444-X1izVDJ5OM891MwcU4QajucL_AeHziSuAgoQ29z0PwAjaAq7Oef56Ry8BceOkjf-b1LUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLyb5v1dcs2zs6JILMMQOGt3D85e0BlyCGhLkxM8KQZo3aX3iH1Zcv0ppm-VTtyTo8zPNDf1YzhrdQpXlZRyvt_Ml-oEo8qfBsNH8qphTsB3vblKYAc-2IUp-_stnXFjjGlHVmh7T-TDK0SLzE7ywT7UGT2xJsPZqWbtXest39owBylQwsiAPjmlLuyVxo5lbYxHwfcD3uCCM97ONLBXwLX2i1nAJL2OUiFV1UGH74PsbRNkmtjPgj1bHnmcPUH_j1_WHN3Fpm8zZNgk4p80L41fmY8Q2FYP-1u6g5ThMjp4yiykWkHKKzWqLJhgFxRf-lgZskqZ4Meu0-xLJdhF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=ZRhm3WKXwJTwPFgy_1IAaTNh6n6zvbs-nlNES96pspIHjJo3QdjzkfMAiUjVF0Ae7Qq6HFliHFaqoSogCcYqB2MAhA3IWUs4yIFsgD0ZEd5uwNoZNo-vJy6cTTjDRWTegEZIcLHAz9cWAF9SW_8m7hFfsPtNDG9v7l0CUIw3r5610h3xjPj2soFVEIzdfTaNgY5lezCqTiHjjVyYZUTWY_NGWBUSwasyKJfVkAZcxNH_7pgtsJzvPSRA-VPF6EG03IJEBIsJOaKNQGkUFTDpy5XvrQ3O5-VciAgbRv6lME4iGH7EwyhC68uH_17UccdtmsV0PSOe50uVeHp-YnzvfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=ZRhm3WKXwJTwPFgy_1IAaTNh6n6zvbs-nlNES96pspIHjJo3QdjzkfMAiUjVF0Ae7Qq6HFliHFaqoSogCcYqB2MAhA3IWUs4yIFsgD0ZEd5uwNoZNo-vJy6cTTjDRWTegEZIcLHAz9cWAF9SW_8m7hFfsPtNDG9v7l0CUIw3r5610h3xjPj2soFVEIzdfTaNgY5lezCqTiHjjVyYZUTWY_NGWBUSwasyKJfVkAZcxNH_7pgtsJzvPSRA-VPF6EG03IJEBIsJOaKNQGkUFTDpy5XvrQ3O5-VciAgbRv6lME4iGH7EwyhC68uH_17UccdtmsV0PSOe50uVeHp-YnzvfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFf_q6_Xz0KWW8pQucChXGGEDqRkZRo8INcxKiCNKexZKFvay-v3VPGyvd8kb4KTbV1WY5Rz2jdxwsDC0dPuvuJcORBKXkf_r3SjO0JxOC4ATdRow69LsaMxcNGSXx_qvrZBrkcNcVtYQFMbIBfPXYjpzDa2M27-tIrKXWhLZctLG6cjzQTz7h-QIEDbOX6XHp0VWojl1zSkoHbuvMb4zfKVK58_98Fw52E9m8goBHZxq9fxeCYVaxaXPAUGI6mSbtG8mtmj2XKKZnDs7GOoE1mSt0S7d-pNfc6WXVn8dCoVkPXrtyC255QIAzWCepwW5vmPOv9a-znvl_l5mdmuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bs5K6FBVOz_p8kMRhsqhhcjsGlCrPelI12y3FotDVD2PPKiTHGqF2cBRDVL9MtcnnQjQBvhI1-nHHR8oNv6nLrfOXMidtvajiJl5Vr6eo1BMxk10DRjgqa5AVby6_L2nqTH4Kl-L4txlzwH0494sm8Nmt3XgaOxgN-AuD20xdMUc663TiiNQcjdKMmHIk7E5QdB2y10eJimH_R_bupifNllkTSBC8Kv5bA1rc5ndcij3UaDkC3y91kakIzUdUw15xt2Hztvz47TgF8CXBqkGsHaFbz6Hedz5vSI0B7LhRkdPQ8s13SdrJOpgr4Zg6RsYMhh0w3etfQFS4xBa_-5sTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=ZlVfcYCG8sY55qqxVgbiV4izAz-GtWaKCwH03FrGA8jjANBBnJhvWcGLOAzCaii25KKNJqK8bNJZAGD0XcTaG-dhg-iAlyeDS_p4SBYfOA_gZjUdq-z_rR2XK5CmyAAL4O4Gc2UdSwE7vEQGlclR5TExlTK76Y9Ay3YSZzdzgIk6AABK4171RHTWqzpXK6SUVCwt_NXKVeMh7W4lZEVotJ5_QGauj831PXh3KVr7n8bcMuxZsy2EhtQtFRRqPZ_KbMIJeTbYxNhABZzXeuH1Hnslj1IcvAMeGqxDkJImgbCrQVxFdUwq-P16xt28yBzkghjqRJVpHdjzIzzowUAb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=ZlVfcYCG8sY55qqxVgbiV4izAz-GtWaKCwH03FrGA8jjANBBnJhvWcGLOAzCaii25KKNJqK8bNJZAGD0XcTaG-dhg-iAlyeDS_p4SBYfOA_gZjUdq-z_rR2XK5CmyAAL4O4Gc2UdSwE7vEQGlclR5TExlTK76Y9Ay3YSZzdzgIk6AABK4171RHTWqzpXK6SUVCwt_NXKVeMh7W4lZEVotJ5_QGauj831PXh3KVr7n8bcMuxZsy2EhtQtFRRqPZ_KbMIJeTbYxNhABZzXeuH1Hnslj1IcvAMeGqxDkJImgbCrQVxFdUwq-P16xt28yBzkghjqRJVpHdjzIzzowUAb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuSVMnzg5V_MCgdRLhno_LdN3F1nTZMnTHbT1G2I6p1WzboKEuhwBsUyUJ63T-Lss5446o5zNq1mBL8b5JJOla9AKjETSxoF80o5SMN197cio2sEkwAa890O-seQ-E2-1S3vBXKxmO7SwsSqVpNiTZSAERwsoESFATqafeU7nZPpM9D8zj-HzSvyNPMXpxmkiA1LVrgJUM5uOT8xjA2keXuwMWDXVwbvmRKnqnj329wI-AbeOZjSvJnSUGDyvpaQyaKmZdFA6r0ZfGsFUO6u30sV5QtfHCZ4hW_kNorFjTOFlJHc5R-wQgjmfO_HJVNB90eTDKRrUjkjYONWkz1Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIrgJDezyXVDd6ps9UghDn2U8rEwOCzXZdsEcyVofccc_f583zVtLxM-AlATVbJFD1jRZ1ZL21EQHbF2fWOsIafShISiwK4jRId2RjAhh1-E_gJBCe6rRHXKKzvTj2BkdTNNK2Rs-yxKscjjmC2GhSBeG2Q_-C_INFZLqjWVsxdlgUazN9WAxtgHbUd5suUdEI0u_Iq8it9S1C0_DPiZ4EB9nEF8uno8At7HlOVfiOKVNJQKDvcG8Bs6mGxiwuVQIEzBOfYdyVeARkQZmjzaK8QiK_QIKSohlTMUghB0AOhjQHZoOz6WOB6zP-8nDo6FTHDv4RkEH-lgiapcACJ57A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBCEUwBpelyJiO7UjmALKc-_-v522PeUCWqPtqIOiHJbNXbOPVbH5mGI2GSsZpWaa_4gZMeqUC7K-8stgqfDW6-UtCumBapvJnsGMit2Nnfeah66oox_PTSUmGs5n3tPKnRPYvk1X63IGK3l_GQI2gZU2gB1ocYe40h_Md0xLLfHChf1eJFr7oHhrnPJEhrwoeknwiIKF5lsOH6D3Oo-TqFSOPyKhFGfD3OyP59ZF7lpdkMa2t3GoQOPoB_P-AkfwJ7sKONfaWPadp6PLalrPeJvCkAGt81s_2K__h-aw30lbx7_3Xc0e1R6SQ_UlnRMzkFdxFu0Izn-DOe6_4EzvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=O8zMfgOwgjtqf_VeTnKlJhTswLRXBja8QmsUdfwwy20FUfaYYv_e6bMPSZeLSlMxBBiaVJ_jK-t59zGkSQkaC7g_v3NvuiPXpHPicTInrK3J-MMVhDJk4jvpsQ_PoqDrgAS1g5yiUVLIOfqWf28SNVOGvQqBWfO5Uzb55E4Lta13cNob6ZNcW23IKCPrV0qGymjwuxU7xqpLFuHSSdXhfdCrD_-xhNmlxLNQ1aTWWl1-vWUVkHtNkSFxqnU2aRtRMLmVwAHXokiFnmyO76Tu3PYejjLicipXLP8am4swn5iT3OnCsJeCZY7hf2D3Tfa2wv3jFBoGYYxUPWSk9w0wLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=O8zMfgOwgjtqf_VeTnKlJhTswLRXBja8QmsUdfwwy20FUfaYYv_e6bMPSZeLSlMxBBiaVJ_jK-t59zGkSQkaC7g_v3NvuiPXpHPicTInrK3J-MMVhDJk4jvpsQ_PoqDrgAS1g5yiUVLIOfqWf28SNVOGvQqBWfO5Uzb55E4Lta13cNob6ZNcW23IKCPrV0qGymjwuxU7xqpLFuHSSdXhfdCrD_-xhNmlxLNQ1aTWWl1-vWUVkHtNkSFxqnU2aRtRMLmVwAHXokiFnmyO76Tu3PYejjLicipXLP8am4swn5iT3OnCsJeCZY7hf2D3Tfa2wv3jFBoGYYxUPWSk9w0wLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=lQuKf8ZV-Z-gNb67V5RC44vQo_YYXRlS3f1DPhE8U87QXOmepJ-e2txDTS6ZeSeJlXKVtrQuvL698Lm6ZVqJk6vsiY3SJ_B0jG_ZLyP0HumgwvDfMlaQFQwbffKMYrzRf7L6PUnlxHKYIGrEk1CoUB_g39VVB2m_SC4TwHrfXh3GWTbGWoXXp-_9NzF5_ehDai5XUs0_NnFGnoLlkludImKS_oBldxuJ9XzfJ2AkCebR_iOB3AFCn8kxJsgWqZEUH-CPZdSRMYumXD6eLhPiq-lQcm8Dq5uB-GnBt3nAymsdOH9It4YNkVpYvK9FraHuj9cWhZPlioy_96vomuTIQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=lQuKf8ZV-Z-gNb67V5RC44vQo_YYXRlS3f1DPhE8U87QXOmepJ-e2txDTS6ZeSeJlXKVtrQuvL698Lm6ZVqJk6vsiY3SJ_B0jG_ZLyP0HumgwvDfMlaQFQwbffKMYrzRf7L6PUnlxHKYIGrEk1CoUB_g39VVB2m_SC4TwHrfXh3GWTbGWoXXp-_9NzF5_ehDai5XUs0_NnFGnoLlkludImKS_oBldxuJ9XzfJ2AkCebR_iOB3AFCn8kxJsgWqZEUH-CPZdSRMYumXD6eLhPiq-lQcm8Dq5uB-GnBt3nAymsdOH9It4YNkVpYvK9FraHuj9cWhZPlioy_96vomuTIQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bulvij45AcTGXTZ1FnkEMOuMIF7ma_P8m55cLBBxqRKU2mnMiO8qQ5CXJLuqKrXRQxUpa8djzCFmJbPwcOUEjLHn-7FX1Guout6fzxCHaK_ylCYtqVFXdE07LyFRy5WXThv87Z1X0G3tqlPbIt8oyLE0T2IqjxXD6nQB1Fu-ekQJDLuxjlGt1w0fOWiCev48fwDyvYUqt3KvS-XtcocXN_Vp1QMHhDWQ3f2x-Z_C2vWaFybtC8okrzpi3VlaZ7ZBBUXRuJTq1SesswQmLvToYpkEnFY--sUk80SW7nxajL32G_A4iQ5kuB6pGrRH78XmdpAzAmUdphk5wnPyEOtybg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J633c7B2mlEVPbmnWIFHltIcphLnz60DqQGdU91TLWBq9gbFvsSj97qmOc-X_8Dk1unA6bDCMYoTPtndeEJA4R1nD1mf-5CTM1V8uzuQa17tbmd3j2LOiB2EmDi4sdqfWiQK0UqSH_Lhy-lTJS0dqf_ZNSvRmgRlQ6DKsiQqcw9bRDPnseyI9CmGjqi6mdluhW4An1F5uYFWdN_gZddqNb6rOGojWuO0qv-4xRcfTBiNJjfni0eHxaZva3_2YsbOCviYqHc51sIkEn--diWYsW5nPzaPq7Wf85ROcT4I73tpDRnZHQ0YGufRdJx02exPq4nKLeJDwEgcWia5hCUOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey56noqRzdOHPf0rGC-n3KPaCuuCJ0ju6VWu52kjDvtW4w3fjxYLJTukvF-mxxNZf7abWh2sDnFWnMDBLopxGBwNXIWiupUAdE7R_3Oy0OjQmVu9PIeP7ONVJqd65rd1EgDl9zWNe82CtZcRGu0NsPpOjVEGchAUz1CbR7vE5PaKYkXEwKysszqjRQd9Ab6t2r_G4TLaxMDa1lsmrt9OMgiUKNrfsShf_5rhc6Pfb8Q6y8fYTLaFEVhuKiH7nQgPW2B4iQmfiKzMJARbrqwRXTEXx_Tu-TGRrjWnSXZY52XUZvVsePlnUPHWiDY4m2Xf_qwF1qKqs3ADioky2pr20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCaCdgzPrPTckBLiGH4ogIocAO4xKzddaNiwWTpTT46VyZmOkgLrLg5DbyVswGH4W0J8Od_vy8eXHNZNZLbiBHb-RryVSnPiDODoXiC_x-X4HsFonVBvVGsZpfFm6-HX_EvRplDlWYgCwVOf-ylR-yW9DXCx7MqogsVF6pEUCbIl_iyzdlIi_y8aBhIBpvZlX8g8z6reZDsY1ppbhBKuUzRxhs44oCW9S7vbA0IDB_92b7Rm5BOQSeTP55WDAEiq4BUpWytiRMgMAM0bpj0lipxRxGkRz3m2iMgxVL1GFyN63VynltZ2NCzFmiSEJEHsON6wO2tmkX_Au-5VBUEeOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewi-UxTLZ-rI0IOPHEENlRRqCG7bUmHi7gQvRdM2lEEdrNLkevJ5BvaY7aCWrvqbKX2_pXhmTdFzK8PO8-X82BEztrVIV5XpyRAFxHbAdDp-xuq_786uyhJ7Frr3cls0fGE_HadtNn-cSTzxaWxJHc3KqctLAoftIO1jAPdo9SqSc1P-eoGDBTGh7qaLaexiISR41is1uwohn6XBL4TwDp4a9sDDLRF3JkMB_83fl9aMvabebVZV2FpSvdLOprgp1M_HFVcQBe8poqfQKsTO6O5Apddat4MvW9ZSgkYvl-2Vo8XfZLJ25VmZTvU1NNL-ipyku_JmN-Eu0aaavVnRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5RYf0SkAqdghInfnCo6ZxiiMTn0kE-GfsWS3nbTKuNCQTIc83cTn8_NfqF9so727gRZZm9hQ61Ljr5_G8tt6V5p-MiVPikl1Oj93REYahZF5LwXZUsHb9J_7Fk629vMzBIfMfIkbKRnx_bY5CqVmbtCB18HeB2JrJWY-svOkB2hKOSipEslfYXhu3lycdtND5aEcOTvj84P9iSw7L-jXIXHY4sMT3tuR4AGrZaJ-11Quf5fMt_AeXyi-4D483dA6bcgl5GH4ix8YcHHSHzJg9gcwehl2jIP5hHXNxTGbrdsdhza8nJG4H0m6mQMp9f_uMhDlEHdzc_clq3uIbs3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=lvtLBCY0ojrko-_KUSZXZ_dwjZ_YR_UMedZk408bGX0v0E3kOM3pltQi6YOZd6gS3dVvxwHL3aOmsKzxyO8FP8WHlZNRyJz-oalJulKdTxNs1oKPwruTJDr8NEORcHLDbN13Peix8TcI3Todx8TeCemTtRLHPmtgr84A01ff_bf_hThAqTNVS9cfB_cqcgCSedVWjl1YuSdnCULcGAwQ3gXODvYpXHkiNHZZoj9VnXXiAenjwuyVPLyAvawG58NNqc7DqcLzrl5bVnZNF5yDj7IDjQMAVjSYZRmKScRF3LY36FRBEx-TuyPMlqkmCxmA03n5FRgQ3aZiCiwZriVgog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=lvtLBCY0ojrko-_KUSZXZ_dwjZ_YR_UMedZk408bGX0v0E3kOM3pltQi6YOZd6gS3dVvxwHL3aOmsKzxyO8FP8WHlZNRyJz-oalJulKdTxNs1oKPwruTJDr8NEORcHLDbN13Peix8TcI3Todx8TeCemTtRLHPmtgr84A01ff_bf_hThAqTNVS9cfB_cqcgCSedVWjl1YuSdnCULcGAwQ3gXODvYpXHkiNHZZoj9VnXXiAenjwuyVPLyAvawG58NNqc7DqcLzrl5bVnZNF5yDj7IDjQMAVjSYZRmKScRF3LY36FRBEx-TuyPMlqkmCxmA03n5FRgQ3aZiCiwZriVgog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=u58PvyyW-aXc3CahdneMcU53reC8ajsb1hB9Ktr8SDHCOHlGLwvYpZ-70ozWmcmlldQ0sDO0kqxQIYO6eHhjs4zBKETrq7Y4HRc8NzJe3WvFxxRZBtAB6d2klvSAcOVemyv5j42q5wUt6bbYM0GGGScbLVSa6lyDyjry_xpnh-8R8zUwO4hwsj_f65mCIIGOGiFYLR0QG5J3ZVmkDIQJwQzqPiZKeopQvnNfd0ZWzOjCyelYUq3SWR4Uw7IkeQJBbK0_hP7VgR513Ht_e0jHcqli88CpJw_czhkGAb2X0GjkNeZbDpyiyqJxYATi7ziakDGFc7L1pNicJ8-GND9pfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=u58PvyyW-aXc3CahdneMcU53reC8ajsb1hB9Ktr8SDHCOHlGLwvYpZ-70ozWmcmlldQ0sDO0kqxQIYO6eHhjs4zBKETrq7Y4HRc8NzJe3WvFxxRZBtAB6d2klvSAcOVemyv5j42q5wUt6bbYM0GGGScbLVSa6lyDyjry_xpnh-8R8zUwO4hwsj_f65mCIIGOGiFYLR0QG5J3ZVmkDIQJwQzqPiZKeopQvnNfd0ZWzOjCyelYUq3SWR4Uw7IkeQJBbK0_hP7VgR513Ht_e0jHcqli88CpJw_czhkGAb2X0GjkNeZbDpyiyqJxYATi7ziakDGFc7L1pNicJ8-GND9pfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnpWzRn20eP4rNOZw2XlOkA9evRYa2jrtLrnfvcBXP8-GauLXX-ZgLuHxAUzczcE1W1VijQDsaOTgQkXYyEp1mQ0tg-aOMThKa1CkVsUjgegZExjXxFIfL5GpYRWVBmjMwio848ZYecUc2T59GFRrSRg8yruXcBS5qYIPPkjEVZYEK7irhnvta_cZq_k2VJI9LWM-OFc2ewgI3XhKTRPGwbyVPDUGUgENoTh8de7qOGNZmFbEeBwkzu0DNxKm4e8OKbv5cvp31p35POAI2VaPT3Fq82eG5HtdBe_llivTUaJKR4CGE9V8buIBVn4Q8RwMOAqDnGR_B0qMXz-j2_zMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=MbbCrzbSzgUvhyhG7YEwKdw_zPPp6PPNZN2BWU-shJ6buAOIrIWIp5L2veeO635QpQYiT2iLLjjKb9QcUyjb6ZKDdzTsSirywuon80BYCI2cbmckukRYSUrDOKyOryUOSo81mA_bCaw9IRw7rrEKM9WtUwXNW4n1FV3hdaS2KnxxHTevDm0ZE9KHukfPHhqOyionqDtZgPhHfX2dMGEfm2YapUeG_0gJe21ULXkeacRFAytRolLJ7MxOsDoYwYKLuxHuVRpwwBO4_GkWdsV_szOpLnduypmUGf3XNLcmJo06Hgs386gtS7lIuMsNbeRgKnPkA6GXwvOcbs1fNArKCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=MbbCrzbSzgUvhyhG7YEwKdw_zPPp6PPNZN2BWU-shJ6buAOIrIWIp5L2veeO635QpQYiT2iLLjjKb9QcUyjb6ZKDdzTsSirywuon80BYCI2cbmckukRYSUrDOKyOryUOSo81mA_bCaw9IRw7rrEKM9WtUwXNW4n1FV3hdaS2KnxxHTevDm0ZE9KHukfPHhqOyionqDtZgPhHfX2dMGEfm2YapUeG_0gJe21ULXkeacRFAytRolLJ7MxOsDoYwYKLuxHuVRpwwBO4_GkWdsV_szOpLnduypmUGf3XNLcmJo06Hgs386gtS7lIuMsNbeRgKnPkA6GXwvOcbs1fNArKCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=eAGrozd8VukSV7UttqqflTJ_Lg0rnf4fPNeygC1xpeUXEAQbRFN2NlSwX3I2mPL2iZ8tPf_EmzbCulBljT1KbOk7BViLqnLuPerZ7XY4TOlNhQthuZ8cQ9z11O3CKtR1oSOmlyylyD5KjjPXCKrSbJvgqJY1oNxbPjHphjrno2OrguimefxojSlDIWu0kdDj6ED2QZ6wJQ77P5aWXMuUUcr9tgr72URj611ZQ4sk0rLSoCZTYoSQXvN_rRsZF7eBX3QdOl5bPOX8xgpr_l0wn14fW2E7IxKxFB38Rq_wGRsaKZWBozyQe68HgTwYJUBM0NKBHzGG1px5RLQDvx0Tkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=eAGrozd8VukSV7UttqqflTJ_Lg0rnf4fPNeygC1xpeUXEAQbRFN2NlSwX3I2mPL2iZ8tPf_EmzbCulBljT1KbOk7BViLqnLuPerZ7XY4TOlNhQthuZ8cQ9z11O3CKtR1oSOmlyylyD5KjjPXCKrSbJvgqJY1oNxbPjHphjrno2OrguimefxojSlDIWu0kdDj6ED2QZ6wJQ77P5aWXMuUUcr9tgr72URj611ZQ4sk0rLSoCZTYoSQXvN_rRsZF7eBX3QdOl5bPOX8xgpr_l0wn14fW2E7IxKxFB38Rq_wGRsaKZWBozyQe68HgTwYJUBM0NKBHzGG1px5RLQDvx0Tkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSH_Plfg2l2tmi8IlM9LKummKfRlRU_PSE_Y22qPNdz4tS23zDJMhPmXlYWhiFSjCcFY_DRo1PaxT7wTK9QnYVurjYym_aB9C7o1-SFJ_D5YbAGcIZkh-OVgKTUI6T6B7yRjHg4p7kcvbrswNCaP6ZPqVHglopuARW3bJVthGHivOH685pqkZvACuG1AaztVfnvGw5gh41-WGbWnmrfVngITZ-hu5Mf0khrmRTFl8q4XI-OMzSuKxkCl4CQBPe9Cf6fgoONDpNw6P8Hq4Bt6qtnQfU91YRgJmgBHSAYCAYyLeAJ53tbF2r5cTVYdHuFAcbw1mc9J9ZnHDcZW2uD2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRW2J7YrqWvQ_wv1GfMLppXWE_-C5uOBbgmLXcN_G1ktNlJ6ySH-ZDcTn8aHptdtI1riIxZ0d62BRlCQEv2XOMkCYcGklnIGuFTiNNJ1ehxsNrHZqlyHChb37DNqFC9L-F5KzE5UPM-GeWBAVZxTEuX7afBEmJnFigZg3J0VFPcbwOaytICo3hXE9EZDm-PrXZ2FLFzBFSglz0cERlqRN2aM5MkArNvOoteAIJQZVWOJnmGiMvSizLa68wpvViwq_GmDq8bYPWtTqexzqObX7VUGz_SB3FjaoNYT5SFVLN6bX0evFRzDGP_26v8Tuik06U1oParn9eelvxhuEpKEkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYit2J-Ags0n_chRdeUhrhGLchtZ93gLjVNb0doUHjbMVhp2LGMyiHSH01-QBdFTS18__HECaP3K5JMcJaua4B9-ZMVeXAvzGIOU61pforwOIZWx_zYkTrJvwsoZ4sKyv_8S-mf8ZH8wCKXFaaNNOgSX566urj8_unYgJaLnsJNVlF8wvv7A_Zmojwx277HsbHItF0zExpfG8tHhXZXiZKUBWdslle44OpRohN0F5LnvNsCwL5-YzWpDD-MS1kg6d2Ez2Vg8ZQZLHiYMMmPL_HyB6I8xEHZiSkQ5tHAtMMdSzRJZnKe2Vka135qI5wtm2fWfiYSBQB5qu0FXvg6vgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=Q3EiFrdSqS1ZshP4bIjGIgTQ4YYmbY1SL-MbR4SEn4bNCPvkQCVQpRjhK0mVuSibFS8CgRetKvhfxUqAryhcBjM8hzv6A8dZNlnb_SPyd7VAY3-x8-scssCx6z7Crg9TqkMT0LV7V3uTquCtmkmcMaZ0XbIxz6WwyOxTTUUTKP3G6G3JR93vjxiWS6XWTcpsRtZsSofNxPwOOnr83KMDtPWiXogMWpCb3iXoVXvckuDCpaxDXvXCPlllU0HbCUtJJZLCf2cCWR_XbQ4zMHpMb4O7x2v1QcP3QiRVJ0R_qz9AH118m18q_byl05U_V1N6TtyaBOe-qa552dgqLbPpUKke0K3FLtgb0gnPMwT94n9gA2Mz-8RmtdCmOp7sCz2zsrcT5WXsloYuE_HURW-yQ6PCsZBec9euXB_yt4iO4_0ON021FGMUiMk4bDRO890v-aQeA2VhE3Kp9XYBkp7vkzMu_PqT-NzsW-SyEMVBXI5aHxWauXbMkpS-SjPa72bQUCKPatfycrfjqrE-GLTIvXCxk6l2IL2Y2ClroRsndSMoaVSQan1vsR28K3n29L_oZUwvsBuftTTVDWzc2gZZ6o_PXqC4hrcPLsG4NjzSWVLQ6B7ah-EcQoGns2VS4gg_dzWKMyFiOWHpdx1kKJjwqkzi5EbrbILDzQAVO19cbRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=Q3EiFrdSqS1ZshP4bIjGIgTQ4YYmbY1SL-MbR4SEn4bNCPvkQCVQpRjhK0mVuSibFS8CgRetKvhfxUqAryhcBjM8hzv6A8dZNlnb_SPyd7VAY3-x8-scssCx6z7Crg9TqkMT0LV7V3uTquCtmkmcMaZ0XbIxz6WwyOxTTUUTKP3G6G3JR93vjxiWS6XWTcpsRtZsSofNxPwOOnr83KMDtPWiXogMWpCb3iXoVXvckuDCpaxDXvXCPlllU0HbCUtJJZLCf2cCWR_XbQ4zMHpMb4O7x2v1QcP3QiRVJ0R_qz9AH118m18q_byl05U_V1N6TtyaBOe-qa552dgqLbPpUKke0K3FLtgb0gnPMwT94n9gA2Mz-8RmtdCmOp7sCz2zsrcT5WXsloYuE_HURW-yQ6PCsZBec9euXB_yt4iO4_0ON021FGMUiMk4bDRO890v-aQeA2VhE3Kp9XYBkp7vkzMu_PqT-NzsW-SyEMVBXI5aHxWauXbMkpS-SjPa72bQUCKPatfycrfjqrE-GLTIvXCxk6l2IL2Y2ClroRsndSMoaVSQan1vsR28K3n29L_oZUwvsBuftTTVDWzc2gZZ6o_PXqC4hrcPLsG4NjzSWVLQ6B7ah-EcQoGns2VS4gg_dzWKMyFiOWHpdx1kKJjwqkzi5EbrbILDzQAVO19cbRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI1c7BLjMB2HLDXngsHlBoMCJnQMa_LyTsyH8QBvqjysnJkR-i4Xwb6VnGOXkIfT25cDZwaGh254lJaNv6sq44L6mJX6xCbEAa6_dGnd02sAGTkF8_eTblRcFY_knwkyM5uGt0TrAYs3elHJMHseQFupDCOQi__WwLouNC41l4D1sSCM_kj7hObyBYVAgqxgHoPVc8K1J7CZeRNbDvc7fDyP9v4W0m47wwkOJmuAYK3p0mK1HKFJ00sjBL2YvsKWReDX_4E3sSx6pTrccA5NYHeQeMDTrSAwhsH0bI83Gs45SM69uz0UIuZBspSlPBbQ5zEZ3lejDBZCWQsEiosagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYGSEg25k5BUpwQo3_loBlX6548POwTDHP5bB896zTqUGsHPfhVkap6-NCnKtbq9kaN-91Urf1aNBxDKbTBIuLZnurarKg_QuacPZEgp1uK2nyOmYZJL_KlQvTOEnxyZu1PTWOaohz8KgfU9S9snY7IfGLfoemgdcMSWlpmPuUw0SG3I4suf_GKZrybdttbhGpXCgogd6ua2_9CvhgzURYMXiNrkrZ2dUsoKRQ2j01yyVszURp_6rX3pJ275rSZK4RaNhTe1ilB9AsnvMSbGTEXuZytDX_FMoF-_65WPefEgCNmYEqAVI3WoXYV1KSTXaeSfqUPMqHwkB8XMz-W8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPDgWmBD_VqPj2ZQ6A5auNt_Kv-Rd5wMojGKrRyiUSMXXez4vVsp1hZz9iZ_I6X-kJZotYDa7KVM4YPI9EpQ3TUwLwQLIAvG91mYgvzUHTHLcUEN6Ld6LGXBI-FlK1E5qL6tvvWVJCNgK1rV6qZLEJRJh0msZczOes8K2dzr-G0RKoWUYYXXVcnsBvUAefAAkMa1Kb3C-OiLMuE37Z4Itk0BIC93BmBZlp7gF9LMR2ND4KWwp4Don8bIYg71jXXGfsQkYFr_gBBy-XH1z0cSxR2itbgCNh7zxB0YX7Qt7gsZbV-6p6J9f5vL_4Zm73YXU9jbAf_5-ZdfXcgJJsoAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XksDLVeIogIRL_gU2u7qU2js50aEqwqcDH8HHsab4mzAR-vwa---klzx7pcA0ohXSpW0J4eIPSrqZ21Uij-FTtEMg-SMtgRtWRQaXdECMmG30O7CSdg4-jSRpuqarV5YzHBgzNrgdPlLtqwctF69PGv1kjQla5pb84-hpHzeJrmFLQ_l-U6czcG1P68z0-Je991hSgczGgM2Lt3rxyIKyF0lqgce1UQ2Tuipl3DeEjEc3DiZuVTcq7Th6zQnRnWupPVBqL1Atzz_1zQdY5zjbgtkzO31-XE1eS-JoXCfB5La-zCtSZiiMlYrYoYQ7ZV9TKg996Pfvvv-v_LazKiA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcJCtp5Y_wBsCOD29T9pkD_mG7_bUy8me1sePHUyVCBZLLYLjqLywmWMQ0PxBH6NUVPGPmKagiXZSHS6i9_42LhFpELH4j80MJU0YFYt_vdAHVENPwR5no3n0O5vdlMeMKpRe_hzoq3M9R0YbKEcfWnFHk4hiMgnCssU9fkOycxf6xcFk-wbUFnELidYO8xOJoOS2sdl8YqmGMQvGKNtUqOcozPbhXyp8g992JF07PRnw4NFqSI-tc_OIB9nAYYy40htX8y6dyBxgjcnmGbviBlTLrgAA89n-dh6s6tgNXrtm2Vcu1Ps_ACDFdMjtqYt5txMXEAPHDEgB1Y62-EzwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=ckqjO7sanocW_q8oYID9dyS9t63V3xfK53ASciq7Xw_r5-RnSxDXBp109GUjHrrEz0bI_X18gO_0dyrA4OUa2zxkxd71jfVraPAd_I1VdoBC0w4xsxcP6Gnf7oLcwCa2BtBv3zEcp6D-UGdczUH9nw1WZbRsmYUjT_KR07S9gOwKKQSe0NNs-B0UXHoiPvQB7Op8ZmP0IR5J-q7S0K3MWVlOhvY6IXhKw42lXiJzYnEvZh0U1Tr9PZgWxvR_tqjt77GXm2mNclpFBUfMY9fDZMAAMniiHJWO-GBYMk_yQI4AUoTiiEETGBOBwDC5at9wXSX7BACohQP3OjhBbKoOuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=ckqjO7sanocW_q8oYID9dyS9t63V3xfK53ASciq7Xw_r5-RnSxDXBp109GUjHrrEz0bI_X18gO_0dyrA4OUa2zxkxd71jfVraPAd_I1VdoBC0w4xsxcP6Gnf7oLcwCa2BtBv3zEcp6D-UGdczUH9nw1WZbRsmYUjT_KR07S9gOwKKQSe0NNs-B0UXHoiPvQB7Op8ZmP0IR5J-q7S0K3MWVlOhvY6IXhKw42lXiJzYnEvZh0U1Tr9PZgWxvR_tqjt77GXm2mNclpFBUfMY9fDZMAAMniiHJWO-GBYMk_yQI4AUoTiiEETGBOBwDC5at9wXSX7BACohQP3OjhBbKoOuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzfDmqs4_Hd2U61GRZ76_AHxeScRNEfdUG7rgR6530PgshBIcVTgOKL8HjDqoRi7SejZKtOqKPDYWBhNvHhxxB6pSG5Us-UNsNnfaYQGbC77_5zK4q_HMHzjfLJFDSUbuqu6UdMArSw6LJJgu-3-bKZDmc0mwfDipWwmBYaqpmenEY41y01ygTS6qzQ80z7sKnH9yoZOVTc-SQZbJKK38DncH5h7fu-Aq413fC9hLBlIJ6q37IsMSLN_J0z-VDv4-T2ZNKsZO1ndpmMb6WOI0GKKEGeHF2n-mH43CLRCLD_fpMF5EXwRTVTeWf05t0loOjBzEBJ1gctT_FZerHDIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jb49Lpx-93tPZPV6vxS_ugbW0p1m8hbvJyuxjJ-WMwSTvQV4X2RIS13jwnjQO8q4FOkHLcAAV2XJvz8XSQd1l1Y3FIS6sD5OH-8Dm_F52HEVi13lsMS6XmG22gKuC9f0WjVgNyrolhB53j7Qh2hr7YxZNH4fO91BY1RobAFqHx1Qs4124TIihAZ53bb8DnZDC00Nkn9UkELmK7oSkKHLFRR3ax09O1o6GYnVY2Ziv9pfE86IGELV9374mYwXQ5XzS5YRgSn1B2dQQ-gu66eNNZ0Rz4ZOLmjo5AzM7Rk5yklwc6SxsB8I25kWqWxjs1RvKKXxyDl5avMbCi0W9CErQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3-lSJL4Bsnux6HFkGdMUHrDeU_xOMLX0vHGFZ3ss2tHIodXH90d1A5eDRBvuFPAhqUWJingqXYyx2Ju_npRzbLIfga86os8u9Ae-bKmS08eRmnQaGLM4ACL9bvCa6-inA_zBKjKpdHO-uw8KkwhAHZ56jlqBvve7Z3_S0d_g0Om0nZMOAs7TM5BD3rpbrZqNCBRAy73OQB43apU5V-0TdgIr9J4QA1L3PLII6rmNTulvuy2GX-frKnabAs_MxTa0qpZbLn3ELZqwb7XxFkLBEWqPsMaMPwMECFSO0itF3Fvy-aK9Y1-nuxVFlFC4n8JmoladC1d-mVASSLJi2H4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=US4vTj_k1TvgTh2jNpaTdmZvVGsqygY7ZkI1vhkSqgWNSM-_I12wqnqwPlJDGqy4ZueqRVq1TebacjBouGTQMbmAMjViBPRTYTI36ry2g8TdeL4Zh2e_U2gCXhDStHG20ZC70qohDC1VbmZX7rV9HdxZI01qh_LAWxN562225yqHnaWAHietvyp-HlCDy-lALAMvlrWvhPro81wHb2-l7HPinzk16Rk5YydzPyop2T4nTv164R4q2j1o28wGAjH9Mwis22wOO4SqZ4WRJ0qjD9tOU7ak24BKv-xrQmbk2OFkYgdrysEcjCx1b3wqkvtuA6XceuH4VjPp7BgAlVpXCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=US4vTj_k1TvgTh2jNpaTdmZvVGsqygY7ZkI1vhkSqgWNSM-_I12wqnqwPlJDGqy4ZueqRVq1TebacjBouGTQMbmAMjViBPRTYTI36ry2g8TdeL4Zh2e_U2gCXhDStHG20ZC70qohDC1VbmZX7rV9HdxZI01qh_LAWxN562225yqHnaWAHietvyp-HlCDy-lALAMvlrWvhPro81wHb2-l7HPinzk16Rk5YydzPyop2T4nTv164R4q2j1o28wGAjH9Mwis22wOO4SqZ4WRJ0qjD9tOU7ak24BKv-xrQmbk2OFkYgdrysEcjCx1b3wqkvtuA6XceuH4VjPp7BgAlVpXCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjA7GbkAFHgaN820A2myjkGSvWTyJ0eJqRXQ4ql8hsCtnEI6tMiN97nL8dwvbSQmFS6OwmhzDAbZafIuAEIfmEgn914fC9VL8PBF0V_F-5MtWQozfFuk0BtdcJoYR7setJ_TN503sCOpH3Qb6NEc36gBliSJ0fsTFJccSbkcN2Z5FXWRJoEBAUT7IJyurMdXAdvxXV6u5MuDI8M5lrjpY3uetf5iMxvDk_2W8cFhqbyBKOLTI-kJ2QZ2T6Eyg7tmHZJe_Idntv7a2dU7eRepXZ9hSenINX9gGdaozLvDLFvg1JNolnDeI04OtehmWRJ5cVc63Y2ghbKVqlyy1r2BQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-zkHdVxU866yR_zD2nYDKPu-i5w3JT5ARz5nXYdTjvreBqEMlaD4_HTmlkuv3camTql9uGcHjqPBLR9AIOclh3WPanEHMFSbfnzHQDxc6Ne0u6zfc6E4nah92zmxtWJTAkvBGvPesk0f5GyyNZumOqzusybN5cONCNe7KUUDj_pV298P34vBlf9Ql5pSwkBE5CLQe0rHjBKc-NlC_wpRWHwWLcRh8-ze6T2dHevozDroQ2_cfBpu6raEb1EpdBlB3dxJ9lQ-cBAMlBvm22TtvsrIbGY9OSdGO5OUifSEteuLT8jK0wf6a7roVmWWPlpO2G-2XgHhIj1SKI1-_Migg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDlrSv0m4rpjpXAJtSHjOJbEH2gAvXP6eV2J-lYI1rmF5HiU9Ce3HSrx_tz_VkUfdpmKlwKM_2guMr5aA9KqtJYHPskzEK9jzS3MLShjfwWFWLzOZdAd092bhawbvUGortj-Z48gNr13evywTZxJSC4X9c8Jpw6m-O6kqYgoRyj7x7VkkKLQP6DdcR-vttpN--yAt2TtZ7yWhEfkuwBvOmG80yXnZ012VRdm4AvdeNpWRUDhTyH51e_8BjtoZDj2WpI5Lph0jVDf0kHc-pI5DYYc6r3uuxEcgaVbr-vm7eTOIFTcmCguw82lqO0ogLWlpY9iDXR4aOnNofEVvRxpQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKPDiOJy0biwqWYd9uV8TD-QhOuP2pZZv_1NXrpMZXQ1AGzgnIWovYiHAoQs4soMauZSwK98GHm4BZotOBQSlj_aQ7ae1hB2Yt51i14DbnGqwTEhvqpf_oJglHVkaQ4jbUvSbX-_fnR0nLDECzBkBzPexw8uNl1tLGLtSEgiBPhdkCkppS3e3zJOF6nk8AkxB-xBErfW7JabYNO2UX2hDuNhz5nlBRBH47hhUz2h1vz_0MD9G_VtUzv36jczbgy21tkVeznjQoixP-essSgQXnlMVc1Qh8bdbYMxCDwl5tcXyweZyj-KY3rIr6YztdQ_lAddMPrB3roXiYqcn4-lIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFC8JxUgc2oj4s55vj2l8d1Sk7UD3Xwyhz3x4w_dNyOwUXmgZfI73XWlTcyHwy0B0ZAjhphC5GAhtyPXSpLL9hCVSs_UvTgqUjdb2OogBKMh13C2xFXJRdHucHdx0_v1J3bBkt2-V7Fj0N4tgbSqhy1wQdk1zAp2vmhwfeStcqHkoFs-yWEAgBxgVEq4BH3UHgKNJE9TIc_miQWSdM4h12JqnpR8gm47ycekOiifIfz3d_IeLsFTxFX0otZWVSWsLBlyFjPSJ44su0E9ZpmHblS1DPqxXN45mLjBeZos8PfCKiOtUvCql5Afmtmf1Z2KkFh7rbfgL2DIMe5OkwBdJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=hxY4tZalmQ8J8w_wfzyZuuPNowSwa_fMv8lTVjPSfJSq3Eq12EukKjZPx666PQ3zhOvjsHb1-qKAnpCBJJa4U362kT3aAPjoABsksJAU-J6vDE2aA6PS55-mjX6UN4FbnKBKKBAxh1Wf4QNnQn_-ytgRJlHd4YhkSir3RQ_APZOG8Kn7EsbcGkx475HMitA2g9roAqKI-i1VGI6IxYrux-7w2SJsNqIOj2ALgkPnLsw0dZPpAv7R4I5bHiQlUOvV0SJ0RTqtzbKoxh4zrf8pKFUrgu9POPe67j9mfvSws1fsY7iabXg87ZgySYGlEoRka3tv4yQyQnhZtnMUlPo6Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=hxY4tZalmQ8J8w_wfzyZuuPNowSwa_fMv8lTVjPSfJSq3Eq12EukKjZPx666PQ3zhOvjsHb1-qKAnpCBJJa4U362kT3aAPjoABsksJAU-J6vDE2aA6PS55-mjX6UN4FbnKBKKBAxh1Wf4QNnQn_-ytgRJlHd4YhkSir3RQ_APZOG8Kn7EsbcGkx475HMitA2g9roAqKI-i1VGI6IxYrux-7w2SJsNqIOj2ALgkPnLsw0dZPpAv7R4I5bHiQlUOvV0SJ0RTqtzbKoxh4zrf8pKFUrgu9POPe67j9mfvSws1fsY7iabXg87ZgySYGlEoRka3tv4yQyQnhZtnMUlPo6Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=L3xiwGjJnMbk2VCKh3JXgXKFMTSRt2thdS2zhobLFxI7J40I4I11TNAIJid2HjrTedaX8F12rVxmwK6MNAeir88jbg87euMpMMIrH4rFaVvlEG5gcR-q4TG2VHXcdwJW_-6TPWnAQqHW6-edbyzSVvTo9t1uDJcq_5ZevfOh6WerVVTS7mwJI4FXt4V0OnnK4-5rwdPIkWU1zdMZhUaAmh1vcW24aXXEsbZMn6MFDU-XdcdjtCccgYJXwkUGkFIs1Nv3fJbeQipI2bgwZinwUHQO9yCMus1XkrMhcikWYWr49XhaUBFUL2qCo2evvNjlUWANETvxnEv_TL983HYbEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=L3xiwGjJnMbk2VCKh3JXgXKFMTSRt2thdS2zhobLFxI7J40I4I11TNAIJid2HjrTedaX8F12rVxmwK6MNAeir88jbg87euMpMMIrH4rFaVvlEG5gcR-q4TG2VHXcdwJW_-6TPWnAQqHW6-edbyzSVvTo9t1uDJcq_5ZevfOh6WerVVTS7mwJI4FXt4V0OnnK4-5rwdPIkWU1zdMZhUaAmh1vcW24aXXEsbZMn6MFDU-XdcdjtCccgYJXwkUGkFIs1Nv3fJbeQipI2bgwZinwUHQO9yCMus1XkrMhcikWYWr49XhaUBFUL2qCo2evvNjlUWANETvxnEv_TL983HYbEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=LbPFBUca7pmxQB_k2pxg8M4Iq7rolbuic8kIr__gvLcPluWReyWLd3Sul1w86q4udM0J610W0OF0-6APVrH2WeNG5Hj7H8GoR7Yn2pjMXks6UGGs2C4USLfeSUK_EEO7P7MJOhigXZpFigRk4KR_8Ecnjl9oqnaIlUTV4FPG71uxr3rqKOAFU2dMb0L_4PhP9tcnMj_0CXOCOLCQ7fuWd6DBckcnjeZXZe67R9LFuICHfUTP6uOtqzgfn5JS0sfweOC-RnhXqP1PvAaAkyrFWClVBiloOZp2OmCzsHP2xoCkgFaQ2znjiRiSWn1jz-jOc-f-8ox2Ftn8OctJNZiMxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=LbPFBUca7pmxQB_k2pxg8M4Iq7rolbuic8kIr__gvLcPluWReyWLd3Sul1w86q4udM0J610W0OF0-6APVrH2WeNG5Hj7H8GoR7Yn2pjMXks6UGGs2C4USLfeSUK_EEO7P7MJOhigXZpFigRk4KR_8Ecnjl9oqnaIlUTV4FPG71uxr3rqKOAFU2dMb0L_4PhP9tcnMj_0CXOCOLCQ7fuWd6DBckcnjeZXZe67R9LFuICHfUTP6uOtqzgfn5JS0sfweOC-RnhXqP1PvAaAkyrFWClVBiloOZp2OmCzsHP2xoCkgFaQ2znjiRiSWn1jz-jOc-f-8ox2Ftn8OctJNZiMxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛قرارداد محمد خلیفه دروازه‌بان 21 ساله جدید استقلال پنج‌ساله امضا شده است. باشگاه بزودی پوستر رونمایی از خلیفه رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVM7a367qWOSWJRYag3WV2ABU7OmzfWzkn-aVtcxhxIbMHDVGHLPA2hYLqEsFWQANsUhdxXW_iV0VFiOFvYTkH7rDUdDzt90hf5OlthhdgdHmrd0fExy4InOLqfeJlkDqX-dXoNeUtTXid6SgorT1Dux5NDaM8fprI79XRy_qSmKj_m4eUChOAgix1SM-7_SH_EzM4B5BjSY19IR6QaUiQwQc8oygz5yCRn_R25EmF_zGWXTxVyU3eWXSOUXLIyZA8rUax1hN2K2WxFC5yibKCM5hXnf3PVrTXrtEDi9vynk6E-rcNExCpZ-3QeggOeGTPZGIIflEjxjylxPOo1kjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zf0Hz1Bi0daUOyjvcuxDxDHd4S5S1jmqfbLvRA7HLkbsDW1KVpigbIN_AH7FgO9zzsBJC3ysMrqILhEOVD79gEQMS6YTlRwBv1NGmMza59R-RcZIgwWeZibtly6p30-Y7-Z7MUdtkRRG9lRsbn6jo-pmefYgEJDWJvbkwYvfLrGTdgu7_pTS4iWnoI05jRIzu1Lkjj5z2G4ubPKtcEQpXZdb-FeDDUAMYoGZ0kNuLS8pjruyRTnRHgHo816fUo2_iWkjkKVq70OBC0YiEQE2yYz4BsAak84rV3otCSgIUgjd6hRNGOwKepVij6Gnivvlqaq_rckItK2ccQg1JTmQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvMmEWldJQOsEju5o3Mzy37GNnP0CnOY7dGr01VgC1e3XoHrwPdFfNABjHGmAd5DcNcrpaHldoyJcTtxhD-7gD8nTEbngeNJBQhEgLdhgaDaNKtFbi0S87FRxYncIJ4_0t2dK9FU8V6B6X1ThNJYfh5-8zAywuRSlqKCqO31frL0wY9zLAdBhCkmGD5Tl1vxAQdzZYzIYDv2Lpsn5YDHWIozEvQevKScRYngwzoq5pm0_XhaNmASnJxEvPgzPvZQkJKpvWp65LTNAc5j8ye0gapFpGPHLPWjUUjw-bK7itvie4WzPolBDrmZbDu__nCyWuADYEk2m5MaIeqVljfkUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJPBmY8zf3487_uHfJkEzyKgwWdFL3OlftZpVoGQqXA2oYeDiuroz3gsgWf791VaVRL8j4B4E5wqQf-wepTz_yUI7O1qD4CJtOnvlTx0297d_Y--IVAIfbz3MtILKb2Y7c-4FffKIo-_wxPQwS4T1ziAq-uJm3OhiYCyJB-JiAWaHaqnA796upDLll0bMSWBHkp1GDt1kMoj3-aDi07pgprgnxkqqpPsQ-Ozp24O5v866yk-eWTf2GvG_3oo1sN1x15sYxcex9h-MitqqwhNfNzd_xdAXDCNPJioaVZbowIjUNQHT9UCP1cvOA2jBp8JcCQVte16Xnnir0VFiLRgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipdoJ1qT9j1anjIq5Mh8TZX9ywAJV_LpAXuJ5ooasVsW9z1USYmC1eFAkGS3ccKbZEZVNTYRJj_HAUgLHfKLeGchw9URRYQrsqcZ-ZSuMxTMx1c9fBJe-z9ezzzxPr2_vPII1afpm74jXC3EYo7qPpMZ-Jv2SEyKzUSLZPjo0rhZP5_jzRrSldZy6c_JzTFc2DDrhmf1cLydZcQkVTVt6XfoX_Ss3-j3KK-FDrD2hC68X_cBlAvAGcvzFi3YptrbomGzE7QDlXJDjDAnZNH1AAIEmH2W3LuOQjsavF4tEPw7h7NF8iBhbBnGLjDenHgZ-0L61W1wbg6yxFH3nBF0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCjer6UwfCtAGEZ2cEMO9K-KpR7APMGBSFK9FCU7Iwc1ckJfgyhaObr-8yn6bjl5ywmp_E2xUSMldWhtcrY-JGjctPU2RGEL3zP75H5QH9HADcCOhYVsTifdPgQD8w2koiQmqp0jQLUvh7tMxbnRlMWzF1RWeCRWko_9Gq9-kthR8jQ6gO_v8_OOb2dqAayVEax4jokr5p8josUBBwVvENZ6NTbKxONwiIkH88pUiIYtPVkZs38wzGiN8TbUoz7OT0TBEb3VPX_EoRxxYCvJimemLRlHlTbppsh4SCucgH-O1SiMlHPEpa6wgbySX6ROaShbdynWVzhtOGX6pRsOkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmby3fYf4GpV1qhxQNLeyvaNPuPSJ9WITMTJ-j79JxJvVpxtZ6DYh2OGWZIXfm5OEsntuOWbsYqD_Un2Fehormh4UqVRjR0fGardVQJrsyLfN8Qoz9UYP82tw3G87CQPkG5p2mSTYSf9Xi3V6DGwGjXp-EQoTqX0I00h32-wtBKT5ujMLVAsSeVwL6ruBxH7BgVhVlw8LZO8hFjFXGn-rFFrPAm7Qa2e5afo_jcaImcf-QWKm_wPguj2G7nnta4iaVCyyfZWp6hDbD8g0U1A5_-_06DAsfc9VgsRJx4oSNrUuib2FasgJkEUINd7_rhCSzP3f-evscN7yek5qbQhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG8lRytEGHZ_K_crxoF_S656IJvZPBRiNmCTwr5gFKd3BSMj7SQ3Ef5JkI7Ec89cBknHDO5iGRQljjN1nI0kVvkdeYd0H4uOVieH_rhAMPYoZu3ZXEiP1iPjkLLyLYFHp_7_M44S2uU8nUkB2yPB_JxaC74nO1w2n0CWdgg73QNoSXGKenFR1hWGTf8RA2DR2U9IiU5sEKbzKmjn3tu6Kx6JazClum6BNicZZgxEPhXXdcVFqS6Pg48az0X8nbwR3X6u63ojHNJZ6k_-ZzrYaKB9VEPp5SEPdbGS0AALRXkkvgjIyKiPK4xA0tblCyMP565Oa2l68i5WCwrmzU8iyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26213">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Noz2WIsVBT8UlRY0YNSHCfjqL-eG5Uq-zQ0Vr46Vmoc1RLinkqr_F3XYNM9e3WrnjVhFqjptnGTjg-HIz8NZb2nMQQLlkTSDFkfO2rtZ9K1eCNx20_HkAZ_eN-tBfyxSoM7rvKSUSeiyyo3BgEU6w1xvISfgVBZfTC8pMvu_lpyox3iMNeAzSbokj8IiJLkLZ1DBm5CJPYlr6tz53fe12X5z0wakU2-2iXWp1jq23_EjqSYm1OH276YPe4NXtZjt9nX4ACmto-whVTYW2lcICwteTHftS3_6MAr6woZ12F00Rh9NYBWkgVq8V95FRfU8q3sxaiZ4MJQIWyvVky0mkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26213" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26212">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY9i2n_eEo_2w0X0yi9_uBCIq2bGcW_wTkr3RtufEXWxZXX2jRjTbYUi2H_0r9q6ju4DRfflGAMKFt_k4SJu-6ypfnvwRpn2bL6E5R2HcaBSBNAO9qt0zO14mEi2JFjRhTUPICUlplwuKpCUYM0PS8OyaFBFEe47MqFdC5vbq8bAq7OdIOBqQAjIvu_APQ3W3ZJeJ8CenUfMlvia6Ovy1ToVKSGmXsKQ4JV_yo3vbl1Y0pyfGPwNjXNoWNtY_qYD59ePwG3q4pMlIet58HEHvKJ8Bc7end56uLnAOiqGYtl-ADF-Dnc9nyuHB5dwEPCI_P5QfomnL28BCoUSycAaHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26212" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26211">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pk5EylajZqgSkeocx_IOTE9R2pRwEt5hR6YuuleOFcM9UGWoMTTM9bj7t1qtFj5-AdyWXsWAS7CTz-eng4EtK8qsGrgw6C7E3WiRgQ-IoFjdhG8v6cKCcsZdmz3zZapwxw61f-PbUf9SFZY8PXVzdXD67ey4DnqLv2DNdMf82KhDtzapLIkuPz28M8L6lFGD3p6S5aJOm7X4htuqVIW0IqVtYByrYs3hNmsnVm29bXClN31OjQPL6WJScJwGWvC0_cC_KbT5BvTDPp_C6NwQxvwip92bFX7luVLIcBuqXRpOmI4S8bWCliAkIznxjvkC1br_JlnLC147J8lhFoO06A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26211" target="_blank">📅 14:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26210">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aX6q4PPlW2IyeMLEwrUB2guCEARKU00znTLc6nsn5efWB-VvTaOLjk41AGAgqZvRWdk4mwNRmctZGEbFiZtr7JSkIvuDGpmvvXovW8LZKXUhpFZwmqHL_AUZrHm7w2DEtYZcEKQLqqla0R4q9fEGl2qGvSO8zyHXO-2hPvYeocTes7VXlq7EFdP9Tx5dv9lkCYNT9DzJeJeSFx9cYlMgaKdggrun5PMWNBs91jGG3cK3FzZVj-4QX55vmkwdzw0wyyNLzC1BTjQI0wdHwj0FZb7eogwZ6Zo6oDSOTUi4mlWIFrlG_VFB5-gW4C6M4eTWZIMWUM9SrqeOPRnUT_AvBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26210" target="_blank">📅 13:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgLUe7SXwCb2Bj7oAFMkpzIeDcFAMQeYp0ihe_4LAgp4MWgRFcsLlpPDbjBxRvmeLUCFbbFdN0PxDMcqGOh-YxjDdQweHJC7xSxg8VlrL2yzputBLJ70yeTRdj5LaIQdHJoSbuXVuklODmJtiFmvOTrZeXCOqKgxjO_IPpjPJi1PYjxE13XQxT1iYODpVsQm1caQ2_ClB7z-VsvM73S_tvicRLu-hO_2Ho-RSbMgluOOVIeEOOGiKE7qpyaDPlfGNF2TDwCDIZMkhPjRWKMh4U7S_f6-HP3YdP64ElNfJj84al8-Ac0E49WD33dJ1JMldenwaXN11lQY5NB9KnZc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری
؛
رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26209" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26208">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsthxkADAwFt2nx2HLJz7s5VSjkW9ZR5xY23OTq4f-BEonp1yc6KK7rUNFEot8ZX-1xGsJQsJVoL7YIkeTGnA42AFpp4cBD-iccjlz8gBuP5iG3UNse-fPBcBlgyCdcw8qCaZowsVRykFDWBOnodLA3rsw70VLrPAmax1LWp4FbGXj5U8l34eXzjbGNHLKpW1O8gBxC61QUkgYRNSsFPRoXJbhJfP6fOMn5Yn1QFKSK-PtuAP9UMCSt7AYLaAdrzJMDc22-VJWuIVGixxU_L5NvtppEPNaR-raMpvIiR6M9JDGZ4QmvCpTG1XPCT6nme0D4QxM675NMdO08C0LuS-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AW0pWkqF_s3amJf2q9aWUUD2K5onJ3sg5ol4WBnbiJd09mVn4NPTAeFTOR_gszEgcd3osqObIYVdbc_hmrgLTah2eGv3dNUCmprkVB0XDggUhZwEZ0t1b25UqQKlFGqz8HBhotG0jXKP7kKzeXrBgqVuXlWznIH4h6VF9s1fPe0WDrDq4Ad5l_h86eLv0Ev10L9QxTLcXei-gPMKIFxKE4wpNmfqNngZbJV2Dq7J_pFh-ecavAT0raoznWfYSKyRbm_rrqsWCcOPOHZ8NjLLvWQ4kBPRSosGpIjPiZ9cO3fjP0hxlkdsHvUuJy7Yh2XEMluUIT1qw0qrvyNRISYvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26206">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOhNM-JdRgjvXz8yJ0UfaSBKdNPvOUoj98ckMG--Cp98Op6mffiZrOyEfSinWx7Eefv14RHCBm6cDvn8EjKsyV_UV2uxPmQzGtaZTGp_aOwmkT48UFGdXpsGceyRu2IIAEEZrl8H1272F3cy45g4PQ0WRMHHddeGDySfpN2CdxpIf_C5-sl_HxTW_wH4RXRd5GIpLjEiUzMX_1cCpTRGqQxh_C1vAw-AnmcV83jZSAmj_fdctRE0GotfhwdCM-RmrLWX8vxHbp11zW94NyZh9yTShR-5eiDh3yNTUDsSs0ICcGF2EhKPhENnm6zEve6II8T7_SotSDuZmxi1wal8lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26206" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26205">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFIuMoLB-L6GZLI8lTGx6BeNqgRY9z9l92xQ5A3AgM2CD-oGEZulhzWAigyf0AluuZvtKMi_D19xS6PaWZf-JN69QsxOjpOiKml_fddfROdCTRlv9rXq-lCA4yB9Im_t5qbixJ8nxVkoNwW1yhyYHxY4JEDPtuHMNUFPW7j-pBnLClosIzo3QWJz96prM-GhL99yvm2lkDyXII1intgj--WfONkxGBIWOByDciZM1d_66YhHfUL_BSID_zdNUOKuZjVIracOU4soHJaa9ngi-zOVrq8QyHYSTePJXgSdaqXd9gCKudBHndCMfwZHgBIcci3tl94gwv_R3ewet__ghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26205" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26204">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">▶️
هایلایتی‌ازعملکرد بهرام‌گودرزی مدافع‌چپ جدید تیم استقلال در فصل گذشته رقابت‌ های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26204" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26203">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfxeeR0x79iPnkZfBDi5zKf0dS95eC6IpSVwFKI0Q54tF4XAmglZ3TX8B-c8K8Y9zJQFOuWXFaydvOysYJzqER_Yxb_9sSB6fkNU59pmfgh2ngY2H9rHDvvhCStLVljFz6kSaHdhjFqpYT2c_hmNYpEUQwyk4YAmbOfMcKE84VioJHqXBGhR3eCcyxNRd8xpRXG29RaIrBdcoL3o7tZfREkKqlI6fAGDMvn4OdyJjca46MYGaDW7KOGGyRaZDEyTInZPIOw2Lnh91LMI-bmK9cIwoINnywzxU0GIIrSt6xi524w4SJ5ub20npyOkMX8vfmZMtn7fuPScBvuAt-ewyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26203" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26202">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=Omp-9lXliAjtg2ZwcCMJ5O9s7MzKPrGX0uNsH8ildC_ryDbBJjWFmWf3Ax_hMB3D_Z7c1a_MfePLwXf2iv10boKrOMixzjkAf1QI5vM0XM8QvGHayAsxJAzEZqqPmKtnWAwVVrBF7H6pCJwxUMAeiB0UlMiLZ8f0a9xbhPVZp9CxmH2M7UIaq8ginFnaFpaDvEA82BJYcL6DCjcEOeqEJyVoRVU8MQxdaUEg4GINb5oPRiXcPX96M3U-cUtXphmpLq2NPL0t6EGqk8CthfF5jBz-xdCIPYkdPAVRl-8iIsaJvyxAOYredfWkUWzmK1My33HoFHLU3-SVBCdOpTy5dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=Omp-9lXliAjtg2ZwcCMJ5O9s7MzKPrGX0uNsH8ildC_ryDbBJjWFmWf3Ax_hMB3D_Z7c1a_MfePLwXf2iv10boKrOMixzjkAf1QI5vM0XM8QvGHayAsxJAzEZqqPmKtnWAwVVrBF7H6pCJwxUMAeiB0UlMiLZ8f0a9xbhPVZp9CxmH2M7UIaq8ginFnaFpaDvEA82BJYcL6DCjcEOeqEJyVoRVU8MQxdaUEg4GINb5oPRiXcPX96M3U-cUtXphmpLq2NPL0t6EGqk8CthfF5jBz-xdCIPYkdPAVRl-8iIsaJvyxAOYredfWkUWzmK1My33HoFHLU3-SVBCdOpTy5dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26202" target="_blank">📅 11:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2K4hWzHQ7aEQRbydt6zGh-CKU37msqgMbboU6GvxdltsQ2IfmK17PCOu347Ldj9N0Pfs1JUcsTMrsXoBvLQdITJ82V8APiYiNRDgXK7s7914qZvZtii8toZJX3cYeyjE9eU_q0N3fFzAjaI-3XSXXGXgjWxB8DxYQrWkEY76i54oj7OlKFFhGSjosMtimm2rNTq0gVnZAOfhSdxj7bvun0EYQAshUYjo5nOBnBPBL9WZIYq4avK2p73qxfrChg-YuD3afenMzDOwjaftil6Yh-ke1br-fWG88p_e7XY8EpTP_Emjgu_Nl9KHP4tsvTIOWgULs-qjPJQV3LHLWn99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yvd294LcIa9NpkHHYdbqo5u6sqmwbh1ezNzFuUciZ9_ri9Fnk2bjgTVReTYMEFE5j6fHk-pxHyd02GbzONiU1p3udHAau_sSkhGeJpmwzjZeSQdbdC8yfs8QBQKq0SxgINEfwe1swzHLYRTIjAtelxyQRevwiMU1vgOKCnAtbyuWBtGHytrGWP84_YeuUmhufX4ZFk_YkkzsBmDJa8rLiks_sAtN89Qo1fKfNdyk_HqPTE6SjoZ-8rtWIAQWzVvU-e3gVqpd7w3fSFSaMYH1cZwB_AtMeHB6WvaZba5sbwnJizt4_iWCvLzHwsuNB_V32nGZsEfdNXdb6QgxtisMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26199">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGLHQFSJ0FmwkKehej5qVGOBd7pYZmf729QBGoX6HEOshZtENJckXVJqr8fnpuJp1unUvn8uRwgEuVNdep0-3RIWq9aeXFnhYZvQo7vt7yDsZ_lLVu7YuDndt6p-BpFrckPSVDpIlr_Xt5J_4sAOJeHhE6GZQcVVmOx6yH_dgcWSPcuCzugBBtC5p0jEd3gctHGXcbfpW8r8JzAv6EgfKfFLiaBsD4RkWoo6gfNuLcaYJqhUhdPTN23-MMgPrgncu0RFXS9NJcaqzsbUqG_-OszQzBW53RWvW9cpx3YygJ5ubyUDm1X2CNg5eHtYVTwrarOCpOxGdve_RJ7DhHaDzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛
لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26199" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26198">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=BoalYiH23FmEYTjTTLMuPltd74RSaKwo1G2C2JZvZdti7nx1wjkuLUooFb-YKWVH5HoL00Hzbo9RwY81jUfMDFFi_jA0aoxVrv27ulqEC6-X_2qxwe65mjUq7Sql0CnoB0KQFvAb5e0KtjCfKX4wUsM8dU_wBn9F1ygEPFVcUzyfDuYEnbfmixmP5VlcsW8W0ibCpgtC8bD1961znKpfEbxpk8SgJilgADQjsfekBAyZ7SsA0DSBqCJ_k1aZ6XjQV-GIUWKB6MFNbAe26oFqu4FApeTr9_-OAiJcLaYuUiNEvxPcV4cLJLuYy9Tb9cZTlzNqez7Kl_VNkfW7Zv0c8lEYaJNZFTHdNgngIXi_nomWoYE_22U_rPOB9ubAjQrswibvzV5Q1_nenCS8n-0Hi1x0-Ik-ThTD7fpD6p9Fij37Akbda6iWSFBnwOiM0e0IJQIQPCK2bDcgYEe8MGvE7zT_nSrRtc1s6mbASmO0m64kHCIn7Wr74XTwHzVvqO3gVj7uMSEMeXJ3Vud6WvSq8ICsOw6xM5_fXue-t6uvwvMIVItn_vuHr7RHhv3Kh5-z96P2j3Rlhwll7jm033yF268I6i9m_4dV7ZaWvR9GUb36v8RiXsllB9uwfHwbzHQUdBRCFs9Yf42PiMI2RgWDZmYu24SFWmw59EymnRcpBcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=BoalYiH23FmEYTjTTLMuPltd74RSaKwo1G2C2JZvZdti7nx1wjkuLUooFb-YKWVH5HoL00Hzbo9RwY81jUfMDFFi_jA0aoxVrv27ulqEC6-X_2qxwe65mjUq7Sql0CnoB0KQFvAb5e0KtjCfKX4wUsM8dU_wBn9F1ygEPFVcUzyfDuYEnbfmixmP5VlcsW8W0ibCpgtC8bD1961znKpfEbxpk8SgJilgADQjsfekBAyZ7SsA0DSBqCJ_k1aZ6XjQV-GIUWKB6MFNbAe26oFqu4FApeTr9_-OAiJcLaYuUiNEvxPcV4cLJLuYy9Tb9cZTlzNqez7Kl_VNkfW7Zv0c8lEYaJNZFTHdNgngIXi_nomWoYE_22U_rPOB9ubAjQrswibvzV5Q1_nenCS8n-0Hi1x0-Ik-ThTD7fpD6p9Fij37Akbda6iWSFBnwOiM0e0IJQIQPCK2bDcgYEe8MGvE7zT_nSrRtc1s6mbASmO0m64kHCIn7Wr74XTwHzVvqO3gVj7uMSEMeXJ3Vud6WvSq8ICsOw6xM5_fXue-t6uvwvMIVItn_vuHr7RHhv3Kh5-z96P2j3Rlhwll7jm033yF268I6i9m_4dV7ZaWvR9GUb36v8RiXsllB9uwfHwbzHQUdBRCFs9Yf42PiMI2RgWDZmYu24SFWmw59EymnRcpBcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
این‌بخش‌از گفتگو عادل و علی آقا دایی و کریم خان باقری در هفته گذشته بیشترین بازخورد رو در فضای‌مجازی‌داشته‌وحدود 50 میلیون ویو خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26198" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26196">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNjBjuxYz26vVkCmPNI1H_G98xLv3L-kyuwHhUwoiPylzfv2da4LNKo-fVv12CQPH7UJqnRxjgfBaONG-DXs1jXbJ8mlmS2W7X9Dc2iMIvoFqrwCy-aFD3vSLmcr_wnVK5jCLdEn1mDfA61u_ws1yF6Nzluso6YWOLsP4D4OqyT5Dla43wqGiaizKS7Y_nvf61it5VFZi31YlKn4jDRBh3rp5DvlPl5L0bo8q8KV4kr6pHtpQiCc4WJWHy8xhAnyNfKaAGmD9zIK1xx1hFqhtczxoV_jaZITGzV7J_-fQQUP7sdy72lO5e-D5-RqM0hvmd39GqHZac3s85T5nNfsIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسه دست مجری صداوسیما؛ تیکه‌ سنگین رضا جاودانی به میثاقی در گفتگو شب گذشته با عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26196" target="_blank">📅 10:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26195">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoOs889M7eIoVBcnI01ZZf3By6aEIsgRDgpZ_v0eyqKWZjN-ujw58Cc1Lz0yipNPPoLI_fR5_Assrx4cB50X8BwMrsEbdPLqw9GbFUJNWUMM1IuLX407UOYbBAtG0FrqY6ERSWZeKawT6fwz4DclcFYj_rKhubHW6jUhYjPjDm9uFQDi3tQD7sMHBaT0KJFcWXqiYlqWU5rbIYfOweh-L2QBc_N8gX1Vau3IYC3xYOdbI-k_CiYFkdCM5iDMSqfKrEADVEovz_xaQFlWHE-t78EZB0fRu9nvRrZ6w8jlGPZo5nohlnHNFy6eYNhwajGcs5t76ARtJDOrWABKaom-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26195" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26193">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=PnDbwK0lKXShbSSTTukXO3iPmjG5FFadn4MR_e-IVh904PPxuSsHY8bfvCTLIjCBmGbaY4c6hUEnpKrl81AbSCI1vUfTlpH3tLz8wbGmQ7Vw6qSDgIZEcExEd1mCyb96swRSwkTomPdGriFSUmYMu3voY9w_vddEBbzS2GQLar26WFaYqtuMrJB3ufO50PzkFM-X-58FQjd4tofjRmHGxfekouiEZp38A4ZRqiGE3D996AgZew1rQoHxUOzx3amZ3gGawxAJ3OmGlY3g1rNvX-XHQj8eZDb1AOAMnmW8ADQMoIuylUBS-s0pWKWsA5VEaxZHPfeeRug9ozk1x-cgQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=PnDbwK0lKXShbSSTTukXO3iPmjG5FFadn4MR_e-IVh904PPxuSsHY8bfvCTLIjCBmGbaY4c6hUEnpKrl81AbSCI1vUfTlpH3tLz8wbGmQ7Vw6qSDgIZEcExEd1mCyb96swRSwkTomPdGriFSUmYMu3voY9w_vddEBbzS2GQLar26WFaYqtuMrJB3ufO50PzkFM-X-58FQjd4tofjRmHGxfekouiEZp38A4ZRqiGE3D996AgZew1rQoHxUOzx3amZ3gGawxAJ3OmGlY3g1rNvX-XHQj8eZDb1AOAMnmW8ADQMoIuylUBS-s0pWKWsA5VEaxZHPfeeRug9ozk1x-cgQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26193" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26192">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=nR32VVzgCuHFqxyiTvzVWcu4HDyG-t5_eTMmWyoAQxsf30u6Srqa89Ar0LndjTCuP8SjNt4vcvQHTu02PCscnbr7LejZxNEBvVuXRLnGHiJJ1h6i6UIZ6f-eG_i1APmrI7tpQZU0K5eVInDTb9dl8DtS4j059tGyyxoR2N2XKoG1SlFuvQp_czc5ciKjri9_TRh8iwyqAMo2Xh-TjF-OKE5bYsWhO8Fp2nSK3QPsEoTIzY92SJiKUg6WXJh7wP9uq_ibDSzaGHvQQaZPLSndb9ji9CQvbojV5XeVwat8r-qONyXwxPRtkuJ2txCkwy-l3a4lTb4523fJLhA6Y9hJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=nR32VVzgCuHFqxyiTvzVWcu4HDyG-t5_eTMmWyoAQxsf30u6Srqa89Ar0LndjTCuP8SjNt4vcvQHTu02PCscnbr7LejZxNEBvVuXRLnGHiJJ1h6i6UIZ6f-eG_i1APmrI7tpQZU0K5eVInDTb9dl8DtS4j059tGyyxoR2N2XKoG1SlFuvQp_czc5ciKjri9_TRh8iwyqAMo2Xh-TjF-OKE5bYsWhO8Fp2nSK3QPsEoTIzY92SJiKUg6WXJh7wP9uq_ibDSzaGHvQQaZPLSndb9ji9CQvbojV5XeVwat8r-qONyXwxPRtkuJ2txCkwy-l3a4lTb4523fJLhA6Y9hJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26192" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26191">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=m22QDRJaVR2-42_oUELnwzeclEEyFNEZBDYdqqgUBAuYTcTcL8sP_NXKUsvT0l_RVLG5nIFGcVirh1qVn2hEYa_ZHiEsW_3FdZMpLv3s3wpT_Q9eIR_FNC_FVYRQfumpN5aGHOG_dCzsXMIqxjnGmvdg9p-0s9VZdOw5hn3I52XkUV3j30ZzJ0np5OBU0u-ilg0Q4hHuiMu92u0cLsZgsxDw_9MtW466iLORh5sABJUF9V0dko-mMZ0thjR8wgjo_mcbVhnXtbCR_Y-Z1oET_NCx4XoLZcescfAVF3hS-RBqLwsNtYAtNm6nRIoVpsutumfAK4d4b55RniH9uf__Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=m22QDRJaVR2-42_oUELnwzeclEEyFNEZBDYdqqgUBAuYTcTcL8sP_NXKUsvT0l_RVLG5nIFGcVirh1qVn2hEYa_ZHiEsW_3FdZMpLv3s3wpT_Q9eIR_FNC_FVYRQfumpN5aGHOG_dCzsXMIqxjnGmvdg9p-0s9VZdOw5hn3I52XkUV3j30ZzJ0np5OBU0u-ilg0Q4hHuiMu92u0cLsZgsxDw_9MtW466iLORh5sABJUF9V0dko-mMZ0thjR8wgjo_mcbVhnXtbCR_Y-Z1oET_NCx4XoLZcescfAVF3hS-RBqLwsNtYAtNm6nRIoVpsutumfAK4d4b55RniH9uf__Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26191" target="_blank">📅 08:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26190">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeF-sQH6AgbGBnyL2mrZQyYU5_Bmsm0X5_lmnli7CvzUFAonkd4h6zQsCMtbLeGywwcO-W4Gf_eOqZ4XvYAsJuq6cAUZxAXRZVJwatHpdH-Wjh2aI2n4IMMRgObfXZ9uFArXaSberO0ZbMudHSbnkpQ2R45zwHbwlL17jWLcg7ixaI4qyTzZqLzR4pRgUDq6SoSbTEzl4NjOVZWb2Fly0Yxd8tsiwAXHVLSS3c_-vm0N0UDVB5d-ilP2CV2qnWbS2ZJQp9KaYqDIP4VHmP7ZYkPHKvV4HAhlHfxqUsOIPTSd0uBJnfj7m3c27WXtObYNQBLBwZc-MeeG4v3pozZ48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26190" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26189">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRV8ROdBB0abROzZWrl8nWDSKzZnEFhRFbmQwYU1mc16bTvAeGMuMkPo2xBoZcEruCNsXLAefcoZWLRRXxmxdXgrDpeK0c-Cbn4jUhqfRsRsst4wlwGgUNEHLiwggx2jSpKDnhwtfUvEnSUwGRA8L45L5RnVOEe_KI5NXgWpw-vRUxs_fNmVd41rR_sNK3ddd1y99_TjQkK-NmIAeU7vK3bX366OJ4RYZ9JlYGAoZQxfH0H7UAXLt5-ocOIo78-pahtAn3hJfmCXSlKz2iQoCiMIEJDDl-O5f2IHFtpXR_hsD0UlLFaVbmo7YF8U-NfoFDAD1eKo-FppGU5gE-RBmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26189" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26188">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=RbskgRAqyuKfa5FhCPfLNWLevGKpbs8ub5TxCldMhs7OAX7p3xTGlJRbqeEz7mVMRNA-1-I1Dhcsj83sS7HcbIsTvXg6a8SZjLkywWMv3_06MY830Knpr2yMFsDei6uFM20wqRDUdjZZxGMvpDdFFyrvayrDSbUJ87hS9jnBqsDWl8Z1NybEFvAl5Ee4UCeIzZE5vJnka60DpbQL0CbdnIqbuqL0aa148Rdl-0wWDrTqteW2GoZfcgMWQYMgdUl5i2vX82izM1YjFmiwALHZdlYnxC_dFoiFXhnL49w7UoAPrjKd90VH9ssArCZLbHxXxWQ83Uocv3eFkjawMUiaHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=RbskgRAqyuKfa5FhCPfLNWLevGKpbs8ub5TxCldMhs7OAX7p3xTGlJRbqeEz7mVMRNA-1-I1Dhcsj83sS7HcbIsTvXg6a8SZjLkywWMv3_06MY830Knpr2yMFsDei6uFM20wqRDUdjZZxGMvpDdFFyrvayrDSbUJ87hS9jnBqsDWl8Z1NybEFvAl5Ee4UCeIzZE5vJnka60DpbQL0CbdnIqbuqL0aa148Rdl-0wWDrTqteW2GoZfcgMWQYMgdUl5i2vX82izM1YjFmiwALHZdlYnxC_dFoiFXhnL49w7UoAPrjKd90VH9ssArCZLbHxXxWQ83Uocv3eFkjawMUiaHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بغض‌عادل‌ازصحبت‌های حاج‌ رضایی بعداز توهین های بیشرمانه امیرقلعه‌نویی و فیلتر شدن پلتفرم ۳۶۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/persiana_Soccer/26188" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26187">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=MKsH2RzTbwNMQjHlfnWOmaS3Um9-dlrSFu7BO3AO6GBV7k-WTOyOQhb8SOhCX5boBP0fUmaE5mcJaJJPIOl-e1XMkMSpWgOIATToRf2j_JawuH_13EIn-QTLaz8bA5xV9h7JG6zJbshkCbBrCWNNDmRu7hVV_HHXdM0H5thWvEAHV3TBhuRMa7Vm-amryoTxATRMnpgOW38vBbDxsPVBbiD6EbYEFj5f9LpMuRaWJX9d1tpRMCiztX5bbCOmuQhB5DKWTz_P1t_XdOWslp2BkWM5M2SxVysBi1vUTgiHmkTvEPuCh2YiAHHv4J-Ve6q0ONmZlE6A5xzRECBevA7jw7qfBIn_Cggeac8Gro2H1rjf6x_vfuoMhgrTINFowD76GKqrKEOzEvc509sthoy3XQJvRam0VLYnXJsfoorjyBJc0Fn5myerdcNcBuAUK_qNwZj2VGb3d4gY911Zwo46McYQ5jfEySHLuutw8NgMw349U_w3bFyAa6WMITPHeW8iVr5LyX3B77Y4ZVtresrwHew4hPBZL83trz9SvsyKeodWnfJUx5V5zOcxxRqWCC9YWFifeUpnsOhgydvB-hNp60LHYXh1baNdQi3j0Yp95lAmOsAgy1-yZXkhApdThUtes0NdyJm_q1FoouA404TD8FE9PbxGoa5J4LVjfLNJMIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=MKsH2RzTbwNMQjHlfnWOmaS3Um9-dlrSFu7BO3AO6GBV7k-WTOyOQhb8SOhCX5boBP0fUmaE5mcJaJJPIOl-e1XMkMSpWgOIATToRf2j_JawuH_13EIn-QTLaz8bA5xV9h7JG6zJbshkCbBrCWNNDmRu7hVV_HHXdM0H5thWvEAHV3TBhuRMa7Vm-amryoTxATRMnpgOW38vBbDxsPVBbiD6EbYEFj5f9LpMuRaWJX9d1tpRMCiztX5bbCOmuQhB5DKWTz_P1t_XdOWslp2BkWM5M2SxVysBi1vUTgiHmkTvEPuCh2YiAHHv4J-Ve6q0ONmZlE6A5xzRECBevA7jw7qfBIn_Cggeac8Gro2H1rjf6x_vfuoMhgrTINFowD76GKqrKEOzEvc509sthoy3XQJvRam0VLYnXJsfoorjyBJc0Fn5myerdcNcBuAUK_qNwZj2VGb3d4gY911Zwo46McYQ5jfEySHLuutw8NgMw349U_w3bFyAa6WMITPHeW8iVr5LyX3B77Y4ZVtresrwHew4hPBZL83trz9SvsyKeodWnfJUx5V5zOcxxRqWCC9YWFifeUpnsOhgydvB-hNp60LHYXh1baNdQi3j0Yp95lAmOsAgy1-yZXkhApdThUtes0NdyJm_q1FoouA404TD8FE9PbxGoa5J4LVjfLNJMIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اشک‌های تلخ عادل خان درویژه برنامه امشب؛ مردی که پیشنهادهای وسوسه‌انگیز رسانه‌های ایرانی اون آب رو بدون فکر کردن رد میکنه حقش این نوع برخورد از سوی مسئولان دولت نیست واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/26187" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26186">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8srvds-Fa7rqs2SyDzZLoMTWkPW5MAF_wwMwXCIcWvxxIajDTKpflSPVyEHF3mo5GRcjxh8xo4RhOBeBR3WNB1Czegy_JlMzqjgipbEbHtNNZVT-Tb1N_0SWo4cUyzmihBqz6KMKhErqcpGd48G428JL3v9ga41IRfGhdJN509_yV6o1Cl43ZWoAkSFkwocASh8uSIT_xFKefwwAGKvxqwYIl6hxS98LizymRenyCanUR6fBNlqaj6kQfuuHLNxh-hFlZYuyZf69g4vjl_PD7yXl2-GFQrjGIC_HtspoeN0oUi_yBvG_LgfKg7UvxWygsVr4PBn1vI_CMjF6w7nBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26186" target="_blank">📅 01:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26185">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=rXsWVjAqMHLKaD4FCGve-LTaTkiHAO4laKpvT-cnta1Hn8pS_oXpqjV7HTI5Hp_L9b-ooKqJ1UC7LU10RRah2zGv4C_NauZ7GSNvdy66_IGlb8Cf_P5wWV_2rQqXL9iADABmd9xQPLClyJ-hZIcyWLYBV0Q5jDJ9VWuPzay8gfBb2vV1vgakBXyxXWvXA7luHAUgFTwq1nJEYZBHNnuMwMUESIL_t5glkYrjZvQEtyG7WE2_ml4y2L3BxUMqZTC3q0L0n6o2f0v5ATqeHP5XIFMNF-yXHKTOwMNzMQvtZJZCNb7BbIcDOAm8pQgT6xjqpQuzuuZkDY5_N1-rU_pipg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=rXsWVjAqMHLKaD4FCGve-LTaTkiHAO4laKpvT-cnta1Hn8pS_oXpqjV7HTI5Hp_L9b-ooKqJ1UC7LU10RRah2zGv4C_NauZ7GSNvdy66_IGlb8Cf_P5wWV_2rQqXL9iADABmd9xQPLClyJ-hZIcyWLYBV0Q5jDJ9VWuPzay8gfBb2vV1vgakBXyxXWvXA7luHAUgFTwq1nJEYZBHNnuMwMUESIL_t5glkYrjZvQEtyG7WE2_ml4y2L3BxUMqZTC3q0L0n6o2f0v5ATqeHP5XIFMNF-yXHKTOwMNzMQvtZJZCNb7BbIcDOAm8pQgT6xjqpQuzuuZkDY5_N1-rU_pipg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی2026
؛ جامی که اشک سه تااز بهترین و محبوب‌ترین‌بازیکنان تاریخ رو درآورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26185" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26184">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=DkZ2NQMeFG3rFowXqk27H3QCULHYXssJNdP82SJRfslUupCaxJYXe8iqlbM6z6T-WLvepPYza6V3qvnDiEBYw2_OQfwjeYp6f7sLNE2GyRuNalQopMQZ3BNXWxdOglJRk1P2n1mMX2tFGGKLGtfXJrPUZarOUpaNKfo0g3O8LDUTWRyZp-Sex4pgrG5uaYEKvBTEb2mOz72peWA67-GpnLqLfeJtZD3u5fQyvLv0WzV_ItDAzrp6tASNXI5jzBvgMwiSQPqzLOl06PfWfWrW-97zAI1qjn16rjckatMaA9tS5K5iGVgkyW56Shqaamw11E4wmKeEbsG-pVnm0ld4bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=DkZ2NQMeFG3rFowXqk27H3QCULHYXssJNdP82SJRfslUupCaxJYXe8iqlbM6z6T-WLvepPYza6V3qvnDiEBYw2_OQfwjeYp6f7sLNE2GyRuNalQopMQZ3BNXWxdOglJRk1P2n1mMX2tFGGKLGtfXJrPUZarOUpaNKfo0g3O8LDUTWRyZp-Sex4pgrG5uaYEKvBTEb2mOz72peWA67-GpnLqLfeJtZD3u5fQyvLv0WzV_ItDAzrp6tASNXI5jzBvgMwiSQPqzLOl06PfWfWrW-97zAI1qjn16rjckatMaA9tS5K5iGVgkyW56Shqaamw11E4wmKeEbsG-pVnm0ld4bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های تامل‌انگیزومعنادار ایمان صفا بازیگر سینما درباره‌شرافت‌دربرنامه‌شب گذشته‌ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26184" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26182">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDzAX7hIArGwA_3ZC7YgZHPJGgDv0DrCY074MpSYC57D6mQ5gY_u8hDfrhKEfuraZGMaaa5dlVdLvQ3RU5ctXGPuFWvmQewBfbsU_krCKvDvvnREqsca340ovH9DWjgaTiS_FdRibzJ9L9y--xMqd5xHyIa5m8tz56JPv1SHMg7dwf8SqFzuuGKlg8LnCN8oJDQ8EtDD0za_D1rakTjgPW-vgrtqkZWWoD2c_KsHnj4xEbtvoe2BEdlTgkVVbPC13jDIjPQIpY5MIWTFuv-o189Th9iSC0vqEO3YfYyebEXpIOvGcbgTZOf2BG6U8ewgdD6Z5Rg-OrfLsQHHOQjN3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26182" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
